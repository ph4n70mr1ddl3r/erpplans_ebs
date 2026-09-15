#!/usr/bin/env python3
"""Role-coverage matrix generator — 01-model-company/role-coverage-matrix.md.

Parses the workflow catalog (all PA files' Owner / Participants / Steps-table
Role (R) / Role (A) fields), the criticality register (Tier 1/2/3 membership)
and the official table of organization (§5.3 Enterprise Role Register, §7.2
store roster, §7.3 DC roster) and generates a per-role coverage matrix:
role × department × workflows-owned × workflows-participated × step-R/A ×
tier mix of workflows touched.

Resolution order for a role mention:
  1. §5.3 HQ register (its titles are the canonical workflow-RACI vocabulary,
     so workflow Owners resolve one-to-one) — incl. C-suite/role aliases;
  2. §7.3 DC roster and §7.2 store roster (field roles);
  3. IT product-model seats (the §5.3 Information Technology row is
     by-reference to it-product-operating-model.md §5);
  4. department-level actors (the department named as performer — "Finance",
     "Legal", generic mid-management forms) — bucketed per department;
  5. system & automated actors (ERP/EBS, POS, WMS, IAP, agents);
  6. governance bodies (Board and committees);
  7. generic workforce mentions (employee/staff);
  8. external counterparties (customers, vendors, banks, government);
  9. Uncharted — reported honestly as the vocabulary-drift watchlist.

A cell that does not resolve whole is split on "," and "/" and each part is
resolved (preserving canonical titles that legitimately contain "/", e.g.
"Sustainability / ESG Manager", which resolve whole in step 1-8).

Deterministic: no timestamps, sorted outputs — `--check` re-derives and
byte-compares the shipped artifact (regenerate after any PA/role/register
change). `--census` re-derives the owner-resolution census (resolved /
uncharted workflow Owner cells under build()'s own touch semantics, plus the
uncharted-watchlist population) for validate-repo.sh's pinned baseline; the
matrix is a derived view, never hand-edited).

Data integrity asserted at generation: every workflow has exactly one Owner;
every workflow id resolves to exactly one confirmed Tier.
"""
import os
import re
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF = os.path.join(REPO, "01-model-company", "workflows")
OUT = os.path.join(REPO, "01-model-company", "role-coverage-matrix.md")
TO_PATH = os.path.join(REPO, "01-model-company", "optimal-table-of-organization.md")
TIER_PATH = os.path.join(WF, "workflow-criticality-classification.md")

# IT product-model seats (the §5.3 Information Technology row is by-reference
# to it-product-operating-model.md §5 — these are the seats that appear in
# workflow RACI). Keys are normalized (lowercase, parentheticals stripped).
IT_SEATS = {
    "it product owner": "IT Product Owner",
    "product owner": "IT Product Owner",
    "product manager": "IT Product Manager (build squad)",
    "erp functional analyst": "ERP Functional Analyst",
    "functional analyst": "ERP Functional Analyst",
    "erp functional analysts": "ERP Functional Analyst",
    "it helpdesk": "IT Helpdesk Agent (FS)",
    "it helpdesk agent": "IT Helpdesk Agent (FS)",
    "helpdesk": "IT Helpdesk Agent (FS)",
    "helpdesk agent": "IT Helpdesk Agent (FS)",
    "it operations": "IT Operations (FS/INFRA)",
    "it operations manager": "IT Operations (FS/INFRA)",
    "integration engineer": "IAP Integration Engineer",
    "integration support engineer": "IAP Integration Support Engineer",
    "data engineer": "DP Data Engineer",
    "data engineers": "DP Data Engineer",
    "security engineer": "SEC Security Engineer",
    "security analyst": "SEC Security Analyst",
    "it security": "SEC (Cybersecurity, Privacy & OT Security)",
    "it security analyst": "SEC Security Analyst",
    "it security manager": "SEC Security Engineer",
    "ot security lead": "SEC OT Security Lead",
    "system administrator": "INFRA System Administrator",
    "network engineer": "INFRA Network Engineer",
    "database administrator": "INFRA DBA / SaaS Administrator",
    "dba": "INFRA DBA / SaaS Administrator",
    "cloud engineer": "INFRA Cloud Engineer",
    "sre": "INFRA Site Reliability Engineer",
    "software engineer": "Build-Squad Software Engineer",
    "software engineers": "Build-Squad Software Engineer",
    "tech lead": "Build-Squad Tech Lead",
    "qa automation engineer": "Build-Squad QA Automation Engineer",
    "bi": "DP BI Platform",
    "bi manager": "DP BI Platform",
    "bi analyst": "DP BI Platform",
    "data analyst": "DP Data & Reporting Analyst",
    "data scientist": "DP Data Scientist / ML",
    "mdm steward": "DP MDM Steward",
    "mdm stewards": "DP MDM Steward",
    "master data system": "DP MDM Steward",
    "ai engineer": "AAP Agent Engineer",
    "agent engineer": "AAP Agent Engineer",
    "ai governance lead": "AAP AI-Governance Liaison",
    "analytics": "DP / Data & Analytics (VS-28)",
    "security": "SEC (Cybersecurity, Privacy & OT Security)",
    "ai governance": "AAP AI-Governance Liaison",
    "cdp lead": "DP Customer Data Platform",
    "chief enterprise architect": "Head of Enterprise Architecture (CIO Office)",
    "enterprise architect": "Head of Enterprise Architecture (CIO Office)",
    "it asset manager": "FS ITAM Administrator",
    "it team": "Information Technology (department)",
}

