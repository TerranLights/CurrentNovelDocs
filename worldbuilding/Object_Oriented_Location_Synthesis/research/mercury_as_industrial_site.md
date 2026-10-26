# Mercury as an industrial site: surface composition, environment, power, launch and published concepts

*Research file, OOLSD library, seventh tranche. Started 2026-10-11. Physics and engineering only; no setting assumed.*

## 1. Scope

Mercury (the planet, its surface and near-surface, its polar cold traps and its immediate orbital environment) as a site for
mining, processing and launching material. Bulk orbital transfer from Mercury to other bodies is covered by the sibling
trucking file and the tranche-7 logistics file; this file stops at the surface, low orbit and launch.

## 2. SEARCH LOG

| # | Date | Search string (verbatim) or page opened | Result | Used? |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read (allowed, read-only) sibling files: grep for Mercury in `space_processing_and_fabrication.md`, `space_trucking_and_transport_infrastructure.md`, `starlifting_physics_and_minimum_infrastructure.md`, `moon_lagrange_and_comparables.md`; read the Mercury rows | useful | Siblings already hold: NSSDC bulk constants, core radius (Hauck 2013 / Rivoldini 2013 via Wicht and Heyner), Armstrong and Sandberg disassembly, escape 9.03 MJ/kg, Palaszewski Mercury ascent, lunar SP-428 mass driver, lunar MRE/carbothermal energies. Cited, not re-derived. `moon_lagrange_and_comparables.md` has no Mercury rows |
| 2 | 2026-10-11 | `Nittler Weider "The Surface Composition of Mercury" Elements 2019 weight percent Fe Mg Si S` | thin | Leads only; no numbers in results |
| 3 | 2026-10-11 | Page: Carnegie Science, "The Surface Composition of Mercury" (Nittler and Weider 2019 listing) | thin (not used for numbers) | Qualitative only ("enriched in S and C, depleted in Fe"); died at the source for numbers |
| 4 | 2026-10-11 | Page (curl): Smithsonian repository bitstream for Nittler et al. 2011 | dead at the source | Returned a JavaScript HTML shell, not the PDF |
| 5 | 2026-10-11 | `Evans 2012 "Major-element abundances on the surface of Mercury" Gamma-Ray Spectrometer Fe wt% Si Ca S results` | useful | Led to the Arizona abstract page |
| 6 | 2026-10-11 | Page: experts.arizona.edu abstract, Evans et al. 2012, JGR Planets 117, doi 10.1029/2012JE004178 | useful | Na 2.9 wt%; S/Si, Ca/Si, Fe/Si; regolith homogeneous to tens of cm |
| 7 | 2026-10-11 | `arXiv Nittler Chabot Grove Peplowski "The chemical composition of Mercury" 2017` | useful | Located the review chapter preprint |
| 8 | 2026-10-11 | Page (curl + pdftotext): arXiv 1712.02187, Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", chapter 2 of *Mercury: The View after MESSENGER* (Cambridge, 2018); read sections 2.1-2.5 and Tables 2.1-2.3 | useful (core source) | Table 2.1 surface composition; core composition Table 2.3; C, O/Si, Th, U |
| 9 | 2026-10-11 | `Weider 2014 "Variations in the abundance of iron on Mercury's surface" X-Ray Spectrometer Fe wt% metal sulfide` | useful | |
| 10 | 2026-10-11 | Page: cosmochemistry-papers.com abstract repost of Weider et al. 2014, Icarus 235:170-186, doi 10.1016/j.icarus.2014.03.002 | useful (abstract, verbatim from journal) | Fe/Si ~0.06 = ~1.5 wt% Fe; Fe in sulfides and Fe metal |
| 11 | 2026-10-11 | `Weider 2015 "Evidence for geochemical terranes on Mercury" Mg/Si high-magnesium region values Earth and Planetary Science Letters abstract` | useful | |
| 12 | 2026-10-11 | Page: profiles.wustl.edu abstract of Weider et al. 2015, EPSL | useful | Mg/Si 0.1-0.8, Al/Si 0.1-0.4; high-Mg region >5 x 10^6 km^2 |
| 13 | 2026-10-11 | `Peplowski 2016 Nature Geoscience "Remote sensing evidence for an ancient carbon-bearing crust on Mercury" abstract wt% carbon low-reflectance material` | thin | Abstract not reproduced online; numbers taken from [NIT18] instead |
| 14 | 2026-10-11 | Page: Carnegie Science news, "Mercury's Mysterious 'Darkness' Revealed" (7 Mar 2016) | useful (secondary cross-check) | "as much as a few weight percent graphitic carbon" |
| 15 | 2026-10-11 | `Nittler 2011 Science "The major-element composition of Mercury's surface from MESSENGER X-ray spectrometry" abstract sulfur 4 wt% iron` | useful (leads) | |
| 16 | 2026-10-11 | Page: experts.azregents.edu abstract of Nittler et al. 2011 | dead at the source | HTTP 404 |
| 17 | 2026-10-11 | Page: GSA 2011 Annual Meeting abstract Paper193666 (Nittler et al., XRS results) | useful | S "up to ~4 wt%", Fe "less than ~4 wt%", Ti "less than ~0.8 wt%" |
| 18 | 2026-10-11 | Page (curl + pdftotext): NTRS 20160002643, Vander Kaaden et al., "Mineralogy of the Mercurian Surface", LPSC 47 (2016) abstract 1476 | useful | Normative mineralogy Table 1 for nine terranes |
| 19 | 2026-10-11 | `Mercury surface metallic iron nanophase space weathering abundance MESSENGER reflectance "metallic iron" wt% Trang Lucey` | thin | Leads to PDS product and AGU abstract |
| 20 | 2026-10-11 | Page (curl): PDS Geosciences, Trang 2017 "Mercury space weathering map" document | thin (not used for numbers) | Describes wt% maps of nanophase/microphase iron and carbon; no averages in the text. Died at the source |
| 21 | 2026-10-11 | Page: AGU Fall Meeting 2015 abstract, Trang, Lucey, Izenberg (after redirect to studio.m-anage.com) | useful | Submicroscopic carbon 1.4 +/- 0.3 wt%; no iron figure |
| 22 | 2026-10-11 | `Mercury surface fraction of iron as Fe metal versus FeS versus FeO MESSENGER "reduced" iron metal surface regolith estimate` (extended mode) | useful | Led to Nittler et al. 2020 maps paper |
| 23 | 2026-10-11 | Page (curl + pdftotext): arXiv 2003.00650, Nittler, Frank, Weider et al., "Global Major-Element Maps of Mercury from Four Years of MESSENGER X-Ray Spectrometer Observations", Icarus (2020), doi 10.1016/j.icarus.2020.113716 | useful | Fe form statement and the factor-of-five systematic on Fe/Si |
| 24 | 2026-10-11 | Page: NASA NSSDCA Mercury Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html (last updated 11 Jan 2024) | useful | Bulk, orbit, rotation, irradiance, surface temperature, field |
| 25 | 2026-10-11 | `Genova 2019 "Geodetic evidence that Mercury has a solid inner core" inner core radius outer core radius km moment of inertia` | useful | |
| 26 | 2026-10-11 | Page (curl): MIT DSpace nihms-1529127.pdf | dead at the source | HTML shell, not a PDF |
| 27 | 2026-10-11 | Page (curl + pdftotext): Sapienza IRIS, Genova et al. 2019 preprint (GRL 46:3625-3633), NASA author manuscript | useful | C/MR^2 0.333; outer core radius 1,985 / 1,967 km; inner core ratio |
| 28 | 2026-10-11 | Page (curl + pdftotext): arXiv 2011.15066, Beuthe, Charlier, Namur, Rivoldini, Van Hoolst, "Mercury's crustal thickness correlates with lateral variations in mantle melt production", GRL 47 (2020) | useful | Crust 19 to 50 km regionally; mantle 400 km |
| 29 | 2026-10-11 | `Mercury impact basin excavation depth mantle exposed Caloris Rembrandt excavated material from depth km MESSENGER study` | thin | No study of excavating to the mantle or core; volcanic fill thickness only from a search summary. Died at the sources for the core question |
| 30 | 2026-10-11 | `Kola Superdeep Borehole SG-3 depth 12,262 m reached 1989 temperature 180 C` | thin (secondary) | Wikipedia-class results only; used once, labeled secondary, for scale |
| 31 | 2026-10-11 | `Mercury regolith thickness depth estimate meters MESSENGER small crater morphology regolith depth Kreslavsky Head` | useful | |
| 32 | 2026-10-11 | Page: Université de Lorraine CRPG listing, Joulaud, Allemand, Flahaut, Füri, "Regolith thickness across the Borealis Planitia region of Mercury", Planetary and Space Science 282 (Nov 2026, article 106338) | useful | Median regolith 4.6 m (smooth plains), 3.7 m (intercrater plains); 3,546 craters |
| 33 | 2026-10-11 | Page: AGU FM15 abstract, Zharkova, Kreslavsky et al., "Morphometry of Small Flat Floored Craters on Mercury: Implications for Regolith Thickness" (after redirect) | dead at the source | Title and authors only; no abstract text. The search summary's "25-40 m" early estimate not used |
| 34 | 2026-10-11 | `Vasavada Paige Wood 1999 "Near-surface temperatures on Mercury and the Moon" regolith thermal conductivity density thermal inertia polar ice stability` | useful (leads) | |
| 35 | 2026-10-11 | Pages: LPL Arizona copy of Vasavada et al. 1999 (curl and WebFetch); Caltech thesis PDF (curl) | dead at the source | 404 / redirect to LPL home page; thesis download timed out |
| 36 | 2026-10-11 | `Paige 2013 Science "Thermal stability of volatiles in the north polar region of Mercury" maximum temperature permanently shadowed 50 K biannual average` | thin | Leads; PMC link hit a reCAPTCHA (dead at the source) |
| 37 | 2026-10-11 | `Chabot Lawrence Neumann Feldman Paige "Mercury's Polar Deposits" chapter Mercury The View after MESSENGER pdf` | thin | APL library PDFs of the chapter and of Chabot et al. 2016 GRL both returned 404 (dead at the source) |
| 38 | 2026-10-11 | Page: BAAS 2021 white paper on Mercury polar volatiles (curl and WebFetch) | dead at the source | 403 Forbidden |
| 39 | 2026-10-11 | `Mercury polar water ice total mass estimate kg Lawrence 2013 neutron spectrometer 2.1 x 10^16 g Deutsch 2016 ice volume` | useful | Led to Eke et al. and Frantseva et al. arXiv papers |
| 40 | 2026-10-11 | Page (curl + pdftotext): arXiv 1611.05395, Eke, Lawrence, Teodoro, "How thick are Mercury's polar water ice deposits?", MNRAS (2017) | useful | Excess height (50 +/- 35) m; upper limit ~3 x 10^15 kg; 10,000 km^2 radar-bright area |
| 41 | 2026-10-11 | Page (curl + pdftotext): arXiv 2204.11825, Frantseva, Nesvorný, Mueller, van der Tak, ten Kate, Pokorný, "Exogenous delivery of water to Mercury", Icarus (2022) | useful | Lawrence 2013 inventory 2.1 x 10^13 to 1.4 x 10^15 kg; PSR areas; dust flux estimates and their disagreement |
| 42 | 2026-10-11 | Page (curl): Paige KISS workshop presentation PDF | dead at the source | Download failed |
| 43 | 2026-10-11 | `Mercury surface temperature equator "hot pole" "warm pole" 700 K night 100 K subsurface temperature depth model diurnal skin depth` (extended mode) | thin | Summary gave numbers (700 K, 570 K, 93 K, 420 K at 1 m, density 1.5 g/cm^3) without an openable primary; **not used** except where re-found below |
| 44 | 2026-10-11 | Pages: ScienceDirect abstract of the MERTIS surface-temperature paper (S0019103520304310); ResearchGate "Thermal model of Mercury's surface and subsurface" | dead at the source | 403 Forbidden on both |
| 45 | 2026-10-11 | `arxiv Mercury surface temperature model regolith thermal conductivity density profile subsurface 1 m 420 K hot longitude BepiColombo MERTIS` | thin | |
| 46 | 2026-10-11 | Page (curl): EPSC2017-610, Maturilli et al., emissivity of Mercury analogues | thin (not used) | Lab spectra; only "Mercury regolith is mostly composed of very fine particles" (they chose <25 µm) |
| 47 | 2026-10-11 | Page: Münster CRIS "Insolation and Resulting Surface Temperatures of Study Regions on Mercury" | dead at the source | Redirected to portal home |
| 48 | 2026-10-11 | Page: UCLA Diviner group poster "Mercury's Surface Temperature" (WebFetch and curl) | dead at the source | TLS certificate error; no content |
| 49 | 2026-10-11 | `lpi.usra.edu Paige Mercury north polar region temperatures thermal model MLA permanently shadowed maximum temperature K water ice stable LPSC abstract` | useful | Led to EPSC2012-595 |
| 50 | 2026-10-11 | Page (curl + pdftotext): EPSC2012-595, Paige, Siegler, Harmon, Smith, Zuber, Neumann, Solomon, "Thermal Stability of Frozen Volatiles in the North Polar Region of Mercury" | useful | Annual wave ~0.4 m; radar-bright Tav peak 100 K, Tmax ~170 K; ~10 cm dark layer |
| 51 | 2026-10-11 | `Mitchell de Pater 1994 Icarus "Microwave imaging of Mercury's thermal emission" density 1.5 g cm-3 equatorial midnight temperature 100 K loss tangent` | thin | Citation confirmed (Icarus 110:2-32); numbers not openable. Springer chapter link hit a login redirect (dead at the source) |
| 52 | 2026-10-11 | Page (curl + pdftotext): arXiv astro-ph/0409220, Butler, Campbell, de Pater, Gary, "Solar System Science with SKA" (2004) | thin | Only "skin depths ... a few 10's of cm (Moon, Mercury ...)"; not used |
| 53 | 2026-10-11 | Page: NASA Science, "Mercury Facts" (page date 25 Apr 2025) | useful (agency, popular level) | 430 C day, -180 C night, 176-day solar day, field 1% of Earth's |
| 54 | 2026-10-11 | `Mercury polar illumination conditions "persistently illuminated" OR "peaks of eternal light" MLA topography percent of time illuminated north pole lander site` (extended mode) | useful | |
| 55 | 2026-10-11 | Page: NASA image article "There Is a Light that Never Goes Out (Almost)" (MESSENGER, 24 Dec 2011 data) | useful | 82% at 89 S, 50.7 E; no peak of eternal light at the south pole |
| 56 | 2026-10-11 | `Mercury north pole illumination map MESSENGER MDIS maximum illuminated fraction solar day percent "north polar" Chabot 2012 permanent shadow area` | thin | North-pole maximum-illumination figure not found (died at the sources) |
| 57 | 2026-10-11 | Page: NTRS 20160008397, Deutsch, Chabot, Mazarico et al., "Comparison of Areas in Shadow from Imaging and Altimetry in the North Polar Region of Mercury ..." (25 Jun 2016) | useful | ~46% / ~43% of shadowed area hosts radar-bright material |
| 58 | 2026-10-11 | `Cintala 1992 "Impact-induced thermal effects in the lunar and Mercurian regoliths" micrometeoroid flux Mercury times Moon mean impact velocity melt vapor` | useful | |
| 59 | 2026-10-11 | Page: NTRS 19940009826, Cintala, "Impact Melting and Vaporization in Planetary Regoliths" (1993) | thin (not used) | Qualitative overview only |
| 60 | 2026-10-11 | Page: EarthRef ERR 60235, abstract of Cintala 1992, JGR | useful | Impact rate 5.5 times the Moon's; mean velocity >60% higher |
| 61 | 2026-10-11 | `Mercury surface charging dayside potential photoelectron nightside dust levitation electrostatic study regolith grains` | useful | |
| 62 | 2026-10-11 | Page (curl + pdftotext): arXiv 2305.09498, Lavorenti, Jensen, Aizawa et al., "Maps of solar wind plasma precipitation onto Mercury's surface: a geographical perspective" (2023) | useful | Field shields ~90% of solar wind flux; surface charging "an open question"; protons <0.5 to >1.5 keV, electrons 0.1-4 keV at surface |
| 63 | 2026-10-11 | Page (curl + pdftotext): arXiv 2410.05913, Miyake et al., "Micro-scale electrostatic structures formed on the rough surfaces of the Moon" (2024) | useful (lunar anchor) | Lunar dayside "several to 10 V positive" |
| 64 | 2026-10-11 | `Mercury Lander mission concept study 2020 Ernst APL Planetary Science Journal landing site night operations power radioisotope thermal design surface duration` | useful | |
| 65 | 2026-10-11 | Page (curl + pdftotext): NASA Planetary Mission Concept Study, "Mercury Lander" final report (APL, Ernst et al., 2020; v2 tagged PDF on science.nasa.gov) | useful (core source for items 6, 8, 12) | Dusk landing, RTG night ops, 3.3 km/s SRM braking, DTE gaps, array temperature limits, lunar-terrain assumption |
| 66 | 2026-10-11 | `Mercury "hot poles" longitude 0 180 perihelion noon temperature "warm poles" 90 270 aphelion temperature MESSENGER jhuapl` (domains limited to agencies, arXiv, LPI, Copernicus) | useful | |
| 67 | 2026-10-11 | Page (curl + pdftotext): Ercol, Dakermanji, Le, "The MESSENGER Spacecraft Power Subsystem Thermal Design and Early Mission Performance", AIAA 2006-4144 | useful | 28% cells, 1:2 cell-to-OSR, 150 C panel limit, 275 C anomaly case, -140 to 275 C qualification |
| 68 | 2026-10-11 | Page (curl + pdftotext): Holtzman, Begley, Ercol, "Return to Mercury: An Overview of the MESSENGER Spacecraft Thermal Environmental Predictions and Analysis Process", ICES-2015-307 | useful | 4.7-11.1 ESC; 451 C subsolar; -163 C night; emissivity 0.93; orbit dates |
| 69 | 2026-10-11 | Re-read: arXiv 2305.09498 §1 (row 62) for the hot-pole/warm-pole statement | useful | 700 K / 570 K attributed to Bauch et al. 2021 |
| 70 | 2026-10-11 | `BepiColombo MPO solar array design high temperature GaAs cells operating temperature 230 C Mercury degradation solar array qualification paper` | thin | Search summary had rich numbers (190 C nominal, 205 C for 600 h, 1,800 W, 20% loss at 500 K / 11 suns, 5,500 cycles) but the E3S/DOAJ pages that carry them returned 403; **those figures are not used** except where re-found at ESA (rows 72-73) |
| 71 | 2026-10-11 | Pages: E3S Web of Conferences ESPC 2017 papers 02007, 04006, 04007 (HTML and PDF), DOAJ records, JAXA repository PDF | dead at the source | 403 / HTML shells |
| 72 | 2026-10-11 | Page: ESA, "Going solar for interplanetary missions" (27 May 2009) | useful | ~350 C array temperature, "120 degrees higher than the maximum tolerable solar cell operating temperature"; mirrors next to each cell row; high Sun angle |
| 73 | 2026-10-11 | Page: ESA, "Hot stuff: the making of BepiColombo, 6. A life in the Sun" (1 Jun 2011) (m.esa.int failed DNS; www.esa.int worked) | useful | "just one simulated month saw a 20% power loss"; UV plus heat; mission near cancellation |
| 74 | 2026-10-11 | Page: ESA sci.esa.int BepiColombo "Spacecraft" page (last update 30 Mar 2020) | thin | Only "up to 1000 W" during science phases |
| 75 | 2026-10-11 | `Landis NASA Glenn high temperature solar cells performance temperature coefficient 400 C 450 C Mercury surface GaInP wide bandgap NTRS` | useful | |
| 76 | 2026-10-11 | Page (curl, read as PDF images): NTRS 20050198948, Landis, Raffaelle, Merritt, "High Temperature Solar Cell Development", 19th European PV Solar Energy Conf., Paris, June 2004 | useful | Mercury surface station equilibrium ~450 C; MESSENGER >2/3 mirrors at 10.6 AM0; optimum bandgap ~1.5 eV (300 K) to ~2 eV (1,000 K); SiC cells, contacts to 900 C |
| 77 | 2026-10-11 | Page (curl): NTRS 20050214479 (same paper, other copy) and NTRS 20150016298 (Landis and Haag, Venus solar cells) | thin (not used) | Duplicate; Venus paper belongs to the Venus file |
| 78 | 2026-10-11 | `radial dependence solar energetic particle peak intensity fluence MESSENGER Helios 0.3 AU scaling R^-2 R^-3 Lario 2006 2013 Mercury` | useful | |
| 79 | 2026-10-11 | Page: EGU24-6213 abstract, Rodríguez-García, "Acceleration and transport of solar energetic particles in the inner heliosphere" | useful | Electron peak intensities ~R^-3, 0.3-1 au |
| 80 | 2026-10-11 | `Lario 2006 ApJ "Radial and longitudinal dependence of solar 4-13 MeV and 27-37 MeV proton peak intensities and fluences" Helios IMP-8 abstract exponent` | useful | |
| 81 | 2026-10-11 | Page (curl + pdftotext): COSPAR 2006 abstract A-02607, Lario, Decker, Krimigis, Roelof, Aran | useful | Exponents and the Shea 1988 guideline comparison |
| 82 | 2026-10-11 | Page (curl): ACE News #148 (28 Feb 2012), Lario and Roelof | thin (not used for numbers) | Longitudinal Gaussian widths only |
| 83 | 2026-10-11 | `Mercury magnetosphere cutoff rigidity solar energetic particles access to surface galactic cosmic rays shielding MESSENGER study dose` (extended mode) | useful | |
| 84 | 2026-10-11 | Page (curl + pdftotext): arXiv 2202.13243, Milillo, Fujimoto, Murakami et al., "Investigating Mercury's Environment with the Two-Spacecraft BepiColombo Mission", Space Sci. Rev. 216:93 (2020) | useful | Størmer cutoffs; no radiation belts; GCR only modeled |
| 85 | 2026-10-11 | `BepiColombo radiation monitor BERM dose rate measurements cruise inner heliosphere GCR solar particle events paper` | thin | Instrument paper located (Pinto et al. 2022, Space Sci. Rev.), but no dose number in the pages listed; not opened. Died at the query for a dose figure |
| 86 | 2026-10-11 | Page: NASA NSSDCA Sun Fact Sheet (last updated 9 May 2024) | useful | Radius 695,700 km; Teff 5,772 K; luminosity 382.8 x 10^24 W |
| 87 | 2026-10-11 | Local Python: irradiance at perihelion/aphelion, concentration ratios, storage, PV bounds, SEP scaling (D3-D7) | useful | Section 5 |
| 88 | 2026-10-11 | `"Mercury" mass driver electromagnetic launcher surface launch study paper escape velocity solar power satellite construction Dyson swarm material from Mercury` (extended mode) | dead at the sources | Blogs, Wikipedia, a social-media post and a patent; one article gave Mercury's escape speed as 4.5 km/s (NSSDC: 4.3) |
| 89 | 2026-10-11 | `Mercury in-situ resource utilization ISRU paper polar ice propellant Mercury surface resources mining study NTRS OR AIAA OR "Acta Astronautica"` (extended mode) | useful | Led to Palaszewski 2017 |
| 90 | 2026-10-11 | Page + PDF (curl + pdftotext): NTRS 20170001561, Palaszewski, "Solar System Exploration Augmented by In-Situ Resource Utilization: Human Planetary Base Issues for Mercury and Saturn" (13 Jan 2017) | useful | Lander masses, ISRU hydrogen, base siting, >10^18 g water |
| 91 | 2026-10-11 | `MESSENGER orbit solar gravity perturbation periapsis altitude drift km per orbit correction maneuvers Mercury low orbit stability frozen orbit BepiColombo MPO 480 km 1500 km` | useful | |
| 92 | 2026-10-11 | Page (curl + pdftotext): Moessner and McAdams, "The Final Two Years: MESSENGER's Trajectory from the Third Year in Orbit through Mercury Impact", ISSFD 24 (2014) | useful | Periapsis decay, OCM delta-v, conjunction timing |
| 93 | 2026-10-11 | Page: NASA NSSDCA Earth Fact Sheet (last updated 15 Nov 2024) | useful | Earth perihelion/aphelion, 1,361.0 W/m^2 |
| 94 | 2026-10-11 | `rotating tether maximum tip velocity material characteristic velocity sqrt(2 sigma/rho) Spectra Zylon km/s taper ratio Hoyt Forward NTRS` | thin | Patents and forums; summary's Spectra 1.83 km/s and Zylon 3 km/s figures not opened (not used) |
| 95 | 2026-10-11 | Page (curl + pdftotext): arXiv 1805.06438, Howe, "A Tether-Assisted Space Launch System for Super-Earths" (2018, physics.pop-ph) | thin (preprint, low weight) | v_c formula; CNT 5.4 km/s; aramid ~3.0 km/s |
| 96 | 2026-10-11 | `arXiv Dyson sphere swarm construction Mercury material disassembly review Wright 2020 "Dyson spheres" Serbian Astronomical Journal energy timescale` | useful | |
| 97 | 2026-10-11 | Page (curl + pdftotext): arXiv 2006.16734, Wright, "Dyson Spheres", Serb. Astron. J. 200 (2020) | useful (review; no Mercury numbers) | Dyson 1966 deconstruction; Criswell 1986 pointer. The search summary's Mercury sentence was not in the text |
| 98 | 2026-10-11 | `vacuum pyrolysis lunar regolith oxygen extraction temperature sodium potassium volatilize first energy kWh per kg Senior Matchett NTRS` | useful | |
| 99 | 2026-10-11 | Page (curl + pdftotext): NTRS 20070014929, Cardiff et al. (NASA GSFC), "Vacuum Pyrolysis and Related ISRU Techniques" | useful | ~10 g simulant fully vaporized at 1,400 C in vacuum; no kWh/kg |
| 100 | 2026-10-11 | `magnesium production energy consumption Pidgeon silicothermic process kWh per kg Mg electrolytic MgCl2 life cycle study peer-reviewed` | thin | Summaries gave unclear units; PMC link not used |
| 101 | 2026-10-11 | Page (curl + pdftotext): Li, Zhang, Yang, Liu, Liu, "Research, development and application of compound-vertical-retort technology for magnesium production", J. Magnesium and Alloys 11:4724-4736 (2023) | useful | ~1,200 C, ~100 Pa; 1.0-1.6 tce/t Mg reduction stage |
| 102 | 2026-10-11 | Local Python: launch speeds, energies, track lengths, powers, asymptote turn, light times, conjunction days (D8, D10) | useful | Section 5. **Self-correction logged:** the first pass used the sibling's 7.55 km/s as Mercury's v-infinity; it is the burn from a 200 km orbit (v-inf 9.61 km/s). Corrected before writing |
| 103 | 2026-10-11 | `NASA Glenn silicon carbide JFET integrated circuit 500 C operation one year Neudeck Spry durability demonstration Venus GEER 60 days` | useful | |
| 104 | 2026-10-11 | Page: NTRS 20180003391, Neudeck et al., "Yearlong 500 C Operational Demonstration of Up-Scaled 4H-SiC JFET Integrated Circuits" (8 May 2018) | useful | >1 year at 500 C; 175+ transistors |
| 105 | 2026-10-11 | Page: NTRS 20240013278, Neudeck, "Progress Towards SiC ASICs for Extreme Temperature and Radiation Environments" (18 Oct 2024) (first attempt timed out; second succeeded) | useful | 60 days at 460 C / 9.3 MPa; -190 to +812 C; 7 Mrad |
| 106 | 2026-10-11 | `MESSENGER superior solar conjunction communications outage days Mercury orbit DSN BepiColombo solar conjunction duration weeks` | thin | Summaries mention a 47-day cruise conjunction for MESSENGER (not opened; not used) |
| 107 | 2026-10-11 | Page (curl + pdftotext): arXiv 2201.05107, di Stefano, Cappuccio, Iess, "The BepiColombo Solar Conjunction Experiments Revisited" | useful | X-band degraded below 5-7 solar radii; 14-day arcs; flyby count |
| 108 | 2026-10-11 | Local Python: flat-plate equilibrium, radiator sinks, ground IR, rejection capacity (D11) | useful | Section 5 |
| 109 | 2026-10-11 | **Second-angle pass (LAW 0-R) begins.** `Mercury regolith depth thickness estimate impact gardening model meters "regolith" Mercury versus Moon thicker Kreslavsky 2014 LPSC small craters concentric` (extended mode) | useful | Re-opened a topic logged as covered (row 32) |
| 110 | 2026-10-11 | Page (curl + pdftotext): Kreslavsky and Head, "A Thicker Regolith on Mercury", LPSC 46 (2015) abstract 1246 | useful | 20-90 m weak layer; ~25-40 m in smooth plains (preliminary): **conflicts with row 32** |
| 111 | 2026-10-11 | Page (curl + pdftotext): Costello, Ghent, Lucey, "Impact Gardening on the Moon and Mercury: the Source, Age, and Depth to Ice at the Poles", LPSC 50 (2019) abstract 1991 | useful | Gardening slower on Mercury; 1 cm-100 m impactor flux ~10 times lower (Marchi) |
| 112 | 2026-10-11 | `Pokorný 2018 "The Meteoroid Environment and Impacts on Mercury" ApJ abstract mass flux impact velocity` (the title in the query was wrong; the search found the right paper) | useful | |
| 113 | 2026-10-11 | Page (curl + pdftotext): arXiv 1807.02749, Pokorný, Sarantos, Janches, "A comprehensive model of the meteoroid environment around Mercury", ApJ (2018) | useful | 12.2 t/day by population; impact speeds |
| 114 | 2026-10-11 | `MESSENGER spacecraft radiation environment total ionizing dose requirement krad Mercury orbit design solar proton fluence` | dead at the sources | No MESSENGER dose requirement found in any listed page |
| 115 | 2026-10-11 | Page (curl): SPENVIS SUW 2010 "8312_MESSENGER.pdf" | dead (rejected) | It is a solar-cell radiation talk by an author named Messenger (NRL), not the mission |
| 116 | 2026-10-11 | `Mercury north polar illumination model MLA topography maximum average illumination percent solar day Mazarico Deutsch 2014 Icarus "illumination conditions"` | thin | Hamill et al. 2020 PSJ located; APL PDF returned 404 (dead at the source). North-pole maximum illumination still not found |
| 117 | 2026-10-11 | Local Python: meteoroid influx per unit area vs Earth (D12) | useful | |
| 118 | 2026-10-11 | `Mercury surface reduced phases metal silicide Fe-Si metal grains regolith exogenous meteoritic iron contribution weight percent MESSENGER implications` (second angle on free metal, row 22) | useful | Led back to the Mercury Lander report; summary's "up to approximately 6 wt%" sulfur not traced to an opened page (not used) |
| 119 | 2026-10-11 | Page (curl + pdftotext): arXiv 2107.06795 (Mercury Lander report, PSJ/arXiv version), Appendix B and the science traceability matrix | useful | Metals predicted (Si-rich), not measured; XRD detection >1 wt% |
| 120 | 2026-10-11 | `galactic cosmic ray dose rate inner heliosphere 0.3 AU radial gradient percent per AU Helios measurements GCR intensity Mercury orbit` (second angle on GCR, row 83) | useful | |
| 121 | 2026-10-11 | Page (curl + pdftotext): arXiv 1905.01052, Marquardt and Heber, "Galactic cosmic ray hydrogen spectra and radial gradients in the inner heliosphere measured by the HELIOS Experiment 6", A&A (2019) | useful | 2 +/- 2.5 %/AU (250-600 MeV protons); 6.6 +/- 4 %/AU in another channel |
| 122 | 2026-10-11 | Re-read of [NIT18] Table 2.1 layout during the final check | useful | **Self-correction:** the GRS value 0.29 (+0.05/-0.13) had been attached to Mg/Si; [EV12] shows the GRS reported Al, not Mg, so it is Al/Si. Fixed in F1. Two other claims that had come only from search summaries (a melt/vapor ratio and a 28-event SEP index) were removed |
| 123 | 2026-10-11 | Final check against "no figure from memory / every number from a page opened" | useful | **Self-correction:** numbers that had entered the findings from search-engine summaries only (basin fill thickness, Kola depth, a microwave density, a 93 K minimum, BepiColombo cell limits) were removed and their sources moved to Rejected |

