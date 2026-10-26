#!/usr/bin/env python3
"""
Eclipse and Sun-angle statistics for a point station at Earth-Moon L4/L5 (OOLSD, 2026-10-11).

Run with:  python3 -I lagrange_eclipse.py [validate|l45|all]

MODEL (stated limits)
  * Earth-centered ecliptic inertial frame. The Sun is on the ecliptic at mean distance D_ES, moving at the
    sidereal year rate (eccentricity of the Earth's orbit ignored).
  * The Moon is on a CIRCULAR orbit of radius A_EM, inclination INC to the ecliptic, argument of latitude
    advancing at the draconic rate, node longitude regressing at (n_sidereal - n_draconic). Lunar orbit
    eccentricity (0.0549), evection, variation and the other solar perturbations are ignored.
  * L4/L5 are the vertices of the equilateral triangle with Earth and Moon: the same circle and plane as the
    Moon, +/-60 degrees in argument of latitude, same radius. (Circular restricted three-body limit; the
    real points are quasi-stable under the Sun's perturbation and a real station librates about them.)
  * The station is a POINT. The Sun is a uniform disc. Earth and Moon are discs.
  * Obscuration = overlap area of the occulter disc with the Sun disc, as seen from the station.

CONSTANTS (each opened this session; sources in research/lagrange_eclipse_calculation.md section 2)
"""
import math, sys, json
import numpy as np

R_E = 6378.137          # km  NASA Earth fact sheet, equatorial radius
R_S = 695700.0          # km  NASA Sun fact sheet, volumetric mean radius
R_M = 1737.4            # km  NASA Moon fact sheet, volumetric mean radius
D_ES = 149.598e6        # km  NASA Earth fact sheet, semimajor axis
A_EM = 384400.0         # km  NASA Moon fact sheet, semimajor axis (0.3844e6)
INC = math.radians(5.145)   # NASA Moon fact sheet, inclination to ecliptic
T_SID = 27.3217         # d   NASA Moon fact sheet, revolution (sidereal) period
T_DRA = 27.212221       # d   NASA eclipse site (Espenak), draconic month
T_YR = 365.256          # d   NASA Earth fact sheet, sidereal orbit period
T_SYN = 29.530589       # d   NASA eclipse site, synodic month (check value)

N_DRA = 2 * math.pi / T_DRA
N_SID = 2 * math.pi / T_SID
N_SUN = 2 * math.pi / T_YR
OMEGA_DOT = N_SID - N_DRA          # rad/d, negative: nodes regress
DT = 120.0                          # s, time step
YEARS = 6 * (2 * math.pi / abs(OMEGA_DOT)) / 365.25   # six nodal cycles
CHUNK = 1_000_000


def moon_vec(u, om):
    cu, su, co, so = np.cos(u), np.sin(u), np.cos(om), np.sin(om)
    ci, si = math.cos(INC), math.sin(INC)
    x = cu * co - su * ci * so
    y = cu * so + su * ci * co
    z = su * si
    return A_EM * np.stack([x, y, z], axis=1)


def frac_obscured(rs, ro, d):
    """Fraction of the Sun disc (angular radius rs) covered by an occulter disc (ro) at separation d (rad)."""
    f = np.zeros_like(d)
    rs_a = np.broadcast_to(rs, d.shape)
    ro_a = np.broadcast_to(ro, d.shape)
    near = d < (rs_a + ro_a)
    inside = d <= np.abs(ro_a - rs_a)
    big = near & inside     # one disc entirely inside the other
    f[big] = np.where(ro_a[big] >= rs_a[big], 1.0, (ro_a[big] / rs_a[big]) ** 2)
    lens = near & ~inside
    if lens.any():
        dd, a, b = d[lens], rs_a[lens], ro_a[lens]
        c1 = np.clip((dd**2 + a**2 - b**2) / (2 * dd * a), -1, 1)
        c2 = np.clip((dd**2 + b**2 - a**2) / (2 * dd * b), -1, 1)
        k = (-dd + a + b) * (dd + a - b) * (dd - a + b) * (dd + a + b)
        area = a**2 * np.arccos(c1) + b**2 * np.arccos(c2) - 0.5 * np.sqrt(np.clip(k, 0, None))
        f[lens] = area / (math.pi * a**2)
    return f


