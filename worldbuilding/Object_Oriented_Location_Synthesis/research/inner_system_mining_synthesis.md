# Mining the inner Solar System: synthesis

*OOLSD, written 2026-10-11 from the three tranche-7 files plus the tranche-6 files. Answers the developer's question: "it sounds as though
it would be better to stage a full-scale mining operation on Mercury (and maybe possibly Venus, maybe). What would be the logistics of mining
the inner Solar System?" Status: a synthesis of unreviewed research. Every figure traces to a row in a source file or to a numbered line in
`_calc/inner_mining_synthesis_calc_output_run2.txt` (run 1 had a unit error in the strip-area lines; run 2 is authoritative).*

## 0. Method and limits

- **Nothing in this file was read from canon or the interplanetary timeline.** The comparison with canon is a separate step, not yet done.
- **Inputs (read-only):** **[ME]** `mercury_as_industrial_site.md` (582 lines) · **[VE]** `venus_as_extraction_site.md` (437) ·
  **[NW]** `inner_system_logistics_network.md` (849) · **[TR]** `space_trucking_and_transport_infrastructure.md` · **[PR]**
  `space_processing_and_fabrication.md` · **[SL]** `starlifting_physics_and_minimum_infrastructure.md` · **[RM]** `industrial_ramp_timelines.md` ·
  **[SYN]** `starlifting_synthesis.md`. References like F6, D8, 3.7 are sections in those files.
- Each file was reviewed by me (key tables read), not independently verified. Their candidate handwaves are entered in
  `04_Handwave_Register.md` as C-75 to C-95 (proposals, none accepted) and their open threads in `DEFERRED_RESEARCH.md` Batches 13 to 15.
- **Evidence words:** DEMONSTRATED (flown or built), STUDY (a quantitative design), SPECULATIVE, DERIVED (arithmetic from sourced inputs).
- **No study sizes any Mercury or Venus extraction economy.** Where this file gives a fleet or a flow it is the research agents'
  derivation from sourced rates, not a published design ([NW] F6, [VE] 3.9). That is stated again where it matters.

## 1. The short answer

1. **Mercury's surface is not an iron ore, so Mercury is not the obvious bulk-metal mine.** MESSENGER measured about 1 to 2 wt% iron at the
   surface (13 to 19 kg per tonne), partly as sulfide, with no free iron-nickel metal measured anywhere. The planet's metal is in a core
   420 to 470 km down. The average rock is a magnesium-rich silicate with silicon about 25%, magnesium about 11%, aluminum about 7%, calcium
   4 to 6%, sulfur 2 to 4%, sodium about 3%, and 1 to 2% carbon as graphite ([ME] F1, F2, D1).
2. **What Mercury does offer:** the most sunlight in the inner system (4.6 to 10.6 times Earth's), a shallow gravity well (escape 4.25 km/s,
   9.0 MJ/kg), no atmosphere, polar water ice (1 x 10^13 to 3 x 10^15 kg, uncertain about 100-fold), and silicates, magnesium, aluminum,
   calcium, sulfur and carbon in quantity ([ME] F5, F6, F8).
3. **The hard part is not mining Mercury, it is leaving it.** A launcher to Mercury escape or orbit is plausible on paper. Everything
   after that is not: reaching Earth costs 7.55 km/s from low Mercury orbit, shipments are possible only inside two-week windows every
   116 days, arrivals come in at 6.5 to 11 km/s, and every way of carrying the cargo (electric tugs, sails, flyby routes) fails or
   becomes enormous at megatonne scale (section 5).
