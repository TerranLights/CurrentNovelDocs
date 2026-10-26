#!/usr/bin/env python3
"""Arithmetic for research/canon_vs_physics_comparison.md (OOLSD, 2026-10-12). Run: python3 -I canon_comparison_calc.py
Canon inputs (K-ids) come from research/_canon_extract_interplanetary.md. Physics inputs come from the tranche-6/7/8 syntheses and their source files, keyed in comments:
[SYN]=starlifting_synthesis.md, [IMS]=inner_system_mining_synthesis.md, [PHB]=planetary_harvesting_and_benefits_synthesis.md, [PR]=space_processing_and_fabrication.md,
[TR]=space_trucking_and_transport_infrastructure.md, [LEO]=leo_and_orbital_habitats.md. Nothing is fitted; no canon is edited."""
import math

def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)

YR = 3.15576e7
pop = 10_104_964                       # K-18 canon orbital population (combined)

hdr("1. MASS TO HOUSE THE CANON ORBITAL POPULATION (K-18) AT SOURCED MASS-PER-PERSON FIGURES")
rows = [
    ("canon OMB low-shield LEO 'debris-built' (10-20 t/person)", 10.0, 20.0, "K-8 / OMB s6: 'as low as ~10-20 tonnes/person'"),
    ("SP-413 O'Neill-type cylinder (80.2 Mt / 820,000 people)", 80.2e6 / 820_000, 80.2e6 / 820_000, "[PR] 6 (SP-413 Table 4-1), L5-type site"),
    ("canon OMB working estimate (1-10 Mt for 10,000-20,000 residents)", 1e6 / 20_000, 10e6 / 10_000, "K-7 / OMB s2"),
    ("SP-413 torus (10.09 Mt / 10,000 people)", 10.09e6 / 10_000, 10.09e6 / 10_000, "[PR] 6"),
    ("Kalpana One (7 Mt / 3,000 people)", 7e6 / 3_000, 7e6 / 3_000, "K-7 / OMB s2"),
]
for name, lo, hi, src in rows:
    print(f"{name:<72} {lo:>8,.1f}-{hi:>8,.1f} t/person -> {pop*lo/1e6:>10,.0f}-{pop*hi/1e6:>10,.0f} Mt  ({pop*lo/1e9:.2f}-{pop*hi/1e9:.2f} Gt)   [{src}]")
print(f"canon debris ceiling for comparison: 16,200 t (K-8) = {16200/ (pop*10) :.2e} of the lowest figure above")
print("(real mass in orbit end-2025: 16,185 t [TR F3, McDowell]; matches the ESA figure canon uses)")

hdr("2. HOW LONG TO SUPPLY THAT MASS, FROM CANON'S DATES")
t_staging = 2340.0           # K-1 'mid-2300s' (approximate)
t_tower = 2688.0             # K-11
t_war = 2812.0               # K-11
print(f"staging stations ~{t_staging:.0f} to the war {t_war:.0f}: {t_war-t_staging:.0f} yr; Tower completion to the war: {t_war-t_tower:.0f} yr")
for mass_gt in (0.1, 1.0, 10.0, 24.0):
    for window, label in ((t_war - t_staging, "staging to war"), (t_war - t_tower, "Tower era only")):
        flow = mass_gt * 1e9 / window            # t/yr
        print(f"{mass_gt:>5.1f} Gt over {window:>4.0f} yr ({label:<15}): average {flow/1e6:>7.2f} Mt/yr = {flow*1e3/YR:>7.3f} t/s")
print("physics anchors: world launched mass 3,194 t/yr (2025) [TR F3]; one lunar launcher design 0.65 Mt/yr (SP-428); stage-C shield flow 1.2 Mt/yr (SP-413) [SYN 5]")

hdr("3. EXPONENTIAL REACH FROM 1.2 Mt/yr (SYN stage C) AT ONE DOUBLING PER 2 YEARS (the fast reading; a handwave if it persists: C-65)")
r0, dbl = 1.2, 2.0                                     # Mt/yr, years
k = math.log(2) / dbl
for target_gt in (0.1, 1.0, 10.0, 24.0):
    need = target_gt * 1000.0                          # Mt cumulative
    t = math.log(need * k / r0 + 1) / k
    print(f"cumulative {target_gt:>5.1f} Gt: {t:>5.1f} yr after the 1.2 Mt/yr stage; flow then = {r0*math.exp(k*t):>8.1f} Mt/yr")
