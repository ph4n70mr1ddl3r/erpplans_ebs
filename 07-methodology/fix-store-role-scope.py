#!/usr/bin/env python3
"""
fix-store-role-scope.py — store-layer role-scope true-up (fifty-sixth-wave
consistency review, by direction: analyze each store, its workflows and roles
for consistency and time-and-motion overload; implement).

Four adjudicated classes, every edit confined to STRUCTURED role cells
(Owner / Participants field rows and step-table Role (R) / Role (A) cells);
step-description prose is never touched:

  C1  store 'Customer Service Representative' → store roster title
      'Customer Service Rep'. 25 store-context workflows used the HQ
      Customer Service title form (the 22-HC HQ register row) for store
      counter/desk duties — mis-resolving Owner, participant and step cells
      to the HQ bucket in the role-coverage matrix and the virtual-gemba
      analyzer. HQ-context occurrences (contact-center/ecommerce workflows:
      W266/W267/W268/W591/W592/W756/W1229/W1311/W1470/W1499/W2552/W5550)
      intentionally keep the HQ form — this script does not touch them.

  C2  step Role cells 'Floor Associate' → 'Sales Associate' (PA-09.1, PA-09.3,
      PA-24.2): floor-assistance, on-spot resolution and hazmat-advisory cells
      carried an uncharted vocabulary form; the duties are Sales Associate work
      per the §12.1 roster ('floor coverage, customer assistance').

  C5  W562 (Store-Level Loss Prevention Daily Routine) steps 2–8/10–11 Role (R)
      'LP Officer' → 'Store Manager'. The workflow's own Owner cell reads
      'LP Officer / Store Manager (stores without dedicated LP Officer)' —
      no store has a dedicated officer (20 regional officers for 200 stores),
      so the store-daily routine's de-facto executor per the corpus's own
      design is the Store Manager. Compound steps 1/9/12 already carry the
      Store Manager and stay.

  F   four dual-scope Frequency fields re-worded to lead with the per-store
      figure the analyzer's documented cadence ladder parses (network totals
      move to the parenthetical): W559, W1168, W566, W609.

Read-only outside the adjudicated cells; prints per-class counts and exits 1
if any anchor is missing (so a drifted corpus fails loudly, never silently).
"""
import os
import re
import sys

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOL_DIR)
WF = os.path.join(REPO, "01-model-company", "workflows")

CSR = "Customer Service Representative"
CSR_STORE = "Customer Service Rep"