## 3. Findings

Source tags used in the tables are expanded in the **Source key** at the end of this section. Every number below was read
in a source opened this session (see the log); derived numbers point to section 5.

### F1. Surface and near-surface composition (MESSENGER XRS, GRS, NS)

**Plain statement for the premise.** The surface that can be mined is **not iron-rich**. Mercury's surface holds about
**1 to 2 wt% iron in total**, in sulfides and possibly some metal, with almost none in silicates. Its rocks are
magnesium-rich silicates (forsterite, enstatite, sodic plagioclase), with unusually high sulfur, sodium, chlorine and
graphitic carbon. The planet's iron is in its core, under a mantle and crust a few hundred kilometers thick (F2).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Total Fe, surface average | "~1–2 wt%" (review); XRS Fe/Si 0.053 (sigma 0.013), GRS Fe/Si 0.077 +/- 0.013; Weider 2014: mean Fe/Si "~0.06 (equivalent to ~1.5 wt % Fe)"; observed range Fe/Si 0.02 to 0.1 | [NIT18] §2.3.2 and Table 2.1; [WEI14] abstract | Primary | [EV12] GRS Fe/Si 0.077; early XRS (Nittler 2011 GSA abstract [NIT11a]): "less than ~4 wt%"; LPSC 2016 [VK16]: "less than 2.5 wt%" | High that Fe is a few wt% at most; medium on the exact average (next row) |
| Systematic uncertainty on Fe | Iron grains larger than a few tens of micrometers could change the XRS Fe/Si photon ratio "by up to a factor of five"; "there is a very large systematic uncertainty to the overall normalization of Fe/Si from the XRS data"; the XRS map was arbitrarily normalized to an average Fe/Si of 0.06, "slightly lower than" the GRS 0.077 | [NIT20] §2 | Primary | GRS (not subject to the XRS mixing effect, sampling tens of cm) gives 0.077 +/- 0.013 [EV12] | High that this caveat is real; GRS bounds the average near 2 wt% |
| Form of the iron | "Iron on Mercury's surface is highly reduced and most likely largely incorporated into metal and/or sulfide phases in the regolith"; "Fe is most likely contained as a minor component in sulfide phases (e.g., troilite, niningerite, daubréelite) and as Fe metal" rather than in mafic silicates. Pre-MESSENGER spectra: surface silicates "no more than ~3–5 wt% FeO, and possibly much less" | [NIT20] §2; [WEI14]; [NIT18] §2.1 | Primary | Normative mineralogy [VK16] assigns all Fe to FeS: 0.21 to 2.68 wt% FeS across nine regions | Medium. **No measurement found that shows free iron-nickel metal at the surface in a stated quantity.** Metal is inferred, not measured; at most it is a share of the 1-2 wt% total |
| Metal at the surface: predicted, not measured | Surface minerals are predicted to include "Mg-rich silicates, oxides, sulfides, and metals"; owing to the lack of spectral features MESSENGER could not determine mineralogy directly; one hypothesis (McCubbin et al. 2017) is that degassing "smelting reactions" left "highly reduced metals (e.g., Si-rich metals) on the surface"; the 2020 Mercury Lander's X-ray diffractometer is specified to find metallic phases "if present at concentrations of >1 wt%" | [ML20] App. B and STM | Primary (NASA study) | [NIT20], [WEI14] (Fe as metal and/or sulfide) | High that free metal is unconfirmed; the metal that is predicted is Si-rich, not iron-nickel |
| Space-weathering metal | VIRS radiative-transfer maps give wt% of nanophase and microphase native iron and amorphous carbon; the global submicroscopic carbon average is "1.4±0.3 wt.% C"; no iron average was given in the pages opened | [TRA17] PDS product description; [TRA15] AGU abstract | Primary | none for iron | Low for iron (number not found) |
| Si (absolute, used to convert ratios) | about 25 wt% (implied by Weider 2014: Fe/Si 0.06 = 1.5 wt% Fe). GRS Si varies "by just ~15%" across the surface | [WEI14]; [NIT18] §2.3 | Primary (derived ratio) | none | Medium |
| Mg | Mg/Si 0.436 (sigma 0.106) XRS average, i.e. **about 11 wt%** (D1); mapped range Mg/Si 0.1 to 0.8 (about 2.5 to 20 wt%) | [NIT18] Table 2.1; [WEI15] | Primary | none (the GRS did not report Mg, per [EV12]) | Medium (large regional spread) |
| Al | Al/Si 0.268 (sigma 0.048), **about 6.7 wt%**; range Al/Si 0.1 to 0.4 | [NIT18] Table 2.1; [WEI15] | Primary | GRS Al/Si 0.29 (+0.05/-0.13) [NIT18] Table 2.1 (the table's layout places this value between the Mg and Al rows; the GRS measured Al, not Mg, per [EV12]) | Medium |
| S | XRS S/Si 0.076 (sigma 0.019), GRS 0.092 +/- 0.015: **about 1.9 to 2.3 wt%** average; "up to ~4 wt%" locally; "at least 10 times higher" than Earth's or the Moon's silicate portion | [NIT18] Table 2.1; [EV12]; [NIT11a] | Primary | [VK16]: "up to 4 wt%" | High |
| Ca | XRS Ca/Si 0.165 (sigma 0.030), GRS 0.24 +/- 0.05: about 4 to 6 wt%; Ca/Si "highly correlated with S/Si" (CaS/oldhamite component suspected) | [NIT18] Table 2.1 and §2.3.2 | Primary | [EV12] | Medium |
| Na | **2.9 +/- 0.1 wt%** (GRS, northern hemisphere); Na/Si 0.107 at 0-60 N rising to 0.198 at 80-90 N | [EV12]; [NIT18] Table 2.1 | Primary | Na/Si 0.12 x 25 = 3.0 wt% (D1) | High |
| K | 1,288 +/- 234 ppm average; range 240 to 2,500 ppm | [NIT18] Table 2.1 | Primary | none | High |
| Cl | Cl/Si 0.0057 +/- 0.0010 average (about 0.14 wt%), 0.014 at 80-90 N | [NIT18] Table 2.1 | Primary | none | Medium |
| C | GRS **1.4 +/- 0.9 wt%** northern average (upper limit <4.1 wt% at 3 sigma); spectral model ~1 wt% globally, ~5 wt% in low-reflectance material (LRM); LRM deposits measured +1.1 to 3.1 wt% above ~1 wt% surroundings; carbon is graphite, endogenic, "remnants of a primary graphite-rich crust" excavated by impacts | [NIT18] §2.3.3 | Primary | VIRS model 1.4 +/- 0.3 wt% [TRA15]; Carnegie release: "as much as a few weight percent graphitic carbon" [CAR16] | High that C is ~1-4 wt% |
| O | GRS O/Si 1.2 +/- 0.1, lower than stoichiometry predicts (~1.7); may reflect near-surface alteration by magmatic degassing "similar to industrial smelting" | [NIT18] §2.3.3 | Primary | none | Low (authors caution) |
| Ti, Cr, Mn | Ti/Si 0.012, Cr/Si 0.006, Mn/Si 0.004 (each <1 wt%; Ti about 0.3 wt%) | [NIT18] Table 2.1 | Primary | [NIT11a]: Ti "less than ~0.8 wt%" | Medium (near detection limit) |
| Th, U | Th 0.155 +/- 0.054 ppm; U 90 +/- 20 ppb | [NIT18] Table 2.1 | Primary | none | Medium (U possibly overestimated through radon transport) |
| Regolith homogeneity with depth | XRS (micrometers) and GRS (tens of cm) agree, so the regolith is "on average, homogenous to a depth of tens of centimeters" | [EV12] | Primary | [NIT18] §2.3 | High |
| Normative mineralogy (nine regions) | Plagioclase 32-58 wt%, olivine 0-35, hypersthene 0-37 (sic), diopside 0-37, quartz 0-8, FeS 0.21-2.68, MgS 0-3.23, CaS 0-0.33, TiS2 0-1.85, CrS 0-0.88, MnS 0-0.86 wt%; "dominated by forsterite, enstatite, and albitic plagioclase" | [VK16] Table 1 and text | Primary (conference abstract) | [NIT18]: rocks "more similar to low-FeO terrestrial magnesian basalts" (norites or boninites) | Medium (a calculation, not a measurement) |
| Regional terranes | **High-Mg region (HMR)**, >5 x 10^6 km^2, mid-north to equatorial, western hemisphere: highest Mg/Si, Ca/Si, S/Si and Fe/Si, lowest Al/Si, thin crust, possibly an ancient basin. **Northern smooth plains**: low Mg, Al, Ca, S; high K, Na, Cl. **Caloris interior plains**: relatively high Al, low Mg, Ca, S, Fe, K. **LRM**: carbon-enriched | [WEI15]; [NIT18] §2.3.2 | Primary | [NIT20] maps | High (qualitative) |
| Oxygen fugacity | Interior log fO2 = IW-5.4 +/- 0.4 (range of estimates IW-3 to IW-7) | [NIT18] §2.3.2 | Primary | [VK16]: 2.6 to 7.3 log units below IW | High |
| Volatile loss from hot ground | ~10 µm Na-rich feldspar grains can lose Na over ~1 Gy at ~400 K; K loss at ~475 K; surface reaches "up to ~700 K at places" | [NIT18] §2.3.1 | Primary | none | Medium |

**What the high sulfur implies for processing** (from F1 and F10): with sulfur at 2-4 wt% held in Ca-, Mg-, Fe-, Cr-,
Ti- and Mn-sulfides, any melt or thermal process releases sulfur species; at Mercury's oxygen fugacity sulfur
partitions into silicate rather than metal ([NIT18] §2.5: below about IW-4 "more S partitions into the silicate
phase than the metallic phase"). See F10.

### F2. Bulk structure and how much metal is reachable

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mass, mean radius, mean density | 0.33010 x 10^24 kg; 2,439.7 km (equatorial 2,440.5, polar 2,438.3); 5,429 kg/m^3 | [NSSDC-Me] (last updated 11 Jan 2024) | Primary | sibling `starlifting_physics_and_minimum_infrastructure.md` uses the same sheet | High |
| Uncompressed density | 5.4 g/cm^3, against 4.4 for Earth and Venus | [NIT18] §2.1 | Primary | none | High |
| Polar moment of inertia | 0.333 +/- 0.005 (C/MR^2, MESSENGER geodesy); fact sheet still lists 0.35 | [GEN19]; [NSSDC-Me] | Primary | see Conflicts K2 | High for 0.333 |
| Outer (liquid) core radius | 1,985 +/- 39 km (4-shell models) or 1,967 +/- 23 km (multi-layer Fe-Si), "significantly lower" than 2,020 +/- 30 km (Hauck et al. 2013); Rivoldini and Van Hoolst 2013: 2,004 +/- 39 km | [GEN19]; sibling `starlifting_physics_and_minimum_infrastructure.md` (via [WH17]) | Primary | each other | High (about 1,970 to 2,020 km) |
| Solid inner core | Radius ratio r_ic/r_oc = 0.538 +/- 0.195 (4-shell) or 0.445 +/- 0.181 (Fe-Si) or 0.517 +/- 0.170 (Fe-S-Si); stated range "between 0.3 and 0.7" of the outer core; Fe-S outer core cases give >= 0.4 | [GEN19] | Primary | AGU press release: inner core "about ... 2,000 kilometers wide" and "about half" of the core [AGU19] (secondary) | Medium (wide uncertainty) |
| Core composition | Fe ~75-95 wt%, Ni ~5 wt% (assumed), Si >0 to 17 wt%, S 0 to 20 wt%, C up to a few wt% (geophysical and experimental models) | [NIT18] Table 2.3 | Primary | sibling: "not pure metal (Fe with S and Si)" | Medium (light-element content poorly constrained) |
| Core mass fraction | About 73% for r = 2,020 km and 6,980 kg/m^3 (sibling D6); about 69 to 72% for r = 1,985 km at 6,980 to 7,233 kg/m^3 (D2) | sibling `starlifting_physics_and_minimum_infrastructure.md`; D2 | Derived | [AS13] "70% metal" (sibling) | Medium (depends on density model) |
| Mantle thickness | "the mantle is 400 km thick" (Hauck 2013; Rivoldini and Van Hoolst 2013; Margot 2018) | [BEU20] §1 | Primary (review statement) | depth to core 420 to 473 km (D2) minus crust | High |
| Crust thickness, average | "Recent estimates ... range from 20 to 50 km"; 35 +/- 18 km (Padovan 2015, geoid-to-topography); 26 +/- 11 km (Sori 2018); 35 km adopted by Genova 2019 | [BEU20] §1 and §S; [GEN19] | Primary | each other | Medium |
| Crust thickness, regional | Northern Volcanic Plains 19 +/- 3 km; High-Mg region 50 +/- 12 km (thickest; "refuting the hypothesis of an impact origin for that region") | [BEU20] abstract | Primary | Contradicts [WEI15]'s "relatively thin crust" for the HMR: see Conflicts K3 | Medium |
| Depth from surface to core metal | **About 420 to 470 km** (D2) | D2 from [GEN19], [WH17] | Derived | [WH17]: mantle is "only the outer 16 to 19%" of the radius (sibling) | High |
| Volcanic fill in basins | Thickness figures appeared only in a search summary (row 29) and are **not used**; no page with them was opened | row 29 | n/a | none | Gap |
| Published study of reaching Mercury's metal from the surface | **None found.** No paper located that addresses mining or excavating the core of Mercury other than whole-planet disassembly (F9) | rows 28-29 | n/a | n/a | Gap |

### F3. Regolith and surface properties

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Regolith thickness | Median **4.6 m** (smooth plains) and **3.7 m** (intercrater plains), "highly variable laterally", Borealis Planitia (66 N), from 3,546 craters <400 m with flat floors, central mounds or concentric forms, plus 855 bowl-shaped craters as a lower bound | [JOU26] abstract (Planet. Space Sci. 282, Nov 2026, in press as listed) | Primary | **Conflicts with** Kreslavsky and Head 2015: weak-layer thickness 20-90 m from >100 craters on images better than 14 m/pixel, "preliminary", "~25 - 40 m thick regolith in smooth plains"; they note lunar melt pools could be mistaken for flat floors at that resolution [KRE15]. See Conflicts K5 | Medium-low (two methods disagree by about 6-10 times) |
| Regolith homogeneity with depth | Homogeneous on average to tens of cm (XRS vs GRS) | [EV12] | Primary | [NIT18] | High |
| Grain size | No measured value found. The lab group preparing BepiColombo's MERTIS states "Mercury regolith is mostly composed of very fine particles" and used <25 µm fractions | [MAT17] (EPSC 2017 abstract) | Primary (statement of assumption, not a measurement) | none | Low |
| Bulk density, thermal inertia, strength | **No Mercury measurement opened.** A microwave-derived near-surface density (Mitchell and de Pater 1994, Icarus 110:2-32) surfaced only in a search summary (row 43); the paper could not be opened, so no value is given. The 2020 Mercury Lander study **assumed** lunar-like terrain and rock size-frequency distribution for landing | [ML20] §3.3 | Primary (lander assumption) | none | Gap: see Open threads. Use lunar values as an explicitly assumed analog only |
| Micrometeoroid flux relative to the Moon | Impact rate **5.5 times** the Moon's; mean impact velocity **more than 60% higher** (extrapolated from the terrestrial flux) | [CIN92] abstract | Primary | Kreslavsky and Head: micrometeorite bombardment argued to be "orders of magnitude more intensive than on the Moon" (citing Cintala 1992 and Borin 2009) [KRE15]. (A search summary's "~15 times the melt and ~20 times the vapor" was not found in an opened page and is not used) | Medium (a 1992 extrapolation) |
| Gardening rate (meter scale) | A 1 m ice deposit on Mercury "would still be cohesive after 1 Gyr", while one on the Moon is pulverized in about 200 Myr, because the flux of 1 cm-100 m impactors is "about ten times lower on Mercury" (Marchi et al.) | [COS19] | Primary (LPSC abstract) | Kreslavsky and Head: micrometeorite bombardment "orders of magnitude more intensive" (cm-scale and below) [KRE15]. Size ranges differ: see Conflicts K6 | Medium |
| Meteoroid mass influx (calibrated model) | **12.2 t/day** total (asteroidal 0.26, Jupiter-family comets 7.84, Halley-type 1.69, Oort-cloud 2.37 t/day), i.e. 4.4 x 10^6 kg/yr; impact speeds mostly 15-80 km/s with a retrograde population near 60-80 km/s; about 1.9 times Earth's top-of-atmosphere influx per unit area (D12) | [POK18] §4-5 | Primary (ApJ preprint) | [FRA22] quotes 4.4 x 10^6 kg/yr | Medium |
| Total dust mass flux onto Mercury | Estimates disagree by about 45 times: 1.97 x 10^8 kg/yr (Borin et al. 2017, 5-100 µm); 4.4 x 10^6 kg/yr (Pokorný et al. 2018, 10-2,000 µm); ~6 x 10^6 kg/yr (Frantseva et al. 2022) | [FRA22] §1 and §2.3 | Primary | Eke 2017: recent estimates "~60, 30 and 10 times" those of Moses 1999 [EKE17] | Low (the disagreement is the finding) |
| Surface charging | "Surface charging at Mercury remains an open question at present"; models show a tendency to negative charging on the nightside and in dayside shadow (electron fluence about twice the proton fluence); photoemission not modeled | [LAV23] §4 | Primary (preprint of a journal paper) | Lunar anchor: dayside "several to 10 V positive" from photoemission [MIY24] | Medium (qualitative) |
| Dust lofted by landing | The Mercury Lander design flies the last 15 m on inertial measurement only, "to avoid any interference of lofted dust with LIDAR" | [ML20] §3.3 | Primary | none | Medium |

### F4. Thermal environment, rotation and illumination

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Rotation and day | Sidereal rotation 1,407.6 h (58.65 d); orbit 87.969 d (3:2 spin-orbit, D3); **solar day 4,222.6 h = 175.9 d**; obliquity 0.034 deg | [NSSDC-Me] | Primary | NASA: "One Mercury solar day ... equals 176 Earth days" [NASA-F] | High |
| Continuous daylight and darkness at the equator | About **88 Earth days of day, then about 88 of night** (half a solar day, D3) | Derived D3 | Derived | [ML20]: the lander's night lasts "88 Earth days" | High |
| Sunlight at the surface | 4.7 to 11.1 times Earth's (aphelion 0.46 AU to perihelion 0.30 AU); NSSDC mean 9,082.7 W/m^2 (6.67 times Earth's) | [HOL15] §I; [NSSDC-Me] | Primary | D4: 6,250 (aphelion) to 14,390 W/m^2 (perihelion); 4.6 to 10.6 times 1,361 W/m^2 | High (see Conflicts K4 on rounding) |
| Subsolar maximum | **Up to 451 C (724 K)** at the subsolar point near perihelion; 335 C at 60 deg from the subsolar point | [HOL15] §I | Primary (MESSENGER thermal team) | NSSDC: "590-725 K, sunward side"; hot poles (0 and 180 deg longitude) max ~700 K, warm poles (90 and 270) ~570 K (Bauch et al. 2021 as quoted by [LAV23]); D4 radiative equilibrium 710 K / 576 K | High |
| Night minimum | **-163 C (110 K)** nightside; NASA: "as low as -290 F (-180 C)" | [HOL15]; [NASA-F] | Primary | none opened beyond these two | Medium (the two primaries differ by 17 K) |
| Surface emissivity | ~0.93, varying slightly with location | [HOL15] | Primary | none | Medium |
| Diurnal and annual thermal wave | Annual average temperature "representative of the expected temperatures at depths greater than **~0.4 m**, the depth of penetration of Mercury's annual temperature wave" | [PAI12] | Primary (conference abstract) | Butler et al.: skin depths "a few 10's of cm" for the Moon and Mercury [BUT04] | Medium |
| Polar cold traps | Model annual-average temperatures in radar-bright regions peak at **100 K**; annual maximum ~**170 K**; exposed ice too warm in most radar-bright areas, but stable ~10 cm down | [PAI12] | Primary | [EKE17]: radar-bright regions are where modeled temperatures stay below ~100-150 K | Medium |
| Permanently shadowed area | North (1.25 to 1.46) x 10^10 m^2 (12,500 to 14,600 km^2); south (4.3 +/- 1.4) x 10^10 m^2 | [FRA22] citing Chabot 2012 and Neumann 2013 | Primary (citing primary) | radar-bright area ~10,000 km^2 at the north pole [EKE17] | Medium |
| Share of shadow holding radar-bright material | ~46% of persistently shadowed area (images) and ~43% of permanently shadowed area (altimetry); all large deposits (craters >= 6 km) lie in shadow | [DEU16] | Primary | none | High |
| Best-lit polar point ("peak of eternal light") | **About 82% of the solar day** at 89 S, 50.7 E; "no such peak of eternal light has been identified at Mercury's south pole" | [NASA-PEL] (MESSENGER, 24 Dec 2011) | Primary (agency) | north-pole figure not found (row 56) | Medium |
| Lander-scale thermal facts | Landing at dusk near aphelion with 2 deg Sun elevation keeps the surface under 40 C; the lander survives the night on an RTG; "thermal conditions exceed vehicle operating temperatures shortly after sunrise", ending the mission | [ML20] §2.1, §3.2.3 | Primary (NASA mission concept study) | none | High (as a design statement) |

