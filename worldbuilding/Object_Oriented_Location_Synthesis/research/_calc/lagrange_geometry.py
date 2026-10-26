#!/usr/bin/env python3
"""Closed-form geometry for the L4/L5 eclipse question (OOLSD, 2026-10-11). Run: python3 -I lagrange_geometry.py
Constants (S): NASA Earth/Moon/Sun fact sheets, see research/lagrange_eclipse_calculation.md section 2."""
import math

R_E, R_S, R_M = 6378.137, 695700.0, 1737.4         # km
D_ES = 149.598e6                                   # km
A_EM = 384400.0                                    # km
V_ORB = 2 * math.pi * A_EM / (27.3217 * 86400.0)   # km/s, orbital speed of the Moon and of L4/L5 (sidereal 27.3217 d)

print("== A. Earth's shadow cones (geometric, no atmosphere)")
L_umbra = R_E * D_ES / (R_S - R_E)
print(f"  umbra length = R_E D / (R_S - R_E) = {R_E} x {D_ES:.4g} / ({R_S} - {R_E}) = {L_umbra:,.0f} km")
for d in (A_EM,):
    ru = R_E - d * (R_S - R_E) / D_ES
    rp = R_E + d * (R_S + R_E) / D_ES
    print(f"  at d = {d:,.0f} km: umbra radius = {R_E} - {d:,.0f} x ({R_S}-{R_E})/{D_ES:.4g} = {ru:,.0f} km; penumbra radius = {R_E} + {d:,.0f} x ({R_S}+{R_E})/{D_ES:.4g} = {rp:,.0f} km")
    print(f"  orbital speed of the station = 2 pi {A_EM:,.0f} / (27.3217 x 86,400 s) = {V_ORB:.4f} km/s")
    sun_rate = 2 * math.pi / (365.256 * 86400.0) * d
    print(f"  the shadow axis moves with the Sun at {sun_rate:.4f} km/s at that distance; relative speed {V_ORB - sun_rate:.4f} km/s")
    print(f"  central chord through the umbra: 2 x {ru:,.0f} / {V_ORB - sun_rate:.4f} = {2*ru/(V_ORB-sun_rate)/60:.0f} min")
    print(f"  central chord through the penumbra: 2 x {rp:,.0f} / {V_ORB - sun_rate:.4f} = {2*rp/(V_ORB-sun_rate)/60:.0f} min")

print("\n== B. Angular sizes seen from an Earth-Moon L4/L5 point (distance to Earth and to Moon both = 384,400 km)")
a_sun = math.degrees(math.asin(R_S / D_ES))
a_earth = math.degrees(math.asin(R_E / A_EM))
a_moon = math.degrees(math.asin(R_M / A_EM))
print(f"  Sun angular radius {a_sun:.4f} deg; Earth {a_earth:.4f} deg; Moon {a_moon:.4f} deg")
print(f"  Moon/Sun disc-area ratio = ({a_moon:.4f}/{a_sun:.4f})^2 = {(a_moon/a_sun)**2:.3f} (best-case annular obscuration, matches the simulation's 0.947)")
print(f"  Earth/Sun disc-area ratio = {(a_earth/a_sun)**2:.1f} (Earth fully covers the Sun when aligned)")

print("\n== C. Sun-Earth L4/L5 (vertices of an equilateral triangle with the Sun and Earth)")
print("  As seen from L4/L5 the Sun-to-Earth angular separation is 60 deg (equilateral triangle).")
a_earth_se = math.degrees(math.asin(R_E / D_ES))
a_moon_se = math.degrees(math.asin(R_M / D_ES))
print(f"  Earth angular radius from L4 = asin({R_E}/{D_ES:.4g}) = {a_earth_se:.5f} deg; Moon {a_moon_se:.5f} deg; Sun {a_sun:.4f} deg")
print(f"  Occultation needs separation < {a_sun + a_earth_se:.4f} deg; the separation is 60 deg, so the Earth or Moon never occults the Sun: margin factor {60/(a_sun+a_earth_se):.0f}.")
print(f"  Earth's umbra ends {L_umbra:,.0f} km behind the Earth, {L_umbra/D_ES*100:.2f} % of the Earth-Sun distance; L4/L5 are {D_ES:,.0f} km from Earth, off the shadow axis.")
print("  The corotating Sun-Earth frame turns once per year; a station fixed in it sees the Sun at a fixed direction (60 deg off the Earth direction).")

print("\n== D. Sun direction in the Earth-Moon rotating frame")
syn = 29.530589
print(f"  The Sun's azimuth in the frame rotating with the Moon sweeps 360 deg per synodic month: {360/syn:.2f} deg/day (retrograde).")
print(f"  Its elevation above the lunar orbit plane is within +/-5.145 deg (inclination) plus parallax; simulation max 5.158 deg.")
print(f"  Elevation oscillation period = eclipse year; simulation 346.614 d. A one-axis array turning once per {syn} d tracks it with cos(5.158 deg) = {math.cos(math.radians(5.158)):.4f} (loss {100*(1-math.cos(math.radians(5.158))):.2f} %).")
