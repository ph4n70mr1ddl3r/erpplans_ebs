#!/usr/bin/env python3
"""Generate BPMN 2.0 models from the erpplans workflow markdown corpus.

Reads every PA-*.md process-area file under 01-model-company/workflows/VS-*/,
parses each workflow block (## W<id>. <Name> — including ###/#### sub-workflow
blocks such as W5A), and emits one valid BPMN 2.0 XML file per process area
into bpmn/VS-<slug>/PA-<slug>.bpmn, with one <process> per workflow.

Conversion rules (documented in bpmn/README.md):
  * Trigger                    -> labeled start event (name truncated)
  * Steps table rows           -> sequential tasks, joined by sequence flows
  * Role (R) contains "System" or Duration "Automated" -> serviceTask, else userTask
  * Role (R)                   -> lane per distinct responsible role (first
                                  role when compound "A / B"), in first-seen order
  * Activity full text + R/A/Duration -> task documentation (activity name
                                  = bold lead phrase, else first words, truncated)
  * Field table (Frequency, Volume, Owner, Participants, ...) -> process documentation
  * Controls section           -> text annotation associated with the start event
  * Diagram Interchange (BPMNDiagram/BPMNPlane/shapes/edges) generated for
    every element so the files open directly in any BPMN 2.0 modeler.

Modes:
  * default        — regenerate bpmn/ in place (idempotent, byte-identical on
                     an unchanged corpus); every file re-validated after write.
  * --check        — re-derive every file in memory and byte-compare against
                     the shipped tree WITHOUT writing (added by the 2026-09-16
                     forty-seventh-wave consistency review; exit 1 on any
                     drift, missing file, or shipped file with no PA source).
                     Wired into validate-repo.sh Check 71 so a PA edit shipped
                     without regeneration — invisible to structural validation
                     and to the documentation/start/annotation content mirror
                     wherever only task names, lanes or wiring move — now fails
                     the validator (the seventeenth-wave stale-PA-133 class,
                     closed for the remaining surfaces).

Validation (built in): every generated file is re-parsed and all internal
references (sequenceFlow/association source/target, lane flowNodeRef, DI
bpmnElement) are checked to resolve, and every node's incoming/outgoing
wiring is checked to mirror the sequence flows exactly. Since the
2026-09-05 seventh-wave consistency review the structural invariants its
independent deep validation probed are enforced here too: exactly one
start and one end event per process; every flow node covered by >= 1 lane
with lane refs staying inside their own process; exactly one
BPMNDiagram/BPMNPlane per process (plane ref = the process id); a DI shape
for every node/lane/annotation and an edge for every flow/association;
positive dc:Bounds and >= 1 waypoint per edge; and no unreplaced
PLACEHOLDER_ residue. Exit code 1 on any failure.
"""

import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "01-model-company" / "workflows"
OUT = REPO / "bpmn"

WF_HEADER = re.compile(r"^(#{2,4}) (W\d+[A-Za-z]?)\. (.+?)\s*$")
FIELD_ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$")
STEPS_HEADER = re.compile(
    r"^\|\s*#\s*\|\s*Activity\s*\|\s*Role \(R\)\s*\|\s*Role \(A\)\s*\|\s*(?:Duration|Frequency|Latency)\s*\|\s*$",
    re.IGNORECASE,
)
CTL_TOKEN = re.compile(r"CTL-\d+")

ESC_PIPE = "\x00"

MAX_NAME = 80
MAX_ANNOTATION = 900


# ---------------------------------------------------------------- parsing

def strip_md(text: str) -> str:
    text = text.replace(ESC_PIPE, "|")
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def step_name(activity: str) -> str:
    """Short display name: bold lead phrase if present, else leading words."""
    plain = strip_md(activity)
    m = re.search(r"\*\*(.+?)\*\*", activity)
    if m:
        lead = strip_md(m.group(1)).rstrip(":.;, ")
        if lead:
            return truncate(lead, MAX_NAME)
    return truncate(plain, MAX_NAME)


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:.") + "…"