### F5. Volatiles: polar ice and other species

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Ice identification | Neutron spectrometer: a hydrogen-rich layer "of unknown thickness" under a less hydrogen-rich layer (< 25 wt% water-equivalent hydrogen) **0.1 to 0.3 m** thick (Lawrence 2013); "nearly pure water ice" | [FRA22] §1; [EKE17] §1 | Primary (citing primary) | Paige: ~10 cm dark, organic-rich layer over stable ice [PAI12] | High that it is water ice |
| Radar evidence | Bright, depolarizing echoes at 3.5, 12.6 and 70 cm wavelengths; deposits "extend to depths of several meters" | [EKE17]; [PAI12] | Primary | each other | High |
| Surface albedo of deposits | Only Prokofiev crater shows high albedo (exposed ice) in MDIS images; most radar-bright regions are anomalously dark (buried under the dark layer) | [EKE17] §1 | Primary | MLA 1,064 nm reflectance (Neumann 2013 via [EKE17]) | High |
| Ice mass, MESSENGER range | **2.1 x 10^13 to 1.4 x 10^15 kg** (Lawrence 2013; both poles, assuming the south is like the north, layers 0.5 to 20 m) | [FRA22] §1 | Primary (citing primary) | Moses 1999 (radar): 4 x 10^13 to 8 x 10^14 kg for 2-20 m | Medium (thickness unknown) |
| Ice mass, upper limit | Typical excess height of radar-bright regions in 12 fresh craters (50 +/- 35) m, a ~1.5 sigma detection; upper limit **~3 x 10^15 kg** total | [EKE17] abstract and §4 | Primary | none | Medium |
| Ice delivery today | Asteroids ~1 x 10^3, comets ~1 x 10^3, dust ~16 x 10^3 kg/yr of water reaching the poles, "within a factor of several" | [FRA22] abstract | Primary | none | Low-medium |
| Other cold-trapped species | Sulfur and aromatic hydrocarbons can also be cold-trapped; the dark layer is interpreted as organic-rich | [PAI12] | Primary | [NIT18] §2.3.1: "possibly C-bearing organic compounds" | Medium |
| Burial rate | Impact gardening buries polar volatiles at ~0.4 cm/Myr (Crider and Killen 2005) | [NIT18] §2.3.1 | Primary (citing primary) | none | Medium |
| Moderately volatile elements in rock | Na ~2.9 wt%, S ~2-4 wt%, K ~0.13 wt%, Cl ~0.14 wt% (F1); "similar to those found on the surface of Mars" | [NIT18] §2.3.1 | Primary | F1 | High |
| Exosphere | Surface pressure < ~5 x 10^-15 bar; Na column 12,000 to 200,000 per cm^2 (fact sheet); "composed mostly of oxygen, sodium, hydrogen, helium, and potassium"; total mass under about 10,000 kg (sibling) | [NSSDC-Me]; [NASA-F]; sibling `starlifting_physics_and_minimum_infrastructure.md` | Primary | none | High (it is negligible as a resource) |