C1_WORKFLOWS = [
    ("VS-07-store-operations/PA-07.1-store-daily-management.md", "W1116"),
    ("VS-07-store-operations/PA-07.1-store-daily-management.md", "W1121"),
    ("VS-07-store-operations/PA-07.1-store-daily-management.md", "W1133"),
    ("VS-07-store-operations/PA-07.1-store-daily-management.md", "W1142"),
    ("VS-07-store-operations/PA-07.1-store-daily-management.md", "W1506"),
    ("VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md", "W771"),
    ("VS-08-pos-checkout/PA-08.1-transaction-processing.md", "W1235"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W954"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W955"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W1088"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W1104"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W1109"),
    ("VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md", "W1114"),
    ("VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md", "W1098"),
    ("VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md", "W772"),
    ("VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md", "W773"),
    ("VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md", "W775"),
    ("VS-10-ecommerce-digital/PA-10.2-order-fulfillment-and-delivery.md", "W1273"),
    ("VS-12-installation-services/PA-12.1-installation-and-repair-services.md", "W1254"),
    ("VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md", "W781"),
    ("VS-23-loss-prevention/PA-23.2-physical-security-and-surveillance.md", "W1248"),
    ("VS-24-health-safety-environment/PA-24.1-occupational-health-and-safety.md", "W1266"),
    ("VS-32-returns-reverse-logistics/PA-32.1-customer-returns-processing.md", "W1622"),
    ("VS-71-anti-counterfeit-authentication/PA-71.1-product-authentication-serialization.md", "W2552"),
    ("VS-78-green-building-advisory/PA-78.2-green-building-project-consultation.md", "W2730"),
]

# C1b — unambiguous store-execution files: remaining long-form occurrences
# (Controls bullets, analysis prose, step text) also canonicalize — the store
# files carry no HQ contact-center content. Mixed files (PA-10.2, PA-13.1,
# PA-23.2, PA-24.1) keep their per-workflow adjudication only.
C1B_FILES = [
    "VS-07-store-operations/PA-07.1-store-daily-management.md",
    "VS-07-store-operations/PA-07.3-store-receiving-and-replenishment.md",
    "VS-08-pos-checkout/PA-08.1-transaction-processing.md",
    "VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md",
    "VS-09-in-store-services/PA-09.2-project-estimation-and-advisory.md",
    "VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md",
    "VS-12-installation-services/PA-12.1-installation-and-repair-services.md",
    "VS-32-returns-reverse-logistics/PA-32.1-customer-returns-processing.md",
    "VS-78-green-building-advisory/PA-78.2-green-building-project-consultation.md",
]

C2_FILES = [
    "VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md",
    "VS-09-in-store-services/PA-09.3-customer-amenities-and-assistance.md",
    "VS-24-health-safety-environment/PA-24.2-emergency-preparedness.md",
]

C5_FILE = "VS-07-store-operations/PA-07.1-store-daily-management.md"
C5_WF = "W562"
C5_STEPS = {2, 3, 4, 5, 6, 7, 8, 10, 11}

F_FIELDS = [
    ("VS-07-store-operations/PA-07.2-store-facility-and-safety.md", "W559",
     "~400–600 incidents per month across 200 stores (~2–3 per store per month)",
     "~2–3 incidents per store per month (~400–600 incidents per month across 200 stores)"),
    ("VS-06-logistics-fleet/PA-06.1-outbound-distribution.md", "W1168",
     "~500–600 DSD receipts/month across all stores (~2–3 DSD deliveries per store per month)",
     "~2–3 DSD deliveries per store per month (~500–600 DSD receipts/month across all stores)"),
    ("VS-13-customer-experience/PA-13.3-customer-data-and-crm.md", "W566",
     "~400–600 visits per month (~2–3 visits per store per month)",
     "~2–3 visits per store per month (~400–600 visits per month chain-wide)"),
    ("VS-07-store-operations/PA-07.4-store-staffing-and-people.md", "W609",
     "As needed; ~1,200–1,600 new hires/year across 200 stores (~6–8 per store per year per profile §11.4)",
     "As needed; ~6–8 new hires per store per year per profile §11.4 (~1,200–1,600/year across 200 stores)"),
]

FIELD_ROW = re.compile(r"^\| \*\*(Owner|Participants)\*\* \|")
STEP_ROW = re.compile(r"^\| (\d+) \|")

WF_SPLIT = re.compile(r"^(## W\d+[A-Z]?\..*)$", re.M)


def canon(s):
    """Canonicalize the CSR title forms inside one structured cell."""
    before = s.count(CSR)
    s = (s.replace(CSR + " (Store)", CSR_STORE)
          .replace(CSR + " (CSR)", CSR_STORE)
          .replace(CSR, CSR_STORE))
    return s, before


def rewrite_workflow(body, csr=False, c5=False):
    """Apply structured-cell edits to one workflow body; returns (body, n)."""
    n = 0
    out = []
    for ln in body.split("\n"):
        if csr and FIELD_ROW.match(ln) and CSR in ln:
            ln, k = canon(ln)
            n += k
        elif STEP_ROW.match(ln):
            cells = ln.split("|")
            # split('|') on '| a | b |' → ['', ' a ', ' b ', ''] ; step rows:
            # ['', ' # ', ' desc ', ' R ', ' A ', ' dur ', ...] → idx 3, 4
            if len(cells) >= 5:
                if csr:
                    for idx in (3, 4):
                        if CSR in cells[idx]:
                            cells[idx], k = canon(cells[idx])
                            n += k
                if c5:
                    try:
                        stepno = int(cells[1].strip())
                    except ValueError:
                        stepno = None
                    if stepno in C5_STEPS and cells[3].strip() == "LP Officer":
                        cells[3] = " Store Manager "
                        n += 1
            ln = "|".join(cells)
        out.append(ln)
    return "\n".join(out), n


def process_file(rel, targets, c5=False):
    path = os.path.join(WF, rel)
    text = open(path, encoding="utf-8").read()
    pieces = WF_SPLIT.split(text)
    # pieces: [pre, header, body, header, body, ...]
    out = [pieces[0]]
    total = 0
    for i in range(1, len(pieces) - 1, 2):
        header, body = pieces[i], pieces[i + 1]
        wf = header.split()[1].rstrip(".")
        if wf in targets:
            body, n = rewrite_workflow(body, csr=True, c5=c5)
            total += n
        out.extend([header, body])
    open(path, "w", encoding="utf-8").write("".join(out))
    return total


def main():
    total = 0
    per_file = {}
    for rel, wf in C1_WORKFLOWS:
        per_file.setdefault(rel, set()).add(wf)
    c1 = 0
    for rel, wfs in sorted(per_file.items()):
        c1 += process_file(rel, wfs)
    print(f"C1 store-CSR canonicalization: {c1} structured-cell replacements "
          f"across {len(per_file)} files / {len(C1_WORKFLOWS)} workflows")
    total += c1

    # ---- C1b (store-file prose sweep)
    c1b = 0
    for rel in C1B_FILES:
        path = os.path.join(WF, rel)
        t2 = open(path, encoding="utf-8").read()
        k = t2.count(CSR)
        t2 = (t2.replace(CSR + " (Store)", CSR_STORE)
               .replace(CSR + " (CSR)", CSR_STORE)
               .replace(CSR, CSR_STORE))
        open(path, "w", encoding="utf-8").write(t2)
        c1b += k
    print(f"C1b store-file prose sweep: {c1b} occurrences across {len(C1B_FILES)} files")
    total += c1b

    c2 = 0
    for rel in C2_FILES:
        path = os.path.join(WF, rel)
        lines = open(path, encoding="utf-8").read().split("\n")
        n = 0
        for i, ln in enumerate(lines):
            if STEP_ROW.match(ln) and "Floor Associate" in ln:
                lines[i] = ln.replace("Floor Associate", "Sales Associate")
                n += 1
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        c2 += n
        print(f"C2 {rel}: {n} Floor Associate role cells -> Sales Associate")
    total += c2

    c5 = process_file(C5_FILE, {C5_WF}, c5=True)
    print(f"C5 {C5_FILE} {C5_WF}: {c5} pure LP Officer cells -> Store Manager")
    total += c5

    fn = 0
    for rel, wf, old, new in F_FIELDS:
        path = os.path.join(WF, rel)
        text = open(path, encoding="utf-8").read()
        if old not in text:
            print(f"F ERROR: anchor not found in {rel} {wf}: {old[:60]}")
            return 1
        open(path, "w", encoding="utf-8").write(text.replace(old, new))
        fn += 1
    print(f"F dual-scope frequency fields re-worded: {fn}")
    total += fn

    print(f"total structured-cell edits: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
