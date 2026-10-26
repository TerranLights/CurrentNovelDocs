# Inner Solar System logistics network: Mercury, Venus, Earth, Moon, Mars, near-Earth asteroids, main belt

*Research file, OOLSD library, seventh tranche, section 3. Started 2026-10-11. Physics and engineering only.*

## Scope

Mercury (surface, poles, low orbit), Venus (orbit and cloud level), Earth and the Moon (high orbit and cislunar nodes),
Mars, near-Earth asteroids and the main belt (Ceres as the reference body), treated as one transport network: windows,
gravity-assist routes, propulsion near the Sun, launch from Mercury, capture at destinations, fleet sizes for 1 kt, 100 kt
and 1 Mt per year, communications, power beaming, propellant supply, space weather and scaling evidence. Delta-v tables,
tug scaling and xenon limits already in `space_trucking_and_transport_infrastructure.md` are cited, not repeated.

## SEARCH LOG

All entries dated 2026-10-11 unless stated. Tally: 119 rows; 47 web searches, about 69 pages, PDFs or API records opened, 3 calculation snags. Eleven rows died at the sources (HTTP 403/405, scanned or HTML-instead-of-PDF files, a defunct domain, no study existing) and one at the query (row 89); twelve were thin. One finding from a search summary was killed after checking (row 63), five other search-summary figures were discarded as unconfirmed (see Rejected sources), and one set of constants typed from memory was replaced by sourced values (row 113). Units: t = metric ton (1,000 kg); kt = 1,000 t; Mt = 10^6 t.

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| 1 | Page: JPL SSD, "Approximate Positions of the Planets", Table 1 (1800-2050 AD), https://ssd.jpl.nasa.gov/planets/approx_pos.html | useful | a, e, i for Mercury, Venus, Earth-Moon barycenter, Mars; page shows no revision date |
| 2 | API: JPL SBDB, https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1&full-prec=1 (and &phys-par=1) | useful | Ceres a = 2.76555 au, e = 0.0797, i = 10.59 deg, period 1,679.85 d, epoch JD 2461200.5, solution 2021-04-13; GM 62.6284 km^3/s^2 |
| 3 | Page: JPL SSD, "Astrodynamic Parameters", https://ssd.jpl.nasa.gov/astro_par.html (raw HTML grep) | useful | GM Sun, au, c re-read this session |
| 4 | Search: `Langevin "Mercury" ballistic multiple gravity assist trajectories Earth-Venus-Mercury delta-v` | useful (leads) | Led to the ISAS 1999 paper; Langevin's own paper not surfaced |
| 5 | Search: `Yen "Mercury orbiter" trajectory "Venus-Venus-Mercury" JPL ballistic` | useful (leads) | Same ISAS paper; science.gov topic page; NTRS 19740013378 (not opened) |
| 6 | Page: Yamakawa (ISAS), "ISAS Mercury Orbiter Mission Trajectory Design Strategy", ISSFD 1999, https://issfd.org/ISSFD_1999/pdf/IFL_1.pdf | useful | WebFetch could not decode; PDF saved and read with pdftotext. Yen-type sequence, flight times, arrival v-inf, MOI and total delta-v |
| 7 | Search: `Mercury sample return mission trajectory study Earth return delta-v flight time Venus flyby` | useful (leads) | ESA solar-sail Mercury sample return; Strathprints record |
| 8 | Page: ESA Future Missions, "Analysis of a solar sail Mercury sample return mission", https://sci.esa.int/web/future-missions-department/-/37071-analysis-of-a-solar-sail-mercury-sample-return-mission | useful | Summary; "275 m" sail ambiguous (side or area?) resolved in row 11 |
| 9 | Page: Strathprints 6663, Hughes et al., J. Spacecraft and Rockets 43(4) 828-835, 2006 | useful (abstract only) | Abstract renders "275-m²" (an extraction artifact; the full paper says 275 m side, 75,625 m²) |
| 10 | Search: `Hughes Macdonald McInnes "Sample return from Mercury and other terrestrial planets using solar sail propulsion" pdf characteristic acceleration` | useful | Found the ESA-hosted full paper |
| 11 | Page: Hughes, Macdonald, McInnes et al., "Analysis of a Solar Sail Mercury Sample Return Mission", IAC-04 (ESA TRS PDF), https://sci.esa.int/documents/34923/36148/1567254578500-TRS-SolarSail-Mercury-SRM.pdf | useful | Read in full via pdftotext: sail 275 x 275 m, 448 kg, 0.25 / 0.7839 mm/s^2, outbound 2.85 yr, return 369 d, escape spiral 16 d, comparison with SEP and chemical concepts |
| 12 | Search: `Langevin "Chemical and solar electric propulsion options for a cornerstone mission to Mercury" Acta Astronautica` | thin | Citation confirmed (Acta Astronautica 47(2-9) 443-452, 2000) via a reference list; no open full text found. Died at the sources (paywall) |
| 13 | Search: `Earth-Venus cycler trajectory Hollister Menning period v-infinity` | thin | Only Wikipedia-grade summaries and the MIT thesis record; no numbers |
| 14 | Page: MIT DSpace handle 1721.1/14165 (Menning thesis record) | dead (at the sources: HTTP 405) | |
| 15 | Page: NTRS 20070002800 (Montgomery, Young, Adams, MSFC, "Mercury Sample Return using Solar Sails", 2006) record | thin | No abstract or numbers on the record page; not used |
| 16 | Search: `"Low Excess Speed Triple Cyclers of Venus, Earth, and Mars" Jones Hernandez Jesick` | useful (leads) | NTRS record 20190028464 |
| 17 | Page: NTRS 20190028464 record (Jones, Hernandez, Jesick, JPL, AAS/AIAA Astrodynamics Specialist Conf., Aug 2017) | useful (abstract only) | "average transit leg excess speed below 5 kilometers per second"; no PDF on NTRS |
| 18 | Search: `Hollister "Periodic orbits for interplanetary flight" Earth Venus cycler 1969 Journal of Spacecraft and Rockets` | useful (leads) | NTRS 19700017824 |
| 19 | Page: NTRS 19700017824, Rall, "Free-Fall Periodic Orbits Connecting Earth and Mars", MIT Measurement Systems Laboratory, Oct 1969 (PDF, OCR) | useful | Describes the Hollister and Menning Earth-Venus periodic orbits (repeat interval OCR-garbled, see Conflicts); Earth-Venus-Mars near-repeat 6.4 yr and 32 yr |
| 20 | Page: Georgia Tech SSDL "AAS-17-zzz.pdf" | dead (at the sources: returned an HTML page, not the PDF) | |
| 21 | Search (extended): `"Earth-Venus" cycler orbits v-infinity km/s ballistic "Venus cycler" paper` | thin | MDPI Earth-Venus weak-capture paper (not a cycler); academia.edu "cycler-quartet between Venus and Sol/Terra L1" (self-published, not used, see Rejected); ResearchGate triple-cycler PDF (not opened: ResearchGate blocks tools) |
| 22 | Page: arXiv 2107.06795, NASA "Mercury Lander: Planetary Mission Concept Study for the 2023-2032 Decadal Survey" (APL-led, 2021), PDF read with pdftotext | useful | SEP cruise with 1 Earth, 2 Venus, 5 Mercury flybys; 117.5 months; 484 kg xenon; v-inf at each flyby; arrival v-inf 0 |
| 23 | Search: `BepiColombo solar electric propulsion system T6 thrusters thrust power at 0.3 AU solar array temperature derating in-flight performance` | useful (leads) | Frontiers 2021 paper; ESA image captions; Universe Today (secondary, not used) |
| 24 | Page: Filleul, Sutherland, Cipriani, Charles, "BepiColombo: A Platform for Improving Modeling of Electric Propulsion-Spacecraft Interactions", Frontiers in Space Technologies 2:639819, 11 Mar 2021 (PDF, pdftotext) | useful | T6 at full thrust: <4.7 kW, 145 mN, 3,875 s, 3.802 mg/s; life test at 125 mN; MTM arrays 14 m long, >40 m^2, SEPS <=11 kW; Sun aspect angle 13 to 23 deg |
| 25 | Page: Airbus "BepiColombo mission" PDF | dead (at the sources: returned HTML, not the PDF) | |
| 26 | Search: `ESA BepiColombo Mercury Transfer Module solar arrays tilted to limit temperature power 0.3 AU high-intensity high-temperature cells design` | useful (leads) | ESA "High temperature challenge" page |
| 27 | Page: ESA, "High temperature challenge", https://www.esa.int/Science_Exploration/Space_Science/BepiColombo/High_temperature_challenge (no date shown) | useful | 42 m^2 MTM array; "about 10 times" solar intensity at Mercury; >450 C |
| 28 | Search: `ESA BepiColombo thruster power issue 2024 reduced thrust Mercury arrival November 2026 statement` | useful (leads) | ESA 2 Sep 2024 article; space.com and others (secondary, not used) |
| 29 | Page: ESA, "Fourth Mercury flyby begins BepiColombo's new trajectory", 2 Sep 2024 | useful | Thrusters "below the minimum thrust required" for Dec 2025 insertion; new arrival Nov 2026; cause: unexpected currents between array and power unit |
| 30 | Pages: NSSDC fact sheets Mercury (11 Jan 2024), Venus (11 Jan 2024), Earth (15 Nov 2024), Mars (19 May 2025) | useful | Solar irradiance 9,082.7 / 2,601.3 / 1,361.0 / 586.2 W/m^2; Mercury/Earth ratio 6.674; Venus atmosphere mass and composition |
| 31 | Search: `"Solar Power Technologies for Future Planetary Science Missions" JPL 2017 high intensity high temperature Mercury solar array power per area` | useful (leads) | JPL D-101316 PDF on solarsystem.nasa.gov |
| 32 | Page: JPL D-101316, "Solar Power Technologies for Future Planetary Science Missions", Dec 2017 (PDF, pdftotext) | useful | MESSENGER: about 2/3 of cells replaced by OSRs, array off-pointed, ~130 C operating; Bepi arrays to 190 C; 1 AU state of practice ~80 W/kg rigid, 100-175 W/kg flexible, ~330-338 W/m^2; temperature coefficient -0.22%/C |
| 33 | Search (extended): `BepiColombo MTM solar array design paper European Space Power Conference power output versus Sun distance kW optical solar reflectors cell coverage` | useful (leads) | ESPC 2017 MPO paper (E3S); ADS record for 2011 MTM/MPO paper; MTM "peak power of about 13000W" from the search summary |
| 34 | Page: E3S Web of Conferences, ESPC 2017 paper 04006 (MPO solar array) PDF and HTML record | dead (at the sources: HTTP 403, and curl returned HTML) | The "13,000 W" MTM peak figure therefore rests on a search summary only; not used as a primary value |
| 35 | Page: NASA ADS 2011ESASP.690E..98P (MTM and MPO solar array design) | dead (at the sources: HTTP 405) | |
| 36 | Page: Springer, Benkhoff et al., "BepiColombo - Mission Overview and Science Goals", Space Sci. Rev. 2021 (HTML and PDF) | dead (at the sources: login redirect; PDF request returned HTML) | |
| 37 | Search: `IEPC-2019 "BepiColombo" "Solar Electric Propulsion System Operations for the Transit to Mercury" electricrocket.org` | useful (leads) | EUCASS 2019 GNC paper; INAF news item |
| 38 | Page: Steiger et al. (ESA/ESOC, Airbus), "GNC Operations for the BepiColombo Mission to Mercury: First In-flight Experience", EUCASS 2019, DOI 10.13009/EUCASS2019-218 (PDF, pdftotext) | useful | "Despite approaching the Sun, the mission is highly power-constrained"; no array off-pointing above 0.62 AU, significant below; backside illumination critical below 0.7 AU; power "generally does not allow" max thrust; weekly navigation pass |
| 39 | Page: INAF Media, "BepiColombo aggiornamento thrusters", 27 May 2024 (Italian) | useful (secondary, quoting ESA's Montagnon) | Thrust at 90% of plan after the April 2024 anomaly |
| 40 | Search: `solar sail "sundiver" perihelion characteristic acceleration lightness number heliocentric close approach temperature limit study` | useful (leads) | Bailer-Jones arXiv 2009.12659; MPIA pages; Dachwald slides (not opened) |
| 41 | Page: Bailer-Jones (MPIA), "The Sun Diver: Combining solar sails with the Oberth effect", Am. J. Phys. (accepted 26 Sep 2020), arXiv 2009.12659 (PDF, pdftotext) | useful | 9.1 uPa on a perfect reflector at 1 AU; lambda = 1 at 1.5 g/m^2; IKAROS lambda < 0.01, LightSail 2 about 0.01; 0.1 AU dive example about 1,000 K sail temperature |
| 42 | Search: `NASA Solar Cruiser solar sail 1653 m2 characteristic acceleration areal density NTRS` | useful (leads) | NTRS 20210000631, 20220011260 |
| 43 | Page: Clements et al. (MSFC), "Attitude Control System for the Solar Cruiser and Future Solar Sail Missions", NTRS 20210000631 (abstract PDF, Jan 2021) | useful | 95 kg craft, 1,654 m^2 sail; Solar Polar Imager needs about 7,000 m^2; IKAROS 196 m^2 largest flown |
| 44 | Search: `Solar Cruiser solar sail mission status not flown IMAP rideshare cancelled 2024 deployment test NASA Marshall` | useful (leads) | Wikipedia and skyrocket (secondary, not used); NTRS 20220011260 |
| 45 | Page: Johnson et al. (MSFC, GSFC, Redwire, Ball), "The NASA Solar Cruiser Mission - Solar Sail Propulsion Enabling Heliophysics Missions", NTRS 20220011260 (slides, 2022) | useful | 1,653 m^2, 2.5 um film; "not confirmed for flight" |
| 46 | Search: `Edelbaum low-thrust circle-to-circle delta-v approximation formula plane change "Edelbaum" NASA technical report equation` | useful (leads) | arXiv 2502.15914 states the formula with references |
| 47 | Page: Choi and Ho (Georgia Tech), "Orbital Depot Location Optimization for Satellite Constellation Servicing with Low-Thrust Transfers", arXiv 2502.15914v2, 25 Aug 2025 (preprint) | useful | Edelbaum circle-to-circle low-thrust delta-v with plane change, citing Edelbaum 1961 (ARS J. 31(8)) and Kechichian 1997 (JGCD 20(5)) |
| 48 | Search: `Hohmann transfer Earth to Mercury arrival hyperbolic excess velocity 9.6 km/s departure 7.5 km/s C3 56` | useful (one primary-grade hit) | Orbiter-forum and Q&A sites (secondary, not used); TU Delft slides |
| 49 | Page: TU Delft OCW, AE2104 Flight and Orbital Mechanics, slides 11-12 (PDF, pdftotext) | useful | Earth-to-Mercury Hohmann: departure v-inf 7.533 km/s, C3 56.7, Mercury capture 7.565 km/s, total 13.122 km/s; cross-checks D1 and exposes [TR]'s C1 error |
| 50 | Search (extended): `"Mercury sample return" solar electric propulsion return trajectory Mercury to Earth flight time years Venus gravity assist JPL Team X study` | thin | No primary SEP or chemical Mercury-to-Earth return trajectory found; only the sail studies again, an Acta Astronautica sail-plus-Venus paper (paywalled, not opened) and the E-sail overview. Died at the sources for SEP returns |
| 51 | Page: Janhunen et al. (FMI, ESA ESTEC, Tartu), "Electric solar wind sail applications overview", arXiv 1404.5815v1, 23 Apr 2014 | useful | E-sail thrust scales about 1/r (photon sail and SEP 1/r^2); 1 mm/s^2 = 31.5 km/s per year; 391 kg craft with 143 kg E-sail (44 tethers x 15.3 km); Mercury rendezvous "in less than one year" and return "in the same time"; aluminum tethers may not tolerate Mercury temperatures (all SPECULATIVE: unflown) |
| 52 | Search: `Armstrong Sandberg "Eternity in six hours" Mercury disassembly mass driver energy Dyson swarm Acta Astronautica` | useful (leads) | Citation confirmed (Acta Astronautica 89, 1-13, 2013); substack and forum discussion (not used) |
| 53 | Page: FHI publication page for the paper | dead (at the sources: domain no longer resolves; the institute closed) | |
| 54 | Search: `"Eternity in six hours" pdf Armstrong Sandberg Mercury "mass driver" efficiency disassembly years` | useful (leads) | Old FHI PDF URL |
| 55 | Page: Internet Archive copy of http://www.fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf (preprint of Armstrong and Sandberg 2013) | useful | Section 4.2 "Disassembling Mercury": 9 MJ/kg to escape, 1/10 of energy to launching, 1/3 captor efficiency, 1 km^2 seed array, 5-yr processing lag; "completely disassembled in 31 years and 85 days" (SPECULATIVE thought experiment) |
| 56 | Page: NSSDC Mercury fact sheet (re-opened, raw HTML) | useful | Sidereal rotation 1,407.6 h; length of day 4,222.6 h; obliquity 0.034 deg; 590-725 K sunward surface; GM 0.022032 x 10^6 km^3/s^2 |
| 57 | Search: `lunar electromagnetic mass driver launcher recent study NTRS 2020s coilgun lunar regolith export kg per year power` | thin | No 2020s primary study; blogs and a capstone project page (not used); several NTRS records |
| 58 | API: NTRS records 19930007725, 19900012490, 19920010134, 20205008049, 19890044698 (titles and abstracts) | useful (two used) | Snow and Kolm, lunar superconducting quenchgun: 1 t LOX containers every 2 h, about 4,400 t/yr to low lunar orbit (in NASA JSC "Space Resources" vol. 2, 1992); Schroeder, Gully, Driga, IEEE Trans. Magnetics 25 (1989): coilgun designed for 10 kg to 11 km/s (design, not built). The other three not relevant |
| 59 | Search: `Hoyt Uphoff "Cislunar tether transport" Lunavator tip velocity tether mass ratio NIAC final report` | thin | Citation only (NIAC 2000; AIAA 99-2690); no numbers; [CY] already holds Hoyt figures |
| 60 | Search: `rotating tether tip velocity characteristic velocity material tensile strength density tether mass ratio exponential Spectra Zylon NASA TP` | useful (leads) | Hoyt and Forward patents; NSS Lunar Bases paper (not opened); substack and forum (not used) |
| 61 | Page: USPTO image PDF of US 6,386,484 | dead (at the sources: scanned images, no text) | |
| 62 | Page: Google Patents US6386484B1 (Hoyt and Forward, "Failure resistant multiline tether", priority 8 Sep 2000, issued 14 May 2002), read twice | useful | Characteristic velocity sqrt(T/D); "most metals and fibers ... around 1 km/s"; commercial fibers to 4 km/s at 60% of measured strength; Spectra 2000 at safety factor 2 "approximately 80 times the payload mass"; 3.3 km/s tip speed for lunar transfer from LEO |
| 63 | Pages: MPIA Sun Diver page (bailer-jones.www3.mpia.de/sundiver.html, dated 29 Dec 2020), poster PDF (mpia-hd.mpg.de/~calj/sundiver/sundiver_mpia_poster.pdf) and sundiver.pdf; re-grep of the arXiv text | dead (at the sources) for the claim checked | **Killed finding:** the search summary in row 40 attributed a "0.1 AU perihelion, 937 m sail, about 1000 K" example to the Sun Diver work; none of the four Sun Diver documents contains it. The row built on it was deleted from F3. The likely origin is a different paper in the same result list (arXiv 0809.3535, beryllium hollow-body sail), not opened |
| 64 | Search: `Girija "quantitative assessment of aerocapture" Venus Earth Mars Titan corridor width peak heat rate deceleration arXiv` | useful (leads) | arXiv 2309.09438; engrxiv preprint; Universe Today (secondary, not used) |
| 65 | Search: `Lockwood "Aerocapture Systems Analysis for a Venus Mission" NASA TM 2006 entry velocity ballistic coefficient mass fraction` | useful (leads) | NTRS 20060010899 |
| 66 | Page: Lockwood, Starr et al. (NASA LaRC, ARC, JPL), "Systems Analysis for a Venus Aerocapture Mission", NASA/TM-2006-214291, March 2006, NTRS 20060010899 (PDF, pdftotext) | useful | Entry 11.25 km/s; about 4,300 m/s removed in one pass; delivered 687 kg vs 374 kg (chemical plus 122 d / 670 aerobraking orbits) vs 111.5 kg (all-chemical); aeroshell 30% of launch mass; heating 500-600 W/cm^2 convective plus 500-700 radiative; corridor plus or minus 0.76 deg; scale heights Venus 3.5-4.7, Earth 8.4, Mars 6.4-8.2 km |
| 67 | Page: Girija (Purdue), "Performance Benefit of Aerocapture for the Design Reference Mission Set", arXiv 2309.09438 (2023 preprint) | useful | Delivered-mass gain from drag-modulation aerocapture: Venus 92%, Earth 108%, Mars 17%; insertion delta-v replaced: Venus 3,533 m/s (v-inf 3.5), Earth 3,731 m/s (v-inf 3.5), Mars 2,079 m/s (v-inf 2.6), all to 400 km circular |
| 68 | Search: `first aerocapture flight demonstration ever flown spacecraft 2025 2026 drag modulation` | useful (leads) | NASA STRG page, Georgia Tech theses (not opened), trade-press article |
| 69 | Page: Military and Aerospace Electronics, "NASA seeks industry support for aerocapture demo mission in Earth orbit", 27 Jun 2025 | useful (secondary) | ARRIVAL demonstration solicited (1 m aeroshell, about 500 km orbit); does not itself state flight history. Supports "not yet flown" only together with Lockwood 2006 and Spilker 2016 ([TR]) |
| 70 | Search: `NASA OIG Deep Space Network report oversubscribed antennas capacity demand hours 2023` | useful (leads) | IG-23-016; trade press (not used) |
| 71 | Page: NASA OIG, "Audit of NASA's Deep Space Network", IG-23-016, 12 Jul 2023 (PDF, pdftotext) | useful | Three complexes (Goldstone, Madrid, Canberra), one 70 m plus several 34 m antennas each; nearly 60 missions; about 77,000 antenna hours in FY2022; demand exceeds supply by up to 40%, about 50% by the 2030s; 8,500-15,000 hours a year short of requests; Artemis I used over 900 hours in 25 days |
| 72 | Search: `Deep Space 1 AutoNav autonomous optical navigation flight results accuracy NTRS Riedel` | useful (leads) | NTRS records |
| 73 | API: NTRS 20060032732 (Riedel et al. 2000), 20060029673 (Bhaskaran et al. 2002), 19980137229 (Riedel et al. 1997) | useful (abstracts) | First autonomous optical navigation in deep space, controlling an ion-propelled cruise; Borrelly flyby accuracy under 10 km with radio, optical and interferometric data combined |
| 74 | Search: `Deep Space Atomic Clock mission results one-way navigation stability NASA JPL 2021 Nature` | useful (leads) | Nature 2021; NTRS 20220001460; press (not used) |
| 75 | Page: RePEc record of Burt et al., "Demonstration of a trapped-ion atomic clock in space", Nature 595, 43-47, Jul 2021 (abstract) | useful | 3 x 10^-15 stability at 23 days, drift 3.0 x 10^-16 per day, up to an order of magnitude better than earlier space clocks |
| 76 | API: NTRS 20220001460, Stuart, Ely, Seubert, "Results of the Deep Space Atomic Clock Deep Space Navigation Analog Experiment" (Aug 2020) | useful (abstract) | One-way radiometric data "with accuracy equivalent to current two-way tracking data" |
| 77 | Page: Morabito and Hastrup, "Communications with Mars During Periods of Solar Conjunction: Initial Study Results", IPN Progress Report 42-147, 15 Nov 2001, https://tmo.jpl.nasa.gov/progress_report/42-147/147C.pdf (PDF, pdftotext) | useful | X-band works to about 2.3 deg Sun-Earth-probe angle (NEAR test); S-band unreliable below 4 deg (Galileo); Ka-band amplitude saturation near 0.67 deg, usable with special methods to about 0.4 deg; Sun disk radius 0.264 deg from Earth; relay option weighed against outage |
| 78 | Page: NSSDC Sun fact sheet (9 May 2024) | useful | Solar volumetric mean radius 695,700 km |
| 79 | Search: `DARPA POWER program laser power beaming record 800 watts 8.6 km 2025 efficiency` | useful (leads) | DARPA news; NRL; trade press (not used) |
| 80 | Page: DARPA, "DARPA program sets distance record for power beaming", 16 May 2025 | useful | Over 800 W delivered for 30 s over 8.6 km; over 1 MJ in the campaign; over 20% optical-out-to-electrical-out at shorter range; earlier record 230 W at 1.7 km |
| 81 | Search: `Dickinson 1975 Goldstone microwave power transmission 30 kW 1.54 km rectenna efficiency 82 percent NASA JPL report` | useful (leads) | NTRS records; SSI pages (not opened) |
| 82 | API: NTRS 19760004119, Dickinson (JPL), "Evaluation of a microwave high-power reception-conversion array for wireless power transmission", Sep 1975 (abstract) | useful | 24 m^2 rectenna at 1.54 km, 2,388 MHz; up to 30.4 kW DC; collection-conversion efficiency "greater than 80 percent". (The 34 kW and 82.5% figures in the search summary were not in the abstract and are not used) |
| 83 | Page: NASA OTPS, Rodgers et al., "Space-Based Solar Power", 11 Jan 2024 (PDF, pdftotext; previously used by [TR] for launch costs) | useful | GEO reference designs: about 2 GW delivered; rectenna 6 km (2.45 GHz) or 4 km (5.8 GHz); efficiency chain cells 0.35, DC-DC 0.9, DC-RF 0.7, antenna 0.9, atmosphere 0.98, beam collection 0.95, rectenna 0.78, ground DC-DC 0.9 |
| 84 | Search: `Goubau parameter tau = sqrt(At Ar)/(lambda D) beam collection efficiency microwave power transmission formula` | useful (leads) | Starshot model; a 2026 LEO SBSP preprint; a 2018 J. Electromagn. Waves Appl. paper (abstract); an undergraduate Dyson-swarm preprint (rejected) |
| 85 | Pages: Parkin, "The Breakthrough Starshot System Model", arXiv 1805.01306v3 (Jul 2018); Chen, Chen, Duan, J. Electromagnetic Waves and Applications 32(9) 1136-1151 (2018) (abstract); Smith, "Viability of a Dyson Swarm as a Form of Dyson Sphere", arXiv 2109.11443 (2021) | thin | Parkin defines tau inversely to the usual form; Chen et al. warn the Goubau formula errs in the near field with non-optimal apertures; Smith is an undergraduate pop-physics preprint (see Rejected sources) |
| 86 | Page: Alhassan, Iqbal, Hu (U. Manitoba), "Constellation-Level Power Allocation for LEO Space-Based Solar Power", arXiv 2606.18416 (2026, IEEE preprint) | useful | Goubau-Brown: tau^2 = A_TX A_RX / (lambda^2 R^2), beam efficiency 1 - exp(-tau^2), citing Goubau and Schwering 1961 and Brown 1984; worked check 200 m and 500 m apertures at 450 km, 2.45 GHz: tau^2 3.30, 96% |
| 87 | Search: `solar power satellite near Sun orbit beamed power to Earth interplanetary distance laser Landis "power beaming" Mercury orbit concept paper` | dead (at the sources) for the target | No published engineering concept for space solar power exported from Mercury or another inner site was found; the only "Mercury orbit" beaming reference surfaced was to fiction. Several NTRS power-beaming items |
| 88 | Page: Landis et al. (NASA GRC), "Laser Power Beaming for Applications on the Moon", Space Power Workshop, 29 Apr-1 May 2025, NTRS 20250003925 (slides, pdftotext) | useful | Commercial 1,070 nm fiber laser about 38% efficient (over 50% demonstrated); matched PV receiver about 50%; beam full divergence 2.44 lambda / D (1.4 m mirror gives 1.86 x 10^-6 rad) |
| 89 | Search: `Lawrence 2013 Science MESSENGER neutron spectrometer Mercury north polar water ice mass 10^16 10^18 g` | thin | Press items only (secondary, not used); no mass figure in results. Died at the query (paper not surfaced) |
| 90 | Search: `Deutsch 2016 Mercury polar ice volume total water ice estimate km3 MESSENGER laser altimeter reflectance Icarus` | useful (leads) | NTRS 20190001152; arXiv 1611.05395 |
| 91 | Page: Eke, Lawrence, Teodoro, "How thick are Mercury's polar water ice deposits?", MNRAS (arXiv 1611.05395, Nov 2016) | useful | Radar-bright deposits (50 +/- 35) m thick; about 10^15 kg of polar water ice (both poles, 10,000 km^2 north-pole radar-bright area); upper limit about 3 x 10^15 kg |
| 92 | API: NTRS 20190001152, Deutsch, Head, Chabot, Neumann, "Constraining the Thickness of Polar Ice Deposits on Mercury ...", Icarus 305 (May 2018) (abstract) | useful | Infill about 41 (+30/-14) m; total polar water ice about 10^14 to 10^15 kg (about 100-1,000 km^3) |
| 93 | Page: NSSDC Venus fact sheet (re-opened, raw HTML) | useful | Mean molecular weight 43.45; H2O 20 ppm, Ar 70 ppm, SO2 150 ppm, CO 17 ppm by volume near the surface |
| 94 | Search: `water propellant electric propulsion in-space demonstration ion thruster water flown JAXA EQUULEUS AQUARIUS or Hall thruster water test performance Isp` | useful (leads) | eoPortal AQT-D; Imperial College news; Wikipedia (not used) |
| 95 | Page: Imperial College London news, "Imperial researchers collaborate to achieve water-fueled satellite engine", 10 May 2023 | useful (thin) | AQUAHET Hall thruster ignited and sustained on water-electrolysis products in the lab; no performance figures given |
| 96 | Page: eoPortal, AQT-D | useful (secondary, quoting the University of Tokyo) | AQUARIUS-1U water resistojet: 4 mN, Isp 70 s, 0.22 mN/W, launched 24 Sep 2019 (to the ISS); no EQUULEUS results in the page |
| 97 | Page: NSSDC Venus fact sheet (third read, raw HTML) | useful | Number of natural satellites 0; average surface temperature 737 K; surface density about 65 kg/m^3 |
| 98 | Search: `Lario 2006 radial dependence solar energetic particle peak intensity fluence Helios r^-2.7 r^-1.9 0.3 AU 1 AU ApJ` | useful (leads) | ESA Solar Orbiter nugget; arXiv 1706.05443 (model, not opened); Lario 2006/2007 summarized (model range R^-3 to R^-1.3 peak, R^-1.5 to R^-0.7 fluence; search summary only, not used) |
| 99 | Page: ESA Solar Orbiter science nugget #55, "Radial dependence of solar energetic particle peak fluxes and fluences", 19 Mar 2025 | useful | Proton peak flux R^-3.7 to R^-2, fluence R^-2.7 to R^-1.4 (10.5-40 MeV; SOHO, PSP 0.05-0.78 AU, Solar Orbiter 0.29-1.01 AU; 2021-2024); steeper at lower energy. Cites "A&A, 965, A25 (2025)" (volume misprinted, see Conflicts) |
| 100 | API: Crossref, DOI 10.1051/0004-6361/202452591 | useful | Cao, Wang, Guo et al., "Radial dependence of solar energetic particle peak fluxes and fluences", A&A 695 (published 27 Feb 2025); 42 events seen by at least two of SOHO, PSP, Solar Orbiter, footpoints within 30 deg. The A&A page itself returned HTTP 403 |
| 101 | Search: `Posner 2007 relativistic electrons forecast solar energetic proton warning time up to one hour Space Weather` | useful (leads) | SwRI release; CCMC slides; press (not used) |
| 102 | Page: SwRI news, 25 May 2007 (Posner, Space Weather, May 2007) | useful | "advance warning up to about one hour"; NASA's Cucinotta: odds of being caught outside a lunar habitat reduced "by more than 20 percent". (The "7 to 74 minutes for 2003" figure in the search summary is not on the page and is not used) |
| 103 | Page: Posner, "Prompt SPEs and the Relativistic Electron Alert System for Exploration (REleASE)", CCMC Community Workshop, 26 Jan 2010 (slides, pdftotext) | useful | 2003-2007 archive: 10 of 11 prompt events forecast, 122 min average warning; overall 79%, 195 min average; 13 false-warning series; fastest-rising event on record (20 Jan 2005) gave 20-25 min of electron precursor |
| 104 | Page: NIST CODATA, proton mass energy equivalent in MeV | useful | 938.272 089 43 MeV (for transit-time arithmetic) |
| 105 | Search: `Little 2011 "Little's Law as Viewed on Its 50th Anniversary" Operations Research L = lambda W pdf MIT` | useful (leads) | INFORMS record; a university-hosted PDF |
| 106 | Page: Little (MIT Sloan), "Little's Law as Viewed on Its 50th Anniversary", Operations Research 59(3) 536-549, 2011 (university-hosted PDF, pdftotext) | useful | "Average Inventory = Average Flow Rate x Average Flow Time" (L = lambda W), stated for operations management |
| 107 | Search: `ISS cargo resupply logistics consumables reserve months contingency NASA OIG commercial resupply report propellant upmass` | useful (leads) | OIG IG-16-025; congressional testimony (not opened) |
| 108 | Page: NASA OIG, "NASA's Response to SpaceX's June 2015 Launch Failure: Impacts on Commercial Resupply of the International Space Station", IG-16-025, 28 Jun 2016 (PDF, pdftotext) | useful | Reserves: food 216 rations (6 crew x 0.8 per day x 45 d), oxygen 290 kg (6 months US segment), water 1,034.5 L (55 d with no regeneration), nitrogen 132 kg; SPX-7 lost 690 kg of crew supplies; FY2015 upmass shortfall 3.48 t, reduced to 2.63 t |
| 109 | Page: Purdue e-Pubs dissertation record AAI10248372, K. M. Hughes, "Gravity-assist trajectories to Venus, Mars, and the ice giants" (abstract) | thin | Venus free-returns and Earth-Mars free-returns with an intermediate Venus flyby; no cycler numbers. Second angle on Venus-as-hub gave nothing quantitative |
| 110 | Search: `Caltech MAPLE space solar power demonstrator wireless power transfer in orbit 2023 results detected on Earth` | useful (leads) | Trade press and Caltech expert page |
| 111 | Search: `caltech.edu news "Space Solar Power Demonstrator Wirelessly Transmits Power in Space" June 2023 MAPLE receivers distance` | thin | Only trade press quoting Caltech: receivers "about a foot away" inside the craft; a beam aimed at Earth was "detected" at Caltech; no power figures. Recorded as secondary |
| 112 | Search (extended): `"Mercury" surface "mass driver" OR "electromagnetic launcher" resource export industrialization concept escape velocity 4.25 km/s paper` | dead (at the sources) | Second angle on [TR]'s logged gap: still no Mercury launcher study; only lunar items, a space-mining blog (secondary, not used) and homework sites (rejected) |
| 113 | Pages: NIST Chemistry WebBook entries for water, argon, carbon monoxide, sulfur dioxide, carbon dioxide (curl; first attempt returned nothing because of a redirect, second succeeded) | useful | Molecular weights 18.0153, 39.948, 28.0101, 64.064, 44.0095 g/mol. **Self-correction:** D13 had first been computed with molar masses typed from memory; replaced by these sourced values (results unchanged at the precision reported) |
| 114 | Search: `orbital atmospheric scoop propellant collection Venus upper atmosphere skimming spacecraft study CO2 collection NASA` | useful (leads) | PHARO (Georgia Tech, 2010); Mars NIAC NTRS 20170002795; Landis Venus ASCEND 2024 (already in [TR]); forums (not used). No Venus scoop study surfaced: died at the sources for Venus |
| 115 | Page: Jones, Masse, Wilhite, Walker et al. (Georgia Tech / NIA), "PHARO - Propellant Harvesting of Atmospheric Resources in Orbit", IEEE Aerospace Conference 2010 (PDF, pdftotext) | thin | Concept and requirement maps for a Mars collector; conclusion text truncated by the two-column extraction; no Venus case. Not used for numbers |
| 116 | Page: Mueller (PI) et al., "Mars Molniya Orbit Atmospheric Resource Mining", NIAC FY16 Phase I Final Report, NTRS 20170002795 (PDF, pdftotext) | useful | 81 scooping passes at 79 km, 3.57-4.5 km/s; about 431 kg of CO2 per pass; 34,939 kg CO2 stored; about 20% becomes O2 (6,986 kg) by solid-oxide electrolysis (ENGINEERING-STUDIED, Phase I) |
| 117 | Snag and self-correction (calculation, not a search): D3 window widths | n/a | The first circular-orbit Lambert scan allowed only transfer angles under 180 deg and gave direction-asymmetric widths; suspected a bug, added long-way transfers, asymmetry persisted. Resolved by reasoning: mirror-plus-time-reversal maps departure dates of A-to-B onto arrival dates of B-to-A, so departure-window widths need not match. Kept, with the basis stated |
| 118 | Snag and self-correction (calculation): D6 sail spiral | n/a | First steering law (maximize energy gain) pumped eccentricity (final e up to 0.65) and gave non-monotonic times; replaced by the fixed 35.26 deg transverse law, which is valid only up to about 0.5 mm/s^2; above that the sourced Hughes figure is used. Earlier output discarded |
| 119 | Snag (calculation): D4 launcher alignment | n/a | The first alignment count ignored the out-of-plane part of the required asymptote (20-35 usable days in 6 yr); adding a near-planar filter cut it to 1.4-5.5 days. Both reported, with the filter stated |

## Findings

Evidence levels: **DEMONSTRATED** (flown or built), **ENGINEERING-STUDIED** (a quantitative design study),
**SPECULATIVE** (concept or thought experiment), **DERIVED** (calculated here from sourced constants; the arithmetic is
in *Derived figures*). The sibling file `space_trucking_and_transport_infrastructure.md` is cited as **[TR]**,
`cyclers_and_large_slow_vehicles.md` as **[CY]**, `industrial_ramp_timelines.md` as **[RM]**. Their tables are cited, not repeated.

### F1. Orbital data, synodic periods, windows and how windows bunch cargo (checklist 1)

**Sourced constants.**

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mean orbital elements, a (au) and e | Mercury 0.38709927, 0.20563593; Venus 0.72333566, 0.00677672; Earth-Moon barycenter 1.00000261, 0.01671123; Mars 1.52371034, 0.09339410. Inclinations to the ecliptic: Mercury 7.005 deg, Venus 3.395 deg, Mars 1.850 deg. Valid 1800 to 2050 AD, with century rates | JPL SSD, "Approximate Positions of the Planets", Table 1, https://ssd.jpl.nasa.gov/planets/approx_pos.html (no revision date on page; read 2026-10-11) | Primary | NSSDC: Mercury perihelion 46.000, aphelion 69.818 (10^6 km), inclination 7.004 deg; Venus inclination 3.395 deg | High |
| Ceres orbit | a = 2.765552595 au, e = 0.0796923, i = 10.588 deg, period 1,679.853 d; GM 62.6284 km^3/s^2; diameter 939.4 km | JPL SBDB API (orbit solution dated 2021-04-13, epoch JD 2461200.5), https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1 | Primary (dataset) | none sought (dataset) | High |
| GM Sun, au, c | 1.32712440041279419 x 10^20 m^3/s^2; 149,597,870,700 m; 299,792,458 m/s | JPL SSD Astrodynamic Parameters, https://ssd.jpl.nasa.gov/astro_par.html | Primary | [TR] F1 uses the same | High |
| Synodic periods with Earth (published) | Mercury 115.88 d; Venus 583.92 d; Mars 779.94 d | NSSDC fact sheets (Mercury and Venus 11 Jan 2024; Mars 19 May 2025) | Primary | DERIVED D1 below reproduces 115.88, 583.93, 779.93 d | High |
| Solar irradiance (mean) | Mercury 9,082.7 W/m^2 (ratio to Earth 6.674); Venus 2,601.3 (1.911); Earth 1,361.0; Mars 586.2 | NSSDC fact sheets (dates as above; Earth 15 Nov 2024) | Primary | ESA "High temperature challenge" says "about 10 times" Earth at Mercury, which is the perihelion value (1/0.3075^2 = 10.6, DERIVED); the mean is 6.67 | High |
| Earth-to-Mercury Hohmann (textbook check) | Earth departure v-infinity 7.533 km/s (C3 56.7 km^2/s^2); Mercury capture burn 7.565 km/s into a parking orbit; total 13.122 km/s from LEO | TU Delft OCW, AE2104 Flight and Orbital Mechanics, lecture slides 11-12, https://ocw.tudelft.nl/wp-content/uploads/AE2104-Orbital-Mechanics-Slides_11_12.pdf (undated course material) | Primary-grade (university course; textbook arithmetic) | DERIVED D1: 7.53 km/s Earth-end, 9.61 km/s Mercury-end v-infinity; capture into a 200 km orbit 7.55 km/s. **See Conflicts C1: [TR]'s v-infinity sum is understated** | High |
| Hollister and Menning Earth-Venus periodic orbits | Ballistic periodic orbits connecting Earth and Venus, "with fairly quick transfers between the two planets", found in the late 1960s; a three-planet (Earth, Venus, Mars) arrangement nearly repeats every 6.4 yr (circular coplanar) and the absolute positions repeat to a few degrees after 32 yr (Earth 32, Venus 52, Mars 17 revolutions per Rall's table) | Rall, "Free-Fall Periodic Orbits Connecting Earth and Mars", MIT Measurement Systems Laboratory, Oct 1969, NTRS 19700017824 (OCR text) | Primary (thesis) | The repeat interval of the Earth-Venus orbits is OCR-garbled ("16" or similar); DERIVED: 5 Earth-Venus synodic periods = 2,919.6 d = 7.99 yr, close to 13 Venus orbits (2,921.1 d), so Earth-Venus geometry repeats about every 8 yr | Medium (OCR) |

**DERIVED D1: synodic periods, Hohmann times and windows per year** (circular coplanar orbits at the JPL mean semimajor
axes; Hohmann transfer).

| Pair | Synodic period (d) | Synodic (yr) | Windows per year | Hohmann transfer time (d) | v-infinity at inner body / outer body (km/s) |
|---|---|---|---|---|---|
| Mercury-Venus | 144.57 | 0.396 | 2.53 | 75.6 | 6.77 / 5.78 |
| Mercury-Earth | 115.88 | 0.317 | 3.15 | 105.5 | 9.61 / 7.53 |
| Mercury-Mars | 100.89 | 0.276 | 3.62 | 170.5 | 12.58 / 8.77 |
| Mercury-Ceres | 92.83 | 0.254 | 3.94 | 361.4 | 15.54 / 9.03 |
| Venus-Earth | 583.93 | 1.599 | 0.63 | 146.1 | 2.71 / 2.50 |
| Venus-Mars | 333.92 | 0.914 | 1.09 | 217.5 | 5.76 / 4.77 |
| Venus-Ceres | 259.40 | 0.710 | 1.41 | 420.8 | 9.07 / 6.38 |
| Earth-Mars | 779.93 | 2.135 | 0.47 | 258.9 | 2.94 / 2.65 |
| Earth-Ceres | 466.74 | 1.278 | 0.78 | 471.8 | 6.31 / 4.86 |
| Mars-Ceres | 1,162.35 | 3.182 | 0.31 | 573.6 | 3.27 / 2.81 |

Mercury's eccentricity matters (D1): a tangential departure from Mercury's **perihelion** (0.3075 au, 58.98 km/s) needs a
v-infinity of 4.65 km/s to Venus, 7.45 to Earth, 10.31 to Mars; from **aphelion** (0.4667 au, 38.86 km/s) it needs 9.21,
12.05 and 15.09 km/s. Leaving from near perihelion saves 4.6 km/s of v-infinity on the Earth route, at the cost of a
higher arrival speed (9.36 vs 6.02 km/s at Earth).

**DERIVED D2: real windows, 2030 to 2035** (3-D zero-revolution Lambert scan on the JPL Table 1 ephemeris, eccentric and
inclined orbits, departure every 2 days, flight time free within the stated range; checked against the Earth-to-Mars Hohmann departure
v-infinity of 2.945 km/s in the TU Delft table: the scan's best 2033 window departs at 2.99 km/s). "Width" is the run of consecutive
departure days whose best total v-infinity is within 10% of that window's minimum.

| Route | Windows in 6 yr | Window-minimum total v-infinity, range (km/s) | Departure v-infinity at the minimum (km/s) | Flight time at the minimum (d) | Width at +10% (d) | Share of time inside a +10% window |
|---|---|---|---|---|---|---|
| Mercury to Earth | 19 | 17.6 to 22.9 | 8.2 to 15.5 | 78 to 134 | 8 to 24 (mean 15) | about 13% |
| Mercury to Venus | 14 | 13.3 to 16.9 | 5.8 to 10.5 | 57 to 103 | 8 to 18 | about 9% |
| Mercury to Mars | 21 | 21.1 to 25.9 | 11.1 to 17.6 | 132 to 228 | 8 to 28 | about 14% |
| Venus to Earth | 3 full | 5.7 to 6.9 | 2.8 to 4.2 | 140 to 175 | 28 to 54 | about 7% |
| Earth to Venus | 4 | 5.9 to 8.1 | 2.5 to 4.8 | 158 to 198 | 36 to 52 | about 8% |
| Venus to Mars | 7 | 11.5 to 12.1 | 5.8 to 7.5 | 170 to 287 | 36 to 46 | about 12% |
| Earth to Mars (validation) | 3 | 5.9 to 6.8 | 3.0 to 3.2 | 197 to 285 | 42 to 60 | about 7% |

**How windows bunch cargo (reading of D1 and D2):**

- **From Mercury, departures cluster into windows about two weeks wide, three times a year to Earth** (every 115.9 d),
  2.5 times a year to Venus and 3.6 times to Mars. A launcher or tug fleet based at Mercury that ships only inside +10%
  windows is idle for about 87% of the year on the Earth route, or must store cargo for up to about 100 days.
- **Window quality cycles with Mercury's eccentricity.** The Mercury-to-Earth window minimum ranges from 17.6 to 22.9 km/s
  of total v-infinity, and the cheap windows recur about once a year (three synodic periods, 347.6 d, is close to four
  Mercury orbits, 351.9 d): in the scan the cheapest windows fall on 6 Feb 2033, 22 Jan 2034 and 5 Jan 2035, each with
  departure v-infinity near 8.2 km/s. A cargo schedule that ships only in the cheap window ships once a year.
- **Windows from the inner, faster body are narrower than windows from the outer body** (D3 in *Derived figures*,
  circular model): Mercury-to-Earth 11 d at +10% against Earth-to-Mercury 50 d; Venus-to-Earth 29 d against Earth-to-Venus
  46 d; Mercury-to-Ceres 14 d against Ceres-to-Mercury open all cycle. Departing the fast body, the target's position is
  the constraint; departing the slow body, a fast target comes round again and a longer or shorter flight time catches it.
  **Inbound cargo from the inner system therefore bunches harder than outbound supply going to it.**
- **Venus is the worst-connected inner node to Earth in time** (one window per 1.6 yr, about a month wide) but the
  cheapest in energy (about 5.7 to 6.9 km/s total v-infinity). Venus-Mars windows recur every 0.91 yr.
- **Earth-Venus geometry repeats about every 8 years** (5 synodic periods, 7.99 yr, D1); Earth-Venus-Mars nearly repeats
  every 6.4 yr and closely after 32 yr (Rall 1969). Any schedule that uses Venus flybys inherits these cycles.

### F2. Gravity-assist routing among the inner bodies (checklist 2)

[TR] F1 already holds MESSENGER (">2213 m/s" propulsive, six flybys, 10.8 years) and the 2014 BepiColombo study case (SEP
4.254 km/s, 1 Earth, 2 Venus and 5 Mercury flybys, 7.5 years). Added here:

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Ballistic (chemical) Earth-to-Mercury route of the Yen type | Launch C3 16 km^2/s^2 (Aug 2005 case); 2 Venus and 2 Mercury swingbys plus 5 deep-space maneuvers; Venus-to-Venus leg 1:1 resonant with Venus; Mercury legs 2:3 and 3:4 resonant; **total flight time 1,517.4 d (4.15 yr)**; Mercury arrival v-infinity **3.37 km/s**; orbit insertion 1,652 m/s (three-impulse sequence); **total delta-v by main engine 2,843 m/s** plus 53 m/s by thrusters; departure mass 1,650 kg of which fuel 1,071 kg (Isp 310 s) (ENGINEERING-STUDIED) | Yamakawa (ISAS), "ISAS Mercury Orbiter Mission Trajectory Design Strategy", ISSFD 1999, https://issfd.org/ISSFD_1999/pdf/IFL_1.pdf | Primary | Explicitly "based on JPL's C.W. Yen's multi-revolution and multiple swingby trajectory"; MESSENGER ([TR] F1) flew a chemical route with six planetary flybys | High for the study case |
| Why Venus flybys are used | "This synchronous Venus swingbys are dedicated to lower the aphelion of the orbit nearly to the radius of Venus's orbit, and the perihelion distance to that of Mercury"; Mercury swingbys with small deep-space maneuvers ("reverse delta-V Mercury gravity assist") lower the Mercury-relative speed, so a "small DSM results in a large saving of Mercury capture delta-V" | Yamakawa 1999 (as above) | Primary | E-sail overview: Mercury probes use flybys "resulting in long transfer times" | High |
| SEP plus flybys, the slow, low-propellant route | Mercury Lander decadal concept: launch 23 Mar 2035, C3 14.7 km^2/s^2 (Falcon Heavy expendable); **1 Earth, 2 Venus, 5 Mercury flybys; arrives at Mercury with v-infinity 0 km/s on 13 Jan 2045 (117.5 months)**; flyby v-infinity 3.85 (Earth), 7.42 and 7.53 (Venus), 5.9, 5.17, 3.91, 3.62, 2.51 km/s (Mercury); **cruise xenon 484 kg (513 kg with contingency)**; cruise-stage delta-v budget 2 km/s; two NEXT-C engines; cruise array 9.3 kW BOL at 0.99 AU for SEP; total launch mass 9,410 kg; margins: 90% duty cycle, 10% power, 6% propellant; thrust-Sun angle held within plus or minus 10 deg (ENGINEERING-STUDIED) | NASA (APL-led), "Mercury Lander: Planetary Mission Concept Study for the 2023-2032 Decadal Survey", 2021, arXiv 2107.06795, Exhibits 23-26 (cites Shannon et al. 2020 for the trajectory) | Primary | BepiColombo study ([TR]): 4.25 km/s SEP, 7.5 yr. Backup 2036 launch: 105.5 months, 514 kg xenon | High as a study |
| Solar sail, no flybys (comparison) | Outbound Earth to Mercury 2.85 yr at characteristic acceleration 0.25 mm/s^2, C3 = 0; return Mercury escape to Earth (v-infinity 0) **369 d** at 0.78 mm/s^2; "Lengthy multiple gravity assists are not required, and the launch window is always open in principle", though "minimum time launch opportunities occur once every year" and launch date changes trip time by up to 300 d; a Venus gravity assist "could reduce the outbound trip time by 140 days"; ballistic direct transfer to low Mercury orbit "of order 13 km/s" (ENGINEERING-STUDIED) | Hughes, Macdonald, McInnes, Lyngvi, Falkner, Atzei, "Analysis of a Solar Sail Mercury Sample Return Mission", IAC 2004 (ESA-hosted PDF); journal version J. Spacecraft and Rockets 43(4) 828-835, 2006 | Primary | The same paper reports a NASA/JPL Team X SEP sample return at 5,775 kg launch mass and 6.9 yr, and an ESA chemical/SEP concept at 6,500 kg and 7.2 yr (secondary for those two; their reports were not opened) | Medium-high |
| Venus-including Earth-Mars cyclers | Ballistic "triple cyclers" with at least one Venus flyby; "numerous solutions ... with average transit leg excess speed below 5 kilometers per second, independent of encounter epoch"; energy "lower than previously documented cyclers not involving Venus, but the repeat periods are generally longer" (ENGINEERING-STUDIED) | Jones, Hernandez, Jesick (JPL), "Low Excess Speed Triple Cyclers of Venus, Earth, and Mars", AAS/AIAA Astrodynamics Specialist Conf., Aug 2017, NTRS 20190028464 (abstract only) | Primary (abstract) | [CY] A: Earth-Mars cycler Earth v-infinity 2.8 to 8.0 km/s | Medium (no numbers beyond the abstract) |
| Earth-Venus periodic orbits | Found by Hollister and Menning (MIT, late 1960s): ballistic periodic orbits with direct returns at both planets and "fairly quick transfers" between them | Rall 1969 (NTRS 19700017824) | Primary (thesis, secondary account of the Hollister and Menning result) | Hollister's and Menning's own papers not opened (Open threads) | Medium |

**Reading (route trade, flybys versus direct, all figures sourced above or in [TR]):**

| Route from low Mercury orbit (or to it) | Propulsive delta-v | Time | Status |
|---|---|---|---|
| Direct impulsive Hohmann, low Mercury orbit to Earth-crossing transfer | 7.55 km/s departure, plus 5.54 km/s capture into low Earth orbit or aerocapture ([TR] D1) | 105 d | DERIVED |
| Direct low-thrust spiral, Mercury low orbit to Earth vicinity at C3 = 0 | about 22.4 km/s (Edelbaum, D5) | loaded leg about 1.2 to 5.2 yr for payloads of 0.5 to 2 times the tug's dry mass, depending on power (D7) | DERIVED |
| Chemical with Venus and Mercury flybys (Yen type, reversed in direction) | about 2.8 km/s total in the Earth-to-Mercury direction | about 4.2 yr | ENGINEERING-STUDIED (outbound only) |
| SEP with 1 Earth, 2 Venus, 5 Mercury flybys | about 2 km/s of SEP plus launch C3 14.7 | about 9 to 10 yr | ENGINEERING-STUDIED (outbound only) |
| Solar sail, no flybys | none (propellantless) | 369 d at 0.78 mm/s^2; 2.85 yr at 0.25 mm/s^2 | ENGINEERING-STUDIED |

**Flyby routes buy delta-v with years.** Every primary source found studies the **Earth-to-Mercury** direction. A
ballistic trajectory run backward in time is also a valid trajectory, so the same sequences exist for Mercury-to-Earth
cargo, and they would arrive at Earth with the v-infinity at which the outbound craft departed (3.8 to 4.0 km/s in these
cases; C3 14.7 to 16 km^2/s^2). **No study of Mercury-to-Earth or Mercury-to-Venus cargo routing with flybys was found**
(Open threads). Each flyby sequence is tied to specific planetary alignments (resonant Venus and Mercury legs), so a
flyby route is a schedule, not a lane: a fleet using one ships in convoys fixed by the alignment.

### F3. Propulsion performance versus distance from the Sun (checklist 3)

**Solar-electric: sunlight rises as 1/r^2, usable power does not.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| BepiColombo T6 ion thruster at full thrust (flight-qualification configuration) | Power < 4.7 kW; thrust 145.0 mN; Isp 3,875 s; beam current 2.167 A; xenon flow 3.802 mg/s; qualified at 145 mN, **life-tested at 125 mN, "the final nominal SEPS flight configuration"**; four thrusters on the transfer module (DEMONSTRATED in flight) | Filleul, Sutherland, Cipriani, Charles, Frontiers in Space Technologies 2:639819, 11 Mar 2021, Table 1 and Sec. 2 | Primary (peer-reviewed) | Steiger et al. EUCASS 2019: "max thrust 145 mN" | High |
| BepiColombo transfer-module arrays | Two 14 m arrays, over 40 m^2 of cells, supplying the propulsion system "(≤11kW)"; Sun aspect angle held within 13 to 23 deg for thermal reasons | Filleul et al. 2021 | Primary | ESA "High temperature challenge": 42 m^2; Steiger et al. 2019: "up to 11 kW", "over 40 m2" | High |
| **Array off-pointing near the Sun (flight operations)** | "Despite approaching the Sun, the mission is highly power-constrained"; "above 0.62 AU distance, there are no constraints, while below that distance significant offpointing of the array may be required"; "the power available generally does not allow firing the thrusters at the max thrust level they're capable of"; array backside illumination "becomes critical at Sun distance below 0.7 AU"; thrust level changed gradually "due to the change of distance to the Sun, limiting the maximum power available" (DEMONSTRATED) | Steiger, Altay, Montagnon, Budnik, Casasco, Espeillac, Fugger, Strandberg (ESA/ESOC, Terma, ESA/ESTEC, Airbus), "GNC Operations for the BepiColombo Mission to Mercury: First In-flight Experience", EUCASS 2019, DOI 10.13009/EUCASS2019-218, Sec. 4.4 | Primary | JPL D-101316 (next row) | High |
| Why: hot arrays | MESSENGER (designed for 0.31 AU) replaced "a significant fraction of the solar cells" with optical solar reflectors ("about 2/3-cell coverage" as printed) and off-pointed its arrays; "the nominal operating temperature was ~130°C, compared with 40 to 70°C that is typical at 1 AU"; BepiColombo arrays rated to 190 C and mix cells with reflectors; cell temperature coefficient about -0.22 to -0.23% of maximum power per C; Mercury missions face "1000-14000 W/m2" and "~270°C" | JPL, "Solar Power Technologies for Future Planetary Science Missions", JPL D-101316, Dec 2017, Secs. 2 and 3.3 | Primary | Steiger 2019 | High. The printed "2/3-cell coverage" may mean two thirds of the area is cells or reflectors; the text says "a significant fraction" was replaced (ambiguous, see Conflicts C3) |
| A 2024 power fault | In April 2024 the transfer module "stopped delivering enough electrical power"; cause "unexpected electric currents between MTM's solar array and the unit responsible for extracting power"; thrusters remain "below the minimum thrust required for an insertion into orbit around Mercury in December 2025"; new arrival November 2026; a closer fourth Mercury flyby (165 km) recovered part of the shortfall (DEMONSTRATED, as an anomaly) | ESA, "Fourth Mercury flyby begins BepiColombo's new trajectory", 2 Sep 2024 | Primary | INAF Media, 27 May 2024, quoting ESA's E. Montagnon: thrust at about 90% of plan (secondary) | High |
| SEP at Mercury itself | For the Mercury Lander orbit phase, SEP was rejected: "the specific acceleration provided by the SEP system was too small even at the highest power settings", and "the spacecraft thrust angle constraint required to maintain thermal shielding in the Sun direction significantly reduces the feasible thrust durations ... and adds years to the total mission duration"; cruise thrust-Sun angle held within plus or minus 10 deg (ENGINEERING-STUDIED) | Mercury Lander decadal study 2021 (arXiv 2107.06795), pp. 18-19 | Primary | Steiger 2019 | High |
| Low-thrust delta-v between circular orbits (method) | Edelbaum: delta-v = sqrt(V1^2 - 2 V1 V2 cos[(pi/2) delta-theta] + V2^2) for a tilt delta-theta (rad) between circular orbits of speeds V1, V2; delta-v = V1 + V2 if delta-theta > 2 rad | Choi and Ho (Georgia Tech), arXiv 2502.15914v2 (25 Aug 2025), Eq. 6, citing Edelbaum, ARS J. 31(8), 1961 and Kechichian, JGCD 20(5), 1997 | Primary (preprint stating a standard result) | DERIVED D5: 19.48 km/s from Mercury's orbit to Earth's with the 7.005 deg tilt; 18.09 km/s coplanar | High |

**Photon sails near the Sun.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Radiation pressure and lightness number | A perfect reflector facing the Sun at 1 AU feels "just 9.1 µPa"; lightness number lambda = a/g is independent of distance because both fall as 1/r^2; lambda = 1 at a mass per area of 1.5 x 10^-3 kg/m^2 ("about ten times less than plastic food wrap"); solar gravity at 1 AU 5.9 x 10^-3 m/s^2; IKAROS lambda "below 0.01"; LightSail 2 (32 m^2, 5 kg) about 0.01 | Bailer-Jones (MPIA), "The Sun Diver: Combining solar sails with the Oberth effect", Am. J. Phys. (accepted 26 Sep 2020), arXiv 2009.12659 | Primary (peer-reviewed) | [TR] F2: IKAROS 1.12 mN measured on about 196 m^2 = 5.7 µN/m^2; Hughes et al.: 0.588 N on 75,625 m^2 = 7.78 µN/m^2 at 0.85 reflective efficiency (DERIVED from their Table 5 and launch mass) | High |
| Mercury sail point design | 275 x 275 m square (75,625 m^2), sail assembly loading 5.9 g/m^2 (with 40% contingency), sail mass 448 kg, 2 µm CP1 film with coilable booms, reflective efficiency 0.85; characteristic acceleration 0.25 mm/s^2 at Earth departure (2,353 kg launch mass), 0.7367 during sample acquisition, 0.7839 mm/s^2 at Mercury departure; Mercury capture spiral 28 d; escape spiral 16 d; **sail film temperature at most 443.7 K on the trajectory and 494.5 K "face on to the Sun at Mercury perihelion", below "the predicted 520 K upper limit of polyimide films"** (ENGINEERING-STUDIED) | Hughes et al. IAC 2004 / JSR 2006 (as F2) | Primary | DERIVED: 2,353 kg x 0.25 / 0.7839 = 750 kg at Mercury departure (448 kg sail, about 300 kg everything else) | Medium-high |
| Largest sails made | Flown in deep space: IKAROS 196 m^2; in Earth orbit: ACS3 80 m^2 ([TR] F2). Solar Cruiser (1,653 m^2, 2.5 µm film, 95 kg craft) completed ground development but "was not confirmed for flight"; a Solar Polar Imager would need "approximately 7000 square-meters" | Johnson et al., NTRS 20220011260 (2022); Clements et al., NTRS 20210000631 (Jan 2021) | Primary | [TR] F2 | High |

**Electric solar-wind sail (unflown).** Thrust falls about as 1/r, not 1/r^2 ("the effective area of the sail is
proportional to the electron sheath width ... which scales similarly to the plasma Debye length ... as ~r"), so it gains
less than a photon sail near the Sun, and the electron-gun power it needs "increases as the inverse square of the
distance" while hot solar panels lose efficiency; aluminum tethers "do not necessarily tolerate the high temperature
encountered on a Mercury mission"; claimed Mercury rendezvous "in less than one year" each way (Janhunen et al.,
arXiv 1404.5815, 2014; SPECULATIVE: the only flight test, ESTCube-1, failed to deploy its tether, [TR] F2).

**DERIVED D6 (sail transfer time, circle to circle, Mercury's orbit to 1 AU).** A planar ideal-sail integration with
the transverse-thrust-maximizing cone angle (35.26 deg) gives, for low characteristic accelerations where the orbit stays
near-circular: 0.10 mm/s^2, 2,281 d outward and 2,290 d inward; 0.25 mm/s^2, 912 d and 934 d; 0.50 mm/s^2, 467 d and
484 d (final eccentricity 0.04 to 0.10). The product (time x a_c) is nearly constant, **about 230 d x mm/s^2**. Check:
Hughes et al.'s optimized Earth-to-Mercury leg at 0.25 mm/s^2 took 2.85 yr (1,041 d) including launch-date and
rendezvous constraints, against 934 d here. Above about 0.7 mm/s^2 this simple steering law no longer gives a
circular arrival (eccentricity 0.2 to 0.6), so the optimized 369 d at 0.78 mm/s^2 (Hughes) is used instead.

**What a tug or sail convoy from Mercury orbit to Earth would take (sourced rates, D5 to D7):**

- **SEP tug, direct spiral:** about 22.4 km/s each way (2.9 km/s Mercury escape spiral plus 19.5 km/s heliocentric).
  With AEPS-class Isp 2,890 s, 0.67 thruster efficiency and a 68 kg/kW all-in tug, a tug carrying twice its own dry
  mass takes about 1,890 d loaded and 630 d back empty if its power stays at the 1-AU value (the BepiColombo-like
  thermal limit), or 857 d and 322 d if power rises as 1/r^2 up to a cap at 0.62 AU. Propellant is about 2.4 t per
  metric ton delivered for the round trip (D7).
- **SEP with flybys:** about 2 km/s of SEP and about 9 to 10 years per one-way leg (Mercury Lander, reversed).
- **Photon sail:** 369 d at 0.78 mm/s^2 (Hughes; about 300 kg carried by a 448 kg sail); the empty return at the sail's
  own 1.32 mm/s^2 (7.78/5.9) is beyond the range where D6 is valid; at the D6 scaling it would be about 180 d.

### F4. Launch from airless, low-gravity bodies: a launcher on Mercury (checklist 4)

**Anchors (sourced).** The lunar point designs are in [TR] F2 and F6 (SP-428 III-3: 2,400 m/s, 1,000 g, 488 m, 125 MW,
650,000 t/yr, 3,130 t machine; SP-413: about 10 km track, 288 m/s^2) and [TR] F4 (SP-413 catcher, 200 m/s arrivals).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mercury constants for a launcher | GM 0.022032 x 10^6 km^3/s^2; mean radius 2,439.7 km; escape speed 4.3 km/s (DERIVED 4.250); sidereal rotation 1,407.6 h (58.65 d); solar day 4,222.6 h (175.9 d); obliquity 0.034 deg; sunward surface 590 to 725 K; total atmosphere "<~10000 kg" | NSSDC Mercury fact sheet (11 Jan 2024) | Primary | DERIVED equatorial rotation speed 3.0 m/s (no useful launch assist) | High |
| Lunar quenchgun (second lunar anchor) | Superconducting quenchgun launching "1-ton containers of liquid oxygen, one every 2 hours", "nearly 4400 tons ... into low lunar orbit in a year"; energy from "locally supplied, solar- or nuclear-generated electrical power" (ENGINEERING-STUDIED) | Snow and Kolm, "Electromagnetic launch of lunar material", in NASA JSC "Space Resources", Vol. 2, 1992, NTRS 19930007725 (abstract) | Primary (abstract) | SP-428 III-3 ([TR]) | Medium |
| Coilgun to Mercury-class speeds (ground design) | A coilgun "designed to accelerate a 14-kg mass to 6 km/s and, by adding additional equipment, to accelerate a 10-kg mass to 11 km/s"; railgun version 14 kg to 6 km/s (ENGINEERING-STUDIED, for NASA Langley hypervelocity testing; not built at these figures as far as found) | Schroeder, Gully, Driga, "Electromagnetic launchers for space applications", IEEE Trans. Magnetics 25 (1989), NTRS 19890044698 (abstract) | Primary (abstract) | none | Medium (design only) |
| Rotating tether limits | Characteristic velocity = sqrt(design strength / density); "most metals and fibers is around 1 km/s"; commercial fibers to "4 km/s" when design strength is 60% of fiber strength; Spectra 2000 at safety factor 2 "would require a tether massing approximately 80 times the payload mass" for the 3.3 km/s lunar-transfer throw described there (ENGINEERING-STUDIED) | Hoyt and Forward, US Patent 6,386,484 B1 (priority 8 Sep 2000, issued 14 May 2002), Google Patents text | Primary (patent) | [TR] F2 MXER: about 75% of Earth escape delta-v, 2 g tip; [CY] E: 110 km MXER tether, 172 to 345 MPa | Medium (the 80x figure's exact basis is not restated in the passage) |
| Planet-scale launching (thought experiment) | Lifting 1 kg to escape on Mercury "requires about nine mega-joules"; with 1/10 of captured solar energy spent on launching, a 1 km^2 seed array and a 5-yr processing lag, the authors' model disassembles Mercury in "31 years and 85 days" (SPECULATIVE; exponential self-replication assumed, no engineering design) | Armstrong and Sandberg, "Eternity in six hours", Acta Astronautica 89 (2013) 1-13 (preprint via Internet Archive) | Primary (peer-reviewed thought experiment) | DERIVED 9.03 MJ/kg ([TR] D5) | Low as an engineering estimate; recorded so it is not mistaken for one |

**DERIVED D4 (what a Mercury launcher must do; arithmetic in *Derived figures*):**

| Launch target from Mercury's surface | Muzzle speed (km/s) | Kinetic energy (MJ/kg) | Energy vs the lunar 2.4 km/s launcher | Acceleration length at 1,000 g (m) | SP-428 machine mass scaled by v^2 (kt) |
|---|---|---|---|---|---|
| Escape (v-infinity 0) | 4.25 | 9.0 | 3.1 x | 921 | 9.8 |
| Venus transfer, best window (v-infinity 6.08) | 7.42 | 27.5 | 9.6 x | 2,806 | n/a |
| Earth transfer, Hohmann (v-infinity 9.61) | 10.51 | 55.2 | 19.2 x | 5,630 | 60.0 |
| Earth transfer, cheapest 2030-2035 window (8.15) | 9.19 | 42.2 | 14.7 x | 4,307 | n/a |
| Mars transfer, best window (11.05) | 11.84 | 70.1 | 24.3 x | 7,146 | n/a |

- **Best launch direction:** along Mercury's orbital velocity for outbound transfers. In the 2030-2035 scan the
  needed asymptote lay within about plus or minus 50 to 60 deg of that direction (median within 2 to 4 deg), and a
  horizontal launch must leave from a point about 91 to 102 deg behind the outgoing asymptote (the hyperbola's turn).
- **Out-of-plane need:** because Mercury's orbit is tilted 7.0 deg to Earth's, the departure asymptote inside a +10%
  window was a median 26 deg out of Mercury's orbital plane for Earth, 19 deg for Venus and 22 deg for Mars; only about
  9% (Earth), 9% (Venus) and 8% (Mars) of window days needed less than 5 deg. For Earth and Venus the
  near-planar days include the cheapest windows of the scan; for Mars the cheapest near-planar window (21.5 km/s) is
  2% above the overall minimum (21.1 km/s).
- **Rotation does not aim it.** A fixed track turns with the planet once per 58.65 d, while the required asymptote
  turns once per orbit (87.97 d); the alignment repeats every solar day (175.9 d). For the best-placed fixed equatorial
  track, 2030-2035, with plus or minus 5 deg tolerance: **20 d (one-way track) or 35 d (two-way track) of usable launch
  time in 6 years to Earth (18 opportunities) if any asymptote declination were acceptable, and 2.4 d in 6 years
  once the asymptote must lie within 5 deg of the orbit plane.** Venus: 5.5 d; Mars: 1.4 d (two-way track).
- **What scales and what does not:** energy per kilogram scales with v^2 (3 to 24 times the lunar design); track
  length at fixed acceleration scales with v^2; the per-shot release accuracy needed for a long ballistic flight to
  another planet is not given by any source found; the catcher's job grows with arrival speed (the SP-413 catcher took
  200 m/s; a direct Mercury-to-Earth throw arrives at 6.5 to 11 km/s v-infinity, D2). **Nothing in the sources supports a
  surface launcher throwing cargo directly to Earth or Venus.** What the numbers support is a launcher to Mercury escape
  or Mercury orbit (4.25 km/s, about 9 MJ/kg, any time and any direction relative to a catcher in orbit), with a separate
  heliocentric carrier (tug or sail) for the long leg.
- **A rotating tether to pick cargo off the surface** would need a tip speed near low-orbit speed (3.0 km/s at the
  surface, DERIVED), the same class as the 3.3 km/s lunar-transfer case in the patent, where a Spectra tether masses
  about 80 times its payload.
- **Mercury's Hill sphere radius is about 221,000 km** (DERIVED from the GM ratio), so Sun-Mercury L1 and L2 sit that far
  out and move with Mercury's eccentric orbit; a catcher there is in a weak, perturbed regime (no study found).

### F5. Capture and delivery at the destination (checklist 5)

[TR] F4 holds the SP-413 mass catcher (L2, 200 m/s arrivals, 0.32 Mt/yr per catcher, 5 catchers for 11 Mt in 10 yr), the
momentum-exchange tether, aerobraking history (Magellan, MRO 400 passes) and the 2016 aerocapture assessment. Added:

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Venus aerocapture point design | Entry 11.25 km/s at 150 km, flight path -6.12 deg; **about 4,300 m/s removed in one pass**, then 99 m/s to circularize at 300 km; 1,090 kg vehicle, ballistic coefficient 138 kg/m^2; **delivered to orbit 687 kg, against 374 kg by chemical insertion plus aerobraking (122 d and 670 orbits) and 111.5 kg all-chemical**; aeroshell taken as 30% of launch mass; peak heating 500-600 W/cm^2 convective plus 500-700 W/cm^2 radiative; heat load about 55 kJ/cm^2; **corridor width plus or minus 0.76 deg**; "No tile system has ever been subjected to the heating levels predicted" (ENGINEERING-STUDIED) | Lockwood, Starr et al., NASA/TM-2006-214291, March 2006, NTRS 20060010899 | Primary | Girija 2023 (next row) | High as a study |
| Why Venus is hard to aim at | Density scale height: Venus 3.5-4.7 km, Earth 8.4 km, Mars 6.4-8.2 km; "small changes in altitude can result in large changes in atmospheric density which ... will result in very narrow entry corridor widths" | Lockwood et al. 2006 | Primary | none sought | High |
| Benefit by destination | Drag-modulation aerocapture vs propulsive insertion to a 400 km circular orbit: delivered-mass gain **Venus 92%, Earth 108%, Mars 17%**; replaces insertion delta-v of 3,533 m/s (Venus, v-infinity 3.5 km/s), 3,731 m/s (Earth, 3.5 km/s), 2,079 m/s (Mars, 2.6 km/s); at Venus "only 25% of the arrival mass" reaches orbit propulsively vs about 50% with aerocapture (ENGINEERING-STUDIED) | Girija (Purdue), arXiv 2309.09438 (2023 preprint) | Primary (preprint) | Lockwood 2006 (Venus, 6.2 x delivered mass vs all-chemical at that v-infinity) | Medium-high |
| Flight status | Single-pass aerocapture "unproven operationally" (2006); "has yet to be implemented on a space flight mission" (2016, [TR] F4); NASA solicited industry for ARRIVAL, an Earth-orbit aerocapture demonstrator with a 1 m aeroshell, in June 2025 (trade press) | Lockwood 2006; Spilker 2016 via [TR]; Military and Aerospace Electronics, 27 Jun 2025 | Primary / secondary | No flown aerocapture found | High that it had not flown by mid-2025 |

**DERIVED D8 (what the arrival speeds of F1 mean at each destination).** Impulsive capture from the arrival
v-infinity of the D2 windows (Oberth effect included; low orbit 400 km at Earth, 300 km at Venus and Mars) and the
speed at an atmospheric entry interface (125 km Earth and Mars, 150 km Venus; an assumed altitude):

| Destination, arriving from | Arrival v-infinity (km/s) | Capture to low circular orbit (km/s) | Capture to a high ellipse (km/s) | Entry speed for aerocapture (km/s) |
|---|---|---|---|---|
| Earth, from Mercury (cheapest windows) | 9.45 | 6.72 | 3.63 (apogee 384,400 km) | 14.6 |
| Earth, from Mercury (best arrival end) | 6.55 | 5.00 | 1.92 | 12.9 |
| Earth, by a flyby route (reversed outbound) | 3.8 | 3.82 | 0.74 | 11.7 |
| Venus, from Mercury | 4.98 to 9.05 | 4.12 to 6.42 | n/a | 11.4 to 13.7 |
| Venus, from Earth (D1 Hohmann) | 2.70 | 3.32 | n/a | 10.6 |
| Mars, from Mercury | 8.15 to 11.65 | 6.06 to 9.20 | 5.04 to 8.18 (apoapsis 20,000 km) | 9.5 to 12.7 |
| Mars, from Earth (D1 Hohmann) | 2.65 | 2.09 | 1.07 | 5.6 |

**Reading:**

- **Fast inner-system cargo arrives fast.** Direct Mercury-to-Earth cargo meets Earth at 6.5 to 11 km/s v-infinity and
  would need 5 to 7 km/s to stop in low orbit, or an aerocapture at 13 to 15 km/s entry speed, faster than the one
  Venus design studied (11.25 km/s), which already exceeded any tested tile system. The catcher designs found handle
  200 m/s.
- **Slow routes arrive slow.** A flyby or spiral route that ends near v-infinity 0 to 4 km/s needs 0 to 0.8 km/s to
  enter a high Earth ellipse. The cost of a cheap arrival is the years spent on flybys or spirals (F2, F3).
- **Venus is the easiest place in the inner system to stop something** (the 92% to 6x delivered-mass gains above),
  but the hardest corridor to hit (plus or minus 0.76 deg) and the hottest entry. What is caught in low Venus orbit is still
  about 3.3 km/s (Hohmann departure from 300 km, D1) from
  leaving for Earth.
- **The destination processing node.** No study found sizes a receiving and processing node for bulk inner-system
  cargo (Open threads). [TR] F4 and [CY] G give the only node concepts found: the SP-413 catcher (220 t, about 2,000 N
  stream force), cycler "Spaceports" at lunar-orbit radius and Phobos-orbit radius, and propellant depots.

### F6. Fleet and infrastructure sizes for stated flows, Mercury orbit to Earth (checklist 6)

No study was found that sizes any fleet for Mercury-to-Earth cargo ([TR] F7 reached the same result). Everything below
is **DERIVED** (D5, D7, D9 in *Derived figures*) from the sourced rates in F2, F3 and F4 and from [TR]. Basis common to
all rows: destination is Earth vicinity at C3 about 0 (a high orbit or Earth-Moon Lagrange region; F5 gives the extra cost
of going lower); 1 kt = 1,000 t. "In transit" is flow x loaded trip time (cargo that exists but is not yet delivered).

**(a) Solar-electric tugs, direct spiral (22.4 km/s each way; AEPS-class Isp 2,890 s, thruster efficiency 0.67, 90% duty,
tug dry mass 68 kg per kW, cargo per trip = 2 x tug dry mass, refueled at both ends; 100 kW tugs, each 6.8 t dry carrying
13.6 t).** Two power assumptions bracket the BepiColombo experience (F3): power flat at its 1-AU value, or rising as 1/r^2
and capped at 0.62 AU (2.6 times).

| Flow | Power case | Thruster power | Tugs of 100 kW | Round-trip cycle | Propellant per year (2.4 t per t delivered) | Cargo in transit |
|---|---|---|---|---|---|---|
| 1 kt/yr | flat | 53 MW | about 530 | 2,550 d | 2,400 t | about 5,200 t |
| 1 kt/yr | capped 1/r^2 | 24 MW | about 240 | 1,209 d | 2,400 t | about 2,300 t |
| 100 kt/yr | flat | 5.3 GW | about 53,000 | 2,550 d | 240,000 t | about 520,000 t |
| 100 kt/yr | capped 1/r^2 | 2.4 GW | about 24,000 | 1,209 d | 240,000 t | about 230,000 t |
| 1 Mt/yr | flat | 53 GW | about 530,000 | 2,550 d | 2.4 Mt | about 5.2 Mt |
| 1 Mt/yr | capped 1/r^2 | 24 GW | about 240,000 | 1,209 d | 2.4 Mt | about 2.3 Mt |

Productivity is 0.019 to 0.041 t of cargo per kW-year, against 0.279 t per kW-year for the 3.4 km/s lunar leg in [TR] D3:
**the Mercury leg is 7 to 15 times worse per kilowatt**, and its propellant demand (2.4 t per t delivered) is 13 times
[TR]'s 0.18 t per t. **Even 1 kt/yr needs about 2,400 t/yr of propellant, about 37 times the world's xenon output (about
65 t/yr, [TR] F3).**

**(a') Solar-electric with flybys (one-way stages modeled on the Mercury Lander cruise stage: about 7.7 t delivered per
9.3 kW stage (orbital 3,764 + descent 3,231 + lander 723 kg), 117.5 months, 484 kg xenon; assumes the outbound trajectory run in reverse is available as often as needed,
which F2 says it is not).**

| Flow | Stages per year | Array power built per year | Xenon per year | Cargo in transit |
|---|---|---|---|---|
| 1 kt/yr | about 130 | 1.2 MW | about 63 t (about one year of world output) | about 9,800 t |
| 100 kt/yr | about 13,000 | 121 MW | about 6,300 t | about 980,000 t |
| 1 Mt/yr | about 130,000 | 1.2 GW | about 63,000 t | about 9.8 Mt |

Propellant falls by a factor of about 38, but **ten years of cargo is always in flight**, and the flyby alignments
(F2) mean the stages leave in batches, not continuously.

**(b) Mass driver on Mercury's surface plus catcher.** A surface launcher cannot throw directly to Earth on any useful
schedule (F4: 2.4 d of usable time in 6 years for a fixed track). What it can do is lift cargo to Mercury escape
(4.25 km/s, 9.03 MJ/kg), where a catcher hands it to a heliocentric carrier. This replaces only the 2.9 km/s Mercury escape
spiral (13% of the 22.4 km/s) or, for sails, the 16-day escape spiral.

| Flow | Launcher jet power (100% duty) | Electrical power at the SP-428 efficiency 96.4% (100% duty / SP-428 duty of 179 d per yr) | SP-413-class catchers (0.32 Mt/yr each, 100% duty) |
|---|---|---|---|
| 1 kt/yr | 0.29 MW | 0.30 / 0.59 MW | 0.003 (one small catcher) |
| 100 kt/yr | 29 MW | 30 / 59 MW | 0.31 |
| 1 Mt/yr | 286 MW | 297 / 594 MW | 3.1 (SP-413 installed 5 for 3.5 operating) |

A launcher scaled from SP-428 by v^2 at the same 42 kg/s (650 kt/yr if fired 179 d a year) would be about 9.8 kt and
about 920 m of acceleration track at 1,000 g (F4). Night on Mercury's surface lasts half of a 175.9-day solar day, so
continuous launching from one equatorial site needs about 88 days of energy storage or power from elsewhere
(DERIVED from the NSSDC day length).

**(c) Photon-sail convoys (Hughes sail technology: 5.9 g/m^2 assembly, 7.78 µN/m^2 at 1 AU; trip time about 230 d /
a_c from D6; 30 d dwell per round trip; no wait for phasing, which Hughes found can add up to 300 d).**

| Cargo loading | Loaded a_c / empty a_c (mm/s^2) | Out / back (d) | 1 kt/yr: sail area, sail mass | 100 kt/yr | 1 Mt/yr | Cargo in transit at 1 Mt/yr |
|---|---|---|---|---|---|---|
| 4.07 g/m^2 (as in Hughes' return leg) | 0.78 / 1.32 | 295 / 174 | 336 km^2, 2,000 t | 33,600 km^2, 198,000 t | 336,000 km^2, 2.0 Mt | 0.8 Mt |
| 10 g/m^2 | 0.49 / 1.32 | 470 / 174 | 185 km^2, 1,100 t | 18,500 km^2, 109,000 t | 185,000 km^2, 1.1 Mt | 1.3 Mt |
| 20 g/m^2 | 0.30 / 1.32 | 766 / 174 | 133 km^2, 780 t | 13,300 km^2, 78,000 t | 133,000 km^2, 0.78 Mt | 2.1 Mt |

At 1 Mt/yr that is 1.8 to 4.4 million sails the size of Hughes' 75,625 m^2 design. **Sails need no propellant, but the
sail fleet's own mass is of the same order as one year's cargo**, so the question that decides sail convoys is sail
lifetime in the Mercury-orbit environment, which no source found gives (Open threads). For scale, the largest sail ever
flown in deep space is 196 m^2 (F3).

**Venus cloud-level cargo to Earth or Mars orbit.** [TR] F1b gives the only figures: about 9 km/s to orbit from a balloon
at 60 to 67 km; 1,800 kg ascent vehicle for a 10 kg canister (0.55%); CO/O2 propellant from atmospheric CO2 at 250 s.
DERIVED: an ideal single stage (no structure at all) burning CO/O2 at 250 s would be 97.5% propellant for 9 km/s, and
86.9% even at the RS-25's 452.3 s. At the NIAC study's 0.55% payload fraction, **1 kt/yr of Venus cloud cargo means about
180 kt/yr of ascent vehicles and propellant lifted from balloon altitude**; 1 Mt/yr means about 180 Mt/yr. The figures in
[TR] do not support anything larger than sample-return scale; the Venus-orbit-to-Earth leg itself is cheap (Hohmann
v-infinity 2.71 out, 2.50 in, D1).

### F7. Communications and navigation across the inner system (checklist 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Deep Space Network size and load | Three complexes (Goldstone, Madrid, Canberra), each with one 70 m antenna and several 34 m antennas; supports "nearly 60" missions; **about 77,000 antenna utilization hours in FY 2022**; "demand exceeding supply at times by as much as 40 percent", excess demand "about 50 percent by the 2030s"; missions received 8,500 to 15,000 fewer hours than requested in each of the past 5 years; Artemis I used "more than 900 hours" in a 25-day mission; expansion plan cost rose from $419 M to $706 M, full antennas not before 2029 (DEMONSTRATED operations) | NASA OIG, "Audit of NASA's Deep Space Network", IG-23-016, 12 Jul 2023 | Primary | none sought | High |
| Tracking load of one electric-propulsion cruise | BepiColombo thrust arcs: one weekly "navigation pass" (thrusting stopped for radiometric tracking) plus "two ground station contacts ... per week to monitor S/C status" | Steiger et al., EUCASS 2019 | Primary | none | High for that mission |
| Solar-conjunction link limits | X-band: good data above a Sun-Earth-probe angle of about 2.3 deg (NEAR test; 99.7-100% frames at 2.3-3.4 deg, 54% at 1.3 deg); S-band: Galileo telemetry unreliable below 4 deg; Ka-band amplitude scintillation saturates near 0.67 deg, usable with special techniques to about 0.4 deg; the Sun's disk is 0.264 deg in radius seen from Earth; for a source behind the disk "the option of taking a temporary communication outage should be weighed against the expense of inserting a trailing or leading relay satellite" | Morabito and Hastrup (JPL), IPN Progress Report 42-147, 15 Nov 2001 | Primary | [TR] F4: Mars missions stop commanding inside 2 deg, about two weeks every two years (LASP/MAVEN 2015) | High |
| Autonomous navigation (flown) | Deep Space 1 flew "the first autonomous optical navigation system to be used in deep space", doing cruise orbit determination from asteroid images and controlling the ion-propulsion trajectory; Borrelly flyby accuracy under 10 km using radio, optical and interferometric data together (DEMONSTRATED) | Riedel et al., NTRS 20060032732 (2000); Bhaskaran et al., NTRS 20060029673 (2002) | Primary (abstracts) | none | High |
| One-way navigation clock (flown in Earth orbit) | Deep Space Atomic Clock: long-term stability 3 x 10^-15 at 23 days, drift 3.0 x 10^-16 per day; "will enable one-way radiometric measurements with accuracy equivalent to current two-way tracking data" (DEMONSTRATED in low Earth orbit, 2019-2021) | Burt et al., Nature 595, 43-47 (2021); Stuart, Ely, Seubert, NTRS 20220001460 (2020) | Primary | each other | High |

**DERIVED D10: solar-conjunction outages for every pair, 2030-2035** (JPL ephemeris as in D2; Ceres from SBDB). The Mars
thresholds above are angles seen from Earth at 1 AU; they are converted here to the distance at which the line of sight
passes the Sun (sin 2.3 deg x 1 AU = 0.040 AU for X-band; 0.0117 AU for Ka-band at 0.67 deg; 0.070 AU for S-band at
4 deg) and applied to the straight line between each pair. Check: Earth-Mars gives 3 X-band events averaging 14.5 d,
matching the two-week Mars moratorium.

| Link | X-band outages in 6 yr (mean / longest) | Share of time out (X) | Ka-band outages (mean / longest) | S-band share out | Sun's disk blocks the line (days in 6 yr) |
|---|---|---|---|---|---|
| Mercury-Earth | 19 (4.2 d / 7.8 d) | 3.6% | 4 (1.2 d / 2.2 d) | 7.5% | 1.5 |
| Mercury-Venus | 15 (6.8 d / 12.5 d) | 4.7% | 8 (1.5 d / 2.8 d) | 8.4% | 1.5 |
| Mercury-Mars | 22 (3.6 d / 5.5 d) | 3.7% | 6 (1.0 d / 1.5 d) | 7.1% | 0.5 |
| Mercury-Ceres | 24 (2.5 d / 4.5 d) | 2.7% | 5 (0.7 d / 1.0 d) | 6.3% | 0.2 |
| Venus-Earth | 4 (16.2 d / 18.8 d) | 3.0% | 2 (3.2 d / 4.8 d) | 5.4% | 1.8 |
| Venus-Mars | 7 (8.3 d / 9.5 d) | 2.7% | 0 | 4.9% | 0 |
| Venus-Ceres | 4 (4.2 d / 5.8 d) | 0.8% | 0 | 2.3% | 0 |
| Earth-Mars | 3 (14.5 d / 17.8 d) | 2.0% | 1 (4.8 d) | 3.6% | 0 |
| Earth-Ceres | 1 (3.8 d) | 0.2% | 0 | 0.6% | 0 |
| Mars-Ceres | 0 | 0% | 0 | 0.4% | 0 |

**DERIVED D11: distance and one-way light time, 2030-2035.** Mercury-Earth 0.55 to 1.45 AU, 4.6 to 12.1 min;
Mercury-Venus 0.26 to 1.19 AU, 2.2 to 9.9 min; Mercury-Mars 8.1 to 17.3 min; Mercury-Ceres 18.1 to 27.9 min; Venus-Earth
2.2 to 14.4 min; Venus-Mars 6.4 to 19.9 min; Venus-Ceres 15.3 to 30.8 min; Earth-Mars 3.2 to 22.2 min; Earth-Ceres 13.2
to 32.8 min; Mars-Ceres 11.2 to 38.3 min. Round trips are twice these.

**Reading:**

- **Mercury links black out most often but most briefly:** about 19 to 24 X-band outages in 6 years on every Mercury
  link, each a few days; Venus-Earth and Earth-Mars outages are rare but last two to three weeks. Moving the main link to
  Ka-band cuts every outage to a few days or none. A relay off the line (the "trailing or leading relay satellite" of
  Morabito and Hastrup) removes the outage at the cost of another spacecraft; no study sizing such relays for an
  inner-system network was found.
- **The DSN cannot track a fleet.** At BepiColombo's three passes per week, the 240 to 530 tugs of the smallest flow in
  F6 would need about 37,000 to 83,000 passes a year, against about 77,000 antenna hours the whole network delivered in
  FY 2022 to about 60 missions while already 40% oversubscribed (DERIVED). Fleet operation at any F6 scale implies
  autonomous navigation (flown on Deep Space 1), one-way radiometrics (enabled by clocks like DSAC) and a dedicated
  network; none of these has been operated at fleet scale.
- **Delay rules out remote driving.** At 2 to 38 min one way, every close operation (rendezvous with a catcher,
  aerocapture, a launcher's release) must be closed-loop on board.

### F8. Wireless power transfer as part of the network (checklist 8)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Microwave beaming, largest field test found | 2,388 MHz over 1.54 km to a 24 m^2 rectenna; up to 30.4 kW DC; collection-conversion efficiency "greater than 80 percent" (DEMONSTRATED, 1975, on the ground) | Dickinson (JPL), NTRS 19760004119, Sep 1975 (abstract) | Primary | none opened | High |
| Laser beaming, distance record | More than 800 W delivered for 30 s from 8.6 km; over 1 MJ in the campaign; "more than 20% efficiency from the optical power out of the laser to the electrical power out of the receiver at shorter distances"; previous record 230 W at 1.7 km (DEMONSTRATED, 2025, in air) | DARPA news, 16 May 2025 | Primary (agency) | none | High |
| Laser beaming components | Commercial 1,070 nm fiber laser about 38% wall-plug efficient (">50%" demonstrated elsewhere); photovoltaic receiver matched to the wavelength about 50%; full beam divergence 2.44 lambda / D (1.86 x 10^-6 rad for a 1.4 m mirror) (ENGINEERING-STUDIED) | Landis et al. (NASA GRC), Space Power Workshop 2025, NTRS 20250003925 | Primary | DARPA's >20% optical-to-electrical at the receiver | Medium-high |
| GEO solar power satellite reference (efficiency chain and receiver size) | About 2 GW delivered; rectenna 6 km at 2.45 GHz (RD1) or 4 km at 5.8 GHz (RD2); cells 0.35, DC-DC 0.90, DC-RF 0.70, antenna 0.90, atmosphere 0.98, beam collection 0.95, rectenna 0.78, ground DC-DC 0.90 (ENGINEERING-STUDIED) | Rodgers et al., NASA OTPS, "Space-Based Solar Power", 11 Jan 2024, Appendix B | Primary | DERIVED: product of the chain from space DC to ground DC = 0.37; from sunlight = 0.13 | Medium (study assumptions) |
| Beam collection law | tau^2 = A_TX A_RX / (lambda^2 R^2); collection efficiency = 1 - exp(-tau^2) (Goubau and Schwering 1961; Brown 1984); worked case 200 m and 500 m apertures, 450 km, 2.45 GHz: tau^2 about 3.30, 96% | Alhassan, Iqbal, Hu, arXiv 2606.18416 (2026 preprint) | Primary (preprint stating a standard result) | Chen et al. (JEWA 2018): the formula errs in the near field and for non-ideal apertures | High for the far-field case |
| Power beaming from orbit (first demonstration) | Caltech's MAPLE (on SSPD-1, launched Jan 2023) beamed microwave power to receivers "about a foot" away inside the spacecraft and steered a beam that was detected on the ground at Caltech; no delivered-power figure published in the items found (DEMONSTRATED; delivered power not stated) | Trade press quoting Caltech (POWER magazine, pv magazine, June 2023) | Secondary | none primary found | Low-medium |
| Space solar power exported from Mercury or another inner site | **No published engineering concept found** (searched; Open threads) | n/a | n/a | n/a | n/a |

**DERIVED D12: aperture sizes that diffraction requires at inner-system distances** (equal circular transmitter and
receiver, Goubau-Brown law above):

| Distance | 5.8 GHz microwave, 90% / 50% collected | 2.45 GHz, 90% / 50% | 1.07 µm laser, 90% / 50% |
|---|---|---|---|
| 0.30 AU | 67 km / 50 km each | 103 km / 76 km | 305 m / 226 m |
| 0.55 AU (Mercury-Earth at its closest) | 91 km / 67 km | 139 km / 103 km | 412 m / 305 m |
| 1.00 AU | 122 km / 91 km | 188 km / 139 km | 556 m / 412 m |
| 1.45 AU (Mercury-Earth at its farthest) | 147 km / 109 km | 226 km / 168 km | 670 m / 496 m |

With an unequal pair the product of the diameters is what matters (D_t x D_r is fixed for a given efficiency). A 1.4 m
laser mirror (the Landis lunar design) spreads 84% of its beam over 153 km at 0.55 AU and 279 km at 1 AU; a 100 m
mirror over 2.1 km and 3.9 km.

**Reading:**

- **Microwaves are out at interplanetary range:** paired apertures of 67 to 226 km. The highest-power microwave link found ran
  1.54 km on the ground (MAPLE's beam from orbit was only detected), and the GEO reference design needs a 4 to 6 km rectenna from geostationary orbit, a
  distance thousands of times shorter than 1 AU.
- **Lasers are diffraction-feasible with apertures of a few hundred meters**, but the demonstrated links are 800 W over
  8.6 km in air, with over 20% optical-to-electrical efficiency only at shorter range, with components at about 38% (laser) and 50% (receiver), before beam
  losses. A receiver 400 m wide at 1 AU subtends about 3 nanoradians (DERIVED), so the pointing problem is roughly
  30,000 times finer than the 87 µrad budget adopted for the LEO study above.
- **Energy budget of beaming instead of shipping.** At the D7 tug productivity, moving 1 Mt/yr of cargo from Mercury
  takes 24 to 53 GW of thruster power (F6), all of which is generated locally from sunlight on the tugs. Beamed power
  would only make sense for loads that cannot carry their own arrays (catchers, launchers at night, F6(b)); no study
  found sizes such a link.

### F9. Propellant and consumables supply for the network (checklist 9)

Sibling files cited: `moon_lagrange_and_comparables.md` as **[ML]**, `mars_venus_and_transfer.md` as **[MV]**,
`belt_jupiter_saturn_and_deep_transit.md` as **[BT]**.

| Node | What is there | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|---|
| Mercury poles | Water ice in permanently shadowed, radar-bright deposits | **About 10^14 to 10^15 kg (about 100 to 1,000 km^3)**; infill about 41 (+30/-14) m in 9 craters | Deutsch, Head, Chabot, Neumann, Icarus 305 (2018), NTRS 20190001152 (abstract) | Primary | Eke, Lawrence, Teodoro (MNRAS, arXiv 1611.05395, 2016): (50 +/- 35) m thick, about 10^15 kg, upper limit about 3 x 10^15 kg; north-pole radar-bright area about 10,000 km^2 | Medium-high (two independent thickness methods agree on order) |
| Venus atmosphere | Bulk gas available at cloud level | Atmosphere about 4.8 x 10^20 kg; 96.5% CO2, 3.5% N2 by volume; minor (ppm by volume, near surface): SO2 150, Ar 70, H2O 20, CO 17; mean molecular weight 43.45 | NSSDC Venus fact sheet (11 Jan 2024) | Primary | [TR] F1b: CO/O2 propellant from CO2, Isp 250 s (Landis and Oleson 2024) | High (composition is "near surface"; cloud-level values differ, Open threads) |
| Venus atmosphere (DERIVED) | Inventories by mass | CO2 about 4.7 x 10^20 kg; argon about 3.1 x 10^16 kg (mass fraction 6.4 x 10^-5); water about 4.0 x 10^15 kg (8.3 x 10^-6); per 1,000 t extracted: about 15.5 Mt of atmosphere processed for argon, about 121 Mt for water | DERIVED from NSSDC | Derived | none | Medium (near-surface mixing ratios) |
| Moon | Polar ice | Cabeus regolith 5.6 +/- 2.9% water by mass (LCROSS); "at least ... 600 million metric tons" in north-polar craters (Mini-SAR, NASA 2010) | [ML] A5 and Conflicts 2 | Primary (via [ML]) | [ML]: estimates range 4.3 to 8.2 wt% depending on assumed density | Medium |
| Carbonaceous asteroids and Ceres | Bound water | CI chondrites about 20 wt%, CM about 9 wt%; C-complex main-belt surfaces average 4.5 wt% (0 to 11.5); Ceres up to about 25% water | [BT] composition rows (Garenne et al. 2014; Beck et al. 2021) | Primary (via [BT]) | [TR] F5/F6: Sonter assumes at most about 10% recoverable water | Medium |
| Mars | Water in soil and ice | 1.5 to 3 wt% water bound in soil; ice within meters at mid and high latitudes (SWIM) | [MV] 3.4 | Primary (via [MV]) | none | Medium |
| Electric-propulsion propellants actually flown | Xenon (Dawn, BepiColombo), krypton and argon (Starlink) | [TR] F2, F3; Filleul et al. 2021 | Primary / secondary | n/a | High |
| Water as an electric propellant | Water resistojet flown (AQUARIUS-1U: 4 mN, Isp 70 s, 0.22 mN/W, 2019); a Hall thruster run on water-electrolysis products in the laboratory (AQUAHET, Imperial College, May 2023), no performance published in the release | eoPortal AQT-D (secondary, quoting the University of Tokyo); Imperial College news, 10 May 2023 | Secondary / primary (institutional news) | none | Medium. **No high-Isp water electric thruster has flown** |

**DERIVED D13: propellant budget implied by the F6 flows.**

| Flow (Mercury to Earth) | SEP direct spiral (2.4 t per t) | SEP with flybys (xenon, about 63 t per kt) | Sails |
|---|---|---|---|
| 1 kt/yr | 2,400 t/yr | about 63 t/yr | none |
| 100 kt/yr | 240,000 t/yr | about 6,300 t/yr | none |
| 1 Mt/yr | 2.4 Mt/yr | about 63,000 t/yr | none |

**Reading:**

- **Mercury's ice could feed the direct-spiral fleet for a long time, if water could be the propellant.** 2.4 Mt/yr against
  10^11 to 10^12 t of ice is a draw of about 40,000 to 400,000 years. **The blocker is the thruster, not the ice:** high-Isp
  electric propulsion on water has not flown (F9 table); the only flown water thruster gives 70 s.
- **Xenon cannot supply even the 1 kt/yr direct-spiral case** (about 37 times world output, F6), and the 1 kt/yr flyby case
  takes about one year of world xenon production every year.
- **Venus holds about 3 x 10^16 kg of argon**, a flown Hall-thruster propellant, but it is 64 parts per million by mass and
  sits at the bottom of a 9 km/s ascent (F6, [TR] F1b), so it is not an export.
- **The inner network has no propellant node between Mercury and the Moon** in the sources found: bulk Venus gas is
  reached only through the 9 km/s ascent; the only orbital-scoop studies found are for Mars (NIAC Molniya collector:
  about 431 kg of CO2 per pass at 79 km, 34.9 t over 81 passes, about 7 t of O2), none for Venus; Venus's surface is
  at 737 K and 92 bar, and Venus has no natural satellites (NSSDC). Lunar ice (about 6 x 10^8 t in
  one radar estimate) and near-Earth carbonaceous asteroids are the nearest sources at the Earth end.

### F10. Space weather along the network (checklist 10)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| How solar-energetic-proton intensity grows toward the Sun (measured) | Peak flux scales as R^-3.7 to R^-2; event fluence as R^-2.7 to R^-1.4; 10.5 to 40 MeV protons; 42 events seen by at least two of SOHO (1 AU), Parker Solar Probe (0.05-0.78 AU) and Solar Orbiter (0.29-1.01 AU), 2021-2023, magnetic footpoints within 30 deg; the exponent is steeper at lower energy (DEMONSTRATED, measured) | Cao, Wang, Guo et al., "Radial dependence of solar energetic particle peak fluxes and fluences", A&A 695 (27 Feb 2025), DOI 10.1051/0004-6361/202452591 (abstract via Crossref); ESA Solar Orbiter science nugget #55, 19 Mar 2025 | Primary | Older Helios-era modeling (Lario et al. 2006-2007) gave a shallower range in a search summary only (not used) | Medium-high (exponents are statistical; individual events vary) |
| Warning from relativistic electrons (at 1 AU) | Electrons arrive "about one hour before the solar proton radiation hazard"; 2003-2007 archive: 10 of 11 prompt events forecast with 122 min average warning, 79% overall with 195 min average, 13 false-warning series; fastest-rising event on record (20 Jan 2005): electron precursor 20-25 min ahead (DEMONSTRATED as a forecasting method on archived data; entered NASA JSC verification) | Posner, Space Weather (May 2007); Posner, CCMC workshop slides, 26 Jan 2010; SwRI release 25 May 2007 | Primary | none | Medium-high |
| Dose scale at 1 AU (for reference) | Interplanetary cruise solar particle events 1.2 to 19.5 mSv each inside MSL; Mars Odyssey saw dose rate rise about 40 times in Oct 2002; NASA design limits 250 mSv per event, 600 mSv career; aluminum/polyethylene shielding gives about 50% reduction for solar events and about 7% for galactic cosmic rays | [MV] 3.3 (Hassler 2014, Guo et al., NASA OCHMO) | Primary (via [MV]) | [BT]: 1.8 mSv/day galactic background inside MSL | Medium |

**DERIVED D14 (scaling to the inner nodes; basis: the measured exponents above and straight-line particle paths).**

| Location | Fluence relative to 1 AU (R^-1.4 to R^-2.7) | Peak flux relative to 1 AU (R^-2 to R^-3.7) | Electron lead over 30 MeV protons, straight-line path (min) | Same, 100 MeV protons (min) |
|---|---|---|---|---|
| 1.0 AU (Earth, Moon) | 1 | 1 | 25.4 | 11.1 |
| 0.723 AU (Venus) | 1.6 to 2.4 | 1.9 to 3.3 | 18.3 | 8.0 |
| 0.387 AU (Mercury, mean) | 3.8 to 13 | 6.7 to 34 | 9.8 | 4.3 |
| 0.307 AU (Mercury, perihelion) | 5.2 to 24 | 11 to 79 | 7.8 | 3.4 |

The real path follows the curved interplanetary magnetic field and is longer than a straight line at every distance, so
these leads are lower bounds; the 1-AU archive (122 min average) shows that the rise time of the proton event, not just
transit, sets the usable warning. The direction of the result is robust: **warning shrinks about in proportion to
distance, while dose grows faster than 1/R.**

**Reading:**

- **At Mercury a solar particle event is several to about 25 times the fluence seen at Earth, and arrives with roughly a
  third of the warning.** An Earth-side alert is useless there: light-time alone from Mercury to Earth is 4.6 to 12.1 min
  (D11), comparable to the whole electron lead.
- **Events are magnetically local.** The measurements above required magnetic footpoints within 30 deg; a node is warned
  only by sensors on its own field line, so each node (or each convoy) needs its own particle monitor.
- **Machine-tended traffic is exposed too:** transit legs from Mercury last months to a decade (F2, F3), so every vehicle
  integrates many events. No dose figure for electronics at 0.3-0.5 AU was found as a sourced number (Open threads).

### F11. Reference-class evidence for how fast such an operation could scale or fail (checklist 11)

The build-out and failure evidence is in **[RM]**: historical network build-outs (F1), learning rates (F2; launch cost
per kg falls 21.2% per doubling of cumulative payload), space-infrastructure assembly histories (F3), bootstrapping
models (F4: NASA CP-2255, SP-413, SP-428 Vajk, Metzger et al.), dependency lags (F6: reactors 59 to 121 months median,
grid interconnection nearly 5 years, NASA's 36 major projects 14 years of cumulative delay, Flyvbjerg's "iron law" of
megaprojects) and stage ratios (F7). Not repeated here. Two primary points on supply-chain length were found and are
added:

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Pipeline inventory law | "Average Inventory = Average Flow Rate x Average Flow Time" (Little's Law, L = lambda W), holding for any stable flow regardless of the details of the process | Little (MIT Sloan), "Little's Law as Viewed on Its 50th Anniversary", Operations Research 59(3) 536-549, 2011 | Primary (peer-reviewed) | none needed (theorem) | High |
| What one lost delivery does at the end of a long supply line | ISS reserve rules: food for 45 days for six crew (216 rations), oxygen 290 kg (6 months of US-segment use), water 1,034.5 L (55 days without regeneration), nitrogen 132 kg; one launch failure (SPX-7, June 2015) destroyed 690 kg of crew supplies and left a 3.48 t upmass shortfall for the year, cut to 2.63 t by repacking other flights; "NASA was forced to make changes to its cargo manifests for subsequent missions" (DEMONSTRATED) | NASA OIG, IG-16-025, 28 Jun 2016, Table 5 and pp. 10-12 | Primary | [ML] E: South Pole fuel "nearly eight times its original purchase price" and one flight season a year | High |

**DERIVED (applying Little's Law to F6):** cargo in flight equals annual flow x trip time. At 1 Mt/yr from Mercury that
is 0.8 to 2.1 Mt aboard sails, 2.3 to 5.2 Mt aboard direct-spiral tugs, or about 9.8 Mt on a flyby route; at 1 kt/yr,
0.8 to 9.8 kt. **The longer the route, the more material (and vehicle capital) is committed before the first metric ton
arrives**, and the ISS record shows what a single lost carrier does when the next window is months away: reserves at
the receiving end must cover at least one window gap (about 116 d Mercury-to-Earth, F1) plus one lost shipment. On
the flyby route the first delivery arrives about ten years after the first departure (F2), so a decade of production
precedes any return; [RM] F6's dependency lags apply on top of that.

## Conflicts

- **C1. The sibling trucking file understates the Mercury-Earth v-infinity sum.** [TR] Conflicts C1 says "DERIVED D1 gives
  hyperbolic excess speeds 7.55 + 7.53 = 15.1 km/s" and its D1 text says "Earth to Mercury v-inf 7.55 (depart) and 7.53
  (arrive)". Recomputed here with the same constants (D1): the v-infinity at **Mercury** on a Hohmann transfer is
  **9.61 km/s** and at **Earth 7.53 km/s**, sum **17.14 km/s**. The 7.55 km/s in [TR]'s table is correct as what it is
  labeled there (the burn to leave a 200 km Mercury orbit, which benefits from the Oberth effect); the error is only in
  calling it a v-infinity in C1 and the D1 note. TU Delft's course table independently gives Earth departure v-infinity
  7.533 km/s and a Mercury capture burn of 7.565 km/s, which requires a Mercury-end v-infinity near 9.6 km/s. Jehn and
  Schoenmaekers' "about 16 km/s" sits between the impulsive total from low orbits (11.2 to 13.1 km/s) and the v-infinity
  sum for circular orbits (17.1 km/s); Mercury's real eccentricity moves both (D2 window minima 17.6 to 22.9 km/s). Not
  edited in [TR] (outside this task's write permission); flagged for the developer.
- **C2. Hughes et al. sail size: "275-m²" (Strathprints abstract rendering) vs "275 x 275 m", 75,625 m^2 (full paper,
  Table 5).** The full paper is unambiguous (448 kg at 5.9 g/m^2 only works for 75,625 m^2); the abstract's superscript
  is an extraction artifact.
- **C3. MESSENGER array design: "about 2/3-cell coverage" (JPL D-101316, p. 13) vs "replacement of a significant
  fraction of the solar cells by optical solar reflectors" (same page).** Could mean two thirds cells or two thirds
  reflectors; the report does not say which. Not resolved; the operating temperature (~130 C) is used instead.
- **C4. Solar intensity at Mercury: "about 10 times" Earth (ESA) vs 6.674 (NSSDC).** ESA's figure matches perihelion
  (1/0.3075^2 = 10.6); NSSDC's is the mean. Definition, not disagreement.
- **C5. Citation of the Solar Orbiter SEP result: "A&A, 965, A25 (2025)" (ESA nugget) vs volume 695, published 27 Feb
  2025 (Crossref).** A misprint in the nugget; the DOI resolves to volume 695.
- **C6. Mercury polar ice: about 10^14 to 10^15 kg (Deutsch et al. 2018) vs about 10^15 kg with an upper limit of about
  3 x 10^15 kg (Eke, Lawrence, Teodoro 2016).** Different methods (infill of 9 small craters vs excess height in 12 larger
  craters) and areas; they overlap at about 10^15 kg. Both used as a range.
- **C7. Sail transfer time at 0.25 mm/s^2: 934 d (D6, circle to circle) vs 1,041 d (Hughes, Earth to Mercury with launch
  date and rendezvous).** The 11% difference is the cost of real phasing and rendezvous; D6 is a lower bound. At
  0.78 mm/s^2 D6's steering law fails (eccentricity 0.2) and Hughes' 369 d is used.
- **C8. Goldstone 1975: "up to 30.4 kW" and "greater than 80 percent" (Dickinson abstract, NTRS) vs "over 34 kW" and
  "82.5%" (search summary of another report).** Only the abstract was read; its figures are used.
- **C9. Electron warning time: "up to about one hour" (SwRI 2007) vs "122 min average" for prompt events and "195 min
  average" overall (Posner 2010 slides).** The slides use a 2003-2007 archive and a different definition of warning
  (from alert to hazard threshold, including slow-rising events); the one-hour figure is the electron-to-proton lead.

## Derived figures

All arithmetic was run in Python with the constants named in F1 (JPL SSD, NSSDC, SBDB) unless stated. Scripts are in
the scratch folder (not part of the library); every formula is given here so it can be repeated.

- **D1. Synodic periods, Hohmann transfers (F1).** T = 2 pi sqrt(a^3 / GM_sun); S = 1 / |1/T1 - 1/T2|; transfer
  semimajor axis a_t = (r1 + r2)/2; time = T(a_t)/2; v-infinity = |sqrt(GM(2/r - 1/a_t)) - sqrt(GM/r)| at each end.
  Mercury perihelion/aphelion cases use r = a(1 -/+ e) and Mercury's speed sqrt(GM(2/r - 1/a)). Checks: S(Mercury-Earth)
  115.88 d, S(Venus-Earth) 583.93 d, S(Earth-Mars) 779.93 d against NSSDC 115.88, 583.92, 779.94.
- **D2. Window scan (F1).** Planet states from the JPL Table 1 elements and rates (Kepler's equation solved by Newton
  iteration), 1 Jan 2030 to 31 Dec 2035, departures every 2 d; zero-revolution Lambert problem by universal variables
  (bisection on z), 61 flight times spanning the ranges in the table; best total v-infinity per departure date; window =
  local minimum within plus or minus 30 d; width = contiguous days within 10% of that minimum. Check: Earth-to-Mars
  15 Apr 2033 departure v-infinity 2.99 km/s against the Hohmann 2.945 km/s (TU Delft).
- **D3. Window-width asymmetry (F1).** Same Lambert method on circular coplanar orbits, 240 departure phases per
  synodic period, flight time 0.3 to 2.0 x Hohmann: Mercury-to-Earth 11 d at +10% vs Earth-to-Mercury 50 d; Venus-to-Earth
  29 d vs 46 d; Mars-to-Earth 88 d vs Earth-to-Mars 45 d; Mercury-to-Ceres 14 d vs Ceres-to-Mercury the whole cycle.
- **D4. Mercury launcher (F4).** Horizontal surface launch: muzzle speed v = sqrt(v_inf^2 + 2 GM/R); KE = v^2/2;
  acceleration length L = v^2 / (2 x 1,000 g0); SP-428 machine mass x (v/2.4)^2. Hyperbolic turn: e = 1 + R v_inf^2 / GM,
  angle from launch point to asymptote = arccos(-1/e). For each 2-day departure (D2 Lambert, best total v-infinity), the
  asymptote's direction was expressed in Mercury's orbital plane (in-plane angle and declination); a fixed equatorial
  site rotates at 360 deg / 58.65 d; alignment counted on a 0.1-day interpolated grid when the site lay within plus or
  minus 2 or 5 deg of the required launch point, inside a +10% window, for the best of 180 site longitudes; a "two-way
  track" may also launch westward (asymptote = site - turn angle). Near-planar filter: |declination| at most 5 deg.
- **D5. Edelbaum low-thrust delta-v (F3, F6).** V1 = sqrt(GM_sun / 0.38709927 AU) = 47.87 km/s, V2 = 29.78 km/s,
  tilt 7.005 deg = 0.1223 rad: sqrt(47.87^2 + 29.78^2 - 2 x 47.87 x 29.78 x cos(pi/2 x 0.1223)) = 19.48 km/s; Mercury
  escape spiral from 200 km taken as the circular speed there (Edelbaum with V2 = 0), sqrt(22,032 / 2,639.7) = 2.89 km/s;
  total 22.37 km/s.
- **D6. Sail spiral (F3).** Planar two-body integration (semi-implicit Euler, 1,800 s step); acceleration
  a_c (1 AU / r)^2 cos^2(alpha) along the sail normal at cone angle alpha = 35.26 deg (tan alpha = 1/sqrt 2), clocked
  prograde for outward and retrograde for inward; stop when the osculating semimajor axis reaches the target. Valid
  while the final eccentricity stays small (a_c up to 0.5 mm/s^2). Sail pressure from Hughes: 2,353 kg x 0.25 mm/s^2 /
  75,625 m^2 = 7.78 µN/m^2 (0.85 of the 9.1 µPa perfect-reflector value, Bailer-Jones). a_c = 7.78 / sigma mm/s^2
  with sigma in g/m^2.
- **D7. SEP tug productivity (F3, F6).** Isp 2,890 s (v_e 28.34 km/s), thrust T = 2 eta P / v_e with eta 0.67, duty 0.9;
  tug dry 68 kg/kW (from [TR] D3's Cassady tug: 9,750 kg initial, 6,940 kg payload, mass ratio exp(3,420/28,341) =
  1.128, so 1,701 kg dry tug for 25 kW). Heliocentric leg integrated over circular speed with r = GM/v^2 and the D5
  plane-change factor (19.48/18.09); power either constant or (1/r)^2 capped at (1/0.62)^2 = 2.60. Propellant from
  the rocket equation on each leg; cycle = loaded + empty + 30 d. Payload 2 x dry: 857 d + 322 d (capped) or 1,890 d +
  630 d (flat); 0.041 or 0.019 t per kW-year; 2.40 t of propellant per t delivered.
- **D8. Capture (F5).** dv = sqrt(v_inf^2 + 2 GM/r_p) - v_p, with v_p circular or the periapsis speed of the target
  ellipse; entry speed sqrt(v_inf^2 + 2 GM/(R + h)), h = 125 km (Earth, Mars) or 150 km (Venus), an assumed interface.
  GM and radii from [TR] F1 constants.
- **D9. Fleets (F6).** Tug power = flow / productivity; number = power / 100 kW; in transit = flow x loaded time.
  Flyby stages: 7.718 t delivered per stage (3,764 + 3,231 + 723 kg), 9.3 kW, 484 kg xenon, 117.5 months. Mass driver:
  jet power = flow x 9.03 MJ/kg / 3.156 x 10^7 s; electrical / 0.964; SP-428 duty 179 d/yr doubles it. Sails: trip
  = 230 / a_c d each way, 30 d dwell; area = flow / (payload loading x trips per year).
- **D10. Conjunction outages (F7).** For each pair, every 6 h for 6 years, the closest distance from the Sun to the
  straight segment between the two bodies; thresholds 0.0117 / 0.0401 / 0.0698 AU (Ka / X / S, from 0.67 / 2.3 / 4 deg
  at 1 AU) and the solar radius 695,700 km (NSSDC). Check: Earth-Mars X-band events average 14.5 d.
- **D11. Light time (F7).** Daily distances 2030-2035 / c (299,792.458 km/s).
- **D12. Beam apertures (F8).** Equal circular apertures: tau^2 = (pi D^2/4)^2 / (lambda R)^2, so D = sqrt((4/pi)
  lambda R tau) with tau = sqrt(-ln(1 - eta)); lambda = c/f (5.17 cm at 5.8 GHz, 12.2 cm at 2.45 GHz) or 1.07 µm.
  84% spot = 2.44 lambda R / D_t (Landis). Pointing: 400 m / 1 AU = 2.7 x 10^-9 rad.
- **D13. Propellant budgets (F9).** From D7 (2.40 t/t) and D9 (484 kg xenon per 7.718 t). Venus inventories: mass
  fraction = ppm x 10^-6 x (molar mass / 43.45) x 4.8 x 10^20 kg; molar masses H2O 18.0153, Ar 39.948, CO 28.0101,
  SO2 64.064, CO2 44.0095 g/mol (NIST Chemistry WebBook, log row 113; the run used 64.066 for SO2, a 0.003% difference). Mercury ice draw: 2.4 x 10^6 t/yr against 10^11 to 10^12 t.
- **D14. Space weather (F10).** Scaling R^-alpha with the measured exponent ranges; straight-line transit t = r x
  499.005 s/AU / beta, beta = sqrt(1 - (m_p c^2 / (E + m_p c^2))^2), m_p c^2 = 938.272 MeV (NIST): 30 MeV beta 0.247,
  100 MeV beta 0.428; electron lead = proton time - light time.

## Constraints for any inhabitant

These apply to whoever lives or works at a node of an inner-system network (a Mercury launch or ice site, a Mercury-orbit
catcher, a Venus-orbit station, an Earth-vicinity receiving node), or rides its vehicles.

- **Shipping from Mercury is pulsed: about two weeks of good departures every 116 days to Earth, every 145 days to
  Venus, every 101 days to Mars, and the cheapest windows only about once a year** (F1, D2). Stock piles up between
  windows; receiving ends see bursts.
- **Inbound windows from the inner planets are narrower than outbound ones** (F1, D3): a node at Mercury has less schedule
  slack for sending than its suppliers have for reaching it.
- **A launcher on Mercury cannot be aimed by the planet's rotation.** A fixed track lines up with a useful Earth or Venus
  departure only a few days in six years (F4); the practical launcher throws to Mercury orbit or escape, where a catcher
  and a long-haul carrier take over. Mercury's surface has 88-day nights at any one equatorial site (F6) and a 590 to
  725 K sunward surface (F4).
- **Anything thrown by a launcher rides at hundreds to a thousand g** ([TR] F2, F6); a human-shaped machine must travel
  by tug, sail or rocket, not in the cargo stream.
- **Trips are long, and the shortest ones are the costliest.** Mercury to Earth: about 3 to 4 months on an impulsive
  transfer that needs 7.5 km/s to leave and 5 to 7 km/s to stop (F1, F5); about 1 year by an optimized sail; about 2 to 7
  years per tug round trip; about 10 years each way by SEP with flybys (F2, F3, F6).
- **Arrivals from Mercury are fast:** 6.5 to 11 km/s v-infinity at Earth, 5 to 9 at Venus, 8 to 12 at Mars (F1, F5). A
  receiving node must either spend 5 to 9 km/s per kilogram to stop it, aerocapture at 13 to 15 km/s entry speed (never
  flown, beyond tested heat shields), or accept slow routes.
- **Power near the Sun is limited by heat, not by sunlight.** Arrays must be tilted or diluted with mirrors inside about
  0.6 to 0.7 AU (F3); BepiColombo, "despite approaching the Sun", was "highly power-constrained".
- **Communication blackouts recur:** Mercury links lose X-band about 3 to 4 times a year for a few days each (mean 2.5 to
  6.8 d, longest 12.5 d); Venus-Earth and
  Earth-Mars links for 2 to 3 weeks once per synodic period (F7). Light time is 2 to 38 minutes one way. Nothing near a
  node can be operated live from another planet.
- **Tracking capacity does not exist for fleets:** the DSN delivered about 77,000 antenna hours in FY2022 to about 60
  missions and was 40% oversubscribed (F7). A fleet of hundreds of vehicles must navigate itself.
- **Radiation storms at Mercury are several to about 25 times the fluence at Earth, with about a third of the warning**
  (minutes) (F10). Every node needs its own particle monitor and shelter; an alert relayed from Earth arrives after the
  particles.
- **Propellant is the binding resource for electric tugs.** Xenon cannot cover even 1 kt/yr from Mercury by direct
  spiral (F6, F9). Mercury's polar ice (10^14 to 10^15 kg) is large, but no flown high-Isp thruster burns water (F9).
- **Long routes lock up cargo and reserves:** cargo in flight equals annual flow times trip time (Little's Law, F11);
  the receiving end must hold reserves for at least one window gap plus one lost carrier, as the ISS holds 45 days of food
  and 6 months of oxygen (F11).

## Candidate handwaves

Flagged, not accepted. The developer decides. [TR] HW-1 to HW-7 (near-Sun bulk export, giant-planet gas export, xenon
at scale, routine aerocapture, catchers and depots at scale, E-sail cargo, zero boil-off) remain open and are not
repeated; the items below are additional.

- **HW-8. A Mercury surface launcher throwing directly onto Earth, Venus or Mars transfers.** Muzzle speeds 7.4 to
  11.8 km/s (14 to 24 times the lunar design's energy), out-of-plane asymptotes a median 19 to 26 deg, and only a few
  usable days in six years for a fixed track (F4). Plausible only as a launcher to Mercury escape or orbit.
- **HW-9. Electric tugs on water (or any propellant made at Mercury) at Hall- or ion-class Isp.** Needed for any
  direct-spiral flow above a few hundred metric tons a year (F6, F9); only a 70 s water resistojet has flown.
- **HW-10. Square-kilometer-to-hundred-thousand-square-kilometer sail fleets near Mercury** (133 to 336 km^2 for 1 kt/yr,
  F6), with sail lifetimes long enough to amortize sail mass comparable to a year's cargo. The largest sail flown in
  deep space is 196 m^2, and no lifetime figure was found.
- **HW-11. Aerocapture of fast inner-system cargo** at 11 to 15 km/s entry at Earth or Venus (F5); the one Venus design
  studied (11.25 km/s) already exceeded every tested tile system.
- **HW-12. Interplanetary power beaming.** Microwaves need paired apertures of 67 to 226 km; lasers need hundreds of
  meters and nanoradian pointing (F8); demonstrated links reach 8.6 km in air.
- **HW-13. Fleet operations at DSN scale or beyond.** Hundreds to hundreds of thousands of vehicles cannot be tracked by
  any existing network (F7); autonomy has flown on single spacecraft only.
- **HW-14. Flyby-route cargo on every window.** The flyby routes (F2) are tied to specific resonant alignments; treating
  them as a lane open every synodic period would bend orbital mechanics.
- **HW-15. Bulk export from Venus's clouds** (about 180 t lifted per metric ton delivered at the one studied payload fraction,
  F6).

## Open threads

- **Mercury-to-Earth and Mercury-to-Venus cargo trajectories with flybys:** no study found; only outbound (Earth-to-Mercury)
  designs (rows 4-6, 12, 22, 50). Next: Langevin, Acta Astronautica 47 (2000) 443-452 (paywalled); C. W. Yen, "Ballistic
  Mercury orbiter mission via Venus and Mercury gravity assists", J. Astronautical Sciences 37 (1989) (not located);
  NTRS 19740013378 (found, not opened); the ScienceDirect paper "Solar sail missions to Mercury with Venus gravity assist"
  (found, not opened).
- **Earth-Venus cycler numbers:** Hollister and Menning's own papers and the Jones-Hernandez-Jesick triple-cycler full
  text (ResearchGate, not readable by the tools) were not obtained; only abstracts (rows 13-21, 109).
- **BepiColombo transfer-module array power versus Sun distance:** Steiger et al. Fig. 14 is a plot (not extracted as
  numbers); the ESPC 2017 array papers returned HTTP 403 (row 34); the "about 13 kW peak" figure came only from a search
  summary. Next: ESA BepiColombo Red Book, the 2011 ESPC paper via another host.
- **Sail lifetime and degradation near the Sun**, and optimal-control sail transfer times above about 0.5 mm/s^2 (D6's
  simple law fails there). Next: McInnes, *Solar Sailing* (1999); Dachwald's slides (found, not opened); NASA sail
  degradation studies.
- **High-Isp electric propulsion on water** (performance of AQUAHET or ion thrusters on water): no figures found
  (rows 94-96).
- **Release accuracy of a mass driver for an interplanetary throw**, and catcher dynamics at Sun-Mercury L1/L2 (Mercury's
  Hill radius about 221,000 km): no source.
- **A sized destination processing node** for bulk inner-system cargo: none found.
- **Relay constellations for conjunctions** (count, orbit, power): only the qualitative recommendation of Morabito and
  Hastrup (row 77).
- **Radiation dose to electronics at 0.3 to 0.5 AU** (MESSENGER and BepiColombo radiation-monitor data), and solar-wind
  and dust environment at Mercury orbit: not searched in depth.
- **Venus cloud-level composition** (the NSSDC mixing ratios are near-surface): not searched.
- **Space solar power exported from Mercury or another inner site:** no published engineering concept found (row 87).
- **Sources found but not read:** arXiv 1706.05443 (SEP radial dependence model); arXiv 0809.3535 (beryllium hollow-body
  sail; likely source of the killed 1,000 K claim, row 63); Kim, Hu, Cucinotta (AIAA 2005) on acute exposure; Posner,
  Space Weather (2007) paper itself; NASA STRG page on an Earth smallsat aerocapture test; Georgia Tech aerocapture
  theses; Hughes, Macdonald et al., "Terrestrial planet sample return missions using solar sail propulsion" (Strathprints
  6245).

## Rejected sources

- **Wikipedia pages** (Mars cycler, Cycler, AQT-D, Solar Cruiser, Mass driver, Aerocapture, Geoffrey Landis): leads only.
- **Orbiter-forum, Kerbal forum, physicsforums, scientific-speculation, LessWrong, GreaterWrong, substack posts**: not
  sources of physics data.
- **Homework sites (brainly, quizlet, gr.inc, byjus)**: rejected.
- **space-mining.com "Resource Potential of Mercury"**: an unsourced blog; not used.
- **academia.edu, "A cycler-quartet between Venus and Sol/Terra L1"**: self-published, not peer-reviewed; not used.
- **Smith, "Viability of a Dyson Swarm as a Form of Dyson Sphere" (arXiv 2109.11443, physics.pop-ph, undergraduate)**:
  read in part; not used for any number.
- **Universe Today, Interesting Engineering, techxplore, phys.org, space.com, Potomac Officers Club**: secondary press;
  used only to find primary documents.
- **Search-summary figures not confirmed in the opened source** (all discarded): the "0.1 AU, 937 m sail, about 1000 K"
  example (row 63); Goldstone "34 kW / 82.5%" (row 82); Posner "7 to 74 minutes in 2003" (row 102); MTM "13,000 W peak"
  (row 33); Lario "R^-3 to R^-1.3" (row 98).