def parse_workflow_block(lines):
    """Parse one workflow block (list of lines without the header)."""
    fields = {}
    steps = []          # list of dicts: activity, r, a, duration
    sections = {}       # other ### section -> list of bullet/paragraph text
    current_section = None
    in_steps_table = False

    for raw in lines:
        line = raw.rstrip("\n")

        if STEPS_HEADER.match(line.replace("\\|", ESC_PIPE)):
            in_steps_table = True
            current_section = None
            continue
        if in_steps_table:
            stripped = line.strip().replace("\\|", ESC_PIPE)
            if stripped.startswith("|"):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                if len(cells) >= 5 and re.fullmatch(r"\d+", cells[0] or ""):
                    steps.append({
                        "activity": cells[1],
                        "r": strip_md(cells[2]) or "Unassigned",
                        "a": strip_md(cells[3]) or "—",
                        "duration": strip_md(cells[4]) or "—",
                    })
                continue  # separator / other rows inside table
            in_steps_table = False

        m = FIELD_ROW.match(line.strip())
        if m:
            fields[m.group(1).strip()] = strip_md(m.group(2))
            current_section = None
            continue

        m = re.match(r"^### (.+?)\s*$", line)
        if m:
            current_section = m.group(1)
            sections.setdefault(current_section, [])
            continue

        if current_section and line.strip():
            sections[current_section].append(line.strip())

    return {"fields": fields, "steps": steps, "sections": sections}


def parse_pa_file(path: Path):
    """Yield (wf_id, wf_name, block_dict) for every workflow in a PA file."""
    text = path.read_text(encoding="utf-8")
    workflows = []
    current = None

    def flush():
        nonlocal current
        if current is not None:
            workflows.append(current)
            current = None

    for line in text.splitlines():
        m = WF_HEADER.match(line)
        if m:
            flush()
            current = {"id": m.group(2), "name": m.group(3), "lines": []}
        elif current is not None:
            if re.match(r"^## (?!#)", line) or line.startswith("*Workflow Count"):
                flush()
            else:
                current["lines"].append(line)
    flush()
    for wf in workflows:
        wf.update(parse_workflow_block(wf.pop("lines")))
    return workflows


# ---------------------------------------------------------------- BPMN emission

def esc(s: str) -> str:
    return html.escape(s, quote=True)


def lane_of(role: str) -> str:
    part = re.split(r"\s*/\s*", role)[0]
    part = re.sub(r"\s*\(.*?\)\s*", " ", part).strip()
    return truncate(part or "Unassigned", 48)


def is_automated(step) -> bool:
    if step["duration"].lower() == "automated":
        return True
    return "system" in step["r"].lower() or "system" in step["a"].lower()


class Ids:
    """Per-process id factory; every id prefixed with the workflow id."""
    def __init__(self, wf_id: str):
        self.wf = re.sub(r"[^A-Za-z0-9_.-]", "_", wf_id)
        self.n = 0

    def next(self, kind: str) -> str:
        self.n += 1
        return f"{self.wf}_{kind}{self.n}"


