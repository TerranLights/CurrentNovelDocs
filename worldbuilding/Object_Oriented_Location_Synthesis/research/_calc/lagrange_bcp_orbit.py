#!/usr/bin/env python3
"""
The Sun-forced one-month orbit about Earth-Moon L4/L5, in the planar bicircular restricted four-body model (OOLSD, 2026-10-11).
Run: python3 -I lagrange_bcp_orbit.py [orbit|eclipse|all]

MODEL (planar bicircular problem; the equations follow from point-mass gravity of Earth, Moon and Sun in the Earth-Moon rotating
frame, with the barycenter's acceleration toward the Sun as the indirect term. They are written out here and were NOT taken from a
source opened this session; stated limits)
  * Earth and Moon on circular orbits about their barycenter; the Sun on a circular orbit about that barycenter at 1 AU
    (Earth-Moon barycenter motion about the Sun treated as circular). All coplanar: the 5.145 deg inclination and the Sun's
    out-of-plane offset are NOT in the dynamics; they ARE in the eclipse geometry (section 'eclipse'), where the dynamics' in-plane
    orbit is embedded in the inclined lunar plane exactly as in lagrange_eclipse.py.
  * Units: distance = A_EM, G(M_E + M_M) = 1, rotating frame angular rate n = 1 (sidereal month). Normalized time unit = T_SID / (2 pi).
  * Third body (station) equations in the Earth-Moon rotating barycentric frame, Sun at angle theta = w_S t + theta0:
        x'' - 2 y' = Om_x,    y'' + 2 x' = Om_y
        Om = (x^2 + y^2)/2 + (1-mu)/r1 + mu/r2 + mS/r3 - (mS/aS^2)(x cos(theta) + y sin(theta))
    r1: to Earth at (-mu, 0), r2: to Moon at (1-mu, 0), r3: to Sun at aS (cos theta, sin theta).
  * w_S = (T_SID / T_YR) - 1 (the Sun's angular rate in the rotating frame, negative). The forcing is periodic with the synodic period
    2 pi / |w_S|; the 'dynamical equivalent' of L4/L5 is the periodic orbit of that period found by Newton shooting.
CONSTANTS (S = opened 2026-10-11; see research/lagrange_eclipse_calculation.md section 2 and 5.10):
  masses: Earth 5.9722e24, Moon 0.07346e24, Sun 1,988,400e24 kg (NASA fact sheets); T_SID 27.3217 d; T_YR 365.256 d; a_EM 384,400 km; 1 AU 149.598e6 km.
"""
import sys, os, math, json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
from scipy.interpolate import CubicSpline

M_E, M_M, M_S = 5.9722e24, 0.07346e24, 1988400e24
MU = M_M / (M_E + M_M)
MS = M_S / (M_E + M_M)
A_EM = 384400.0
AS = 149.598e6 / A_EM
T_SID, T_YR = 27.3217, 365.256
W_S = T_SID / T_YR - 1.0                      # rad per normalized time, negative
T_PER = 2 * math.pi / abs(W_S)                # synodic period in normalized time
DAY_PER_UNIT = T_SID / (2 * math.pi)


def rhs(t, s, th0):
    x, y, vx, vy = s
    th = W_S * t + th0
    c, sn = math.cos(th), math.sin(th)
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    r3 = math.hypot(x - AS * c, y - AS * sn)
    ox = x - (1 - MU) * (x + MU) / r1**3 - MU * (x - 1 + MU) / r2**3 - MS * (x - AS * c) / r3**3 - MS / AS**2 * c
    oy = y - (1 - MU) * y / r1**3 - MU * y / r2**3 - MS * (y - AS * sn) / r3**3 - MS / AS**2 * sn
    return [vx, vy, ox + 2 * vy, oy - 2 * vx]


def flow(s0, T, th0=0.0, dense=False, n=None):
    t_eval = np.linspace(0, T, n) if n else None
    return solve_ivp(rhs, (0, T), s0, args=(th0,), method="DOP853", rtol=1e-12, atol=1e-14, t_eval=t_eval, dense_output=dense)


def shoot(s0):
    sol = flow(s0, T_PER)
    return sol.y[:, -1] - np.asarray(s0)


def monodromy(s0, h=1e-7):
    M = np.zeros((4, 4))
    for j in range(4):
        sp, sm = np.array(s0, float), np.array(s0, float)
        sp[j] += h
        sm[j] -= h
        M[:, j] = (flow(sp, T_PER).y[:, -1] - flow(sm, T_PER).y[:, -1]) / (2 * h)
    return M


