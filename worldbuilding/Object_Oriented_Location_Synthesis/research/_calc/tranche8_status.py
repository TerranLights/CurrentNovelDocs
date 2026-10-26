#!/usr/bin/env python3
"""Status check for the eighth research tranche (harvesting whole planets; benefits of mining Mercury, Venus and the Sun). Run: python3 -I tranche6_status.py
Prints, per file: exists, lines, last write time, how many of the brief's nine sections are present, and whether it looks complete
(all nine sections present). A file with fewer than nine sections is INCOMPLETE: resume or re-dispatch it (see research/_dispatch_prompts_tranche8.md)."""
import os, re, time

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
FILES = [
    ("planet_deconstruction_literature_and_engineering.md", "ada2e82ab65f8eb25"),
    ("mercury_whole_planet_inventory_and_extraction.md", "ae15914eae03e12cd"),
    ("venus_whole_planet_inventory_and_stripping.md", "a2ecf6d6f2849ebd5"),
    ("planetary_scale_power_and_heat.md", "abf3ac0fdfcc1f65d"),
    ("orbital_dynamics_of_planetary_harvesting.md", "a186abe871ad95b1e"),
    ("oxygen_and_hydrogen_supply_for_mars_water.md", "a5f74ef2c7c54323a"),
    ("mars_water_budget_and_retention.md", "a1b59993142ff1681"),
    ("benefits_of_mining_mercury.md", "a101f849b761ae2d3"),
    ("benefits_of_mining_venus.md", "a8af1fb3e15f8a82a"),
    ("benefits_of_mining_the_sun.md", "aa11bbed6b5662e03"),
    ("value_and_markets_of_inner_system_materials.md", "a82428d79b97ad40c"),
]
SECTIONS = ["Scope", "SEARCH LOG", "Findings", "Conflicts", "Derived", "Constraints", "Candidate handwaves", "Open threads", "Rejected sources"]
print(f"now {time.strftime('%Y-%m-%d %H:%M')}")
for name, agent in FILES:
    p = os.path.join(R, name)
    if not os.path.isfile(p):
        print(f"MISSING     {name}  (agent {agent} from the 2026-10-11 evening dispatch; re-dispatch from _dispatch_prompts_tranche8.md)")
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