# Executive shorthands → §5.3 Executive Office rows.
EXEC_ALIASES = {
    "ceo": "CEO / President",
    "ceo / president": "CEO / President",
    "president": "CEO / President",
    "cfo": "Chief Finance Officer (CFO)",
    "coo": "Chief Operating Officer (COO)",
    "cio": "Chief Information Officer (CIO)",
    "cmo": "Chief Marketing Officer (CMO)",
    "chro": "Chief Human Resources Officer (CHRO)",
}

# Role aliases → canonical §5.3 titles (or rosters via STORE_/DC_ prefixes).
ROLE_ALIASES = {
    "vp merchandising": "VP for Merchandising",
    "vp supply chain": "VP Supply Chain & Logistics (dual-hat GM, BuildRight Logistics, Inc.)",
    "vp legal": "VP Legal & Compliance",
    "vp legal & compliance": "VP Legal & Compliance",
    "vp hr": "VP Human Resources",
    "vp store ops": "VP Store Operations (Director Field Retail Operations)",
    "controller": "VP Finance & Accounting / Corporate Controller",
    "finance controller": "VP Finance & Accounting / Corporate Controller",
    "dpo": "Data Privacy Officer (DPO)",
    "head of ia": "Head of Internal Audit & Risk",
    "s&op lead": "S&OP/IBP Lead",
    "logistics finance analyst": "Logistics & Cost Finance Analyst",
    "credit manager": "AR & Credit Manager",
    "treasury mgr": "Treasury Manager",
    "quality manager": "Head of Quality Management",
    "hse officer": "Safety Officer (HSE Officer, DOLE-accredited SO2)",
    "lp officer": "Regional LP Officer",
    "lp officers": "Regional LP Officer",
    "lp analyst": "LP Analytics Analyst",
    "merchandise planner": "Merchandise Planner / Allocator",
    "merchandise planners": "Merchandise Planner / Allocator",
    "category managers": "Category Manager",
    "category mgr": "Category Manager",
    "loyalty program manager": "Loyalty & CRM Manager",
    "govt affairs mgr": "Government Affairs Manager",
    "sustainability lead": "Head of Sustainability / ESG",
    "sustainability/esg manager": "Head of Sustainability / ESG",
    "master data manager": "Merchandising Operations & Master Data Manager",
    "hr head": "VP Human Resources",
    "records manager": "Litigation & IP Counsel (records program)",
    "dc manager": "DC Manager (DC roster)",
    "dc supervisor": "Shift Supervisor (DC roster)",
    "store manager": "STORE:Store Manager",
    "store managers": "STORE:Store Manager",
    "department supervisor": "STORE:Department Supervisor",
    "dept. supervisor": "STORE:Department Supervisor",
    "department supervisors": "STORE:Department Supervisor",
    "sales associate": "STORE:Sales Associate",
    "sales associates": "STORE:Sales Associate",
    "associate": "STORE:Sales Associate",
    "cashier": "STORE:Cashier",
    "cashiers": "STORE:Cashier",
    "stock associate": "STORE:Stock Associate",
    "csr": "STORE:Customer Service Representative",
    "customer service rep": "STORE:Customer Service Representative",
    "sales rep": "STORE:Sales Associate",
    "security guard": "EXTERNAL:Security Guard (contracted)",
    "receiving clerk": "DC:Receiving Clerk",
    "receiving clerks": "DC:Receiving Clerk",
}

