# Canon adjustment proposals (from the physics comparison)

*Step 4 of `_canon_comparison_CHECKPOINT.md`, written 2026-10-12. **Proposals only. Nothing here has been applied to any canon file, and none is binding.** Each follows
the "both-are-true" test: it first says what canon can keep as it stands, then what the physics suggests adding or changing. Row numbers (R7, R24) refer to
`canon_vs_physics_comparison.md`; K-IDs to `_canon_extract_interplanetary.md`.*

**Headline.** Of 32 compared rows, none is a CONFLICT: **canon is physically allowed everywhere the research reaches.** Its dates are 2.6 to 10 times longer than the physics needs
(R5, R30), so no date has to move. What the research exposes are **gaps** (canon says nothing where physics says a decision is needed) and **two tensions**. The proposals are
ordered by consequence.

**Where each proposal lives.** Orbital-society questions belong to the Cryptograph Helix repo (`OCH` boundary). Proposals marked **[IT]** concern this repo (facts that Inner
Tepenia establishes); **[HELIX]** concern the Helix repo; **[BOTH]** need coordination.

---

## AP-1 [BOTH]. State where the orbital mass came from (R8, R9, R27; canon gap K-9, K-26)

**Canon can keep as it stands:** every date, the three stages, 10,104,964 orbital people. Nothing here contradicts it.

**The gap.** `Orbital_Infrastructure_Mass_Budget.md` says debris alone supports at most about 1,000 to 2,000 people and that more needs lunar or asteroid imports "unless canon separately establishes"
otherwise. Canon has not. The physics sizes the need: **0.1 to 23.6 Gt** for 10.1 million people (calc 1), which is 6,000 to 1.5 million times the 16,200 t debris budget; it is reached at an
average 0.2 to 51 Mt/yr over canon's 472 years (calc 2), and the research's bulk sources that pass break-even are the **Moon and near-Earth or carbonaceous asteroids** for Earth-side
material and the **main belt** for Mars (VAL G, IMS section 6).

