# Eclipse and Sun-angle statistics at Earth-Moon and Sun-Earth L4/L5, with thermal sizing (calculation file)

*Written 2026-10-11 by the orchestrator (not a research agent), in the section order of `_BRIEF.md`; §5.9 added the same evening after the companion file was read. This file answers the developer's
2026-10-11 point (waste-heat file §10.3, deferred item P3): what the thermal cycle of a station "grav-locked" at L4/L5 actually is, and what that
does to heat batteries, radiators and heat pumps. Companion file by a research agent: `lagrange_thermal_environment.md` (missions' thermal control,
L4/L5 stability and dust, heat-storage heritage, coatings). Every script and raw output is in `_calc/`. No figure is from recall: each input
is either opened this session (section 2), taken from a sibling research file with its source named, or marked ASSUMED.*

## 1. Scope

A point station at (a) Earth-Moon L4 and L5 and (b) Sun-Earth L4 and L5. Questions: how often and how long is the Sun hidden; how does the Sun's
direction move in the station's frame; what do those two facts do to a radiator, a heat pump and a heat battery. Not covered: Jovian and Saturnian
orbits and the heliocentric case in general (deferred item P2, except where §5.6 follows from the same geometry); libration orbits about the points;
radiation; station-keeping.

## 2. SEARCH LOG and sources opened (2026-10-11)

| # | String or page | Outcome |
|--:|---|---|
| S1 | `NASA eclipse web site lunar eclipse statistics 2001 to 2100 number of penumbral partial total lunar eclipses draconic month 27.2122 days nodes regression 18.6 years` | useful (leads). The search summary quoted counts and month lengths; **none was used from the summary**: counts were re-read on the page (F4), month lengths on the page (F5). |
| S2 | `NASA eclipse Moon orbit nodes regress 18.6 years draconic month 27.21222 days saros lunar eclipse cycles Espenak` | useful (leads to F5). |
| F1 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | opened: Moon volumetric mean radius 1737.4 km; semimajor axis 0.3844 x 10^6 km; perigee 0.3633, apogee 0.4055 x 10^6 km; revolution period 27.3217 d; synodic 29.53 d; inclination to ecliptic 5.145 deg; eccentricity 0.0549; geometric albedo 0.12. The sheet gives no nodal-regression period (**died at the source**). |
| F2 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | opened: equatorial radius 6378.137 km; solar irradiance 1361.0 W/m2; black-body temperature 254.0 K; Bond albedo 0.294; semimajor axis 149.598 x 10^6 km; perihelion 147.095, aphelion 152.100 x 10^6 km; sidereal orbit period 365.256 d. |
| F3 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | opened: Sun volumetric mean radius 695,700 km; mean Earth-Sun distance 149.6 x 10^6 km. |
| F4 | https://eclipse.gsfc.nasa.gov/LEcat5/LE2001-2100.html | opened: "During the 21st century CE, Earth will experience 228 lunar eclipses": penumbral 86, partial 57, total 85. Shadows computed "using Danjon's enlargement method"; **the page gives no enlargement percentage** (died at the source). |
| F5 | https://eclipse.gsfc.nasa.gov/SEsaros/SEperiodicity.html | opened: synodic month 29.530589 d; anomalistic 27.554550 d; draconic (node to node) 27.212221 d; the lunar nodes "regress westward by 19.3 degrees per year". |
| F6 | JPL Horizons API, https://ssd.jpl.nasa.gov/api/horizons.api (DE441), geocentric state vectors of the Moon (301) and Sun (10), ecliptic J2000, 10-minute steps, 2026-01-01 to 2064-01-01 | opened by script `_calc/horizons_fetch.py`: 1,998,577 rows per body. Earth-Moon distance 356,421 to 406,707 km; Sun distance 147,091,641 to 152,103,781 km. |
| — | Sibling files (read, not re-opened at source): `leo_and_orbital_habitats.md` (sigma 5.670374419e-8 W m-2 K-4, NIST CODATA 2022; ISS about 36 min of darkness in about 93 min); `waste_heat_utilization.md` (PCM 48.8 kJ/kg system level, hexadecane 235 kJ/kg, ice melt 333.44 kJ/kg, LiCl absorber 800 kJ/kg; ISS ammonia supply 275 K; ISS radiator 14.2 kg/m2 of planform); `robot_body_in_space.md` S33 (Li-ion cell specific energy 182 to 264 Wh/kg, NASA State-of-the-Art Small Spacecraft power chapter); `life_support_lowg_power_structures.md` (space solar cell output 229.2 W/m2 silicon, about 392-416 W/m2 triple junction, at the cell). | used by pointer |

**Dead ends:** no source for the lunar nodal-regression period or for a quantified Danjon enlargement was found on the pages opened (both F1 and F4 are
silent). Neither is needed: the regression rate is derived from two sourced periods (§5.1) and the enlargement is run as a sensitivity (§5.2).

