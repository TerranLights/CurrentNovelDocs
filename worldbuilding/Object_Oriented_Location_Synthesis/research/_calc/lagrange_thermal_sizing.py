#!/usr/bin/env python3
"""
Thermal sizing for a station at Earth-Moon or Sun-Earth L4/L5 (OOLSD, 2026-10-11). Run: python3 -I lagrange_thermal_sizing.py

Every input is either (S) sourced in research/lagrange_eclipse_calculation.md section 2, or (A) an ASSUMPTION labeled
as such. Nothing is from recall. Coating values (alpha, epsilon) are ASSUMED brackets here and are to be replaced by the
sourced values in lagrange_thermal_environment.md when that file is complete.
"""
import math

SIGMA = 5.670374419e-8        # (S) W m-2 K-4, NIST CODATA 2022, as cited in sibling leo_and_orbital_habitats.md section 5
S0 = 1361.0                   # (S) W/m2, NASA Earth fact sheet
D_MEAN, D_PERI, D_APH = 149.598, 147.095, 152.100   # (S) 10^6 km, NASA Earth fact sheet
EPS = 0.85                    # (A) radiator emissivity, bracket 0.8-0.9
SUN_ELEV_MAX_DEG = 5.158      # (S->derived) lagrange_eclipse.py output: max |Sun elevation above lunar orbit plane|
SUN_ELEV_MEAN_DEG = 3.274     # derived, same run (mean of |elevation|)

print("== 1. Solar flux over the year at the Earth's distance (derived from NASA distances)")
for name, d in (("mean", D_MEAN), ("perihelion", D_PERI), ("aphelion", D_APH)):
    s = S0 * (D_MEAN / d) ** 2
    print(f"  {name:10s} d={d} Gm: S = {S0} x ({D_MEAN}/{d})^2 = {s:.1f} W/m2  ({(s/S0-1)*100:+.1f} %)")

print("\n== 2. Equilibrium temperature of an isothermal body in sunlight at 1 AU (no Earth/Moon load; sink 3 K neglected)")
print("   plate normal to the Sun, radiating one face: T = (alpha S / (eps sigma))^0.25")
print("   plate radiating both faces:                  T = (alpha S / (2 eps sigma))^0.25")
print("   isothermal sphere:                           T = (alpha S / (4 eps sigma))^0.25")
for ratio in (0.1, 0.25, 0.5, 1.0):
    t1 = (ratio * S0 / SIGMA) ** 0.25
    t2 = (ratio * S0 / (2 * SIGMA)) ** 0.25
    t4 = (ratio * S0 / (4 * SIGMA)) ** 0.25
    print(f"  alpha/eps = {ratio:4.2f}:  one face {t1:6.1f} K | both faces {t2:6.1f} K | sphere {t4:6.1f} K")

print("\n== 3. Radiator area per kW of heat rejected (one radiating face; sink 3 K neglected: (3/300)^4 = 1e-8)")
print(f"   eps = {EPS} (assumed). Flux = eps sigma T^4. A = 1000 W / flux. Edge-on to the Sun (no solar load).")
alpha_hi = 0.25                # (A) absorptance bracket for the worst-case solar term
cos_max = math.sin(math.radians(SUN_ELEV_MAX_DEG))
cos_mean = math.sin(math.radians(SUN_ELEV_MEAN_DEG))
print(f"   Radiator normal along the lunar-orbit normal: Sun incidence cosine <= sin({SUN_ELEV_MAX_DEG} deg) = {cos_max:.4f}"
      f" (mean sin({SUN_ELEV_MEAN_DEG} deg) = {cos_mean:.4f})")
print(f"   Solar load on that face at alpha = {alpha_hi} (assumed): max {alpha_hi*S0*cos_max:.1f} W/m2, mean {alpha_hi*S0*cos_mean:.1f} W/m2")
print("   T(K)  flux(W/m2)  A_edge_on(m2/kW)  A_worst_sun(m2/kW)  load as % of flux")
for T in (250, 275, 300, 320, 350, 375, 400):
    flux = EPS * SIGMA * T ** 4
    a0 = 1000 / flux
    load = alpha_hi * S0 * cos_max
    a1 = 1000 / (flux - load)
    print(f"  {T:4d}  {flux:9.1f}  {a0:14.3f}  {a1:16.3f}  {100*load/flux:12.1f}")

