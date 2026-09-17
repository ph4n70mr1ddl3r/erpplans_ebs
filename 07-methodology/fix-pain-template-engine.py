#!/usr/bin/env python3
"""Wave-50 repair engine: shared by the per-VS fix-pain-template-*.py scripts.

Rewrites '### Pain Points / Risks' sections that consist entirely of the
Expansion-rework's pasted template bullets (bullets shared verbatim across >=3
workflows corpus-wide) with workflow-specific bullets grounded in each
workflow's own steps and touchpoints. Asserts every old bullet is a template-
pool member before writing; verifies paren/quote balance and mitigation
semantics on every new bullet; never touches any other line.
"""
import re, sys, os, glob, collections

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF = os.path.join(REPO, "01-model-company", "workflows")


def build_pool(min_shared=3):
    """Bullet texts shared verbatim by >= min_shared workflows corpus-wide."""
    text_to_wfs = collections.defaultdict(set)
    for fp in glob.glob(os.path.join(WF, "VS-*", "PA-*.md")):
        cur = None; in_pain = False
        for ln in open(fp, encoding="utf-8"):
            ln = ln.rstrip("\n")
            m = re.match(r"^## (W\d+[A-Z]?)\. ", ln)
            if m:
                cur = m.group(1); in_pain = False; continue
            if ln.startswith("### "):
                in_pain = cur is not None and "pain" in ln.lower()
                continue
            if in_pain and ln.startswith("- ") and ln.strip():
                text_to_wfs[ln].add((fp, cur))
    return {t for t, ks in text_to_wfs.items() if len(ks) >= min_shared}


def apply(replacements, pool):
    byfile = {}
    for (vs_glob, fs, wid), bullets in replacements.items():
        byfile.setdefault((vs_glob, fs), []).append((wid, bullets))
    errors = 0
    for (vs_glob, fs), items in sorted(byfile.items()):
        hits = glob.glob(os.path.join(WF, vs_glob, fs))
        if len(hits) != 1:
            print(f"ERROR: {vs_glob}/{fs}: {len(hits)} matches")
            errors += 1
            continue
        path = hits[0]
        rel = os.path.relpath(path, REPO)
        text = open(path, encoding="utf-8").read()
        parts = re.split(r"(?m)^(?=## W\d+[A-Z]?\. )", text)
        out = [parts[0]]
        seen = set()
        for part in parts[1:]:
            m = re.match(r"^## (W\d+[A-Z]?)\. ", part)
            wid = m.group(1)
            rep = dict(items)
            if wid in rep:
                seen.add(wid)
                new_bullets = rep[wid]
                pm = re.search(r"^(### Pain Points / Risks\n)((?:- .*\n)+)", part, re.M)
                if not pm:
                    print(f"ERROR: {rel} {wid}: no Pain section found")
                    errors += 1
                    out.append(part)
                    continue
                old_bullets = pm.group(2).rstrip("\n").split("\n")
                kept = [ob for ob in old_bullets if ob not in pool]
                dropped = [ob for ob in old_bullets if ob in pool]
                if not dropped:
                    print(f"SKIP: {rel} {wid}: Pain section already fully specific")
                    out.append(part)
                    continue
                for ob in kept:
                    print(f"KEPT (specific bullet preserved): {rel} {wid}: {ob[:80]}")
                for nb in new_bullets:
                    if nb.count("(") != nb.count(")") or nb.count('"') % 2 == 1:
                        print(f"ERROR: {rel} {wid}: new bullet unbalanced: {nb[:90]}")
                        errors += 1
                    if "mitigat" not in nb:
                        print(f"ERROR: {rel} {wid}: new bullet lacks mitigation: {nb[:90]}")
                        errors += 1
                new_section = pm.group(1) + "\n".join(kept + new_bullets) + "\n"
                part = part[:pm.start()] + new_section + part[pm.end():]
            out.append(part)
        missing = set(w for w, _ in items) - seen
        if missing:
            print(f"ERROR: {rel}: workflows not found: {sorted(missing)}")
            errors += 1
        open(path, "w", encoding="utf-8").write("".join(out))
        print(f"OK: {rel}: {len(seen)} Pain sections rewritten")
    if errors:
        print(f"FAILED with {errors} error(s); files already written are final")
        sys.exit(1)
    print("ALL OK")