# Department-level actors: the department (or a generic form within it) named
# as performer. Canonical department labels follow the §5.1 department names.
DEPT_ACTORS = {
    "finance": "Finance & Accounting", "accounting": "Finance & Accounting",
    "finance manager": "Finance & Accounting", "finance analyst": "Finance & Accounting",
    "finance analysts": "Finance & Accounting", "accounting manager": "Finance & Accounting",
    "chief accountant": "Finance & Accounting", "cost accountant": "Finance & Accounting",
    "fixed asset accountant": "Finance & Accounting", "ap": "Finance & Accounting",
    "ar": "Finance & Accounting", "ap clerk": "Finance & Accounting",
    "treasury": "Finance & Accounting", "insurance": "Finance & Accounting",
    "fraud management lead": "Finance & Accounting",
    "legal": "Legal & Compliance", "compliance": "Legal & Compliance",
    "compliance officer": "Legal & Compliance", "compliance specialist": "Legal & Compliance",
    "legal counsel": "Legal & Compliance", "privacy": "Legal & Compliance",
    "records": "Legal & Compliance", "trade compliance manager": "Legal & Compliance",
    "ethics & compliance officer": "Legal & Compliance",
    "human resources": "Human Resources", "hr": "Human Resources",
    "hr manager": "Human Resources", "l&d": "Human Resources",
    "it": "Information Technology", "ecommerce": "Digital Commerce (IT-built platforms)",
    "ecommerce manager": "Digital Commerce (IT-built platforms)",
    "digital commerce inc": "Digital Commerce (IT-built platforms)",
    "digital product manager": "Digital Commerce (IT-built platforms)",
    "marketing": "Marketing", "marketing manager": "Marketing",
    "insights": "Marketing", "insights analyst": "Marketing",
    "market research analyst": "Marketing", "event marketing mgr": "Marketing",
    "sales enablement lead": "Marketing",
    "merchandising": "Merchandising & Buying",
    "pricing": "Merchandising & Buying",
    "master data analyst": "Merchandising & Buying",
    "procurement": "Supply Chain & Logistics", "procurement specialist": "Supply Chain & Logistics",
    "procurement director": "Supply Chain & Logistics", "vendor mgmt": "Supply Chain & Logistics",
    "logistics": "Supply Chain & Logistics", "logistics manager": "Supply Chain & Logistics",
    "supply planning": "Supply Chain & Logistics", "supply planning manager": "Supply Chain & Logistics",
    "supply planner": "Supply Chain & Logistics", "dc ops": "Supply Chain & Logistics",
    "store ops": "Store Operations", "store operation": "Store Operations",
    "operations": "Store Operations", "services manager": "Store Operations",
    "rental fleet manager": "Store Operations", "store": "Store Operations",
    "stores": "Store Operations",
    "internal audit": "Internal Audit & Risk", "audit": "Internal Audit & Risk",
    "auditor": "Internal Audit & Risk", "risk": "Internal Audit & Risk",
    "customer service": "Customer Service", "cx": "Customer Service",
    "customer service manager": "Customer Service", "cs manager": "Customer Service",
    "quality": "Quality Management",
    "facilities": "Facilities & Real Estate", "real estate": "Facilities & Real Estate",
    "facilities & real estate": "Facilities & Real Estate",
    "strategy": "Strategy / Corporate Planning", "pmo": "Strategy / Corporate Planning",
    "sponsor": "Strategy / Corporate Planning",
    "sustainability": "Sustainability / ESG",
    "hse": "Health, Safety & Environment",
    "lp": "Regional Loss Prevention", "lp manager": "Regional Loss Prevention",
    "loss prevention": "Regional Loss Prevention",
    "trade sales": "Trade / Account Management", "trade sales manager": "Trade / Account Management",
    "trade capability lead": "Trade / Account Management",
    "head of strategic accounts": "Trade / Account Management",
    "account manager": "Trade / Account Management",
    "head of trade / account management": "Trade / Account Management",
    "tax": "Finance & Accounting (Tax)",
    "inventory": "Supply Chain & Logistics", "warehouse": "Supply Chain & Logistics",
    "payroll": "Human Resources (Payroll)", "loyalty": "Marketing (Loyalty)",
    "dc operations": "Supply Chain & Logistics",
    "store operations": "Store Operations",
    "project manager": "Strategy / Corporate Planning (PMO)",
    "department head": "Generic / cross-department",
    "director": "Generic / cross-department",
    "gm": "Generic / cross-department",
    "management": "Generic / cross-department",
    "department heads": "Generic / cross-department",
    "data protection officer": "Data Privacy Officer (DPO)",
    "vp merch": "VP for Merchandising",
    "vp finance": "VP Finance & Accounting / Corporate Controller",
    "regulatory officer": "Regulatory Affairs Specialist",
    "govt affairs": "Government Affairs Manager",
    "fp&a": "Finance & Accounting (FP&A)",
    "product compliance manager": "Quality Management",
    "esg": "Sustainability / ESG", "occupational health": "Health, Safety & Environment",
    "safety": "Health, Safety & Environment",
    "master data": "Merchandising & Buying (Master Data)",
    "global sourcing": "Merchandising & Buying (Direct Sourcing)",
    "category": "Merchandising & Buying", "planogram": "Merchandising & Buying",
    "data science": "DP Data Scientist / ML",
    "ecommerce operations manager": "Digital Commerce (IT-built platforms)",
    "ifm": "Facilities & Real Estate", "maintenance": "Facilities & Real Estate",
    "engineering": "Facilities & Real Estate",
    "sales enablement": "Marketing", "crm": "Marketing", "retail media": "Marketing",
    "marketing ops": "Marketing",
    "fleet": "Supply Chain & Logistics", "import": "Supply Chain & Logistics",
    "imports": "Supply Chain & Logistics", "customs": "Supply Chain & Logistics",
    "fleet manager": "Supply Chain & Logistics",
    "recruitment": "Human Resources", "recruiting": "Human Resources",
    "training": "Human Resources", "hris": "Human Resources",
    "credit": "Finance & Accounting", "collections": "Finance & Accounting",
    "revenue assurance": "Finance & Accounting", "revenue": "Finance & Accounting",
    "trade": "Trade / Account Management", "b2b": "Trade / Account Management",
    "asset protection": "Regional Loss Prevention", "shrink": "Regional Loss Prevention",
    "front end": "Store Operations", "visual merchandising": "Merchandising & Buying",
    "operations manager": "Generic / cross-department",
    "buyer": "Merchandising & Buying", "buyers": "Merchandising & Buying",
}

