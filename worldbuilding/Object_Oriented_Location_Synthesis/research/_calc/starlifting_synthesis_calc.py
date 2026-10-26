#!/usr/bin/env python3
"""Arithmetic behind research/starlifting_synthesis.md (OOLSD, 2026-10-11). Run: python3 -I starlifting_synthesis_calc.py
Every INPUT below is a figure sourced in one of the five tranche-6 files (key in the comment). Nothing here is read from the
project's interplanetary timeline or any other canon. Nothing is fitted; ranges come from stating each analog's own numbers.
Keys: [SL]=starlifting_physics_and_minimum_infrastructure.md  [TR]=space_trucking_and_transport_infrastructure.md
      [PR]=space_processing_and_fabrication.md  [RM]=industrial_ramp_timelines.md  [CY]=cyclers_and_large_slow_vehicles.md"""
import math

def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)

def loginterp(points, x):
    """points: [(multiple, years)] sorted by multiple; interpolate years linearly in log10(multiple); returns years."""
    lx = math.log10(x)
    for (m0, y0), (m1, y1) in zip(points, points[1:]):
        if m0 <= x <= m1:
            l0, l1 = math.log10(m0), math.log10(m1)
            return y0 + (lx - l0) / (l1 - l0) * (y1 - y0)
    raise ValueError("outside range")

YR = 3.15576e7

# ---------------------------------------------------------------- 1. The Sun as a materials source
hdr("1. SUN AS A MATERIALS SOURCE")
GM_sun, R_sun = 1.32712e20, 6.957e8           # [SL] NSSDC
e_lift = GM_sun / R_sun                        # J/kg to escape from the photosphere
fe_t_per_t = 841.0                             # [SL] 3B: t of photosphere per t of Fe (A21)
struct_t_per_t = 513.0                         # [SL] 3B: per t of Fe+Ni+Mg+Al+Ti+Cu together
print(f"escape energy GM/R = {e_lift:.4e} J/kg")
E_fe = fe_t_per_t * 1e3 * e_lift
print(f"ideal lift energy per t Fe = {fe_t_per_t} t x 1000 kg x {e_lift:.3e} = {E_fe:.2e} J")
P_fe = E_fe / YR
print(f"=> continuous ideal power for 1 t Fe per YEAR = {E_fe:.2e} J / {YR:.4e} s = {P_fe/1e9:.2f} GW (100% efficiency, separation excluded)")
E_struct = struct_t_per_t * 1e3 * e_lift
print(f"structural-metal mix: {struct_t_per_t} t lifted per t -> {E_struct:.2e} J per t = {E_struct/YR/1e9:.2f} GW per (t/yr)")
Mercury_MJ = 9.03e6                           # [SL] D6 J/kg
E_merc = Mercury_MJ * 1e3 / 0.70              # per t of 70 %-metal material
print(f"Mercury, 70 % metal material: {E_merc:.2e} J per t Fe -> {E_merc/YR:.0f} W per (t/yr); ratio Sun/Mercury = {E_fe/E_merc:.2e}")
print(f"compare Earth surface -> 400 km orbit 33.1 MJ/kg [TR D5]: Sun lift / that = {e_lift/33.1e6:,.0f}x")
print(f"compare raising 1 kg from a 0.1 AU circular orbit to 1 AU, 3,992 MJ/kg [TR D5]: Sun lift / that = {e_lift/3.992e9:.1f}x")
sc = 2397.0                                    # [RM] world solar capacity end-2025, GW
print(f"1 t Fe/yr from the photosphere ({P_fe/1e9:.1f} GW) = {P_fe/1e9/sc*100:.2f} % of ALL world solar capacity at end-2025 ({sc:.0f} GW) [RM]")

hdr("1b. SOLAR-WIND COLLECTION: area for iron")
flux_1au = 3.09e-15                            # [SL] D3 kg m-2 s-1, slow wind, 1 AU
fe_per_t_wind = 1.0 / fe_t_per_t               # t Fe per t wind, photospheric proportions (FIP enrichment 1.6-2.3x NOT applied)
for r in (1.0, 0.3, 0.1, 0.0465):
    f = flux_1au / r**2
    area_t_wind = 1.0 / (f * YR / 1e3) / 1e6   # km2 per (t wind / yr)
    area_t_fe = area_t_wind * fe_t_per_t
    kg_fe_km2 = f * YR * 1e6 * fe_per_t_wind   # kg Fe per km2 per year
    print(f"r={r:<6} AU: {area_t_wind:>9,.0f} km2 per t wind/yr;  {area_t_fe:>12,.0f} km2 per t Fe/yr (no FIP credit);  {kg_fe_km2*1e3:.3f} g Fe per km2 per yr")