print("stage-C reach from commitment (fast reading) = 8.2-13.5 + 6.6-13.3 + 5.8-11.7 + 4.5-9.7 =", round(8.2+6.6+5.8+4.5, 1), "-", round(13.5+13.3+11.7+9.7, 1), "yr [SYN calc 5]")

hdr("4. WHERE THE FAST AND SLOW READINGS PLACE THE MILESTONES IF 'COMMITMENT' IS HANA JINN'S RECRUITMENT (K-2: after 2318, early-to-mid 2300s)")
for c0 in (2318, 2330, 2340):
    print(f"commitment {c0}: first hardware {c0+8.2:.0f}-{c0+13.5:.0f}; Mt/yr-class industry {c0+25:.0f}-{c0+48:.0f}; first ~10 Mt torus (fast, sequential) {c0+33:.0f}-{c0+56:.0f}; (slow bound) {c0+128:.0f}-{c0+133:.0f}")
print("canon: Mallory Dufay 'oversaw the actual first orbital launches ... mid-2300s' (K-3): gap Hana->Mallory must be >= 8.2-13.5 yr for the physics-based first-hardware lead")

hdr("5. THE TOWER AS A BULK EXPORT CHANNEL (K-12, K-14)")
e_leo = 33.1e6                         # J/kg Earth surface to 400 km orbit, ideal [TR D5]
net_gw = 324.0                         # K-12
pellet = 270.0                         # t/s circulating loop, not payload (K-12)
for flow_mt in (1.0, 8.0, 82.0, 190.0):
    p = flow_mt * 1e9 * e_leo / YR / 1e9
    print(f"payload {flow_mt:>6.1f} Mt/yr = {flow_mt*1e9/YR:>7.2f} kg/s ... ideal lift energy {p:>7.2f} GW = {p/net_gw*100:>5.1f} % of the Tower's 324 GW net draw; {flow_mt*1e6/YR/pellet*100:.3f} % of the 270 t/s pellet loop by mass")
g0, isp, dv = 9.80665, 452.3, 7820.0   # RS-25 vacuum Isp [TR F2]; K-12 'about 7.82 km/s orbital velocity needed'
mr = math.exp(dv / (g0 * isp))
print(f"final-stage rocket for {dv/1e3:.2f} km/s at Isp {isp} s: mass ratio {mr:.2f}, propellant {100*(1-1/mr):.1f} % of departing mass, {mr-1:.2f} t propellant per t of (payload + dry mass) [rocket equation]")
print(f"Tower draw vs world solar capacity end-2025 (2,397 GW [RM F1]): {net_gw/2397*100:.1f} %")
print("South Pole site: no rotational speed boost; every Tower launch starts toward a polar orbit (standard geometry; not researched in the tranches: open thread)")

hdr("6. POPULATION MOVED BY THE TOWER (K-16): CANON ARITHMETIC CHECK")
for people, years in ((10_104_964, 124), (10_104_964, 178), (12_000_000, 124)):
    print(f"{people:,} people over {years} yr = {people/years/8766:.2f} per hour (canon: 9.30/h for 124 yr, 6.48/h for 178 yr)")
print(f"design capacity 194/h x 8766 h x 124 yr = {194*8766*124/1e6:.0f} million (canon: ~204 million over 120 yr: {194*8766*120/1e6:.0f} million)")

hdr("7. MARS AND VENUS DATES FROM PHYSICS (earliest, if commitment is not earlier than the Second Interwar start 2564)")
for c0 in (2564, 2600, 2688):
    print(f"commitment {c0}: first Mars landing {c0+8.2:.0f}-{c0+13.5:.0f}; ~110 people at the survival minimum {c0+17:.0f}-{c0+39:.0f}; M5 million people (claim) {c0+43:.0f}-{c0+107:.0f}")
print("Helix opening 3012-3112 minus game present 2822-2827 =", 3012-2827, "to", 3112-2822, "yr")
print("Venus cloud-deck habitat: 0.9 g, ~1 bar at 50-55 km [IMS 3.2 / BVE]; bulk export 180-670 kt lifted per kt delivered [IMS 4]")
