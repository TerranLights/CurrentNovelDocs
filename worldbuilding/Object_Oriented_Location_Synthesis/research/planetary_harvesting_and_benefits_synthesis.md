# Harvesting Mercury and Venus whole, and the benefits of mining Mercury, Venus and the Sun: synthesis

*OOLSD, written 2026-10-12 from the eleven tranche-8 research files, answering the developer's request: research all aspects of
harvesting Mercury and Venus themselves; research every benefit of mining the two and "mining" the Sun; and answer whether oxygen can be
harvested from Mercury or Venus and hydrogen from the Sun and trucked to Mars to give Mars water. Status: a synthesis of unreviewed
research. Every figure traces to a row in a source file; the agents' calculation scripts are in their scratch folders, and the earlier
arithmetic is in `_calc/` (`planet_disassembly_calc_output.txt`).*

## 0. Method and limits

- **Nothing here was read from canon or the interplanetary timeline.** The comparison with canon is a separate step, not yet done.
- **Sources (all in `research/`, read-only):** **[PDL]** `planet_deconstruction_literature_and_engineering.md` (353 lines) · **[MWI]**
  `mercury_whole_planet_inventory_and_extraction.md` (392) · **[VWI]** `venus_whole_planet_inventory_and_stripping.md` (395) ·
  **[PWH]** `planetary_scale_power_and_heat.md` (650) · **[ORB]** `orbital_dynamics_of_planetary_harvesting.md` (420) · **[OHM]**
  `oxygen_and_hydrogen_supply_for_mars_water.md` (432) · **[MWB]** `mars_water_budget_and_retention.md` (415) · **[BME]**
  `benefits_of_mining_mercury.md` (454) · **[BVE]** `benefits_of_mining_venus.md` (416) · **[BSU]** `benefits_of_mining_the_sun.md` (440)
  · **[VAL]** `value_and_markets_of_inner_system_materials.md` (507). Earlier syntheses: **[SYN]** `starlifting_synthesis.md`,
  **[IMS]** `inner_system_mining_synthesis.md`.
- I read the findings tables, constraints, handwaves and ranked tables of each file and the agents' reports; I did not re-verify
  individual citations. Their candidate handwaves are entered in `04_Handwave_Register.md` as C-96 to C-167 (proposals, none accepted) and open threads in
  `DEFERRED_RESEARCH.md` as Batches 16 to 26.
- Evidence words: DEMONSTRATED, ENGINEERING-STUDIED, SPECULATIVE, DERIVED. **No source gives an engineering design for taking apart a
  planet; every published timescale is a thought experiment** ([PDL] F5).

## 1. The short answers

1. **Oxygen from Mercury or Venus to Mars fails on every link.** Rock everywhere is 33 to 47 wt% oxygen and Mars's soil is about 43%;
   shipping oxygen to low Mars orbit costs 16.9 km/s from Mercury and 15.2 km/s from Venus's cloud deck, against 0 km/s for Mars's own
   ([OHM] F3).
2. **Hydrogen from the Sun is plentiful in the Sun, but not plentiful to harvest.** One tonne of hydrogen a year needs 8,200 to 12,300 km^2
   of perfect collector at 1 AU (82 to 123 km^2 at 0.1 AU), and no capture-and-store device exists even as a design. Lifting it from the
   photosphere takes 8.1 GW of continuous power per kt/yr at the theoretical minimum ([OHM] F4).
3. **Mars does not need the water.** It already holds 16 to 22 m of global-equivalent water in its polar caps alone and 20 to 40 m near the
   surface. What it lacks is warmth and pressure; loss to space is slow (1 m lasts 0.3 to 3 billion years today) ([MWB], [OHM] F5).
4. **Taking Mercury apart is limited by heat, not by machines or collector mass.** At the published 31-year pace its whole surface would
   radiate at about 4,600 K; even a 1,000-year pace puts it near 840 K ([PWH] F6, H-1). The top ~26% of its mass is nearly iron-free
   ([MWI]).
5. **Venus's solid body has no disassembly study.** Removing the atmosphere alone takes 2.6 x 10^28 J (about 2,700 years of all the sunlight Venus
   intercepts) ([VWI]).