def runs(flag):
    """Return (starts, lengths) of True runs in a 1-D bool array."""
    x = np.concatenate(([False], flag, [False])).astype(np.int8)
    d = np.diff(x)
    s = np.flatnonzero(d == 1)
    e = np.flatnonzero(d == -1)
    return s, e - s


def validate(seed, k_enl):
    """Moon in Earth's shadow, circular model, counts per century (NASA 2001-2100: 228 total, 142 umbral)."""
    rng = np.random.default_rng(seed)
    lam0, om0, u0 = rng.uniform(0, 2 * math.pi, 3)
    n = int(YEARS * 365.25 * 86400 / DT)
    pen = np.zeros(n, dtype=bool)
    umb = np.zeros(n, dtype=bool)
    for i0 in range(0, n, CHUNK):
        i1 = min(n, i0 + CHUNK)
        t = np.arange(i0, i1) * DT / 86400.0
        lam = lam0 + N_SUN * t
        s_hat = np.stack([np.cos(lam), np.sin(lam), np.zeros_like(lam)], axis=1)
        M = moon_vec(u0 + N_DRA * t, om0 + OMEGA_DOT * t)
        along = -np.einsum("ij,ij->i", M, s_hat)          # distance behind Earth along the anti-Sun axis
        rho = np.sqrt(np.clip(np.einsum("ij,ij->i", M, M) - along**2, 0, None))
        re = R_E * k_enl
        r_u = re - along * (R_S - re) / D_ES
        r_p = re + along * (R_S + re) / D_ES
        behind = along > 0
        umb[i0:i1] = behind & (rho < r_u + R_M)
        pen[i0:i1] = behind & (rho < r_p + R_M)
    ps, pl = runs(pen)
    us, ul = runs(umb)
    yrs = n * DT / 86400.0 / 365.25
    return {"seed": seed, "k": k_enl, "years": round(yrs, 2),
            "penumbral_or_deeper_per_century": round(len(ps) / yrs * 100, 1),
            "umbral_per_century": round(len(us) / yrs * 100, 1)}