## 3. Findings (sourced inputs and the published figures the model was tested against)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Radii and distances | R_E = 6378.137 km; R_S = 695,700 km; R_M = 1737.4 km; Earth-Sun 149.598 x 10^6 km; Earth-Moon mean 384,400 km | F1-F3 | Primary (agency fact sheets) | Horizons distances span 356,421-406,707 km (Moon) and 147.09-152.10 x 10^6 km (Sun), consistent with F1/F2 perigee-apogee | High |
| Lunar orbit | inclination 5.145 deg; sidereal 27.3217 d; draconic 27.212221 d; synodic 29.530589 d | F1, F5 | Primary | the simulation reproduces the synodic month (29.53064 d) and gives an eclipse year of 346.614 d | High |
| Node regression | derived: 2 pi / (n_sidereal - n_draconic) = 6,791.1 d = 18.593 yr (19.36 deg per year) | derived from F1, F5 | Derived | F5 states 19.3 deg per year; the textbook 18.61 yr differs by 0.1 percent because F1 gives the sidereal month to four decimals | High |
| Published lunar-eclipse count, 2001-2100 | 228 total: 86 penumbral, 57 partial, 85 total (so 142 reach the umbra) | F4 | Primary | model: §5.2 | High |
| Solar irradiance at 1 AU | 1361.0 W/m2 (mean); 1407.7 at perihelion (+3.4 %), 1316.6 at aphelion (-3.3 %) (derived from F2 distances, inverse square) | F2 | Primary | `_calc/lagrange_thermal_sizing_output_full.txt` §1 | High |

## 4. Conflicts and model limits

1. **Circular model against real ephemerides.** The circular-orbit model (`lagrange_eclipse.py`) and the Horizons run (`lagrange_eclipse_horizons.py`) agree
   on event rates within about 10 percent, but the real Earth-Moon distance varies by +/-6.5 percent (356,421-406,707 km against 384,400), which changes the
   shadow size and the Moon's angular size. **The extremes come from the real run:** longest Earth-shadow event 310 min (circular model 288), longest total
   event 170 min (164), deepest Moon transit 98.9 percent (94.7). Use the real-ephemeris figures for extremes and either for rates.
2. **Danjon enlargement.** NASA's catalog (F4) names the method and gives no percentage. The model is run with Earth's radius enlarged by 0, 1 and 2 percent
   (§5.2); a station is a point, so the atmosphere's enlargement of the umbra matters at the margin and is carried as a sensitivity, not a claim about which value
   NASA used.
3. **A real station librates.** The real L4/L5 are quasi-stable under the Sun's perturbation (sibling `moon_lagrange_and_comparables.md`); anything "at" L4/L5
   moves on an orbit about the point. The statistics below are for the instantaneous equilateral vertex. A libration orbit with enough out-of-plane amplitude would
   change which eclipses occur (§8, item 1).
4. **Time resolution.** The circular run steps 120 s; the real run steps 600 s, so durations in the real run are good to about 10 minutes and the deepest
   transit may be slightly underestimated.

## 5. Derived figures (arithmetic and results; scripts in `_calc/`)

### 5.1 Method (so the numbers can be reproduced)

Earth-centered ecliptic frame. Sun on the ecliptic at 149.598 x 10^6 km (circular model) or at its real, varying position (Horizons run). Moon on a circular
orbit of radius 384,400 km in a plane inclined 5.145 deg, argument of latitude advancing at 2 pi / 27.212221 d, node longitude regressing at
(2 pi / 27.3217 - 2 pi / 27.212221) = -0.000925207 rad/d. L4 and L5 are the same circle rotated +60 and -60 deg in the plane (equilateral triangle with Earth and Moon).
The Sun is a disc of angular radius asin(R_S / d); Earth and Moon are discs; the obscuration is the overlap area of the two discs divided by the Sun disc's area
(lens formula, `frac_obscured`). The station is a point. In the Horizons run L4/L5 are the geocentric Moon vector rotated +/-60 deg about the instantaneous orbit
normal (r x v), so the distance to Earth and to the Moon equals the real, varying Earth-Moon distance.

### 5.2 Validation: the same model applied to the Moon itself

Count lunar eclipses in the model and compare with F4 (228 per century, 142 reaching the umbra):

| Run | Earth radius enlargement | penumbral or deeper per century | umbral per century |
|---|---|--:|--:|
| NASA catalog 2001-2100 (F4) | Danjon (not quantified) | **228** | **142** |
| Circular model, 111.56 yr, 3 seeds | 0 % | 230.4 / 229.5 / 230.4 | 147.0 / 147.0 / 147.0 |
| | 1 % | 231.3 / 230.4 / 233.1 | 147.0 / 147.9 / 147.9 |
| | 2 % | 233.1 / 232.2 / 234.0 | 148.8 / 149.7 / 148.8 |
| Horizons DE441, 38.0 yr (85-86 and 53-55 events) | 0 % | 223.7 | 139.5 |
| | 1 % | 226.3 | 142.1 |
| | 2 % | 226.3 | 144.7 |

The circular model is 1-3 percent high on all lunar eclipses and 3-5 percent high on umbral ones; the real-ephemeris run at 1 percent enlargement reproduces
F4 (226.3 against 228; 142.1 against 142). The method is sound; the circular model is a fair approximation for rates.

### 5.3 Geometry check in closed form (`lagrange_geometry.py`)