**Options.**
- **A (recommended, minimal).** One sentence of canon: *bulk orbital mass comes from lunar and near-Earth-asteroid industry; Earth supplies chips, magnets, lithium and people.* It matches the
  physics, the cheapest by delta-v (lunar surface to LEO 2.52 km/s, 5 days) and by energy (lunar escape 2.83 MJ/kg vs 33.1 MJ/kg from Earth's surface), and leaves the Tower free to be the
  passenger and high-value channel.
- **B.** Tower-sourced Earth material only. Possible (82 Mt/yr costs 26.5% of the Tower's 324 GW, R10) but each tonne needs about 4.8 t of final-stage propellant, and it ties the build-up to
  the post-2688 window, which cuts the build time from 472 to 124 years. Not recommended.
- **C.** Leave it silent. Physics permits; the mass-budget file's own guidance asks for it to be stated before orbital composition work starts.

**Downstream.** Option A means a lunar industrial history exists by the late 2300s to 2400s (physics: Mt/yr-class industry 25 to 48 years after commitment, R5), which has no canon yet. It also feeds
the reserved Orbital Composition task.

**Not proposed:** any Mercury, Venus or solar-matter source (they fail break-even, IMS/PHB); any change to dates.

## AP-2 [IT]. Fix the dose standard the orbital population lives under (R7)

**Canon can keep:** the low-shield "10 to 20 t/person" figure as a valid *crew* case.

**The tension.** That figure gives worker-level dose (LEO/ISS dose is about 70 to 180 mSv/yr; SP-413's general-population design is 5 mSv/yr at 4.5 t/m^2). For a population of families and children
the mass per person is 98 to 2,333 t, which is 5 to 230 times larger. The same choice sets RL-1's open item (the register's ruling that robots need "the degree a human requires").

**Option (the decision).** Pick the numeric dose budget: (a) general-population standard for everyone; (b) worker-level for adults, general-population shelters and nurseries; (c) different standards
by orbit (inside vs outside the belts). Each gives a different mass and a different feel to orbital life. Recommended: (b), because it matches both the 10 to 20 t/person case and a
multigenerational population with a protected core.

**Downstream.** Edit the mass-budget file's caveat; answers RL-1's open dose item; changes the per-person mass used in AP-1. **Not proposed:** changing any population number.

## AP-3 [IT]. Put a tonnage and the final-stage reality on the Tower's "bulk export" (R10, R12)

**Canon can keep:** the Tower's design, its primary purposes, its 2688 date.

**The gap.** The Tower file states bulk export as a primary purpose and no tonnage. Physics: 8 Mt/yr costs 8.4 GW ideal (2.6% of the net draw) and 82 Mt/yr costs 86 GW (26.5%); the pellet loop
is under 1% by mass. But the Tower delivers 3.62 km/s of a 7.82 km/s need, so a final stage is **82.8% propellant** (4.83 t per tonne) at hydrolox Isp, and the South Pole means polar orbits.
**Options:** (a) add "on the order of several Mt/yr, final-stage dominated" to the Tower file; (b) leave it unquantified. **Open thread, not a proposal:** what a polar-orbit-only Tower implies
for equatorial cylinders and Mars departures (no research file covers it); recommended as the next small research item.

**Not proposed:** changing the structure's height, power or date.

## AP-4 [HELIX]. Clarify what Venus's "mines" and "exploitation" are (R23, R24)

**Canon can keep:** floating prison gulags, a Venus occupied and exploited in the ~300 to 500 years after the war.

**The tension.** Physics supports cloud-level habitation (about 0.9 g, ~1 bar, the best radiation shelter outside Earth) and extraction of carbon, nitrogen, oxygen and sulfur from the air for the platforms'
own use. It does not support exporting bulk material or gas to Mars or Earth (180 to 670 kt lifted per kt delivered; Earth's air is richer in nitrogen and argon).
**Options:** (a) "mines" = atmospheric extraction for Venus's own platforms; exploitation = labor, location and strategic position (gravity-assist waypoint, 584-day windows); exports are people, data and
small high-value items. (b) If the story needs Venus to supply Mars or Earth with tonnage, treat it as a stated handwave (register C-81, C-95: a non-rocket Venus launch) rather than letting the physics
imply it. (c) Surface "mines" read as the tall tale or the myth of the gulags, not a working fact (737 K, 92 bar, landers last two hours).

**Not proposed:** changing the gulags or their dates.

## AP-5 [BOTH]. Resolve three canon-internal items (R13, R28; K-21/K-22)

These are inconsistencies between canon files, not physics. Reported only.
- **Tower window:** the At-a-Glance table uses ~178 years and 6.48 people/h; the Throughput section uses ~124 years and 9.30 people/h (the 2688 resolution). Both calculations are right; the old window should be retired
  (`Amundsen_Tower_Space_Fountain_Design.md`).
- **12 million vs 10,104,964:** the reconciliation is open; physics shows the throughput is no constraint (11.04 vs 9.30 people/h against a 194/h design).
- **Mass-budget wording:** `Orbital_Infrastructure_Mass_Budget.md` (lines 85-86) contrasts its 10-20 t/person case with "millions of tonnes/person in fully-shielded deep-space designs"; its own 1-10 Mt for 5,000-10,000 people, and SP-413's torus, are about 1,000 t/person. "Millions" should read "about a thousand" (found in the step-5 audit).
- **Mars:** K-21 ("active plans to colonize Mars itself" at the game present) and K-22 ("colonization began during the Second Interwar Period") read differently; physics permits either (R17, R18). Pick one reading.

## AP-6 [HELIX]. Say where Mars's water is (R20)

**Canon can keep:** silence about water.

**Why say it.** The developer's own idea (oxygen from Mercury or Venus plus hydrogen from the Sun, trucked to Mars) fails on cost (OHM): Mars already has 16 to 22 m of global-equivalent water in its caps and
20 to 40 m near the surface, 43 wt% oxygen soil, and slow loss to space (MWB). **Options:** (a) canon states Mars's water is local ice, with import only for an ocean-scale project; (b) if the fiction wants an
imported-water Mars, mark it as a handwave with the numbers (register C-129 to C-132, C-133). **Not proposed:** any Mercury/Sun-sourced water.

## AP-7 [none]. Keep the cylinder and wheel roles; record the design note (R3, R4)

The developer's note (early space trucking may involve O'Neill Cylinders) is physically defensible only in one form: a cylinder-class habitat **built in place** on its slow orbit, after Mt/yr industry exists
(about 25 to 48 years after commitment, SYN). As a moved vehicle it fails (10 to 62 years of 10 GW thrust for the 80.2 Mt cylinder). Canon already gives cylinders the residence role and wheels the mobility role,
which is exactly what the physics supports. **No canon change.** If the note is wanted in fiction: "cylinders as waystations and depots on slow orbits," built where they stay; "wheels" as the small crewed
transports (a cycler-class vehicle, about 70 t for 10 people).

## AP-8 [IT]. Do not compress the dates

Canon's 348 years from the staging stations to the Tower and 472 to the war are 2.6 to 10 times the physics chain (R30). **No date should move.** The slack is a feature: it absorbs the dependency lags,
slow growth and setbacks the research flags (SYN section 5; register C-64, C-65, C-68), and Mars has 185 to 290 years between the game present and the Helix opening against a physics need of under 110 (R19, R32).

## AP-9 [BOTH, optional]. Fill silences only if wanted: the Moon, Mercury, the Sun (R27)

Canon says nothing about the Moon, Mercury or the Sun. If the developer wants them, the research gives the following *minimal true statements*: the Moon is the natural early industrial site (AP-1);
Mercury is an energy-rich site for local construction, not an Earth supplier; the Sun contributes light and gravity, not matter. **Not proposed:** a Mercury iron mine, planetary disassembly, or solar-matter harvesting
at any scale (all in the register as C-75, C-96 to C-101, C-153 to C-158).

---

## Decisions needed from the developer, in order

1. **AP-1:** state the bulk orbital mass source (recommended: Moon plus near-Earth asteroids).
2. **AP-2:** pick the dose standard (recommended: worker-level for adults with general-population shelters and nurseries).
3. **AP-4:** what Venus's "mines" are (recommended: atmospheric extraction for local platforms).
4. **AP-6:** where Mars's water is (recommended: local ice).
5. **AP-3, AP-5, AP-9:** smaller clarifications; AP-3's polar-orbit research is a candidate next small research item.

**Nothing above needs a date to move.**
