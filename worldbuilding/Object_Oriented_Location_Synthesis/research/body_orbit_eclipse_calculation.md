# Eclipse and sunlight statistics for circular orbits about the Moon, Mars, Jupiter and Saturn (calculation file)

*Written 2026-10-11 by the orchestrator (not a research agent), in the section order of `_BRIEF.md`. Answers deferred item P2 (heat batteries for
stations in orbit around the Sun, Moon, Mars, Jupiter and Saturn: eclipse and shade statistics per body, the heliocentric case) and feeds the heat-battery
comparison. Sibling: `lagrange_eclipse_calculation.md` (L4/L5). Scripts and raw outputs in `_calc/`. No figure is from recall: inputs are opened
this session (section 2), taken from a named sibling file, or marked ASSUMED.*

## 1. Scope

Circular, equatorial orbits about the Moon, Mars, Jupiter and Saturn at the radii in §5, plus a heliocentric orbit. Questions: how long and how often is the Sun
hidden; what that means for storing heat or electricity; how much sunlight there is. Not covered: polar or inclined orbits, eccentric orbits, orbits about moons
of Jupiter and Saturn (Ganymede, Titan, Enceladus), Saturn's ring shadows and ring-plane hazards, radiation (sibling files hold the doses), stability of a given radius.

## 2. SEARCH LOG and sources opened (2026-10-11)

| # | String or page | Outcome |
|--:|---|---|
| S1 | `geostationary satellite eclipse season 44 days around equinox maximum eclipse duration 72 minutes` | useful (leads). Summary figures were not used; the NOAA page was opened (F7). |
| F1 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html | opened: volumetric mean radius 3389.5 km, equatorial radius 3396.2 km; GM 0.042828 x 10^6 km3/s2; sidereal rotation 24.6229 h; obliquity to orbit 25.19 deg; sidereal orbit period 686.980 d; solar irradiance 586.2 W/m2. |
| F2 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html | opened: mass 1898.13 x 10^24 kg; equatorial radius (1 bar) 71,492 km; sidereal rotation 9.9250 h; obliquity 3.13 deg; orbit period 4332.589 d; solar irradiance 50.26 W/m2. |
| F3 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html | opened: mass 568.32 x 10^24 kg; equatorial radius (1 bar) 60,268 km; sidereal rotation 10.656 h; obliquity 26.73 deg; orbit period 10,755.699 d; solar irradiance 14.82 W/m2. |
| F4 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | opened (also in the L4/L5 file): mass 0.07346 x 10^24 kg; volumetric mean radius 1737.4 km; sidereal rotation 655.720 h; obliquity to orbit 6.68 deg; inclination to ecliptic 5.145 deg. |
| F5 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | opened: equatorial radius 6378.137 km; GM 0.39860 x 10^6 km3/s2; sidereal rotation 23.9345 h; obliquity to orbit 23.44 deg; sidereal year 365.256 d; irradiance 1361.0 W/m2. |
| F6 | https://physics.nist.gov/cgi-bin/cuu/Value?bg | opened: G = 6.674 30 x 10^-11 m3 kg-1 s-2, standard uncertainty 0.000 15 x 10^-11, 2022 CODATA. |
| F7 | https://www.nesdis.noaa.gov/our-satellites/currently-flying/goes-east-west/goes-eclipse-schedule | opened: "spacecraft must use batteries up to 72 minutes each day"; eclipses "approximately from late February to mid-April, and from late August to mid-October"; stray-light contamination "for approximately 45 days before and after the vernal and autumnal equinox". |
| — | Sibling files by pointer: sigma (NIST CODATA 2022, `leo_and_orbital_habitats.md`); PCM 48.8 kJ/kg system level (13.6 Wh/kg), ice melt 333.44 kJ/kg (92.6 Wh/kg) (`waste_heat_utilization.md` E1); Li-ion cell 182-264 Wh/kg (`robot_body_in_space.md` S33); ISS dark 36 of 93 min (`leo_and_orbital_habitats.md`). | used by pointer |

**Dead end:** the Moon fact sheet has no row for the equator's inclination to the ecliptic. It is derived below (§3) under an ASSUMED Cassini-state coplanarity.

## 3. Findings (sourced inputs)

