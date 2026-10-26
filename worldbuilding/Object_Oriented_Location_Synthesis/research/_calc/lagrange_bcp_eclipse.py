#!/usr/bin/env python3
"""Eclipse statistics for a station on the Sun-forced periodic orbits about Earth-Moon L4/L5 (OOLSD, 2026-10-11).
Run: python3 -I lagrange_bcp_eclipse.py     (needs bcp_orbits_L4.json and bcp_orbits_L5.json from lagrange_bcp_search.py)

The in-plane orbit (planar bicircular model) is embedded in the inclined lunar plane exactly as the Moon is in lagrange_eclipse.py
(circular model, same constants, same 111.56-year span, 120 s steps). The Sun's phase relative to the Moon, Delta(t), advances at
(n_sun - n_sidereal) and sets the orbit's phase through theta = Delta(t) (mod 2 pi). The station is a point; Earth and Moon are discs."""
import sys, os, json, math
import numpy as np
from scipy.interpolate import CubicSpline
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lagrange_eclipse as LE
from lagrange_eclipse import R_E, R_S, R_M, D_ES, A_EM, INC, N_DRA, N_SUN, N_SID, OMEGA_DOT, DT, YEARS, CHUNK, frac_obscured, runs
from lagrange_bcp_orbit import MU, W_S, T_PER, flow

CI, SI = math.cos(INC), math.sin(INC)


def orbit_spline(state):
    tr = flow(state, T_PER, n=7201)
    tau = tr.t
    yx, yy = tr.y[0].copy(), tr.y[1].copy()
    yx[-1], yy[-1] = yx[0], yy[0]               # close the orbit (shooting residual is ~1e-14)
    cx = CubicSpline(tau, yx, bc_type="periodic")
    cy = CubicSpline(tau, yy, bc_type="periodic")
    return cx, cy


def run_orbit(state, seed):
    cx, cy = orbit_spline(state)
    rng = np.random.default_rng(seed)
    lam0, om0, u0 = rng.uniform(0, 2 * math.pi, 3)
    n = int(YEARS * 365.25 * 86400 / DT)
    fE = np.zeros(n, dtype=np.float32)
    fM = np.zeros(n, dtype=np.float32)
    dEmin, dEmax = 1e99, 0.0
    for i0 in range(0, n, CHUNK):
        i1 = min(n, i0 + CHUNK)
        t = np.arange(i0, i1) * DT / 86400.0
        lam = lam0 + N_SUN * t
        om = om0 + OMEGA_DOT * t
        u = u0 + N_DRA * t
        delta = (lam - om - u)                       # Sun's angle from the Moon, in the lunar plane
        th = np.mod(delta, 2 * math.pi)
        tau = np.mod((2 * math.pi - th) / abs(W_S), T_PER)
        x, y = cx(tau), cy(tau)
        X = (x + MU) * np.cos(u) - y * np.sin(u)
        Y = (x + MU) * np.sin(u) + y * np.cos(u)
        e1 = np.stack([np.cos(om), np.sin(om), np.zeros_like(om)], axis=1)
        e2 = np.stack([-CI * np.sin(om), CI * np.cos(om), np.full_like(om, SI)], axis=1)
        P = A_EM * (X[:, None] * e1 + Y[:, None] * e2)
        M = A_EM * (np.cos(u)[:, None] * e1 + np.sin(u)[:, None] * e2)
        S = D_ES * np.stack([np.cos(lam), np.sin(lam), np.zeros_like(lam)], axis=1)
        PS = S - P
        dPS = np.linalg.norm(PS, axis=1)
        rs = np.arcsin(R_S / dPS)
        PE = -P
        dPE = np.linalg.norm(PE, axis=1)
        dEmin, dEmax = min(dEmin, float(dPE.min())), max(dEmax, float(dPE.max()))
        c = np.einsum("ij,ij->i", PS, PE) / (dPS * dPE)
        fE[i0:i1] = frac_obscured(rs, np.arcsin(R_E / dPE), np.arccos(np.clip(c, -1, 1)))
        PM = M - P
        dPM = np.linalg.norm(PM, axis=1)
        c = np.einsum("ij,ij->i", PS, PM) / (dPS * dPM)
        fM[i0:i1] = frac_obscured(rs, np.arcsin(R_M / dPM), np.arccos(np.clip(c, -1, 1)))
    yrs = n * DT / 86400.0 / 365.25
    out = {"years": round(yrs, 2), "earth_distance_km": [round(dEmin), round(dEmax)]}

    def ev(name, flag):
        s, l = runs(flag)
        dur = l * DT / 60.0
        d = {"events_per_year": round(len(s) / yrs, 3), "time_fraction_pct": round(float(flag.mean()) * 100, 4)}
        if len(s):
            d.update({"dur_min_mean": round(float(dur.mean()), 1), "dur_min_median": round(float(np.median(dur)), 1),
                      "dur_min_max": round(float(dur.max()), 1)})
            if len(s) > 1:
                d["gap_days_max"] = round(float(((s[1:] - (s[:-1] + l[:-1])) * DT / 86400.0).max()), 1)
        out[name] = d

    ev("earth_any", fE > 0.0)
    ev("earth_total", fE >= 0.999)
    ev("moon_any", fM > 0.0)
    ev("moon_ge90pct", fM >= 0.9)
    ev("moon_total", fM >= 0.999)
    ev("either_any", (fE > 0.0) | (fM > 0.0))
    ev("whole_sun_hidden", (fE + fM) >= 0.999)
    out["moon_max_obscuration"] = round(float(fM.max()), 4)
    out["mean_sunlight_lost_pct"] = round(float((fE + fM).mean()) * 100, 4)
    return out


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    results = []
    for name in ("L4", "L5"):
        orbits = json.load(open(os.path.join(here, f"bcp_orbits_{name}.json")))
        for o in sorted(orbits, key=lambda o: o["dev_max_km"]):
            kind = "small forced orbit (unstable)" if o["max_abs_eig"] > 1.0 + 1e-6 else "large orbit (stable)"
            r = run_orbit(np.array(o["state"]), seed=0)
            r.update({"point": name, "kind": kind, "orbit_dev_max_km": round(o["dev_max_km"]), "orbit_dev_mean_km": round(o["dev_mean_km"])})
            print("ORBIT", json.dumps(r))
            results.append(r)
    print("JSON", json.dumps(results))
