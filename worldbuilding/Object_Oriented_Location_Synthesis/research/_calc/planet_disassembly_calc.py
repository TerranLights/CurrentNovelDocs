#!/usr/bin/env python3
"""Order-of-magnitude arithmetic for disassembling Mercury or Venus whole (OOLSD, 2026-10-11). Run: python3 -I planet_disassembly_calc.py
Inputs are sourced constants from the research files: GM and radius from the JPL/NSSDC values used in space_trucking_and_transport_infrastructure.md (F1)
and starlifting_physics_and_minimum_infrastructure.md (D6, 3F); G = 6.674e-11 as in starlifting file D6; luminosity 3.828e26 W; solar flux values from the NSSDC fact sheets.
The Armstrong and Sandberg figures (31 yr 85 d; 1.80e30 J; 3.92 kg/m2 = 0.5 mm iron; capture 1/3, 1/10 to drivers, 5-yr lag, half the mass usable) are quoted from
starlifting_physics_and_minimum_infrastructure.md 3F. A uniform-sphere binding energy 3GM^2/(5R) is used for both planets; real planets are centrally condensed,
so the true binding energy is higher (not sourced here). This is NOT a design; it sets scales only."""
import math

G = 6.674e-11
L_SUN = 3.828e26
YR = 3.15576e7
AU = 1.495978707e11
bodies = {
    "Mercury": dict(GM=2.2032e13, R=2.4397e6, a=0.38709927, flux=9082.7),
    "Venus":   dict(GM=3.2486e14, R=6.0518e6, a=0.72333566, flux=2601.3),
}
atm_venus = 4.8e20          # kg [SL 3F / NSSDC]
atm_remove_MJ = 50.0        # MJ/kg to remove Venus's atmosphere to space [VE 3.10, Landis 2011]

def hdr(s):
    print("\n" + "=" * 96 + "\n" + s + "\n" + "=" * 96)

res = {}
for name, b in bodies.items():
    M = b["GM"] / G
    U = 3 * b["GM"] ** 2 / (5 * G * b["R"])
    u_kg = 3 * b["GM"] / (5 * b["R"])
    vesc = math.sqrt(2 * b["GM"] / b["R"])
    res[name] = dict(M=M, U=U, u_kg=u_kg)
    hdr(f"{name}")
    print(f"mass from GM/G = {M:.4e} kg; surface escape {vesc/1e3:.2f} km/s = {0.5*vesc**2/1e6:.1f} MJ/kg")
    print(f"uniform-sphere binding energy 3GM^2/(5R) = {U:.3e} J; mean {u_kg/1e6:.1f} MJ/kg (the average cost per kg over the whole disassembly if each kg only needs to escape the planet)")
    print(f"= {U/(L_SUN):.3e} s of the Sun's entire output ({U/L_SUN/YR:.3e} yr)")
    for T in (31.2, 100.0, 1000.0, 10000.0):
        P = U / (T * YR)
        flow = M / (T * YR)
        print(f"   in {T:>7,.1f} yr: mean power {P:.2e} W = {P/L_SUN:.2e} of solar luminosity; mean mass flow {flow:.2e} kg/s ({flow*YR/1e3:.2e} t/yr)")
    cross = math.pi * b["R"] ** 2
    print(f"sunlight the planet's own disc intercepts at its orbit: {cross*b['flux']:.2e} W; to supply the 31-yr mean power at 1/3 efficiency and 1/10 to drivers one needs collectors of {U/(31.2*YR)/(b['flux']/3/10):.2e} m2")
    sphere = 4 * math.pi * (b["a"] * AU) ** 2
    print(f"sphere at the orbit radius ({b['a']} AU): {sphere:.2e} m2; collectors needed = {U/(31.2*YR)/(b['flux']/30)/sphere:.1e} of that sphere")
    print(f"if ALL the mass were spread over that sphere: {M/sphere:.2f} kg/m2 (the paper's 3.92 kg/m2 = 0.5 mm of iron at the same conversion = {0.5/3.92*M/sphere:.2f} mm)")

hdr("Mercury check against Armstrong and Sandberg")
print(f"A&S binding energy 1.80e30 J; here {res['Mercury']['U']:.3e} J")
print(f"A&S: swarm at Mercury's orbit of 3.92 kg/m2 over the sphere = {3.92*4*math.pi*(0.38709927*AU)**2:.2e} kg = {3.92*4*math.pi*(0.38709927*AU)**2/res['Mercury']['M']*100:.0f} % of Mercury's mass (they say half the mass usable)")

hdr("Venus extras")
print(f"Venus / Mercury: mass {res['Venus']['M']/res['Mercury']['M']:.1f}x, binding energy {res['Venus']['U']/res['Mercury']['U']:.0f}x, mean MJ/kg {res['Venus']['u_kg']/res['Mercury']['u_kg']:.1f}x")
Ea = atm_venus * atm_remove_MJ * 1e6
print(f"atmosphere: {atm_venus:.1e} kg = {atm_venus/res['Venus']['M']*100:.4f} % of Venus's mass; removal energy at {atm_remove_MJ:.0f} MJ/kg = {Ea:.2e} J (Landis 2011 quoted 2.5e28 J for the whole atmosphere in [VE] 3.10) = {Ea/res['Venus']['U']*100:.2f} % of the solid planet's binding energy")
print(f"Venus's disc intercepts only {math.pi*bodies['Venus']['R']**2*bodies['Venus']['flux']:.2e} W; 735 K surface radiates {5.670374e-8*735**4:.2e} W/m2 (sigma T^4), the whole planet {5.670374e-8*735**4*4*math.pi*bodies['Venus']['R']**2:.2e} W")
print("Armstrong and Sandberg's model was run for Mercury only in the sources read; no Venus solid-body disassembly study was found in any tranche file")