def station(seed, phase_deg):
    """Point station at u_moon + phase. Returns metrics dict."""
    rng = np.random.default_rng(seed)
    lam0, om0, u0 = rng.uniform(0, 2 * math.pi, 3)
    ph = math.radians(phase_deg)
    n = int(YEARS * 365.25 * 86400 / DT)
    fE = np.zeros(n, dtype=np.float32)
    fM = np.zeros(n, dtype=np.float32)
    elev_max = 0.0
    elev_sum = 0.0
    elev_abs_gt2 = 0
    for i0 in range(0, n, CHUNK):
        i1 = min(n, i0 + CHUNK)
        t = np.arange(i0, i1) * DT / 86400.0
        lam = lam0 + N_SUN * t
        S = D_ES * np.stack([np.cos(lam), np.sin(lam), np.zeros_like(lam)], axis=1)
        um = u0 + N_DRA * t
        om = om0 + OMEGA_DOT * t
        M = moon_vec(um, om)
        P = moon_vec(um + ph, om)
        PS = S - P
        dPS = np.linalg.norm(PS, axis=1)
        rs = np.arcsin(R_S / dPS)
        # Earth occulter
        PE = -P
        dPE = np.linalg.norm(PE, axis=1)
        cosd = np.einsum("ij,ij->i", PS, PE) / (dPS * dPE)
        dE = np.arccos(np.clip(cosd, -1, 1))
        fE[i0:i1] = frac_obscured(rs, np.arcsin(R_E / dPE), dE)
        # Moon occulter
        PM = M - P
        dPM = np.linalg.norm(PM, axis=1)
        cosd = np.einsum("ij,ij->i", PS, PM) / (dPS * dPM)
        dM = np.arccos(np.clip(cosd, -1, 1))
        fM[i0:i1] = frac_obscured(rs, np.arcsin(R_M / dPM), dM)
        # Sun elevation above the lunar orbital plane, seen from the station
        zhat = np.stack([math.sin(INC) * np.sin(om), -math.sin(INC) * np.cos(om),
                         np.full_like(om, math.cos(INC))], axis=1)
        el = np.degrees(np.arcsin(np.einsum("ij,ij->i", PS / dPS[:, None], zhat)))
        elev_max = max(elev_max, float(np.abs(el).max()))
        elev_sum += float(np.abs(el).sum())
        elev_abs_gt2 += int((np.abs(el) > 2.0).sum())
    yrs = n * DT / 86400.0 / 365.25
    out = {"seed": seed, "phase_deg": phase_deg, "years": round(yrs, 2),
           "sun_elev_abs_max_deg": round(elev_max, 3),
           "sun_elev_abs_mean_deg": round(elev_sum / n, 3),
           "frac_time_sun_elev_abs_gt_2deg": round(elev_abs_gt2 / n, 4)}

    def ev(name, flag):
        s, l = runs(flag)
        dur = l * DT / 60.0
        d = {"events": int(len(s)), "events_per_year": round(len(s) / yrs, 3),
             "time_fraction": float(flag.mean())}
        if len(s):
            d.update({"dur_min_mean": round(float(dur.mean()), 1), "dur_min_median": round(float(np.median(dur)), 1),
                      "dur_min_p90": round(float(np.percentile(dur, 90)), 1), "dur_min_max": round(float(dur.max()), 1)})
            gaps = (s[1:] - (s[:-1] + l[:-1])) * DT / 86400.0
            if len(gaps):
                d["gap_days_max"] = round(float(gaps.max()), 1)
                d["gap_days_median"] = round(float(np.median(gaps)), 1)
        out[name] = d

    ev("earth_any_obscuration", fE > 0.0)
    ev("earth_ge50pct", fE >= 0.5)
    ev("earth_total_f_ge_0.999", fE >= 0.999)
    ev("moon_any_obscuration", fM > 0.0)
    out["moon_max_obscuration"] = round(float(fM.max()), 4)
    ev("moon_ge50pct", fM >= 0.5)
    ev("either_any", (fE > 0.0) | (fM > 0.0))
    ev("either_total_loss_ge_0.999", (fE + fM) >= 0.999)
    out["mean_sunlight_lost_fraction"] = float((fE + fM).mean())
    return out


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"constants: R_E={R_E} R_S={R_S} R_M={R_M} D_ES={D_ES} A_EM={A_EM} INC={math.degrees(INC)} deg")
    print(f"rates: N_DRA={N_DRA:.9f} N_SID={N_SID:.9f} OMEGA_DOT={OMEGA_DOT:.9f} rad/d -> node regression period "
          f"{2*math.pi/abs(OMEGA_DOT):.2f} d = {2*math.pi/abs(OMEGA_DOT)/365.25:.3f} yr; simulated years {YEARS:.2f}; dt {DT} s")
    syn = 2 * math.pi / (N_SID - N_SUN)
    eclyr = 2 * math.pi / (N_SUN - OMEGA_DOT)
    print(f"derived: synodic month {syn:.5f} d (NASA 29.530589); eclipse year {eclyr:.3f} d")
    res = {}
    if mode in ("validate", "all"):
        res["validation"] = []
        for k in (1.00, 1.01, 1.02):
            for seed in (0, 1, 2):
                r = validate(seed, k)
                print("VALIDATE", json.dumps(r))
                res["validation"].append(r)
    if mode in ("l45", "all"):
        res["stations"] = []
        for phase in (60.0, -60.0):
            for seed in (0, 1, 2):
                r = station(seed, phase)
                print("STATION", json.dumps(r))
                res["stations"].append(r)
    print("JSON", json.dumps(res))