print("with the FIP enrichment fFIP = 1.6-2.3 [SL 3E] the iron areas above shrink by that factor, if it applies to Fe/H (not confirmed: Open thread)")
print(f"Genesis [SL D4]: 0.46 mg H in 853 d on 1.67 m2 -> {0.46/853*365.25:.2f} mg/yr")

# ---------------------------------------------------------------- 2. Ramp arithmetic
hdr("2. RAMP ARITHMETIC: multiples and analog times")
PV = [(1, 0), (10, 8), (100, 13), (1000, 23)]            # [RM] F1 solar capacity from 2000: 10x 8 yr, 100x 13 yr, 1000x 23 yr
RAIL = [(1, 0), (10, 16), (100, 46.5)]                   # [RM] F1 railroad from 1,075 mi (1835): 10x 16 yr, 100x 46-47 yr
payload_doubling = 6 / math.log2(3194.0 / 399.2)         # [RM] D9: 399.2 t (2019) -> 3194.0 t (2025)
print(f"world payload to orbit 2019->2025: x{3194.0/399.2:.2f} in 6 yr -> doubling time {payload_doubling:.2f} yr [RM D9]")
METZGER_GEN = 2.0                                        # [RM] F4: generations 2 yr apart
ramps = [("A: 10 -> 1,000 t/yr", 10, 1e3), ("B: 1,000 -> 54,000 t/yr (SP-413 refinery, 54 kt/yr [PR 5])", 1e3, 5.4e4),
         ("C: 54,000 t/yr -> 1.2 Mt/yr (SP-413 shield rate [RM F3])", 5.4e4, 1.2e6)]
rows = {}
for name, a, b in ramps:
    m = b / a
    d = math.log2(m)
    pv = loginterp(PV, m) if m <= 1000 else float("nan")
    rail = loginterp(RAIL, m) if m <= 100 else float("nan")
    cp_work = d                                          # CP-2255 simple exponential: one doubling per working year [RM F4]
    cp_cal = 2 * d                                       # Table 5.2 converts calendar = 2 x working
    met = d * METZGER_GEN                                # one doubling per 2-yr generation (upper bound of 'two or fewer new sets per year')
    pay = d * payload_doubling
    print(f"\n{name}: multiple {m:,.1f}x = {d:.2f} doublings")
    print(f"   solar-PV analog (log-interpolated 10x/8, 100x/13, 1000x/23 yr): {pv:.1f} yr")
    print(f"   railroad analog (10x/16, 100x/46.5 yr):                          {rail:.1f} yr")
    print(f"   world launched-mass analog (doubling {payload_doubling:.1f} yr):                    {pay:.1f} yr")
    print(f"   CP-2255 simple exponential: {cp_work:.1f} working yr = {cp_cal:.1f} calendar yr (Table 5.2 conversion)")
    print(f"   Metzger generations (1 doubling per {METZGER_GEN:.0f} yr):                         {met:.1f} yr")
    rows[name] = (pv, rail, pay, cp_work, cp_cal, met)

# ---------------------------------------------------------------- 3. Commitment -> first hardware
hdr("3. COMMITMENT TO FIRST OPERATING HARDWARE (development lead times)")
apollo = 8 + 2 / 12                                    # [RM F3] 25 May 1961 -> 20 Jul 1969: 8 yr 2 mo
shuttle = 9.3                                            # [RM F3] 5 Jan 1972 -> 12 Apr 1981
iss = 12.5                                               # [RM F3] Zarya Nov 1998 -> US assembly complete May 2011 (assembly, not development)
sp413_rd = (5 + 3, 5 + 5)                                # [RM F3] 5 yr R&D + 3-5 yr development and test
sp428 = (4, 5)                                           # [RM F3] 'less than 8 years of launch ... follow 4 or 5 years of development' (assumed 60 Shuttle flights/yr)
slip = 14.5 / 10.0                                       # [RM F6] Flyvbjerg: dams 10 yr planned -> 14.5 yr ('preliminary')
print(f"Apollo {apollo:.1f} yr; Shuttle {shuttle} yr; SP-413 R&D+dev {sp413_rd[0]}-{sp413_rd[1]} yr; SP-428 {sp428[0]}-{sp428[1]} yr (study; assumed a 60-flight/yr Shuttle that did not exist)")
print(f"reference-class slip factor {slip:.2f}: Apollo -> {apollo*slip:.1f} yr; Shuttle -> {shuttle*slip:.1f} yr")
lead_lo, lead_hi = apollo, shuttle * slip
print(f"=> commitment-to-first-hardware range used: {lead_lo:.1f} (Apollo, no slip) to {lead_hi:.1f} (Shuttle x slip) yr")

