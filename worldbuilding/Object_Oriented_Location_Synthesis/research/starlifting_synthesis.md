# Starlifting and the industrial chain: synthesis

*OOLSD, written 2026-10-11 from the five tranche-6 research files. Status: a synthesis of unreviewed research; every figure is
traceable to a row in a source file or to a numbered line in `_calc/starlifting_synthesis_calc_output_run2.txt`.*

## 0. Method and limits

- **Developer ruling, 2026-10-11:** research the physics first; adjust the interplanetary timeline to what is realistic
  afterward. **Nothing in this file was read back from the project's interplanetary timeline or any other canon.** The
  comparison with canon is a separate, later step and has not been done.
- **Inputs:** `starlifting_physics_and_minimum_infrastructure.md` **[SL]**, `space_trucking_and_transport_infrastructure.md` **[TR]**,
  `space_processing_and_fabrication.md` **[PR]**, `industrial_ramp_timelines.md` **[RM]**, `cyclers_and_large_slow_vehicles.md` **[CY]**.
  Section references (F3, D5, 5.5) are to those files. The five files were reviewed by me, not independently verified; their
  source-error findings are carried in section 9.
- **Arithmetic:** `_calc/starlifting_synthesis_calc.py`; authoritative output is `..._output_run2.txt` (run 1 had one misleading last
  line, replaced in run 2).
- **Evidence words:** DEMONSTRATED (flown or built), STUDY (a quantitative design or schedule), CLAIM or SPECULATIVE.
  **A stage duration below is never a forecast.** It is the stated range of the analogs the sources give, with the arithmetic shown.
- **Not covered by tranche 6:** Mercury as an industrial site (no study of a Mercury mass driver or Mercury-to-Earth cargo fleet was
  found, [TR] F1c and F7), the Moon and belt resource inventories (sibling files `moon_lagrange_and_comparables.md`,
  `belt_jupiter_saturn_and_deep_transit.md`), and every question about people, as opposed to machines.

## 1. The answers in brief

1. **Starlifting from the Sun does not compete as a source of material, on any figure found.** Lifting one tonne of iron out of the
   photosphere costs about 1.6 x 10^17 J, about 12 million times the energy to lift the same iron off Mercury, and about 500 t of solar
   material must be lifted per tonne of structural metal because 98.6% of it is hydrogen and helium (section 2). The literature
   that models starlifting does so to extend the Sun's life, not to supply material, and none has an engineering design.
2. **What the Sun does give cheaply is power**, and sunlight (not solar matter) is what an early industry is built on.
3. **The first real off-Earth industry is built from nearby, shallow-well bodies** (the Moon, near-Earth asteroids, later the belt),
   with water and rock as the first products: propellant, shielding mass, and bulk metal. Its first useful scale is about 1,000 t/yr
   (one miner, one plant under 5 t, [TR] F7).
4. **Time from commitment to a first Mt-class habitat is about 33 to 56 years in the fast-growth reading** (stages one after another),
   and about 128 to 133 in a slow reading; a study's own overlapped figure of 22 years has never been tested (section 5).
5. **A first human presence on Mars does not need space industry.** The mass of three crewed missions (2.5 to 3.8 kt) is 0.8 to 1.2
   times the whole world's launched mass in 2025. What it needs is vehicle development (8 to 13.5 years from commitment) and
   launch windows 2.14 years apart. **A Mars industry that does not depend on Earth for chips, rare-earth magnets and lithium has no
   sourced date at all** (section 6).
6. **Human-shaped machines can have locally made bodies (aluminum, steel, glass, ceramics, wiring) long before they can have local
   brains.** Chips, magnets and battery lithium are the dependency, and they are cheap to import by mass (2 to 3 kg of magnet per
   robot) and impossible to make locally at any demonstrated scale (section 4).
7. **The O'Neill-cylinder idea for early trucking:** the physics allows a big, slow, inhabited vehicle, but a cylinder-class habitat
   cannot be moved on a useful timescale (10 to 62 years of thrust at 10 GW), so it works only if built in place on its orbit, which
   makes it a late stage, not an early one (section 8).

## 2. Starlifting itself (question a)

**What exists.** Only the *life-extension* literature: remove about 5 x 10^19 kg/yr (about 1,200 times the natural solar wind) so a star
stays at constant output, which needs at least about 8 x 10^-4 of the Sun's total luminosity even at 100% efficiency ([SL] 3A, D1).
Its mechanisms (beamed heating, magnetic schemes, space elevators) are described and never designed; one concept paper says the
elevator version needs "as-yet uninvented materials". A flown precedent for collecting solar matter exists once: Genesis, 0.2 mg of
hydrogen per year on 1.67 m^2 at 1 AU ([SL] 3E, D4).

