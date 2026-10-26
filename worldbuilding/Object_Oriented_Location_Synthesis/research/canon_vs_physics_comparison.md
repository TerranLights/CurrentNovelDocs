# Canon vs physics: comparison of the interplanetary canon with the OOLSD research

*Step 3 of `_canon_comparison_CHECKPOINT.md`, written 2026-10-12. Canon claims are the K-IDs in `_canon_extract_interplanetary.md`; physics findings are from the
syntheses **SYN** (`starlifting_synthesis.md`), **IMS** (`inner_system_mining_synthesis.md`), **PHB** (`planetary_harvesting_and_benefits_synthesis.md`) and the
source files they cite (**LEO** `leo_and_orbital_habitats.md`, **CY** `cyclers_and_large_slow_vehicles.md`, **PR** `space_processing_and_fabrication.md`,
**OHM** `oxygen_and_hydrogen_supply_for_mars_water.md`, **MWB** `mars_water_budget_and_retention.md`, **VAL** `value_and_markets_of_inner_system_materials.md`,
**BVE** `benefits_of_mining_venus.md`). Arithmetic: `_calc/canon_comparison_calc.py`, output `_calc/canon_comparison_calc_output.txt` (cited as "calc n").
No canon file was edited. Rulings that bound the comparison: physics first, canon adjusted after; proposals only; orbital-society questions belong to the
Cryptograph Helix repo.*

**Verdict key.** CONSISTENT (physics supports it as stated) · CONSISTENT-WITH-CONDITIONS (physics allows it if a stated condition holds; the condition is named) ·
TENSION (physics allows only part of it, or only at a cost canon has not accepted) · CONFLICT (physics forbids it as stated) · NO PHYSICS BASIS (the research set has
no finding that bears on it) · CANON-INTERNAL (the issue is between canon files, not canon and physics).

**Rows that read the same canon number against a physics number show the arithmetic once, in the calc output, not here.**