print("\n== 4. Heat-pump case: lift a load at T_l to a hotter radiator T_r, cold sink (A) f = fraction of Carnot COP")
print("   COP = f T_l/(T_r - T_l); heat rejected per kW of load = 1 + 1/COP; compressor work = 1/COP kW per kW of load")
TL = 275.0                     # (S, sibling) ISS ammonia supply temperature, waste_heat_utilization.md B-HP
T_BASE = 300.0
print(f"   T_l = {TL} K; baseline: reject directly at {T_BASE} K")
base_a = 1000 / (EPS * SIGMA * T_BASE ** 4)
print(f"   baseline area at {T_BASE} K: {base_a:.3f} m2 per kW")
for TR in (320.0, 360.0, 400.0):
    for f in (0.38, 0.5, 0.6):
        cop = f * TL / (TR - TL)
        qrej = 1 + 1 / cop
        a = qrej * 1000 / (EPS * SIGMA * TR ** 4)
        w = 1000 / cop
        saved = base_a - a
        for ae in (229.2, 300.0, 416.0):   # array output W/m2: silicon 229.2, ASSUMED 300, triple-junction 416 (sibling life_support 5-row)
            extra = (w / 1000) * 1000 / ae
            pass
        print(f"   T_r={TR:5.0f} K f={f:4.2f}: COP {cop:5.2f}, Q_rej {qrej:5.2f} kW, area {a:5.3f} m2 (saved {saved:+.3f} m2 vs {T_BASE:.0f} K), "
              f"compressor {w:6.1f} W -> array area {w/229.2:5.2f} / {w/300.0:5.2f} / {w/416.0:5.2f} m2 at 229.2 / 300 / 416 W/m2")

print("\n== 5. Stored energy to carry 1 kW through the longest eclipse events found (lagrange_eclipse.py)")
events = {"longest total (umbral) event, 164 min": 164 / 60.0, "longest any-obscuration event, 288 min": 288 / 60.0}
media = {
    "PCM, system level, 48.8 kJ/kg (13.6 Wh/kg) [sibling E1]": 48.8e3 / 3600.0,
    "n-hexadecane, 235 kJ/kg before packaging [sibling]": 235e3 / 3600.0,
    "ice melt, 333.44 kJ/kg before tank [sibling]": 333.44e3 / 3600.0,
    "LiCl absorber concept, 800 kJ/kg [sibling]": 800e3 / 3600.0,
    "Li-ion cell, 182 Wh/kg low [sibling robot_body S33]": 182.0,
    "Li-ion cell, 264 Wh/kg high [sibling robot_body S33]": 264.0,
}
for ename, h in events.items():
    print(f"  {ename} = {h:.3f} h -> {h:.3f} kWh per kW")
    for mname, e in media.items():
        print(f"     {mname:60s} {e:7.1f} Wh/kg -> {h*1000/e:7.1f} kg per kW")

print("\n== 6. Dark time and cycle count against the ISS orbit")
iss_dark = 36.0 / 93.0
iss_cycles = 365.25 * 24 * 60 / 93.0
print(f"   ISS (sibling: about 36 min of darkness in about 93 min): dark fraction {iss_dark*100:.1f} %; {iss_cycles:,.0f} dark periods per year (365.25 x 1440 / 93)")
print("   (L4/L5 figures are read from lagrange_eclipse.py output in section 4 of the calculation file.)")

print("\n== 7. Heat loads from the Earth and the Moon at Earth-Moon L4/L5 (distance 384,400 km to each), against the Sun")
R_E_KM, R_M_KM, D_KM = 6378.137, 1737.4, 384400.0     # (S) NASA fact sheets, semimajor axis 0.3844e6 km
T_BB_EARTH = 254.0       # (S) NASA Earth fact sheet, black-body temperature K
BOND_E, GEO_M = 0.294, 0.12   # (S) NASA Earth fact sheet Bond albedo; NASA Moon fact sheet geometric albedo
exitance_e = SIGMA * T_BB_EARTH ** 4
view_e = (R_E_KM / D_KM) ** 2
print(f"  Earth thermal exitance = sigma x {T_BB_EARTH}^4 = {exitance_e:.1f} W/m2; geometric factor (R/d)^2 = ({R_E_KM}/{D_KM:,.0f})^2 = {view_e:.4e}")
print(f"  Earth thermal irradiance at the station (surface facing Earth) = {exitance_e*view_e:.4f} W/m2 = {exitance_e*view_e/S0*100:.4f} % of the Sun")
print(f"  Earth reflected sunlight, upper bound = Bond albedo x S x (R/d)^2 = {BOND_E} x {S0} x {view_e:.4e} = {BOND_E*S0*view_e:.4f} W/m2 = {BOND_E*S0*view_e/S0*100:.4f} % of the Sun")
view_m = (R_M_KM / D_KM) ** 2
t_max_moon = 400.0       # (A) assumed upper bound for the sunlit lunar surface, K (not sourced here)
print(f"  Moon reflected sunlight, upper bound = {GEO_M} x {S0} x ({R_M_KM}/{D_KM:,.0f})^2 = {GEO_M*S0*view_m:.5f} W/m2")
print(f"  Moon thermal emission, bound at an ASSUMED {t_max_moon:.0f} K everywhere = sigma x {t_max_moon:.0f}^4 x {view_m:.4e} = {SIGMA*t_max_moon**4*view_m:.4f} W/m2")
print("  Conclusion: Earth and Moon together add well under 0.3 W/m2 against 1,361 W/m2 from the Sun; the sink is deep space plus the Sun.")