| Body | Radius used (km) | GM (km3/s2) | Rotation (h) | Obliquity (deg) | Year (d) | Sunlight (W/m2) |
|---|--:|--:|--:|--:|--:|--:|
| Earth (validation) | 6378.137 (equatorial) | 398,600 | 23.9345 | 23.44 | 365.256 | 1361.0 |
| Moon | 1737.4 (volumetric mean) | 4,902.9 (= G x 0.07346e24 kg) | 655.720 | **1.54 (DERIVED: 6.68 - 5.145; Cassini-state coplanarity ASSUMED)** | 346.62 (eclipse year, from the L4/L5 simulation) | 1361.0 |
| Mars | 3396.2 (equatorial) | 42,828 | 24.6229 | 25.19 | 686.980 | 586.2 |
| Jupiter | 71,492 (1 bar, equatorial) | 126,686,891 (= G x 1898.13e24 kg) | 9.9250 | 3.13 | 4332.589 | 50.26 |
| Saturn | 60,268 (1 bar, equatorial) | 37,931,382 (= G x 568.32e24 kg) | 10.656 | 26.73 | 10,755.699 | 14.82 |

Cross-check: Mars GM from the sheet (42,828) against G x 0.64169e24 kg = 42,827 km3/s2 (agrees).

## 4. Conflicts and model limits