# ---------------------------------------------------------------- 4. Habitat scale
hdr("4. HABITAT SCALE")
iss_t, torus_t, cyl_t = 419.725, 10.09e6, 80.2e6        # [PR 6] ISS; SP-413 torus total; cylinder total
print(f"torus / ISS mass = {torus_t/iss_t:,.0f}x = {math.log2(torus_t/iss_t):.1f} doublings;  cylinder / ISS = {cyl_t/iss_t:,.0f}x = {math.log2(cyl_t/iss_t):.1f} doublings")
print(f"ISS observed assembly rate: {iss_t:.0f} t / {iss} yr = {iss_t/iss:.0f} t per yr")
print(f"torus structure 150 kt at refinery output 54 kt/yr = {150/54:.1f} yr [PR D14];  torus shield 9.9 Mt at 1.2 Mt/yr = {9.9/1.2:.2f} yr")
print(f"1 Mt/yr vs 2025 world launched mass 3,194 t = {1e6/3194:.0f}x [TR]; vs cataloged mass in orbit 16,185 t = {1e6/16185:.0f}x")

# ---------------------------------------------------------------- 5. Chain totals
hdr("5. CHAIN TOTALS (lowest of the analogs per stage, highest of the analogs per stage)")
def lo_hi(key):
    pv, rail, pay, cpw, cpc, met = rows[key]
    vals = [v for v in (pv, pay, cpw, cpc, met) if not math.isnan(v)]   # railroad shown but excluded from the range: a network built on land
    return min(vals), max(vals)
tot_lo, tot_hi = lead_lo, lead_hi
print(f"commitment -> first hardware: {lead_lo:.1f} - {lead_hi:.1f}")
for name, *_ in ramps:
    lo, hi = lo_hi(name)
    print(f"{name}: {lo:.1f} - {hi:.1f}")
    tot_lo += lo
    tot_hi += hi
shield_lo, shield_hi = 9.9 / 1.2, 9.9 / 1.2 * 1.0
print(f"deliver the 9.9 Mt shield at 1.2 Mt/yr: {shield_lo:.1f} yr (both ends; rate fixed by the study)")
tot_lo += shield_lo
tot_hi += shield_hi
print(f"SEQUENTIAL SUM to a first ~10 Mt torus: {tot_lo:.0f} - {tot_hi:.0f} yr (stages treated one after another: an upper bound)")
print(f"SP-413's own overlapped schedule: 22 yr (study; never tested). With slip factor {slip:.2f}: {22*slip:.0f} yr")

# ---------------------------------------------------------------- 6. Moving a habitat
hdr("6. MOVING A LARGE HABITAT BY ELECTRIC PROPULSION ([CY] 5.5 method)")
g0, eta, Isp = 9.80665, 0.6, 5000.0
ve = Isp * g0
tp = 2 * eta / ve                                       # N per W
print(f"T/P = 2*eta/(g0*Isp) = {tp*1e3*1e3:.1f} mN per kW at eta {eta}, Isp {Isp:.0f} s (ve {ve/1e3:.1f} km/s)")
for label, M in (("1e6 t", 1e9), ("SP-413 torus 10.09 Mt", 10.09e9), ("SP-413 cylinder 80.2 Mt", 80.2e9)):
    for P in (1e9, 1e10):
        F = P * tp
        for dv in (1000.0, 3500.0, 5800.0, 6400.0):
            mp = M * (1 - math.exp(-dv / ve))
            t = mp * ve / F / YR
            print(f"{label:>24} | {P/1e9:>4.0f} GW | thrust {F/1e3:>6.0f} kN | a {F/M/9.80665:.1e} g | dv {dv/1e3:.1f} km/s: propellant {mp/1e9:>9,.2f} Mt ({100*(1-math.exp(-dv/ve)):.1f} %), burn {t:>8.2f} yr")
print(f"world xenon ~65 t/yr [TR F3]: 1.2 Mt of propellant = {1.2e6/65:,.0f} years of world xenon output")
print(f"power plant at 4-8 kg/kWe [CY]: 10 GW = {10e6*4/1e3:,.0f} - {10e6*8/1e3:,.0f} t  (= {40e3/10.09e6*100:.2f}-{80e3/10.09e6*100:.2f} % of the torus mass)")