### F6. Solar power

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Irradiance, mean / perihelion / aphelion | 9,082.7 W/m^2 at the semimajor axis (6.67 times Earth's); **14,390 W/m^2 at perihelion, 6,250 W/m^2 at aphelion** (D4); orbit-time average 9,280 W/m^2 (D4) | [NSSDC-Me]; D4 | Primary / derived | [HOL15]: 4.7 to 11.1 Earth solar constants; D5 from solar luminosity gives the same 14,396 / 6,249 | High |
| Flown array practice at Mercury (MESSENGER) | 28% triple-junction cells between optical solar reflectors at a **1:2 cell-to-mirror ratio**; panels held normal to the Sun only until **150 C**, then tilted away; anomaly case up to 275 C; qualified -140 to +275 C, flight panels cycled to 240 C (substrate glass-transition limit); spacecraft load 595 W in orbit | [ERC06] | Primary | Landis 2004: MESSENGER "incorporates reflective panels over 2/3 of the solar array area" at 10.6 AM0 [LAN04] | High |
| BepiColombo arrays | Facing the Sun they would reach "about 350 C – 120 degrees higher than the maximum tolerable solar cell operating temperature" (i.e. about 230 C); design uses mirrors beside each cell row and a high Sun angle; in testing "just one simulated month saw a 20% power loss" from UV plus heat, which "brought the mission to the brink of cancellation"; MPO array "up to 1000 W" in science phases | [ESA09]; [ESA11]; [ESA-BC] | Primary (agency) | MPO design temperature limits appeared only in a search summary (row 70), not used | Medium-high |
| Mercury Lander arrays (study) | Inverted metamorphic multijunction cells, 32% BOL; wings "must be rotated off normal ... to maintain an operating temperature below 165 C", and 90 deg off Sun during sub-solar crossings; orbital stage array 1.1 kW BOL at 0.46 AU from 3 m^2 total | [ML20] §3.2.4 and summary table | Primary (study) | none | Medium (design, not flown) |
| High-temperature cell physics | Mercury surface station equilibrium "about 450 C"; efficiency falls with temperature mainly through open-circuit voltage; the optimum bandgap rises from slightly under 1.5 eV at 300 K to about 2 eV at 1,000 K; SiC cells with TiSi2 contacts made for 600 C operation (contacts stable to 900 C); irreversible failure modes listed (contact degradation, dopant diffusion, coverglass debonding) | [LAN04] | Primary (conference preprint) | none | Medium (theory plus prototypes; no flown cell at 450 C) |
| Theoretical efficiency vs temperature | Optimum-bandgap cell, read off [LAN04] Fig. 4: roughly 33-35% at 300 K, about 20% near 600 K, about 13% near 800 K (approximate graph reading) | [LAN04] Fig. 4 | Primary (theory) | none | Low (read from a plot) |
| Power per m^2 of sun-facing cell | Bound: S x efficiency, i.e. about 1,250 (aphelion) to 2,880 W/m^2 (perihelion) at 20%, and 1,750 to 4,030 W/m^2 at 28% if the cell could be held cool enough (D5). Flown designs cut this deliberately by mirrors (2/3 of area) and tilt | D5 from [NSSDC-Me], [LAN04], [ERC06] | Derived | none | Medium as an upper bound |
| Surface night storage | Equatorial night ~88 days: **about 2,100 kWh of storage per kW of continuous load** (D6). Best polar point (82% lit): about 32 days of darkness per 176-day solar day in total, about 760 kWh per kW if contiguous (D6; contiguity not stated by the source) | D6 from [NSSDC-Me], [NASA-PEL] | Derived | none | High (arithmetic) |
| Published surface power concept | The 2020 Mercury Lander uses **one NextGen RTG (16 GPHS), 373 W BOL** and a 4.5 Ah battery; no surface solar power; the mission ends shortly after sunrise on thermal grounds | [ML20] summary table, §3.2.4 | Primary (study) | none | High (as a design choice) |
| Solar concentration for furnaces | Ideal stagnation concentration needed (no losses): to 1,923 K (1,650 C, the carbothermal temperature in sibling `space_processing_and_fabrication.md`) about **54x at perihelion, 124x at aphelion vs 570x at 1 AU**; the brightest achievable focus (sun-surface brightness, 5,772 K) is the same at any distance, but the maximum concentration falls from about 46,000 at 1 AU to about 4,400 at perihelion (D5) | D5 from [NSSDC-Sun], [NSSDC-Me] | Derived | none | High (geometry), low as a furnace design figure |

### F7. Radiation and plasma

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| SEP proton peak intensity vs distance | Ensemble average **R^-2.5 (4-13 MeV) to R^-1.6 (27-37 MeV)**; fluences R^-1.9 to R^-0.9; the dominant factor is magnetic connection longitude, "not the heliocentric radial distance"; the older engineering guideline (R^-3 peak, R^-2.5 fluence, Shea 1988) overestimates inner-heliosphere values | [LAR06] (COSPAR 2006 abstract of ApJ 653:1531) | Primary | Diffusion models: R^-3.3 and R^-2.1 [LAR06] | Medium |
| Implied factors at Mercury | At 0.31 to 0.47 AU: peak intensity x 6.5 to 18.7 (0.31 AU) and x 3.4 to 6.6 (0.47 AU); fluence x 2.9 to 9.3 and x 2.0 to 4.2, relative to 1 AU (D7) | D7 | Derived | none | Medium (ensemble average; single events vary widely) |
| SEP electrons | Peak intensities follow about R^-3 between 0.3 and 1 au (MESSENGER 2011-2015 vs 1 au spacecraft); spectra soften outward | [ROD24] (EGU24-6213 abstract) | Primary (abstract) | none | Medium |
| GCR at Mercury | GCRs "continuously bombard Mercury's surface"; GCR flux at Mercury's orbit has so far been available "only through modeling" | [MIL20] §2 | Primary (review) | Helios E6 (1974-78): GCR proton (250-600 MeV) radial gradient **2 +/- 2.5 %/AU** between 0.3 and 1 AU, i.e. GCR intensity at Mercury is within a few percent of Earth's (outside the magnetosphere) [MAR19] | Medium for intensity; gap for a dose number |
| Magnetospheric shielding of SEPs | Størmer cutoff: protons < 55 MV (~2 MeV) cannot reach the surface within +/-20 deg latitude; < 20 MV (~200 keV) cannot reach +/-40 deg; at tens to 100 MeV "the field is no longer able to significantly alter the particle trajectories" | [MIL20] §2 (citing Laurenza 2011) | Primary | none | Medium. **The field does not shield the surface from penetrating (tens of MeV and above) protons or GCRs** |
| Solar wind shielding | The intrinsic field shields the surface from "roughly 90% of the incoming solar wind flux"; precipitating protons <0.5 to >1.5 keV, electrons 0.1-4 keV | [LAV23] abstract | Primary | none | Medium (simulation) |
| Radiation belts | Substorm electrons "often unable to complete a full orbit ... no 'Van Allen'-like radiation belts are formed" | [MIL20] §2 | Primary | none | High |
| Surface field | Dipole ~0.002 G R^3; surface 0.0025 to 0.007 G; "1% the strength of Earth's" | [NSSDC-Me]; [NASA-F] | Primary | none | High |
| Micrometeoroids and ejecta | See F3: 5.5 times the lunar impact rate at >60% higher speed; total dust flux estimates disagree by ~45 times | [CIN92]; [FRA22] | Primary | none | Medium-low |

### F8. Landing, surface launch and low orbit

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Surface gravity, escape speed, GM | 3.70 m/s^2; 4.3 km/s (4.25 computed); GM 22,031.8636 km^3/s^2 | [NSSDC-Me]; [GEN19] (GM); D8 | Primary | sibling trucking file: 4.25 km/s, 9.03 MJ/kg | High |
| Circular speed at the surface | 3.005 km/s (D8); 2.945 km/s at 100 km (Palaszewski) | D8; [PAL17] | Derived / primary | sibling: 2.89 km/s at 200 km | High |
| Equatorial rotation speed | ~3.0 m/s (D8): no useful launch boost | D8 from [NSSDC-Me] | Derived | none | High |
| Landing and ascent delta-v (study figures) | Lander one-way 3.5 km/s, ascent 3.5 km/s (~19% gravity loss) (Palaszewski, already in the sibling trucking file); Mercury Lander: SRM braking from **3.395 km/s horizontal to 83 m/s (3.313 km/s)** in 75 s, then a 34 s liquid descent; stage budgets: orbital stage 917 m/s, descent stage 3.3 km/s, lander 316 m/s | [PAL17]; [ML20] §3.3 and Exhibit 27 | Primary | each other | High (as study figures) |
| Landing hazard assumption | Hazard detection "assumes similar terrain and rock size-frequency distribution as found on the Moon"; final 15 m on IMU only because of lofted dust | [ML20] §3.3 | Primary | none | Medium |
| Low-orbit stability | MESSENGER's periapsis fell from ~450 km to 115 km over 15 months under solar gravity (rate set by the angle between the Sun line and the orbit plane); four OCMs of 5.1, 8.5, 19.3 and 9.7 m/s held 25 km and 15 km minimum altitudes and delayed impact about seven months; impact 30 Apr 2015 | [MOE14]; [HOL15] | Primary | sibling: MOI 0.86 km/s into a 12-h orbit | High (for MESSENGER's eccentric orbit; no figure found for a low circular orbit's lifetime) |
| Orbit thermal choice | The Mercury Lander parks in a 100 x 6,000 km polar orbit chosen to keep stage sink temperatures at or below ~0 C; behind the sunshade the sink swings from below -100 C to ~255 C in 30-minute passes over the hot planet | [ML20] §3.2.3 | Primary | MESSENGER flew a dawn-dusk initial orbit for the same reason [HOL15] | High |
| Surface launch speed needed (no gravity assists) | Escape only 4.25 km/s; Hohmann to Venus (v-inf 6.77 km/s) **7.99 km/s**; to Earth (v-inf 9.61) **10.51 km/s**; to Mars (v-inf 12.58) **13.28 km/s** (D8, circular coplanar orbits) | D8 | Derived | sibling trucking D1 gives the same 9.61 km/s implicitly (7.55 km/s burn from 200 km orbit) | High as an ideal lower bound |
| Energy per kg at launch | 9.0 MJ/kg (escape), 31.9 (Venus), 55.2 (Earth), 88.2 MJ/kg (Mars) kinetic energy at the muzzle (D8) | D8 | Derived | lunar SP-428 driver: 2.88 MJ/kg | High |
| Lunar mass-driver anchor | SP-428 III-3 point design: 2,400 m/s, 1,000 g, 488 m, 125 MW, 42 kg/s, 650,000 t/yr, 96.4% efficiency, 3,130 t (sibling trucking file) | sibling `space_trucking_and_transport_infrastructure.md` | Primary (via sibling) | none | Medium (never built at scale) |
| Mercury scaling of that design | At the same 1,000 g and 42 kg/s: accelerating length **0.92 km** (escape), **5.6 km** (Earth Hohmann), 9.0 km (Mars); muzzle power **0.39 GW** (escape) to **2.4 GW** (Earth) at 96.4% efficiency; a 1 Mt/yr average flow needs 0.30 GW (escape) to 1.8 GW (Earth) of continuous electric power (D8). At 100 g lengths are ten times longer | D8 | Derived | none | Medium: the linear scalings are physics; whether 1,000 g buckets, 10 km/s muzzle speeds and multi-GW pulsed power can be built is not established anywhere found |
| What scales and what does not | Scales: track length with v^2/a, energy with v^2, power with v^2 x mass flow. Does not scale from the Moon: Mercury needs 1.8 (escape) to 4.4 (Earth Hohmann) times the lunar 2.4 km/s and 3.1 to 19 times the energy per kg (5.5 and 31 times for Mars); the solar power available is 4.6 to 10.6 times the Moon's per m^2, but the equatorial night is 88 days and the day surface reaches ~700 K (F4) | D8, F4, F6 | Derived | none | Medium |
| Launch direction | For outbound targets (Venus, Earth, Mars) the hyperbolic excess velocity must point along Mercury's orbital velocity (prograde); the asymptote turns only 3 to 10 deg from the launch direction at these speeds (D8). A fixed track on the slowly rotating surface faces a given direction relative to the Sun once per 176-day solar day, while windows to Earth recur every 115.88 days (synodic period, [NSSDC-Me]) | D8 | Derived (reasoning, no source found) | none | Medium: **a fixed launcher cannot fire on every window**; see Constraints |
| Rotating tether anchor | Characteristic speed v_c = sqrt(2 sigma / rho); carbon-nanotube cable estimate 22 GPa and 1.5 g/cm^3 gives v_c ~5.4 km/s; aramid fibers "approaching 3.0 km/s" (untapered) | [HOW18] (arXiv physics.pop-ph preprint) | Preprint (low) | sibling `moon_lagrange_and_comparables.md`: O'Neill rotary launcher tip speed 2,400 m/s | Low. A surface-skimming skyhook needs tip speed about equal to 3.0 km/s orbital speed, at the edge of untapered aramid; escape from the surface needs 4.25 km/s |
| Launch loop at Mercury | No published study found | rows 88, 132 (sibling) | n/a | n/a | Gap |

### F9. Published concepts for using Mercury's material

| Concept | Stated masses, rates, power, timescales | Source | Evidence level | Notes |
|---|---|---|---|---|
| Whole-planet disassembly for a Dyson swarm (Armstrong and Sandberg) | 1 km^2 seed of panels; 1/3 efficiency; 1/10 of power to mass drivers; 5-year processing lag; Mercury "completely disassembled in 31 years and 85 days"; binding energy 1.80 x 10^30 J | sibling `starlifting_physics_and_minimum_infrastructure.md` ([AS13]) | **SPECULATIVE** (exploratory engineering; authors: "would cost a lot and would be unlikely to be attempted") | Assumes "30% silicate and 70% metal" bulk; does not use the MESSENGER surface data. **The metal is the core, 420-470 km down (F2)** |
| Dyson's original planet deconstruction | Dyson (1966): no physical barrier to rigid structures up to 10^6 km; planets "can (in principle) be deconstructed" for a sphere "of order meters" thick; Wright notes the Sun could unbind every atom of Jupiter in under 1,000 years, and leaves the mechanics of deconstruction to Criswell 1986 | [WRI20] | **SPECULATIVE** (review) | No Mercury-specific numbers in the review (the search summary's Mercury sentence was not found in the text) |
| Mercury polar-ice propellant for crewed missions (Palaszewski) | Hydrogen from polar water shipped to orbit: 104 t (NTP-1) or 90 t (NTP-2); LEO mass 3,892 t to 1,517 t and 2,793 t to 1,136 t; about 10-11 round-trip lander flights; 10 t payload lander 27 t (one-way) vs 140 t (round trip) in LEO; base and mining sites at the shadowed crater edge with PV outside the shadow; quotes ">10^18 grams" of water | [PAL17] | **ENGINEERING-STUDIED** (parametric) | Ice figure is at the top of the Lawrence 2013 range (F5) |
| Mercury Lander (NASA PMCS 2020) | 9,410 kg wet; launch 2035, arrival 2045 via 1 Earth, 2 Venus, 5 Mercury flybys; one Mercury year on the surface on a 373 W RTG; cost about $1.5 billion without launch | [ML20] | **ENGINEERING-STUDIED** (concept maturity level 4) | Science lander, not a resource mission; the only detailed Mercury surface system design found |
| Mercury mass driver, Mercury industrialization or Mercury-based solar power satellites | No primary study found (two extended searches here, one in the sibling trucking file) | rows 88-90 | — | Popular articles and social posts only; one gave a wrong escape speed (rejected) |