4. **Venus cannot be a bulk exporter on any figure found.** Its value is carbon and nitrogen in quantity (atmospheric carbon 1.9 x 10^4
   times Mars's) for use at Venus, but leaving the cloud deck costs about 9 km/s at a studied payload fraction of 0.15 to 0.56%, which
   means 180 to 670 kt of vehicles and propellant lifted for each 1 kt delivered. There is no study of exporting by any means except
   rockets, and a stationary space elevator is geometrically impossible ([VE] 3.7).
5. **The numbers favor different sources for different customers:** the Moon and near-Earth or carbonaceous asteroids for Earth-side
   metal, oxygen and water; the main belt for Mars (belt-to-Mars costs 44 to 59% of belt-to-Earth in delta-v); Mercury for energy-intensive
   and local-use work and for polar ice; Venus for local atmospheric chemistry (sections 3 and 6).

## 2. What each body can supply, per tonne of material, from sourced figures

| Source | Iron | Other things of value | Cost to leave (from the surface or low orbit) | Notes |
|---|---|---|---|---|
| **Mercury** surface | 13 to 19 kg/t (53 to 77 t of regolith per t Fe), partly sulfide | Si 250, Mg 110, Al 67, Ca 40 to 60, Na 29, S 19 to 23, C 14 kg/t; polar ice | Escape 4.25 km/s (9.0 MJ/kg). Low orbit to Earth 7.55 km/s (13.09 km/s all-propulsive), 105 d | Regolith depth disputed: 3.7 to 4.6 m vs 25 to 40 m ([ME] F3) |
| **Venus** atmosphere | none | Air at 55 km holds about 250 g C and 21 g N per m^3; total C 1.3 x 10^20 kg, N 1.1 x 10^19 kg; hydrogen only 7 x 10^14 kg | About 9 km/s from the cloud deck to orbit; payload 0.15 to 0.56% of lift-off mass | Surface is basalt with no measured metal enrichment ([VE] 3.2, 3.6, 3.7) |
| **Moon** (mare) | 140 to 170 kg/t, mostly in silicates and ilmenite (7 to 13 times Mercury's grade) | O, polar water, regolith for shielding | 2.52 km/s to LEO with aerocapture (5.60 km/s all-propulsive), 5 d | Lunar launcher point design 650,000 t/yr ([TR] F2; [SL] 3F) |
| **Carbonaceous (CI) asteroid** | 183 kg/t (10 to 14 times Mercury's grade) | C 3.5 wt%, N 0.3 wt%, H 2.0 wt%, water up to about 20 wt% | Main belt 2.2 AU to Earth 4.21 km/s depart (8.54 all-propulsive), 370 d; to **Mars 1.91 (3.76)**, 464 d | CI is the most volatile-rich class, not an average asteroid ([VE] 3.2; [TR] D1) |
| **Metal-rich asteroid** | "may be up to 99%" native ferrous alloy for M-types | Ni, Co, platinum-group carbonyl residues | as the belt row | 1990 report, hedged ([PR] 1b) |
| **The Sun** (reference) | 1.2 kg/t | none usable | about 1.9 x 10^11 J/kg | 11 to 16 times poorer than Mercury's surface in iron by mass ([SYN]) |

These are grades, not recoverable fractions: lunar iron sits in silicates and ilmenite, Mercury's partly in sulfide, and nobody has measured
how much of either is free metal or how it would be won (no Mercury regolith process study exists, [ME] F10).

## 3. Mercury as a site

**What a mine at the surface looks like** (DERIVED, calc 2). To produce iron at all it must process large tonnages for a by-product:

| Iron output | Regolith processed | Strip area per year at 4.6 m depth, assumed lunar density 1,660 kg/m^3 |
|---|---|---|
| 1 kt/yr | 0.05 to 0.08 Mt/yr | 0.007 to 0.010 km^2 |
| 100 kt/yr | 5.3 to 7.7 Mt/yr | 0.7 to 1.0 km^2 |
| 1 Mt/yr | 53 to 77 Mt/yr | 6.9 to 10.1 km^2 |

At 1 Mt Fe/yr the same stream carries 5.8 to 8.5 Mt/yr of magnesium, 13 to 19 Mt/yr of silicon and 3.5 to 5.2 Mt/yr of aluminum as unavoidable
co-products. **The density is an assumed lunar analog; Mercury regolith density, strength and grain size have no measurement** ([ME] F3).
The 1 to 2 wt% average itself has a stated systematic uncertainty (iron grains above a few tens of micrometers could shift the X-ray
ratio by up to a factor of five; the gamma-ray value, 0.077 Fe/Si, bounds it near 2 wt%, [ME] F1), and local grades are unknown: the
high-magnesium region has the highest Fe/Si measured.

**Environment** ([ME] F4 to F7, F11):

- **Equator:** 88 days of continuous day at up to 451 C (724 K) near perihelion, then 88 days of night near 110 K. Solar power stops for
  the whole night: about 2,100 kWh of storage per kW of continuous load.
- **Poles:** cold traps near 100 K average, water ice beneath about 10 cm of dark material; the best-lit polar point is sunlit about 82% of
  the solar day, no peak of eternal light is known; about 32 days of darkness per solar day if contiguous, 760 kWh per kW.
- **Heat rejection governs by day.** A room-temperature surface facing the Sun needs absorptance/emittance near 0.03; a radiator beside
  sunlit ground has a 580 K sink; ground infrared alone is about 12.7 kW/m^2 against about 0.4 to 0.5 kW/m^2 of rejection at body
  temperature. Flown arrays run at 150 to 230 C by tilting and mirrors and still lose power (20% in a simulated month in BepiColombo tests).
- **Radiation:** solar particle fluence several to about 25 times Earth's, about a third of the warning; the weak field gives no
  protection above tens of MeV; galactic cosmic rays are within a few percent of Earth's.
- **Launch to Mercury escape or orbit** (supported by the numbers): 4.25 km/s, 9.0 MJ/kg, 0.92 km of track at 1,000 g; at the lunar design's
  scaling, 0.29 to 0.30 GW of electrical power for 1 Mt/yr at 100% duty ([NW] F6(b); [ME] F8). **Direct launch onto Earth, Venus or Mars
  transfers is not supported:** 7.4 to 11.8 km/s muzzle speeds, 14 to 24 times the lunar design's energy, asymptotes a median 19 to 26
  degrees out of Mercury's orbital plane, and a fixed track on the slowly turning surface has about 2.4 usable days in six years for Earth
  (20 to 35 days if any asymptote declination were acceptable) ([NW] F4).
- **No lander has operated on Mercury.** The one detailed design (2020 NASA study) lands at dusk, runs on an RTG, and ends shortly
  after sunrise on thermal grounds ([ME] F6, F12).
- **No published Mercury mass driver, Mercury industry or Mercury space-solar-power concept was found**; the only Mercury material-use
  work is the whole-planet disassembly thought experiment (31 years, exponential self-replication assumed, authors call it unlikely to be
  attempted, built on a 70%-metal bulk that is the core) and a propellant-from-polar-ice crewed-mission study ([ME] F9).

## 4. Venus as a site

- **Extraction from the air is demonstrated at instrument scale:** the Mars MOXIE unit made 6 to 12 g/hr of oxygen from CO2 at 300 W
  (25 to 50 kWh per kg at that scale), a full-scale plant study gives about 5.7 kWh per kg of oxygen (thermodynamic floor 4.9),
  and Venus needs no compressor at cloud pressure. One full-scale plant (3 kg/hr) uses about 72 t of CO2 per year; splitting all of
  Venus's CO2 needs 3 x 10^27 J ([VE] 3.3, 3.10).
- **Platforms:** two VEGA balloons flew 46.5 hours in 1985; a long-life ISRU-replenished balloon (12.5 m, 10 W, 10 years) is a
  2026 concept; PTFE survives 85% acid in tests, no multi-year exposure exists; failure modes include downdrafts, gravity waves, acid
  drizzle loading and falling into hotter layers (107 C at 50 km, 258 C at 30 km) ([VE] 3.4).
- **Hydrogen is scarce** (7 x 10^14 kg, 400 to 530 times less than Mars's polar deposits, 2 to 6 times Mercury's ice), so hydrogen
  propellant and lifting gas are not locally available; carbon monoxide and oxygen from CO2 are, at 250 s specific impulse ([VE] 3.2, 3.7).
- **The surface is unmineable on present evidence:** 737 K and 92 bar, landers last about 2 hours at most, silicon-carbide electronics have
  run 60 days in a test chamber, rejecting heat into 735 K costs 1.4 to 5.2 W of work per watt, and no surface-mining engineering study exists;
  the rock is an ordinary basalt (SiO2 45 to 49%, FeO 8 to 9%) ([VE] 3.6).
- **Export:** ascent from the cloud deck is about 9 km/s; at 0.15 to 0.56% payload fraction 1 kt delivered requires 180 to 670 kt of
  vehicle and propellant lifted (calc 5). A synchronous orbit for Venus's 243-day rotation lies 1.5 times outside its Hill sphere, so no
  stationary elevator anchor exists; skyhook, balloon-launched electromagnetic launch and beamed propulsion have no Venus study ([VE] 3.7).
- **Orbit and arrival are the easy end:** aerocapture there is the most beneficial in the inner system (92% delivered-mass gain), though
  the corridor is +/-0.76 degree and the heating exceeds any tested tile ([NW] F5); Venus-to-Earth needs only 2.5 to 2.7 km/s of
  v-infinity, windows every 584 days.
- **Where Venus's carbon and nitrogen matter:** for use at Venus. Carbonaceous material offers nitrogen at 2.95 kg per tonne against
  81 g per tonne of lunar regolith and 21 g per m^3 of Venus air (about 45 t of air per tonne of nitrogen at 3.5% by volume) (calc 5).

## 5. The network: routes, windows, fleets (Mercury orbit to Earth vicinity)

**Windows** ([NW] F1, D1, D2, 2030 to 2035 scan): departures from Mercury cluster into windows 8 to 24 days wide (mean 15), about
13% of the time, every 115.9 days to Earth, 144.6 to Venus, 100.9 to Mars; the cheap Earth windows recur about once a year (total
v-infinity 17.6 to 22.9 km/s). Windows leaving the faster inner body are narrower than windows leaving the slower outer body, so inbound
cargo from the inner system bunches harder than supply going out to it. Venus-to-Earth windows recur every 1.6 years.

**Routes** ([NW] F2, F3):

| Route, low Mercury orbit to Earth | Propulsive delta-v | Time | Status |
|---|---|---|---|
| Direct impulsive Hohmann | 7.55 depart, 5.54 capture (13.09 all-propulsive) | 105 d | DERIVED |
| Direct low-thrust spiral | about 22.4 km/s | loaded leg 1.2 to 5.2 yr | DERIVED |
| Chemical with Venus and Mercury flybys | about 2.8 km/s (outbound direction) | about 4.2 yr | STUDY (Earth to Mercury only) |
| Solar-electric with 1 Earth, 2 Venus, 5 Mercury flybys | about 2 km/s | about 9 to 10 yr | STUDY (outbound only) |
| Photon sail, no flybys | none | 369 d at 0.78 mm/s^2 (2.85 yr at 0.25) | STUDY |

Every primary source studies the Earth-to-Mercury direction; no Mercury-to-Earth cargo route study was found. A flyby route is a schedule
tied to resonant alignments, not a lane ([NW] F2).

**Fleets for a stated flow, Mercury orbit to Earth** (DERIVED by the research agent from sourced rates; no published design; [NW] F6):

| Flow | Solar-electric direct spiral (100 kW tugs) | Solar-electric with flybys | Photon sails |
|---|---|---|---|
| 1 kt/yr | 24 to 53 MW; 240 to 530 tugs; 2,400 t/yr of propellant (**37 times world xenon output**) | about 130 stages/yr; 63 t/yr xenon (about one year of world output) | 133 to 336 km^2; 0.8 to 2.0 kt of sail |
| 100 kt/yr | 2.4 to 5.3 GW; 24,000 to 53,000 tugs | about 13,000 stages/yr; 6,300 t/yr xenon (97 times world output) | 13,300 to 33,600 km^2; 78 to 198 kt |
| 1 Mt/yr | 24 to 53 GW; 240,000 to 530,000 tugs (1.6 to 3.6 Mt of tugs) | about 130,000 stages/yr; 63,000 t/yr xenon | 133,000 to 336,000 km^2 (1.8 to 4.4 million Hughes-size sails); 0.8 to 2.0 Mt of sail |

Reading ([NW] F6, F9, F11; calc 3, 4):

- **The Mercury leg is 7 to 15 times less productive per kilowatt than the lunar leg** (19 to 41 t per MW-year against 279) and needs 2.4 t of
  propellant per tonne delivered against 0.18. **Xenon fails at 1 kt/yr by direct spiral**; Mercury's ice (about 10^14 to 10^15 kg)
  could feed it for 40,000 to 400,000 years, but **no high-specific-impulse water thruster has flown** (the one flown water thruster gives 70 s).
- **Flybys cut propellant 38-fold but lock up ten years of cargo** in flight and deliver in batches fixed by the alignments (Little's Law:
  flow times trip time).
- **Sails need no propellant but the sail fleet's mass equals about a year of cargo,** the largest sail flown in deep space is 196 m^2, and no
  sail lifetime in the Mercury environment was found.
- **Arrival:** direct Mercury cargo reaches Earth at 6.5 to 11 km/s v-infinity; stopping in low orbit costs 5 to 7 km/s, aerocapture would be at
  13 to 15 km/s entry speed (beyond the one Venus design studied, 11.25 km/s, itself beyond any tested tile). Slow routes arrive near
  0 to 4 km/s and are cheap to catch. No study sizes a receiving and processing node ([NW] F5).
- **Hardware is not the limit at 1 kt/yr:** 1.6 to 3.6 kt of tugs is 0.5 to 1.2 years of Starlink-class satellite production by mass (calc 4;
  satellite mass is low-confidence trade press). Propellant, route and arrival are the limits.
- **Control and tracking:** the Deep Space Network delivered about 77,000 antenna hours in FY2022 to about 60 missions and was 40%
  oversubscribed, so fleets must navigate themselves; Mercury links black out 3 to 4 times a year for a few days; light time is 2 to 38
  minutes one way; warning of a solar particle event at Mercury is about a third of Earth's, so each node needs its own monitor ([NW] F7, F10).
- **Power beaming** is not a substitute: microwaves need paired apertures of 67 to 226 km at these ranges, lasers hundreds of meters
  with nanoradian pointing; demonstrated links reach 8.6 km in air ([NW] F8).

## 6. What the numbers support, as an architecture

Stated plainly: **these are inferences from the sourced figures, not published designs.**

| Customer | Best-supported source | Why (sourced) | What is missing |
|---|---|---|---|
| Earth orbit: metal, oxygen, water, shielding mass | Moon (mare, poles) and near-Earth or carbonaceous asteroids | 2.52 km/s and 5 days from the Moon, a mass driver at 5,200 t per MW-yr against 280 for solar-electric tugs; asteroids at 183 kg/t Fe and 4.21 km/s | Lunar and asteroid processing at scale is all STUDY or lab ([PR]) |
| Mars orbit: volatiles, metal, shielding mass | Main belt | Belt-to-Mars 1.91 to 3.28 km/s departure against 4.2 to 5.2 to Earth; windows every 2.8 to 4.4 years | No belt cargo-fleet study; the long synodic bunching |
| Local energy-intensive work in the Mercury region | Mercury | Sunlight 4.6 to 10.6 times Earth's, escape 4.25 km/s, polar ice, Mg, Si, Al, Ca, O, S, C in place | Everything on the surface side of the heat-rejection and night problems; no Mercury process study |
| Material that never needs to reach Earth (construction near the source) | Mercury (inference) | Only the 4.25 km/s launch to orbit is needed; the one concept in the literature (disassembly into a swarm at Mercury's orbit) works that way | The literature on it is SPECULATIVE; no engineering design |
| Local habitat chemistry at Venus | Venus clouds | Carbon and nitrogen in the air at 250 and 21 g per m^3; MOXIE-class chemistry works at cloud pressure | Platform lifetime, scale, hydrogen |
| Bulk export from Venus | none supported | 180 to 670 kt lifted per kt delivered | Any non-rocket launch study |

The picture that follows is not "Mercury as the mine." It is **several mines, each matched to what its material is good for and where it can
go**, with Mercury's role set by energy and by what can be made *there* and used *near there*. **What would change this** (each is a
research or design finding, none is available now): free iron-nickel metal found at Mercury's surface at a stated grade; a flown high-Isp
water thruster (opens the 2.4 t-per-tonne tug case); a measured sail lifetime near Mercury; a Mercury-to-Earth flyby route study;
single-pass aerocapture flown at 13 to 15 km/s; any engineering study of Venus launch other than rockets.

**Scale and time.** The ramp arithmetic in [SYN] applies unchanged: a Mercury flow of 1 kt/yr is reachable only after the ramp stages that
produce kt-per-year industry (about 15 to 27 years after commitment in the fast-growth reading), and Mercury adds no shortcut because its
first stage (commitment to working hardware, 8 to 13.5 years) has no flown precedent and the lander design needs a decade of cruise alone
(launch 2035, arrival 2045 in the 2020 study).

## 7. The setting this implies (constraints, from the three files)

- **Pulses and convoys, not streams:** two weeks of good departures every 116 days from Mercury, cheap ones once a year, flyby convoys fixed
  by alignment, and ten years of cargo in flight on the long route.
- **Heat and night are the working conditions at Mercury:** 88-day nights, 700 K ground by day, shade and polar sites as the livable places,
  machines that either run hot (silicon carbide at 500 C) or live behind shields.
- **Distance and autonomy:** 4 to 12 minutes one way to Mercury, outages every few months, tracking capacity that does not exist, so fleets
  and nodes act alone; particle storms hit with minutes of warning.
- **Dependence on receiving ends:** reserves for a window gap plus one lost shipment (the ISS holds 45 days of food); anything fragile
  travels by tug or sail, not in a mass-driver stream (hundreds to 1,000 g).
- **Venus is a place to live and make things, not to ship from:** acid, wind and a thin margin above hotter air; carbon and nitrogen in
  quantity; hydrogen scarce; its orbit and aerocapture are friendly, its ascent is not.

## 8. Source conflicts carried

- [NW] Conflict C1 reports that [TR]'s Earth-to-Mercury v-infinity sum is understated: 17.1 km/s (7.53 + 9.61), not 15.1; not yet corrected in
  the trucking file (it is not edited here).
- [ME] disagreements: regolith thickness (3.7 to 4.6 m vs 25 to 40 m), iron normalization (factor of five), high-magnesium region crust
  thickness, meteoroid dust flux (45-fold), polar ice mass (100-fold).
- [VE] Conflicts section: lightning evidence disputed; cloud temperature profiles differ between models.

## 9. Candidate handwaves raised at synthesis level

Flagged for the developer; none accepted. (The files' own candidates are entered in the register as C-75 onward.)

- **M-1.** Mercury as a bulk iron exporter. Needs a free-metal grade nobody has measured, or access to the core 420 to 470 km down.
- **M-2.** Venus as a bulk exporter by any means. 180 to 670 kt lifted per kt delivered by rocket; no other method has a study.
- **M-3.** Mercury-to-Earth cargo at kt per year or more by any studied propulsion, without one of the "what would change this" items.

## 10. Open threads

- Mercury-to-Earth and Mercury-to-Venus cargo route studies with flybys (none found); Mercury process studies for a high-sulfur,
  high-alkali, low-iron regolith (none found); sail lifetime in Mercury orbit; a measured Mercury regolith density, grain size and strength.
- Surface-mining engineering for Venus (none); non-rocket Venus launch (none); an economics study of Venus volatile export (none).
- A high-Isp water or steam electric thruster flown; a dose figure for electronics at 0.3 to 0.5 AU.
- Nothing here yet compares these findings with the interplanetary timeline or places Mercury or Venus in the fiction.
