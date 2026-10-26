#!/usr/bin/env python3
"""Search for one-synodic-month periodic orbits about Earth-Moon L4 in the planar bicircular model, and their stability (OOLSD, 2026-10-11).
Run: python3 -I lagrange_bcp_search.py [+1|-1]   (+1 = L4, -1 = L5; writes bcp_orbits_L4.json / bcp_orbits_L5.json beside this script)
Starts Newton shooting (lagrange_bcp_orbit.shoot) from rings of guesses around the equilateral point and keeps distinct converged orbits."""
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lagrange_bcp_orbit import MU, A_EM, T_PER, DAY_PER_UNIT, flow, shoot, monodromy
from scipy.optimize import fsolve

SIGN = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0     # +1 = L4, -1 = L5
xc, yc = 0.5 - MU, SIGN * math.sqrt(3) / 2
OMEGA_L4 = 0.9545     # NOT used as truth: only to size velocity guesses (unperturbed short-period frequency is computed below)
# linear frequencies of the unperturbed L4 (circular restricted problem): s^4 + s^2 + 27 mu (1-mu)/4 = 0 -> w^2 = (1 -/+ sqrt(1 - 27 mu (1-mu)))/2
disc = math.sqrt(1 - 27 * MU * (1 - MU))
w_short = math.sqrt((1 + disc) / 2)
w_long = math.sqrt((1 - disc) / 2)
print(f"unperturbed L4 linear frequencies (units of the Moon's mean motion): short {w_short:.5f}, long {w_long:.5f}; forcing |w_S| = {abs(-0.925198):.5f}")

found = []
rings = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
for r in rings:
    for k in range(8):
        a = 2 * math.pi * k / 8
        for sense in (+1, -1):
            x0, y0 = xc + r * math.cos(a), yc + r * math.sin(a)
            speed = r * w_short
            vx0 = -sense * speed * math.sin(a)
            vy0 = sense * speed * math.cos(a)
            g = [x0, y0, vx0, vy0]
            try:
                sol, info, ier, msg = fsolve(shoot, g, full_output=True, xtol=1e-12)
            except Exception:
                continue
            res = float(np.max(np.abs(shoot(sol))))
            if ier != 1 or res > 1e-9:
                continue
            tr = flow(sol, T_PER, n=801)
            dev = np.hypot(tr.y[0] - xc, tr.y[1] - yc)
            d_e = np.hypot(tr.y[0] + MU, tr.y[1])
            d_m = np.hypot(tr.y[0] - 1 + MU, tr.y[1])
            if dev.max() > 1.0 or d_m.min() < 0.1:
                continue
            key = (round(sol[0], 4), round(sol[1], 4))
            if any(abs(f["state"][0] - sol[0]) < 2e-4 and abs(f["state"][1] - sol[1]) < 2e-4 for f in found):
                continue
            Mn = monodromy(sol)
            ev = np.linalg.eigvals(Mn)
            found.append({"state": sol.copy(), "dev_max": float(dev.max()), "dev_mean": float(dev.mean()), "d_e": (float(d_e.min()), float(d_e.max())),
                          "d_m": (float(d_m.min()), float(d_m.max())), "eig": sorted([float(abs(e)) for e in ev]), "start_ring": r})
print(f"\n{len(found)} distinct periodic orbits (period = one synodic month, theta0 = 0) found:")
for f in sorted(found, key=lambda f: f["dev_max"]):
    stable = max(f["eig"]) <= 1 + 1e-6
    s = f["state"]
    print(f"  start ring {f['start_ring']:.2f}: x0={s[0]:.5f} y0={s[1]:.5f} vx0={s[2]:.5f} vy0={s[3]:.5f} | max distance from the point {f['dev_max']*A_EM:9,.0f} km"
          f" (mean {f['dev_mean']*A_EM:9,.0f}) | Earth {f['d_e'][0]*A_EM:9,.0f}-{f['d_e'][1]*A_EM:9,.0f} km | Moon {f['d_m'][0]*A_EM:9,.0f}-{f['d_m'][1]*A_EM:9,.0f} km"
          f" | max |lambda| {max(f['eig']):.6f} -> {'STABLE' if stable else 'unstable'}")
import json
out = [{"state": [float(v) for v in f["state"]], "dev_max_km": f["dev_max"] * A_EM, "dev_mean_km": f["dev_mean"] * A_EM,
        "earth_km": [f["d_e"][0] * A_EM, f["d_e"][1] * A_EM], "moon_km": [f["d_m"][0] * A_EM, f["d_m"][1] * A_EM],
        "max_abs_eig": max(f["eig"])} for f in found]
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bcp_orbits_%s.json" % ("L4" if SIGN > 0 else "L5")), "w"), indent=1)