### F10. Processing: what the surface can yield

The process energies (molten regolith electrolysis, carbothermal reduction, molten-salt electrolysis, aluminum by
chloride electrolysis) are in sibling `space_processing_and_fabrication.md` and are **not repeated**. What follows is what
changes at Mercury.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Yield per tonne of average regolith (elemental content, before losses) | Si ~250 kg; Mg ~110 kg (25 to 200 kg regionally); Al ~67 kg; Ca ~40-60 kg; Na ~29 kg; S ~19-23 kg (up to ~40); Fe **~13-19 kg**; C ~14 kg (up to ~50 in LRM); K ~1.3 kg; Cl ~1.4 kg; Ti ~3 kg; oxygen the balance (D1) | D1 from F1 | Derived | none | Medium (ratios from orbit; local grades unknown) |
| Iron as a product | About 1-2% of the rock, partly as sulfides (FeS) and possibly some metal grains; MESSENGER cannot say how much is metal (F1). Iron is a by-product at best | F1 | Primary-based | none | Medium |
| Carbon as a reductant | Graphite at ~1 wt% (to ~4-5 wt% in LRM) is an in-place carbon source; carbothermal reduction needs >= 1,650 C (sibling) | F1; sibling | Primary | none | Medium (no Mercury-specific process study found) |
| Vacuum and thermal processes | Vacuum pyrolysis vaporized ~10 g of lunar simulant completely at 1,400 C under vacuum; "vaporization of the oxides ... will occur at lower temperature for stronger vacuums" | [CAR07] | Primary (NASA GSFC) | Silicothermic magnesium reduction runs at ~1,200 C and ~100 Pa on Earth [LI23] | Medium |
| Magnesium | Mercury's surface is Mg-rich (F1). Terrestrial silicothermic (Pidgeon-family) reduction: CaO·MgO + FeSi75 at ~1,200 C and ~100 Pa; reducing-furnace energy ~1.0 (compound vertical retort) to ~1.6 tce per tonne Mg (Pidgeon), reduction stage only; about 8 to 13 kWh(th)/kg Mg if tce is taken as 29.3 GJ (D9) | [LI23] Tables 1, 5 | Primary (peer-reviewed) | none | Low-medium (terrestrial feed and reductant; conversion uses a conventional coal-equivalent factor) |
| Solar furnace concentration | 54x (perihelion) to 124x (aphelion) ideal concentration for 1,650 C vs 570x at 1 AU (F6, D5) | D5 | Derived | none | High (geometry) |
| High sulfur | S at 2-4 wt%, bonded to Fe, Cr, Ti, Mn, Mg and Ca (in that order of preference) in the normative calculation; "Due to the high amount of sulfur ... the CIPW normative mineralogy calculations could not be conducted in the conventional manner" | [VK16] | Primary | Mercury's surface O/Si deficit may reflect degassing "similar to industrial smelting" [NIT18] | Medium. **No processing study of high-sulfur regolith found** (Open threads) |
| High Na and K | Na ~3 wt%, K ~0.13 wt%; Na and K are lost from fine grains by diffusion at only ~400-475 K over long times (F1); any melt process at >1,400 C will drive off alkalis first (inference, not measured on Mercury material) | [NIT18] §2.3.1 | Primary for the diffusion data; inference for processing | none | Low (inference flagged) |