6. **Removing a planet is not a local act.** Cutting Venus to 25 to 52% of its mass sweeps Mercury through the resonance that makes it
   chaotic, and reshapes Earth's eccentricity cycles ([ORB]).
7. **Every benefit of the Sun that works today comes from its light and gravity, not its matter** ([BSU]). Mercury's benefits are
   local (energy, crustal materials, ice, sulfur); Venus's are local too, plus gravity assists ([BME], [BVE]).
8. **On the sourced numbers, only short, shallow routes with bulk cargo pass the break-even test:** Moon to cislunar space, the Moon's own
   surface, and the belt to Mars. Mercury-to-Earth cargo fails by 2 to 11 times; Venus and solar-wind cargo fail everywhere ([VAL] G).

## 2. Harvesting the planets themselves

### 2.1 What the literature supports

- **Every published timescale is a thought experiment** ([PDL] F5). Armstrong and Sandberg's "Mercury in 31 years 85 days" assumes
  self-replicating automation, a 1/3 power chain, 1/10 of the power to launching, a 5-year processing delay, half the mass usable, and
  unlimited launchers, catchers and power delivery; the file reproduced it at 35.6 years from the paper's own assumptions. "Mercury in 5
  hours" (Bradbury) is an energy floor, not a schedule.
- **The only rates with hardware behind them** are the 1970s lunar launcher and catcher (under 1 Mt/yr each) and the 1985 launch loop (3.5
  Mt/yr). At those rates all of Mercury is about 10^14 machine-years of work; a 1,000-year pace needs about 2.5 x 10^11 lunar-class
  launchers and 10^12 catchers running continuously ([PDL] F5, handwave D-2).
- **A swarm built from the planet is a debris field waiting to happen:** unmaintained, one at Mercury's distance would start colliding
  within weeks ([PDL] constraints).
- **Partial harvesting is enough for a full swarm on the literature's own areal masses:** the same sphere at 4.2 g/m^2 needs 0.05% of
  Mercury's mass, not 50%; removing the crust alone in 1,000 years is 2.5 x 10^11 kg/s ([PDL] F6).

### 2.2 Mercury, layer by layer ([MWI])