**The numbers that decide it** (calc section 1):

| Quantity | Value | Source |
|---|---|---|
| Energy to escape the photosphere | 1.91 x 10^11 J/kg | [SL] D1 |
| Solar material to lift per tonne of Fe / of structural-metal mix | 841 t / 513 t | [SL] 3B |
| Ideal lift energy per tonne of Fe | 1.6 x 10^17 J = **5.1 GW continuous per tonne per year** | calc 1 |
| Same, Mercury (70% metal material) | 1.3 x 10^10 J = 409 W per tonne per year; **ratio 1.2 x 10^7** | calc 1, [SL] D7 |
| Same, as a multiple of Earth surface to 400 km orbit (33.1 MJ/kg) | 5,763 times | calc 1, [TR] D5 |
| One tonne of iron per year, as a share of all world solar capacity at end-2025 (2,397 GW) | 0.21% (ideal; no separation, no losses) | calc 1, [RM] F1 |

**Collecting the solar wind instead** costs no lifting energy (the Sun already paid it) but the yield is tiny. At the photospheric
iron fraction, area needed per tonne of *iron* per year (calc 1b; no credit taken for the first-ionization-potential enrichment of
1.6 to 2.3, which is unconfirmed for Fe/H, [SL] 3E):

| Collector distance | Area per t Fe per yr |
|---|---|
| 1 AU | 8.6 million km^2 |
| 0.3 AU | 0.78 million km^2 |
| 0.1 AU | 86,000 km^2 |
| 0.0465 AU (Parker's perihelion) | 19,000 km^2 |

No capture-and-store device exists even on paper ([SL] 3E); the magnetic structures studied deflect the wind for thrust.

**Minimum infrastructure to begin, at any scale** ([SL] 3D, 3E, 6): solar arrays (Genesis and Parker run on hundreds of watts),
autonomous control (8 minutes of light time at 1 AU; Parker keeps itself in its shield's shadow without help), passive collectors,
and a return capsule. **Nothing in the sources supports a rate above gram-per-year by design;** larger rates are area scaling only.
Survivable hardware near the Sun is bounded by what has flown: a 73 kg carbon shield at about 1,400 C admitting under 50 W, hours per
pass, to 9.86 solar radii. A passive sun-facing plate passes the highest melting point of any compound (4,232 K) at about 1.4 to 1.9
solar radii.

**Verdict.** On the figures found, the Sun's matter is the most expensive matter in the solar system to reach, and its yield of
structural metal is the smallest. Its value is power. **Therefore "starlifting" as the user framed it (harvesting raw materials from
the Sun) should not be treated as an early-era source; as a setting element it is either a very late, very large, energy-rich
project or a handwave (candidate S-1 below).** Whether the user's intended in-fiction meaning differs (for example, solar
*orbit* collection of wind and dust, or power-satellite construction) is the user's to say.

## 3. Trucking: moving material to the habitable zone (question b)

**Delta-v from candidate sources** (Hohmann, coplanar, no flybys; [TR] F1 table; lower bounds):

| Source (from low orbit unless noted) | To depart | All-propulsive to low Earth orbit | Transit |
|---|---|---|---|
| Lunar surface to LEO (aerocapture) | 2.52 | 5.60 | 5 d |
| Low Mercury orbit to Earth | 7.55 | 13.09 | 105 d |
| Main belt 2.2 AU to Earth | 4.21 | 8.54 | 370 d |
| Main belt 2.2 AU to **Mars** | 1.91 | **3.76** | 464 d |
| 0.3 AU circular to Earth | 13.07 | 19.85 | 96 d |
| 0.1 AU circular to Earth | 32.81 | 45.38 | 74 d |

The belt-to-Mars figures are 44 to 59% of the belt-to-Earth figures (calc 7): **Mars is the cheaper customer for belt material,
in delta-v**, though belt-to-Mars windows recur only every 2.8 to 4.4 years against 1.2 to 1.4 years to Earth ([TR] F4, D6).

**Propulsion that has carried mass** ([TR] F2): chemical (hydrolox RS-25, 452 s); solar-electric Hall (AEPS-class 12 kW, about 2,900 s),
Dawn (11.5 km/s of delta-v, 416 kg xenon); nuclear-thermal tested on the ground only; nuclear-electric never beyond about 500 We in
flight; solar and electric sails with thrust measured only at millinewton scale or not at all; the lunar mass driver is a 1977 point
design (650,000 t/yr, 125 MW, 3,130 t machine, [TR] F2). Rock and metal can be thrown (288 to 10,000 m/s^2 accelerations); water
ships as ice; hydrogen and helium need cryogenic tanks whose in-orbit loss rate no source gave ([TR] F6).

**Throughput arithmetic** ([TR] F3, D3, D4): a 25 kW solar-electric tug moves about 0.279 t per kW per year over a 3.4 km/s leg, so
1,000 t/yr needs about 143 tugs (3.6 MW) and **about 180 t/yr of xenon, 2.8 times the world's production (about 65 t/yr)**. For 100,000
t/yr, about 14,300 tugs. **Kilotonne-per-year electric trucking therefore needs a different propellant (argon, flown on Starlink
since 2023, or water- or rock-derived reaction mass) or the whole world's xenon.** Hardware is the lesser constraint: 143 tugs
(1,394 t) equals 0.48 years of Starlink satellite production by mass (calc 8; the satellite mass is trade-press and low confidence).

**Infrastructure every bulk scheme needs** ([TR] F4): a receiver (propellant depot, mass catcher, aerobrake, or tether catch) and a local
propellant source. The only receiver type ever demonstrated is slow aerobraking (MRO: about 400 passes, about 6 months). Catchers,
single-pass aerocapture, depots with vehicle-to-vehicle cryogen transfer, and momentum-exchange tethers exist as studies and ground
tests. Launch cost to low orbit fell to about $1,500/kg (Falcon Heavy, 2021 dollars) at a 21.2% decline per doubling of cumulative
payload ([TR] F5, [RM] F2); the same source warns this is not a forecast.

**Cycler trucking** ([CY] A, B, F): ballistic Earth-Mars cyclers repeat every 2.14 years in a 14.95-year cycle; a 70 t vehicle needs 87
to 147 t of propellant to establish; two vehicles serve an Aldrin cycler, four serve a two-synodic cycler; **nothing stops, so every
passenger and package rides a taxi that rendezvouses within about 7 days at 3 to 12 km/s relative speed**. A 1,256 t asteroid has been
simulated onto a cycler by a 10 t tug as shielding mass ([CY] E).

## 4. Processing, fabrication and robots (question c)

**Chains demonstrated, all at laboratory or one-batch scale** ([PR] 1, 5): oxygen and metal by molten regolith electrolysis (25 kg run,
9 kW, about 104 to 135 kWh/kg O2), carbothermal reduction (TRL 6 on the ground), hydrogen reduction of ilmenite (24.3 kWh per kg of liquid
oxygen in the end-to-end model), molten-salt electrolysis of simulant (96% of the oxygen out in 50 h), water from heated carbonaceous
material (more than 95% released below 600 C). Metal 3D printing in orbit: 180 kg of printer making under 250 g per 2 to 4 weeks, about
**28 kg of plant per kg of yearly output**, against design-study paybacks of 0.14 to 1.0 ([PR] 5, D7). **Studies are 20 to 200 times
more productive than hardware has been.**

**What cannot be made from bulk space material at any demonstrated scale** ([PR] 3, 4): integrated circuits (no lithography or wafer
step ever done in space; one lithography tool alone is over 150 t), rare-earth magnet material (per robot, 1,073 to 1,610 t of
carbonaceous material at full recovery, or 0.5 to 0.75 t of the richest lunar rock) and lithium (95 to 152 t of carbonaceous material per
2 kWh battery). The studies converge on 90 to 96% materials closure with 4 to 10% imported as "vitamin parts" ([PR] 3, [RM] F4).

**Derived (calc 8):** for 1,000 human-shaped machines, magnet material alone is 1.07 to 1.61 Mt of carbonaceous material, **20 to 30
years of the entire output of a 54 kt/yr plant**. Importing the same magnets from Earth is 2 to 3 t, about $3,000 to $4,500 per robot
at $1,500/kg. **So the dependency on outside chips, magnets and lithium is the cheapest to keep and the most expensive to end.**
Magnet-free actuators are a physics-compliant alternative that no tranche-6 file researched ([PR] 8).

**Bootstrapping models** ([PR] 3, [RM] F4): a modeled path from 12 t landed on the Moon reaches closure in about 20 years with
generations 2 years apart; electronics closure runs 90, 95, 99, 100% across Generations 3 to 6, with basic lithography only by Generation
5, and the model assumes robotics at "mouse-level" autonomy. The 41 t-launched case grows to 40,000 t in 20 years, **2.0 years per
doubling** (calc 8). An undergraduate simulation with explicit power limits grew linearly ([RM] F4, low weight). Every published
growth curve is a design, none has been built at any size.

## 5. Stage-to-stage durations (question d)

**How these were derived.** Each stage is a multiple of throughput. Time = the analog's own time for that multiple (solar PV from 2000
for 10x, 100x, 1000x; US railroad miles; world launched mass; a self-replicating-factory table; generations 2 years apart), interpolated
in log multiple (calc 2). Development leads come from Apollo, Shuttle and the megaproject slip factor (calc 3). **The four exponential
analogs agree closely because they are all roughly one doubling per 2 years; that agreement is not confidence. The railroad analog
and the one linear simulation say the real rate may be much slower.**