### F11. Hot-environment engineering

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Demonstrated high-temperature electronics | NASA Glenn 4H-SiC JFET-R integrated circuits: **over 1 year at 500 C in air**; 60 days at 460 C and 9.3 MPa in the Venus chamber; operation from -190 C to +812 C; 7 Mrad(Si) total dose and 86 MeV-cm^2/mg heavy ions; chips of 175 or more transistors (2018), a 7-fold step from 24-transistor ring oscillators (2016) | [NEU24]; [NEU18] | Primary (NASA) | each other | High (demonstrated, small-scale logic) |
| Flown practice: keep standard electronics cool | MESSENGER and the Mercury Lander design use sunshades (sunshade up to 325 C, tested at 355 C for ~432 h), diode heat pipes to radiators behind the shade, and standard electronics; the Lander body is held to a 30 C maximum, its RTG ~180-250 C; battery held at -5 to 0 C | [ERC06]; [ML20] §3.2.3 | Primary | [HOL15] | High |
| Solar-cell temperature limits | MESSENGER 150 C operating set point (275 C anomaly); BepiColombo about 230 C maximum tolerable; Mercury Lander arrays 165 C | F6 | Primary | — | High |
| Flat plate facing the Sun (equilibrium) | 710 K at perihelion and 576 K at aphelion for a black plate (absorptance/emittance = 1); to stay at ~300 K at perihelion a sun-facing surface needs absorptance/emittance of about **0.03** (0.07 at aphelion) (D11) | D11 | Derived | [LAN04]: ~450 C for a Mercury surface station | High (physics) |
| Radiator sink, equator by day | A vertical radiator seeing half sky and half 700 K ground has an effective sink of about **580 K (about 305 C)**, so it cannot reject heat at room temperature; ground infrared alone is ~12.7 kW/m^2 at 700 K (D11) | D11 from [HOL15] (emissivity 0.93, temperatures) | Derived | Mercury Lander orbit analysis: "the once very-cold space sink temperature (< -100 C) behind the sunshades varies from ~0-255 C" during passes over the hot planet [ML20] | High |
| Radiator sink, night side and polar shadow | ~90 K for night ground at 110 K; ~83 K beside 100 K shadowed ground (D11); permanently shadowed floors average ~100 K (F4) | D11; [PAI12] | Derived | none | High |
| Heat rejection capacity at room temperature | A 300 K surface with emittance 0.9 radiates ~413 W/m^2 to deep space (310 K: ~471 W/m^2) (D11) | D11 | Derived | none | High |
| Human-shaped machine (general constraint) | In equatorial daylight the machine sits between a sky source of 6,250-14,400 W/m^2 and ground radiating up to ~12.7 kW/m^2, against a rejection capacity of ~0.4-0.5 kW/m^2 at body temperature. **It cannot operate unshielded in equatorial daylight at body-normal temperatures**; it needs a sunshade, a cooled enclosure or high-temperature parts. At night or in polar shadow the sink is cold (~80-90 K) and the problem reverses to keeping warm | D11, F4 | Derived | Mercury Lander: operations end "shortly after sunrise" | High (physics) |