| Layer | What it is | Consequence |
|---|---|---|
| First ~26% of the mass, down 377 to 470 km | Nearly iron-free silicate (about 1 wt% Fe); crust and mantle | Everything built from early output is glass, ceramic, aluminum, magnesium or silicon, not iron |
| Below roughly 270 to 340 km | Rock hot enough to melt if the load above is removed; 7 to 11 wt% sulfur and some carbon | Deep workings meet partial melt, sulfur-gas and CO release |
| Core | Liquid metal at about 1,700 to 1,950 K under 5 GPa; bare-core surface gravity 3.99 m/s^2 (stronger than Mercury's today) | Exposed core radiates ~0.6 to 0.9 MW/m^2 and evaporates iron until it skins over; escape speed falls only from 4.25 to 4.02 km/s |

The "70% iron" figure is true of the core's mass share (73.9%) with light elements dissolved; bulk Fe is 50 to 69 wt% ([MWI] HW-7). Hydrogen
and nitrogen are not in Mercury in quantity (its only known hydrogen is the polar ice; no nitrogen has been measured).

### 2.3 Venus, layer by layer ([VWI])

- **Interior:** core radius somewhere in 2,900 to 4,350 km, holding 22 to 38% of the mass, state unknown; crust 8 to 25 km. Four bulk models
  agree on oxygen at about 31 to 34 wt%, iron 28 to 31%, silicon 14 to 17%, magnesium 15 to 16%. Venus lacks water and hydrogen.
- **The atmosphere is the first layer.** Sending all of it to escape takes 2.6 x 10^28 J; a century takes 27 times all the sunlight Venus
  intercepts, at 100% conversion. Chemical routes fail on hydrogen (the Bosch route needs 61,000 times Venus's hydrogen) or need about 2
  km of crust ground and reacted for carbonates, and only hold below about 560 K. A sunshade-and-freeze scheme leaves about 90 bar of CO2 as
  ice that returns if the shade fails.
- **After the atmosphere:** about 58 days of sun at up to ~450 K, 58-day nights, meteoroids at 10 to 14 km/s with nothing to stop them,
  and a cooling crust that cracks (30 MPa of thermal stress per 100 K against 12 to 21 MPa of strength).
- **The solid body:** binding energy 1.6 to 1.7 x 10^32 J (88 times Mercury's); 1.5 x 10^14 kg/s for a 1,000-year schedule; no published
  concept. Material thrown near escape speed stays on Venus-crossing orbits and much of it returns over millions of years unless caught.

### 2.4 Energy, heat and power ([PWH])

- **Collector mass and area never limit the job. The heat made on the planet does.** At Mercury, planet-side losses of a 31- to
  1,000-year disassembly exceed the sunlight already falling on the surface by 3 to 1,300 times; the efficiency needed merely to
  match today's sunlight is 99.963% (31 yr), 99.880% (100 yr) or 98.80% (1,000 yr), against 96.4% (coil losses only) as the best
  sourced figure. The paper's own end state puts 10^23 to 10^24 W near Mercury, nine-tenths as heat: an 18,000 to 21,000 K surface if radiated
  from the planet, so all processing would have to happen off the planet, which the paper does not specify.
- **Processing the whole planet** takes 5 to 37 times its binding energy by [MWI] and 11 to 99 times by [PWH] (different plant-energy
  bases; both exceed the binding energy by a wide margin). All sourced process chains are 8 to 56 kWh/kg against a mean binding energy of
  5.4 MJ/kg.
- **Power beamed to the surface at 10^19 to 10^21 W** would deposit about 3 x 10^18 to 3 x 10^20 W of heat there (29.8% of what is received); no
  source sizes such a link.
- **Collectors made entirely from the planet** are not shown to be possible: chips, dopants, polymer hydrogen and nitrogen are not in Mercury or
  Venus in usable form.
- **Night at an equatorial Mercury site** needs 15 to 28 t of battery per kW of continuous load.

### 2.5 Orbital and dynamical consequences ([ORB])

| Effect | Finding (the first four are the agent's own calculations; no study of planetary mass removal was found) |
|---|---|
| Recoil on the planet | A planet's own orbit barely changes when mined; moving it "a little" (1% in semimajor axis) costs 2.4 to 21% of Mercury or 1.7 to 16% of Venus expelled in one direction |
| Mercury's spin | A net one-directional launch of about 5 x 10^16 kg/yr (or ~7 x 10^17 kg in a burst) knocks Mercury out of its 3:2 spin lock; the published planetary-scale pace is ~10^22 kg/yr, 10^5 times above that. Launch tracks balancing east and west, or radial launch, avoid it |
| Venus's spin | Throwing the atmosphere off tangentially pushes back on the planet with 1.2 to 1.7 times its whole spin, so launch direction sets the day (about 90 days retrograde to about a year prograde); exporting the whole atmosphere cannot shorten the day below about 90 d |
| Other planets | Cutting Venus to 25 to 52% of its mass puts Mercury's precession through g1 = g5; slow removal (10^6 to 10^7 yr) kicks Mercury's eccentricity by 0.1 to 0.4, fast removal (10^4 yr) by about 0.01. Earth's ~100 kyr eccentricity band nearly vanishes, the dominant cycle becomes ~376 kyr and maximum e falls to ~0.043 |
| Catchers | Sun-line L1/L2 points are unstable (doubling in 3.9 d at Mercury, 9.8 d at Venus); catchers need burns several times a month |
| Light structures | A 1 kg/m^2 collector near Mercury spirals into the Sun in ~79,000 yr; a 10 g/m^2 film in ~800 yr; grains under ~0.4 micron blow out |
| Lost debris | A few percent of rock leaving Mercury and 5 to 30% leaving Venus reaches Earth over 1 to 30 Myr; losing 10^-7 of Mercury's mass equals today's zodiacal cloud |
| Unloading | Removing Venus's ~9 MPa air load or ~1 km of Mercury's rock is the same order as the ice load whose removal multiplied Iceland's eruption rate 5 to 30 times; not studied for planets |

## 3. The benefits of mining Mercury, Venus and the Sun

### 3.1 Mercury ([BME] F9)

| Rank | Benefit | Earth transport needed? | Key limit |
|---|---|---|---|
| 1 | Sunlight for energy-intensive processing (Al, Si, Mg, glass, oxygen) | No | Hot arrays; 88-day equatorial night |
| 2 | Bulk crustal material (Si, Mg, Al, Ca, O, S) for structures near Mercury; 9.0 MJ/kg, 4.25 km/s to escape | No | No Mercury process study |
| 3 | Polar water ice (hydrogen, oxygen, propellant) | No | Inventory uncertain 100-fold; 21,000 to 3,000,000 yr at 1 Mt/yr |
| 4 | Oxygen from oxides (30 to 45 wt%) | No | Needs the electricity of rank 1 |
| 5 | Sulfur (24 to 49 times lunar grade) | No | Melts at ~119 C |
| 6 | Cheap high-temperature process heat (solar furnaces need 54 to 124x vs 570x at 1 AU) | No | Night; furnace hardware unstudied there |
| 8 | Launch base for the 0.1 to 0.47 AU region | No | Worse than Earth below ~0.1 AU |
| 11 | Refined material shipped to Venus, Earth or Mars | Yes | The leg itself |
| 13 | Iron and nickel | n/a | By-product at 13 to 19 kg/t |
| 14 | Base for reaching the Sun's surface | No | **4.8 to 13.6 km/s more** than from Earth, except from aphelion |

Every benefit with real support is local. None supports shipping to Earth ([BME]). Popular framing of Mercury as the natural staging
point for the Sun is a premise the arithmetic does not support ([BME] K6).

### 3.2 Venus ([BVE] 3.9)

- **Cheapest first:** gravity assists (4.7 to 7.1 km/s per flyby, no export needed); the scientific record (D/H, noble gases); high-temperature
  electronics know-how; the 50 to 55 km habitat environment (0.9 g, ~1 bar, 1,290 g/cm^2 of shielding, air as lift gas); local O2, CO, N2, Ar, CO2
  at the intake (5.7 kWh per kg O2; 0.3 to 0.45 MJ per kg N2 floor); solid carbon without hydrogen (~8.8 MWh per t C).
- **Export is not competitive:** 180 to 670 kg lifted and 0.31 to 1.34 MWh per kg delivered to Venus orbit; nitrogen and carbon to Mars, Mercury,
  the Moon or habitats is "not competitive on any figure found". Ideal mass ratio to a Mars transfer on local CO/LOX at 250 s is 124, against 13.6
  from Earth on hydrolox. **Earth's air is richer than Venus's in nitrogen (34 times), argon (~200 times) and krypton (36 times).** Carbon is
  the one exception. Carbonaceous asteroids give 2.95 kg N per tonne against 21 g per m^3 of Venus air.
- **Deuterium** at 100 to 160 times terrestrial concentration is speculative (total only 2 to 3 x 10^13 kg).

### 3.3 The Sun ([BSU] F9)

| Rank | Benefit | Lifts solar matter? | Evidence |
|---|---|---|---|
| 1 | Sunlight as electric power (1,361 W/m^2 at 1 AU to 136,000 at 0.1 AU; arrays 80 to 150 W/kg) | No | DEMONSTRATED |
| 2 | Concentrated sunlight as process heat (up to 10 MW/m^2 demonstrated) | No | DEMONSTRATED on Earth |
| 3 | Radiation pressure: sails, statites (9.1 uPa at 1 AU, x100 at 0.1 AU) | No | DEMONSTRATED at 196 m^2 |
| 4 | Solar Oberth maneuver (3 km/s at 3.2 R_sun gives 45.6 km/s outbound); judged no better than a Jupiter assist by APL | No | ENGINEERING-STUDIED |
| 5 | Solar-thermal propulsion (~630 s hydrogen-equivalent, ground) | No | Ground-DEMONSTRATED |
| 6 | Solar-wind hydrogen and helium (78 to 82 km^2 per t/yr of H at 0.1 AU) | No | SPECULATIVE beyond Genesis's milligram |
| 7 | Solar-wind helium-3 (39 to 54 g per tonne of wind) | No | SPECULATIVE; D-3He has never given net energy (best Q 1.25%) |
| 8-9 | Solar-wind noble gases, nitrogen, metals | No | SPECULATIVE; iron needs 18,000 to 25,000 km^2 per t/yr at 0.1 AU |
| 10-12 | Photospheric starlifting, stellar engines, solar antimatter | Yes (the first two) | SPECULATIVE |

**Plainly: every benefit that is real today comes from the Sun's light and gravity, not from its matter** ([BSU]). The iron-in-wind area
is smaller than [SYN] gave (86,000 km^2) by a factor of 3.5 to 4.8: a flux-basis difference of 1.5 times the measured FIP enrichment of iron
(2.0 to 2.9), which resolves an open thread from [SYN].

### 3.4 What is worth moving ([VAL] G, H)

| Route | Verdict on the sourced numbers |
|---|---|
| Lunar regolith or slag as shielding, Moon to L2 or L5 | PASS by 7 to 500 times (optimistic hardware); fails against a $200/kg launch future if hardware costs $1 M/kg |
| Lunar water or propellant to LEO | PASS today, optimistic hardware only; fails at $200 to $1,000/kg launch |
| Lunar propellant used on the lunar surface | PASS at 17 t/yr or more with a 3 to 5-year plant life |
| Belt material to low Mars orbit | PASS today ($625 to $1,900/kg delivered vs $6,400 to $13,900 value); marginal to fail at $200/kg Earth launch |
| Mercury material to Earth orbit (spiral tug or sail) | FAIL by 2 to 11 times ($7,600 to $20,200/kg vs $1,782 to $3,868); the sail passes only if it lasts about 10 years at mass-production cost, and then fails at $200 to $1,000/kg launch |
| Mercury material used near Mercury | PASS on transport (2.51 kWh/kg to orbit); the surface plant (heat, night) has no study |
| Venus cloud-level carbon, nitrogen or argon to any orbit | FAIL everywhere by 4 to 400 times on hardware alone |
| Solar-wind matter | FAIL (payback about 1,350 years at 0.1 AU); the ceiling is the wind's mass flux, a physics limit |
| Space solar power to Earth | FAIL baseline by 12 to 80 times (NASA LCOE $0.61 to $1.59/kWh vs $0.02 to $0.05) |
| Lunar helium-3 | Market-limited: 5.4 kg/yr, about $80 M/yr even at $14.9 M/kg |

**The pattern:** short, shallow routes carrying low-value bulk to places where the alternative is Earth launch. Every route that passes becomes
marginal or fails if Earth launch reaches $200/kg, unless hardware is mass-produced near $10,000/kg or less. Time costs nothing on lunar routes but the
Mercury flyby route's 9.8 years of cargo in flight multiplies the value cargo must reach by 1.6 to 6.8 at 5 to 21.7% capital cost, and at 1 Mt/yr holds
$2 to $38 trillion in flight. The honest units for benefits that are survival or capability are mass not launched from Earth (about 10 kg per kg of propellant
made on Mars) and time not spent waiting for a window.

## 4. The developer's question: oxygen from Mercury or Venus, hydrogen from the Sun, water for Mars

**Verdict: the premise holds in two places and fails in the rest.** It holds in that both elements exist in vast quantity (hydrogen is 74% of
the Sun by mass; oxygen is about half of every rock), and water is exactly H2O. It fails because Mars already has both locally and the
imports are very costly.

| Link | Sourced finding | Source |
|---|---|---|
| Oxygen at Mercury | 42.5 to 47 wt% in surface rock by stoichiometry (about 30% as measured); 11.5% of the whole planet; no oxygen process studied on its sulfur-rich, iron-poor feed; hydrogen reduction of FeO yields almost nothing there; plant power 11.5 MW per kt O/yr at 114 kWh/kg | [OHM] F1 |
| Oxygen at Venus | 72.7% of CO2; 3.4 x 10^20 kg in the atmosphere; solid-oxide electrolysis 5.7 kWh/kg O2; 1.75 kg CO per kg O2 | [OHM] F2 |
| Oxygen at Mars | Soil 42.5 to 43.6%; air holds 1.75 x 10^16 kg of O; ice 88.8%; extraction 1.5 to 18.5 kWh/kg of water from regolith, 5.7 kWh/kg O2 from air | [OHM] F3 |
| Shipping oxygen to low Mars orbit | From Mercury 10.34 (aero) to 16.94 km/s, 1.9 t propellant per t by spiral; from Venus 11.82 to 15.19 km/s ideal, 248 to 985 t of CO/LOX per t delivered; from the Moon 3.28 to 5.37; from the belt 1.91 to 6.10; from Phobos 1.21 | [OHM] F3c |
| Fleet for 1 Mt/yr of oxygen from Mercury | About 28 GW of tugs burning 1.7 Mt/yr of propellant (world xenon ~65 t/yr) | [OHM] F3c |
| Hydrogen by solar-wind collection | 1 t/yr needs 8,200 to 12,300 km^2 at 1 AU, 82 to 123 at 0.1 AU, 18 to 27 at Parker's perihelion, always as a perfect collector; hydrogen is 83 to 86% of the wind by mass; no device exists; best flown yield is about 10^-11 kg per kg of spacecraft per year (Genesis); a proposed electrostatic inlet would store about 0.06 kg/yr per km of diameter at 1 AU | [OHM] F4a |
| Hydrogen by lifting from the photosphere | 2.57 x 10^11 J per kg of H; 8.1 GW per kt/yr; yield per unit hardware undefined | [OHM] F4b |
| Hydrogen from CMEs | Adds 1 to 5% to the wind; helium-rich | [OHM] F4c |
| Moving hydrogen | Liquid H2 at 20.4 K, 70.85 kg/m^3; passive boil-off 0.6 to 6% per month; cooling costs 117 to 467 W of input per W lifted at 20 K; ammonia, methane and water all hold more hydrogen per m^3 than liquid hydrogen; shipping hydrogen instead of water moves 8.94 times less cargo | [OHM] F6 |
| Sizes of "giving Mars water" | 1 kt of water needs 112 t of H and 888 t of O (collector 1.33 x 10^6 km^2 for a year at 1 AU); 1 Mt needs 1.33 x 10^9 km^2; a 1 m global layer (1.44 x 10^17 kg) is 0.45 years of the Sun's entire wind hydrogen, or about 11 seconds of the Sun's total output spent on lifting | [OHM] F7 |
| Mars's own water | Polar layered deposits alone 16 to 22 m global-equivalent (2.3 to 3.2 x 10^18 kg); near-surface 20 to 40 m; buried glacial ice hundreds of meters thick | [OHM] F5, [MWB] |
| Alternatives nearer Mars | Phobos 1.2 km/s to orbit (water unknown until MMX returns samples in 2031); Ceres up to ~25% water, windows every 3.18 yr; carbonaceous asteroids ~20 wt% water (CI), belt to Mars 1.91 to 3.28 km/s; lunar polar ice; Mercury polar ice 10.34 to 16.94 km/s away | [OHM] F5 |
| Mars's air as an oxygen source | Enough oxygen for only about 0.14 m of global water; beyond that, oxygen must come from rock or ice, and each kg of water made from air by reverse water-gas shift leaves 1.55 kg of CO | [OHM] F8 |

**What "giving Mars water" would actually need,** by purpose ([MWB]): a settlement's life support is tiny (a million people use 1 m of global-equivalent
water in 13 million years open-loop); one crewed ascent needs about 16 t of water; Earth-style open farming is the largest use at 2,000 to 5,000 L per
person-day. An open lake disappears in under 60 years at any pressure from 7 mbar to 3 bar unless covered or resupplied; water vapor cannot pressurize the
air (at most 612 Pa at 0 C); and making liquid water stable needs about 60 K of warming, which the available CO2 cannot deliver. Delivered water ends up as
ice, liquid or mineral-bound, and 30 to 99% of Mars's original water is in crustal minerals. Losses to space are slow; the fast losses are to the ground. A
magnetic shield would mainly address storm bursts and surface radiation, not the steady loss, which is already slow.

**Where an import would be needed:** an ocean. A 137 m global-equivalent ocean needs 1.4 to 1.7 x 10^19 kg beyond what is on the surface; a 30 kPa nitrogen
buffer is 1.2 x 10^18 kg, 2,800 times what the atmosphere holds, with no Mars reservoir of that size identified (about 1.4 x 10^5 ammonia bodies of 10^10 t each
by import). Capturing the entire solar wind and supplying its oxygen would add 1.9 m global-equivalent per year ([MWB] H1); all of Venus's hydrogen makes
0.043 m. Even there the source is a comet or ice-body problem, not a Mercury-Venus-Sun one.

**What would make the chain make sense** (none is available): a capture-and-store device for the wind with a yield above gram-per-year hardware; a protected
status for Mars's own ice (a choice outside the physics); or a goal at ocean scale with a transport rate no study supplies.

## 5. The setting these findings imply (constraints from all eleven files)

- **Work near a harvested world happens in the hottest place in the system.** Launch and receiving sites are heat sources, not places to stand; among
  collectors, shade and edge-on geometry are the working conditions (a black panel at Mercury's distance sits at 490 to 610 K); hardware degrades near the Sun (20%
  power loss in a simulated month).
- **What is dug first is silicate, not metal,** and the deeper workings meet melt, sulfur gas and a liquid metal core.
- **The world under the operation changes:** its spin can be broken by one-way launching; its sky fills with the debris of its own harvest; its neighbors' orbits move.
- **Venus is a place to live and make things, not to ship from;** a bared Venus is not livable either (58-day thermal swings, unshielded meteoroids, cracked ground).
- **Shipping is pulsed:** about two weeks of usable Mercury departures every 116 days; cheap ones once a year ([IMS]).
- **Dependence on elsewhere is structural:** electronics, magnets, dopants and lithium for collectors cannot come from Mercury or Venus; hydrogen and nitrogen are
  missing from Mercury.
- **Hydrogen cargo is hostile cargo:** cryogenic, lossy, expensive to refrigerate; ice and methane are easier.

## 6. Candidate handwaves raised at synthesis level

Flagged for the developer; none accepted. (The files' own candidates are entered in the register as C-96 to C-167.)

- **P-1.** Whole-planet disassembly of Mercury on any timescale of 1,000 years or less, without an off-planet processing architecture no source specifies.
- **P-2.** Any Venus disassembly, atmosphere removal on a human timescale, or a bared Venus as a livable surface.
- **P-3.** Oxygen, or hydrogen, imported to Mars from Mercury, Venus or the Sun at any scale, when Mars holds both locally at lower cost.
- **P-4.** A solar-wind or photospheric hydrogen supply at kilotonne-per-year scale or more.
- **P-5.** A planetary harvest with no consequence for neighboring orbits or for the harvested world's spin.

## 7. Source conflicts and errors carried

- Wikipedia's star-lifting energy figure is about 85 times too high (rejected by [OHM]); [PDL] counts the Bradbury "550,000 years" figure as twice too high.
- [MWI] and [PWH] give different multiples of binding energy for whole-planet processing (5 to 37 vs 11 to 99); different plant-energy assumptions.
- [BSU] resolves a [SYN] open thread (iron enrichment in the wind) and finds a 1.5-times flux-basis difference between this and earlier files.
- [BVE] flags VIP-INSPR's Table 2 air volumes as about 100 times too small; the report's conclusion survives only at 30 ppmv water, not at 5 to 6 ppmv.
- [MWB] notes the magnetic-shield simulations do not exist; the compact L1 magnet is infeasible on superconductor physics.
- [IMS] Section 8 (v-infinity understatement in the trucking file) remains uncorrected.

## 8. Open threads (selected; full lists in `DEFERRED_RESEARCH.md` Batches 16 to 26)

- Dyson 1966, Criswell 1985 and the published Armstrong and Sandberg paper were not opened; no end-to-end launcher efficiency including the pulsed-power chain.
- Venus solid-body removal (none); N-body study of Venus mass removal (none); a measured Mercury or Venus interior sample (none).
- Phobos and Deimos water (MMX returns in 2031); comet and Kuiper-belt ice inventories (blocked).
- A capture-and-store device for the solar wind; hydrogen carriers' hydride release temperatures; water electric thruster flown at high Isp.
- Comparison of all this with the interplanetary timeline has not been done.
