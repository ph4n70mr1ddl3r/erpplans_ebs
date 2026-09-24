#!/usr/bin/env python3
"""production-volume-of-record.py — standing volume-of-record instrument.

Makes the actual operator's production EBS (CitiHardware PROD, R12.2.4 — the
estate the model company mirrors) the data of record for the model company's
operating volumes, per direction ("make ~/access_ebs our model since that's
realistic and actual"). One-off read-outs (the 2026-06 reports, the 2026-07-30
POS probe, the 2026-09-23 data-volumes §1.1 calibration) become a re-derivable
register: --refresh queries PROD read-only and rewrites both the JSON cache and
the generated register; --check re-renders the register from the committed
cache in memory and byte-compares the shipped file (validator Check 81), so the
register can never drift from its extraction of record.

Credentials never live in this repository: they come from the environment
(EBSV_DSN / EBSV_USER / EBSV_PASS) or are parsed from the operator's own access
notes (ACCESS_EBS_HOME/access.txt, default ~/access_ebs/access.txt) — the
fifty-fifth-wave rule that retired the hardcoded VM password, applied to the
database route.

This instrument changes NO model-company canon. §4 of the register is the
calibration surface: every canon-vs-actual delta is an explicit decision (the
W5580 governance, executive direction), never an automatic re-base.

Usage:
  python3 production-volume-of-record.py --refresh   # live query, rewrite cache + register
  python3 production-volume-of-record.py --check     # offline byte-verify (validator Check 81)
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")
CACHE = os.path.join(REPO, "07-methodology", "production-volume-of-record-cache.json")
REGISTER = os.path.join(MC, "production-volume-of-record.md")
ACCESS_EBS_HOME = os.environ.get("ACCESS_EBS_HOME", os.path.join(os.path.expanduser("~"), "access_ebs"))
CALL_TIMEOUT_MS = 180000

# ---------------------------------------------------------------- credentials

def _creds_from_access_notes():
    path = os.path.join(ACCESS_EBS_HOME, "access.txt")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8", errors="replace").read()

    def grab(label):
        m = re.search(r"^\s*" + label + r"\s*:\s*(\S+)", text, re.M | re.I)
        return m.group(1) if m else None

    host, port, sid = grab("hostname/ip"), grab("port"), grab("sid")
    user, pw = grab("user"), grab("pass")
    if not (host and port and sid and user and pw):
        return None
    return f"{host}:{port}/{sid}", user, pw


def credentials():
    dsn, user, pw = (os.environ.get("EBSV_DSN"), os.environ.get("EBSV_USER"),
                     os.environ.get("EBSV_PASS"))
    if dsn and user and pw:
        return dsn, user, pw
    got = _creds_from_access_notes()
    if got:
        return got
    sys.exit("error: no credentials — set EBSV_DSN/EBSV_USER/EBSV_PASS or provide "
             f"{ACCESS_EBS_HOME}/access.txt (never commit credentials)")


def connect():
    try:
        import oracledb
    except ImportError:
        sys.exit("error: --refresh needs the oracledb package (python3 -m pip install oracledb)")
    # The PROD server's password verifier (0x939) needs python-oracledb thick mode;
    # the operator's instant client is at /opt/oracle/instantclient (env-overridable).
    client = os.environ.get("EBSV_CLIENT", "/opt/oracle/instantclient")
    if os.path.isdir(client):
        oracledb.init_oracle_client(lib_dir=client)
    dsn, user, pw = credentials()
    con = oracledb.connect(user=user, password=pw, dsn=dsn)
    con.call_timeout = CALL_TIMEOUT_MS
    return con

# ---------------------------------------------------------------- query set
# Each query is cheap (12-month windows / small tables) and read-only. A query
# that times out or errors degrades to status "timeout"/"error" — the register
# renders it as unavailable and lists it in §6; --check stays deterministic.

QUERIES = [
    ("pos_trx_12m", "POS transactions (headers), trailing 12 mo",
     "SELECT COUNT(*) FROM osipos.osipos_trx_header WHERE trx_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("pos_stores_12m", "POS-active stores (distinct STORE_ID), last 7 days",
     "SELECT COUNT(DISTINCT store_id) FROM osipos.osipos_trx_header WHERE trx_date >= TRUNC(SYSDATE)-7"),
    ("po_docs_12m", "Purchase orders, trailing 12 mo",
     "SELECT COUNT(*) FROM po_headers_all WHERE creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("po_lines_12m", "PO lines, trailing 12 mo",
     "SELECT COUNT(*) FROM po_lines_all WHERE creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("sto_docs_12m", "Inter-branch transfer orders (STROO), trailing 12 mo",
     "SELECT COUNT(*) FROM oe_order_headers_all WHERE creation_date >= ADD_MONTHS(SYSDATE,-12) "
     "AND order_type_id IN (SELECT transaction_type_id FROM oe_transaction_types_tl WHERE name LIKE 'STROO%')"),
    ("om_lines_12m", "OM order lines (all order types), trailing 12 mo",
     "SELECT COUNT(*) FROM oe_order_lines_all WHERE creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("ap_invoices_12m", "AP supplier invoices, trailing 12 mo",
     "SELECT COUNT(*) FROM ap_invoices_all WHERE creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("ar_cm_12m", "AR credit memos (the returns instrument), trailing 12 mo",
     "SELECT COUNT(*) FROM ra_customer_trx_all t, ra_cust_trx_types_all tt "
     "WHERE t.cust_trx_type_id = tt.cust_trx_type_id AND tt.type = 'CM' "
     "AND t.creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("rcv_lines_12m", "PO receipt transaction lines, trailing 12 mo",
     "SELECT COUNT(*) FROM rcv_transactions WHERE transaction_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("gl_je_12m", "GL journal batches, trailing 12 mo",
     "SELECT COUNT(*) FROM gl_je_headers WHERE creation_date >= ADD_MONTHS(SYSDATE,-12)"),
    ("inv_orgs", "Inventory organizations",
     "SELECT COUNT(*) FROM org_organization_definitions"),
    ("legal_entities", "Distinct legal entities (inventory-org view)",
     "SELECT COUNT(DISTINCT legal_entity) FROM org_organization_definitions"),
    ("suppliers_total", "Suppliers on the master",
     "SELECT COUNT(*) FROM po_vendors"),
    ("suppliers_active", "Suppliers active (end_date_active open or future)",
     "SELECT COUNT(*) FROM po_vendors WHERE end_date_active IS NULL OR end_date_active >= SYSDATE"),
    ("users_active", "EBS accounts active (no end date)",
     "SELECT COUNT(*) FROM fnd_user WHERE end_date IS NULL"),
    ("users_30d", "EBS accounts logged in within 30 days",
     "SELECT COUNT(*) FROM fnd_user WHERE last_logon_date >= SYSDATE-30"),
    ("items_defined", "Distinct items defined in the item master",
     "SELECT COUNT(DISTINCT inventory_item_id) FROM mtl_system_items_b"),
    ("items_onhand", "Distinct items with on-hand inventory",
     "SELECT COUNT(DISTINCT inventory_item_id) FROM mtl_onhand_quantities_detail"),
    ("categories_top", "Top item catalog groups, by distinct items",
     "SELECT g.segment1, g.description, COUNT(DISTINCT i.inventory_item_id) n "
     "FROM mtl_system_items_b i, mtl_item_catalog_groups_b g "
     "WHERE i.item_catalog_group_id = g.item_catalog_group_id "
     "GROUP BY g.segment1, g.description ORDER BY n DESC FETCH FIRST 12 ROWS ONLY"),
]

# ---------------------------------------------------------------- canon
# The model-company figures this register calibrates against. Sources are the
# documents of record; a canon change is a deliberate repo edit HERE plus the
# governed document change — never the reverse.

CANON = [
    ("Stores", "200", "root README At-a-Glance; data-volumes §1.1 mirrors the operator"),
    ("POS receipts per store per day (design target)", "467 (93,333/day ÷ 200 stores)", "root README 14,000/store/month"),
    ("Purchase orders per month", "1,650–1,950 (55–65/day)", "root README; data-volumes §1.1 calibrated"),
    ("Replenishment transfers per month", "~50,000 (~250/store, ~1,700/day)", "data-volumes §1.1 calibrated"),
    ("Customer returns (AR credit memos) per month", "~1,200 (~40/day)", "data-volumes §1.1 calibrated"),
    ("Active SKUs", "35,000", "root README At-a-Glance"),
    ("Item master (distinct items)", "~55,000", "profile §10.2 item-master basis"),
    ("Legal entities", "5", "ebs-platform-architecture (5 legal entities · 205 inventory orgs)"),
    ("Inventory organizations", "205", "ebs-platform-architecture"),
    ("Suppliers on the master", "—", "no model-company canon figure"),
    ("EBS application users", "—", "no model-company canon figure"),
]


def _fmt(n):
    return f"{n:,}" if isinstance(n, int) else str(n)


def render(cache):
    ts = cache["extracted_at"]
    m = cache["metrics"]
    cats = m.get("categories_top", {})
    rows_cat = cats.get("value") or []

    def val(key):
        e = m.get(key, {})
        return _fmt(e["value"]) if e.get("status") == "ok" and e.get("value") is not None else "— (unavailable this run)"

    lines = []
    A = lines.append
    A("# Production Volume of Record — the actual operator's PROD (generated)")
    A("")
    A(f"> **Generated** by [`production-volume-of-record.py`](../07-methodology/production-volume-of-record.py)"
      f" `--refresh` on **{ts}** — read-only `appsro` against the production Active Data Guard"
      f" standby. **This file is generated — do not hand-edit.** Validator Check 81 runs the"
      f" instrument's `--check` mode: the register is re-rendered from the committed JSON cache"
      f" (`production-volume-of-record-cache.json`) and byte-compared, so it cannot drift from its"
      f" extraction of record. The instrument carries **no credentials** — they come from the"
      f" environment or the operator's own access notes outside this repository. This register"
      f" changes **no** model-company canon: every §4 delta is an explicit decision (W5580"
      f" governance, executive direction), never an automatic re-base.")
    A("")
    A("## §1 Operating volumes — trailing 12 months, measured live")
    A("")
    A("| Metric | Actual (12 mo) |")
    A("|---|---|")
    A(f"| POS transactions (headers) | {val('pos_trx_12m')} |")
    A(f"| POS-active stores (last 7 days) | {val('pos_stores_12m')} |")
    A(f"| Purchase orders | {val('po_docs_12m')} |")
    A(f"| PO lines | {val('po_lines_12m')} |")
    A(f"| Inter-branch transfer orders (STROO) | {val('sto_docs_12m')} |")
    A(f"| OM order lines (all types) | {val('om_lines_12m')} |")
    A(f"| AP supplier invoices | {val('ap_invoices_12m')} |")
    A(f"| AR credit memos (returns instrument) | {val('ar_cm_12m')} |")
    A(f"| PO receipt lines | {val('rcv_lines_12m')} |")
    A(f"| GL journal batches | {val('gl_je_12m')} |")
    A("")
    A("## §2 Structure & estate")
    A("")
    A("| Metric | Actual |")
    A("|---|---|")
    A(f"| Legal entities (inventory-org view) | {val('legal_entities')} |")
    A(f"| Inventory organizations | {val('inv_orgs')} |")
    A(f"| Suppliers total / active | {val('suppliers_total')} / {val('suppliers_active')} |")
    A(f"| EBS accounts active / logged-in 30d | {val('users_active')} / {val('users_30d')} |")
    A("")
    A("## §3 Masterfiles")
    A("")
    A(f"- Items defined in the item master: **{val('items_defined')}**")
    A(f"- Items with on-hand inventory: **{val('items_onhand')}**")
    A(f"- POS-active stores (distinct STORE_ID, last 7 days): **{val('pos_stores_12m')}**")
    if rows_cat:
        A(f"- Top item catalog groups (by distinct items): " +
          "; ".join(f"{c[0]} {c[1]} ({_fmt(c[2])})" for c in rows_cat))
    elif m.get("categories_top", {}).get("status") == "ok":
        A("- Top item catalog groups: none maintained on the item master (catalog groups "
          "unused — the operator's item taxonomy, if any, lives in item categories)")
    else:
        A("- Top item catalog groups: — (unavailable this run)")
    A("")
    A("## §4 Calibration surface — model-company canon vs production actual")
    A("")
    A("| Parameter | Model-company canon (source) | Production actual | Reading |")
    A("|---|---|---|---|")

    def num(key):
        e = m.get(key, {})
        return e.get("value") if e.get("status") == "ok" else None

    pos, stores = num("pos_trx_12m"), num("pos_stores_12m")
    per_store_day = (pos / 12.0 / 30.44 / stores) if (pos and stores) else None
    po, sto, cm = num("po_docs_12m"), num("sto_docs_12m"), num("ar_cm_12m")

    def f1(x):
        return f"{x:,.1f}" if x is not None else "—"

    A("| Stores | 200 (root README; data-volumes §1.1 mirrors the operator) | "
      f"{val('pos_stores_12m')} POS-active (§2 inventory orgs {val('inv_orgs')}) | "
      "OPEN — reconcile the 171-store calibration basis (data-volumes v4.7) vs the ~232-store audit figure vs the live POS-active count |")
    A(f"| POS receipts per store per day (design target 467 = 93,333/day ÷ 200) | 467 | "
      + (f"≈ {f1(per_store_day)} (12-mo POS ÷ stores ÷ days)" if per_store_day else "—") +
      " | OPEN — the 2026-07-30 probe measured 126–510/store/day, mean ~330; decide target-vs-measured |")
    A("| Purchase orders per month (canon 1,650–1,950) | 1,650–1,950 | "
      + (f"≈ {_fmt(round(po / 12))}" if po else "—") + " | CONFIRMED if within band — the §1.1 calibration held |")
    A("| Replenishment transfers per month (canon ~50,000) | ~50,000 | "
      + (f"≈ {_fmt(round(sto / 12))}" if sto else "—") + " | CONFIRMED if ~250/store on the live store count |")
    A("| Customer returns AR credit memos per month (canon ~1,200) | ~1,200 | "
      + (f"≈ {_fmt(round(cm / 12))}" if cm else "—") + " | CONFIRMED if within band |")
    A(f"| Active SKUs | 35,000 | {val('items_onhand')} items with on-hand | OPEN — near-canon if within ±15% |")
    A(f"| Item master | ~55,000 | {val('items_defined')} defined | OPEN — the operator runs ~2x the modeled master |")
    A(f"| Legal entities | 5 (ebs-platform-architecture) | {val('legal_entities')} | BY DESIGN — the model company consolidates; the operator runs 15 entity books |")
    A(f"| Inventory organizations | 205 | {val('inv_orgs')} | BY DESIGN — re-base only with the store/DC estate decision |")
    A(f"| Suppliers on the master | — | {val('suppliers_total')} total / {val('suppliers_active')} active | NEW BASIS — adopt as the supplier-master scale when the P2P docs are next revised |")
    A(f"| EBS application users | — | {val('users_active')} active / {val('users_30d')} 30-day logins | NEW BASIS — the licensing-BOM user driver grounds here |")
    A("")
    A("## §5 Decision register")
    A("")
    A("1. **Store-count basis** — one number of record for the mirrored estate (the §1.1")
    A("   calibration used 171; the capability audit says ~232; §2 is the live POS-active")
    A("   count). Re-point data-volumes §1.1, the profile and the TO store math to it in one")
    A("   governed pass.")
    A("2. **POS design target** — keep the 467/store/day planning canon (top of the measured")
    A("   band) or re-base to the measured mean; either way, state the choice once, here and")
    A("   in data-volumes §1.1, not per-document.")
    A("3. **Entity posture** — the model company's 5-entity consolidation is a design choice")
    A("   against the operator's 15 books; confirm it stays a design choice as the fit-gap")
    A("   and ledger-model docs evolve.")
    A("4. **Masterfile scale** — the ~55,000 item-master canon and the supplier-master")
    A("   vacuum: adopt §3 actuals as the P2P/master-data planning basis at the next")
    A("   revision of the docs that quote them.")
    A("5. **Role-load reliability** — the load model's cadence layer graduates from prose")
    A("   parsing (53% coverage) to this register: per-workflow-event cadences ground on the")
    A("   measured 12-month volumes above before any headcount optimization is taken.")
    A("")
    A("## §6 Method & freshness")
    A("")
    A(f"- Extracted: **{ts}**; query window: trailing 12 months from the database SYSDATE.")
    A("- Route: read-only `appsro` on the Active Data Guard standby (the operator's own")
    A("  access route; credentials via environment or ACCESS_EBS_HOME notes — never committed).")
    A("- Timeout/error queries degrade to '—' here and are listed in the cache with their")
    A("  status; `--refresh` re-attempts everything. Prior published sources: the 2026-06")
    A("  reports and the 2026-07-30 POS probe under the operator's access_ebs folder.")
    A("- Pinned by validate-repo.sh **Check 81** (`--check` byte-verify from the committed")
    A("  cache). Refresh cadence: monthly, or before any calibration decision.")
    A("")
    A(f"*Generated {ts} by production-volume-of-record.py — do not hand-edit.*")
    return "\n".join(lines) + "\n"


def refresh():
    con = connect()
    cur = con.cursor()
    metrics = {}
    for key, _label, sql in QUERIES:
        entry = {"status": "ok", "value": None}
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            entry["value"] = [[r[0], int(r[1])] for r in rows] if key == "categories_top" else int(rows[0][0])
        except Exception as e:  # noqa: BLE001 — degrade, never abort the register
            entry = {"status": "error", "value": None, "detail": str(e).split("\n")[0][:200]}
        metrics[key] = entry
        print(f"  {key:18} {entry['status']:7} {_fmt(entry['value']) if entry['status'] == 'ok' else entry.get('detail', '')}")
    cur.close()
    con.close()
    cache = {"extracted_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
             "metrics": metrics}
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), indent=1, sort_keys=True)
    open(REGISTER, "w", encoding="utf-8").write(render(cache))
    print(f"cache -> {CACHE}")
    print(f"register -> {REGISTER}")


def check():
    if not (os.path.exists(CACHE) and os.path.exists(REGISTER)):
        print("production-volume-of-record: cache or register missing")
        return 1
    rendered = render(json.load(open(CACHE, encoding="utf-8")))
    shipped = open(REGISTER, encoding="utf-8").read()
    if rendered == shipped:
        print("production-volume-of-record: register byte-identical to the cache re-render, OK")
        return 0
    shipped_lines, rendered_lines = shipped.splitlines(), rendered.splitlines()
    diff = [f"  line {i + 1}: shipped   {shipped_lines[i][:100] if i < len(shipped_lines) else '<missing>'}"
            for i in range(max(len(shipped_lines), len(rendered_lines)))
            if i >= len(shipped_lines) or i >= len(rendered_lines) or shipped_lines[i] != rendered_lines[i]][:10]
    print("production-volume-of-record: register does NOT match the cache re-render")
    print("\n".join(diff))
    return 1


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--refresh", action="store_true", help="live PROD query; rewrite cache + register")
    g.add_argument("--check", action="store_true", help="offline byte-verify register vs cache (Check 81)")
    args = ap.parse_args()
    if args.refresh:
        refresh()
        return 0
    return check()


if __name__ == "__main__":
    sys.exit(main())
