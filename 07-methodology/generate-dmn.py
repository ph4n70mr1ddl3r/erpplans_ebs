#!/usr/bin/env python3
"""Generate DMN 1.3 decision models from the erpplans workflow markdown corpus.

Companion to generate-bpmn.py. Reads every PA-*.md process-area file under
01-model-company/workflows/VS-*/ and extracts the two kinds of content that
already exist as explicit, structured rules in the source:

  1. Rule-shaped markdown tables — a table whose header has at least one
     criteria-like column (severity, tier, amount, scenario, ...) and at
     least one outcome-like column (action, approval, sla, escalation, ...).
     Each row becomes one DMN rule; each criteria column an input, each
     outcome column an output.

  2. Tiered money-threshold authorization rules embedded in step prose —
     the recurring "(a) <= PHP X: Role A; (b) PHP X–Y: Role B; (c) > PHP Y:
     Role C" pattern (also "Role approves ... up to PHP X; ... PHP X–Y; ...
     > PHP Y" and "> PHP X -> Role" forms). Each tier set becomes a decision
     table over the amount with the approver(s) as output.

Everything else (unstructured conditional prose, percent tiers, single-bound
rules without a complementary tier) is NOT extracted — it is counted and
listed as deferred rather than faked into tables. The markdown remains the
source of truth; dmn/ is a projection of it, exactly like bpmn/.

Output: one DMN 1.3 XML file per process area that yields >= 1 decision,
at dmn/VS-<slug>/PA-<slug>.dmn (mirroring the bpmn/ tree), with DMNDI shape
layout so the files open in dmn-js / Camunda Modeler.

Validation (built in): every generated file is re-parsed; ids are checked
unique; every decisionTable has >= 1 input/output/rule; every rule's
entry counts match the table's; no entry text is empty; all DMNShape
dmnElementRefs resolve and every decision carries a DMNShape (so it
renders in a DRD; added by the 2026-09-05 seventh-wave consistency
review); numeric band inputs are verified pairwise-disjoint (a failing
band set is demoted to hitPolicy "Collect", never silently published as
Unique). Exit code 1 on any failure.

Modes: default regenerates dmn/ in place (idempotent, byte-identical on an
unchanged corpus); --check re-derives every file in memory and byte-compares
against the shipped tree WITHOUT writing (added by the 2026-09-16
forty-seventh-wave consistency review, exit 1 on drift/missing/extra; wired
into validate-repo.sh Check 71).
"""

import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "01-model-company" / "workflows"
OUT = REPO / "dmn"

MAX_NAME = 70
MAX_DESC = 700

# ---------------------------------------------------------------- patterns

# rule-shaped markdown table header: needs a criteria-like and an outcome-like column
OUT_COL = re.compile(
    r"(action|approval|approver|authoriz\w*|decision|escalation|sla|impact|result|"
    r"next step|response|treatment|rating|disposition|override|path|policy|plan|required|authority)",
    re.I,
)
CRIT_COL = re.compile(
    r"(condition|scenario|severit|tier|level|amount|limit|threshold|categ\w+|type|status|"
    r"priority|score|risk|age|days|qty|value|range|volume|frequency|trigger|credit limit)",
    re.I,
)
NUMERIC_CELL = re.compile(r"^\s*[\d.,]+\s*%?\s*$")

AMT = r"(?:PHP|₱)\s*([\d,.]+)\s*(K|M|million|thousand)?"
TIER_MARK = re.compile(r"\(([a-e])\)")
VERB = re.compile(r"\b(approv\w+|authoriz\w+|escalat\w+|endorse\w+|sign(?:-| )?off)\b", re.I)
ROLE_WORD = re.compile(
    r"(manager|head|officer|director|president|supervisor|cfo|ceo|coo|cio|cto|controller|"
    r"treasurer|committee|board|analyst|buyer|clerk|coordinator|auditor|accountant|engineer|"
    r"partner|admin|lead|chef|pharmacist|staff|planner|chair|suite|sr\.)",
    re.I,
)
CSUITE = re.compile(r"^(?:vp|evp|svp|avp|chief|ceo|coo|cfo|cio|cto|chair(?:man)?)\b", re.I)
ROLE_PHRASE = re.compile(
    r"[A-Z][A-Za-z&./-]*(?:(?:\s+(?:of|the|and|&|for|per|Dept\.?|[A-Z][A-Za-z&./-]*))*)",
)
RANGE_DASH = r"(?:-|–|—|to)"