SYSTEM_ACTORS = {
    "system", "systems", "erp", "ebs", "erp system", "oracle ebs", "pos system",
    "pos", "wms", "wms system", "iap", "aap", "agent", "ai agent", "ai agent (tier-gated)",
    "automation", "rpa", "edi", "portal", "system (automated)", "platform",
}

GOVERNANCE = {
    "board", "board of directors", "audit committee", "board audit committee",
    "executive committee", "exco", "board risk committee",
    "related-party transactions committee", "nomination & compensation committee",
}

WORKFORCE = {"employee", "employees", "staff", "workforce", "new hire", "new hires"}

EXTERNAL = {
    "customer", "customers", "shopper", "member", "loyalty member", "guest",
    "vendor", "vendors", "supplier", "suppliers", "vendor representative",
    "supplier representative", "concessionaire", "landlord", "lessor",
    "bank", "banks", "bank representative", "lender", "insurer",
    "insurance company", "3pl", "3pl carrier", "carrier", "carriers",
    "courier", "driver", "third-party delivery partner", "delivery partner",
    "applicant", "job applicant", "candidate", "job candidate",
    "external auditor", "external audit firm", "qsa", "pci qsa",
    "government agency", "regulator", "bir", "lgu", "dole", "sss",
    "philhealth", "pag-ibig", "denr", "bfp", "phivolcs", "pagasa",
    "contractor", "contractors", "service provider", "managed soc",
    "it vendor", "erp vendor", "oracle", "software vendor",
    "financing partner", "acquirer", "carrier partner",
}

SPLIT_RE = re.compile(r"\s*,\s*(?![^()]*\))")


def norm(s):
    s = re.sub(r"\s+", " ", s or "").strip().rstrip(".")
    return s.strip("*").strip()


def key(s):
    k = re.sub(r"\s*\([^)]*\)", "", norm(s)).strip().lower()
    return k.rstrip("*").strip()


def split_commas(cell):
    out = []
    for part in SPLIT_RE.split(norm(cell)):
        p = part.strip().strip("*").strip()
        if not p or p in {"—", "-", "–", "None", "N/A", "TBD"}:
            continue
        out.append(p)
    return out