- Earth's umbra length = R_E D / (R_S - R_E) = 6378.137 x 149.598 x 10^6 / (695,700 - 6378.137) = 1,384,196 km.
- At 384,400 km: umbra radius = 6378.137 - 384,400 x (695,700 - 6378.137) / 149.598 x 10^6 = 4,607 km; penumbra radius = 6378.137 + 384,400 x (695,700 + 6378.137) / 149.598 x 10^6 = 8,182 km.
- Station speed = 2 pi x 384,400 / (27.3217 x 86,400 s) = 1.0232 km/s; the shadow axis moves with the Sun at 0.0765 km/s at that distance; relative speed 0.9466 km/s.
- Central chord: umbra 2 x 4,607 / 0.9466 = 9,734 s = **162 min**; penumbra 2 x 8,182 / 0.9466 = 17,287 s = **288 min**. The simulation gives 164 and 288 (circular model maxima).
- Angular radii seen from L4/L5: Sun 0.2665 deg, Earth 0.9507 deg, Moon 0.2590 deg. Moon-to-Sun disc-area ratio (0.2590 / 0.2665)^2 = 0.945: a mean-distance Moon cannot cover the Sun. The Moon's angular radius equals the Sun's at R_M D_sun / R_S = 1737.4 x 149.598 x 10^6 / 695,700 = **373,597 km**; the real Earth-Moon distance is below that 30.2 percent of the time, so a **total** occultation of the Sun by the Moon is geometrically possible from L4/L5 near perigee.
- At the real apogee distance (406,707 km) the same formulas give a penumbra radius of 8,288 km and an umbra radius of 4,502 km; with a relative speed of about 0.885 km/s that is about 312 and 170 minutes, which is what the Horizons run found (310 and 170).

### 5.4 Result: Earth-Moon L4 and L5 (the headline table)

Events per year, durations, and the fraction of time the Sun is (partly) hidden. "Any" means any part of the Sun's disc covered; "total" means the whole disc.
Circular model: 111.56 years x 3 seeds, 120 s steps (L4 in the first column, L5 in brackets; they differ by less than 1 percent). Horizons: 38.0 years, 600 s steps.

