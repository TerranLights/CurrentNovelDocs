#!/usr/bin/env python3
"""Moon-transit events at L4/L5 from the Horizons cache: how deep, and at what Earth-Moon distance? (OOLSD, 2026-10-11)
Usage: python3 -I lagrange_moon_events.py <cache_dir>"""
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lagrange_eclipse import R_E, R_S, R_M, frac_obscured, runs
from lagrange_eclipse_horizons import rot_about_normal, DT

cache = sys.argv[1]
moon = np.load(f"{cache}/moon.npy")
sun = np.load(f"{cache}/sun.npy")
n = min(len(moon), len(sun))
M, V, S = moon[:n, :3], moon[:n, 3:], sun[:n, :3]
D = np.linalg.norm(M, axis=1)
d_sun_mean = 149.598e6
thr = R_M * d_sun_mean / R_S
print(f"Distance at which the Moon's angular radius equals the Sun's: R_M x D / R_S = {R_M} x {d_sun_mean:.6g} / {R_S} = {thr:,.0f} km")
print(f"Fraction of time the real Earth-Moon distance is below that: {(D < thr).mean():.3f} (min {D.min():,.0f}, max {D.max():,.0f} km)")
for name, ang in (("L4", math.radians(60)), ("L5", math.radians(-60))):
    P, nrm = rot_about_normal(M, V, ang)
    PS = S - P
    dPS = np.linalg.norm(PS, axis=1)
    rs = np.arcsin(R_S / dPS)
    PM = M - P
    dPM = np.linalg.norm(PM, axis=1)
    c = np.einsum("ij,ij->i", PS, PM) / (dPS * dPM)
    fM = frac_obscured(rs, np.arcsin(R_M / dPM), np.arccos(np.clip(c, -1, 1)))
    s, l = runs(fM > 0)
    peaks = np.array([fM[a:a + b].max() for a, b in zip(s, l)])
    dpk = np.array([D[a + int(np.argmax(fM[a:a + b]))] for a, b in zip(s, l)])
    print(f"\n{name}: {len(s)} Moon-transit events in {n*DT/86400/365.25:.1f} yr (10-minute samples)")
    for lo, hi in ((0, 0.5), (0.5, 0.8), (0.8, 0.95), (0.95, 0.999), (0.999, 1.01)):
        m = (peaks >= lo) & (peaks < hi)
        print(f"   peak obscuration {lo:5.3f}-{min(hi,1.0):5.3f}: {int(m.sum()):3d} events" + (f", Earth-Moon distance at peak {dpk[m].min():,.0f}-{dpk[m].max():,.0f} km" if m.any() else ""))
    top = np.argsort(-peaks)[:5]
    for i in top:
        print(f"   deepest: peak {peaks[i]:.4f}, distance {dpk[i]:,.0f} km, duration {l[i]*DT/60:.0f} min")