class Resolver:
    def __init__(self, hq, dc, store, dept_order):
        self.hq = hq
        self.dc = dc
        self.store = store
        self.dept_order = dept_order
        self.cache = {}

    def resolve(self, raw):
        """Return (bucket, dept, title, hc) for a raw role string."""
        k = key(raw)
        if k in self.cache:
            return self.cache[k]
        r = self._resolve(k, raw)
        self.cache[k] = r
        return r

    def _resolve(self, k, raw):
        if k in self.hq:
            t, d, hc = self.hq[k]
            return ("hq", d, t, hc)
        if k in EXEC_ALIASES:
            t = EXEC_ALIASES[k]
            if t in {v[1] for v in self.hq.values()} or True:
                hk = key(t)
                if hk in self.hq:
                    t2, d2, hc2 = self.hq[hk]
                    return ("hq", d2, t2, hc2)
                return ("hq", "Executive Office", t, None)
        if k in self.dc:
            t, label = self.dc[k]
            return ("dc", label, t, None)
        if k in self.store:
            t, label = self.store[k]
            return ("store", label, t, None)
        if k in ROLE_ALIASES:
            v = ROLE_ALIASES[k]
            if v.startswith("STORE:"):
                return ("store", "Store (field, per-store roster)", v.split(":", 1)[1], None)
            if v.startswith("DC:"):
                return ("dc", "DC (field, per-DC roster)", v.split(":", 1)[1], None)
            if v.startswith("EXTERNAL:"):
                return ("ext", "External / counterparty", v.split(":", 1)[1], None)
            hk = key(v)
            if hk in self.hq:
                t2, d2, hc2 = self.hq[hk]
                return ("hq", d2, t2, hc2)
            return ("hq", "Information Technology (product model)", v, None)
        if k in IT_SEATS:
            return ("it", "Information Technology (product model)", IT_SEATS[k], None)
        if k in DEPT_ACTORS:
            return ("dept", DEPT_ACTORS[k], key(raw).title(), None)
        if k in SYSTEM_ACTORS:
            return ("sys", "System & automated actors", key(raw).title(), None)
        if k in GOVERNANCE:
            return ("gov", "Governance bodies", key(raw).title(), None)
        if k in WORKFORCE:
            return ("wf", "Workforce (generic)", key(raw).title(), None)
        if k in EXTERNAL:
            return ("ext", "External / counterparty", key(raw).title(), None)
        return ("unc", "Uncharted", norm(raw), None)


def parse_workflows():
    wfs = []
    vs_dirs = sorted(d for d in os.listdir(WF) if d.startswith("VS-"))
    for vd in vs_dirs:
        dd = os.path.join(WF, vd)
        vs_num = int(re.match(r"VS-(\d+)", vd).group(1))
        for fn in sorted(f for f in os.listdir(dd) if f.startswith("PA-") and f.endswith(".md")):
            pa = fn[:-3]
            text = open(os.path.join(dd, fn), encoding="utf-8").read()
            parts = re.split(r"^## (W\d+[A-Z]?)\. (.+)$", text, flags=re.M)
            for i in range(1, len(parts) - 2, 3):
                wid, title, body = parts[i], parts[i + 1], parts[i + 2]
                m = re.search(r"\| \*\*Owner\*\* \|(.*?)\|", body)
                owner = norm(m.group(1)) if m else None
                m = re.search(r"\| \*\*Participants\*\* \|(.*?)\|", body)
                participants = split_commas(m.group(1)) if m else []
                step_r, step_a = [], []
                lines = body.splitlines()
                in_steps = False
                for ln in lines:
                    if re.match(r"^\|\s*#\s*\|", ln) and "Role (R)" in ln:
                        in_steps = True
                        continue
                    if in_steps:
                        if not ln.startswith("|"):
                            in_steps = False
                            continue
                        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                        if len(cells) < 5 or set(cells[0]) <= set("- "):
                            continue
                        step_r.extend(split_commas(cells[2]))
                        step_a.extend(split_commas(cells[3]))
                wfs.append({"id": wid, "title": norm(title), "vs": vs_num, "pa": pa,
                            "owner": owner, "participants": participants,
                            "step_r": step_r, "step_a": step_a})
    return wfs


def parse_tiers():
    # Mirrors audit-model-docs.register_heading_hits' attribution exactly:
    # '## Tier N:', '### Tier N Additions' and '#### Tier N' blocks set the
    # context; other level-1/2 headings reset it; level-3/4 non-Tier headings
    # do not. This reproduces the canonical 1,396 / 3,296 / 758 attribution.
    tier = {}
    cur = None
    for ln in open(TIER_PATH, encoding="utf-8"):
        m = re.match(r"^(#{1,4}) (.*)", ln)
        if m:
            level, text = len(m.group(1)), m.group(2)
            tm = re.match(r"^Tier (\d):", text)
            am = re.match(r"^Tier (\d) Additions", text)
            t4 = re.match(r"^Tier (\d)", text) if level == 4 else None
            if tm:
                cur = int(tm.group(1))
            elif am:
                cur = int(am.group(1))
            elif t4:
                cur = int(t4.group(1))
            elif level <= 2:
                cur = None
            continue
        m = re.match(r"^\| (W\d+[A-Z]?) \| ", ln)
        if m and cur:
            tier[m.group(1)] = cur
    return tier