def build_process(wf) -> str:
    """Return the <bpmn:process> + <bpmndi:BPMNDiagram> XML for one workflow."""
    ids = Ids(wf["id"])
    p_id = f"W_{ids.wf}"

    # -- lanes: first-seen order of responsible roles ----------------------
    lanes = []          # (lane_id, lane_name, [node_ids])
    lane_index = {}
    for step in wf["steps"]:
        ln = lane_of(step["r"])
        if ln not in lane_index:
            lane_id = ids.next("Lane")
            lane_index[ln] = lane_id
            lanes.append((lane_id, ln, []))
    if not lanes:  # no steps parsed -> fallback lane
        lane_index["Unassigned"] = ids.next("Lane")
        lanes.append((lane_index["Unassigned"], "Unassigned", []))

    # -- semantic elements -------------------------------------------------
    proc_doc_lines = []
    for key in ("Trigger", "Frequency", "Volume", "Owner", "Participants"):
        if key in wf["fields"]:
            proc_doc_lines.append(f"{key}: {wf['fields'][key]}")
    proc_doc_lines.append(f"Source: workflow {wf['id']} — {wf['name']}")
    proc_doc = esc("\n".join(proc_doc_lines))

    out = []
    out.append(
        f'    <bpmn:process id="{p_id}" name="{esc(wf["id"] + ". " + wf["name"])}" isExecutable="false">'
    )
    out.append(f"      <bpmn:documentation>{proc_doc}</bpmn:documentation>")

    out.append(f'      <bpmn:laneSet id="{ids.next("LaneSet")}">')
    for lane_id, lane_name, _ in lanes:
        out.append(
            f'        <bpmn:lane id="{lane_id}" name="{esc(lane_name)}">'
        )
        out.append(f"          <bpmn:documentation>Lane for responsible role: {esc(lane_name)}</bpmn:documentation>")
        out.append("        </bpmn:lane>")
    out.append("      </bpmn:laneSet>")

    start_id = ids.next("Start")
    start_name = truncate(strip_md(wf["fields"].get("Trigger", "Trigger")), 90)
    out.append(
        f'      <bpmn:startEvent id="{start_id}" name="{esc(start_name)}">'
    )
    out.append("        <bpmn:outgoing>PLACEHOLDER_OUT_0</bpmn:outgoing>")
    out.append("      </bpmn:startEvent>")

    task_ids = []
    for i, step in enumerate(wf["steps"]):
        tid = ids.next("Task")
        task_ids.append(tid)
        name = step_name(step["activity"])
        doc = "\n".join([
            f"Step {i + 1}: {strip_md(step['activity'])}",
            f"Responsible (R): {step['r']}",
            f"Accountable (A): {step['a']}",
            f"Duration: {step['duration']}",
        ])
        tag = "serviceTask" if is_automated(step) else "userTask"
        out.append(
            f'      <bpmn:{tag} id="{tid}" name="{esc(name)}">'
        )
        out.append(f"        <bpmn:documentation>{esc(doc)}</bpmn:documentation>")
        out.append("        <bpmn:incoming>PLACEHOLDER_IN_%d</bpmn:incoming>" % (i + 1))
        out.append(f"        <bpmn:outgoing>PLACEHOLDER_OUT_{i + 1}</bpmn:outgoing>")
        out.append(f"      </bpmn:{tag}>")

    end_id = ids.next("End")
    out.append(f'      <bpmn:endEvent id="{end_id}" name="Complete">')
    out.append(f"        <bpmn:incoming>PLACEHOLDER_IN_{len(task_ids) + 1}</bpmn:incoming>")
    out.append("      </bpmn:endEvent>")

    controls_text = "Controls: " + " | ".join(
        strip_md(b) for b in wf["sections"].get("Controls", [])
    ) if wf["sections"].get("Controls") else "Controls: (none recorded)"
    if wf["fields"].get("Owner"):
        controls_text += f"\nOwner: {wf['fields']['Owner']}"
    anno_id = ids.next("Annotation")
    out.append(f'      <bpmn:textAnnotation id="{anno_id}">')
    out.append(
        f"        <bpmn:text>{esc(truncate(controls_text, MAX_ANNOTATION))}</bpmn:text>"
    )
    out.append("      </bpmn:textAnnotation>")
    assoc_id = ids.next("Assoc")
    out.append(
        f'      <bpmn:association id="{assoc_id}" sourceRef="{anno_id}" targetRef="{start_id}" '
        'associationDirection="None" />'
    )

    flow_ids = []
    chain = [start_id] + task_ids + [end_id]
    for i in range(len(chain) - 1):
        fid = ids.next("Flow")
        flow_ids.append(fid)
        out.append(
            f'      <bpmn:sequenceFlow id="{fid}" sourceRef="{chain[i]}" targetRef="{chain[i + 1]}" />'
        )

    # resolve placeholders. Flow k joins chain[k] -> chain[k + 1], so it is the
    # outgoing ref of chain[k] and the incoming ref of chain[k + 1]. Replace
    # longest placeholders first: ascending replacement would let
    # PLACEHOLDER_OUT_1/IN_1 clobber the prefixes of OUT_10+/IN_10+ and leave
    # digit residue pointing at flows that do not exist.
    repl: dict[str, str] = {}
    for k, fid in enumerate(flow_ids):
        repl[f"PLACEHOLDER_OUT_{k}"] = fid
        repl[f"PLACEHOLDER_IN_{k + 1}"] = fid
    body = "\n".join(out)
    for ph in sorted(repl, key=len, reverse=True):
        body = body.replace(ph, repl[ph])
    if "PLACEHOLDER" in body:
        raise RuntimeError(f"unresolved wiring placeholder in process {p_id}")
    body += "\n    </bpmn:process>"

    # -- assign lane flowNodeRefs -----------------------------------------
    lane_members = {lane_id: [] for lane_id, _, _ in lanes}
    for step, tid in zip(wf["steps"], task_ids):
        lane_members[lane_index[lane_of(step["r"])]].append(tid)
    if task_ids:
        lane_members[lanes[0][0]].append(start_id)
        lane_members[lanes[-1][0]].append(end_id)
    else:
        lane_members[lanes[0][0]] += [start_id, end_id]
    for lane_id, _, _ in lanes:
        refs = "\n".join(
            f"        <bpmn:flowNodeRef>{n}</bpmn:flowNodeRef>"
            for n in lane_members[lane_id]
        )
        block = (
            f'        <bpmn:lane id="{lane_id}" name="{esc(dict((l, n) for l, n, _ in lanes)[lane_id])}">\n'
            + (refs + "\n" if refs else "")
            + "        </bpmn:lane>"
        )
        body = re.sub(
            r'        <bpmn:lane id="%s" name="[^"]*">.*?</bpmn:lane>' % re.escape(lane_id),
            lambda m: block, body, count=1, flags=re.S,
        )

    # -- diagram interchange -----------------------------------------------
    out.append(build_di(wf, ids, start_id, end_id, task_ids, anno_id, assoc_id,
                        flow_ids, lanes, lane_members))
    return body + "\n" + out[-1]


