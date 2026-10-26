#!/usr/bin/env python3
"""Status check for the sixth research tranche (starlifting and the industrial chain). Run: python3 -I tranche6_status.py
Prints, per file: exists, lines, last write time, how many of the brief's nine sections are present, and whether it looks complete
(all nine sections present). A file with fewer than nine sections is INCOMPLETE: resume or re-dispatch it (see research/_dispatch_prompts_tranche6.md)."""
import os, re, time

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
FILES = [
    ("starlifting_physics_and_minimum_infrastructure.md", "a018afb0c3905cd6e"),
    ("space_trucking_and_transport_infrastructure.md", "a3087c9acfbd6473d"),
    ("space_processing_and_fabrication.md", "acd0b43fb3bcffbf0"),
    ("industrial_ramp_timelines.md", "a721724ab45263369"),
    ("cyclers_and_large_slow_vehicles.md", "a6141bb61a43c43a8"),
]
SECTIONS = ["Scope", "SEARCH LOG", "Findings", "Conflicts", "Derived", "Constraints", "Candidate handwaves", "Open threads", "Rejected sources"]
print(f"now {time.strftime('%Y-%m-%d %H:%M')}")
for name, agent in FILES:
    p = os.path.join(R, name)
    if not os.path.isfile(p):
        print(f"MISSING     {name}  (agent {agent} from the 2026-10-11 session; re-dispatch from _dispatch_prompts_tranche6.md)")
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