def parse_toc():
    text = open(TO_PATH, encoding="utf-8").read()
    s53 = text[text.index("### 5.3"):text.index("## 6.")]
    hq, dept_order = {}, []
    for m in re.finditer(r"^#### (.+?) \((\d+)[^)]*\)\s*$", s53, re.M):
        dept = m.group(1).strip()
        dept_order.append(dept)
        end = s53.find("\n#### ", m.end())
        body = s53[m.end():end if end > 0 else len(s53)]
        for r in re.finditer(r"^\| ([^*\n|][^|]*?) \| (\d+) \|", body, re.M):
            title = norm(r.group(1))
            hq[key(title)] = (title, dept, int(r.group(2)))
    dc = {}
    s73 = text[text.index("### 7.3"):text.index("## 8.")]
    for ln in s73.splitlines():
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[1] and cells[1] != "Role":
            hc = (cells[2] or "").strip("*").strip()
            if re.match(r"^\d+$", hc):
                title = norm(cells[1])
                if title and title.lower() != "total":
                    k = key(title)
                    dc.setdefault(k, (title, "DC (field, per-DC roster)"))
                    if k.endswith("s"):
                        dc.setdefault(k[:-1], (title, "DC (field, per-DC roster)"))
                    else:
                        dc.setdefault(k + "s", (title, "DC (field, per-DC roster)"))
    store = {}
    s72 = text[text.index("### 7.2"):text.index("### 7.3")]
    for ln in s72.splitlines():
        if not ln.startswith("|") or "Reports-to" in ln or set(ln) <= set("|- "):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue

        def add_store(t):
            t = norm(t)
            if not t or t in {"Roles", "Span"}:
                return
            k = key(t)
            store.setdefault(k, (t, "Store (field, per-store roster)"))
            if k.endswith("s"):
                store.setdefault(k[:-1], (t, "Store (field, per-store roster)"))
            else:
                store.setdefault(k + "s", (t, "Store (field, per-store roster)"))

        add_store(re.sub(r"\s*\(.*?\)$", "", cells[0]))
        for token in re.split(r";", cells[1]):
            t = re.sub(r"^\d+\s+", "", norm(token))
            t = re.sub(r"\s*\(.*?\)$", "", t).strip()
            add_store(t)
    return hq, dc, store, dept_order


def build():
    wfs = parse_workflows()
    tier = parse_tiers()
    hq, dc, store, dept_order = parse_toc()
    resolver = Resolver(hq, dc, store, dept_order)

    missing_owner = [w["id"] for w in wfs if not w["owner"]]
    untiered = sorted(w["id"] for w in wfs if w["id"] not in tier)
    assert not missing_owner, f"workflows without Owner: {missing_owner[:10]}"
    assert not untiered, f"workflows without confirmed Tier: {untiered[:10]}"

    stats = defaultdict(lambda: {"own": 0, "part": 0, "sr": 0, "sa": 0,
                                 "w": set(), "t": defaultdict(int)})
    meta = {}

    def _touch(bucket, dept, title, hc, w, field):
        k = key(title)
        meta.setdefault(k, {"bucket": bucket, "dept": dept, "title": title, "hc": hc})
        st = stats[k]
        st["w"].add(w["id"])
        st["t"][tier[w["id"]]] += 1
        st[field] += 1

    def touch(raw, w, field):
        bucket, dept, title, hc = resolver.resolve(raw)
        if bucket == "unc":
            parts = [p.strip() for p in re.split(r"\s*/\s*", raw) if p.strip()]
            if len(parts) > 1:
                resolved = [resolver.resolve(p) for p in parts]
                if all(r[0] != "unc" for r in resolved):
                    for r in resolved:
                        _touch(r[0], r[1], r[2], r[3], w, field)
                    return
        _touch(bucket, dept, title, hc, w, field)

    for w in wfs:
        touch(w["owner"], w, "own")
        for p in w["participants"]:
            touch(p, w, "part")
        for r in w["step_r"]:
            touch(r, w, "sr")
        for a in w["step_a"]:
            touch(a, w, "sa")

    rows = []
    for k, st in stats.items():
        m = meta[k]
        tmix = defaultdict(int)
        for wid in st["w"]:
            tmix[tier[wid]] += 1
        rows.append({"key": k, "title": m["title"], "bucket": m["bucket"],
                     "dept": m["dept"], "hc": m["hc"], "own": st["own"],
                     "part": st["part"], "sr": st["sr"], "sa": st["sa"],
                     "touched": len(st["w"]), "t1": tmix[1], "t2": tmix[2],
                     "t3": tmix[3]})
    dept_rank = {d: i for i, d in enumerate(dept_order)}
    rows.sort(key=lambda r: (["hq", "it", "store", "dc", "dept", "sys", "gov",
                              "wf", "ext", "unc"].index(r["bucket"]),
                             dept_rank.get(r["dept"], 99),
                             -r["own"], -r["touched"], r["title"].lower()))
    return wfs, tier, rows, dept_order