| Stage | Starts at | Ends at | Multiple | Fast reading (yr) | Basis | Slow bound (railroad analog) |
|---|---|---|---|---|---|---|
| 0. Commitment to first operating hardware | decision | first miner and tug working | n/a | **8.2 to 13.5** | Apollo 8.2; Shuttle 9.3 x 1.45 slip (calc 3) | same |
| A. First tonnes to a first useful market | 10 t/yr | 1,000 t/yr | 100x (6.6 doublings) | **6.6 to 13.3** | CP-2255 working years 6.6; PV 13.0; launched mass 13.3 | 46.5 |
| B. To refinery scale | 1,000 t/yr | 54,000 t/yr | 54x (5.75 doublings) | **5.8 to 11.7** | CP-2255 5.8; PV 11.7 | 38.3 |
| C. To shielding scale | 54,000 t/yr | 1.2 Mt/yr | 22x (4.5 doublings) | **4.5 to 9.7** | CP-2255 4.5; PV 9.7 | 26.6 |
| D. Deliver the 9.9 Mt shield of one torus | 1.2 Mt/yr | done | 8.25 yr at the study's rate | **8.2** | [RM] F3, [PR] 6 | 8.2 |
| **Sequential sum to a first ~10 Mt torus** | | | | **33 to 56** | calc 5 | **128 to 133** |

