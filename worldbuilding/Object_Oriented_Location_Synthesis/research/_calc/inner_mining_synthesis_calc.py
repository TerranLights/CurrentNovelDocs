#!/usr/bin/env python3
"""Arithmetic behind research/inner_system_mining_synthesis.md (OOLSD, 2026-10-11). Run: python3 -I inner_mining_synthesis_calc.py
Inputs are figures sourced in the tranche-6 and tranche-7 files; keys: [ME]=mercury_as_industrial_site.md [VE]=venus_as_extraction_site.md
[NW]=inner_system_logistics_network.md [TR]=space_trucking_and_transport_infrastructure.md [SL]=starlifting_physics_and_minimum_infrastructure.md
[PR]=space_processing_and_fabrication.md [ML]=moon_lagrange_and_comparables.md (via [SL] 3F). Nothing here is read from canon."""
import math

def hdr(s):
    print("\n" + "=" * 96 + "\n" + s + "\n" + "=" * 96)

hdr("1. IRON PER TONNE OF MATERIAL, BY SOURCE")
fe_mercury = (13.0, 19.0)                 # [ME] D1 / F10: kg Fe per tonne of average regolith
fe_mare = (140.0, 170.0)                  # [SL] 3F (via ML): mare Fe 14-17 wt%, mostly in silicates and ilmenite
fe_ci = 182.8                             # [PR] 3: CI chondrite Fe 18.28 wt% (Lodders 2003)
fe_sun = 1000.0 / 841.0                   # [SL] 3B: 841 t photosphere per t Fe -> kg Fe per tonne
print(f"Mercury surface: {fe_mercury[0]:.0f}-{fe_mercury[1]:.0f} kg Fe/t  -> {1000/fe_mercury[1]:.0f}-{1000/fe_mercury[0]:.0f} t of regolith per t of iron")
print(f"Lunar mare: {fe_mare[0]:.0f}-{fe_mare[1]:.0f} kg Fe/t (mostly in silicates and ilmenite, not metal): {fe_mare[0]/fe_mercury[1]:.1f}-{fe_mare[1]/fe_mercury[0]:.1f} x Mercury's")
print(f"CI carbonaceous chondrite: {fe_ci:.0f} kg Fe/t: {fe_ci/fe_mercury[1]:.1f}-{fe_ci/fe_mercury[0]:.1f} x Mercury's")
print(f"Sun photosphere: {fe_sun:.2f} kg Fe/t = {fe_mercury[0]/fe_sun:.0f}-{fe_mercury[1]/fe_sun:.0f} x poorer than Mercury's surface in iron by mass")
print("(grades are not recoverability: Mercury's iron is partly sulfide; lunar iron is mostly in silicates; CI iron is largely oxide/sulfide; native-metal grades: Moon ~0.5 wt% [SL 3F], average meteorite ~20 % free metal [PR 1b])")

hdr("2. WHAT A 1 Mt/yr OF IRON FROM MERCURY'S SURFACE WOULD MEAN")
for flow_t in (1e3, 1e5, 1e6):
    lo, hi = flow_t * 1000 / fe_mercury[1], flow_t * 1000 / fe_mercury[0]
    print(f"{flow_t:>9,.0f} t Fe/yr -> {lo/1e6:>8.2f}-{hi/1e6:>8.2f} Mt/yr of regolith processed")
rho = 1660.0                               # kg/m3, LUNAR regolith (Crawford, in [VE] 3.2): an ASSUMED analog, no Mercury density was measured [ME] F3
depth = 4.6                                # m, median regolith thickness [ME] F3 (disputed: 3.7-4.6 m vs 25-40 m)
areal = rho * depth / 1000.0               # t per m2
for flow_t in (1e3, 1e5, 1e6):
    lo, hi = flow_t * 1000 / fe_mercury[1], flow_t * 1000 / fe_mercury[0]   # tonnes of regolith per year
    print(f"{flow_t:>9,.0f} t Fe/yr: stripping to {depth} m at an assumed {rho:.0f} kg/m3 = {areal:.1f} t/m2 -> {lo/areal/1e6:.3f}-{hi/areal/1e6:.3f} km2 per year")
print("co-products per tonne of regolith [ME] D1: Si 250, Mg 110, Al 67, Ca 40-60, Na 29, S 19-23, C 14 kg")
lo, hi = 1e6 * 1000 / fe_mercury[1] / 1e3, 1e6 * 1000 / fe_mercury[0] / 1e3
print(f"at 1 Mt Fe/yr: Mg {lo*0.110/1e3:.1f}-{hi*0.110/1e3:.1f} Mt/yr, Si {lo*0.250/1e3:.1f}-{hi*0.250/1e3:.1f} Mt/yr, Al {lo*0.067/1e3:.1f}-{hi*0.067/1e3:.1f} Mt/yr as unavoidable co-products (Mt = 1e6 t)")
print(f"escape energy of the iron alone if launched as metal: 1 t Fe = 9.03e9 J; 1 Mt/yr = {9.03e9*1e6/3.15576e7/1e6:.0f} MW of jet power at 100 % [NW F6(b): 286 MW]")