def esc(s):
    return s.replace("|", "\\|")


BUCKET_ORDER = ["hq", "it", "store", "dc", "dept", "sys", "gov", "wf", "ext", "unc"]


def render(wfs, tier, rows, dept_order):
    L = []
    a = L.append
    a("# BuildRight Depot Corp. — Role–Workflow Coverage Matrix (generated)")
    a("")
    a("> **Generated artifact — do not hand-edit.** Produced by")
    a("> [`../07-methodology/generate-role-coverage.py`](../07-methodology/generate-role-coverage.py)")
    a("> from the canonical registers: every PA file's Owner / Participants /")
    a("> Steps-table Role (R) / Role (A) fields (the workflow catalog's canonical")
    a("> RACI vocabulary), the criticality register's confirmed Tier assignment,")
    a("> and the official table of organization (§5.3 Enterprise Role Register,")
    a("> §7.2 store roster, §7.3 DC roster). Regenerate after any PA, role, or")
    a("> register change; `generate-role-coverage.py --check` byte-verifies this")
    a("> file. Resolution order: §5.3 register (incl. C-suite/role aliases) →")
    a("> §7.3/§7.2 field rosters → IT product-model seats → department-level")
    a("> actors → system actors → governance bodies → generic workforce →")
    a("> external counterparties → Uncharted watchlist (reported, never dropped).")
    a("> Cells that do not resolve whole are split on commas and slashes and the")
    a("> parts resolved individually; canonical titles containing slashes (e.g.")
    a("> Sustainability / ESG Manager) resolve whole first.")
    a("")
    t1 = sum(1 for v in tier.values() if v == 1)
    t2 = sum(1 for v in tier.values() if v == 2)
    t3 = sum(1 for v in tier.values() if v == 3)
    counts = defaultdict(int)
    for r in rows:
        counts[r["bucket"]] += 1
    a("## Summary")
    a("")
    a("| Measure | Value |")
    a("|---|---|")
    a(f"| Workflows mapped | {len(wfs)} (exactly one Owner each — asserted) |")
    a(f"| Confirmed Tier register | {len(tier)} rows (Tier 1: {t1} · Tier 2: {t2} · Tier 3: {t3}) |")
    a(f"| Distinct resolved actors | {len(rows)} — §5.3 register roles {counts['hq']} · IT product-model seats {counts['it']} · store field {counts['store']} · DC field {counts['dc']} · department-level actors {counts['dept']} · system actors {counts['sys']} · governance {counts['gov']} · workforce {counts['wf']} · external {counts['ext']} · uncharted {counts['unc']} |")
    a("")
    a("> Tier mix = confirmed tiers of the workflows a role touches (a workflow")
    a("> counts once per role regardless of how many steps mention it). HC is")
    a("> shown for §5.3 register roles; field rosters are per-store/per-DC and")
    a("> external/system actors carry no headcount by definition.")
    a("")

    labels = {
        "hq": "§5.3 Enterprise Role Register (HQ roles)",
        "it": "Information Technology product-model seats (§5.3 by reference)",
        "store": "Store field roles (§7.2 roster)",
        "dc": "DC field roles (§7.3 roster)",
        "dept": "Department-level actors (department or generic form named as performer)",
        "sys": "System & automated actors",
        "gov": "Governance bodies",
        "wf": "Generic workforce mentions",
        "ext": "External counterparties (not staff)",
        "unc": "Uncharted titles (vocabulary-drift watchlist)",
    }
    by_bucket = defaultdict(list)
    for r in rows:
        by_bucket[r["bucket"]].append(r)
    for b in BUCKET_ORDER:
        subset = by_bucket.get(b, [])
        if not subset:
            continue
        a(f"## {labels[b]}")
        a("")
        if b == "unc":
            top = subset[:60]
            tail = subset[60:]
            a(f"{len(subset)} distinct uncharted forms; the 60 with the widest workflow")
            a("coverage are listed — the remaining tail is aggregated below. This table")
            a("is the role-vocabulary drift watchlist: promote recurring forms into the")
            a("canonical vocabulary (or the alias tables) via the normal governance.")
            a("")
            a("| Form | Touched | T1 | T2 | T3 |")
            a("|---|---|---|---|---|")
            for r in top:
                a(f"| {esc(r['title'])} | {r['touched']} | {r['t1']} | {r['t2']} | {r['t3']} |")
            tw = sum(r["touched"] for r in tail)
            a("")
            a(f"Tail: {len(tail)} further forms, {tw} aggregated touches (each form")
            a("touches fewer workflows than the last row above).")
            a("")
            continue
        show_dept = b in ("hq", "it", "dept")
        header = "| Role | Dept / source | " + ("HC | " if b == "hq" else "") + \
                 "Owns | Participant | Step-R | Step-A | Touched | T1 | T2 | T3 |"
        a(header)
        a("|---|---|" + ("---|" if b == "hq" else "") + "---|---|---|---|---|---|---|---|")
        for r in subset:
            hc = str(r["hc"]) if b == "hq" and r["hc"] else "—"
            dept = re.sub(r"\s*\(\d+.*\)$", "", r["dept"]) if b in ("hq", "dept") else r["dept"]
            cells = [esc(r["title"]), esc(dept)]
            if b == "hq":
                cells.append(hc)
            cells += [str(r["own"]), str(r["part"]), str(r["sr"]), str(r["sa"]),
                      str(r["touched"]), str(r["t1"]), str(r["t2"]), str(r["t3"])]
            a("| " + " | ".join(cells) + " |")
        a("")
    return "\n".join(L) + "\n"