Cross-checks: the one habitat actually assembled in orbit, ISS (420 t), took 12.5 years at 34 t/yr; a 10.09 Mt torus is 24,040 times
its mass (14.6 doublings). SP-413's own schedule is 22 years from go-ahead, with the plan's productivity assumption (8.3 plant masses per
year) never used to bootstrap; with the megaproject slip factor that is about 32 years. **1 Mt/yr is 313 times the 2025 world launched mass**,
so Mt-class flows can only be non-Earth material. **The last quarter takes as long as the first three** in every completed build-out
([RM] F1: Interstate 74% open after 14 years, 99.98% after 41).

**What dominates the uncertainty** ([RM] F6): reactors take 59 to 121 months to first grid power, fabs about 1.9 years, environmental review
a median of 3.5 years; one megaproject in ten is on schedule. Dependency lags, not production rates, are where ramps stall.

## 6. Mars presence (purpose 2)

| Rung | What it needs (sourced) | Duration or rate (arithmetic in calc 7) |
|---|---|---|
| M1. First crewed landing set | DRA 5.0: three missions on consecutive windows, 848.7 t (nuclear-thermal) or 1,251.8 t (chemical) each to low Earth orbit, cargo landed 2+ years ahead | Mass 2.5 to 3.8 kt = **0.8 to 1.2 x the 2025 world launched mass**; commitment to first landing 8.2 to 13.5 yr (stage 0); three missions span 2 x 2.14 = 4.3 yr |
| M2. Small permanent base | About 280 t of hardware for 20 people, 50 t of replacement hardware every 15 years ([CY] G) | Set by windows (2.14 yr) and vehicle capacity |
| M3. Population at the survival minimum | 110 people ([RM] F5, Salotti 2020, with Earth supply cut and local resources) | 10 windows at 12 per window = **21.4 yr**; 2 windows at 100 per window = 4.3 yr |
| M4. Industry not dependent on Earth for chips, magnets, lithium | Moon-analog bootstrapping: 20 years in a model, 2-year generations; Mars sunlight is **43% of Earth's** (586 W/m^2) | **No sourced duration for Mars.** The model was not run for Mars; its own caveat is that cutting solar duty by under 2x cuts growth by more than 10x ([RM] F4) |
| M5. A million people | 20 to 50 rendezvous at one window per 2.14 yr (a CLAIM, fully reusable ships assumed) | 43 to 107 yr |

