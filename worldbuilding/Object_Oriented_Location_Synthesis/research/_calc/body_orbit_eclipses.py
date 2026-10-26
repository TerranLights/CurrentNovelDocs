#!/usr/bin/env python3
"""
Eclipse statistics for circular equatorial orbits about the Moon, Mars, Jupiter and Saturn, validated on Earth GEO
(OOLSD deferred item P2, 2026-10-11). Run: python3 -I body_orbit_eclipses.py

MODEL (stated limits)
  * Cylindrical shadow of a sphere of the stated radius. The Sun's finite size (penumbra, umbra taper) is ignored; at the
    radii used it changes the dark time by a few percent (the GEO check below shows the size of the effect).
  * Circular orbit in the body's equatorial plane. The Sun's elevation above that plane is the Sun's declination,
    delta(L) = asin(sin(obliquity) sin L), L uniform over the body's year (orbital eccentricity ignored).
  * Dark fraction of one orbit at Sun elevation beta:  f(beta) = (1/pi) acos( sqrt(1-(R/r)^2) / cos(beta) ) for |beta| < asin(R/r), else 0.
  * Oblateness, ring shadows (Saturn), moons' shadows and the body's own thermal/albedo loads are not modeled.
INPUTS (S = NASA fact sheets opened 2026-10-11 and NIST CODATA 2022; see research/body_orbit_eclipse_calculation.md section 2)
"""
import math
import numpy as np

G = 6.67430e-11          # (S) m3 kg-1 s-2, NIST CODATA 2022

# name: (radius_km, GM_km3_s2, rotation_h, obliquity_deg, year_d, source note)
BODIES = {
    "Earth": (6378.137, 398600.0, 23.9345, 23.44, 365.256, "radius equatorial, GM 0.39860e6, rotation, obliquity, sidereal year: NASA Earth sheet"),
    "Moon": (1737.4, G * 0.07346e24 / 1e9, 655.720, 6.68 - 5.145, 346.62, "radius volumetric mean, mass 0.07346e24: NASA Moon sheet; obliquity to ecliptic DERIVED as 6.68 - 5.145 (Cassini-state coplanarity ASSUMED); year = eclipse year 346.62 d (simulation)"),
    "Mars": (3396.2, 42828.0, 24.6229, 25.19, 686.980, "radius equatorial, GM 0.042828e6, rotation, obliquity, year: NASA Mars sheet"),
    "Jupiter": (71492.0, G * 1898.13e24 / 1e9, 9.9250, 3.13, 4332.589, "radius equatorial (1 bar), mass 1898.13e24, rotation, obliquity, year: NASA Jupiter sheet"),
    "Saturn": (60268.0, G * 568.32e24 / 1e9, 10.656, 26.73, 10755.699, "radius equatorial (1 bar), mass 568.32e24, rotation, obliquity, year: NASA Saturn sheet"),
}
SOLAR = {"Mars": 586.2, "Jupiter": 50.26, "Saturn": 14.82, "Earth": 1361.0, "Moon": 1361.0}   # (S) W/m2, NASA sheets (Moon: Earth's)
LI_ION_WH_KG = 182.0       # (S, sibling robot_body S33) cell level, low end
ICE_WH_KG = 92.6           # (S, sibling waste-heat E1) ice melt before tank
PCM_WH_KG = 13.6           # (S, sibling waste-heat E1) system-level PCM


def f_dark(R, r, beta):
    sb = R / r
    beta = np.asarray(beta, dtype=float)
    out = np.zeros_like(beta)
    ok = np.abs(beta) < math.asin(sb)
    out[ok] = np.arccos(np.clip(math.sqrt(1 - sb**2) / np.cos(beta[ok]), -1, 1)) / math.pi
    return out


def season_stats(R, r, eps_deg, n=200000):
    L = np.linspace(0, 2 * math.pi, n, endpoint=False)
    delta = np.arcsin(math.sin(math.radians(eps_deg)) * np.sin(L))
    f = f_dark(R, r, delta)
    return float(f.mean()), float((f > 0).mean()), float(f.max())