def census():
    """Owner-resolution census over the unique workflow catalog.

    Re-derives, every run, the numbers the role-vocabulary governance baseline
    is pinned against: how many workflows' Owner cells resolve through the
    resolution order (whole-string first, then the slash-part fallback — the
    same semantics as build()'s touch()), and the size of the uncharted
    watchlist. validate-repo.sh Check 71 pins these numbers, so any corpus,
    alias, register or resolver change that moves them forces a conscious
    re-adjudication with the baseline re-pointed (the Check-74 deferred-anchor
    pattern; armed by the 2026-09-15 thirty-first-wave review).
    """
    wfs, tier, rows, dept_order = build()
    hq, dc, store, dorder = parse_toc()
    res = Resolver(hq, dc, store, dorder)

    def owner_resolves(raw):
        b, _, _, _ = res.resolve(raw)
        if b != "unc":
            return True, [raw]
        parts = [p.strip() for p in re.split(r"\s*/\s*", raw) if p.strip()]
        if len(parts) > 1:
            rs = [res.resolve(p) for p in parts]
            if all(r[0] != "unc" for r in rs):
                return True, parts
        return False, [raw]

    resolved = uncharted = 0
    unc_owner_forms = set()
    for w in wfs:
        ok, forms = owner_resolves(w["owner"])
        if ok:
            resolved += 1
        else:
            uncharted += 1
            for f in forms:
                unc_owner_forms.add(norm(f))
    unc_rows = sum(1 for r in rows if r["bucket"] == "unc")
    print(f"CENSUS workflows={len(wfs)} owner_resolved={resolved} "
          f"owner_uncharted={uncharted} owner_uncharted_forms={len(unc_owner_forms)} "
          f"uncharted_forms={unc_rows}")
    return 0


def main():
    if "--census" in sys.argv:
        return census()
    wfs, tier, rows, dept_order = build()
    out = render(wfs, tier, rows, dept_order)
    if "--check" in sys.argv:
        if os.path.exists(OUT):
            shipped = open(OUT, encoding="utf-8").read()
            if shipped == out:
                print("role-coverage-matrix: byte-identical, OK")
                return 0
            import difflib
            diff = list(difflib.unified_diff(shipped.splitlines(), out.splitlines(),
                                             "shipped", "re-derived", lineterm=""))
            print(f"role-coverage-matrix DRIFT ({len(diff)} diff lines) — regenerate")
            for d in diff[:20]:
                print(d)
            return 1
        print("role-coverage-matrix missing — run without --check to generate")
        return 1
    open(OUT, "w", encoding="utf-8").write(out)
    by_bucket = defaultdict(int)
    for r in rows:
        by_bucket[r["bucket"]] += 1
    print(f"role-coverage-matrix written: {len(rows)} resolved actors over {len(wfs)} workflows "
          f"(hq {by_bucket['hq']} · it {by_bucket['it']} · store {by_bucket['store']} · dc {by_bucket['dc']} · "
          f"dept {by_bucket['dept']} · sys {by_bucket['sys']} · gov {by_bucket['gov']} · wf {by_bucket['wf']} · "
          f"ext {by_bucket['ext']} · uncharted {by_bucket['unc']})")
    unc = [r for r in rows if r["bucket"] == "unc"]
    if unc:
        print("top uncharted forms — extend ROLE_ALIASES/DEPT_ACTORS to promote them:")
        for r in sorted(unc, key=lambda r: -r["touched"])[:15]:
            print(f"  {r['touched']:4d} wf  {r['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