# ---------------------------------------------------------------- 7. Mars
hdr("7. MARS PRESENCE")
a_mars = 227.956 / 149.598
print(f"Mars semimajor axis {a_mars:.3f} AU: sunlight {1/a_mars**2*100:.0f} % of Earth's ({1361/a_mars**2:.0f} W/m2)")
syn = 779.94 / 365.25
print(f"Earth-Mars synodic period {syn:.3f} yr [TR F1]")
print(f"Musk claim: 20-50 rendezvous x {syn:.3f} = {20*syn:.1f} - {50*syn:.1f} yr")
print(f"DRA 5.0 [RM F3]: three missions on consecutive opportunities: first-to-third = 2 x {syn:.2f} = {2*syn:.1f} yr; cargo pre-deployed 'just over 2 years' ahead of the first crew")
print(f"DRA 5.0 IMLEO 3 missions: {3*848.7:,.0f} t (NTR) - {3*1251.8:,.0f} t (chemical) = {3*848.7/3194:.2f} - {3*1251.8/3194:.2f} x the 2025 world launched mass of 3,194 t")
for cap, label in ((12, "12 per window (one Astrotel-class cycler, Landau/Nock)"), (100, "100 per window (one 100-person ship per window, Musk claim)")):
    w = math.ceil(110 / cap)
    print(f"110 people (Salotti minimum) at {label}: {w} windows = {w*syn:.1f} yr")
print(f"Phobos-radius spaceport 3 h; Aldrin cycler Mars V-inf 7-12 km/s, Earth ~6 km/s [CY]; Earth-Mars Hohmann LEO->LMO 5.66 km/s, 259 d [TR D1]")
print(f"Main belt -> Mars all-propulsive 3.76-6.10 km/s vs belt -> Earth 8.54-10.39 km/s [TR D1]: ratio {3.76/8.54:.2f}-{6.10/10.39:.2f}")

# ---------------------------------------------------------------- 8. Hardware and robots
hdr("8. HARDWARE PRODUCTION ANALOG AND ROBOT VITAMINS")
sl_per_yr, sl_kg = 3640, 800                              # [RM F2] S-1; [TR F3] ~800 kg V2 mini (trade-press, flagged)
print(f"Starlink production ~{sl_per_yr}/yr x ~{sl_kg} kg (mass is trade-press, low-medium) = {sl_per_yr*sl_kg/1e3:,.0f} t/yr of satellites")
tugs = 143
print(f"143 SEP tugs x 9.75 t = {tugs*9.75:,.0f} t = {tugs*9.75/(sl_per_yr*sl_kg/1e3):.2f} yr of Starlink-mass production [TR F3]")
mag_lo, mag_hi = 1073.0, 1610.0                           # [PR D8] t of CI material per robot (Nd+Pr, 100 % recovery)
li_lo, li_hi = 94.5, 152.0                                # [PR D9] t of CI material per robot battery (NMC811)
for n in (1000, 100000):
    print(f"{n:>7,} robots: magnet rare earths {n*mag_lo/1e6:,.2f}-{n*mag_hi/1e6:,.2f} Mt of CI-type material; battery lithium {n*li_lo/1e3:,.0f}-{n*li_hi/1e3:,.0f} kt")
print(f"1,000 robots' magnets at 54 kt/yr whole-plant throughput = {1000*mag_lo/54e3:.0f}-{1000*mag_hi/54e3:.0f} yr of that entire output")
print(f"imported instead: 2-3 kg NdFeB per robot x 1,000 = 2-3 t; at $1,500/kg to LEO (Falcon Heavy, 2021 USD [TR F5]) = ${2*1500:,}-${3*1500:,} per robot")
print(f"Metzger electronics closure: Gens 3.0/4.0/5.0/6.0 = 90/95/99/100 %, generations 2 yr apart [RM F4, PR 3]; Gen 1.0 set 7.7 t makes 24.5 t/yr of parts")
print(f"Metzger bootstrapping, 41 t launched -> up to 40,000 t with up to 100,000 robots in ~20 yr: {math.log2(40000/41):.1f} doublings -> {20/math.log2(40000/41):.1f} yr per doubling (matches the 2-yr generations)")
print(f"Metzger bootstrapping, 12 t landed -> 156 t end state (60 robots) in ~20 yr: {math.log2(156/12):.1f} doublings -> {20/math.log2(156/12):.1f} yr per doubling (a smaller end state, not a slower rate)")

hdr("9. SLOW BOUND: the railroad analog in place of the 2-yr doubling (a network built across land; not a central case)")
rail_total = 0.0
for name, *_ in ramps:
    rail_total += rows[name][1]
print(f"railroad analog, stages A+B+C = {rail_total:.1f} yr; plus first hardware {lead_lo:.1f}-{lead_hi:.1f} and shield delivery 8.2 -> {rail_total+lead_lo+8.25:.0f} - {rail_total+lead_hi+8.25:.0f} yr")
print("Ono 2025 (undergraduate thesis, low weight): power and processing bottlenecks gave LINEAR growth; tripled mass in 5 yr from 8,925 kg [RM F4]")
ono_x3 = math.log2(3.0)
print(f"   x3 in 5 yr = {ono_x3:.2f} doublings -> {5/ono_x3:.1f} yr per 'doubling' if read as exponential; as linear, each added 8,925 kg-equivalent takes a constant 2.5 yr")