def row(name, label, r):
    R, GM, rot_h, eps, year, _ = BODIES[name]
    T = 2 * math.pi * math.sqrt(r**3 / GM)               # s
    f0 = float(f_dark(R, r, [0.0])[0])
    fmean, season, fmax = season_stats(R, r, eps)
    dark_max_min = f0 * T / 60.0
    orbits_per_year = year * 86400.0 / T
    dark_events_per_year = orbits_per_year * season
    kwh_per_kw = f0 * T / 3600.0
    print(f"  {label:26s} r={r:11,.0f} km ({r/R:5.2f} R)  T={T/3600:8.3f} h  beta*={math.degrees(math.asin(R/r)):5.1f} deg  "
          f"max dark {dark_max_min:7.1f} min ({f0*100:4.1f} % of orbit)  year-mean dark {fmean*100:5.2f} %  eclipse season {season*100:5.1f} % of year  "
          f"dark periods/yr {dark_events_per_year:10,.0f}  kWh/kW {kwh_per_kw:6.3f}  Li-ion cell {kwh_per_kw*1000/LI_ION_WH_KG:7.1f} kg/kW  ice {kwh_per_kw*1000/ICE_WH_KG:7.1f}  PCM {kwh_per_kw*1000/PCM_WH_KG:8.1f}")


def synchronous(name):
    R, GM, rot_h, eps, year, _ = BODIES[name]
    return (GM * (rot_h * 3600.0 / (2 * math.pi)) ** 2) ** (1.0 / 3.0)


if __name__ == "__main__":
    print("NIST CODATA 2022 G = 6.67430e-11 m3 kg-1 s-2")
    for k, v in BODIES.items():
        print(f"  {k:8s} R={v[0]:>9,.1f} km  GM={v[1]:>14,.1f} km3/s2  rotation {v[2]} h  obliquity {v[3]:.2f} deg  year {v[4]} d")
    print("\n== Validation: Earth geostationary orbit against the NOAA GOES statements (up to 72 min a day; eclipse seasons ~45 days either side of each equinox)")
    r_geo = synchronous("Earth")
    row("Earth", "GEO (synchronous)", r_geo)
    R = BODIES["Earth"][0]
    print(f"  synchronous radius = (GM (T/2pi)^2)^(1/3) = {r_geo:,.0f} km; model max dark above vs NOAA 72 min (difference: the Sun's finite size)")
    print("\n== Circular equatorial orbits (dark fraction, season, storage per kW through the longest dark interval)")
    plan = {
        "Moon": [("low lunar orbit, 100 km", 1737.4 + 100.0), ("1,000 km altitude", 1737.4 + 1000.0), ("2 R", 2 * 1737.4), ("4 R", 4 * 1737.4), ("10 R", 10 * 1737.4)],
        "Mars": [("low Mars orbit, 400 km", 3396.2 + 400.0), ("2 R", 2 * 3396.2), ("4 R", 4 * 3396.2), ("areostationary", synchronous("Mars")), ("10 R", 10 * 3396.2)],
        "Jupiter": [("2 R", 2 * 71492.0), ("3 R", 3 * 71492.0), ("5 R", 5 * 71492.0), ("synchronous", synchronous("Jupiter")), ("10 R", 10 * 71492.0), ("20 R", 20 * 71492.0)],
        "Saturn": [("2 R", 2 * 60268.0), ("3 R", 3 * 60268.0), ("5 R", 5 * 60268.0), ("synchronous", synchronous("Saturn")), ("10 R", 10 * 60268.0), ("20 R", 20 * 60268.0)],
    }
    for body, orbits in plan.items():
        print(f"\n{body}:")
        for label, r in orbits:
            row(body, label, r)
    print("\n== Sunlight at the planets (NASA sheets) and the heliocentric case")
    for b in ("Mars", "Jupiter", "Saturn"):
        print(f"  {b}: {SOLAR[b]} W/m2 = {SOLAR[b]/1361.0*100:.1f} % of the Earth value")
    print("  A circular heliocentric orbit has no planetary shadow at any distance: no dark interval, flux = 1361 W/m2 x (1 AU / r)^2.")
