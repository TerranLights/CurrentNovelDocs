#!/usr/bin/env python3
"""Cross-check of lagrange_eclipse.py with real ephemerides (JPL Horizons DE441, geocentric, ecliptic J2000, 10-minute steps).
Usage: python3 -I lagrange_eclipse_horizons.py <cache_dir>      (cache built by horizons_fetch.py)

L4/L5 are taken as the INSTANTANEOUS equilateral vertices: the geocentric Moon vector rotated by +/-60 degrees about the
Moon's instantaneous orbit normal (r x v). Their distance from Earth and from the Moon therefore equals the real, varying
Earth-Moon distance. The real eccentricity, evection and the Sun's true distance are all included; the libration of a real
station about the point, and the point's own dynamics under solar perturbation, are not.
"""
import sys, os, math, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lagrange_eclipse import R_E, R_S, R_M, frac_obscured, runs

DT = 600.0


def rot_about_normal(M, V, ang):
    n = np.cross(M, V)
    n /= np.linalg.norm(n, axis=1)[:, None]
    return M * math.cos(ang) + np.cross(n, M) * math.sin(ang), n


def metrics(P, M, S, n_normal):
    nrow = len(P)
    yrs = nrow * DT / 86400.0 / 365.25
    PS = S - P
    dPS = np.linalg.norm(PS, axis=1)
    rs = np.arcsin(R_S / dPS)
    out = {"years": round(yrs, 2)}
    fE = np.zeros(nrow)
    fM = np.zeros(nrow)
    for i0 in range(0, nrow, 500_000):
        i1 = min(nrow, i0 + 500_000)
        sl = slice(i0, i1)
        PE = -P[sl]
        dPE = np.linalg.norm(PE, axis=1)
        c = np.einsum("ij,ij->i", PS[sl], PE) / (dPS[sl] * dPE)
        fE[sl] = frac_obscured(rs[sl], np.arcsin(R_E / dPE), np.arccos(np.clip(c, -1, 1)))
        PM = M[sl] - P[sl]
        dPM = np.linalg.norm(PM, axis=1)
        c = np.einsum("ij,ij->i", PS[sl], PM) / (dPS[sl] * dPM)
        fM[sl] = frac_obscured(rs[sl], np.arcsin(R_M / dPM), np.arccos(np.clip(c, -1, 1)))
    el = np.degrees(np.arcsin(np.einsum("ij,ij->i", PS / dPS[:, None], n_normal)))
    out["sun_elev_abs_max_deg"] = round(float(np.abs(el).max()), 3)
    out["sun_elev_abs_mean_deg"] = round(float(np.abs(el).mean()), 3)

    def ev(name, flag):
        s, l = runs(flag)
        dur = l * DT / 60.0
        d = {"events": int(len(s)), "events_per_year": round(len(s) / yrs, 3), "time_fraction": float(flag.mean())}
        if len(s):
            d.update({"dur_min_mean": round(float(dur.mean()), 1), "dur_min_median": round(float(np.median(dur)), 1),
                      "dur_min_p90": round(float(np.percentile(dur, 90)), 1), "dur_min_max": round(float(dur.max()), 1)})
        out[name] = d

    ev("earth_any_obscuration", fE > 0.0)
    ev("earth_total_f_ge_0.999", fE >= 0.999)
    ev("moon_any_obscuration", fM > 0.0)
    ev("either_any", (fE > 0.0) | (fM > 0.0))
    out["moon_max_obscuration"] = round(float(fM.max()), 4)
    out["mean_sunlight_lost_fraction"] = float((fE + fM).mean())
    return out


def lunar_eclipses(M, S, k):
    """Moon disc against Earth's shadow cones with the real Sun distance."""
    D = np.linalg.norm(S, axis=1)
    shat = S / D[:, None]
    along = -np.einsum("ij,ij->i", M, shat)
    rho = np.sqrt(np.clip(np.einsum("ij,ij->i", M, M) - along**2, 0, None))
    re = R_E * k
    r_u = re - along * (R_S - re) / D
    r_p = re + along * (R_S + re) / D
    behind = along > 0
    pen = behind & (rho < r_p + R_M)
    umb = behind & (rho < r_u + R_M)
    return pen, umb


if __name__ == "__main__":
    cache = sys.argv[1]
    moon = np.load(f"{cache}/moon.npy")
    sun = np.load(f"{cache}/sun.npy")
    n = min(len(moon), len(sun))
    M, V, S = moon[:n, :3], moon[:n, 3:], sun[:n, :3]
    print(f"rows {n}; span {n*DT/86400/365.25:.2f} yr; Earth-Moon distance min {np.linalg.norm(M,axis=1).min():,.0f} max {np.linalg.norm(M,axis=1).max():,.0f} km; "
          f"Sun distance min {np.linalg.norm(S,axis=1).min():,.0f} max {np.linalg.norm(S,axis=1).max():,.0f} km")
    yrs = n * DT / 86400.0 / 365.25
    res = {"lunar_eclipse_check": []}
    for k in (1.00, 1.01, 1.02):
        pen, umb = lunar_eclipses(M, S, k)
        ps, _ = runs(pen)
        us, _ = runs(umb)
        r = {"k": k, "years": round(yrs, 2), "penumbral_or_deeper_events": int(len(ps)), "umbral_events": int(len(us)),
             "per_century_penumbral_or_deeper": round(len(ps) / yrs * 100, 1), "per_century_umbral": round(len(us) / yrs * 100, 1)}
        print("LUNAR", json.dumps(r))
        res["lunar_eclipse_check"].append(r)
    res["stations"] = []
    for name, ang in (("L4 (+60 deg)", math.radians(60)), ("L5 (-60 deg)", math.radians(-60))):
        P, nrm = rot_about_normal(M, V, ang)
        r = metrics(P, M, S, nrm)
        r["station"] = name
        print("STATION", json.dumps(r))
        res["stations"].append(r)
    print("JSON", json.dumps(res))