### F12. Operations: communication, flight heritage, landing studies

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| One-way light time Earth-Mercury | 5.1 to 11.5 min (circular orbits); about 4.3 to 12.3 min at the extremes of both orbits (D10) | D10 from [NSSDC-Me], [NSSDC-E] | Derived | MESSENGER impacted with Earth 1.316 AU away (~10.9 min) [MOE14] | High |
| Superior conjunction outage | Within 2 deg of the Sun for about **4.6 days** at each superior conjunction and ~2.0 days near inferior conjunction (when the Sun is behind the link only if Mercury is near a node), every 115.88 days (D10, circular coplanar) | D10 | Derived | BepiColombo radio science: the X-band link degrades below ~5-7 solar radii impact parameter (7 R_sun = 1.86 deg at 1 AU); 14-day observation arcs planned across each conjunction [DIS22]; MESSENGER planned its impact before "a solar conjunction in early April 2015" [MOE14] | Medium (real geometry, eccentricity and 7 deg inclination change the figures) |
| Landed-site Earth visibility | Mercury Lander at 40 S, 178 E: direct-to-Earth for the first **3 weeks**, then **6 weeks with no Earth contact**, then 4 weeks; landed downlink 15-55 kbps at Ka-band (32 GHz) from a 0.6 m antenna, 170-600 MB/day; autonomous operations through the gap | [ML20] §2.1 and Exhibit 31 | Primary | none | High (as a design) |
| Relay need | No relay was assumed by the Mercury Lander; the 6-week gap was accepted. A continuous link from one surface site therefore needs a relay orbiter or a site chosen for Earth visibility (inference) | [ML20] | Primary + inference | none | Medium |
| MESSENGER heritage | Launched 3 Aug 2004; orbit 18 Mar 2011; more than four years in orbit; impact 30 Apr 2015; cruise used six planetary flybys (sibling); periapsis maintained by OCMs | [HOL15]; [MOE14]; sibling trucking file | Primary | none | High |
| BepiColombo heritage | 7-year cruise (one Earth, two Venus and six Mercury flybys per [DIS22]; the sibling trucking file's 2014 trajectory option had five); arrays degrade under UV and heat (F6) | [DIS22]; [ESA11] | Primary | sibling trucking file | Medium |
| Landers on Mercury | **None has operated on Mercury.** Studies found: NASA PMCS Mercury Lander (2020, New Frontiers class, ~88 days on the surface, RTG, dusk landing, lunar-like terrain assumed); Palaszewski 2017 parametric crewed and robotic landers (3.5 km/s each way, 480 s Isp, polar targets) | [ML20]; [PAL17] | Primary | NASA: "the only inner planet unexplored by a lander" ([ML20] summary) | High |

### Source key

- **[NSSDC-Me]** NASA NSSDCA, Mercury Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html (last updated 11 Jan 2024). **[NSSDC-E]** Earth Fact Sheet (15 Nov 2024). **[NSSDC-Sun]** Sun Fact Sheet (9 May 2024). Primary.
- **[NIT18]** Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", in *Mercury: The View after MESSENGER* (Cambridge, 2018), arXiv 1712.02187 (Dec 2017). Primary (review chapter).
- **[NIT20]** Nittler, Frank, Weider et al., "Global Major-Element Maps of Mercury from Four Years of MESSENGER X-Ray Spectrometer Observations", Icarus (2020), doi 10.1016/j.icarus.2020.113716, arXiv 2003.00650. Primary.
- **[NIT11a]** Nittler et al., XRS results abstract, GSA Annual Meeting 2011, Paper 193666, https://gsa.confex.com/gsa/2011AM/webprogram/Paper193666.html. Primary (abstract of Science 333:1847).
- **[EV12]** Evans et al., "Major-element abundances on the surface of Mercury: Results from the MESSENGER Gamma-Ray Spectrometer", JGR Planets 117 (2012), doi 10.1029/2012JE004178; abstract at experts.arizona.edu. Primary.
- **[WEI14]** Weider, Nittler, Starr, McCoy, Solomon, "Variations in the abundance of iron on Mercury's surface from MESSENGER X-Ray Spectrometer observations", Icarus 235:170-186 (2014), abstract via cosmochemistry-papers.com (19 Mar 2014). Primary.
- **[WEI15]** Weider et al., "Evidence for geochemical terranes on Mercury: Global mapping of major elements with MESSENGER's X-Ray Spectrometer", EPSL (2015), abstract at profiles.wustl.edu. Primary.
- **[VK16]** Vander Kaaden, McCubbin, Nittler et al., "Mineralogy of the Mercurian Surface", LPSC 47 (2016) abstract 1476, NTRS 20160002643. Primary.
- **[TRA15]** Trang, Lucey, Izenberg, AGU Fall Meeting 2015 abstract (carbon by VIRS radiative transfer). **[TRA17]** Trang, Mercury space-weathering map product description, PDS Geosciences. Primary.
- **[CAR16]** Carnegie Science news, "Mercury's Mysterious 'Darkness' Revealed" (7 Mar 2016). Secondary (institutional release).
- **[GEN19]** Genova et al., "Geodetic Evidence That Mercury Has A Solid Inner Core", GRL 46:3625-3633 (2019), author manuscript via iris.uniroma1.it. Primary. **[AGU19]** AGU press release (secondary).
- **[BEU20]** Beuthe, Charlier, Namur, Rivoldini, Van Hoolst, "Mercury's crustal thickness correlates with lateral variations in mantle melt production", GRL 47 (2020), arXiv 2011.15066. Primary.
- **[WH17]** Wicht and Heyner, arXiv 1701.05060 (2017), via sibling `starlifting_physics_and_minimum_infrastructure.md`. **[AS13]** Armstrong and Sandberg (2013), via the same sibling.
- **[JOU26]** Joulaud, Allemand, Flahaut, Füri, "Regolith thickness across the Borealis Planitia region of Mercury", Planetary and Space Science 282, art. 106338 (Nov 2026), listing at crpg.univ-lorraine.fr. Primary.
- **[KRE15]** Kreslavsky and Head, "A Thicker Regolith on Mercury", LPSC 46 (2015) abstract 1246. Primary (abstract, preliminary).
- **[COS19]** Costello, Ghent, Lucey, "Impact Gardening on the Moon and Mercury ...", LPSC 50 (2019) abstract 1991. Primary (abstract).
- **[CIN92]** Cintala, "Impact-induced thermal effects in the lunar and mercurian regoliths", JGR (1992), abstract at EarthRef ERR 60235. Primary.
- **[POK18]** Pokorný, Sarantos, Janches, "A comprehensive model of the meteoroid environment around Mercury", ApJ (2018), arXiv 1807.02749. Primary.
- **[FRA22]** Frantseva, Nesvorný, Mueller et al., "Exogenous delivery of water to Mercury", Icarus (2022), arXiv 2204.11825. Primary.
- **[EKE17]** Eke, Lawrence, Teodoro, "How thick are Mercury's polar water ice deposits?", MNRAS (2017), arXiv 1611.05395. Primary.
- **[PAI12]** Paige, Siegler, Harmon et al., "Thermal Stability of Frozen Volatiles in the North Polar Region of Mercury", EPSC 2012-595. Primary (abstract of Science 339:300, 2013).
- **[DEU16]** Deutsch, Chabot, Mazarico et al., "Comparison of Areas in Shadow from Imaging and Altimetry in the North Polar Region of Mercury ...", NTRS 20160008397 (25 Jun 2016). Primary.
- **[NASA-PEL]** NASA image article, "There Is a Light that Never Goes Out (Almost)" (MESSENGER, 24 Dec 2011). Primary (agency).
- **[NASA-F]** NASA Science, "Mercury Facts" (page date 25 Apr 2025). Primary (agency, popular level).
- **[HOL15]** Holtzman, Begley, Ercol, "Return to Mercury: An Overview of the MESSENGER Spacecraft Thermal Environmental Predictions and Analysis Process", ICES-2015-307. Primary.
- **[ERC06]** Ercol, Dakermanji, Le, "The MESSENGER Spacecraft Power Subsystem Thermal Design and Early Mission Performance", AIAA 2006-4144. Primary.
- **[ESA09]** ESA, "Going solar for interplanetary missions" (27 May 2009). **[ESA11]** ESA, "Hot stuff: the making of BepiColombo, 6. A life in the Sun" (1 Jun 2011). **[ESA-BC]** ESA BepiColombo "Spacecraft" page (30 Mar 2020). Primary (agency).
- **[LAN04]** Landis, Raffaelle, Merritt, "High Temperature Solar Cell Development", 19th European PV Solar Energy Conference (2004), NTRS 20050198948. Primary (preprint).
- **[ML20]** Ernst et al. (APL), "Mercury Lander: Planetary Mission Concept Study for the 2023-2032 Decadal Survey", NASA PMCS final report (2020), science.nasa.gov PDF and arXiv 2107.06795. Primary.
- **[PAL17]** Palaszewski, "Solar System Exploration Augmented by In-Situ Resource Utilization: Human Planetary Base Issues for Mercury and Saturn", NTRS 20170001561 (13 Jan 2017). Primary.
- **[MOE14]** Moessner and McAdams, "The Final Two Years: MESSENGER's Trajectory from the Third Year in Orbit through Mercury Impact", ISSFD 24 (2014). Primary.
- **[LAR06]** Lario, Decker, Krimigis, Roelof, Aran, COSPAR 2006 abstract A-02607 (of ApJ 653:1531-1544). Primary.
- **[ROD24]** Rodríguez-García, EGU24-6213 abstract (2024). Primary (abstract).
- **[MIL20]** Milillo et al., "Investigating Mercury's Environment with the Two-Spacecraft BepiColombo Mission", Space Sci. Rev. 216:93 (2020), arXiv 2202.13243. Primary.
- **[LAV23]** Lavorenti et al., "Maps of solar wind plasma precipitation onto Mercury's surface: a geographical perspective", arXiv 2305.09498 (2023). Primary (preprint).
- **[MIY24]** Miyake et al., "Micro-scale electrostatic structures formed on the rough surfaces of the Moon", arXiv 2410.05913 (2024). Primary (preprint).
- **[MAR19]** Marquardt and Heber, "Galactic cosmic ray hydrogen spectra and radial gradients in the inner heliosphere measured by the HELIOS Experiment 6", A&A (2019), arXiv 1905.01052. Primary.
- **[NEU18]** Neudeck et al., "Yearlong 500 C Operational Demonstration of Up-Scaled 4H-SiC JFET Integrated Circuits", NTRS 20180003391 (2018). **[NEU24]** Neudeck, "Progress Towards SiC ASICs for Extreme Temperature and Radiation Environments", NTRS 20240013278 (2024). Primary.
- **[DIS22]** di Stefano, Cappuccio, Iess, "The BepiColombo Solar Conjunction Experiments Revisited", arXiv 2201.05107. Primary (preprint).
- **[CAR07]** Cardiff et al., "Vacuum Pyrolysis and Related ISRU Techniques", NTRS 20070014929. Primary.
- **[LI23]** Li, Zhang, Yang, Liu, Liu, "Research, development and application of compound-vertical-retort technology for magnesium production", J. Magnesium and Alloys 11:4724-4736 (2023). Primary.
- **[WRI20]** Wright, "Dyson Spheres", Serbian Astronomical Journal 200 (2020), arXiv 2006.16734. Primary (review).
- **[HOW18]** Howe, "A Tether-Assisted Space Launch System for Super-Earths", arXiv 1805.06438 (2018, physics.pop-ph). Preprint, low weight.
- **[MAT17]** Maturilli, Helbert, Varatharajan, D'Amore, EPSC 2017-610. Primary (abstract).
- **[BUT04]** Butler, Campbell, de Pater, Gary, "Solar System Science with SKA", arXiv astro-ph/0409220 (2004). Primary (review).

## 4. Conflicts

- **K1. Surface iron: XRS vs GRS.** XRS average Fe/Si 0.053 (sigma 0.013, later normalized to 0.06) vs GRS 0.077 +/- 0.013
  ([NIT18] Table 2.1, [NIT20]). Why: XRS samples micrometers and is subject to a "mineral mixing" effect that can change
  the Fe/Si photon ratio by up to five times if iron sits in grains larger than tens of micrometers; the XRS map was
  normalized arbitrarily; the GRS samples tens of centimeters and averages the northern hemisphere only. Both put total
  Fe near 1.3-1.9 wt%. Early XRS gave an upper bound "less than ~4 wt%" ([NIT11a]).
- **K2. Moment of inertia.** NSSDC lists 0.35; MESSENGER-era geodesy gives 0.333 +/- 0.005 ([GEN19]). The fact sheet
  value predates the MESSENGER solution.
- **K3. Crust under the high-Mg region.** Weider 2015: "relatively thin crust", possibly an ancient basin; Beuthe 2020:
  the thickest crust on the planet (50 +/- 12 km), "refuting the hypothesis of an impact origin". Different crustal
  density assumptions: Beuthe lets density vary laterally with surface composition.
- **K4. Solar intensity at Mercury.** Holtzman: 4.7 to 11.1 Earth solar constants (from 0.46 and 0.30 AU, rounded);
  D4 from NSSDC distances: 4.6 to 10.6 times 1,361 W/m^2; Landis: "10.6 times AM0"; ESA: "ten times". Rounding of the
  perihelion distance (0.3075 AU true) explains the spread.
- **K5. Regolith thickness.** Kreslavsky and Head 2015: weak layer 20-90 m, "~25-40 m" in smooth plains (preliminary,
  images better than 14 m/pixel); Joulaud et al. 2026: median 4.6 m (smooth plains) and 3.7 m (intercrater plains)
  from 3,546 craters plus bowl-shaped craters. Possible causes: resolution (Kreslavsky themselves warn that melt pools
  can mimic flat floors at MDIS resolution), region and sample size. The newer, larger survey gives the lower values.
- **K6. Impact flux relative to the Moon.** Cintala 1992: micrometeoroid impact rate 5.5 times the Moon's at >60%
  higher speed; Kreslavsky 2015: micrometeorite bombardment "orders of magnitude more intensive"; Costello 2019 (using
  Marchi): flux of 1 cm-100 m impactors "about ten times lower on Mercury", so meter-scale gardening is slower. These
  refer to different size ranges and are not necessarily contradictory: dust-scale impacts may be more intense while
  centimeter-to-hundred-meter impacts are rarer.
- **K7. Total dust mass influx.** Borin et al. 2017 1.97 x 10^8 kg/yr vs Pokorný et al. 2018 4.4 x 10^6 kg/yr vs
  Frantseva 2022 ~6 x 10^6 kg/yr ([FRA22], [POK18]). Different size ranges (5-100 µm vs 10-2,000 µm) and calibration
  (Pokorný calibrates to Earth's measured influx).
- **K8. Night temperature.** -163 C (110 K) in the MESSENGER thermal paper vs "as low as -180 C" (93 K) on the NASA
  facts page. Likely different locations or times (warm-pole pre-dawn minimum vs a nightside average).
- **K9. Polar ice mass.** Lawrence 2013 (via [FRA22]): 2.1 x 10^13 to 1.4 x 10^15 kg; Moses 1999: 4 x 10^13 to
  8 x 10^14 kg; Eke 2017 upper limit ~3 x 10^15 kg; Palaszewski 2017 quotes "over 10^18 grams" (10^15 kg). All hinge
  on the unknown thickness (0.5-20 m assumed; Eke measures ~50 +/- 35 m excess height at only ~1.5 sigma).
- **K10. Outer core radius.** 2,020 +/- 30 km (Hauck 2013), 2,004 +/- 39 km (Rivoldini and Van Hoolst 2013),
  1,985 +/- 39 and 1,967 +/- 23 km (Genova 2019). Genova uses a newer obliquity from gravity tracking rather than
  surface features.
- **K11. Normative mineralogy text vs table** ([VK16]): the text gives hypersthene and diopside up to 37.13 wt% while
  the table's maxima are 31.91 and 22.43. Probably an error in the abstract's text; the table is used here.
- **K13. MESSENGER impact date.** The 2014 trajectory paper predicted impact "on or about 28 March 2015" ([MOE14]); the
  2015 thermal paper reports impact on 30 Apr 2015 ([HOL15]). The later paper reports the event; the earlier was a
  forecast (the reason for the extension was not in the pages read).
- **K12. Mercury's escape speed in popular sources.** 4.5 km/s in one article (rejected) vs 4.3 (NSSDC) and 4.25
  computed.

## 5. Derived figures

All inputs are from sources in section 3; Python run locally (log rows 87, 102, 108, 117).

- **D1. Weight percent from ratios.** Si = 1.5 wt% / 0.06 = 25 wt% (from [WEI14]). Then Mg = 0.436 x 25 = 10.9;
  Al = 0.268 x 25 = 6.7; S = 0.076 x 25 = 1.9 (XRS) or 0.092 x 25 = 2.3 (GRS); Ca = 0.165 x 25 = 4.1 (XRS) or
  0.24 x 25 = 6.0 (GRS); Ti = 0.3; Fe = 1.3 (XRS) or 1.9 (GRS); Na = 0.12 x 25 = 3.0 (GRS direct 2.9); Cl = 0.14 wt%.
  Mg range 0.1-0.8 x 25 = 2.5-20 wt%. Per tonne: multiply wt% by 10 kg.
- **D2. Depth to the core and core mass.** Depth = 2,439.7 - r_core = 420 (2,020 km), 436 (2,004), 455 (1,985),
  473 km (1,967). Core volume fraction (r/R)^3 = 0.52-0.57. Core mass (4/3) pi r^3 rho: 2,020 km at 6,980 kg/m^3 =
  2.41 x 10^23 kg (73%); 1,985 km at 6,980 = 2.29 x 10^23 kg (69%); at 7,233 = 2.37 x 10^23 kg (72%) of 3.3010 x 10^23 kg.
- **D3. Day length.** Sidereal rotation 1,407.6 h = 58.65 d; 3 x 58.65 = 175.95 d = 2 x 87.969 d (3:2 resonance);
  solar day 4,222.6 h = 175.94 d; half = 87.97 d of daylight then darkness at a point on the equator.
- **D4. Irradiance.** S(r) = 9,082.7 x (57.909 / r)^2: perihelion r = 46.000 x 10^6 km gives 14,394 W/m^2; aphelion
  69.818 gives 6,248 W/m^2; orbit-time average S_a / sqrt(1 - e^2) = 9,281 W/m^2 (e = 0.2056). Ratio to 1,361.0 W/m^2:
  10.58 and 4.59. Check from luminosity: L / (4 pi r^2) with L = 3.828 x 10^26 W gives 14,396 and 6,249 W/m^2.
  Radiative equilibrium of a black subsolar surface (sigma T^4 = S): 710 K (perihelion), 576 K (aphelion).
- **D5. Concentration and PV bounds.** Ideal stagnation concentration C = sigma T^4 / S: for 1,923 K, C = 54
  (perihelion), 85 (mean), 124 (aphelion), 570 (1 AU); for 1,673 K: 31 / 49 / 71 / 326; for 2,273 K: 105 / 167 / 242 /
  1,112. Maximum concentration 1 / sin^2(R_sun / d): 4,372 (perihelion), 6,929 (mean), 10,071 (aphelion), 46,239
  (1 AU); C_max x S = sigma x 5,772^4 = 6.29 x 10^7 W/m^2 at every distance. PV output bound = S x efficiency:
  20% gives 2,879 (perihelion) and 1,250 (aphelion) W/m^2; 28% gives 4,030 and 1,749 W/m^2.
- **D6. Night storage.** Equator: 87.97 d x 24 h = 2,111 kWh per kW of continuous load. Best polar point: 18% of
  175.94 d = 31.7 d, 760 kWh per kW if contiguous.
- **D7. SEP scaling.** Factor relative to 1 AU = r^-n. r = 0.31 AU: n = 2.5 gives 18.7; 1.6 gives 6.5; 1.9 gives 9.3;
  0.9 gives 2.9; 3.0 (old guideline) gives 33.6. r = 0.47 AU: 6.6, 3.4, 4.2, 2.0, 9.6.
- **D8. Launch from the surface.** v_esc = sqrt(2 x 22,031.86 / 2,439.7) = 4.250 km/s; surface circular speed 3.005 km/s;
  equatorial rotation 2 pi x 2,440.5 km / 1,407.6 h = 3.03 m/s. Hohmann departure v-infinity at Mercury
  (GM_sun 1.32712440041 x 10^20 m^3/s^2, Mercury at 57.909 x 10^6 km): Venus (108.210 x 10^6 km) 6.77 km/s, 76 d;
  Earth (149.598) 9.61 km/s, 105 d; Mars (227.956) 12.58 km/s, 171 d. Surface launch speed sqrt(v_esc^2 + v_inf^2):
  7.99 / 10.51 / 13.28 km/s; kinetic energy 31.9 / 55.2 / 88.2 MJ/kg (escape alone 9.03). Accelerating length v^2 / (2a)
  at 1,000 g (9,806.65 m/s^2): 0.92 / 3.26 / 5.63 / 8.99 km (escape / Venus / Earth / Mars) vs 0.29 km for the lunar
  2.4 km/s. Muzzle power at 42 kg/s and 96.4% efficiency: 393 / 1,392 / 2,405 / 3,841 MW. Average power for 1 Mt/yr:
  297 / 1,050 / 1,815 / 2,898 MW. Asymptote turn from the launch direction (hyperbola from the surface,
  e = 1 + R v_inf^2 / GM; turn = arccos(-1/e) - 90 deg): 9.5 deg (Venus), 5.1 (Earth), 3.1 (Mars). Cross-check with the
  sibling trucking table: from a 200 km orbit, sqrt(9.61^2 + 4.086^2) - 2.889 = 7.55 km/s, matching its "Depart" column.
- **D9. Magnesium energy conversion.** 1.0-1.6 tce/t Mg x 29.3 GJ/tce (Chinese standard coal equivalent, 7,000 kcal/kg;
  a conventional factor, not from [LI23]) = 29-47 GJ/t = 8.1-13 kWh(th)/kg, reduction stage only.
- **D10. Communication geometry.** Circular coplanar orbits, 200,000 steps over one synodic period (115.88 d): Earth-
  Mercury distance 0.613-1.387 AU, one-way light time 5.1-11.5 min (c = 299,792,458 m/s, AU = 149,597,870,700 m);
  extremes from the fact sheets: (147.095 - 69.818) x 10^6 km = 0.517 AU (4.3 min) to (152.100 + 69.818) x 10^6 km =
  1.483 AU (12.3 min). Sun-Mercury angle under 2 deg: 4.6 d near superior conjunction, 2.0 d near inferior conjunction
  (in reality inferior conjunction clears the Sun except near the nodes because of the 7 deg inclination). Maximum
  elongation (circular) 22.8 deg. 7 solar radii at 1 AU = 7 x 695,700 / 1.496 x 10^8 rad = 1.86 deg.
- **D11. Thermal balances.** Flat plate, sun-facing, insulated back: T = (alpha/epsilon x S / sigma)^(1/4): 710 / 525 /
  399 / 295 K at perihelion for alpha/epsilon = 1 / 0.3 / 0.1 / 0.03; 576 / 426 / 324 / 240 K at aphelion. Required
  alpha/epsilon for 300 K: 0.032 (perihelion), 0.074 (aphelion). Rejection at 300 K, epsilon 0.9: 413 W/m^2 (310 K: 471).
  Ground IR at 700 K, epsilon 0.93: 12.7 kW/m^2. Vertical radiator sink (half sky, half ground of emissivity 0.93):
  (0.5 x 0.93 x T_g^4)^(1/4) = 578 K (700 K ground), 475 K (575 K), 363 K (440 K), 91 K (110 K), 83 K (100 K).
- **D12. Meteoroid influx per area.** Mercury 12.16 t/day over radius 2,439.7 km vs Earth 43.3 t/day (3.7 + 34.6 + 5.0,
  as quoted by [POK18]) over 6,371.0 km: ratio (12.16 / 2,439.7^2) / (43.3 / 6,371.0^2) = 1.9.

## 6. Constraints for any inhabitant

- **The surface is not an iron ore.** Average rock holds about 13-19 kg of iron per tonne, partly as sulfide, possibly
  some as fine metal, none confirmed as free iron-nickel (F1). Any iron-dependent industry on Mercury must either process
  very large tonnages for by-product iron or reach the core, which lies 420-470 km down (F2). What the surface offers in
  quantity is oxygen, silicon, magnesium, aluminum, calcium, sulfur, sodium and some carbon (F10).
- **Equatorial sites see about 88 days of continuous day at up to ~700 K and 88 days of night near 100-110 K** (F4).
  Solar power stops for the whole night: about 2,100 kWh of storage per kW of load, or a polar site, or a non-solar
  source (F6). The only detailed surface design found uses an RTG and does not survive sunrise (F6, F12).
- **Polar sites are the most benign:** cold traps near 100 K annual average with water ice beneath ~10 cm of dark
  material; the best-lit polar point is lit about 82% of the solar day, and no peak of eternal light is known (F4, F5).
  Ice mass is uncertain by about 100 times (2 x 10^13 to 3 x 10^15 kg).
- **Heat rejection is the governing problem by day.** A room-temperature surface facing the Sun needs
  absorptance/emittance near 0.03; a radiator beside sunlit ground has a ~580 K sink. Shade, polar siting, night-side
  operation or high-temperature parts (SiC electronics demonstrated at 500 C) are required (F11).
- **Solar arrays must run hot and off-normal.** Flown and designed arrays cap cells at 150-230 C by tilt and mirrors and
  still lose power to UV-plus-heat degradation (20% in a simulated month in BepiColombo testing) (F6).
- **Radiation:** SEP peak intensities typically several to ~19 times those at 1 AU; the magnetic field blocks low-energy
  protons only near the equator and gives no protection above tens of MeV; GCR intensity is about Earth's (F7).
- **Impacts and dust:** dust-scale impacts are more frequent and faster than at the Moon; meter-scale gardening is
  slower; regolith depth is disputed (4-40 m) (F3).
- **Launch is energetic.** Escape needs 9.0 MJ/kg; a direct surface launch onto an Earth-bound Hohmann transfer needs
  10.5 km/s and 55 MJ/kg, about 19 times the lunar launcher's energy per kg. A fixed launcher can only fire when its
  track is correctly oriented relative to the Sun, which on Mercury's slowly rotating surface recurs once per 176-day
  solar day, while windows to Earth recur every 116 days (F8).
- **Communications:** 4-12 minutes one way; a few days near each superior conjunction every 116 days with a degraded or
  lost link; a fixed surface site can lose Earth for weeks (6 weeks in the Lander design) unless relayed (F12).
- **Low orbits drift.** Solar gravity lowered MESSENGER's periapsis by hundreds of km over months; orbit maintenance is a
  standing propellant cost (F8).
- **A human-shaped machine** cannot work unshielded in equatorial daylight; in shadow or at night it must hold heat in
  against an 80-110 K environment (F11).

## 7. Candidate handwaves

Flagged, not accepted. The developer decides.

- **HW-1. Mercury as an iron source from surface mining.** Requires either a free-metal grade nobody has measured or
  access to a core 420-470 km down. No physics forbids by-product iron from very large tonnages; nothing found supports a
  rich surface iron ore.
- **HW-2. Multi-gigawatt, 10 km/s surface mass drivers.** The lunar point design reaches 2.4 km/s on paper. Mercury
  needs 4.25 km/s just to escape and 8-13 km/s for direct transfers; scaling to several kilometers of track and GW-class
  pulsed power is linear arithmetic, but no design, test or study at these speeds was found.
- **HW-3. Continuous solar power on the surface.** No peak of eternal light is known; equatorial nights last 88 days.
  Any design with uninterrupted solar power needs either a polar site with storage for the dark fraction or power beamed
  from orbit (not studied here).
- **HW-4. Room-temperature machines in equatorial daylight.** Needs absorptance/emittance near 0.03 on every
  sun-facing surface and protection from 12.7 kW/m^2 of ground infrared; not demonstrated for a mobile machine.
- **HW-5. Surface-skimming rotating tethers at Mercury.** Tip speed ~3 km/s is at the edge of untapered aramid's
  characteristic speed; escape needs 4.25 km/s. Only a pop-physics preprint was found.
- **HW-6. Whole-planet disassembly in decades.** Exploratory-engineering result built on exponential self-replication
  and a 70% metal bulk; its authors call it unlikely to be attempted.

## 8. Open threads

- **Free-metal content of the regolith.** Not measured; BepiColombo MIXS and a landed XRD (>1 wt% detection) are the
  routes. Next search: McCubbin et al. 2017 (JGR) on Si-rich metal; BepiColombo MIXS first results.
- **Regolith bulk density, grain size, strength, thermal inertia.** Mitchell and de Pater 1994 (Icarus 110:2-32) and
  Vasavada et al. 1999 (Icarus 141:179) could not be opened (403/404). Next: BepiColombo MERTIS first results; Bauch et
  al. 2021 (Icarus, surface temperatures for MERTIS).
- **North-pole maximum illumination fraction.** Not found; Hamill et al. 2020 (PSJ 1:57) located but the PDF was dead.
- **Radiation dose at Mercury and on its surface.** No dose rate found. BERM (Pinto et al. 2022, Space Sci. Rev.)
  located but no dose number seen; MESSENGER design dose requirement not found.
- **BepiColombo MPO array design limits** (nominal and survival cell temperatures, power, test degradation): seen only in a
  search summary of E3S/DOAJ pages that returned 403. Next: ESA ESPC proceedings mirror, or Airbus papers.
- **Processing of high-sulfur, high-alkali regolith.** No study found. Next: molten oxide electrolysis and sulfur;
  vacuum pyrolysis volatility series for Na and K; McCubbin 2017 smelting hypothesis.
- **Electrolytic magnesium from silicate feed, energy per kg.** Only a terrestrial silicothermic figure in coal
  equivalent was found.
- **Mercury mass driver / launch loop / Mercury industrialization studies.** None found in three extended searches here
  and in the sibling. Next: Criswell 1986 (planet deconstruction), Ehricke's Mercury studies (AIAA 67-28, cited by
  [PAL17]), JBIS archives.
- **Low circular orbit lifetime at Mercury.** Only MESSENGER's eccentric-orbit decay found. Next: frozen-orbit studies
  for BepiColombo MPO (480 x 1,500 km) such as the Zaragoza averaged-model paper (located, not read).
- **Exact conjunction durations** with Mercury's real orbit (eccentricity and inclination); D10 is a circular model.
- **Sources found but not read:** Peplowski et al. 2016 (Nature Geoscience, carbon) full text; Lawrence et al. 2013
  (Science, ice) full text; Chabot et al. 2018 polar deposits chapter; BERM paper; Hamill 2020; Zaragoza Mercury orbit
  paper (zaguan.unizar.es record 130420); NTRS 20120010094 (polar, not opened).

## 9. Rejected sources

- **Popular article (search row 88)** giving Mercury's escape velocity as 4.5 km/s: contradicts NSSDC (4.3) and the
  computed 4.25 km/s.
- **Social-media post and blog pages on Mercury mass drivers** (row 88): no numbers traceable to a primary source.
- **Search-engine summaries with unopened numbers** (rows 29, 43, 70, 94, 106, 118): their figures (a warm-pole pre-dawn
  minimum, a 1 m subsurface temperature, a microwave regolith density, BepiColombo cell limits, a Spectra tether speed, a
  MESSENGER cruise conjunction length, a sulfur maximum, basin fill thicknesses) were not used because no page carrying
  them was opened.
- **SPENVIS "8312_MESSENGER.pdf"** (row 115): about solar-cell radiation testing by an author named Messenger, not the
  MESSENGER mission.
- **Kola borehole figures** (row 30): Wikipedia-class search summary only; removed from the findings.
- **EPSC 2017-610** (row 46): laboratory emissivity work; only a grain-size assumption was taken from it.
- **Wright 2020 for Mercury-specific numbers** (row 97): the review contains none; the search summary's Mercury sentence
  is not in the text.