**Reading.** A first presence is a vehicle-and-schedule problem (about 8 to 14 years to a first landing, 4 to 5 years more for a base on
three windows) and is independent of the starlifting question. A settled population at the survival minimum is about 17 to 39 years from
commitment (8.2 to 13.5 + 4.3 + 4.3 to 21.4). **Industrial independence, the thing that makes Mars a civilization rather than an
outpost, has no sourced timescale; its limiting inputs are power at 43% sunlight and the chip-magnet-lithium chain.** Mars is also the
energetically nearer customer for belt material (section 3), which is the one structural link between the two halves of the question.

## 7. The setting the characters live in (purpose 1)

Read straight from the constraints sections of all five files; none is a design choice.

- **Work happens in shadow, and shadow is life support.** Near the Sun, sunlight is 13 times Earth's at 0.28 AU, and the photosphere
  emits about 100 times the flux that fell on Parker's shield; that shield admits under 50 W. Every exposed surface heats toward 1,000+ K ([SL] 6).
  Heat rejection is a design driver everywhere: an SP-413 aluminum refinery rejects 127 MW through 102,400 m^2 of radiators ([PR] 5).
- **Everything is slow, lagged and bunched.** Legs are 3 months to 1.8 years; a low-thrust tug takes about a year per 3.4 km/s; one-way
  light time is 7.5 to 31 minutes; belt-to-Mars cargo leaves every 2.8 to 4.4 years; a 0.1 AU source is within 2 degrees of the Sun for
  about 23% of each 11.9-day cycle; Mars missions stop commanding for about two weeks every two years ([TR] 6, F4).
- **Remote sites run with no slack.** McMurdo gets nearly all its year's fuel in one sealift; a Mars settlement is the same with 26-month
  gaps. Early colonies lose people before they gain independence (Jamestown: 80 to 90% dead by its third winter) ([RM] F5, 6).
- **The industry is an energy-and-radiator problem first.** Tens to about 100+ kWh per kg for oxygen and metal ([PR] 5); most of a
  habitat's mass is unprocessed shielding (98% of the SP-413 torus); the chief job is moving and packing rock.
- **Dependence on outside supply is structural.** Chips, magnets and lithium come from outside until a local chain exists; a first
  fab is a very large, very clean import ([PR] 6).
- **Light cargo and heavy cargo live different lives.** Rock and metal are thrown at 29 to 1,000 g and caught at the far end by
  machinery beside which people work at a 2 km, 10 s warning distance; anything fragile, a human-shaped machine included, rides a tug
  or a taxi ([TR] 6).
- **Venus's clouds and giant planets trap what they hold.** Leaving Venus's clouds is as hard as leaving Earth's surface (about 9
  km/s); gas-giant mining is studied only at the ice giants and only for fusion fuel ([TR] F1b, F6).
- **Radiation is a mass problem.** A transit storm shelter of 30 cm of water covers about 31 m^2; a whole habitat at general-population
  dose needs 4.5 t/m^2 ([CY] D, 5.6).
- **Early local robots are heavier and cruder** (2.5 times heavier in the model's first generations, "mongrel alloys", aluminum wire
  with basalt insulation) ([PR] 3).

## 8. The cylinder idea (user design note, 2026-10-11)

*Idea: the early stage of "space trucking" can involve O'Neill Cylinders, since those are for slower, larger environments.*

