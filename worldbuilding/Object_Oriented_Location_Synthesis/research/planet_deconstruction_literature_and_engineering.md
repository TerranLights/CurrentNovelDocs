# Planetary deconstruction: the literature and the engineering it actually specifies

*OOLSD research file, tranche 8, section 1. Started 2026-10-11, completed 2026-10-12. Physics and engineering only; no
setting, story or canon was read or assumed.*

## Scope

The published literature on taking a planet apart for its mass (Mercury above all; Jupiter, Venus and the other planets where
the same papers treat them), and on building a collector swarm from that mass: what each source actually states, which numbers
come from an engineering study and which from a thought experiment, and what the named mechanisms (mass drivers, launch loops,
elevators, tethers, ablation, explosives, impacts) can and cannot do at planetary throughput. Evidence words: DEMONSTRATED (built
or flown), ENGINEERING-STUDIED (a quantitative design), SPECULATIVE (a thought experiment or claim), DERIVED (my arithmetic from
sourced inputs; scripts in the scratch subfolder `planet_deconstruction_literature_and_engineering/calc/`).

## SEARCH LOG

| # | Date | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read sibling files (read-only, permitted): `_BRIEF.md`, `starlifting_synthesis.md`, `inner_system_mining_synthesis.md`, `industrial_ramp_timelines.md` F4, `space_trucking_and_transport_infrastructure.md` F2 | useful | Baseline: what is already known (lunar mass driver SP-428, CP-2255, Metzger 2013, Ono 2025) |
| 2 | 2026-10-11 | WebSearch: `Armstrong Sandberg "Eternity in six hours" intergalactic spreading of intelligent life pdf` | useful | FHI PDF URL; fhi.ox.ac.uk no longer resolves (FHI closed) |
| 3 | 2026-10-11 | Fetch attempt: https://www.fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf | dead at the sources | DNS failure: host no longer resolves |
| 4 | 2026-10-11 | Opened (full text, 35 pp. preprint dated 12 Mar 2013, "Preprint submitted to Acta Astronautica") via Wayback Machine: https://web.archive.org/web/2023id_/https://www.fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf | useful | Every parameter of the Mercury disassembly read (sec. 4.1, 4.2, 6.3); no equation for the disassembly model is printed |
| 5 | 2026-10-11 | Opened (full text, OCR) Dyson 1960, *Science* 131:1667, Internet Archive item https://archive.org/details/dyson-1960-search-for-artificial-stellar-sources-of-infrared | useful | OCR dropped superscript exponents; the two exponents used here (10^12 growth factor, 10^44 erg) were reconstructed from the paper's own arithmetic (1%/yr for 3,000 yr; 4 x 10^33 erg/s for 800 yr) and are marked so |
| 6 | 2026-10-11 | Opened (full text) Wright, "Dyson Spheres", arXiv:2006.16734v3 (7 Oct 2020; Serbian Astronomical Journal 200, 2020) | useful | Mechanics (buckling, eq. 18 to 23), mass-efficiency scaling (eq. 64, 65), Landauer computing (eq. 66, 67); points to Dyson 1966 and Criswell 1986 for disassembly |
| 7 | 2026-10-11 | Opened (full text) Smith, "Viability of a Dyson Swarm as a Form of Dyson Sphere", arXiv:2109.11443v1 (20 Sep 2021, physics.pop-ph, undergraduate) | useful (low weight) | The only modeling paper found so far with an explicit launch-rate bottleneck; contains an orbit-radius error (row noted under Conflicts) |
| 8 | 2026-10-11 | Re-read sibling sections permitted by section 1: `industrial_ramp_timelines.md` F4; `space_trucking_and_transport_infrastructure.md` F2 and F4 | useful | Cited, not re-derived: CP-2255, Metzger 2013, Ono 2025, SP-428 III-3 launcher, SP-413 Appendix G catcher, MXER tether |
| 9 | 2026-10-11 | WebSearch: `Dyson 1966 "The search for extraterrestrial technology" Perspectives in Modern Physics disassemble planet` | thin | Only Wright 2020's summary of Dyson 1966 surfaced; no full text |
| 10 | 2026-10-11 | DuckDuckGo (script): `Dyson "search for extraterrestrial technology" 1966 pdf "electric motor" planet rotation dismantle` and `Freeman Dyson 1966 dismantle planet "electric motor" spin up rotation "2500 years"` | dead at the query | Zero results returned for both strings |
| 11 | 2026-10-11 | WebSearch (extended): `Freeman Dyson 1966 dismantle planet "electric motor" spinning rotation planet disassembly Jupiter years energy` | thin | Fan-wiki and encyclopedia pages only; no primary text of Dyson 1966; its mechanism and numbers stay unverified (Open threads) |
| 12 | 2026-10-11 | Fetched https://en.wikipedia.org/wiki/Astronomical_engineering (lead only) | dead at the sources | Redirects to a megastructure page with no planet-disassembly passage |
| 13 | 2026-10-11 | Opened Sandberg, "Dyson Sphere FAQ" (archived), https://web.archive.org/web/2006id_/http://www.nada.kth.se/~asa/dysonFAQ.html | useful (secondary) | Cited by Armstrong and Sandberg as ref. 33; mass table for usable planetary mass; "10-1000 times longer" claim with no basis; one error found (Earth mass) |
| 14 | 2026-10-11 | WebSearch: `Criswell "Solar System Industrialization: Implications for Interstellar Migrations" Interstellar Migration and the Human Experience star lifting` | thin | Confirms chapter, 1985, pp. 50 to 87 (UC Press); no text |
| 15 | 2026-10-11 | Internet Archive search and metadata for `interstellarmigr0000unse` and `interstellarmigr0000unse_h4h6`; search-inside endpoint queried for "Mercury", "disassemble", "dismantle" | dead at the sources | Both copies are lending-restricted; search-inside returns "Item not available". Criswell's chapter not read |
| 16 | 2026-10-11 | WebSearch (extended): `Criswell 1985 "Interstellar Migration" chapter planets dismantled Mercury mass energy "star lifting" summary review` | thin | Secondary summaries only; confirms Criswell coined star lifting (already in the starlifting file) |
| 17 | 2026-10-11 | arXiv API: `Dyson swarm construction`; `Dyson sphere Mercury disassembly`; OpenAlex: `Dyson swarm construction self-replicating Mercury` | useful | Surfaced Lacki 2025 (collisional cascades), Jones 1985 (IAU), "Ringworlds and Dyson spheres can be stable" (2025), Margot et al. 2018; most arXiv hits irrelevant (robot swarms) |
| 18 | 2026-10-11 | Opened Jones, "Where are they? Implications of ancient and future migrations", IAU Symp. 112 (1985), doi:10.1017/S0074180900146844 (Cambridge PDF) | useful (qualitative) | "Convert a bit of Mercury into a swarm of near-Sun power stations"; Clarke Station 150,000 TW at 20 solar radii, checked below |
| 19 | 2026-10-11 | Opened Lacki, "Ground to Dust: Collisional Cascades and the Fate of Kardashev II Megaswarms", ApJ 985:191 (2025), doi:10.3847/1538-4357/adccc5 | useful | Collisional time = orbital period / covering fraction; Table 1 values for a solar twin |
| 20 | 2026-10-11 | Opened Margot, Hauck, Mazarico, Padovan, Peale, "Mercury's Internal Structure", arXiv:1806.02024 (6 Jun 2018; chapter in *Mercury: The View after MESSENGER*, CUP) | useful | Tables 4 to 6: layer masses of 1,479 best-fit models; PRMM; core radius 2,024 +/- 9 km; used to test Armstrong and Sandberg's "70% metal" |
| 21 | 2026-10-11 | Fetched NSSDC Mercury fact sheet (updated 11 Jan 2024) and Sun fact sheet (9 May 2024) | useful | Mass, GM, radius, irradiance 9,082.7 W/m^2, rotation 1,407.6 h, L_sun 3.828 x 10^26 W |
| 22 | 2026-10-11 | Calculation: reproduction of Armstrong and Sandberg sec. 4.2 (`calc/as_model.py`, `as_model_output.txt`, `as_model_variants.txt`) and physical-limit checks (`as_physical_limits.py`, `as_physical_limits_output.txt`) in the scratch subfolder | useful | Reproduces 35.6 yr against the paper's 31.2 yr; see Derived figures |
| 23 | 2026-10-12 | WebSearch: `Lofstrom "launch loop" AIAA 1985 paper capacity tonnes per year power length 2000 km` | useful (leads) | Wikipedia and NSS summaries (secondary); led to the primary |
| 24 | 2026-10-12 | Opened NSS page https://nss.org/settlement/nasa/Nowicki/SPBI116.HTM | thin | One-paragraph summary; "minimum mass 10^4 tons" |
| 25 | 2026-10-12 | Opened Lofstrom, "The Launch Loop: a low cost Earth-to-high-orbit launch system" (AIAA 85-1368, 1985; author's 2002 transcription), http://launchloop.com/LaunchLoop?action=AttachFile&do=get&target=launchloop.pdf | useful | Ribbon mass, power, thermal launch-rate limit, capacity |
| 26 | 2026-10-12 | WebSearch: `Benz Anic Horner Whitby 2007 "The origin of Mercury" giant impact mantle stripping Space Science Reviews` | useful (leads) | Paper located; summary numbers from press (secondary) |
| 27 | 2026-10-12 | Download attempts: doc.rero.ch PDF, lpl.arizona.edu PDF, Springer PDF (with and without cookies), Springer article page via WebFetch | dead at the sources | rero returned HTML, LPL 404, Springer behind a cookie/login redirect. Benz et al. 2007 not read |
| 28 | 2026-10-12 | Opened Franco, Roig, Winter, Sfair, Burger, Schaefer, "Forming Mercury by a grazing giant collision involving similar mass bodies", arXiv:2503.02826 (4 Mar 2025), abstract and HTML full text | useful | Impact parameters for natural mantle stripping; summarizes Benz et al. 1988 and Asphaug and Reufer 2014 |
| 29 | 2026-10-12 | WebSearch: `Ellery self-replicating machines lunar feasibility paper energy limits J. Spacecraft Rockets` | useful | Ellery 2016 (doi:10.2514/1.A33409) located at carleton.ca; IAC-17 "Exponential populations of solar power satellites" surfaced |
| 30 | 2026-10-12 | Opened Ellery, "Are Self-Replicating Machines Feasible?", J. Spacecraft and Rockets 53(2), 2016, doi:10.2514/1.A33409 (carleton.ca PDF) | thin | Two-column text extraction interleaved; used only for the paper's stated conclusion and closure concept; no replication time or growth rate found in it |
| 31 | 2026-10-12 | Fetched Angel, "Feasibility of cooling the Earth with a cloud of small spacecraft near the inner Lagrange point (L1)", PNAS 103(46), 2006 (PMC1859907), twice (summary, then verbatim sentences) | useful | The one published design that builds a swarm by electromagnetic launch: areal density, launcher, rate, years |
| 32 | 2026-10-12 | WebSearch: `rotating tether "characteristic velocity" Spectra Zylon tether mass ratio tip velocity Hoyt Forward NIAC report pdf` | useful (leads) | Led to Forward and Nordley 1999 |
| 33 | 2026-10-12 | Opened Forward and Nordley, "Mars-Earth Rapid Interplanetary Tether Transport (MERITT) System: I. Initial Feasibility Analysis" (1999), https://marspapers.org/paper/Forward_1999.pdf | useful | Tether mass-ratio equation and Spectra 2000 table; one unit typo found (Conflicts) |
| 34 | 2026-10-12 | WebSearch: `laser ablation rock vaporization specific energy J/kg asteroid "mass ejection" Lubin DE-STAR planetary defense paper` | useful (leads) | |
| 35 | 2026-10-12 | Opened Lubin et al., "Toward directed energy planetary defense", Optical Engineering 53(2), 025103 (Feb 2014), UCSB PDF | useful | Heats of vaporization and plume speeds (Table 1); "of order 10^10 J" per m^3 to vaporize |
| 36 | 2026-10-12 | WebSearch: `Sedan crater Plowshare 104 kiloton "12 million tons" displaced NNSS fact sheet`; opened NNSS fact sheet NNSS-SEDN-U-0047 Rev01 (2023) | useful | Nuclear excavation anchor |
| 37 | 2026-10-12 | Fetched IAC-17 abstract, Ellery, "Exponential populations of solar power satellites tending to zero specific cost" (iafastro.directory) | thin | Abstract has no numbers; full paper restricted (dead at the sources for the numbers) |
| 38 | 2026-10-12 | WebSearch (extended): `self-replicating space industry growth model power limited doubling time Dyson swarm construction timescale peer-reviewed analysis bottleneck` | useful (leads) | Surfaced Shubov 2021 and Jensen 2023 (both arXiv, not peer reviewed); a popular page restating the 31-year figure (not used) |
| 39 | 2026-10-12 | Opened Shubov, "Guided Self Replicating Factory for Colonization of Solar System", arXiv:2110.15198v3 (21 Dec 2021, physics.pop-ph) | useful (low weight) | 50 doublings to 10^19 t and 3 x 10^24 W; no engineered doubling time |
| 40 | 2026-10-12 | Opened Jensen, "Autonomous Restructuring of Asteroids into Rotating Space Stations", arXiv:2302.12353 (Feb 2023) | useful (low weight) | A partial-harvest alternative: one asteroid, 12-year simulated build |
| 41 | 2026-10-12 | Opened McInnes, "Ringworlds and Dyson spheres can be stable", MNRAS 537:1249 (2025), doi:10.1093/mnras/staf028 (arXiv:2502.12806) | useful | Dynamical (not structural) stability of a shell in the restricted three-body problem |
| 42 | 2026-10-12 | arXiv API: `Hephaistos Dyson sphere candidates Gaia WISE`; `Dyson sphere upper limit infrared survey` | useful | Detection literature located; a third API call hit "Rate exceeded" (dead at the sources for that call; re-fetched via abstract pages) |
| 43 | 2026-10-12 | Fetched abstracts: Suazo et al., "Project Hephaistos II", arXiv:2405.02927 (MNRAS, 2024); Zackrisson et al., "Project Hephaistos IV: JWST observations of two Dyson sphere candidates", arXiv:2607.09460 (10 Jul 2026) | useful | 7 candidates from 5 million objects; two re-observed with JWST and explained by background galaxies |
| 44 | 2026-10-12 | Opened Bradbury, "Matrioshka Brains" index (archived 23 Feb 2009), https://web.archive.org/web/20090223093348/http://aeiveos.com:8080/~bradbury/MatrioshkaBrains/index.html | useful | Links to the "Planetary Disassembly" page |
| 45 | 2026-10-12 | Opened Bradbury, "Planet Disassembly" (web page, created 4 May 1998, last modified 24 Aug 2006), archived at https://web.archive.org/web/2009id_/http://aeiveos.com:8080/~bradbury/MatrioshkaBrains/PlntDssmbly.html | useful | This is the "unpublished analysis" Armstrong and Sandberg credit; binding-energy table, mechanism, the power-delivery limit A&S do not carry; one factor-of-2 error found |
| 46 | 2026-10-12 | Fetched NIST Chemistry WebBook: Al2O3 (C1344281) and quartz SiO2 (C14808607), enthalpy of formation | useful | To test A&S's "less than one megajoule per mol" for chemical bonds |
| 47 | 2026-10-12 | WebSearch: `slingatron Tidman mass launcher bulk material throughput tons per day velocity paper` | thin | Patent, NSS conference paper and press; no throughput figure; not used beyond "no throughput figure found" |
| 48 | 2026-10-12 | Fetched NSSDC Venus fact sheet (updated 11 Jan 2024) | useful | Semimajor axis 108.210 million km, for Bradbury's Venus-orbit sphere check |
| 49 | 2026-10-12 | Calculation: `calc/scaling.py`, output `calc/scaling_output.txt` | useful | Mechanism counts for 31, 100, 1,000 years; elevator geometry; tether, ablation, bond-energy and source cross-checks |
| 50 | 2026-10-12 | OpenAlex record for doi:10.1016/j.actaastro.2013.04.002 (published *Acta Astronautica* 89:1-13, 2013) | thin | Closed access; published version not read. A forum lead (row 52) says the published text cut the launch-phase section; every A&S figure here is from the preprint and is labeled so |
| 51 | 2026-10-12 | Opened Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", arXiv:1712.02187 (2017; chapter in *Mercury: The View after MESSENGER*) | useful | Second angle on the core: core mass fraction 69 to 77% (citing Hauck et al. 2013); surface Fe 1 to 2 wt% |
| 52 | 2026-10-12 | WebSearch: `"Eternity in six hours" critique OR rebuttal Armstrong Sandberg assumptions Dyson swarm Mercury disassembly unrealistic` | thin | Forum threads (LessWrong, EA Forum) and a 2012 PopSci article; no peer-reviewed critique found (dead at the sources for primary critiques). Forum claims tested by my own arithmetic, not cited as evidence |
| 53 | 2026-10-12 | WebSearch: `space elevator Mercury synchronous orbit outside Hill sphere slow rotation tether planet` | useful (secondary) | Wikipedia "Synchronous orbit" (via search summary) gives Mercury's synchronous semimajor axis 242,895 km and "not within its Hill sphere"; agrees with my derivation (2.429 x 10^8 m). No Mercury elevator study found |
| 54 | 2026-10-12 | WebSearch: `thermodynamic limit solar concentration 46,000 suns etendue Gleckman O'Gallagher Winston 1989 Nature 84,000 suns`; fetched Optica OPN page for Gleckman, O'Gallagher, Winston (1 May 1989) | thin | Confirms 56,000-fold concentration demonstrated and "approach the thermodynamic limit"; the numeric limit statement is in the PDF, not read |

## Findings

**Reading key.** "A&S" is Armstrong and Sandberg, "Eternity in six hours" (preprint of 12 Mar 2013, Wayback copy, log row 4; the
published *Acta Astronautica* 89:1-13 version is closed access and was not read). Sibling files are cited as **[RM]**
`industrial_ramp_timelines.md`, **[TR]** `space_trucking_and_transport_infrastructure.md`, **[PR]** `space_processing_and_fabrication.md`,
**[IMS]** `inner_system_mining_synthesis.md`, **[SYN]** `starlifting_synthesis.md`. "calc [n]" is a numbered line of
`calc/scaling_output.txt`; "repro" is `calc/as_model_output.txt`, `as_model_variants.txt` and `as_physical_limits_output.txt`.

### F1. The primary sources and what each actually specifies (checklist 1)

The headline: **no source found is an engineering design for disassembling a planet.** Every one is a thought experiment,
an order-of-magnitude argument, a web essay or a student paper. The only quantitative designs anywhere in the chain are the
1970s lunar mass driver and mass catcher (SP-428, SP-413), which each move under a megatonne per year.

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Dyson 1960: the argument for using a planet's mass (SPECULATIVE) | Accessible mass "2 x 10^30 grams (the mass of Jupiter)"; Sun "4 x 10^33 ergs per second"; growth by a factor of 10^12 in "say 3000 years" at 1%/yr; "the energy required to disassemble and rearrange a planet the size of Jupiter is about 10^44 ergs, equal to the energy radiated by the sun in 800 years"; Jupiter's mass as a shell at 2 AU is 200 g/cm^2, "2 to 3 meters" thick. **No mechanism, no design, no time to do it.** Exponents reconstructed (OCR dropped them): 1.01^3000 = 9.2 x 10^12; 800 yr x 4 x 10^33 erg/s = 1.0 x 10^44 erg (calc [14]); 4 x 10^33 erg/s matches NSSDC's 3.828 x 10^26 W; the Jupiter mass matches Bradbury's quotation | Dyson, "Search for Artificial Stellar Sources of Infrared Radiation", *Science* 131:1667-1668, 3 Jun 1960, https://archive.org/details/dyson-1960-search-for-artificial-stellar-sources-of-infrared | Primary | Bradbury (row 45) quotes the same 2 x 10^27 kg, 800 years, 10^44 ergs; Smith 2021 quotes "between 2 and 3 metres thick" | High (as stated) |
| Dyson's 10^44 erg versus the binding energy | 10^37 J is about 5 times Jupiter's uniform-sphere binding energy (2.04 x 10^36 J, Bradbury's table), i.e. 169 yr of the Sun's whole output (calc [14]); Bradbury reads the difference as Dyson including "rearrange" | Bradbury, "Planet Disassembly" (row 45); DERIVED | Secondary (web essay) for the reading | none | Medium |
| Dyson 1966 (not read) | Per Wright 2020: no physical barrier to large rigid structures up to 10^6 km; planets "can (in principle) be deconstructed for their material in sufficient quantities to build a sphere of useful thickness (of order meters)" | Dyson, "The search for extraterrestrial technology", in *Perspectives in Modern Physics* (Marshak ed.), 1966, as summarized by Wright 2020 | Secondary (summary only) | none found | Low: the text, mechanism and numbers were not reachable (rows 9 to 11) |
| Bradbury, "Planet Disassembly": the uncredited source of A&S's model (SPECULATIVE) | Binding energies (Mercury 1.80 x 10^30 J) and times at 35% of the Sun's output (1.15 x 10^26 W): Mercury 5 hours, Venus 16 days, Earth 22 days, Jupiter 563 years; method: "a von Neumann automated factory" on Mercury, solar cells over the surface, "mining machines then burrow into the planet, cutting planetary materials into convenient blocks which are delivered to rail guns"; Mercury's surface alone "~3.4 x 10^17 W ... disassembly in ~550,000 years"; with collectors made from the launched mass, "a fully efficient cycle would allow the disassembly of Mercury in less than month!"; areal density of all of Mercury spread at its orbit 7.8 kg/m^2 (Venus at its orbit 33 kg/m^2) | Bradbury, "Planet Disassembly", web page created 4 May 1998, last modified 24 Aug 2006, archived https://web.archive.org/web/2009id_/http://aeiveos.com:8080/~bradbury/MatrioshkaBrains/PlntDssmbly.html | Secondary (unreviewed web essay; A&S call it "Robert Bradbury's unpublished analysis") | Binding energy matches the brief's 1.79 x 10^30 J; 7.8 and 33 kg/m^2 reproduce (3.301 x 10^23 / 4.214 x 10^22; 4.867 x 10^24 / 1.471 x 10^23, calc [15]) | Medium for its arithmetic; it is not an engineering study. **Error:** the 3.4 x 10^17 W surface figure is 2.00 times the sunlight Mercury intercepts (calc [13]; Conflicts) |
| Bradbury: the limit he names that A&S drop | "At some point, the amount of power available in space, significantly exceeds the power which can be delivered to the planet in a useful form"; offers three fixes (vaporize the planet, cut it into planetesimals, raise collectors on columns) and says "further studies are needed" | Bradbury (as above) | Secondary | Quantified here in F4 and Derived D3 | Medium |
| Sandberg, "Dyson Sphere FAQ" (SPECULATIVE) | Self-replicating machinery could convert "the asteroid belt and minor moons ... into habitats in a few years, while disassembly of larger planets would take 10-1000 times longer (depending on how much energy and violence was used)"; usable inner-system mass 11.79 x 10^24 kg giving "around 42 kg/m^2" at 1 AU; Jupiter "~58" and Saturn "~17" x 10^24 kg usable (rough) | Sandberg, "Dyson Sphere FAQ", nada.kth.se (archived 2006; A&S ref. 33) | Secondary (FAQ; numbers from Lewis, *Physics and Chemistry of the Solar System*) | 42 kg/m^2 reproduces (11.79 x 10^24 / 2.812 x 10^23 = 41.9, calc [15]) | Low for times (no derivation given); one table error (Earth mass, Conflicts) |
| Jones 1985 (qualitative) | "Imagine setting them loose (with built in controls), to convert a bit of Mercury into a swarm of near-Sun power stations. With one percent of the Sun's output at their command..."; "Clarke Station with a 1000-kilometer-diameter collector (150,000 terawatts at 20 solar radii)" | Jones, "Where are they? Implications of ancient and future migrations", IAU Symposium 112, 1985, doi:10.1017/S0074180900146844 | Primary (proceedings) but qualitative | Clarke Station power DERIVED as 123,600 TW (calc [12]), 21% below the stated figure | Medium (a vision, not a design) |
| Criswell 1985 (not read) | Coined "star lifting"; chapter "Solar System Industrialization: Implications for Interstellar Migrations", pp. 50-87 in Finney and Jones (eds.), *Interstellar Migration and the Human Experience*, UC Press 1985; Wright 2020 cites it for "the mechanics of deconstructing planets or stars" | Search summaries (rows 14, 16); Wright 2020 | Secondary | Its starlifting content is in the starlifting file ([SYN] section 2) | Low: the book is lending-restricted (row 15). **Gap** |
| Wright 2020 review | A monolithic shell needs an elastic modulus E >~ GM rho / Delta-R, "~10^13 GPa" for 1 g/cm^3 and 10 m, "nine orders of magnitude" above carbyne, so swarms, not shells; radiation pressure balances gravity at about 0.8 g/m^2; to gain each further "nine" of efficiency a sphere needs 10^3 times more radiating area (A = 4 pi R*^2 (1-eta)^-3, or ^-4 for dissipative work); a nominal 1 AU sphere runs at 160 K, 97% (or 390 K, 93%); Landauer-limited computing about 10^47 operations per second for that sphere; lists planet deconstruction as an "ignored" practical issue | Wright, "Dyson Spheres", *Serbian Astronomical Journal* 200 (2020), arXiv:2006.16734v3, 7 Oct 2020 | Primary (peer-reviewed review) | McInnes 2025 (next row) on dynamics; the swarm conclusion matches Dyson's own 1960 reply as quoted by Wright | High |
| McInnes 2025 | A uniform shell or ring "can be stable in the restricted three-body problem" if it encloses the smaller of two primaries, "under certain conditions"; dynamics only, not material strength | McInnes, "Ringworlds and Dyson spheres can be stable", *MNRAS* 537:1249-1267, 2025, doi:10.1093/mnras/staf028 | Primary | Does not answer Wright's buckling limit (different problem) | High (as stated) |
| Lacki 2025: the swarm's own debris problem | Collisional time "roughly an orbital period divided by the covering fraction"; for a full swarm at 1 AU around a solar twin, naive collision time 0.16 yr and cascade time 0.0063 yr; a 340-element "minimal occulter" swarm 1.0 x 10^6 yr; Jupiter "would destroy a megaswarm at Earth's place in a few hundred thousand years" unless maintained; "Most megaswarms are thus likely to be short-lived on cosmic timescales without active upkeep" | Lacki, "Ground to Dust: Collisional Cascades and the Fate of Kardashev II Megaswarms", *ApJ* 985:191, 2025, doi:10.3847/1538-4357/adccc5 | Primary | Wright 2020 also notes the need for course correction | High (as modeled) |
| Detection (to date) | Hephaistos II: 7 candidates (all M dwarfs) from 5 million objects in Gaia, 2MASS and WISE; Hephaistos IV (JWST/MIRI, 2026): two of them (D, E) are background galaxies "within ~1 arcsec", not megastructures | Suazo et al., arXiv:2405.02927 (MNRAS 2024); Zackrisson et al., arXiv:2607.09460 (10 Jul 2026) | Primary | A 2024 contamination paper (arXiv:2405.14921, title only) and a radio-imaging paper on candidate G (arXiv:2501.05152, title only) surfaced, not read | High: no Dyson structure has been detected |
| Smith 2021 (student) | Swarm of 5.51 x 10^9 satellites (about 290 kg each) built on Mars, launched by mass driver into Mars orbit, to supply 18.5 TW to Earth; 47, 60 or 83 years at 90, 70, 50% power reinvestment **only when one new mass driver is added each year**; with one mass driver, growth is linear and the target is not met in 125 years | Smith, "Viability of a Dyson Swarm as a Form of Dyson Sphere", arXiv:2109.11443v1, 20 Sep 2021 (physics.pop-ph) | Not peer reviewed (low weight) | Internal checks fail on two numbers (Conflicts) | Low to medium |
| Shubov 2021 (student) | "After about 50 doubling periods" a guided self-replicating factory reaches "10^19 tons of structure and machinery" and "3 x 10^24 W"; "Building a fully robotic and independent, self replicating factory is beyond current technological capabilities" | Shubov, arXiv:2110.15198v3, 21 Dec 2021 (physics.pop-ph) | Not peer reviewed (low weight) | 10^19 t = 10^22 kg = 3% of Mercury (DERIVED) | Low |

#### F1b. Armstrong and Sandberg, every parameter of the Mercury model (preprint sec. 4.1, 4.2, 6.3)

All ENGINEERING-STUDIED? **No: SPECULATIVE** ("exploratory engineering"). The paper prints the assumptions and the result, two
figures, and **no equations**.

| Quantity | Value and units (verbatim where quoted) | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Framing assumptions | "anything possible in the natural world can also be done under human control"; "any task that can be performed, can be automated"; self-replicators and AI "plausibly available to humans over the next few millennia" | A&S sec. 2 | Primary (preprint) | none | High that this is what it says |
| Swarm design | Swarm at Mercury's semimajor axis 5.79 x 10^10 m, sphere area "about 4.21 x 10^22 m^2"; 50% of Mercury's mass "transformed into reflective surfaces"; 0.5 x 3.3022 x 10^23 / 4.21 x 10^22 = "3.92 kg/m^2", "0.5 mm" of iron; likely "a very thin film (of order 0.001 mm) supported by a network of more rigid struts" | A&S sec. 4.1 | Primary (preprint) | Area 4.214 x 10^22 m^2 (calc [15]); 3.92 kg/m^2 / 7,874 kg/m^3 = 0.50 mm (reproduced) | High (arithmetic) |
| Composition assumed | "mainly composed of 30% silicate and 70% metal, mainly iron or iron oxides" | A&S sec. 4.1, citing Strom and Sprague 2003 | Primary (preprint) | Core mass fraction 69 to 77% (Nittler et al. 2017, citing Hauck et al. 2013); 74% median (Margot et al. 2018: core 2.441 x 10^23 of 3.301 x 10^23 kg); the core is an Fe-Si(-S) metal (PRMM uses 12.83 wt% Si), and the silicate surface holds only 1 to 2 wt% Fe | The 70% is right; "iron oxides" is not supported (Conflicts) |
| Energy to remove | Binding energy "1.80 x 10^30 J"; "Lifting a kilo of matter to escape velocity on Mercury requires about nine megajoules" | A&S sec. 4.2 | Primary (preprint) | v_esc 4,250 m/s and 9.031 MJ/kg from NSSDC GM and radius (calc [1]); binding 1.789 x 10^30 J (brief, and repro) | High |
| Assumption 1 | "overall efficiency of the solar captors is 1/3, by the time the solar energy is concentrated, transformed and beamed back to Mercury" | A&S sec. 4.2 | Primary (preprint) | no study of this chain at this scale found (section 4 agent's topic) | Assumption |
| Assumption 2 | "initial energy generating source will be a 1 km^2 array of solar panels, constructed on Mercury itself" | A&S sec. 4.2 | Primary (preprint) | Gives 3.03 GW at 9,082.7 W/m^2 and 1/3 (repro); ignores the 88-day night ([IMS] section 3) | Assumption |
| Assumption 3 | "Of the energy available, 1/10 will be used to propel material into space ... the rest going to breaking chemical bonds, reprocessing material, or just lost"; "chemical bonds have energy less that one mega-joule per mol. These numbers are comparable" | A&S sec. 4.2 | Primary (preprint) | NIST: Al2O3 formation enthalpy -1,675.7 kJ/mol (above 1 MJ/mol); per kg, Al2O3 16.4 and SiO2 15.2 MJ/kg, 1.7 to 1.8 times the lift energy (calc [9]); demonstrated molten-regolith electrolysis ([TR]/[PR]: 104 to 135 kWh per kg O2) exceeds the 81 MJ/kg non-launch budget for any material above 17 to 22 wt% oxygen (calc [10]) | Assumption; the "comparable" sentence mixes per-mol and per-kg (Conflicts) |
| Assumption 4 | "It takes five years to process the material into solar captors and place them in the correct orbit" | A&S sec. 4.2 | Primary (preprint) | No engineering study gives any processing-to-orbit time for this; it is the dominant parameter (F1c) | Assumption |
| Assumption 5 | "Half of the planet's material will be suitable to construct solar captors" | A&S sec. 4.2 | Primary (preprint) | The first 26% removed (mantle and crust, 8.6 x 10^22 kg) is silicate with 1 to 2 wt% Fe (Margot; Nittler); A&S note "more wasted material initially" | Assumption |
| Result | "Mercury itself will be completely disassembled in 31 years and 85 days, with most of the mass loss happening in the last 4 years"; power grows "in five-year cycles, which gradually smooth out to become linear on the log scale" | A&S sec. 4.2, Figs. 2 and 3 | Primary (preprint) | My reproduction from the stated assumptions: 35.6 years, 99% of the mass removed in the last 4.7 years (F1c) | Medium: not reproduced exactly; equations not given |
| Authors' own caveats | "It would cost a lot and would be unlikely to be attempted, but there are no fundamental technological barriers"; "there are worries as to how the core could be cooled during disassembly"; placement "would be more complicated once there are a lot of other captors already in place" | A&S sec. 4.2 | Primary (preprint) | n/a | High |
| Robustness claim | "planetary disassembly and launch time scales linearly with the available energy"; swarm needs "less than 0.1% of the total planetary mass" | A&S sec. 6.3 | Primary (preprint) | Mercury is 0.012% of total planetary mass (DERIVED from Sandberg FAQ's 2,657 x 10^24 kg sum; consistent). The time does **not** scale linearly in the feedback model: 10x lower efficiency gives 59.3 yr, not 356 (F1c) | Medium |
| Launch-system efficiency (for probes, not the mining) | "theoretical efficiency of coilguns, given superconductors, seems to be close to 1"; assumed "at least 50%" | A&S sec. 4.3 | Primary (preprint) | SP-428 III-3 launcher 96.4% ([TR] F2), a 1977 design, unbuilt | Assumption |

#### F1c. Reproduction and sensitivity of the A&S model (DERIVED; scripts `calc/as_model.py`, `as_physical_limits.py`)

My reading of the five assumptions: power P = (1/3) x 9,082.7 W/m^2 x (1 km^2 + captor area); launch rate = P/10 / 9 MJ/kg;
mass launched becomes captors 5 years later at 0.5 kg per kg launched and 3.92 kg/m^2. One-day steps (half-day steps change
the result by 0.01 yr).

| Case (one change from base) | Time to remove all of Mercury |
|---|---|
| Base (stated assumptions) | **35.6 yr** (paper: 31.2 yr). 1% removed at 30.9 yr, 50% at 35.0, 90% at 35.5 |
| Lift energy falling as (M/M0)^(2/3) as the planet shrinks | 35.2 yr (the constant 9 MJ/kg overstates total lift energy by 1.66 times: 2.97 x 10^30 J against 1.79 x 10^30 J) |
| Initial array without the 1/3 factor / all launched mass usable / lift to orbit only (4.5 MJ/kg) / delay 4 yr | 34.6 / 32.2 / 31.5 / 29.8 yr (the paper's 31.2 lies inside this spread) |
| Delay 1 / 2 / 10 / 20 yr | 10.0 / 17.1 / 62.9 / 112.2 yr |
| Efficiency 1/30 / 1/300 (or launch share 1/100 / 1/1000) | 59.3 / 125.3 yr |
| Seed 0.01 km^2 / 100 km^2 | 40.4 / 30.9 yr |
| Areal density 39.2 / 392 kg/m^2 (or usable 5%) | 55.5 / 110.0 yr |
| A hardware cap of N lunar-design launchers at 42 kg/s each (linear phase) | 2.5 x 10^14 yr / N (10^9 launchers: 249,000 yr) |

**What the reproduction shows:** the result is set by the processing delay (in the late phase power grows tenfold every 2.0 to 2.8
years, about five e-foldings per 5-year delay) and by the absence of any hardware ceiling; efficiency and seed size move it only logarithmically. The model has no
term for launcher count, catcher count, heat rejection, or how much power the planet's surface can accept.

### F2. Mass-lifting mechanisms and what limits each at planetary throughput (checklist 2)

Throughput needed for reference (calc [2]; uniform rate, Mercury's escape energy 9.03 MJ/kg, 96.4% launcher efficiency):
**whole planet in 31 / 100 / 1,000 years = 3.4 x 10^14 / 1.0 x 10^14 / 1.0 x 10^13 kg/s, needing 3.2 x 10^21 / 9.8 x 10^20 /
9.8 x 10^19 W of launch power, which is 18,600 / 5,800 / 580 times all the sunlight Mercury intercepts (1.70 x 10^17 W).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mass driver (anchor, ENGINEERING-STUDIED) | Lunar point design: 2,400 m/s, 1,000 g, 488 m, 125 MW, 42 kg/s (650,000 t/yr), 96.4%, 3,130 t | [TR] F2 (NASA SP-428 III-3, 1977) | Primary via sibling | [TR] reproduces 121 MW from 42 kg/s | Medium (unbuilt) |
| Mass driver at Mercury | 4.25 km/s needs 0.92 km of track at 1,000 g; 0.29 to 0.30 GW per Mt/yr ([IMS] section 3). Whole planet in 1,000 yr needs 2.5 x 10^11 such launchers (7.8 x 10^17 kg of launcher, 0.24% of Mercury); in 31 yr, 8.0 x 10^12 (calc [2]) | [IMS]; DERIVED | Derived | n/a | Medium |
| Mass driver: what limits it | Hardware count and siting, not physics per unit: at the end of the A&S schedule the flow is 1.08 x 10^16 kg/s, i.e. 2.6 x 10^14 lunar-design launchers, **3.4 per square meter of Mercury's whole surface**, or the entire surface receding at 4.0 to 4.6 km per day (repro) | DERIVED from SP-428 and Margot crust density 2,700 to 3,100 kg/m^3 | Derived | n/a | High (arithmetic) |
| Coilgun/quenchgun efficiency claims | "theoretical efficiency ... close to 1" (A&S, citing Kolm et al. 1980 and others) | A&S sec. 4.3 | Primary (claim) | The Kolm et al. MIT report was not opened | Low (theory, unbuilt) |
| Smith 2021 mass driver | 290 kg at 3.52 km/s, 10 km, stated 871 MW; one launch per 5 s per driver | Smith 2021 | Not peer reviewed | My check: 316 MW mean over the shot, 359 MW averaged over 5 s (calc [17]); 871 MW not reproduced | Low |
| Electromagnetic launch of a swarm, designed (ENGINEERING-STUDIED) | Angel 2006 sunshade: 1,000-kg payloads of 800,000 flyers each, 3.1-t vehicles, 12.8 km/s, 2,000 m track at 4,200 g, 20 launchers each fired "a million times on a 5-min cycle", 640 GJ storage per launcher, 40% efficient; ~20 million tons in total | Angel, "Feasibility of cooling the Earth with a cloud of small spacecraft near the inner Lagrange point (L1)", *PNAS* 103(46):17184, 2006, PMC1859907 | Primary | Energy check 6.35 x 10^11 J (calc [3]); throughput 2.1 x 10^9 kg/yr of payload; 1 million shots = 9.5 yr | Medium (study, unbuilt) |
| Launch loop (ENGINEERING-STUDIED, 1985) | 15,600 t iron ribbon at 14 km/s; 5-t vehicles "at rates of up to 80 per hour", a rotor-heating limit; 17 GW at that rate; 500 MW gives 35 vehicles a day; "3.5 million tons per year capacity of the basic system" | Lofstrom, "The Launch Loop", AIAA 85-1368 (1985; author's 2002 transcription) | Primary | 80/hr x 5 t = 3.51 x 10^9 kg/yr (calc [4]); NSS summary says minimum mass 10^4 t | Medium (unbuilt). Its purpose is to rise above an atmosphere; Mercury has none, so it offers no advantage there over a surface driver |
| Space elevator at Mercury | Stationary orbit radius 2.43 x 10^8 m lies **outside** Mercury's Hill radius 2.21 x 10^8 m (ratio 1.10); Mercury spins exactly 1.5 times per orbit, so an elevator through the Sun-Mercury L1 point would not stay over one spot either (calc [5]). **No stationary or L1-anchored Mercury elevator is geometrically possible** | DERIVED from NSSDC; secondary confirmation: Wikipedia "Synchronous orbit" (242,895 km, "not within its Hill sphere", row 53) | Derived | agrees | High |
| Rotating tether (skyhook) | Mass of one arm per payload grows as exp((V/Vc)^2); Spectra 2000 (4.0 GPa, 970 kg/m^3) gives Vc 2.87 km/s ultimate, 1.66 to 2.17 km/s with safety factors 3.0 to 1.75; tether-to-payload mass 2.2 to 4.9 at 1.5 km/s, 8 to 30 at 2.5 km/s | Forward and Nordley, MERITT I (1999), https://marspapers.org/paper/Forward_1999.pdf | Primary (conference paper) | Vc recomputed 2,872 m/s (calc [6]); MXER (100 km, 2 g) in [TR] F2 | Medium. At Mercury a skyhook touching down at rest needs a tip speed near the 3.0 km/s surface orbital speed (calc [1]), beyond Forward's table; usable only as a partial-velocity stage. **No momentum-exchange throw has flown** ([TR] F2) |
| Slingatron | Claims of tons to above 10 km/s and "many thousands of launches per year" | Search summaries of Tidman patents and NSS papers (row 47) | Secondary | none | Low: no throughput figure found |
| Laser or thermal ablation | Heats of vaporization SiO2 2.38, Al2O3 2.87, MgO 8.21 MJ/kg; "of order 10^10 J" per m^3; plume characteristic speeds 1.54 to 2.87 km/s; significant vaporization above about 2 MW/m^2 | Lubin et al., "Toward directed energy planetary defense", *Opt. Eng.* 53(2):025103, Feb 2014 | Primary | Bradbury: surface boiling points 2,500 to 3,800 K, vaporization "efficiencies ... high", no time estimate | Medium. **At Mercury the plume speeds are 0.36 to 0.68 of escape speed (calc [8]); ablation alone does not lift material off Mercury** (it does off asteroids) |
| Nuclear excavation (DEMONSTRATED as excavation) | Sedan, 6 Jul 1962: 104 kt, 635 ft deep, "approximately 12 million tons of earth" displaced, crater 1,280 ft across and 320 ft deep | NNSS fact sheet NNSS-SEDN-U-0047 Rev01 (2023) | Primary | Search summary agrees | High. 0.040 MJ per kg displaced against 9.03 MJ/kg to escape (calc [11]): an excavation tool, not a launcher |
| Giant impact (natural precedent) | Mercury-like body (0.052 to 0.056 Earth masses, iron fraction 0.65 to 0.73) formed when a 0.13-Earth-mass proto-Mercury hit a 0.2 to 0.6 Earth-mass target at 2.96 to 3.78 times mutual escape speed (about 22 to 25 km/s), angle 31.6 to 41 degrees, mantle "almost completely stripped"; earlier model: 2.25 times Mercury's mass hit by a body six times smaller (Benz et al. 1988) | Franco et al., "Forming Mercury by a grazing giant collision involving similar mass bodies", arXiv:2503.02826 (4 Mar 2025) | Primary (preprint) | Benz et al. 2007 not reachable (row 27); Asphaug and Reufer 2014 named only | Medium. Kinetic energy of the projectile (the proto-Mercury itself, 2.36 Mercury masses = 7.8 x 10^23 kg) at 22 km/s is about 1.9 x 10^32 J, roughly 100 times Mercury's binding energy (DERIVED): an impact strip needs a planet-scale impactor |

### F3. Assembly, catching and the swarm's own mass and dynamics (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Catcher (ENGINEERING-STUDIED) | SP-413 mass catcher at Earth-Moon L2: 0.32 x 10^6 t/yr per catcher at 100% duty, radar acquisition 10 s and 2,000 m out | [TR] F4 (NASA SP-413 App. G, 1975) | Primary via sibling | n/a | Medium (unbuilt) |
| Catchers needed at planetary scale | Whole Mercury in 31 / 100 / 1,000 yr: 3.3 x 10^13 / 1.0 x 10^13 / 1.0 x 10^12 catchers; crust only in 1,000 yr: 2.5 x 10^10 (calc [2]) | DERIVED | Derived | n/a | High (arithmetic) |
| The two architectures in the literature | (a) Launch raw material, catch and process it in orbit (SP-413/SP-428 pattern; Bradbury; A&S "a factory reprocessed it"); (b) make the finished element on the surface and launch it whole (Angel 2006 flyers; Smith 2021 satellites). No source sizes the orbital factories of (a) at any planetary rate | A&S; Bradbury; Angel; Smith | Mixed | n/a | Medium |
| Areal mass of the published swarm elements | Dyson shell 200 g/cm^2 (2,000 kg/m^2); Sandberg 42 kg/m^2 (all inner-planet mass at 1 AU); Bradbury 7.8 kg/m^2 (all of Mercury at its orbit); A&S 3.92 kg/m^2; Smith about 0.92 kg/m^2 (290 kg per 314 m^2 mirror, calc [17]); Angel 4.2 g/m^2 (designed); Wright: radiation pressure equals gravity at about 0.8 g/m^2; opaque metamaterial films about 10^-5 g/cm^2 (0.1 g/m^2) | Sources as named | Mixed | n/a | Medium. Bradbury warns that collectors near 1 g/m^2 "become solar sails" and need active positioning |
| Structural stability | Rigid shell impossible by buckling (Wright eq. 22, ~10^13 GPa); swarm of independent orbits is the only form treated as buildable | Wright 2020 | Primary | McInnes 2025: shell dynamically stable only around the smaller of two primaries | High |
| Collisions in a full swarm | Collision time about P_orbit x 0.16 for a full swarm (Lacki Table 1 ratio, solar twin); **at Mercury's 88-day orbit about 14 days** (calc [7]); cascade time 25 times shorter still at 1 AU (0.0063 against 0.16 yr) | Lacki 2025; DERIVED | Primary / derived | none | Medium: the ratio is read off one table row and applied at a different radius |
| Placement | A&S: placing captors "would be more complicated once there are a lot of other captors already in place"; no source gives a placement rate or a traffic model | A&S | Primary (claim) | none | Gap |

### F4. Growth models: exponential versus bottleneck-aware (checklist 4)

Cited, not re-derived: CP-2255 (100 t seed, 1-year replication, 90 to 96% closure), Metzger et al. 2013 (12 to 41 t landed,
2-year generations, solar duty cycle "cutting it by less than a factor of two decreases the net growth by more than an order of
magnitude"), Ono 2025 (power and processing bottlenecks give linear growth) and Freitas and Merkle 2004: all in [RM] F4.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| A&S growth law | Power-limited exponential with a 5-year delay; no hardware, heat or delivery ceiling | A&S; reproduction (F1c) | Primary / derived | n/a | High that this is the structure |
| When A&S's power delivered to Mercury passes natural limits | Exceeds all the sunlight Mercury intercepts at year 20.1, when 2.4 x 10^-7 of the planet has been removed; 100 times at 24.4 yr (1.8 x 10^-5 removed); 10,000 times at 29.2 yr (0.16% removed). **More than 99.8% of the mass is removed while the planet receives over 10^4 times its natural sunlight** (repro) | DERIVED | Derived | n/a | High (arithmetic, given the model) |
| Final delivered flux | 1.3 x 10^10 W/m^2 averaged over the whole surface, **207 times the flux leaving the Sun's photosphere** (6.29 x 10^7 W/m^2, calc [16]); launcher losses alone (3.6% of launch power) give 4.7 x 10^7 W/m^2, a blackbody surface at about 5,400 K; if the other 90% is dissipated at the surface, about 21,000 K (repro) | DERIVED | Derived | Direct optical concentration is bounded by the source's flux (Gleckman, O'Gallagher and Winston 1989 reached 56,000-fold and "approach the thermodynamic limit", row 54), so this power must arrive converted and beamed, which A&S assume | High for the arithmetic; the conclusion that the schedule's last years cannot happen at the surface is mine |
| Launch-rate-limited growth (Smith 2021) | One driver at one launch per 5 s gives linear growth (6.3 x 10^6 launches a year; 5.51 x 10^9 satellites would take about 873 years, calc [17]); adding one driver per year makes it exponential: 47 to 83 years | Smith 2021 | Not peer reviewed | Agrees in kind with Ono 2025 ([RM] F4) | Low to medium |
| Bradbury's ideal case | "A fully efficient cycle would allow the disassembly of Mercury in less than month!" | Bradbury | Secondary | Lower bound only: binding energy over the full solar output is 4.3 hours (his table) | Low |
| Shubov 2021 | About 50 doublings to 10^22 kg of structure and 3 x 10^24 W; doubling time not engineered | Shubov 2021 | Not peer reviewed | n/a | Low |
| Jensen 2023 | Simulated restructuring of a ~5 km asteroid into a 5 km rotating station in about 12 years from one launch (4 robots grow to 3,000 plus 23,500 other machines) | Jensen, arXiv:2302.12353, Feb 2023 | Not peer reviewed | n/a | Low |
| Ellery 2016 | "physical self-replicating machines are within reach"; requires "100% matter, energy, and information closure" to be fully self-replicating | Ellery, *J. Spacecraft and Rockets* 53(2), 2016 | Primary (peer-reviewed) | CP-2255 recommends 90 to 95% closure plus imported "vitamins" ([RM] F4) | Medium for the claim; no growth rate given |

### F5. Every published timescale, and what it rests on (checklist 5)

| Claim | Source | What it assumes | Supported by any engineering study? |
|---|---|---|---|
| A planet-wide biosphere "within a few thousand years" of industrialization | Dyson 1960 | 1%/yr growth for 3,000 yr; energy of 800 years of sunlight for Jupiter | No: a growth-rate extrapolation |
| Mercury in 5 hours; Jupiter in 563 years | Bradbury table | 35% of the Sun's entire output delivered to the planet | No: an energy floor, not a schedule |
| Mercury in ~550,000 years from its own surface | Bradbury | 3.4 x 10^17 W (twice too high, F1) | No |
| Mercury in "less than [a] month" | Bradbury | "A fully efficient cycle" | No |
| Asteroids "in a few years"; planets "10-1000 times longer" | Sandberg FAQ | Self-replicating machinery | No: no derivation given |
| **Mercury in 31 years 85 days** | A&S 2013 | Automation and self-replication; 1/3 chain efficiency; 1/10 to launching; 5-year processing; 50% usable; unlimited launchers, catchers, factories and power delivery | **No.** Unsupported by any study: the 5-year processing-and-placement time, unlimited hardware scaling, full automation and self-replication, the delivery of up to 10^24 W to the planet's surface, heat rejection, and the 1/3 beamed-power chain. Reproduced at 35.6 yr from its own assumptions |
| Mars-based swarm for 18.5 TW in 47 to 83 years | Smith 2021 | One extra mass driver per year; 10^12 J per satellite | No (student paper); not a disassembly |
| "About 50 doubling periods" to a Dyson civilization | Shubov 2021 | Doubling time not engineered | No |
| One asteroid restructured in 12 years | Jensen 2023 | Simulated replicator rates | No (simulation, unpublished) |
| Commitment to 1 Mt/yr industry about 25 to 48 years (fast reading) | [SYN] sections 5 and 8, [RM] | Historical build-out analogs | Analog-based; the nearest thing to evidence in this library |

The plainest statement the sources allow: **no engineering study gives any time for dismantling Mercury or any planet.** The
only rates with hardware behind them are the 1970s lunar launcher and catcher (under 1 Mt/yr each) and the 1985 launch loop
(3.5 Mt/yr); at those rates the whole of Mercury is 10^14 machine-years of work (F1c).

### F6. Alternatives to total disassembly (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Partial harvesting is enough for a full swarm, on the literature's own areal masses | A&S swarm needs 50% of Mercury at 3.92 kg/m^2; at Angel's 4.2 g/m^2 the same sphere would need 1.8 x 10^20 kg, 0.05% of Mercury (DERIVED: 4.214 x 10^22 m^2 x 0.0042 kg/m^2) | A&S; Angel 2006 | Derived | Wright: 0.8 g/m^2 is where light pressure balances gravity | Medium |
| Crust only | Crust 8.0 x 10^21 kg (median; range 2 x 10^18 to 1.6 x 10^22), mantle plus crust 8.6 x 10^22 kg, crust thickness 35 to 53 km (modeled) | Margot et al. 2018 Tables 4 and 5 | Primary | Removing the crust in 1,000 yr: 2.5 x 10^11 kg/s, 2.4 x 10^18 W of launch power (14 times Mercury's intercepted sunlight), 6 x 10^9 lunar-design launchers (calc [2]) | Medium |
| "A bit of Mercury" | Jones 1985 (qualitative, one percent of the Sun's output) | Jones 1985 | Primary (qualitative) | n/a | Low |
| Asteroids instead | Bradbury: asteroids 5.9 x 10^21 kg against Mercury 3.3 x 10^23; lower flux there (200 to 500 W/m^2) means "at least an order of magnitude less material is required for collectors in an orbit near Mercury" | Bradbury | Secondary | Sandberg FAQ asteroids ~0.002 x 10^24 kg (a different figure, Conflicts) | Low to medium |
| Atmosphere only (Venus) | Bradbury: carbon is 27% of Venus's 5 x 10^20 kg atmosphere; "rotating sky hooks with large scoops or upper atmosphere ram-jet mining ships could easily provide ~1.4 x 10^20 kg of carbon"; remove the atmosphere before the planet | Bradbury | Secondary (no design) | Venus carbon 1.3 x 10^20 kg ([IMS] section 2) | Low; Venus is section 3's topic |
| Small swarms | "Minimal occulter" swarms of 11 to 4,800 elements (Lacki Table 1) and partial Dyson spheres (Hephaistos) are the forms the detection literature actually searches for | Lacki 2025; Suazo et al. 2024 | Primary | n/a | Medium |
| Natural mantle stripping | Mercury itself may be the remnant of a giant impact that stripped most of a proto-Mercury's mantle (F2) | Franco et al. 2025 | Primary (preprint) | n/a | Medium |

## Conflicts

1. **A&S composition: "70% metal, mainly iron or iron oxides."** The 70% matches the modeled core mass fraction (69 to 77%,
   Nittler et al. 2017 citing Hauck et al. 2013; 74% median, Margot et al. 2018). "Iron oxides" does not: the metal is an Fe-Si(-S)
   alloy in the core, and the silicate shell that must be removed first holds 1 to 2 wt% Fe. The paper's own caveat ("more wasted
   material initially") acknowledges part of this.
2. **A&S bond energy, "less than one mega-joule per mol ... comparable" to 9 MJ/kg.** Units differ (per mol against per kg).
   NIST gives Al2O3 at -1,675.7 kJ/mol, above their bound; per kg, oxide formation enthalpies (15 to 16 MJ/kg) are 1.7 to 1.8 times
   the lift energy. Bradbury, whom A&S follow, uses "a generous 20,000 kJ/mol" (lattice enthalpies, a different and larger quantity).
   Three definitions are in play: formation enthalpy (to reduce an oxide), lattice enthalpy (to separate into gaseous ions) and
   A&S's undefined "chemical bonds".
3. **A&S robustness: "time scales linearly with the available energy."** In the feedback model it scales roughly with the
   logarithm (10x less efficiency: 35.6 to 59.3 yr). The sentence may refer to the probe-launch phase; for disassembly it is not what
   their own model does.
4. **A&S 31.2 yr against my 35.6 yr.** The paper prints no equations; nearby readings of its assumptions give 29.8 to 34.6 yr.
   Not an error found, an irreproducibility.
5. **Bradbury's 3.4 x 10^17 W from Mercury's surface** is exactly twice the sunlight Mercury intercepts (pi R^2 x 9,082.7 W/m^2 =
   1.70 x 10^17 W): it counts a hemisphere at full normal flux. His 9,214 W/m^2 is 1.4% above NSSDC's 9,082.7 (likely a different
   solar constant).
6. **Jones 1985 Clarke Station, 150,000 TW**: 1,000 km collector at 20 solar radii gives 123,600 TW from NSSDC luminosity and radius
   (21% lower); likely rounded inputs.
7. **Sandberg FAQ Earth mass 5.8742 x 10^24 kg** against Bradbury's 5.9 x 10^24; the FAQ's asteroid mass (about 0.002 x 10^24 kg)
   against Bradbury's 5.9 x 10^21 kg differ by a factor of 3; neither was checked against a primary ephemeris here.
8. **Forward and Nordley 1999** print the Spectra characteristic velocity as "2.9 m/s"; sqrt(2 x 4.0 GPa / 970) = 2.87 km/s. A unit typo.
9. **Smith 2021**: (a) the stated 871 MW mass-driver power is not reproduced (316 MW mean over the shot, 359 MW at the stated
   launch interval); (b) a "55 km orbital radius" around Mars is used where the 3.52 km/s figure implies a near-surface orbit
   (an altitude, not a radius); (c) 18.35 TW in the abstract and 18.5 TW in the text.
10. **Published versus preprint A&S.** A forum lead (rejected as a source) says the published version shortened the launch-phase
    section. Only the preprint was read; any A&S figure here may differ from the journal text.

## Derived figures

All inputs are sourced in the scripts' headers; full output in the scratch subfolder.

- **D1. Mercury's lift energy** (calc [1]): v_esc = sqrt(2GM/R) = sqrt(2 x 2.2032 x 10^13 / 2.4397 x 10^6) = 4,250 m/s; v^2/2 =
  9.031 MJ/kg. Uniform-sphere binding energy 3GM^2/(5R) = 1.789 x 10^30 J; 9 MJ/kg x M = 2.97 x 10^30 J (1.66 times larger).
- **D2. Reproduction of A&S** (F1c): P0 = (1/3)(9,082.7)(10^6) = 3.03 GW; initial flow 0.1 x 3.03 x 10^9 / 9 x 10^6 = 33.6 kg/s
  (1.06 x 10^9 kg/yr). Base result 35.6 yr.
- **D3. Delivered power against natural limits** (repro): Mercury intercepts pi(2.4397 x 10^6)^2 x 9,082.7 = 1.70 x 10^17 W. A&S
  power passes this at 20.1 yr and reaches 9.7 x 10^23 W; spread over 4 pi R^2 = 7.48 x 10^13 m^2 that is 1.30 x 10^10 W/m^2;
  photosphere 3.828 x 10^26 / (4 pi (6.957 x 10^8)^2) = 6.29 x 10^7 W/m^2; ratio 207. Launcher loss 0.036 x 0.1 x 9.74 x 10^23 /
  7.48 x 10^13 = 4.7 x 10^7 W/m^2, T = (q/sigma)^(1/4) = 5,362 K.
- **D4. Hardware at the end of the A&S schedule**: 1.08 x 10^16 kg/s / 42 kg/s = 2.6 x 10^14 lunar-design launchers (8.1 x 10^20 kg,
  0.24% of Mercury), 3.4 per m^2 of surface; uniform surface recession 1.08 x 10^16 / (7.48 x 10^13 x 2,700 to 3,100) = 0.047 to
  0.054 m/s.
- **D5. Uniform-rate table** (calc [2]), whole planet / mantle plus crust / crust:

| Mass removed | Years | Flow (kg/s) | Launch power (W) | x Mercury's sunlight | Lunar-design launchers | SP-413 catchers |
|---|---|---|---|---|---|---|
| Whole planet 3.30 x 10^23 kg | 31 | 3.4 x 10^14 | 3.2 x 10^21 | 18,600 | 8.0 x 10^12 | 3.3 x 10^13 |
| | 100 | 1.0 x 10^14 | 9.8 x 10^20 | 5,800 | 2.5 x 10^12 | 1.0 x 10^13 |
| | 1,000 | 1.0 x 10^13 | 9.8 x 10^19 | 580 | 2.5 x 10^11 | 1.0 x 10^12 |
| Mantle plus crust 8.6 x 10^22 kg | 1,000 | 2.7 x 10^12 | 2.6 x 10^19 | 150 | 6.5 x 10^10 | 2.7 x 10^11 |
| Crust 8.0 x 10^21 kg | 1,000 | 2.5 x 10^11 | 2.4 x 10^18 | 14 | 6.0 x 10^9 | 2.5 x 10^10 |
| A&S swarm mass (50%) | 1,000 | 5.2 x 10^12 | 4.9 x 10^19 | 290 | 1.2 x 10^11 | 5.2 x 10^11 |

  Launch power only; it excludes processing (A&S allot nine times as much) and every conversion loss upstream of the launcher.
  Section 4's file owns the collector and radiator side.
- **D6. Elevator geometry** (calc [5]): r_sync = (GM T^2 / 4 pi^2)^(1/3) with T = 1,407.6 h gives 2.429 x 10^8 m; Hill radius
  a (M / 3 M_sun)^(1/3) = 5.7909 x 10^10 x (3.301 x 10^23 / 5.965 x 10^30)^(1/3) = 2.207 x 10^8 m.
- **D7. Ablation** (calc [8]): plume characteristic speeds 1.54 to 2.87 km/s are 0.36 to 0.68 of 4.25 km/s.
- **D8. Swarm collisions at Mercury** (calc [7]): 0.16 x 87.97 d = 14 d.
- **D9. Partial swarm mass** (F6): 4.214 x 10^22 m^2 x 4.2 g/m^2 = 1.8 x 10^20 kg = 0.054% of Mercury.

## Constraints for any inhabitant

- A swarm built from a planet is a debris field waiting to happen: unmaintained, a full swarm at Mercury's distance would start
  colliding within weeks (D8, Lacki); upkeep (station-keeping, collision avoidance) never ends.
- Any large-scale removal works through a small number of physical bottlenecks that no source sizes: launchers, catchers and
  orbital factories in counts of 10^9 to 10^13 for planetary-scale work (D5), not the handful of machines the studies design.
- A world being dismantled at the A&S pace would be uninhabitable at its surface long before most of its mass moved: delivered
  power would exceed its natural sunlight after a few millionths of its mass had gone, and its surface would be driven past rock's
  vaporization temperatures if even 4% of the launch power were lost there (D3).
- There is no elevator off Mercury (D6); everything leaves by launcher, rocket or partial-speed tether.
- Waste heat, not energy supply, governs work near a planet being harvested (D3; section 4's file has the radiator numbers).
- Removal of the first quarter of Mercury's mass yields silicate, not metal; anything built from the early output is glass,
  ceramic, aluminum, magnesium or silicon, not iron (F1b, Margot, Nittler).

## Candidate handwaves

Flagged for the developer; none accepted.

- **D-1. Mercury dismantled in about three decades** (A&S). Requires unlimited self-replicating hardware, a 5-year processing
  cycle no study supports, and power delivery to the surface hundreds of times the photosphere's flux (F5, D3).
- **D-2. Any whole-planet disassembly on a timescale of centuries or less.** Even at 1,000 years the whole planet needs 2.5 x 10^11
  lunar-class launchers and 10^12 catchers running continuously (D5).
- **D-3. A rigid Dyson shell** (any size): about nine orders of magnitude beyond the strongest known material (Wright).
- **D-4. A space elevator on Mercury** (geometrically impossible, D6).
- **D-5. Lifting Mercury's surface off by laser or sunlight alone** (plume speeds below escape speed, D7).
- **D-6. A long-lived unmaintained swarm** (collision time of days to weeks at Mercury's orbit, D8).

## Open threads

- **Dyson 1966** ("The search for extraterrestrial technology"): text not found online; it would give Dyson's own disassembly
  mechanism and numbers. Next: a library copy of *Perspectives in Modern Physics* (1966), or Dyson's *Selected Papers* (1996).
- **Criswell 1985** chapter (pp. 50-87): lending-restricted on the Internet Archive; next: a library loan. Wright cites it as the
  reference for deconstructing planets.
- **Published A&S** (*Acta Astronautica* 89, 2013): closed access; check whether sec. 4.2 and its numbers survived publication.
- **Benz et al. 2007** ("The Origin of Mercury", *Space Sci. Rev.* 132): blocked by the publisher's cookie redirect; Asphaug and
  Reufer 2014 (*Nature Geoscience*) not opened.
- Kolm et al. 1980 MIT report on electromagnetic guns (A&S ref. 37) and the coilgun-efficiency claims behind A&S sec. 4.3: not opened.
- No peer-reviewed critique of A&S's disassembly section was found; only forum discussion (rejected). Searching citing papers of
  A&S (96 citations per OpenAlex) for "Mercury" would be the next step.
- Slingatron throughput and status (Tidman's NSS papers surfaced, not read). No source at all was found for electromagnetic
  acceleration of loose, uncontained material (as opposed to payload packages); every launcher design read throws discrete payloads.
- A second, independent source for Lacki's collision-time ratio at Mercury's distance (only his 1 AU and 0.32 AU rows were used).
- Catching and orbital processing at planetary rates: no source found that sizes the orbital factories or a placement rate.
- Hephaistos contamination and radio follow-up papers (arXiv:2405.14921, 2501.05152) surfaced by title only.
- The thermodynamic concentration limit in suns (Gleckman et al. 1989 PDF) not read; the étendue point here rests on the
  photosphere-flux arithmetic and the paper's abstract.
- The Galaxies 2022 Kardashev-timeline paper and Hanson's "Burning the cosmic commons" surfaced and were not read (forecasts and
  economics, not engineering).

## Rejected sources

- **LessWrong, EA Forum and GreaterWrong threads** on A&S (row 52): forum comments, not sources. One claims the delivered power
  density exceeds the photosphere's by "6 orders of magnitude"; my arithmetic gives 207 times at the end of the schedule (D3), so
  the claim is not used.
- **PopSci 2012**, "Why Turning Mercury Into a Dyson Sphere ... Is Not Worth It" (row 52): popular press; not opened, not used.
- **sciencereader.com**, "Dismantle Mercury, Build a Dyson Swarm in 31 Years" (row 38): a popular restatement of A&S, including a
  "425,000 years" figure not traced to any primary; not used.
- **Wikipedia** pages (Launch loop, Star lifting, Astronomical engineering, Synchronous orbit) and **fandom wikis**: leads only;
  the synchronous-orbit figure is shown as a secondary cross-check of a derived number.
- **space.com, Centauri Dreams, Grokipedia, NamuWiki, Kerbal forum** results: leads only, not used.
- **Ellery IAC-17 abstract**: no numbers in the accessible text.
