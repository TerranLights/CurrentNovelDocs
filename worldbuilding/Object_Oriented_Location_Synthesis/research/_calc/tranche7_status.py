#!/usr/bin/env python3
"""Status check for the seventh research tranche (mining the inner Solar System). Run: python3 -I tranche6_status.py
Prints, per file: exists, lines, last write time, how many of the brief's nine sections are present, and whether it looks complete
(all nine sections present). A file with fewer than nine sections is INCOMPLETE: resume or re-dispatch it (see research/_dispatch_prompts_tranche7.md)."""
import os, re, time

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
FILES = [
    ("mercury_as_industrial_site.md", "a543e6c0bf845d3e0"),
    ("venus_as_extraction_site.md", "a4ba0930d3021fc25"),
    ("inner_system_logistics_network.md", "ab11524550f3db59b"),
]
SECTIONS = ["Scope", "SEARCH LOG", "Findings", "Conflicts", "Derived", "Constraints", "Candidate handwaves", "Open threads", "Rejected sources"]
print(f"now {time.strftime('%Y-%m-%d %H:%M')}")
for name, agent in FILES:
    p = os.path.join(R, name)
    if not os.path.isfile(p):
        print(f"MISSING     {name}  (agent {agent} from the 2026-10-11 evening dispatch; re-dispatch from _dispatch_prompts_tranche7.md)")
        continue
    txt = open(p, encoding="utf-8").read()
    lines = txt.count("\n") + 1
    heads = [l for l in txt.split("\n") if l.startswith("## ")]
    have = [s for s in SECTIONS if any(s.lower() in h.lower() for h in heads)]
    searches = len(re.findall(r"^\| (S|F|P|W)\d+ \|", txt, flags=re.M))
    mt = time.strftime("%H:%M", time.localtime(os.path.getmtime(p)))
    status = "COMPLETE?" if len(have) == 9 else "INCOMPLETE"
    print(f"{status:11s} {name}  {lines} lines, {len(have)}/9 sections, {searches} logged rows, last write {mt}")
    if len(have) < 9:
        print("            missing:", ", ".join(s for s in SECTIONS if s not in have))
