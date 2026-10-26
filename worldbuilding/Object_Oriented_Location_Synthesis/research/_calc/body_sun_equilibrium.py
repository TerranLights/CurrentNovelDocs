#!/usr/bin/env python3
"""Sunlight and equilibrium temperatures at the planets (OOLSD item P2, 2026-10-11). Run: python3 -I body_sun_equilibrium.py
Irradiances (S): NASA fact sheets opened 2026-10-11 (Earth 1361.0, Mars 586.2, Jupiter 50.26, Saturn 14.82 W/m2).
sigma (S): 5.670374419e-8, NIST CODATA 2022 as cited in sibling leo_and_orbital_habitats.md section 5. alpha/eps ratios are generic brackets."""
SIGMA = 5.670374419e-8
S = {"Earth/Moon (1 AU)": 1361.0, "Mars": 586.2, "Jupiter": 50.26, "Saturn": 14.82}
print("Solar array area for the same electric power, relative to Earth's distance (same cell efficiency): S_earth / S_body")
for k, v in S.items():
    print(f"  {k:18s} S = {v:8.2f} W/m2  area factor {1361.0 / v:6.2f} x")
print("\nEquilibrium temperature of an isothermal body (sink 3 K neglected): one face normal to the Sun / sphere, for alpha/eps = 1.0 and 0.25")
for k, v in S.items():
    t1a = (1.0 * v / SIGMA) ** 0.25
    t4a = (1.0 * v / (4 * SIGMA)) ** 0.25
    t1b = (0.25 * v / SIGMA) ** 0.25
    t4b = (0.25 * v / (4 * SIGMA)) ** 0.25
    print(f"  {k:18s} alpha/eps 1.00: one face {t1a:6.1f} K, sphere {t4a:6.1f} K | alpha/eps 0.25: one face {t1b:6.1f} K, sphere {t4b:6.1f} K")
print("\nHeat a sun-facing surface can collect, per m2 (alpha = 1): equals S. A radiator at 300 K (eps 0.85) radiates",
      f"{0.85 * SIGMA * 300**4:.1f} W/m2, so at Saturn even a perfectly absorbing face collects only {14.82 / (0.85 * SIGMA * 300**4) * 100:.1f} % of what one radiator face sheds at 300 K.")