hdr("3. ENERGY AND DELTA-V TO REACH EARTH ORBIT, BY SOURCE (from low orbit or surface; ideal; [TR] D1, [NW] F2)")
rows = [("Moon surface -> LEO (aerocapture)", 2.52, 5.60, "5 d", "mass driver 5,200 t per MW-yr (SP-428)"),
        ("Main belt 2.2 AU -> Earth", 4.21, 8.54, "370 d", "SEP tug ~280 t per MW-yr at 3.4 km/s"),
        ("Low Mercury orbit -> Earth", 7.55, 13.09, "105 d", "SEP direct spiral 0.019-0.041 t per kW-yr"),
        ("Venus cloud deck -> Earth (ideal)", 10.66, 14.12, "146 d", "0.15-0.56 % payload fraction, ascent")]
for r in rows:
    print(f"{r[0]:<38} depart {r[1]:>5.2f}  all-propulsive {r[2]:>5.2f} km/s  {r[3]:>6}  {r[4]}")
print(f"SEP productivity: lunar leg 279 t per MW-yr [TR D3] vs Mercury direct spiral {0.019*1e3:.0f}-{0.041*1e3:.0f} t per MW-yr [NW F6]: ratio {279/41:.1f}-{279/19:.1f} x worse")
print(f"Mercury-to-Earth propellant per tonne delivered 2.4 t vs lunar leg 0.18 t [NW F6; TR D4]: {2.4/0.18:.0f} x")

hdr("4. FLEETS FOR A STATED FLOW FROM MERCURY ORBIT TO EARTH ([NW] F6, restated for comparison)")
print("flow         SEP direct (power, tugs)        SEP + flybys (stages/yr, xenon/yr)   sails (km2, mass)")
print("1 kt/yr      24-53 MW, 240-530 tugs          ~130 stages, 63 t Xe                 133-336 km2, 0.78-2.0 kt")
print("100 kt/yr    2.4-5.3 GW, 24,000-53,000       ~13,000 stages, 6,300 t Xe           13,300-33,600 km2, 78-198 kt")
print("1 Mt/yr      24-53 GW, 240,000-530,000       ~130,000 stages, 63,000 t Xe         133,000-336,000 km2, 0.78-2.0 Mt")
xe = 65.0
print(f"xenon multiples of world output ({xe:.0f} t/yr): SEP direct 1 kt/yr = {2400/xe:.0f} x; SEP+flybys 1 kt/yr = {63/xe:.1f} x, 100 kt/yr = {6300/xe:.0f} x")
print(f"tug dry mass for 1 kt/yr (100 kW tugs, 6.8 t dry): {240*6.8/1e3:.1f}-{530*6.8/1e3:.1f} kt of tugs; for 1 Mt/yr: {240000*6.8/1e6:.1f}-{530000*6.8/1e6:.1f} Mt of tugs")
print(f"hardware production analog: 2,912 t/yr of Starlink-class satellites [starlifting_synthesis calc 8] -> 1.6-3.6 kt of tugs = {1.6e3/2912:.1f}-{3.6e3/2912:.1f} yr of that output")
print(f"Little's Law cargo in flight at 1 Mt/yr: 0.8-2.1 Mt (sails), 2.3-5.2 Mt (direct tugs), ~9.8 Mt (flyby route) [NW F11]")

hdr("5. VENUS EXPORT")
payload_frac = (0.0015, 0.0056)           # [VE] 3.7: studied payload fractions 0.15 % (SS-520 analog) and 0.56 % (VAV)
for flow_t in (1e3, 1e6):
    lo, hi = flow_t / payload_frac[1], flow_t / payload_frac[0]
    print(f"{flow_t:>9,.0f} t/yr of cargo to orbit -> {lo/1e3:,.0f}-{hi/1e3:,.0f} kt/yr of vehicles and propellant lifted from balloon altitude")
print("Venus atmosphere inventories [VE] 3.2: C 1.3e20 kg, N 1.1e19 kg, H 7e14 kg; one full-scale SOE plant (3 kg/hr O2) uses ~72 t CO2/yr")
n_ci = 0.00295
print(f"nitrogen alternatives: CI chondrite {n_ci*100:.3f} wt% N = {n_ci*1e3:.2f} kg per tonne; lunar regolith 81 ppm = {81e-6*1e3*1e3:.0f} g per tonne; Venus air at 55 km: 21 g N per m3 of air [VE 3.2]")
print("a tonne of N from CI material needs", f"{1/n_ci:,.0f} t of rock at 100 % recovery; from Venus air at 55 km (0.937 kg/m3, 3.5 % N2 by volume): ~{1000/0.021:,.0f} m3 of air = ~{1000/0.021*0.937/1e3:,.0f} t of air")

hdr("6. SYNODIC WINDOWS ([NW] F1, restated)")
print("Mercury->Earth every 115.9 d, window ~8-24 d wide at +10 %, ~13 % of time in a window; cheap windows ~once a year; cheapest total v-inf 17.6-22.9 km/s")
print("Venus->Earth every 583.9 d, ~28-54 d wide; Venus->Mars 333.9 d; belt->Mars every 2.8-4.4 yr [TR F4]; Earth->Mars 779.9 d")