## 3a. Orbital infrastructure stages and dates

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 1 | K-1: Stage 1 robot-only staging stations, small, light, low-tech; need "only energy harvesting... and radiation shielding" | LEO handwave 8: "low-tech" robot-only stations still need radiators, radiation-tolerant electronics and vacuum-rated lubricants ("allowed" if "robust but simple parts"). Register ruling RL-1: robots are radiation-vulnerable "equivalently to humans for shielding purposes"; so even the earliest station is shielded to the degree a human requires. Register C-4: joints wear without servicing | CONSISTENT-WITH-CONDITIONS | Canon names shielding and energy; physics adds heat rejection, hardened or screened electronics and part replacement. RL-1 already aligns canon's "shielding" with a human-equivalent standard. "Low-tech" is safe if it means simple, not absent |
| 2 | K-2 and K-3: Hana Jinn recruited after the 2318 Jeju-do ruling ("early-to-mid 2300s") for metamaterial mass drivers; Mallory Dufay oversees "the actual first orbital launches ... mid-2300s" | SYN stage 0: commitment to first operating hardware 8.2 to 13.5 yr (Apollo 8.2, Shuttle 9.3 x 1.45 slip) (calc 4: commitment 2318 gives first hardware 2326-2332; 2340 gives 2348-2354) | CONSISTENT-WITH-CONDITIONS | Holds if Hana's recruitment is the program start and Mallory's first launches come at least 8 to 13.5 years after it. Canon gives both as spans, so there is room; a two-year gap would not fit |
| 3 | K-4: Stage 2 O'Neill Cylinders: first structure humans occupied with robots; "slow-moving, but huge and floor-space-efficient"; primary long-term residence | PR 6 / calc 1: SP-413 cylinder 97.8 t/person vs torus 1,009 t/person (about 10x; canon's own 5.4x is the same direction); CY 5.5: an 80.2 Mt cylinder needs 10.3 to 62 yr of 10 GW thrust for 1 to 6.4 km/s, 4.4 to 7.2 yr for the 10.09 Mt torus; stability: an unpaired long cylinder tumbles (length up to ~1.3 radii) | CONSISTENT | Cylinders are the efficient residence and are slow because they are huge. Physics adds that a cylinder-class structure is not moved at all; it is built where it stays. That matches "primary long-term residence" |
| 4 | K-5: Stage 3 Von Braun Wheels: "light and easy to move", transport robots and humans together over long distances to build further infrastructure | LEO handwave 7: a wheel is light only without its shield; a transit wheel above the belts needs a storm shelter (~10 g/cm^2 class) or a GCR shield of a few tonnes per m^2; the August 1972 event gives crew 30.9 rem behind 10 g/cm^2 aluminum. CY: the studied inhabited cycler is ~70 t for a crew of 10 with a 30 cm-water storm shelter (9.2 t covering ~31 m^2). VBW: R = 100 m wheel houses ~35 to 150 humans | CONSISTENT-WITH-CONDITIONS | Works if "wheel" means a small crew vehicle with a storm shelter, not a large light habitat. The two roles (cylinders stay, wheels move) are exactly what the physics supports; "light" holds only for the unshielded structure |
| 5 | K-6: orbital infrastructure is "in place well before the war... from early in the Second Interwar Period (2564)" | Calc 4: commitment 2318-2340 puts Mt/yr-class industry at 2343-2388 and a first ~10 Mt torus at 2351-2396 (fast reading, sequential), or 2446-2473 on the slow (railroad-analog) bound | CONSISTENT | Even the slow bound lands 90 to 120 years before 2564. Canon has 4 to 5 centuries between the staging stations and the war, 2.6 to 10 times what the physics needs. This slack lets canon absorb setbacks (SYN: dependency lags, Ono linear growth) without changing dates |
| 6 | K-7 and K-8: cylinder 1 to 10 Mt for 5,000 to 10,000 people plus robots; Kalpana One ~7 Mt; debris-built (~16,200 t) houses ~200 to 800 humans; wheel 5.4x worse | Calc 1: SP-413 10.09 Mt torus for 10,000 (1,009 t/person), 80.2 Mt cylinder for 820,000 (97.8 t/person), Kalpana ~2,333 t/person. TR F3: cataloged mass in orbit at end of 2025 was 16,185 t (canon uses ESA's 16,200 t) | CONSISTENT | Canon's totals and the debris figure agree with the sources to the digit. The wheel penalty differs in size (about 10x against 5.4x) but not direction |
| 7 | K-8's "as low as ~10-20 t/person" low-shield LEO case, and K-10 (orbit mostly LEO) | LEO: ISS dose 0.2 to 0.5 mSv/day, about 70 to 180 mSv/yr; SP-413 designs to 0.5 rem/yr (5 mSv/yr), 4.5 t/m^2; CY conflict 4 and MWB constraints: dose target (worker limit vs general population) sets the mass by orders of magnitude | TENSION (for a population of families and children) | The 10 to 20 t/person case gives worker-level dose. It is fine for a robot crew only if RL-1's human-equivalent standard is relaxed; for a multigenerational population of families it understates the shielding mass by roughly 5 to 230 times (98 to 2,333 t/person). This is the single most consequential number in K-18's mass arithmetic |
| 8 | K-9: beyond ~1,000 to 2,000 people the structures "require importing material from the Moon or asteroids; debris alone cannot support more" | Calc 1: 10.1 million people need 0.10 to 23.6 Gt, which is 6,000 to 1,500,000 times the 16,200 t debris budget. IMS: Earth-side bulk material passes the break-even test from the Moon and near-Earth or carbonaceous asteroids; belt material to Mars passes | CONSISTENT | Canon already says this; physics confirms and sizes it. Note the guidance in K-9 is that imports must be "separately established" by canon, which has not been done (see section 4, gaps) |

## 3b. Materials: where the mass comes from, and the Tower

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 9 | K-18 + K-9: 10,104,964 people in orbit by 2812, housed in the structures above | Calc 2: supplying 0.1 to 24 Gt over the 472 years from the staging stations averages 0.2 to 51 Mt/yr (over the 124 Tower years, 0.8 to 194 Mt/yr). Calc 3: at the fast reading (one doubling per 2 yr from SYN's 1.2 Mt/yr stage) cumulative 1 Gt is reached 16 yr and 10 Gt 23 yr after that stage. SYN S-2 and register C-65: exponential growth beyond a few doublings is a handwave (the one bottleneck-aware simulation grew linearly); C-64: closure of chips | CONSISTENT-WITH-CONDITIONS | The mass is attainable in canon's time if industry reaches 10 to 100 Mt/yr and stays there for centuries. The condition is a sustained, power-fed, non-Earth material source, which canon does not yet state (K-9). With linear instead of exponential growth the time is longer but the 472-year window still holds at the lower population masses |
| 10 | K-14: the Tower's primary purpose is energy regulation and "bulk material export to orbit" (and return cargo) | Calc 5: lifting 8 Mt/yr (253 kg/s) costs 8.4 GW ideal, 2.6% of the Tower's 324 GW net; 82 Mt/yr costs 86 GW (26.5%); either is under 1% of the 270 t/s pellet loop by mass. Rocket equation at Isp 452.3 s: the 7.82 km/s final stage is 82.8% propellant (4.83 t of propellant per tonne of payload and dry mass). A South Pole launch gets no rotational boost and heads for polar orbit | CONSISTENT-WITH-CONDITIONS | Energy and mass flow do not stop the Tower exporting millions of tonnes a year. The conditions are (a) the final stage, not the Tower, supplies 7.82 km/s, so each tonne of payload brings about 4.8 t of propellant that must itself be lifted or made at altitude, (b) orbits reached from the Pole are polar, so equatorial and Mars departures need plane changes (not researched; open thread), (c) the Moon and near-Earth asteroids deliver bulk material to Earth orbit far more cheaply (2.52 km/s from the lunar surface; ~2.83 MJ/kg against 33.1 MJ/kg). The Tower is a plausible export channel, not the cheapest one |
| 11 | K-12 and K-13: 150 km space fountain, 225,000 t tube, 270 t/s at 4 km/s, ~324 GW net, ~3.62 km/s at the top, built over 65-75 yr (completion ~2688) | The research set does not cover space fountains. Scale cross-checks only: 324 GW is 13.5% of end-2025 world solar capacity (2,397 GW, RM F1); SYN stage 0 (8.2 to 13.5 yr to first hardware); LEO handwave 1 (no compression-supported tower reaches orbit; a space fountain is an active mass-flow system, not passive) | NO PHYSICS BASIS | The structure itself is outside the research. The scale is plausible against a civilization with Mt/yr-to-Gt industry by the 2400s (row 5) |
| 12 | K-15: the Tower's bulk material throughput is not quantified | Calc 5 gives the bounds: even 190 Mt/yr is 2.2% of the pellet mass and 61.5% of the power draw | NO PHYSICS BASIS | A gap in canon; physics gives the feasible range, canon has no number to test |
| 13 | K-16: window arithmetic (178 yr vs 124 yr) | Calc 6 reproduces both: 10,104,964 over 124 yr is 9.30/h; over 178 yr is 6.48/h; 194/h x 8,766 h x 120 yr = 204 million | CANON-INTERNAL | The two sections of the Tower file use different windows. The arithmetic is right in each; the file should say which window is current (124, per the resolved 2688 date). Not a physics matter |
| 14 | K-29: datadrives physically carried up where bandwidth is short; rich contact until 2812 | A drive is grams; the Tower or any launch moves it. Light time to orbit is milliseconds | CONSISTENT | Nothing limits it |

## 3c. Robots in space

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 15 | K-27: "once orbital robot-manufacturing draws on space-harvested raw materials, a subset of the robot population becomes genuinely spaceborne - never touched Earth"; "first fully spaceborne generation" | PR 3: structure, wiring, glass and solar cells' bulk can come from lunar or asteroid material; chips (no lithography ever done in space; tool >150 t), rare-earth magnets (1,073 to 1,610 t of carbonaceous material per robot at full recovery, or 0.5 to 0.75 t of the richest lunar rock) and battery lithium (95 to 152 t per 2 kWh) cannot. Imported by mass: 2 to 3 kg of magnet per robot, ~$3,000 to $4,500 at $1,500/kg. SYN: Mars industrial independence has no sourced date | CONSISTENT-WITH-CONDITIONS | A robot assembled in orbit from space-made structure and Earth-made chips, magnets and lithium never touches Earth in its body parts' final form and is spaceborne in the sense that matters (assembly, gravity, upbringing). A robot made entirely from space-harvested material, brains included, has no sourced date. Cheap to import, expensive to end: the dependency on the Tower/Earth for chips is itself a canon-usable fact |
| 16 | K-28: robots need no oxygen, food or sanitation, only energy and shielding | Register H-1 (gel brain waved) and C-1 to C-8: body heat rejection, joint wear, outgassing, charging; RL-1: human-equivalent radiation shielding | CONSISTENT-WITH-CONDITIONS | True of life support; a robot still needs heat rejection, shielding, replacement parts and power. These costs are small next to a habitat's, which is why robot-only stations come first |

## 3d. Mars

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 17 | K-22: Mars/Phobos/Deimos colonization began during the Second Interwar Period (2564-2812) | SYN section 6 / calc 7: first landing 8.2 to 13.5 yr after commitment; ~110 people at the survival minimum 17 to 39 yr after; commitment at 2564 gives 2572-2578 and 2581-2603, at 2688 gives 2696-2702 and 2705-2727. DRA 5.0 three-mission mass 2.5 to 3.8 kt is 0.8 to 1.2x one year of 2025 world launch. OHM F3c: Phobos is 1.21 km/s from Mars orbit | CONSISTENT | Large slack. Mars presence needs no space industry (SYN); an orbital base with Phobos/Deimos infrastructure is a smaller step than the Cylinders already in canon |
| 18 | K-21: at the game present (≈2822-2827) the evacuees have "Active plans to colonize Mars itself; some robots already living on Mars" | As row 17; robots on Mars need no life support, but Mars sunlight is 43% of Earth's (586 W/m^2) and heat rejection and shielding still apply | CONSISTENT | A robot-first Mars presence is the cheapest form. Note the canon-internal wording difference between K-21 ("plans to colonize Mars itself") and K-22 ("colonization began during the Second Interwar Period") |
| 19 | K-23: Cryptograph Helix opens ~3012-3112 with Mars "already fully colonized"; only Mars, its moons and limited inner regions colonized | Calc 7: 185 to 290 yr between the game present and the opening. SYN: 1 million people by claim is 43 to 107 yr (a CLAIM); Mars industry independent of Earth for chips, magnets, lithium has no sourced date; MWB: Mars holds 20 to 40 m global-equivalent water near the surface, loss to space slow | CONSISTENT | The interval is longer than any sourced stage-to-stage chain. "Fully colonized" is the open term: if it means independent industry, no source dates it, but 185 to 290 years exceeds the 20-year bootstrap models by a factor of 9 to 14 |
| 20 | (No canon claim found on the source of Mars's water) | OHM, MWB: Mars's polar caps alone hold 16 to 22 m global-equivalent; import from Mercury/Venus/Sun fails on cost | NO PHYSICS BASIS (canon silent) | Recorded in section 4 as a decision for the Helix repo |
| 21 | K-24: "Silicon Valley tech giants control Mars" | Not physical | NO PHYSICS BASIS | |

## 3e. Venus, Belt, Jupiter, Saturn, Mercury, the Sun

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 22 | K-21 and K-22: evacuees "moving toward Venus"; "Data infrastructure in the space between Venus and Earth" | IMS/NW F1: Venus is the cheapest planet to reach in v-infinity from Earth (2.5 to 2.7 km/s), windows every 584 d; Venus conjunction blackouts (about 20 days autonomous in 2011); Earth-Venus geometry repeats about every 8 yr | CONSISTENT | A relay or data network between Venus and Earth is exactly what blackouts and 584-day windows call for |
| 23 | K-24: Venus "floating prison gulags/mines" | BVE 3.9: cloud-deck habitat at 50 to 55 km has ~0.9 g, ~1 bar, 1,290 g/cm^2 of atmospheric shielding, air as lift gas; platform failure modes (downdraft, acid drizzle, falling into hotter layers); hydrogen scarce; no multi-year platform has flown. venus_as_extraction_site.md 3.6: surface at 737 K and 92 bar, landers last ~2 hours, no surface-mining study | CONSISTENT-WITH-CONDITIONS | "Floating" works, and the cloud deck is the most benign non-Earth place for people. "Mines" works if they extract gas (carbon, nitrogen, oxygen, sulfur) at cloud level; surface ore mining has no physics basis. A gulag's output feeds Venus's own platforms |
| 24 | K-24 / UTL: Venus "becoming colonized and then exploited" over a ~300 to 500 year gap; implies exports | IMS section 4 and BVE: bulk export costs 180 to 670 kt lifted per kt delivered; Earth air holds 34 times more nitrogen and ~200 times more argon than Venus air; "Not competitive on any figure found" | TENSION (if "exploited" means exporting minerals or gas to Mars or Earth) | Physics supports exploitation of Venus's labor, location, and local chemistry; it does not support bulk export. Messages, people and small high-value items are fine; tonnage is not |
| 25 | K-24: the Asteroid Belt as a real setting (Helix Books 3-4) | IMS section 6, VAL G: belt-to-Mars costs 44 to 59% of belt-to-Earth in delta-v, windows every 2.8 to 4.4 yr, passes break-even today; carbonaceous material ~20 wt% water, 183 kg/t iron | CONSISTENT | The belt is the physically favored supplier to Mars |
| 26 | K-23: Jupiter colonized during Helix, Saturn rudimentary exploration | Not part of these syntheses (earlier file `belt_jupiter_saturn_and_deep_transit.md` holds transit figures; not read for this comparison) | NO PHYSICS BASIS (here) | A later pass could test it against the older file |
| 27 | K-26: no canon on Mercury, the Sun, the Moon, mining | IMS, PHB, VAL: the Moon and near-Earth asteroids are the Earth-side sources that pass; Mercury's niche is local energy and materials; Venus is local use; the Sun's benefits are light and gravity | NO PHYSICS BASIS (canon silent) | Canon says nothing about where orbital mass comes from; this is the central gap (section 4) |

## 3f. Population

| # | Canon claim | Physics finding | Verdict | Why |
|---|---|---|---|---|
| 28 | K-19: ~12 million left in the later Second Interwar Period; the Helix founding population; reconciliation with 10,104,964 open | Calc 6: 12 million over 124 yr is 11.04/h; 10.1 million is 9.30/h; the design capacity is 194/h | CANON-INTERNAL | Throughput is no constraint. The reconciliation is bookkeeping (different counts) |
| 29 | K-18: orbital population is 31.6% of Tepenia's population at war start | Not tested | NO PHYSICS BASIS | |

## 3g. Durations between stages

| # | Canon span | Physics duration | Verdict | Why |
|---|---|---|---|---|
| 30 | Staging stations (mid-2300s) to Tower (2688): ~350 yr; to the war (2812): ~470 yr | SYN: first 10 Mt torus 33 to 56 yr from commitment (fast), 128 to 133 (slow bound); Mt/yr industry 25 to 48 yr | CONSISTENT | Canon is 2.6 to 10 times longer than the physics chain; nothing in canon's dates is too short |
| 31 | Tower era (2688 to 2812): 124 yr | Calc 5: if the whole mass of the orbital population came through the Tower, 10 Gt needs 80.7 Mt/yr (26.5% of the Tower's power at 82 Mt/yr) | CONSISTENT-WITH-CONDITIONS | Possible only if the Tower carried most of the build-up. If most mass came from the Moon and asteroids (cheaper), the Tower's role is passengers and high-value cargo |
| 32 | Mars: Second Interwar start (2564) to game present (2822-27) ~260 yr; present to Helix ~185 to 290 yr | Calc 7: first landing 8.2 to 13.5 yr; survival population 17 to 39 yr; 1 million 43 to 107 yr | CONSISTENT | Physics needs under 110 yr to everything sourced. Canon's much longer spans leave room for the slow bound |

## 4. Gaps in canon that the physics comparison exposes (decisions, not defects)

1. **Where the orbital mass came from.** Canon says imports from the Moon or asteroids are needed "unless canon separately establishes" otherwise (K-9) and has not (K-26). The physics says 0.1 to 24 Gt for 10.1 million people (calc 1), depending on shielding standard (row 7).
2. **Which dose standard the 10.1 million live under.** The mass swings by about 230 times (97.8 to 2,333 t/person) between SP-413's general-population standard and canon's low-shield figure (row 7).
3. **What the Tower's bulk export was for.** Canon states the purpose but no tonnage (K-15), and the final stage's propellant dominates (row 10).
4. **Where Mars's water comes from.** Canon is silent; physics shows Mars needs none for anything short of an ocean (row 20).
5. **What "Venus exploited" exports.** Physics supports labor, location and local chemistry, not bulk cargo (row 24).
6. **Polar-launch consequences.** A South Pole Tower launches into polar orbits; no research file covers the plane changes this implies for equatorial structures and Mars departures (row 10).
7. **The Solar-Colonization-era folder is empty** in the timeline repo; any dated Mars/Venus/Belt/Jupiter canon is in memory and drafts only.

## 5. Verdict counts

32 rows (counted by script from the tables above): **12 CONSISTENT, 9 CONSISTENT-WITH-CONDITIONS, 2 TENSION, 0 CONFLICT, 7 NO PHYSICS BASIS, 2 CANON-INTERNAL.**
The two TENSIONs are rows 7 (low-shield LEO dose for a population of families) and 24 (Venus exporting bulk to Mars or Earth). No canon claim in the research set is forbidden by physics.

## 6. Audit (step 5, 2026-10-12)

Every physics and canon figure cited above was checked by pattern against its source file (script run inline; output saved at `_calc/canon_comparison_audit_output.txt` and pasted raw
below). **One MISSING line, resolved by hand:** the pattern for Orbital_Infrastructure_Mass_Budget.md's "10-20 tonnes/person" failed only because the source uses an en dash and a line break
(`**~10–20` / `tonnes/person**`, lines 85-86); the figure is present as cited.

**Corrections and additions found during the audit**
1. *Canon-internal slip, newly found.* The same passage (line 86) says the low-shield figure compares with "millions of tonnes/person in fully-shielded deep-space designs". The file's own earlier
   estimate (1 to 10 Mt for 5,000 to 10,000 people) and SP-413's torus (1,009 t/person) are about 1,000 t/person, three orders smaller than "millions". It is a wording slip in the canon file, not a physics
   finding; added to AP-5 in `canon_adjustment_proposals.md`.
2. Row 11 cites the research file's candidate handwave 1 (no compression-supported tower reaches orbit) only to say a space fountain is active; the research did not evaluate space fountains.
3. Rows 19 and 32 use the physics need "under 110 yr"; the sourced chain maxima are 107 yr (1 million people by claim) and 133 yr (slow bound to a first torus); "under 110" refers to the Mars
   ladder only. Row 30 covers the 133-yr slow bound separately.

**Raw audit output**

```
OK      x1 leo_and_orbital_habitats.md | 0\.2-0\.5 mSv per day | ISS dose 0.2-0.5 mSv/day (row 7)
OK      x1 leo_and_orbital_habitats.md | 30\.9 rem | Aug 1972 30.9 rem (row 4)
OK      x1 leo_and_orbital_habitats.md | \"Low-tech\" robot-only stations | LEO handwave 8 (row 1)
OK      x1 leo_and_orbital_habitats.md | A light, mobile wheel | LEO handwave 7 (row 4)
OK      x1 leo_and_orbital_habitats.md | compression-supported tower | LEO handwave 1 (row 11)
OK      x3 cyclers_and_large_slow_vehicles.md | 9,254 kg | storm-shelter mass (row 4)
OK      x3 cyclers_and_large_slow_vehicles.md | 31 m2 | storm-shelter area (row 4)
OK      x1 cyclers_and_large_slow_vehicles.md | 128 years per km/s|128 yr | 10^9 t immobile (AP-7 context)
OK      x2 space_trucking_and_transport_infrastructure.md | 16,185 t | cataloged mass end-2025 (row 6)
OK      x2 space_trucking_and_transport_infrastructure.md | 33\.1 MJ/kg | Earth surface to 400 km (row 10)
OK      x3 space_trucking_and_transport_infrastructure.md | 452\.3 s | RS-25 Isp (row 10)
OK      x6 space_trucking_and_transport_infrastructure.md | 2\.52 | Moon to LEO delta-v (row 10)
OK      x1 industrial_ramp_timelines.md | 2,397 \(2025\) | world solar capacity 2025 (row 11)
OK      x11 mars_water_budget_and_retention.md | 20 to 40 m | Mars near-surface water (rows 19, 20)
OK      x1 venus_as_extraction_site.md | About 20 days of autonomous operation in | Venus conjunction blackout (row 22)
OK      x1 venus_as_extraction_site.md | 737 K, 92 bar | Venus surface (row 23)
OK      x3 benefits_of_mining_venus.md | 34 times | N in Earth air vs Venus (row 24)
OK      x3 benefits_of_mining_venus.md | 1,290 g/cm | Venus cloud shielding (row 23)
OK      x4 inner_system_mining_synthesis.md | 180 to 670 | Venus export (row 24)
OK      x3 starlifting_synthesis.md | 8\.2 to 13\.5 | stage 0 duration (rows 2, 17)
OK      x2 starlifting_synthesis.md | 33 to 56 | sequential sum to torus (row 30)
OK      x2 starlifting_synthesis.md | 128 to 133 | slow bound (row 5)
OK      x1 starlifting_synthesis.md | 17 to 39|17 to 39 years | 110 people (row 17)
OK      x2 planetary_harvesting_and_benefits_synthesis.md | 16 to 22 m | Mars polar water (row 20)
OK      x1 space_processing_and_fabrication.md | 1,073 to 1,610|1,073-1,610|1,073 | magnet material per robot (row 15)
OK      x6 space_processing_and_fabrication.md | 150 t | lithography tool (row 15)
OK      x1 space_processing_and_fabrication.md | 10,0?9?0?,?000 people|10,000 people | SP-413 torus population (row 6)
OK      x8 Amundsen_Tower_Space_Fountain_Design.md | ~324 GW | Tower net draw (rows 10, 11)
OK      x3 Amundsen_Tower_Space_Fountain_Design.md | ~270 tonnes/s | pellet loop (row 10)
OK      x4 Amundsen_Tower_Space_Fountain_Design.md | 7\.82 km/s | orbital velocity needed (row 10)
OK      x2 Amundsen_Tower_Space_Fountain_Design.md | ~194 people/hour | design capacity (row 13)
OK      x1 Amundsen_Tower_Space_Fountain_Design.md | ~178yr window | old window (row 13)
OK      x1 Amundsen_Tower_Space_Fountain_Design.md | ~9\.30 people/hour | new window (row 13)
OK      x1 Amundsen_Tower_Space_Fountain_Design.md | 3\.225 million tonnes | tower material (K-13)
MISSING x0 Orbital_Infrastructure_Mass_Budget.md | 10-20\s+tonnes/person|~10-20 | canon low-shield mass (row 7)
OK      x5 Orbital_Infrastructure_Mass_Budget.md | 16,200 | debris budget (row 6)
OK      x1 Orbital_Infrastructure_Mass_Budget.md | ~7 million tonnes | Kalpana One (row 6)
OK      x2 Von_Braun_Wheel_Mass_Budget.md | 5\.4x | wheel penalty (row 6)
OK      x2 README.md | 10,104,964 | orbital pop (K-18)
OK      x1 README.md | 31\.6% | 31.6 % (K-18)
OK      x1 README.md | in place well before the war | K-6
OK      x1 README.md | does not develop orbital society|It does | scope boundary
OK      x1 README.md | low-Earth orbit | K-2 Hana Jinn
OK      x1 Timeline.md | closer to the mid-2300s | K-3
OK      x1 Timeline.md | early-to-mid 2300s | K-2 dating
OK      x1 World_History_Reference.md | Active plans to colonize Mars itself | K-21
OK      x1 World_History_Reference.md | Data infrastructure in the space between | K-21
OK      x2 World_History_Reference.md | ~2688 | K-11
OK      x1 universe-timeline.md | floating gulags | K-24
OK      x1 universe-timeline.md | Jupiter colonization happens | K-23
OK      x1 universe-timeline.md | only Mars, its moons | K-23
OK      x1 04_Handwave_Register.md | RL-1 | RL-1 ruling (rows 1, 16)
MISSING/NOFILE total: 1
```