def build_di(wf, ids, start_id, end_id, task_ids, anno_id, assoc_id,
             flow_ids, lanes, lane_members) -> str:
    EV, TS_W, TS_H, LANE_H, X0, Y0, STEP_X = 36, 180, 80, 170, 160, 80, 210
    shapes, edges = [], []

    task_pos = {}
    lane_y = {}
    width = X0 + 240 + len(task_ids) * STEP_X + 120
    for li, (lane_id, _, _) in enumerate(lanes):
        lane_y[lane_id] = Y0 + li * LANE_H
        shapes.append(
            f'        <bpmndi:BPMNShape id="{lane_id}_di" bpmnElement="{lane_id}" isHorizontal="true">'
            f'<dc:Bounds x="{X0}" y="{lane_y[lane_id]}" width="{width - X0 - 40}" height="{LANE_H}" />'
            f"</bpmndi:BPMNShape>"
        )
    for i, tid in enumerate(task_ids):
        lane_id = next(l for l, _, members in
                       ((l, n, lane_members[l]) for l, n, _ in lanes) if tid in members)
        x = X0 + 240 + i * STEP_X
        y = lane_y[lane_id] + (LANE_H - TS_H) // 2
        task_pos[tid] = (x, y)
        shapes.append(
            f'        <bpmndi:BPMNShape id="{tid}_di" bpmnElement="{tid}">'
            f"<dc:Bounds x=\"{x}\" y=\"{y}\" width=\"{TS_W}\" height=\"{TS_H}\" /></bpmndi:BPMNShape>"
        )

    # start event in first lane, left of first task; end in last lane
    first_lane, last_lane = lanes[0][0], lanes[-1][0]
    sx = X0 + 130
    sy = lane_y[first_lane] + (LANE_H - EV) // 2
    shapes.append(
        f'        <bpmndi:BPMNShape id="{start_id}_di" bpmnElement="{start_id}">'
        f'<dc:Bounds x="{sx}" y="{sy}" width="{EV}" height="{EV}" /></bpmndi:BPMNShape>'
    )
    ex = X0 + 240 + len(task_ids) * STEP_X + 20
    ey = lane_y[last_lane] + (LANE_H - EV) // 2
    shapes.append(
        f'        <bpmndi:BPMNShape id="{end_id}_di" bpmnElement="{end_id}">'
        f'<dc:Bounds x="{ex}" y="{ey}" width="{EV}" height="{EV}" /></bpmndi:BPMNShape>'
    )

    ay = Y0 + len(lanes) * LANE_H + 40
    a_text = truncate("Controls: " + " | ".join(
        strip_md(b) for b in wf["sections"].get("Controls", [])
    ) if wf["sections"].get("Controls") else "Controls: (none recorded)", 400)
    a_h = max(60, 14 * (len(a_text) // 60 + 1) + 16)
    shapes.append(
        f'        <bpmndi:BPMNShape id="{anno_id}_di" bpmnElement="{anno_id}">'
        f'<dc:Bounds x="{X0}" y="{ay}" width="360" height="{a_h}" /></bpmndi:BPMNShape>'
    )

    def edge(eid, src, tgt, pts):
        (x1, y1), (x2, y2) = pts
        edges.append(
            f'        <bpmndi:BPMNEdge id="{eid}_di" bpmnElement="{eid}">'
            f'<di:waypoint x="{x1}" y="{y1}" /><di:waypoint x="{x2}" y="{y2}" /></bpmndi:BPMNEdge>'
        )

    chain = [start_id] + task_ids + [end_id]
    centers = {start_id: (sx + EV, sy + EV // 2), end_id: (ex, ey + EV // 2)}
    for tid, (x, y) in task_pos.items():
        centers[tid] = (x + TS_W // 2, y + TS_H // 2)
    for i, fid in enumerate(flow_ids):
        s, t = chain[i], chain[i + 1]
        if s == start_id:
            p1 = (sx + EV, sy + EV // 2)
        else:
            x, y = task_pos[s]
            p1 = (x + TS_W, y + TS_H // 2)
        if t == end_id:
            p2 = (ex, ey + EV // 2)
        else:
            x, y = task_pos[t]
            p2 = (x, y + TS_H // 2)
        edge(fid, s, t, (p1, p2))
    edge(assoc_id, anno_id, start_id, ((X0 + 180, ay), (sx + EV // 2, sy + EV)))

    return (
        f'    <bpmndi:BPMNDiagram id="{ids.wf}_diag">\n'
        f'      <bpmndi:BPMNPlane id="{ids.wf}_plane" bpmnElement="W_{ids.wf}">\n'
        + "\n".join(shapes + edges)
        + "\n      </bpmndi:BPMNPlane>\n    </bpmndi:BPMNDiagram>"
    )


DEFINITIONS_TMPL = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
    'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
    'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
    'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
    'id="Definitions_{def_id}" '
    'targetNamespace="https://erpplans.local/bpmn" '
    'exporter="erpplans generate-bpmn.py" exporterVersion="1.0">\n{procs}\n</bpmn:definitions>\n'
)


def render_file(pa_path: Path) -> tuple[str, int]:
    """Render a PA file's BPMN XML in memory. Returns (xml_text, workflow_count).

    Split from convert_file by the 2026-09-16 forty-seventh-wave consistency review
    so --check can byte-compare the shipped tree against a fresh re-derivation
    without writing (the same shipped-currency guarantee generate-role-coverage.py
    --check has given the role-coverage matrix since the thirtieth wave).
    """
    workflows = parse_pa_file(pa_path)
    procs = []
    for wf in workflows:
        if not wf["steps"]:  # guarantee start->task->end even with no table
            wf["steps"] = [{
                "activity": f"Execute {wf['name']}",
                "r": wf["fields"].get("Owner", "Unassigned"),
                "a": wf["fields"].get("Owner", "Unassigned"),
                "duration": "—",
            }]
        procs.append(build_process(wf))
    def_id = re.sub(r"[^A-Za-z0-9_.-]", "_", pa_path.stem)
    xml = DEFINITIONS_TMPL.format(def_id=def_id, procs="\n".join(procs))
    return xml, len(workflows)


def convert_file(pa_path: Path, out_path: Path) -> int:
    xml, n = render_file(pa_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(xml, encoding="utf-8")
    return n


# ---------------------------------------------------------------- validation

NS = {
    "bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
    "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
}


def validate_file(path: Path) -> str | None:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return f"XML parse error: {e}"
    ids = set()
    for el in root.iter():
        if "id" in el.attrib:
            ids.add(el.attrib["id"])
    for tag, attrs in (
        ("sequenceFlow", ("sourceRef", "targetRef")),
        ("association", ("sourceRef", "targetRef")),
        ("lane", ()),
    ):
        for el in root.iter(f"{{http://www.omg.org/spec/BPMN/20100524/MODEL}}{tag}"):
            for a in attrs:
                if el.attrib.get(a) and el.attrib[a] not in ids:
                    return f"{tag} {el.attrib.get('id')} broken {a}={el.attrib[a]}"
    for el in root.iter(f"{{{NS['bpmn']}}}flowNodeRef"):
        if (el.text or "").strip() not in ids:
            return f"lane flowNodeRef broken: {el.text}"
    # incoming/outgoing wiring must mirror the sequence flows exactly
    flows = {
        el.attrib["id"]: (el.attrib.get("sourceRef"), el.attrib.get("targetRef"))
        for el in root.iter(f"{{{NS['bpmn']}}}sequenceFlow")
    }
    nodes = {
        el.attrib["id"]: el
        for tag in ("startEvent", "endEvent", "userTask", "serviceTask")
        for el in root.iter(f"{{{NS['bpmn']}}}{tag}")
    }
    wire = {nid: ([], []) for nid in nodes}  # node -> (incoming, outgoing) flow ids
    for fid, (src, tgt) in flows.items():
        if src in wire:
            wire[src][1].append(fid)
        if tgt in wire:
            wire[tgt][0].append(fid)
    for nid, el in nodes.items():
        outs = [(o.text or "").strip() for o in el.findall(f"{{{NS['bpmn']}}}outgoing")]
        ins = [(i.text or "").strip() for i in el.findall(f"{{{NS['bpmn']}}}incoming")]
        for ref in outs + ins:
            if ref not in flows:
                return f"{nid}: wiring ref {ref} resolves to no sequenceFlow"
        if sorted(outs) != sorted(wire[nid][1]):
            return f"{nid}: outgoing {sorted(outs)} != flows leaving it {sorted(wire[nid][1])}"
        if sorted(ins) != sorted(wire[nid][0]):
            return f"{nid}: incoming {sorted(ins)} != flows entering it {sorted(wire[nid][0])}"
    procs = list(root.iter(f"{{{NS['bpmn']}}}process"))
    if not procs:
        return "no process elements"
    proc_ids = {p.attrib["id"] for p in procs}
    # exactly one BPMNDiagram/BPMNPlane per process, each plane ref = a process id
    diags = list(root.iter(f"{{{NS['bpmndi']}}}BPMNDiagram"))
    planes = list(root.iter(f"{{{NS['bpmndi']}}}BPMNPlane"))
    if len(diags) != len(procs) or len(planes) != len(procs):
        return (f"{len(procs)} processes but {len(diags)} diagrams / "
                f"{len(planes)} planes (want 1:1:1)")
    for pl in planes:
        if pl.attrib.get("bpmnElement") not in proc_ids:
            return (f"BPMNPlane {pl.attrib.get('id')} bpmnElement "
                    f"{pl.attrib.get('bpmnElement')} is not a process id")
    # structural invariants: start/end cardinality, lane coverage, DI coverage
    shapes = {el.attrib.get("bpmnElement") for el in root.iter(f"{{{NS['bpmndi']}}}BPMNShape")}
    edges = {el.attrib.get("bpmnElement") for el in root.iter(f"{{{NS['bpmndi']}}}BPMNEdge")}
    node_tags = ("startEvent", "endEvent", "userTask", "serviceTask")
    for p in procs:
        pn = [el for t in node_tags for el in p.iter(f"{{{NS['bpmn']}}}{t}")]
        if sum(1 for el in pn if el.tag.endswith("startEvent")) != 1:
            return f"{p.attrib['id']}: process must carry exactly one startEvent"
        if sum(1 for el in pn if el.tag.endswith("endEvent")) != 1:
            return f"{p.attrib['id']}: process must carry exactly one endEvent"
        node_ids = {el.attrib["id"] for el in pn}
        covered = set()
        for lane in p.iter(f"{{{NS['bpmn']}}}lane"):
            for ref in lane.iter(f"{{{NS['bpmn']}}}flowNodeRef"):
                rid = (ref.text or "").strip()
                if rid not in node_ids:
                    return f"{p.attrib['id']}: lane flowNodeRef {rid} is not a node of this process"
                covered.add(rid)
        bare = node_ids - covered
        if bare:
            return f"{p.attrib['id']}: nodes not covered by any lane: {sorted(bare)[:3]}"
        need_shapes = (node_ids
                       | {el.attrib["id"] for el in p.iter(f"{{{NS['bpmn']}}}lane")}
                       | {el.attrib["id"] for el in p.iter(f"{{{NS['bpmn']}}}textAnnotation")})
        missing = need_shapes - shapes
        if missing:
            return f"{p.attrib['id']}: no BPMNShape for {sorted(missing)[:3]}"
        need_edges = ({el.attrib["id"] for el in p.iter(f"{{{NS['bpmn']}}}sequenceFlow")}
                      | {el.attrib["id"] for el in p.iter(f"{{{NS['bpmn']}}}association")})
        missing = need_edges - edges
        if missing:
            return f"{p.attrib['id']}: no BPMNEdge for {sorted(missing)[:3]}"
    for el in root.iter(f"{{{NS['bpmndi']}}}BPMNShape"):
        bounds = [c for c in el if c.tag.endswith("}Bounds")]
        if len(bounds) != 1 or float(bounds[0].attrib["width"]) <= 0 or float(bounds[0].attrib["height"]) <= 0:
            return f"BPMNShape {el.attrib.get('id')}: missing/invalid dc:Bounds"
    for el in root.iter(f"{{{NS['bpmndi']}}}BPMNEdge"):
        if not [c for c in el if c.tag.endswith("}waypoint")]:
            return f"BPMNEdge {el.attrib.get('id')}: no waypoint"
    if "PLACEHOLDER_" in path.read_text(encoding="utf-8"):
        return "unreplaced PLACEHOLDER_ residue in output"
    return None


# ---------------------------------------------------------------- main

def main() -> int:
    check = "--check" in sys.argv[1:]
    pa_files = sorted(SRC.glob("VS-*/PA-*.md"))
    total_wf = 0
    total_tasks = 0
    failures = []
    if check:
        # Forty-seventh-wave shipped-currency arm (2026-09-16): byte-compare the
        # shipped tree against a fresh in-memory re-derivation. Nothing is written.
        # Catches: a PA edit shipped without regeneration (task names, lane names,
        # wiring and step-derived content are invisible to Check 71's structural
        # validation and its documentation/start/annotation content mirror), a
        # hand-edit of a generated file, a partial regeneration, and a shipped file
        # with no PA counterpart. The markdown remains the source of truth: drift is
        # resolved by regenerating, never by hand-editing the tree.
        shipped = {p.relative_to(OUT).as_posix() for p in OUT.rglob("*.bpmn")}
        derived = {p.relative_to(SRC).with_suffix(".bpmn").as_posix() for p in pa_files}
        n_drift = 0
        for pa in pa_files:
            rel = pa.relative_to(SRC).with_suffix(".bpmn")
            out_path = OUT / rel
            xml, n = render_file(pa)
            total_wf += n
            if not out_path.exists():
                print(f"DRIFT|{rel.as_posix()}  missing from the shipped tree (regenerate)")
                n_drift += 1
                continue
            if out_path.read_text(encoding="utf-8") != xml:
                print(f"DRIFT|{rel.as_posix()}  stale vs its markdown source (regenerate)")
                n_drift += 1
        for rel in sorted(shipped - derived):
            print(f"DRIFT|{rel}  shipped but no PA markdown derives it (delete or restore the PA)")
            n_drift += 1
        print(
            f"\n=== --check: {len(pa_files)} PA files, {total_wf} processes re-derived, "
            f"{len(shipped)} shipped files, {n_drift} drifted ==="
        )
        if n_drift:
            print("SHIPPED TREE IS STALE — regenerate (python3 07-methodology/generate-bpmn.py); "
                  "the markdown is the source of truth, never hand-edit bpmn/.")
            return 1
        print("Shipped bpmn/ tree is byte-identical to the generator's re-derivation from "
              "the markdown corpus.")
        return 0
    for pa in pa_files:
        rel = pa.relative_to(SRC).with_suffix(".bpmn")
        out_path = OUT / rel
        n = convert_file(pa, out_path)
        err = validate_file(out_path)
        if err:
            failures.append((out_path, err))
        total_wf += n
        total_tasks += len(re.findall(r"<bpmn:(?:user|service)Task id=", out_path.read_text(encoding='utf-8')))
        print(f"{rel}  workflows={n}")
    print(f"\n=== {len(pa_files)} BPMN files, {total_wf} processes, {total_tasks} tasks ===")
    if failures:
        print("VALIDATION FAILURES:")
        for p, e in failures:
            print(f"  {p}: {e}")
        return 1
    print("All generated files validate (well-formed XML, all refs resolve, wiring mirrors the "
          "sequence flows, structural invariants hold: 1 start/1 end per process, full lane "
          "coverage, 1:1 BPMNDiagram/BPMNPlane per process, complete DI shapes/edges, "
          "no placeholder residue).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