| Question | Finding (sourced; arithmetic in calc 6) |
|---|---|
| Can a rotating habitat thrust and steer while spinning? | Yes, at low thrust: a 100 to 200 t electric vehicle at 1 g loses only about 5% in extra mass, steers at under 2 degrees per day in cruise and 10 to 15 degrees per day at planets; spin is the structural design driver and electric-propulsion loads are about 10^-5 of it ([CY] C, 5.4) |
| Is a cylinder stable? | Not if long: an unpaired cylinder ends up tumbling end over end; passive stability needs length up to about 1.3 radius with flat endcaps, otherwise a counter-rotating partner or active control ([CY] C). The SP-413 cylinder is 10 radii long |
| Can it be moved? | At 10 GW and 49 km/s exhaust (24.5 mN per kW): a 1 Mt vehicle needs 0.13 to 0.78 yr for 1 to 6.4 km/s; the 10.09 Mt torus 1.3 to 7.8 yr; **the 80.2 Mt cylinder 10.3 yr for 1 km/s, 35 yr for 3.5 km/s, 62 yr for 6.4 km/s**, using 1.6 to 9.8 Mt of propellant (18,000 years of world xenon for 1.2 Mt). The 10 GW plant (40,000 to 80,000 t) is a modest share of the torus (0.4 to 0.8%) |
| Can it be put on an Earth-Mars cycler orbit? | Getting a vehicle onto a cycler takes 3.5 to 5.8 km/s from low orbit ([CY] A): 35 to 57 years of 10 GW thrust for the cylinder, 4.4 to 7.2 years for the torus |
| Does size help transport? | Not people: a cycler never stops, so everyone boards by taxi (10 persons per taxi, 3 to 12 km/s relative speed); throughput is the taxi, not the hull ([CY] B). Cargo: a big slow carrier suits bulk, if the far end can catch it (catchers, aerobraking) |
| What does physics favor? | A small inhabited cycler (70 t, crew of 10, 30 cm-water storm shelter) is what the studies design. Shielding mass is the thing that scales; **the observation, mine and not a source's: rock cargo is itself good shielding (98% of a torus's mass is shield), so a cargo train that carries its own habitat inside its load turns trucking mass into radiation protection**; the one sourced example is 1,256 t of asteroid on a cycler (calc, [CY] E) |

**Verdict.** The idea is physically defensible *in one form*: a large rotating habitat **built in place** on its slow orbit from
material delivered there, after Mt/yr industry exists (stages 0 to C of section 5: about 25 to 48 years from commitment). It does not work as an *early* trucking
vehicle that is built elsewhere and moved, or as a passenger ferry; for those the sources give small cyclers and tug convoys. The sourced
direction of the idea is therefore reversed: cylinders do not enable early trucking, early trucking enables cylinders. The canon fact
(cylinders as long-term residences, Von Braun wheels as transport) has not been compared with this finding yet.

## 9. Source errors and open conflicts carried from the five files

- [SL] 4: the Sun's escape energy in one paper's table is low by a factor of 10; a paper's kg total is low by 2; one paper's L_sun
  ratios are low by a factor of 8. All corrected from fact sheets.
- [TR] C1, C5: Earth-Mercury "about 16 km/s" is undefined by its paper; one preprint's "76 km/s" is a typo for 76 m/s.
- [PR] C2, C3: Lewis's ilmenite residue figures are 14 to 29% high against stoichiometry; one lunar-cell power figure is 20 times low
  against its own efficiency.
- [RM] Conflict 1: "a million tons per year in ten years" counts working years; calendar is twenty, and only in the fast-exponential case.
- [CY] Conflict 1, 3: Mars V-infinity for the Aldrin cycler is a range (7 to 12 km/s), not a number; taxi shielding is 3 to 10 g/cm^2
  depending on the page.
- Unresolved: whether the solar wind's iron-to-hydrogen ratio is enriched over the photosphere (changes section 2's areas by a factor
  of 1.6 to 2.3 at most); the in-orbit boil-off rate of any cryogen; a Mercury cargo-fleet study (none found).

## 10. Candidate handwaves raised by the synthesis

Flagged for the developer; none is accepted. (The five source files' own candidate handwaves are entered in
`04_Handwave_Register.md` as C-48 to C-74, and their open threads in `DEFERRED_RESEARCH.md` as Batches 8 to 12.)

- **S-1.** Any use of solar matter as a material source in an early or middle era; the physics gives 1.2 x 10^7 times the lifting cost of
  Mercury per tonne of iron.
- **S-2.** Exponential industrial growth beyond a few doublings, without a stated power, closure and labor assumption (the one
  bottleneck-aware simulation is linear).
- **S-3.** Mars industry independent of Earth-made chips, magnets and lithium on any stated date; no source gives one.
- **S-4.** A cylinder-class habitat as a moved vehicle (10 to 62 years of thrust at 10 GW).

## 11. Open threads

- Mercury as an industrial site: mass-driver and cargo-fleet studies (none found), its surface composition by weight percent, polar
  volatiles.
- Magnet-free actuators (induction, switched reluctance) as the route around the rare-earth bottleneck.
- Whether a local chip chain can be shortened: a clean-room and ultrapure-water budget per wafer (not searched).
- A cycler-versus-direct mass budget on equal assumptions ([CY] 8).
- Solar-wind Fe/H enrichment (arXiv 2411.18984 surfaced, not read).
- Human-shaped machine production rate and the bill of materials by mass and element (not found).
- **Next step, not yet taken:** compare this with the existing interplanetary timeline and propose adjustments to the developer.