| Quantity | Circular model, L4 (L5) | Horizons DE441, L4 | Horizons DE441, L5 |
|---|---|---|---|
| Earth-shadow events, any obscuration, per year | 1.89 (1.89) | 1.90 | 1.76 |
| of which total (whole Sun hidden), per year | 1.07 (1.06) | 1.13 | 1.03 |
| Duration, any: mean / median / 90th percentile / longest (min) | 226 / 248 / 286 / 288 | 231 / 250 / 289 / 310 | 236 / 250 / 300 / 310 |
| Duration, total: mean / median / longest (min) | 127 / 141 / 164 | 125 / 130 / 170 | 125 / 140 / 170 |
| Moon-transit events, any obscuration, per year | 0.81 (0.80) | 0.71 | 0.76 |
| Moon transit duration: mean / longest (min) | 98 / 126 | 106 / 140 | 95 / 140 |
| Deepest Moon transit (fraction of the Sun's disc covered) | 0.947 | 0.989 | 0.902 |
| Either body, any obscuration, events per year | 2.70 (2.69) | 2.61 | 2.53 |
| Fraction of time with any obscuration | 0.0961 % (0.0958 %) | 0.0975 % | 0.0930 % |
| Fraction of time with the whole Sun hidden | 0.0258 % (0.0258 %) | 0.0270 % | 0.0244 % |
| Mean fraction of sunlight lost (time-average) | 0.0531 % (0.0529 %) | 0.0568 % | 0.0533 % |
| Median gap between consecutive Earth-shadow events (days) | 177 | — | — |
| Longest gap between consecutive events: any / total (days) | 325 / 856 | — | — |

**What the table means.** Eclipses at the Earth-Moon equilateral points are **two seasons a year** (median gap 177 days, close to half the 346.6-day eclipse year), each
season holding about one Earth-shadow event and some of the Moon's. The station is in full sunlight 99.9 percent of the time. The longest total loss is 170 minutes
(2.8 hours); the longest partial dimming is about 310 minutes (5.2 hours); about a third of a year can pass between events, and total events can be separated by
more than two years (856 days in the circular run).

### 5.5 Result: the Sun's direction in the station's frame (Earth-Moon L4/L5)

- A station fixed in the rotating frame of the Earth-Moon line sees the Sun's azimuth sweep 360 deg in one synodic month (29.530589 d): 360 / 29.530589 = **12.19 deg per day**, retrograde.
- The Sun's elevation above the lunar orbit plane stays within the orbit's inclination: **maximum 5.158 deg** (circular model), 5.066 deg (Horizons, 38 yr); mean absolute elevation 3.27 deg (circular) and 3.20 deg (Horizons). It oscillates with the eclipse year (346.614 d in the model).
- Consequence for surfaces: a radiator whose normal lies along the orbit normal sees the Sun at an incidence cosine of at most sin(5.158 deg) = **0.0899**, mean sin(3.274 deg) = 0.0571. At an ASSUMED absorptance of 0.25 that is a solar load of 30.6 W/m2 at worst (19.4 W/m2 on average) against 188 to 1,234 W/m2 radiated between 250 and 400 K (§5.7). A one-axis solar array turning once per 29.53 days loses cos(5.158 deg) = 0.9960, i.e. **0.40 percent**.
- There is **no day and night**: the Sun is never behind a body except in the events above. The only thermal cycle is the Sun's slow sweep around the station in 29.53 days, which a station with sun-tracking arrays and normal-to-the-orbit-plane radiators does not feel.

### 5.6 Result: Sun-Earth L4 and L5

- The Sun, Earth and L4/L5 form an equilateral triangle, so the Sun-to-Earth angular separation seen from the point is **60 deg**. Earth's angular radius from there is asin(6378.137 / 149.598 x 10^6) = 0.00244 deg, the Moon's 0.00067 deg, the Sun's 0.2665 deg. Occultation would need a separation under 0.2689 deg: the margin is a factor of 223. **No eclipse by Earth or Moon is geometrically possible.** Earth's umbra ends 1,384,196 km behind Earth (0.93 percent of the Earth-Sun distance).
- A station fixed in the corotating Sun-Earth frame sees the Sun in a **fixed direction** (the frame turns once a year); its elevation above the ecliptic is that of the point's orbit (about zero for the nominal point).
- Solar flux follows the point's distance from the Sun, which follows Earth's orbit: 1,316.6 to 1,407.7 W/m2 (§3). There is no periodic dark interval of any length. This is also the answer to the heliocentric caveat in the waste-heat file §10.2 for this case: **a heat battery has no cycle to carry the station through.**
- Mercury or Venus crossing the Sun's disc as seen from the point would hide only a tiny fraction of it; that is not an eclipse in any thermal sense. **Not computed:** the planets' radii and distances were not opened this session.

### 5.7 Thermal sizing at L4/L5 (`lagrange_thermal_sizing.py`; sink 3 K neglected, (3/300)^4 = 1e-8)

Earth and Moon add **under 0.3 W/m2 in total** (Earth thermal 0.0650 W/m2, Earth reflected at most 0.1102, Moon reflected at most 0.0033, Moon thermal at most 0.0297 at an ASSUMED 400 K everywhere) against 1,361 W/m2 from the Sun: the sink is deep space plus the Sun.

**Equilibrium temperature of an isothermal body in sunlight** (T = (alpha S / (k eps sigma))^0.25, k = 1 one face, 2 both faces, 4 sphere; S = 1361.0 W/m2):

| alpha / eps | one face to the Sun | both faces | sphere |
|--:|--:|--:|--:|
| 0.10 | 221.3 K | 186.1 K | 156.5 K |
| 0.25 | 278.3 K | 234.0 K | 196.8 K |
| 0.50 | 331.0 K | 278.3 K | 234.0 K |
| 1.00 | 393.6 K | 331.0 K | 278.3 K |

**Radiator area per kW rejected** (one radiating face, emissivity 0.85 ASSUMED; absorptance 0.25 ASSUMED for the worst-Sun column):

| T (K) | flux (W/m2) | area, edge-on to the Sun (m2/kW) | area, Sun at the worst incidence (m2/kW) |
|--:|--:|--:|--:|
| 250 | 188.3 | 5.311 | 6.342 |
| 275 | 275.7 | 3.628 | 4.081 |
| 300 | 390.4 | 2.561 | 2.779 |
| 320 | 505.4 | 1.979 | 2.106 |
| 350 | 723.3 | 1.383 | 1.444 |
| 375 | 953.1 | 1.049 | 1.084 |
| 400 | 1,233.9 | 0.810 | 0.831 |

Scale linearly with power: 100 kW at 300 K needs about 256 m2 (278 m2 at the worst Sun). The coating values are to be replaced by the sourced ones in `lagrange_thermal_environment.md`.

**Heat pump** (lift a load at 275 K, the ISS ammonia supply, to a hotter radiator; f = fraction of Carnot COP; baseline rejects directly at 300 K; sink 0 K):

| T_radiator | f | COP | heat rejected per kW of load | radiator area (m2/kW) | area saved vs 300 K | compressor work | solar-array area to supply it at 229.2 / 300 / 416 W/m2 |
|--:|--:|--:|--:|--:|--:|--:|---|
| 320 K | 0.50 | 3.06 | 1.33 kW | 2.626 | -0.065 m2 | 327 W | 1.43 / 1.09 / 0.79 m2 |
| 360 K | 0.38 | 1.23 | 1.81 kW | 2.240 | +0.321 m2 | 813 W | 3.55 / 2.71 / 1.96 m2 |
| 360 K | 0.50 | 1.62 | 1.62 kW | 1.999 | +0.563 m2 | 618 W | 2.70 / 2.06 / 1.49 m2 |
| 360 K | 0.60 | 1.94 | 1.52 kW | 1.872 | +0.690 m2 | 515 W | 2.25 / 1.72 / 1.24 m2 |
| 400 K | 0.50 | 1.10 | 1.91 kW | 1.547 | +1.014 m2 | 909 W | 3.97 / 3.03 / 2.19 m2 |

**At L4/L5 a heat pump saves 0 to 1.1 m2 of radiator per kW of load and costs 0.7 to 5.2 m2 of extra solar array to power it.** The array grows more than the radiator
shrinks at every point in the table (assumptions: f, the load temperature, the array output per m2). The benefit the waste-heat file found for a hot lunar sink does not
carry over: against a cold sink the radiator is already efficient, so a heat pump here is justified only if radiator area or mass is the binding constraint and array
area is not. (Mass comparison needs sourced areal masses; see the companion file.)

**Storing heat or electricity through the longest events** (per kW carried; masses are the storage medium only, before tanks, pumps or packaging unless stated):

| Medium (specific energy, source) | 164 min (2.733 kWh) | 288-310 min (4.80 kWh at 288) |
|---|--:|--:|
| PCM at system level, 48.8 kJ/kg = 13.6 Wh/kg (sibling E1) | 201.6 kg | 354.1 kg |
| n-hexadecane before packaging, 235 kJ/kg = 65.3 Wh/kg | 41.9 kg | 73.5 kg |
| Melting ice before tank, 333.44 kJ/kg = 92.6 Wh/kg | 29.5 kg | 51.8 kg |
| LiCl absorber concept, 800 kJ/kg = 222.2 Wh/kg | 12.3 kg | 21.6 kg |
| Li-ion cell, 182 Wh/kg (sibling S33) | 15.0 kg | 26.4 kg |
| Li-ion cell, 264 Wh/kg (sibling S33) | 10.4 kg | 18.2 kg |

Battery masses are cell level only: the pack, management and radiator add to them (revised against a flown pack in §5.9). **Read:** to carry a load through a 2.8-hour total eclipse, a battery cell is 13 to 19
times lighter per kWh than system-level paraffin PCM (about 5.6 times at the level of a flown ISS battery unit, §5.9), and a lithium-chloride absorber is comparable to a battery. A heat battery's real advantages are different ones: it is
charged from waste heat that must be rejected anyway (no array needed), and its cycle life is not an issue at one to three cycles a year.

**Dark time and cycles against the ISS orbit:** ISS dark fraction 36 / 93 = 38.7 percent, with 365.25 x 1440 / 93 = 5,655 dark periods a year (sibling figures). At Earth-Moon
L4/L5 the whole-Sun-hidden fraction is 0.0244 to 0.0270 percent: **about 1,400 to 1,600 times less dark time** (38.7 / 0.0270 = 1,433; 38.7 / 0.0244 = 1,586), and about 1.1 total events a year: **about 5,000 times fewer
battery cycles** (5,655 / 1.067 = 5,300 against the circular model; 5,655 / 1.132 = 4,996 against Horizons L4).

### 5.8 Answers to the four questions in waste-heat file §10.3

1. *Does a station at L4/L5 have intervals with no sunlight?* Earth-Moon: yes but rare and short: about 1.1 total events a year of at most 170 minutes (2.8 hours), about 2.6
   events a year of any dimming, the longest about 310 minutes. Sun-Earth: none, for any duration.
2. *Is the thermal cycle monthly?* The Sun's direction sweeps once per 29.53 days in the Earth-Moon frame, within 5.2 deg of the orbit plane. It is a **slow change of incidence,
   not a dark interval**; it needs no storage if radiators face the orbit normal and arrays track on one axis. The 354 h lunar-night figures are not the right comparison:
   the longest dark interval is about 125 times shorter than 354 hours (354 / 2.83 = 125; 354 / 5.17 = 68 against the longest partial event).
3. *Steady sunlight changes the problem into continuous rejection.* Yes: §5.7. Every watt consumed is a watt radiated; the radiator must be sized for the continuous load.
4. *Uses that need no cycle.* The ones in the waste-heat file §10.1 rows 1, 4, 5 and 2 remain; §5.7 shows row 2 (heat pump) does not pay in area at L4/L5.

### 5.9 Cross-check against the published figures in the companion file (`lagrange_thermal_environment.md`, read 2026-10-11 after §5.1-5.8 were written)

**Lunar-eclipse analog (NASA TP-2009-214173, via the companion file §3B):** longest totality about 99.8 min, longest partial about 210 min, longest purely penumbral about 296.5 min. The same shadow geometry with the Moon's disc (radius 1737.4 km) gives, at the mean distance and relative speed 0.9466 km/s (§5.3): totality 2 x (4,607 - 1,737.4) / 0.9466 = 6,063 s = **101 min**; partial (first to last umbral contact) 2 x (4,607 + 1,737.4) / 0.9466 = 13,405 s = **223 min**. Against 99.8 and 210 that is 1.3 and 6 percent high, as expected for a catalog maximum taken over 5,000 years with a Danjon-enlarged shadow. A purely penumbral pass that just misses the umbra has half-chord sqrt((8,182 + 1,737.4)^2 - (4,607 + 1,737.4)^2) = 7,625 km, i.e. 2 x 7,625 / 0.9466 = 269 min at the mean distance, near the catalog's 296.5 at larger Moon distance. So the point-station maxima in §5.4 (170 min total, 310 any) are what the Moon's own catalog implies once the Moon's radius is removed from the chord. **Consistent.**

**"Rare and brief" (an O'Neill-era appendix, companion file §3B):** consistent with about 1.1 total eclipses a year of at most 2.8 hours; it carries no number to compare.

**Conflict: Richichi et al. 2024, MNRAS 527, 6616 (companion file §3B):** a side remark that from an L4 orbit "a total solar eclipse ... should occur only once or very few times per month and last of order of a few hours". It names no occulting body and no analysis, and the companion file rates it low-medium. This calculation gives **0.7 to 0.8 Moon-transit events a year** (at most 0.989 of the Sun's disc) and **1.0 to 1.1 Earth total eclipses a year** for the equilateral point: more than ten times fewer than "once a month". Why they can differ: (i) the Sun must lie within about 0.5 degrees of the orbit plane at the moment of alignment, which happens only in the two eclipse seasons; (ii) the remark may concern an orbit about L4 rather than the point, which swings the station tens of thousands of miles through the geometry (next item). The two are **not reconciled**; the remark is a side comment and the calculation shows its arithmetic, but a libration-orbit run (§8 item 1) is what would settle it.

**The point is not where a station can be.** Kamel (NASA CR-1622, 1970; companion file §3B) finds that, with the Sun's perturbation, the points themselves are not usable and the stable motion is on **large one-month elliptic orbits synchronized with the Sun**: semimajor axes of about 60,000 mi (96,561 km), 88,000 mi (141,622 km) and 90,000 mi (144,841 km) in different analyses. Heppenheimer puts the colony orbit about 90,000 miles from the libration point. A "grav-locked" L4/L5 station therefore circles the point once a month on an orbit 100,000 to 145,000 km across, and no annual station-keeping delta-v was found in any source (companion file open threads). **The statistics in §5.4 describe the point, not that orbit.**

**Missions avoid eclipses at a price (companion file §3A):** JWST's orbit "avoids Earth and Moon eclipses of the Sun, ensuring continuous electrical power"; Gaia spent 14 m/s on an eclipse-avoidance maneuver and notes "small (percent level) partial eclipses by the Moon typically occur once per year" (a different geometry, at Sun-Earth L2; the Moon's partial eclipse there is small, whereas at Earth-Moon L4/L5 the Moon covers up to 0.95-0.99 of the Sun); Planck's orbit change cost 50.6 to 75.7 m/s and still crossed 1 to 2 Earth and 4 to 11 Moon eclipses. LRO sat through a 151-minute lunar eclipse by **pre-heating its own structure** (storing heater power in the spacecraft's thermal mass) and by a battery sized to 70 percent depth of discharge, with more than 100 percent margin: the flown alternative to a heat battery is the station's own thermal mass.

**Sourced values to replace the assumed ones in §5.7 (companion file §3F, §3E, §3G):**
- Coatings (beginning of life, absorptance alpha / emittance epsilon): quartz OSR 0.05-0.08 / 0.80; silvered Teflon 5 mil 0.05-0.09 / 0.78 (0.08 / 0.81 in a second table); Z-93 white paint 0.17-0.20 / 0.92; S13G-LO 0.20-0.25 / 0.85. **End of life:** absorptance rises with little change in emittance; a white paint "may rise from around 0.20 to 0.70 in just a few years"; quartz mirrors take essentially no damage; no free-space 1 AU end-of-life figure was found.
- Solar load on a radiator face at the worst incidence found (cosine 0.0899, S = 1361.0 W/m2: 122.4 W/m2 normal-equivalent): quartz OSR (0.065) **8.0 W/m2**; white paint at beginning of life (0.20) **24.5 W/m2**; white paint at end of life (0.70) **85.7 W/m2**. Against the flux one face sheds at 300 K (epsilon 0.80: 367 W/m2; 0.85: 390 W/m2): 2.2, 6.3 and 22 percent. So **a low-absorptance mirror coating makes the Sun's sweep irrelevant; an aged white paint does not**, unless the radiator is oversized for end of life, which the handbook says is standard practice.
- Radiator areal mass (design studies, not flown): 5.24 to 12.76 kg/m2 (heat-pipe radiators in reactor-system designs); the flown ISS figure is 14.2 kg/m2 of planform (sibling). Radiator mass per kW at 300 K (edge-on, §5.7: 2.561 m2/kW, mass basis assumed per radiating m2): 2.561 x 5.24 to 12.76 = **13 to 33 kg/kW** (design studies) and 2.561 x 14.2 = 36 kg/kW (ISS planform figure, if planform equals radiating area).
- Battery: the ISS lithium-ion unit stores about 15 kWh in a 435 lb (197.3 kg) unit = **76 Wh/kg at flown-unit level** (142 Wh/kg implied at cell level, companion file D5; the 15 kWh is a rounded slide figure). Carrying 1 kW through the longest total eclipse found (2.733 kWh) at 76 Wh/kg is 2,733 / 76 = **36 kg/kW**, through 288 minutes (4.8 kWh) **63 kg/kW**. System-level paraffin PCM (13.6 Wh/kg): 201.6 and 354 kg/kW; ratio 201.6 / 36.0 = **5.6** (not 13 to 19, which compared a cell with a system). A battery life test for geostationary eclipse seasons showed "no degradation in 20 degrees C capacity after 20 seasons" (44-day seasons, one discharge a day, up to 75 percent depth); at 1 to 3 eclipses a year cycle life is not the constraint it is in low orbit.
- Solar flux: the companion file's ECSS-based perihelion and aphelion figures (1,412.9 and 1,321.6 W/m2) sit on the older radiometer scale; the NASA-sheet-derived 1,407.7 and 1,316.6 used here are on the 1361.0 scale (companion file conflict C4). Same 6.9 percent swing.

**Corrections this implies for the earlier sections:** (a) §5.7's "13 to 19 times lighter" holds for a cell and is 5.6 for a flown unit; (b) the radiator table's ASSUMED emissivity 0.85 and absorptance 0.25 bracket the sourced white-paint and mirror values (absorptance 0.05 to 0.28 at the start of life), but an end-of-life white paint at 0.70 is outside the 0.25 bracket and is handled above.

### 5.10 The Sun-forced orbit that replaces the point, and eclipses along it (`_calc/lagrange_bcp_orbit.py`, `lagrange_bcp_search.py`, `lagrange_bcp_eclipse.py`)

**Method.** Planar bicircular model (equations in the script docstring: Earth, Moon and Sun as point masses on circular orbits in the Earth-Moon rotating frame, the barycenter's acceleration toward the Sun as the indirect term). Inputs: masses Earth 5.9722, Moon 0.07346 and Sun 1,988,400 x 10^24 kg (NASA fact sheets, F2-F4 and the Sun sheet mass row opened this session); mu = 0.0121509; Sun mass in Earth-Moon units 328,897; Sun distance 389.173 lunar distances; the Sun's angular rate in the rotating frame w_S = 27.3217 / 365.256 - 1 = -0.925198 per unit, so the forcing has the synodic period 29.5306 d. The orbit is the solution of period one synodic month found by Newton shooting (residual under 2e-14), with stability from the monodromy matrix (central differences). The in-plane orbit is then embedded in the inclined lunar plane and run through the same eclipse geometry as §5.4 (111.56 yr, 120 s steps). **Check on the equations:** they were derived, not copied from a source, so the only independent check is that the shooting found stable orbits of the size class the literature reports (above) and an unstable point where the literature says the points are unusable. **Limits:** the dynamics are planar (the Sun's out-of-plane offset and the Moon's eccentricity are in the eclipse geometry only for the Moon's plane and distance, not in the equations of motion); no solar radiation pressure; the model's step sizes and Newton convergence were checked only by the residuals shown.

**Finding 1: the exact point is not a place a station can stay.** The orbit that replaces L4/L5 under the Sun's forcing is small (mean 3,838 km, at most 6,690 km from the equilateral point; Earth distance 379,678 to 386,933 km) and is **linearly unstable**: monodromy eigenvalue magnitudes 1.0, 1.0, **1.097321**, 0.91131, so any error grows by 9.7 percent per synodic month, an e-folding time of 29.5306 / ln(1.097321) = 29.5306 / 0.09287 = **318 days (0.87 yr)**. Numerically, a start displaced by 1,000 km from this orbit had drifted to 236,197 km (L4) and 251,341 km (L5) from the point within about five years (60 periods). This agrees in kind with the literature found by the companion file: "the exact points are not usable" (Kamel, 1970).

**Finding 2: the stable motion is on large one-month orbits.** Starting the shooting from rings of guesses 0.05 to 0.40 lunar distances from the point found two more periodic orbits of the same period, **both with all eigenvalue magnitudes equal to 1.000000 (linearly stable)**:

| Orbit | Mean / maximum distance from the point | Earth distance | Moon distance |
|---|--:|--:|--:|
| Small forced orbit (unstable) | 3,838 / 6,690 km | 379,678 to 386,933 km | 377,989 to 389,815 km |
| Large orbit A (stable) | 100,293 / 152,922 km | 318,887 to 443,680 km | 284,342 to 514,988 km |
| Large orbit B (stable) | 103,893 / 159,193 km | 316,642 to 445,891 km | 281,459 to 520,129 km |

The large orbits are the same size class as the one-month orbits in the literature (semimajor axes of 60,000 to 90,000 miles = 96,561 to 144,841 km, companion file §3B). **Whether these are the same orbits was not verified**: the source abstract's own numbers are lost to OCR. The L5 search gives the mirror images (same sizes, same eigenvalues).

**Finding 3: eclipse statistics along these orbits (per year, 111.56-yr run, L4; L5 within 3 percent):**

| Quantity | Point (§5.4 circular) | Small forced orbit | Large orbit A | Large orbit B |
|---|--:|--:|--:|--:|
| Earth-shadow events per year, any / total | 1.89 / 1.07 | 1.88 / 1.07 | 1.69 / 0.86 | **2.21 / 1.37** |
| Longest Earth-shadow event, any / total (min) | 288 / 164 | 286 / 162 | **352 / 182** | 230 / 144 |
| Moon-transit events per year, any | 0.81 | 0.81 | 0.72 | 0.95 |
| Moon covers at least 90 percent of the Sun, per year | — | 0.054 | 0 | 0.22 (longest 26 min) |
| Moon covers the whole Sun, per year | 0 | 0 | 0 | **0.125 (about once in 8 years; longest 16 min)** |
| Deepest Moon transit | 0.947 | 0.945 | 0.538 | 1.000 |
| Either body, any dimming, per year | 2.70 | 2.69 | 2.40 | **3.16** |
| Whole Sun hidden: events per year / longest (min) | 1.07 / 164 | 1.07 / 162 | 0.86 / 182 | 1.50 / 144 |
| Fraction of time with the whole Sun hidden | 0.0258 % | 0.0256 % | 0.0232 % | 0.0296 % |
| Fraction of time with any dimming | 0.0961 % | 0.0954 % | 0.1021 % | 0.0910 % |
| Longest gap between events, any / whole-Sun (days) | 325 / 856 | 325 / 856 | 502 / 1,034 | 177 / 679 |

**Read.** Moving the station from the point to a stable large orbit changes the eclipse picture by tens of percent, not by orders of magnitude: about **1 to 1.5 whole-Sun-hidden events a year, each at most 3 hours (182 minutes), and 2.4 to 3.2 dimming events a year, the longest about 5.9 hours (352 minutes)**. Orbit B adds a **total solar eclipse by the Moon about once in eight years** (up to 16 minutes). The "once or very few times per month" remark (§5.9) is **not reproduced** by any of these orbits: the highest dimming rate found is 3.2 a year. The remark is therefore either about a different orbit family (the companion file notes 3:1 resonant axial orbits and large vertical amplitudes in the literature) or loose; this stays an open conflict, now bracketed by an actual orbit calculation.

**Limits of finding 3.** The embedding takes the Sun's phase from a circular Moon and a uniform Sun; the orbits' stability is linear stability in a planar circular model, not a statement about a real station with eccentricity, inclination and radiation pressure; no station-keeping cost can be read from it.

## 6. Constraints for any inhabitant

- **Earth-Moon L4/L5 (§5.4):** plan for about 1.1 full eclipses a year, each at most 2.8 hours, and about 2.6 dimming events a year, the longest about 5.2 hours; they cluster in two seasons six months apart, and a quiet stretch of 325 days (or, for full eclipses, more than two years) can occur.
- **Sun-Earth L4/L5 (§5.6):** none; solar flux varies +3.4 / -3.3 percent with the point's distance from the Sun over the year.
- **Thermal environment (§5.7):** the heat sink is deep space; Earth and Moon add under 0.3 W/m2. Radiators should face the orbit normal (Earth-Moon points) so the Sun's incidence stays within 5.2 deg of edge-on.
- **No heat battery earns its mass here** on the cycle length found; a battery or a larger electrical store covers the rare eclipse more cheaply (§5.7). **Waste heat is rejected, not stored.**
- **Electricity from waste heat and heat pumps for area savings** do not pay against a cold sink (§5.7 and waste-heat file §3A).
- **A station "at" Earth-Moon L4/L5 cannot sit at the point** (§5.10): the Sun-forced orbit there is unstable with an e-folding time of about 318 days. The stable motion is on a one-month orbit about 100,000 km (mean) from the point, 153,000 to 159,000 km at most, with a Moon distance of 281,000 to 520,000 km. Its eclipses differ from the point's by tens of percent (§5.10); its station-keeping cost under real perturbations is unpublished and not computed.
- **Radiator coatings age:** a white-paint radiator's absorptance can rise from 0.20 to 0.70 in a few years; a mirror coating does not (§5.9). Size for end of life or choose the mirror.
- **Spacecraft thermal mass is a flown eclipse store** (LRO pre-heated its avionics before a 151-minute eclipse) (§5.9).

## 7. Candidate handwaves

None. Everything here follows from orbital mechanics and radiation. A station that is truly "grav-locked" at L4/L5 with no station-keeping is **not** a handwave of this file's physics, but
it is a claim about orbital dynamics (quasi-stable, perturbed by the Sun) that the companion file quantifies; do not assume zero station-keeping.

## 8. Open threads

1. **Libration orbits: done for the planar bicircular model (§5.10); still open:** the same with the Moon's eccentricity and inclination in the dynamics (a full ephemeris-driven integration), solar radiation pressure, the station-keeping cost of staying on a large orbit or holding the unstable small one (the e-folding time is 318 days; the cost depends on the error budget, not computed), the orbit families with vertical amplitude or 3:1 resonance named in the literature, and whether any orbit avoids Earth eclipses (an out-of-plane amplitude above the penumbra radius, about 8,200 km, would). An out-of-plane amplitude larger than the penumbra radius (about 8,200 km at mean distance) could avoid Earth eclipses altogether; unverified.
2. **Full Moon occultation.** The real Earth-Moon distance is below 373,597 km 30 percent of the time, so a total occultation of the Sun by the Moon is possible from L4/L5; the deepest event in 38 years sampled at 10 minutes reached 0.989. A one-minute ephemeris would settle whether any reaches 1.0.
3. **Sun-Earth L4/L5 with real orbital elements.** This file treats the points as the equilateral vertex; an Earth trojan's orbit (e.g., asteroid 2010 TK7) has finite inclination and libration; see the companion file for the published parameters.
4. **Published eclipse numbers for libration orbits.** The companion file found only qualitative statements ("rare and brief") and one unreconciled side remark (§5.9); He et al. 2026 (Springer) and the 2024 Acta Astronautica paper on 3:1 resonant axial orbits likely hold numbers and were paywalled or returned 403. A library copy or the authors' preprints would settle the conflict in §5.9.
5. **Heat-pump mass trade.** Sourced radiator areal mass (the ISS figure is 14.2 kg/m2 of planform) against array areal mass; not done here because the array mass is not sourced.
6. **Items P2 of the deferred list** (eclipse and shade statistics at Mars, Jupiter, Saturn and the Moon; storage at those bodies) are untouched; the same scripts can be pointed at a circular orbit about any body with its radius, GM and the Sun's elevation.

## 9. Rejected sources

- The search summaries in S1 and S2 as sources for any number: used only to find pages; every number used was read on the page (F4, F5) or computed.
- Any recalled value for the nodal-regression period or the Danjon percentage: replaced by the derivation in §3 and the sensitivity in §5.2.

## Files in `_calc/`

`lagrange_eclipse.py` (circular model and validation) · `horizons_fetch.py` and `lagrange_eclipse_horizons.py` (real-ephemeris run) · `lagrange_geometry.py` (closed form) · `lagrange_moon_events.py` (depth of Moon transits) · `lagrange_thermal_sizing.py` (radiators, heat pump, storage, planetary loads) · `lagrange_bcp_orbit.py`, `lagrange_bcp_search.py`, `lagrange_bcp_eclipse.py` (the Sun-forced orbit about L4/L5, §5.10; orbit files `bcp_orbits_L4.json`, `bcp_orbits_L5.json`) · and their raw outputs: `lagrange_eclipse_validate_output.txt`, `lagrange_eclipse_l45_output.txt`, `lagrange_eclipse_horizons_output.txt`, `lagrange_geometry_output.txt`, `lagrange_moon_events_output.txt`, `lagrange_thermal_sizing_output_full.txt` (`lagrange_thermal_sizing_output.txt` is the earlier run without §7), `lagrange_bcp_orbit_output.txt`, `lagrange_bcp_search_output.txt` (L4, first run) / `lagrange_bcp_search_L4_output.txt` / `lagrange_bcp_search_L5_output.txt`, `lagrange_bcp_eclipse_output_run2.txt` (`lagrange_bcp_eclipse_output.txt` holds the first, failed run's traceback: the spline needed a closed orbit). The 190 MB Horizons cache is not kept; `horizons_fetch.py 2026 38 <dir>` rebuilds it. Run every script with `python3 -I`.