def unit_mult(u: str | None) -> float:
    u = (u or "").lower()
    if u in ("k", "thousand"):
        return 1_000
    if u in ("m", "million"):
        return 1_000_000
    return 1


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def strip_md(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:.") + "…"


def feel_name(title: str) -> str:
    """Sanitize a column title into a FEEL variable name (CamelCase identifier)."""
    words = re.findall(r"[A-Za-z0-9]+", title)
    if not words:
        return "Input"
    name = "".join(w[:1].upper() + w[1:] for w in words)
    if name[0].isdigit():
        name = "N" + name
    return name[:40]


def parse_amount(num: str, unit: str | None) -> float | None:
    try:
        v = float(num.replace(",", ""))
    except ValueError:
        return None
    unit = (unit or "").lower()
    if unit == "k" or unit == "thousand":
        v *= 1_000
    elif unit == "m" or unit == "million":
        v *= 1_000_000
    return v


def fmt_num(v: float) -> str:
    return str(int(v)) if float(v).is_integer() else repr(v)


# ---------------------------------------------------------------- table extraction

def extract_tables(lines):
    """Yield (heading, header_cells, rows) for every rule-shaped markdown table."""
    tables = []
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(#{1,4}) (.+?)\s*$", line)
        if m:
            heading = m.group(2)
            i += 1
            continue
        if (
            i + 1 < len(lines)
            and re.match(r"^\|.+\|\s*$", line)
            and re.match(r"^\|[-\s:|]+\|\s*$", lines[i + 1])
            and "---" in lines[i + 1]
        ):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                if len(cells) == len(header):
                    rows.append(cells)
                j += 1
            ins = [k for k, c in enumerate(header) if CRIT_COL.search(c)]
            outs = [k for k, c in enumerate(header) if OUT_COL.search(c) and k not in ins]
            # columns matching neither pattern are kept as extra outputs (never dropped)
            outs += [k for k in range(len(header)) if k not in ins and k not in outs]
            if ins and outs and len(rows) >= 2:
                tables.append((heading, header, ins, outs, rows))
            i = j
            continue
        i += 1
    return tables


def table_decision(dec_id, heading, header, ins, outs, rows, provenance):
    """Build a decision dict from a rule-shaped table, or None if unusable."""
    in_cols = []
    for k in ins:
        col_vals = [strip_md(r[k]) for r in rows]
        numeric = all(NUMERIC_CELL.match(v) for v in col_vals if v)
        in_cols.append({"label": header[k], "feel": feel_name(header[k]),
                        "type": "number" if numeric else "string", "values": col_vals})
    out_cols = [{"label": header[k], "name": feel_name(header[k]), "values": [strip_md(r[k]) for r in rows]}
                for k in outs]
    # uniqueness of the full input tuple decides hit policy U vs C
    tuples = list(zip(*[c["values"] for c in in_cols]))
    tuples = [tuple(re.sub(r"\s+", " ", str(x)).strip().lower() for x in t) for t in tuples]
    hit = "U" if len(set(tuples)) == len(tuples) else "C"
    rules = []
    for ri, r in enumerate(rows):
        in_entries = []
        for col in in_cols:
            v = col["values"][ri]
            if col["type"] == "number":
                n = parse_amount(v.replace("%", ""), None)
                in_entries.append(fmt_num(n) if n is not None else "-")
            else:
                in_entries.append('"' + v.replace('"', "'") + '"')
        out_entries = ['"' + oc["values"][ri].replace('"', "'") + '"' for oc in out_cols]
        rules.append({"in": in_entries, "out": out_entries})
    name = truncate(f"{strip_md(heading)} — {header[ins[0]]}", MAX_NAME)
    return {
        "id": dec_id, "name": name, "hit": hit,
        "inputs": in_cols, "outputs": out_cols, "rules": rules,
        "description": provenance + "\nSource table: " + " | ".join(header),
    }


# ---------------------------------------------------------------- prose tier extraction

def parse_band(seg: str):
    """Parse the numeric band of one tier segment, anchored on its first amount.
    Returns (lo, lo_inc, hi, hi_inc) with None = unbounded, or None."""
    m1 = re.search(AMT, seg, re.I)
    if not m1:
        return None
    v1 = parse_amount(m1.group(1), m1.group(2))
    if v1 is None:
        return None
    pre = seg[max(0, m1.start() - 16): m1.start()].lower()
    post = seg[m1.end(): m1.end() + 30]
    lo = hi = None
    lo_inc = hi_inc = True

    # range: "PHP X-Y" / "PHP X to PHP Y" (unit-less X inherits Y's scale)
    m2 = re.match(r"\s*" + RANGE_DASH + r"\s*(?:php\s*)?([\d,.]+)\s*(k|m|million|thousand)?", post, re.I)
    if m2:
        v2 = parse_amount(m2.group(1), m2.group(2))
        if v2 is not None and v2 > v1:
            if m1.group(2) is None and m2.group(2):
                v1 *= unit_mult(m2.group(2))
            return (v1, True, v2, True)

    # operator immediately before the amount
    ops = [
        (re.search(r"(?:≤|<=)[\s:;,]*$", pre), "hi_inc"),
        (re.search(r"<\s*$", pre), "hi_exc"),
        (re.search(r"(?:≥|>=)\s*$|at least|minimum of", pre), "lo_inc"),
        (re.search(r">\s*$|above|over|more than|exceeding|beyond", pre), "lo_exc"),
        (re.search(r"below|under", pre), "hi_exc"),
        (re.search(r"up to\s*$", pre), "hi_inc"),
    ]
    matched = next((kind for rx, kind in ops if rx), None)
    if matched in ("lo_inc", "lo_exc"):
        lo, lo_inc = v1, matched == "lo_inc"
    elif matched in ("hi_inc", "hi_exc"):
        hi, hi_inc = v1, matched == "hi_inc"
    elif re.search(r"or more|and above|or above|and up", post, re.I):
        lo, lo_inc = v1, True
    else:
        hi, hi_inc = v1, True  # bare amount ("PHP 500K: Role") — bottom-tier assumption

    # compound upper bound: "> PHP X and <= PHP Y"
    if lo is not None:
        m3 = re.match(r"\s*(?:k|m|million|thousand)?\s*(?:,\s*)?and\s*(?:\(|\b)*(≤|<=|<|>=|≥)?\s*(?:php\s*)?([\d,.]+)\s*(k|m|million|thousand)?", post, re.I)
        if m3:
            v3 = parse_amount(m3.group(2), m3.group(3))
            if v3 is not None and v3 > v1:
                hi = v3
                hi_inc = m3.group(1) not in ("<",)
    return (lo, lo_inc, hi, hi_inc)


def find_roles(seg: str, near: int) -> str:
    """Role phrases near the amount mention, joined with ' + '."""
    window = seg[max(0, near - 90): near + 130]
    seen, picked = set(), []
    for m in ROLE_PHRASE.finditer(window):
        phrase = re.sub(r"\s+", " ", m.group(0)).strip(" .,;:-/")
        if len(phrase) < 3 or len(phrase) > 60:
            continue
        if not (ROLE_WORD.search(phrase) or CSUITE.match(phrase)):
            continue
        if phrase.lower() in {"php", "the", "and"}:
            continue
        if phrase.lower() not in seen:
            seen.add(phrase.lower())
            picked.append(phrase)
    if not picked:
        return ""
    return " + ".join(picked[:3])


def extract_tier_set(row_text: str):
    """Parse a tiered money-authorization rule set from one step row.
    Returns (label_hint, [(band, approver)], verbatim, note) or None.
    Every money-bearing segment must parse fully (band + approver) — a partial
    extraction would publish a wrong policy and is refused instead."""
    text = strip_md(row_text)
    if not (AMT_SEARCH := re.search(AMT, text, re.I)):
        return None
    if not VERB.search(text):
        return None

    # tier segmentation: explicit (a)/(b)/(c) markers, else semicolons, else
    # commas that precede a new bound token — then flatten internal semicolons
    # (a single marker segment often packs sub-tiers: "(c) A up to PHP 10M; B PHP 10–50M; ...")
    segments = []
    marks = list(TIER_MARK.finditer(text))
    if len(marks) >= 2:
        for k, m in enumerate(marks):
            end = marks[k + 1].start() if k + 1 < len(marks) else len(text)
            segments.append(text[m.end(): end])
    else:
        # split on ";" or on commas that precede a new bound token
        parts = re.split(r";", text)
        if len(parts) < 2:
            parts = re.split(r",\s*(?=(?:≤|<=|>=|≥|<|>)\s*(?:PHP|₱)|(?:PHP|₱)\s*[\d,.]+\s*(?:K|M|million|thousand)?\s*(?:-|–|—|to)|(?:above|over|more than|up to|at least)\s+(?:PHP|₱))", text, flags=re.I)
        segments = [p for p in parts if p.strip()]
    segments = [p for seg in segments for p in seg.split(";")]

    # A tier set is emitted only when EVERY money-bearing segment yields a band
    # and an approver — a partial extraction would publish a wrong policy.
    tiers = []
    nonmoney = 0
    for seg in segments:
        seg = seg.strip(" ;,")
        amt = re.search(AMT, seg, re.I)
        if not amt:
            nonmoney += 1
            continue
        band = parse_band(seg)
        approver = find_roles(seg, amt.start()) if band else ""
        if band is None or not approver:
            return None
        tiers.append((band, approver, seg))

    if len(tiers) < 2:
        return None
    notes = []
    if nonmoney:
        notes.append(
            f"Note: {nonmoney} non-monetary tier(s) in the source list are excluded from "
            "this amount-based table."
        )

    # numeric disjointness over present bounds
    typed = []
    for band, approver, seg in tiers:
        lo, lo_inc, hi, hi_inc = band
        lo_v = lo if lo is not None else float("-inf")
        hi_v = hi if hi is not None else float("inf")
        typed.append([lo_v, lo_inc, hi_v, hi_inc, approver, seg])
    typed.sort(key=lambda t: (t[0], t[2]))
    # ladder normalization: "<= X" followed by "PHP X-Y" shares the boundary
    # point; standard tier-ladder reading assigns it to the lower tier
    for a, b in zip(typed, typed[1:]):
        if a[2] == b[0] and a[3] and b[1]:
            b[1] = False
    # escalating open-lower ladder: "> A -> Role1; > B -> Role2" with strictly
    # increasing A < B < ... is the corpus's approval-ladder idiom; rewrite to
    # disjoint (A..B] bands (the boundary amount belongs to the lower tier)
    ladder = bool(typed) and all(
        t[2] == float("inf") and t[1] is False and t[0] > float("-inf") for t in typed
    ) and all(typed[i][0] < typed[i + 1][0] for i in range(len(typed) - 1))
    if ladder:
        for i in range(len(typed) - 1):
            typed[i][2] = typed[i + 1][0]
            typed[i][3] = not typed[i + 1][1]
    for a, b in zip(typed, typed[1:]):
        if a[2] > b[0] or (a[2] == b[0] and a[3] and b[1]):
            return None  # overlapping bands -> defer rather than fake disjointness
    # restore None for unbounded sides (band_to_feel renders comparison form)
    out = []
    for t in typed:
        lo = None if t[0] == float("-inf") else t[0]
        hi = None if t[2] == float("inf") else t[2]
        out.append(((lo, t[1], hi, t[3]), t[4], t[5]))
    if ladder:
        notes.append(
            "The source states only escalating lower bounds (> PHP A -> role 1; "
            "> PHP B -> role 2, ...); interpreted as an approval ladder — each band runs "
            "from its threshold to the next tier's threshold."
        )
    note = "\n" + "\n".join(notes) if notes else ""
    return out, text, note


def band_to_feel(band) -> str:
    lo, lo_inc, hi, hi_inc = band
    if lo is None and hi is None:
        return "-"
    if lo is None:
        return ("<=" if hi_inc else "<") + " " + fmt_num(hi)
    if hi is None:
        return (">=" if lo_inc else ">") + " " + fmt_num(lo)
    l = "[" if lo_inc else "("
    r = "]" if hi_inc else ")"
    return f"{l}{fmt_num(lo)}..{fmt_num(hi)}{r}"


def prose_decision(dec_id, wf_id, row_text, provenance):
    parsed = extract_tier_set(row_text)
    if not parsed:
        return None
    tiers, verbatim, note = parsed
    inputs = [{"label": "Amount (PHP)", "feel": "Amount", "type": "number", "values": None}]
    outputs = [{"label": "Approver", "name": "Approver", "values": None}]
    rules = [{"in": [band_to_feel(b)], "out": ['"' + a.replace('"', "'") + '"']} for b, a, _ in tiers]
    name = truncate(f"Authorization threshold — {wf_id}", MAX_NAME)
    return {
        "id": dec_id, "name": name, "hit": "U",
        "inputs": inputs, "outputs": outputs, "rules": rules,
        "description": provenance + note + "\nVerbatim: " + truncate(verbatim, MAX_DESC),
    }


# ---------------------------------------------------------------- DMN emission

def build_decision_xml(d, num_pad) -> list[str]:
    out = [f'  <decision id="{d["id"]}" name="{esc(d["name"])}">']
    desc = d["description"]
    out.append(f"    <description>{esc(desc)}</description>")
    out.append(f'    <decisionTable hitPolicy="{d["hit"]}">')
    for k, col in enumerate(d["inputs"], 1):
        out.append(f'      <input id="{d["id"]}_In{k:02d}" label="{esc(col["label"])}">')
        out.append(f'        <inputExpression id="{d["id"]}_InExpr{k:02d}" typeRef="{col["type"]}">')
        out.append(f"          <text>{esc(col['feel'])}</text>")
        out.append("        </inputExpression>")
        out.append("      </input>")
    for k, col in enumerate(d["outputs"], 1):
        nm = esc(col["name"]) if col["name"] else f"Output{k}"
        out.append(f'      <output id="{d["id"]}_Out{k:02d}" label="{esc(col["label"])}" name="{nm}" typeRef="string"/>')
    for ri, rule in enumerate(d["rules"], 1):
        out.append(f'      <rule id="{d["id"]}_Rule{ri:02d}">')
        for e in rule["in"]:
            out.append(f"        <inputEntry><text>{esc(e)}</text></inputEntry>")
        for e in rule["out"]:
            out.append(f"        <outputEntry><text>{esc(e)}</text></outputEntry>")
        out.append("      </rule>")
    out.append("    </decisionTable>")
    out.append("  </decision>")
    return out


def build_dmndi(decisions) -> list[str]:
    out = ["  <dmndi:DMNDI>", '    <dmndi:DMNDiagram id="Diagram_1">']
    per_row = 4
    for i, d in enumerate(decisions):
        col, row = i % per_row, i // per_row
        x, y = 160 + col * 260, 80 + row * 140
        out.append(f'      <dmndi:DMNShape id="{d["id"]}_di" dmnElementRef="{d["id"]}">')
        out.append(f'        <dc:Bounds x="{x}" y="{y}" width="200" height="90"/>')
        out.append("      </dmndi:DMNShape>")
    out.append("    </dmndi:DMNDiagram>")
    out.append("  </dmndi:DMNDI>")
    return out


DEFINITIONS_TMPL = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<definitions xmlns="https://www.omg.org/spec/DMN/20191111/MODEL/"\n'
    '             xmlns:dmndi="https://www.omg.org/spec/DMN/20191111/DMNDI/"\n'
    '             xmlns:dc="https://www.omg.org/spec/DMN/20181101/DC/"\n'
    '             xmlns:di="https://www.omg.org/spec/DMN/20181101/DI/"\n'
    '             id="Definitions_{def_id}"\n'
    '             name="{def_name}"\n'
    '             namespace="https://erpplans.local/dmn/{def_id}"\n'
    '             exporter="erpplans generate-dmn.py" exporterVersion="1.0">\n'
    "{body}\n</definitions>\n"
)


def render_file(pa_path: Path) -> tuple[str, int, int]:
    """Render a PA file's DMN XML in memory. Returns (xml_text, decisions, deferred).

    Empty xml_text (= no decisions) means no file should exist. Split from
    convert_file by the 2026-09-16 forty-seventh-wave consistency review so
    --check can byte-compare the shipped tree against a fresh re-derivation
    without writing (the shipped-currency guarantee generate-role-coverage.py
    --check has given the role-coverage matrix since the thirtieth wave).
    """
    text = pa_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    def_id = re.sub(r"[^A-Za-z0-9_.-]", "_", pa_path.stem)
    def_name = truncate(strip_md(pa_path.stem.replace("-", " ")), 80)

    decisions = []
    deferred = 0

    # 1. rule-shaped tables (anywhere in the file; provenance = nearest heading)
    for heading, header, ins, outs, rows in extract_tables(lines):
        n = len(decisions) + 1
        dec = table_decision(
            f"Decision_T{n:02d}", heading, header, ins, outs, rows,
            provenance=f"Source: {pa_path.relative_to(SRC)} · section “{strip_md(heading)}” · rule table",
        )
        if dec:
            decisions.append(dec)

    # 2. tiered money-authorization rules inside workflow step rows
    current_wf = ""
    for line in lines:
        m = re.match(r"^#{2,4} (W\d+[A-Za-z]?)\. (.+?)\s*$", line)
        if m:
            current_wf = m.group(1)
            continue
        row_m = re.match(r"^\|\s*\d+\s*\|(.+)\|\s*$", line)
        if not row_m or not current_wf:
            continue
        row_text = row_m.group(1)
        if not (re.search(AMT, row_text, re.I) and VERB.search(row_text)):
            continue
        prov = (
            f"Source: {pa_path.relative_to(SRC)} · workflow {current_wf} · step row "
            f"(authorization thresholds)"
        )
        dec = prose_decision(f"Decision_{current_wf}_{len(decisions)+1:02d}", current_wf, row_text, prov)
        if dec:
            decisions.append(dec)
        else:
            deferred += 1

    if not decisions:
        return "", 0, deferred

    body = []
    for d in decisions:
        body.extend(build_decision_xml(d, len(decisions)))
    body.extend(build_dmndi(decisions))
    xml = DEFINITIONS_TMPL.format(def_id=def_id, def_name=esc(def_name), body="\n".join(body))
    return xml, len(decisions), deferred


def convert_file(pa_path: Path, out_path: Path) -> tuple[int, int]:
    """Writes render_file()'s output. Returns (decisions_written, deferred_count)."""
    xml, n, deferred = render_file(pa_path)
    if not xml:
        return 0, deferred
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(xml, encoding="utf-8")
    return n, deferred


# ---------------------------------------------------------------- validation

DMN_NS = "https://www.omg.org/spec/DMN/20191111/MODEL/"
DMNDI_NS = "https://www.omg.org/spec/DMN/20191111/DMNDI/"


def validate_file(path: Path) -> str | None:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return f"XML parse error: {e}"
    if root.tag != f"{{{DMN_NS}}}definitions":
        return f"root is {root.tag}"
    ids = set()
    for el in root.iter():
        i = el.attrib.get("id")
        if i:
            if i in ids:
                return f"duplicate id {i}"
            ids.add(i)
    decisions = root.findall(f"{{{DMN_NS}}}decision")
    if not decisions:
        return "no decision elements"
    for dec in decisions:
        dt = dec.find(f"{{{DMN_NS}}}decisionTable")
        if dt is None:
            return f"{dec.get('id')}: no decisionTable"
        inputs = dt.findall(f"{{{DMN_NS}}}input")
        outputs = dt.findall(f"{{{DMN_NS}}}output")
        rules = dt.findall(f"{{{DMN_NS}}}rule")
        if not inputs or not outputs or not rules:
            return f"{dec.get('id')}: decisionTable needs >=1 input, output and rule"
        for r in rules:
            ie = r.findall(f"{{{DMN_NS}}}inputEntry")
            oe = r.findall(f"{{{DMN_NS}}}outputEntry")
            if len(ie) != len(inputs) or len(oe) != len(outputs):
                return f"{r.get('id')}: entry count mismatch ({len(ie)}/{len(inputs)} in, {len(oe)}/{len(outputs)} out)"
            for e in ie + oe:
                if not (e.findtext(f"{{{DMN_NS}}}text") or "").strip():
                    return f"{r.get('id')}: empty entry text"
    for sh in root.iter(f"{{{DMNDI_NS}}}DMNShape"):
        ref = sh.get("dmnElementRef")
        if ref not in ids:
            return f"DMNShape dmnElementRef broken: {ref}"
    shape_refs = {sh.get("dmnElementRef") for sh in root.iter(f"{{{DMNDI_NS}}}DMNShape")}
    for dec in decisions:
        if dec.get("id") not in shape_refs:
            return f"{dec.get('id')}: decision has no DMNShape (would not render in a DRD)"
    return None


# ---------------------------------------------------------------- main

def main() -> int:
    check = "--check" in sys.argv[1:]
    pa_files = sorted(SRC.glob("VS-*/PA-*.md"))
    total_dec = total_deferred = files_out = 0
    failures = []
    if check:
        # Forty-seventh-wave shipped-currency arm (2026-09-16): byte-compare the
        # shipped tree against a fresh in-memory re-derivation. Nothing is written.
        # The dmn/ tree previously had NO content pin at all — Check 71 reads it
        # structurally (decision-table shape, DRD refs) and Check 74 pins only the
        # README quick-stats figures — so a PA edit to a rule-shaped table or a
        # tiered authorization step shipped without regeneration, a hand-edit of a
        # generated file, a partial regeneration, or a stale file whose PA no
        # longer yields decisions all shipped invisibly. The markdown remains the
        # source of truth: drift is resolved by regenerating, never by hand-edit.
        shipped = {p.relative_to(OUT).as_posix() for p in OUT.rglob("*.dmn")}
        derived = {p.relative_to(SRC).with_suffix(".dmn").as_posix() for p in pa_files}
        n_drift = 0
        for pa in pa_files:
            rel = pa.relative_to(SRC).with_suffix(".dmn")
            out_path = OUT / rel
            xml, n, deferred = render_file(pa)
            total_dec += n
            total_deferred += deferred
            if not xml:
                if out_path.exists():
                    print(f"DRIFT|{rel.as_posix()}  shipped but its markdown no longer yields decisions (delete or restore the PA)")
                    n_drift += 1
                continue
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
            f"\n=== --check: {len(pa_files)} PA files, {total_dec} decisions / "
            f"{total_deferred} deferred re-derived, {len(shipped)} shipped files, {n_drift} drifted ==="
        )
        if n_drift:
            print("SHIPPED TREE IS STALE — regenerate (python3 07-methodology/generate-dmn.py); "
                  "the markdown is the source of truth, never hand-edit dmn/.")
            return 1
        print("Shipped dmn/ tree is byte-identical to the generator's re-derivation from "
              "the markdown corpus.")
        return 0
    for pa in pa_files:
        rel = pa.relative_to(SRC).with_suffix(".dmn")
        out_path = OUT / rel
        n, deferred = convert_file(pa, out_path)
        total_dec += n
        total_deferred += deferred
        if n == 0:
            if out_path.exists():
                out_path.unlink()
            continue
        files_out += 1
        err = validate_file(out_path)
        if err:
            failures.append((out_path, err))
        print(f"{rel}  decisions={n} deferred={deferred}")
    print(
        f"\n=== {files_out} DMN files, {total_dec} decisions, {total_deferred} deferred rule sets ==="
    )
    if failures:
        print("VALIDATION FAILURES:")
        for p, e in failures:
            print(f"  {p}: {e}")
        return 1
    print("All generated files validate (well-formed XML, structure, ids, entries, DMNDI).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