1. **Cylindrical shadow.** The Sun's size (penumbra) is ignored. Test on Earth's geostationary orbit: model **69.4 min** of darkness a day at the equinox against NOAA's "up to 72 minutes" (F7): 3.6 percent low. The model's eclipse season is **24.8 percent of the year (91 days)** against NOAA's two seasons of about 45 days each side of an equinox (about 90 days). Treat the dark times below as about 4 percent short, and the season lengths as good.
2. **Equatorial plane only.** Seasons come from the body's obliquity. A polar or inclined orbit has a different seasonal pattern (not computed).
3. **Moon's equator.** The lunar equator's tilt to the ecliptic is derived under an assumption; it only matters for the Moon's seasons, which are all-year at every radius listed (β* is 5.7 deg or more against 1.54 deg).
4. **Orbit stability, rings, oblateness, radiation** are not modeled (Saturn's equatorial orbits inside about 2.3 radii cross the ring system; **ring radii were not opened this session** and no claim is made about them).

## 5. Derived figures

Model: `f(β) = (1/π) acos( sqrt(1 - (R/r)²) / cos β )` for |β| < asin(R/r), else 0 (fraction of one orbit in shadow when the Sun is β above the orbit plane). Period `T = 2π sqrt(r³/GM)`.
Dark time per orbit = `f T`. For an equatorial orbit β is the Sun's declination, `δ = asin(sin(obliquity) sin L)`, L uniform over the body's year. Season = fraction of the year with any eclipse.
Storage is per kW carried through the longest dark interval (β = 0): kWh/kW = f T in hours; Li-ion cell at 182 Wh/kg (low end), ice at 92.6 Wh/kg, system-level PCM at 13.6 Wh/kg.

### 5.1 Results (`_calc/body_orbit_eclipses_output.txt`)

| Orbit | r (km) | Period (h) | Longest dark (min; % of orbit) | Year-mean dark | Eclipse season (% of year) | Dark periods per year | kWh per kW | Li-ion cell (kg/kW) | Ice (kg/kW) | PCM (kg/kW) |
|---|--:|--:|--|--:|--:|--:|--:|--:|--:|--:|
| **Earth GEO (validation)** | 42,164 | 23.934 | 69.4; 4.8 % | 0.94 % | 24.8 | 91 | 1.157 | 6.4 | 12.5 | 85.1 |
| **Moon** 100 km altitude | 1,837 | 1.963 | 46.5; 39.4 % | 39.45 % | 100 | 4,238 | 0.774 | 4.3 | 8.4 | 56.9 |
| Moon 1,000 km | 2,737 | 3.570 | 46.9; 21.9 % | 21.88 % | 100 | 2,330 | 0.781 | 4.3 | 8.4 | 57.5 |
| Moon 2 R | 3,475 | 5.106 | 51.1; 16.7 % | 16.66 % | 100 | 1,629 | 0.851 | 4.7 | 9.2 | 62.6 |
| Moon 4 R | 6,950 | 14.441 | 69.7; 8.0 % | 8.02 % | 100 | 576 | 1.161 | 6.4 | 12.5 | 85.4 |
| Moon 10 R | 17,374 | 57.082 | 109.2; 3.2 % | 3.13 % | 100 | 146 | 1.820 | 10.0 | 19.7 | 133.8 |
| **Mars** 400 km altitude | 3,796 | 1.973 | 41.7; 35.3 % | 34.44 % | 100 | 8,358 | 0.695 | 3.8 | 7.5 | 51.1 |
| Mars 2 R | 6,792 | 4.721 | 47.2; 16.7 % | 13.39 % | 100 | 3,492 | 0.787 | 4.3 | 8.5 | 57.9 |
| Mars 4 R | 13,585 | 13.353 | 64.4; 8.0 % | 2.49 % | 40.0 | 493 | 1.074 | 5.9 | 11.6 | 79.0 |
| Mars areostationary | 20,428 | 24.623 | 78.5; 5.3 % | 1.06 % | 25.5 | 171 | 1.309 | 7.2 | 14.1 | 96.3 |
| Mars 10 R | 33,962 | 52.784 | 101.0; 3.2 % | 0.38 % | 15.1 | 47 | 1.683 | 9.2 | 18.2 | 123.7 |
| **Jupiter** 2 R | 142,984 | 8.384 | 83.8; 16.7 % | 16.63 % | 100 | 12,403 | 1.397 | 7.7 | 15.1 | 102.7 |
| Jupiter synchronous | 160,010 | 9.925 | 87.8; 14.7 % | 14.70 % | 100 | 10,477 | 1.463 | 8.0 | 15.8 | 107.6 |
| Jupiter 3 R | 214,476 | 15.402 | 100.0; 10.8 % | 10.75 % | 100 | 6,751 | 1.666 | 9.2 | 18.0 | 122.5 |
| Jupiter 5 R | 357,460 | 33.140 | 127.4; 6.4 % | 6.29 % | 100 | 3,138 | 2.124 | 11.7 | 22.9 | 156.2 |
| Jupiter 10 R | 714,920 | 93.734 | 179.3; 3.2 % | 2.94 % | 100 | 1,109 | 2.989 | 16.4 | 32.3 | 219.8 |
| Jupiter 20 R | 1,429,840 | 265.120 | 253.3; 1.6 % | 0.85 % | 73.7 | 289 | 4.221 | 23.2 | 45.6 | 310.4 |
| **Saturn** 2 R | 120,536 | 11.859 | 118.6; 16.7 % | 12.83 % | 100 | 21,767 | 1.977 | 10.9 | 21.3 | 145.3 |
| Saturn synchronous | 112,239 | 10.656 | 115.4; 18.0 % | 14.72 % | 100 | 24,225 | 1.923 | 10.6 | 20.8 | 141.4 |
| Saturn 3 R | 180,804 | 21.787 | 141.4; 10.8 % | 4.41 % | 53.1 | 6,296 | 2.357 | 12.9 | 25.5 | 173.3 |
| Saturn 5 R | 301,340 | 46.877 | 180.3; 6.4 % | 1.47 % | 29.3 | 1,615 | 3.005 | 16.5 | 32.4 | 220.9 |
| Saturn 10 R | 602,680 | 132.589 | 253.7; 3.2 % | 0.36 % | 14.3 | 278 | 4.228 | 23.2 | 45.7 | 310.8 |
| Saturn 20 R | 1,205,360 | 375.019 | 358.3; 1.6 % | 0.09 % | 7.1 | 49 | 5.971 | 32.8 | 64.5 | 439.1 |

"R" is the body radius in §3. Masses are the storage medium only (Li-ion at cell level), before tank, pack or exchanger.

### 5.2 Sunlight and the heliocentric case (`_calc/body_sun_equilibrium_output.txt`)

| Place | Sunlight (W/m2) | Solar-array area for the same power (Earth = 1) | Sun-facing face, alpha/eps = 1: one face / sphere | alpha/eps = 0.25: one face / sphere |
|---|--:|--:|--|--|
| Earth/Moon, 1 AU | 1361.0 | 1.00 | 393.6 K / 278.3 K | 278.3 K / 196.8 K |
| Mars | 586.2 | 2.32 | 318.9 K / 225.5 K | 225.5 K / 159.4 K |
| Jupiter | 50.26 | 27.08 | 172.5 K / 122.0 K | 122.0 K / 86.3 K |
| Saturn | 14.82 | 91.84 | 127.1 K / 89.9 K | 89.9 K / 63.6 K |

A radiator face at 300 K (emissivity 0.85) sheds 390.4 W/m2. A perfectly absorbing face at Saturn collects 14.82 W/m2: **3.8 percent of what one radiator face sheds**, so the Sun cannot keep a 300 K station warm there; all the heat must come from the station's own power.
**Heliocentric orbit:** a circular orbit about the Sun has no planetary shadow at any distance, so it has **no dark interval**; the flux is 1361 W/m2 x (1 AU / r)². This confirms the caveat in the waste-heat file §10.2: a heat battery has no periodic dark interval to carry a heliocentric station through.

### 5.3 What the numbers say

- **Low orbit anywhere is dark for 17 to 39 percent of every orbit** (Moon 100 km 39.4 percent; Mars 400 km 35.3; Jupiter 2 R and Saturn 2 R 16.7 percent at the equinox), with **4,000 to 24,000 dark periods a year** (ISS: 5,655 from the sibling figures). Longest dark per orbit is 0.7 to 2 kWh per kW carried.
- **Synchronous orbits** have a dark period every day: Mars (areostationary) 78.5 min on 25.5 percent of the year (171 a year), the same pattern as Earth's GEO; Jupiter 87.8 min **every day of the year** (10,477 a year); Saturn 115.4 min every day (24,225 a year).
- **High orbits have few but long dark intervals:** Jupiter at 20 R 253 min (289 a year); Saturn at 20 R 358 min (49 a year); Saturn at 10 R 254 min (278 a year).
- **Obliquity decides whether there is a season:** Jupiter's 3.13 deg tilt means a Jovian equatorial orbit is eclipsed all year at every radius up to 10 R (β* 5.7 deg exceeds the tilt) and 73.7 percent of the year at 20 R; Saturn's 26.73 deg tilt gives seasons beyond 2 R (3 R: 53.1 percent of the year; 5 R: 29.3; 20 R: 7.1).
- **Storage through the longest dark interval is cheap in mass at these durations:** a Li-ion cell carries 1 kW for 0.7 to 6 kWh at 3.8 to 33 kg/kW (cell level); system-level PCM is 13 to 19 times heavier per kWh (13.6 against 182-264 Wh/kg); ice melt sits between. The cost that grows is **cycles**, not mass: at 4,000 to 24,000 per year the battery's cycle life (not covered here) sets the replacement interval.
- **Weak sunlight reverses the thermal problem at Jupiter and Saturn:** the Sun supplies 27 times (Jupiter) and 92 times (Saturn) less power per m2, so solar arrays are 27 to 92 times larger, and sunlight cannot warm a station (above). Waste heat there is not a rejection problem first; it is the station's only heat source, which is where a **heat battery's value changes character** (carry heat through periods of low internal power), subject to evidence in the companion file.

## 6. Constraints for any inhabitant

- A station in a low circular orbit around the Moon, Mars, Jupiter or Saturn is in shadow 17 to 39 percent of each orbit, every orbit (§5.1).
- A Jovian or Saturnian station gets 27 or 92 times less solar power per m2 than at 1 AU (§5.2); power must come from elsewhere (reactor, radioisotope) or from arrays 27 to 92 times larger.
- A synchronous Mars orbit has two eclipse seasons a year of about 45 days each, up to 78.5 min a day; a synchronous Jupiter or Saturn orbit has a 88 or 115 minute eclipse every day.
- A heliocentric orbit never has a planetary eclipse.

## 7. Candidate handwaves

None. (Where a result depends on an ASSUMED quantity it is marked: the lunar equator's tilt; the cylindrical shadow, which is about 4 percent short on dark time.)

## 8. Open threads

1. Inclined and polar orbits (seasons differ); eccentric orbits; frozen orbits.
2. Orbits about moons: Ganymede, Callisto, Europa, Io, Titan, Enceladus (each has its own radius, GM, and its planet's shadow as a second occulter); Phobos and Deimos.
3. Saturn's ring shadow and ring-plane hazards (ring radii not opened this session); Jupiter's radiation belts at the radii used (sibling files hold doses; not tied to these radii).
4. Battery cycle life at 4,000 to 24,000 cycles a year (primary source needed), and PCM cycling durability: the companion file `lagrange_thermal_environment.md` is to supply heritage data.
5. A one-minute-step version of the validation on Earth GEO, including penumbra (to put a number on the model's 4 percent shortfall).

## 9. Rejected sources

- The search summary S1 as a source for any figure (used for leads only; the NOAA page was opened and quoted).
- Any recalled radius, mass, tilt or ring radius: replaced by the NASA fact sheets above.

## Files in `_calc/`

`body_orbit_eclipses.py` and `body_orbit_eclipses_output.txt` · `body_sun_equilibrium.py` and `body_sun_equilibrium_output.txt`. Run with `python3 -I`.