def find_orbit(guess):
    sol, info, ier, msg = fsolve(shoot, guess, full_output=True, xtol=1e-13)
    return sol, ier, float(np.max(np.abs(shoot(sol))))


def report_orbit(name, y_sign):
    L4 = [0.5 - MU, y_sign * math.sqrt(3) / 2, 0.0, 0.0]
    print(f"\n{name}: guess = the unperturbed equilateral point ({L4[0]:.6f}, {L4[1]:.6f})")
    sol, ier, res = find_orbit(L4)
    print(f"  Newton shooting: ier={ier}, residual {res:.2e}, initial state (theta0 = 0): x={sol[0]:.6f} y={sol[1]:.6f} vx={sol[2]:.6f} vy={sol[3]:.6f}")
    traj = flow(sol, T_PER, n=4001)
    x, y = traj.y[0], traj.y[1]
    xc, yc = 0.5 - MU, y_sign * math.sqrt(3) / 2
    dev = np.hypot(x - xc, y - yc)
    d_earth = np.hypot(x + MU, y)
    d_moon = np.hypot(x - 1 + MU, y)
    print(f"  distance from the equilateral point: max {dev.max():.4f} = {dev.max()*A_EM:,.0f} km; min {dev.min():.4f} = {dev.min()*A_EM:,.0f} km; mean {dev.mean()*A_EM:,.0f} km")
    print(f"  distance from Earth: {d_earth.min()*A_EM:,.0f} to {d_earth.max()*A_EM:,.0f} km; from Moon: {d_moon.min()*A_EM:,.0f} to {d_moon.max()*A_EM:,.0f} km")
    print(f"  x range {x.min()*A_EM:,.0f} to {x.max()*A_EM:,.0f} km, y range {y.min()*A_EM:,.0f} to {y.max()*A_EM:,.0f} km (from the barycenter)")
    Mn = monodromy(sol)
    ev = np.linalg.eigvals(Mn)
    print(f"  monodromy eigenvalues (|lambda|): {[round(abs(e), 6) for e in ev]}   det {np.linalg.det(Mn):.6f}  -> "
          + ("linearly stable (all |lambda| <= 1 + 1e-6)" if all(abs(e) <= 1 + 1e-6 for e in ev) else "UNSTABLE (some |lambda| > 1)"))
    # drift test: integrate 12 periods from the periodic initial state
    sol12 = solve_ivp(rhs, (0, 12 * T_PER), sol, args=(0.0,), method="DOP853", rtol=1e-12, atol=1e-14)
    d12 = np.hypot(sol12.y[0] - xc, sol12.y[1] - yc)
    print(f"  12-period integration: max distance from the equilateral point {d12.max()*A_EM:,.0f} km (periodic orbit is exact to the residual above; growth shows instability)")
    # perturbed start: displace 1000 km
    pert = np.array(sol) + np.array([1000.0 / A_EM, 0, 0, 0])
    solp = solve_ivp(rhs, (0, 60 * T_PER), pert, args=(0.0,), method="DOP853", rtol=1e-11, atol=1e-13)
    dp = np.hypot(solp.y[0] - xc, solp.y[1] - yc)
    sep = np.hypot(solp.y[0] - np.interp(solp.t % T_PER, traj.t, traj.y[0]), solp.y[1] - np.interp(solp.t % T_PER, traj.t, traj.y[1]))
    print(f"  60 periods (about {60*T_PER*DAY_PER_UNIT/365.25:.0f} yr) from a start displaced by 1,000 km: max distance from the point {dp.max()*A_EM:,.0f} km; "
          f"max separation from the periodic orbit {sep.max()*A_EM:,.0f} km")
    return sol, traj


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "orbit"
    print(f"mu = M_M/(M_E+M_M) = {MU:.7f}; mS = {MS:,.1f}; aS = {AS:.3f}; w_S = {W_S:.6f}; synodic period = {T_PER:.5f} units = {T_PER*DAY_PER_UNIT:.4f} d")
    orb = {}
    for name, sgn in (("L4", +1.0), ("L5", -1.0)):
        orb[name] = report_orbit(name, sgn)
    np.save(os.environ.get("BCP_OUT", "/tmp") + "/bcp_orbit_L4.npy", np.vstack([orb["L4"][1].t, orb["L4"][1].y]))
    np.save(os.environ.get("BCP_OUT", "/tmp") + "/bcp_orbit_L5.npy", np.vstack([orb["L5"][1].t, orb["L5"][1].y]))
