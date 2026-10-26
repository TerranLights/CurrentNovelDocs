# Oxygen and hydrogen supply for making water at Mars (Mercury/Venus oxygen, solar hydrogen, and the alternatives)

## 1. Scope

The chain "oxygen from Mercury or Venus + hydrogen from the Sun, shipped to Mars and combined into water", link by link, against
its alternatives: oxygen from the Moon, asteroids, Phobos and Deimos and Mars itself; hydrogen from the solar wind, the photosphere,
coronal mass ejections, the giant planets, comets, Ceres, polar ices and Mars's own water. Physics, chemistry and transport only.

## 2. SEARCH LOG

All dates 2026-10-11 unless stated. Marks: useful / thin / dead (at the query or at the sources) / not used. Rows marked
"sibling" are read-only reads of sibling files allowed by the dispatch; they are cited, not re-researched.

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| 1 | Sibling read: `_BRIEF.md`, `starlifting_synthesis.md`, `inner_system_mining_synthesis.md` (full) | useful | Prior answers: Sun as material source 1.2 x 10^7 times Mercury's lift cost per t Fe; solar-wind area tables; Genesis 0.2 mg H/yr on 1.67 m^2 |
| 2 | Sibling read: `mercury_as_industrial_site.md` F1, F2, F5, F6, F8, F9, F10, D1 to D11 | useful | Surface element ratios (O/Si 1.2 GRS, "oxygen the balance"), polar ice 2.1 x 10^13 to 3 x 10^15 kg, launch energies, Palaszewski Mercury ice-hydrogen study |
| 3 | Sibling read: `venus_as_extraction_site.md` 3.1 to 3.3, 3.7, D2 | useful | Element inventory O 3.4 x 10^20 kg; MOXIE and SOE plant (5.7 kWh/kg, floor 4.91); 9 km/s ascent; Mars polar water 2.3 to 3.2 x 10^18 kg (Plaut 2007) |
| 4 | Sibling read: `mars_venus_and_transfer.md` 3.1, 3.4 to 3.6, 3.11 | useful | Mars atmosphere composition; perchlorate 0.4 to 0.6 wt%; soil water 1.5 to 3 wt%; Phobos/Deimos orbits; Earth-Mars transfer |
| 5 | Sibling read: `moon_lagrange_and_comparables.md` A4 to A6 | useful | Lunar minerals 30 to 45 wt% O (RP-1057); 2 to 4 MW-yr per 1,000 t O2; polar ice estimates |
| 6 | Sibling read: `belt_jupiter_saturn_and_deep_transit.md` 3A to 3C | useful | Belt mass, water in C-types, Ceres up to 25% water, Jupiter/Saturn escape 59.5 / 35.5 km/s |
| 7 | Sibling read: `space_processing_and_fabrication.md` 1a, 5, 7 | useful | MRE 104 to 135 kWh/kg O2 demonstrated, 114 design; H2 reduction 24.3 kWh/kg LOX; carbothermal; ISS OGA 7.75 kWh/kg O2; CM water release below 600 C |
| 8 | Sibling read: `space_trucking_and_transport_infrastructure.md` F1 to F7 and D1 | useful | Delta-v table incl. low Mercury orbit to Mars 10.34 / 16.94 km/s, Venus cloud deck to Mars 11.82 / 15.19, belt to Mars 1.91 to 3.28; tug 0.279 t/kW/yr; KSC LH2 boil-off 0.09 to 0.10%/day; no in-orbit rate |
| 9 | Sibling read: `inner_system_logistics_network.md` F1, F9 | useful | Mercury-Mars synodic 100.89 d; Mars Molniya orbital CO2 scoop (NIAC): 34.9 t CO2, about 7 t O2 over 81 passes |
| 10 | Opened (local copy fetched earlier this session, pdftotext): Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", chapter 2 of *Mercury: The View after MESSENGER* (Cambridge, 2018), author preprint | useful | Sec. 2.3.3: O "typically 40-50 wt%" of silicate rock; GRS O/Si 1.4 (Evans 2012), refined 1.2 +/- 0.1 (McCubbin 2017) vs ~1.7 stoichiometric; Table 2.2 mantle oxide compositions; Sec. 2.6 bulk model (core 2,020 km, 6,980 kg/m^3; shell 3,380 kg/m^3) |
| 11 | Opened: NIST Chemistry WebBook, Thermophysical Properties of Fluid Systems, saturation tables (Type=SatP) for hydrogen (C1333740), oxygen (C7782447), methane (C74828), ammonia (C7664417), water (C7732185), https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=<id>&Type=SatP ... (TSV) | useful | Interpolated at 1 atm (calc/nbp.py): H2 20.37 K, 70.85 kg/m^3, Hvap 448.7 kJ/kg; O2 90.19 K, 1,141 kg/m^3, 213.1 kJ/kg; CH4 111.67 K, 422.4; NH3 239.83 K, 681.6; triple and critical points |
| 12 | Same NIST query for hydrazine (C302012) | dead at the sources | "Query Error": hydrazine is not in the WebBook fluid database |
| 13 | `Nittler Chabot Grove Peplowski "The Chemical Composition of Mercury" arXiv` | useful | Identifies the chapter preprint as arXiv:1712.02187 (the copy in row 10) |
| 14 | `solar wind helium abundance He/H ratio by number slow fast wind average 4% Wind SWE Kasper` | useful | Leads to Kasper et al. 2007; ar5iv 1906.12273 (Alterman), arXiv 1204.2776 (not opened) |
| 15 | WebFetch: Kasper et al. 2007 PDF at lweb.cfa.harvard.edu | dead at the sources | "certificate has expired"; re-fetched with curl -k (row 16) |
| 16 | Opened (curl -k, pdftotext): Kasper, Stevens, Lazarus, Steinberg, Ogilvie, "Solar wind helium abundance as a function of speed and heliographic latitude: variation through a solar cycle", ApJ 660:901-910 (2007) | useful | A_He = 100 n_He/n_H "rarely exceeds 5" in steady wind; about 4.5 in fast wind; photosphere and convection zone about 8; CMEs "A_He > 20" reported; A_He zero at 259 +/- 12 km/s; Wind 1995-2005 |
| 17 | `solar wind average proton density 1 AU speed long-term OMNI statistics mass flux per square meter cm-3 km/s table` | thin | Summary gave OMNI means (5.94 cm^-3, 432 km/s; 6.8 cm^-3, 436 km/s) traced to no opened page; not used |
| 18 | WebFetch: arXiv abs 1112.2967 (Bzowski et al. 2011, ISSI SR-012 ch. 2) | thin | Abstract has no numbers |
| 19 | Opened (curl, pdftotext): arXiv 1112.2967 full text, grep for OMNI averages | dead at the sources | Text is about Lyman-alpha and ionization; only "typical solar wind speed ~440 km/s" (not used as a flux) |
| 20 | `solar wind proton flux 1 AU "cm-2 s-1" average nv 2-4 x 10^8 Ulysses mass loss rate Sun 10^9 kg/s latitude` | useful (leads) | Cohen 2011 (arXiv 1107.2275); Mishra et al. 2019 (arXiv 1904.09898); Ulysses polar proton flux 1.9 to 2.2 x 10^8 cm^-2 s^-1 in summary only (not used) |
| 21 | WebFetch: arXiv abs 1904.09898 (Mishra et al., MNRAS 2019) | thin | Abstract: wind mass loss "an order of magnitude more than" CME loss; no numbers |
| 22 | WebFetch: arXiv abs 1107.2275 (O. Cohen 2011) | useful | Solar mass-loss rate "scattered around an average value of 2 x 10^-14 M_sun/yr" |
| 23 | Opened (curl, pdftotext): Mishra, Srivastava, Wang, Mirtoshev, Zhang, Liu, "Mass loss via solar wind and coronal mass ejections during solar cycle 23 and 24", MNRAS (2019), arXiv 1904.09898 | useful | Wind loss 2.1 x 10^-14 M_sun/yr (cycle 23), about 10% lower in cycle 24; average 3.5 x 10^18 g/month; CME loss peak 3.5 x 10^17 g/month (all latitudes, cycle 23), 2.7 x 10^17 (cycle 24); CMEs about 5% of ecliptic wind mass flux at maximum, negligible at minimum |
| 24 | `Vourlidas 2010 CME mass distribution LASCO average CME mass 10^15 g range 10^13 to 10^16 g` | useful (leads) | arXiv 1008.3737; "average 1.6 x 10^15 g" appeared in a summary only (from arXiv 1407.4258, not opened; not used) |
| 25 | WebFetch: arXiv abs 1008.3737 | thin | Abstract without numbers |
| 26 | Opened (curl, pdftotext): Vourlidas, Howard, Esfandiari, Patsourakos, Yashiro, Michalek, "Comprehensive analysis of coronal mass ejection mass and energy properties over a full solar cycle", ApJ (2010), arXiv 1008.3737 | useful | 7,668 CMEs (widths 20 to 120 deg), 1996-2009; masses 10^11 to 10^17 g; Table 2: 3.4 x 10^14 g histogram peak, 3.9 x 10^14 and 1.1 x 10^15 g in the next two columns (labels "Average", "Median" as extracted); total 9.2 x 10^18 g; mass flux 1.8 x 10^15 g/day (2.6 x 10^15 in 1996-2003, 8.3 x 10^14 in 2003-2009) |
| 27 | `Genesis mission solar wind collector total mass collected micrograms hydrogen helium fluence 27 months bulk array area` | useful (leads) | JPL press kit; Wikipedia and fandom (secondary, not used) |
| 28 | Opened (curl, pdftotext): NASA/JPL, "Genesis Launch Press Kit", July 2001, https://www.jpl.nasa.gov/news/press_kits/genesislaunch.pdf | useful | Goal "10 to 20 micrograms" of solar wind in total; spacecraft 636 kg (capsule 210 kg); halo orbit 30 months, collection to April 2004; passive collector tiles of Si, sapphire, diamond, gold |
| 29 | `capturing solar wind ions magnetic scoop collect hydrogen propellant feasibility study capture fraction plasma collector` (extended) | dead at the sources | Game forums, fandom wiki, Wikipedia (Bussard ramjet), patents; no engineering study of capturing and storing solar-wind hydrogen |
| 30 | `"solar wind" harvesting hydrogen collection spacecraft concept NIAC OR NTRS "collect" protons neutralize store propellant in-space resource` | thin | Genesis pages again; SWIFT (Gemmer and Mazzoleni, IAC-14/IAC-15); lunar-ISRU volatile-loss abstract (NTRS 20070014073, not opened); no collector-and-store design |
| 31 | WebFetch: IAF directory, Gemmer and Mazzoleni (NC State), "Introduction and Performance Analysis of the Solar Wind Ion Focusing Thruster (SWIFT)", IAC-14,C4,8 (2014), abstract | useful | "a cone diameter of 1 km could generate thrust on the order of 2 mN at 1 AU"; exhaust "~1000 km/s"; the focused protons are thrown out as thrust, not stored |
| 32 | `star lifting Criswell 1985 "star lifting" hydrogen extraction from the Sun energy requirement thermally driven magnetic field ring current` | thin | Wikipedia (secondary) states "1.6 x 10^13 J/kg" to lift solar material to Mercury, 85 times the escape energy GM/R = 1.91 x 10^11 J/kg (rejected, see section 9); Lazarus Stars (arXiv 2210.02338) and Criswell are already in sibling starlifting files; no engineering design of lifting found |
| 33 | `Mars average soil composition APXS oxide weight percent SiO2 FeO SO3 Cl Gale Gusev Meridiani "average Mars soil" table` | useful (leads) | PMC5815393; NASA PIA16572; NTRS 20080026156 (not opened) |
| 34 | WebFetch: PMC5815393 (two passes) | thin | Summarizer could not find the tables and misnamed the article; replaced by direct download (row 35) |
| 35 | Opened (curl, parsed HTML tables): Ehlmann et al., "Chemistry, mineralogy, and grain properties at Namib and High dunes, Bagnold dune field, Gale crater, Mars: a synthesis of Curiosity rover observations", JGR Planets 122, 2510-2543 (2017), PMC5815393 | useful | APXS oxide tables: Gusev average soil (SiO2 46.1, FeO 16.3, SO3 5.78, Cl 0.70 wt%...), Meridiani average soil (45.7, 18.8, 5.83, 0.65), Rocknest Portage (43.0, 19.2, SO3 5.5); "Estimated Mars crust (volatile free)" SiO2 49.30, FeO 18.20; all Gale fines average |
| 36 | `Apollo lunar soil average chemical composition table oxide wt% mare highland Apollo 11 12 14 15 16 17 SiO2 FeO TiO2 Al2O3 Lunar Sourcebook` | thin | Summary quoted Lunar Sourcebook highland / high-Ti / low-Ti mare oxides from arXiv 2609.06496 (not opened; not used) |
| 37 | WebFetch: R. L. Korotev, "The chemical composition of lunar soil", Washington University in St. Louis meteorite site | useful | "Oxygen (41-45%)" is the most abundant element in lunar soil; data otherwise in figures |
| 38 | `ordinary chondrite H L LL bulk composition oxygen weight percent table Wasson Kallemeyn 1988 O 35.7 wt% Si Fe Mg` | useful (leads) | Summary gave O 35.7 / 37.7 / 38.3 wt% for H / L / LL (Wasson and Kallemeyn 1988) without an opened page; used only as a cross-check against row 39 |
| 39 | Opened (curl, pdftotext): Schaefer and Fegley, "Outgassing of ordinary chondritic material and some of its implications for the chemistry of asteroids, planets, and satellites", Icarus (2007), arXiv astro-ph/0606671, Table 1 | useful | Average falls (90 / 123 / 29 analyses) H / L / LL: SiO2 36.49 / 39.66 / 40.48; MgO 23.41 / 24.84 / 25.32; FeO 9.54 / 14.14 / 17.44; metal 16.72 / 7.27 / 2.64; FeS 5.33 / 5.99 / 5.87; H2O+ 0.32 / 0.34 / 0.60 wt%; "Most H-chondrites have oxygen abundances within the range 32 - 36 wt%" |
| 40 | `Phobos Deimos composition water content hydrated minerals spectra MMX expected water abundance captured asteroid giant impact 2024` | thin | Popular and outreach pages; one summary line says MMX "launched ... in September 2024", contradicted by row 41 (not used); no measured water or oxygen content for either moon |
| 41 | WebFetch then pdftotext of saved copy: Gautier et al., "MIRS: the infrared spectro-imager aboard the Martian Moon eXploration mission ...", Mars Through Time 2025 abstract, https://www-mars.lmd.jussieu.fr/mtt2025/abstracts/Gautier.pdf | useful | Origin "remains unknown" (giant-impact debris or captured primitive asteroids or a binary comet); MMX "will be launched in 2026", Phobos samples to Earth in 2031; water ice and hydrous silicates listed only as things MIRS could detect "if present" |
| 42 | `Ceres interior structure Dawn water ice content crust weight percent Ermakov 2017 Park 2016 Prettyman hydrogen GRaND near-surface water ice` | useful (leads) | Summary: GRaND ~10 wt% hydrogen-equivalent near surface (not traced; not used); arXiv 2004.10504 |
| 43 | Opened (curl, pdftotext): Formisano, Federico, Castillo-Rogez, De Sanctis, Magni, "Thermal convection in the crust of the dwarf planet (1) Ceres", MNRAS (2020), arXiv 2004.10504 | useful | Bulk density 2,162 kg/m^3; two-layer interior (Ermakov 2017): rock about 2,400 kg/m^3, crust 40 km at about 1,300 kg/m^3; no more than 40 vol% weak phase; Castillo-Rogez 2019 crust: 30 vol% ice, 40 vol% clathrate, 20 vol% salt, 10 vol% rock |
| 44 | `comet 67P nucleus mass 1.0e13 kg refractory-to-ice mass ratio Rosetta water ice fraction Choukroun 2020 review` | useful (leads) | Choukroun et al., Space Sci. Rev. 216 (2020), doi 10.1007/s11214-020-00662-1 |
| 45 | WebFetch: HAL hal-03021621; BORIS 147143 and its redirect | dead at the sources | "Access Denied" (Anubis bot wall) on both repositories |
| 46 | WebFetch: DLR elib 135524 (same paper's record) | thin | Abstract only: "wide ranges of plausible values"; no number. Comet ice fraction left as an open thread |
| 47 | `liquid hydrogen boil-off in space percent per day MLI passive storage NASA cryogenic fluid management zero boil-off 20 K cryocooler mass power study` | useful (leads) | NTRS 20020016025, 20120011680, 20150023072, 20190028305; summary figures "2.3, 1.3 and 0.2 percent per day" not traced to a page (not used) |
| 48 | Opened (curl, pdftotext): Hastings, Plachta, Salerno, Kittel, "An Overview of NASA Efforts on Zero Boiloff Storage of Cryogenic Propellants", 2001 Space Cryogenics Workshop, NTRS 20020016025 | useful | Model case 670 kg LH2 / 4,000 kg LO2 in LEO: ZBO mass advantage begins at 60 d (H2) and 10 d (O2); 95 K pulse tube 10 W, 1 W cooling per 12 W input, >4 kg; LH2 cooler goal 2 W at 20 K, 15 kg, 3 to 5% of Carnot; flight 20 K coolers "limited to cooling capacities of <2 W" (OCR ">2"); ground ZBO shown with a 17.5 W, 18 K cooler on a 1.42 m^3 tank (14.5 W heat leak) |
| 49 | Opened (curl, pdftotext): Muratov, Osipov, Smelyanskiy, "Issues of Long-Term Cryogenic Propellant Storage in Microgravity", NASA/TM-2011-215988, NTRS 20120011680 | useful | Passive best case "below 3% per month"; 50-layer MLI, 240 K surroundings: 7.4 x 10^-2 W/m^2, 15 W on 200 m^2, at least 0.6% per month; at 400 K surroundings 0.8 W/m^2, 160 W, 6% per month (both lower bounds, ignoring penetrations) |
| 50 | Opened (curl, pdftotext): Plachta, Johnson, Feller, "Zero Boil-Off System Testing", NASA GRC/ARC, NTRS 20150023072 | useful | Reverse turbo-Brayton cooler with broad-area cooling tubes held a tank 19 days with no venting in simulated LEO; cooler at 10.6 to 12% of Carnot; parasitic loss 4.2 W; ZBO pays for LO2 loiters > 1 week |
| 51 | Opened header only: Krenn and Desenberg, "Return to service of a liquid hydrogen storage sphere", NTRS 20190028305 (KSC ground sphere) | not used | Ground storage; sibling trucking file already carries the KSC 0.09 to 0.10%/day figures |
| 52 | WebFetch (twice): CIAAW, "Abridged Standard Atomic Weights" (2024 table), https://www.ciaaw.org/abridged-atomic-weights.htm | useful | H 1.0080, He 4.0026, Li 6.94, C 12.011, N 14.007, O 15.999, Na 22.990, Mg 24.305, Al 26.982, Si 28.085, P 30.974, S 32.06, Cl 35.45, K 39.098, Ca 40.078, Ti 47.867, Cr 51.996, Mn 54.938, Fe 55.845 |
| 53 | Opened (curl, parsed): NIST Chemistry WebBook gas-phase thermochemistry pages (Mask=3) for water, CO2, CO, methane, ammonia, FeO (C1345251), Fe2O3 (C1309371), Fe3O4 (C1317619) | useful | CODATA: H2O(l) -285.830, H2O(g) -241.826, CO2 -393.51, CO -110.53, NH3 -45.94 kJ/mol; CH4 -74.87 (Chase) / -74.6 (Manion); FeO(s) -272.04 kJ/mol (Chase 1998); Fe2O3 and Fe3O4 pages carry no enthalpy |
| 54 | Same, condensed-phase pages (Mask=2) for Fe2O3, Fe3O4 (and a mistyped ID that returned potassium bromate) | dead at the sources | No enthalpy rows; hematite and magnetite reduction left uncomputed (FeO used as the iron-oxide case) |
| 55 | `Zubrin reverse water gas shift Mars in-situ propellant hydrogen imported from Earth leverage oxygen methane NTRS Pioneer Astronautics report` | useful (leads) | NTRS 19950021840; NTRS 20120001775; IMISPPS "1 kg/day" in a summary (spinoff page, not opened; not used) |
| 56 | WebFetch: NTRS 19950021840, Zubrin and Price, "Mars Sample Return mission utilizing in-situ propellant production" (1995) | thin | Landing page: only sample-return margins; no leverage numbers |
| 57 | Opened (curl, pdftotext): Muscatello and Santiago-Maldonado (NASA KSC), "Mars In Situ Resource Utilization Technology Evaluation", AIAA paper, NTRS 20120001775 (2012) | useful | Reactions SOE / Sabatier / RWGS; Sabatier ">99% CO2 conversion", "could be considered to be 100% efficient"; RWGS "slightly endothermic with a dH of +9 kcal/mol"; RWGS/electrolysis "theoretically ... infinite leverage" of O2 per H2 brought, "some loss of hydrogen is inevitable"; Phoenix confirmed near-surface ice at high latitudes |
| 58 | Opened (curl): NIST WebBook water, phase-change page (Mask=4), parsed for fusion and sublimation enthalpies | dead at the sources | Page body carried only subscription notices in the HTML returned; no fusion or sublimation value extracted |
| 59 | `Mars Water In-Situ Resource Utilization Planning M-WIP study 2016 energy per kg water ice extraction regolith kWh Rodwell power` | useful (leads) | M-WIP report (UCF mirror), NTRS 20160013682, arXiv 2306.03164 (Metzger thermal extraction model, not opened), NASA ice drilling assessment (not opened) |
| 60 | Opened (curl, pdftotext): Abbud-Madrid et al., "Report of the Mars Water In-Situ Resource Utilization (ISRU) Planning (M-WIP) Study", NASA SMD/HEOMD, 22 Apr 2016, 90 p. (UCF mirror of the MEPAG posting) | useful | 16 t water per crew (fully fueled ascent vehicle plus life support) over 480 sols; ore needed: typical regolith 2,000 t at 425 K (~25 kW) or 1,250 t at 575 K (~8 kW), smectite 583 t, gypsum 186 t (~2 kW); glacial ice "100s of meters thick", 90% ice assumed; ice beats the gypsum case if overburden < 2.2 m, typical regolith if < 5.2 to 6.4 m; ISRU LOX + CH4 makes 20.5 to 22.1 kg of propellant per kg landed vs 8.0 for LOX only |
| 61 | `Venus launch from aerostat electromagnetic launcher OR skyhook OR "launch loop" export oxygen carbon dioxide propellant to orbit study` (extended) | dead at the sources | Only the rocket ascent studies already in the sibling files (Landis and Oleson 2024; Seager), generic tether and launch-loop pages, a blog; no study exporting any Venus product by a non-rocket route |
| 62 | `molten oxide electrolysis sulfur-bearing regolith sulfur effect anode oxygen evolution sulfide feedstock Mercury regolith ISRU` | dead at the sources | Lunar MRE pages only (ROXY, LR-1 25 kg run, already in sibling); no study of MRE or any oxygen process on a sulfur-rich (2 to 4 wt% S) feed |
| 63 | Opened (curl, pdftotext): NTRS 20120003152 (KSC slides, MRE self-heating, Joule heating) | thin | Background slides on the self-heating mode; no sulfur, no energy per kg |
| 64 | WebFetch: NASA NSSDC, "Sun Fact Sheet", https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (last updated 9 May 2024) | useful | Mass 1,988,400 x 10^24 kg; volumetric mean radius 695,700 km; GM 132,712 x 10^6 km^3/s^2; escape velocity 617.6 km/s (so GM/R = 1.908 x 10^11 J/kg, matching the sibling's 1.91 x 10^11) |
| 65 | `Mars north polar layered deposits volume SHARAD Putzig 2009 km3 water ice global equivalent layer north polar cap` | useful (leads) | JPL PIA12200; Putzig CryoGeo 2013 slides and EGU2010 abstract (not opened) |
| 66 | WebFetch: NASA/JPL, "PIA12200: Radar mapping of icy layers under Mars' north pole", 22 Sep 2009 | useful | North polar layered deposits "821,000 cubic kilometers", "about 30 percent" of the Greenland ice sheet (after Putzig et al. 2009, Icarus) |

## 3. Findings

**The answer in brief (each line is backed by a table below; D-numbers are in section 5).**

1. **Oxygen does not need to be found anywhere special: it is 42 to 47% of ordinary silicate rock by mass, on Mercury, the
   Moon, Mars and stony asteroids alike** (F3a). Mars itself holds oxygen in its rock (about 43 wt% of its soil), its air
   (1.75 x 10^16 kg of O in CO2), its perchlorate salts and its water ice (88.8% O). Importing oxygen to Mars from Mercury or
   Venus brings nothing Mars lacks and costs the deepest wells in the inner system: 16.9 km/s (Mercury) and 15.2 km/s (Venus
   clouds, ideal) all-propulsive, against 0 km/s for Mars's own oxygen (F3c). **On the sourced numbers the premise "oxygen
   from Mercury or Venus" fails on every link; it is not a close call.**
2. **Hydrogen is plentiful in the Sun but not plentiful to harvest.** The whole Sun loses about 1.3 x 10^9 kg/s as wind,
   about 85% of it hydrogen, spread over the full sky; a collector at 1 AU intercepts about 3 to 4.5 x 10^-15 kg per m^2 per
   s. One tonne of hydrogen a year needs 8,200 to 12,300 km^2 of perfect collector at 1 AU and about 80 to 120 km^2 at
   0.1 AU (F4a). No device that captures and stores solar-wind ions exists even on paper (F4a). Lifting hydrogen out of the
   photosphere costs 2.6 x 10^11 J per kg of hydrogen (8.1 GW of continuous ideal power per kt per year) (F4b). Coronal
   mass ejections add only 1 to 5% to the wind's mass and arrive spread over 20 to 120 degree cones (F4c).
3. **Mars already holds 16 to 22 m of global-equivalent water in its polar deposits alone** (2.3 to 3.2 x 10^18 kg), with
   glacial ice "100s of meters thick" at mid-latitudes (F5). A global layer 1 m deep (1.44 x 10^17 kg of water) would need
   about **0.45 years of the entire Sun's solar-wind hydrogen output**, caught in full, or 4 to 6% of the water Mars's polar
   caps already contain (D5, D10).
4. **If hydrogen were imported anyway, ship it as water ice, or ship hydrogen alone and take the oxygen from Mars's air or
   rock, never oxygen from elsewhere.** Hydrogen is 11.19% of water; liquid hydrogen holds only 70.85 kg/m^3 and boils at
   20.4 K; ice holds 112 kg of hydrogen per m^3 and needs no cryocooler (F6). Water made at Mars from imported H2 plus
   Martian CO2 (reverse water-gas shift) is endothermic and leaves 1.55 kg of CO per kg of water; burning imported H2 with
   O2 releases 15.9 MJ per kg of water (F8).

### F1. Oxygen on Mercury (checklist 1)

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Oxygen in silicate rock, general | "Oxygen itself is the most abundant element in most silicate rocks, typically making up 40-50 wt%", usually computed by stoichiometry, not measured | Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", ch. 2 in *Mercury: The View after MESSENGER* (Cambridge UP, 2018), arXiv:1712.02187, sec. 2.3.3 | Primary (review chapter) | D1: Mercury mantle and lava compositions give 46.1 to 47.0 wt% O by stoichiometry | High |
| Oxygen at the surface, measured | GRS O/Si weight ratio 1.4 (Evans 2012, "cautioned against over-interpretation"), refined to **1.2 +/- 0.1** (McCubbin 2017), against about 1.7 expected from stoichiometry; may reflect near-surface "magmatic degassing in a process similar to industrial smelting". With Si about 25 wt% (sibling `mercury_as_industrial_site.md` D1): **about 30 wt% O** measured, **about 42.5 wt%** if stoichiometric (D1) | Nittler et al. 2018 sec. 2.3.3; sibling `mercury_as_industrial_site.md` F1 | Primary | Sibling F1 carries the same O/Si 1.2 row | Medium (authors flag the low value as possibly unrepresentative) |
| Oxygen in Mercury's surface rock by stoichiometry | NSP lava 47.0 wt%; IcP-HCT lava 46.3 wt%; pre-melting mantle 46.8 and 46.5 wt% (D1; the table excludes 7 to 11 wt% S, which would dilute O to about 43 wt%) | Nittler et al. 2018 Table 2.2; CIAAW 2024 atomic weights; D1 | Primary inputs, derived | Nittler: "40-50 wt%" | High for the arithmetic; medium as a surface value (O/Si conflict above) |
| Oxygen in the whole planet | About **11.5 to 11.6 wt%** (3.8 x 10^22 kg of O), all in the silicate shell; the core (73% of the mass in this model) is taken as O-free (D2) | D2 from Nittler et al. 2018 sec. 2.6 bulk model (core 2,020 km, 6,980 kg/m^3; shell 3,380 kg/m^3) | Derived | Model shell plus core sums to 3.300 x 10^23 kg vs NSSDC 3.3010 x 10^23 | Medium (core light elements uncertain; Nittler Table 2.3 lists no O in the core) |
| Extraction processes and energy | Molten regolith electrolysis about 104 to 135 kWh/kg O2 demonstrated on 25 kg of lunar simulant, 114 kWh/kg in a plant design; carbothermal about 34 kWh(th)/kg before CO-to-O2 conversion; hydrogen reduction of ilmenite 24.3 kWh/kg LOX end to end. **Not repeated here** | sibling `space_processing_and_fabrication.md` 1a and 5 | (cited) | n/a | Medium (lunar feed) |
| What changes at Mercury | Hydrogen reduction works on FeO and ilmenite; Mercury's surface has **almost no FeO** (0.02 to 0.04 wt% in Table 2.2; total Fe 1 to 2 wt%, mostly sulfide), so hydrogen reduction yields almost no oxygen there (inference from the composition). Sulfur 2 to 4 wt%, Na about 3 wt%: **no oxygen process has been studied on a sulfur-rich feed** (rows 62, 63; sibling F10). Carbothermal reduction has an in-place carbon source (graphite about 1 wt%) | Nittler et al. 2018 Table 2.2; sibling `mercury_as_industrial_site.md` F1, F10; log rows 62-63 | Primary / inference | none | Medium for the composition; the process consequence is an inference, flagged |
| Solar power for the plant | Irradiance 6,250 to 14,390 W/m^2; flown arrays held below 150 to 230 C by tilting and mirrors; equatorial night 88 days (2,100 kWh storage per kW); best polar point lit about 82% of the solar day | sibling `mercury_as_industrial_site.md` F4, F6 | (cited) | n/a | High |
| Plant power for a stated oxygen flow | At 114 kWh/kg: 11.5 MW continuous per kt of O per year; 11.5 GW per Mt (D9) | D9 | Derived | n/a | Medium (lunar-feed process figure) |
| Product form and storage | O2 boils at 90.19 K at 1 atm (liquid 1,141 kg/m^3, Hvap 213.1 kJ/kg); vapor pressure 2.50 atm at 100.0 K, 5.36 atm at 110.0 K, 10.1 atm at 120.0 K; critical point 154.58 K (above it only a compressed gas exists) | NIST Chemistry WebBook fluid tables (row 11) | Primary (dataset) | n/a | High |
| What this means at Mercury (DERIVED) | Mercury's polar cold traps average near 100 K (sibling F5): LOX could sit there in a tank at about 2.5 atm with little or no active cooling; anywhere sunlit (ground to 700 K, radiator sink about 580 K by day) it boils off unless refrigerated | D13; sibling `mercury_as_industrial_site.md` F4, F11 | Derived | none | Medium (tank-level heat leaks not modeled) |
| Launch to Mercury orbit | Escape 4.25 km/s, 9.0 MJ/kg; lander ascent 3.5 km/s with about 19% gravity loss (Palaszewski); a launcher at the lunar design's scaling needs 0.30 GW per Mt/yr to escape | sibling `mercury_as_industrial_site.md` F8; `inner_system_mining_synthesis.md` 3 | (cited) | n/a | Medium |
| Whether liquid oxygen can ride a mass driver | **Not found.** The designs carry sintered rock at 288 to 10,000 m/s^2; no source treats a cryogenic liquid payload at those accelerations | sibling `space_trucking_and_transport_infrastructure.md` F6 | n/a | none | Gap |

### F2. Oxygen on Venus (checklist 2)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Oxygen mass fraction of CO2 | **72.71%** (D1); of the whole atmosphere (96.5% CO2 by volume, 3.5% N2) the oxygen inventory is **3.4 x 10^20 kg** | D1 (CIAAW); sibling `venus_as_extraction_site.md` 3.1 (element inventory) | Derived | n/a | High |
| Extraction: solid-oxide electrolysis | MOXIE (flown on Mars) 6 to 12 g/hr, 300 W, 25 to 50 kWh/kg at instrument scale; full-scale study **5.7 kWh/kg O2**; thermodynamic floor 4.91 kWh/kg; no compressor needed at cloud pressure; intake needs an acid filter | sibling `venus_as_extraction_site.md` 3.3 | (cited) | Same chemistry in Landis and Oleson 2024 and Horn et al. 2026 (sibling) | Medium |
| Product streams | 2 CO2 -> 2 CO + O2: **1.75 kg of CO per kg of O2** (stoichiometry); the sibling records MOXIE making "nearly twice" its O2 mass of CO | D1 arithmetic; sibling 3.3 | Derived / cited | each other | High |
| What the CO is worth | CO/O2 burns as rocket propellant at Isp 250 s (the only ascent propellant Venus can make without imported hydrogen); a balloon can recombine CO and O2 for power through the about 50-hour night (Horn et al.); CO is a reductant and a carbon feedstock (Fischer-Tropsch-type use is an inference, not studied here) | sibling `venus_as_extraction_site.md` 3.3, 3.7 | (cited) | none | Medium |
| Storage at cloud level | Platforms fly at about 50 to 61 km (Horn et al., sibling), where the air is 107 C at 50 km (sibling); everywhere there is far above O2's critical temperature (154.58 K, NIST), so oxygen can only be stored there as a compressed gas or refrigerated liquid, or kept chemically (unsplit CO2, or recombined) | NIST row 11; sibling 3.4 | Primary / derived | none | High (phase physics) |
| The export problem | Ascent from the cloud deck about 9 km/s (circular speed 7.29 km/s at 55 km); payload fraction 0.15 to 0.56%; 180 to 670 kt lifted per kt delivered; cloud deck to low Mars orbit 11.82 km/s ideal, 15.19 all-propulsive; on CO/LOX at 250 s, **248 to 985 t of propellant per t delivered** with the studied 9 km/s ascent (D7) | sibling `venus_as_extraction_site.md` 3.7; `space_trucking_and_transport_infrastructure.md` D1; D7 | (cited) / derived | n/a | Medium |
| Any non-rocket export route | **None studied.** No electromagnetic launch, skyhook, launch loop or beamed launch from Venus (row 61, a second search after the sibling's row 76); no stationary elevator is possible (synchronous radius 1.5 times outside the Hill sphere, sibling) | log row 61; sibling 3.7 | n/a | sibling row 76 | High that none is published |

### F3. The deciding comparison: oxygen at the destination and along the route (checklist 3)

#### F3a. Oxygen mass fraction by source

| Source | O, wt% | Basis | Source | Primary or secondary | Confidence |
|---|---|---|---|---|---|
| Mercury surface rock | 42.5 to 47 by stoichiometry; about 30 as measured by GRS | F1 | Nittler et al. 2018 | Primary | Medium |
| Mercury, whole planet | about 11.5 | D2 | derived | Derived | Medium |
| Venus atmosphere (CO2) | 72.7 of CO2; 3.4 x 10^20 kg O total | F2 | sibling + D1 | Derived | High |
| Lunar soil | **41 to 45** ("Oxygen (41-45%)"); minerals 30 to 45 (RP-1057, sibling) | Korotev | R. L. Korotev (Washington University in St. Louis), "The chemical composition of lunar soil", https://sites.wustl.edu/meteoritesite/items/the-chemical-composition-of-lunar-soil (undated web page) | Primary (specialist's reference page) | High |
| Carbonaceous CI chondrite (C-type analog) | 45.9 | Lodders 2010, Table 2 | sibling `venus_as_extraction_site.md` 3.2 | (cited) | High for CI |
| Ordinary chondrites (S-type analog) | **33.5 (H), 36.7 (L), 38.4 (LL)** by stoichiometry of the average-fall oxides (metal, FeS carry none) (D1); paper: "Most H-chondrites have oxygen abundances within the range 32-36 wt%" | Schaefer and Fegley, "Outgassing of ordinary chondritic material...", Icarus (2007), arXiv astro-ph/0606671, Table 1 and sec. on O | Primary | Search summary of Wasson and Kallemeyn 1988: 35.7 / 37.7 / 38.3 (row 38, not opened) | High |
| Phobos, Deimos | **Not measured.** Origin unknown (giant-impact debris, captured primitive asteroid, or binary comet); MMX launches 2026, returns Phobos samples in 2031. By analog, 42 to 46 if Mars-like or CI-like, about 34 to 38 if ordinary-chondrite-like | Gautier et al., MIRS abstract, Mars Through Time 2025, https://www-mars.lmd.jussieu.fr/mtt2025/abstracts/Gautier.pdf; sibling `mars_venus_and_transfer.md` 3.5 (C-type spectra) | Primary (abstract) | none | Low (no composition measurement) |
| **Mars soil** | **42.5 to 43.6** (Gusev 43.6, Meridiani 43.1, Rocknest 42.5); volatile-free crust 42.8 (D1) | APXS averages | Ehlmann et al., "Chemistry, mineralogy, and grain properties at Namib and High dunes...", JGR Planets 122:2510 (2017), https://pmc.ncbi.nlm.nih.gov/articles/PMC5815393/ | Primary | High |
| Mars perchlorate | 64.35% of ClO4- is O; at 0.4 to 0.6 wt% perchlorate, 0.26 to 0.39 wt% of soil (D1) | Hecht 2009 (sibling) | sibling `mars_venus_and_transfer.md` 3.4 | Derived | Medium |
| Mars atmosphere | CO2 96.2% by mass (95.1% by volume): **1.75 x 10^16 kg of O** in 2.5 x 10^16 kg of air (D1) | NSSDC via sibling | sibling 3.1 | Derived | High |
| Mars water ice | 88.81% O by mass; polar deposits 2.3 to 3.2 x 10^18 kg of water | Plaut 2007 via sibling; D5 | sibling `venus_as_extraction_site.md` 3.2 | Primary (cited) | High |

#### F3b. Extraction energy at Mars, for comparison with F1 and F2

| Route at Mars | Energy | Source | Primary or secondary | Confidence |
|---|---|---|---|---|
| O2 from the air (solid-oxide CO2 electrolysis, MOXIE flown) | about 5.7 kWh/kg O2 in a full-scale design including compression and liquefaction (25 to 50 kWh/kg at MOXIE scale) | sibling `venus_as_extraction_site.md` 3.3 (Hinterman 2021) | (cited) | Medium |
| Water from regolith (M-WIP reference cases, 16 t over 480 sols, 33.3 kg/sol) | About **1.5 kWh/kg** (gypsum-rich, 186 t ore, ~2 kW), **5.9** (typical regolith at 575 K, 1,250 t, ~8 kW), **18.5** (typical regolith at 425 K, 2,000 t, ~25 kW) (D-extra) | Abbud-Madrid et al., M-WIP Study report, 22 Apr 2016 (MEPAG), UCF mirror https://sciences.ucf.edu/class/wp-content/uploads/sites/23/2020/04/Mars_Water_ISRU_Stud1.pdf | Primary (NASA study) | Medium (powers are read from a flow chart and exclude loading and transport, per the report's note) |
| Water from buried glacial ice | Glacial ice "100s of meters thick"; ice is the better ore than gypsum if overburden is under 2.2 m, than typical regolith if under 5.2 to 6.4 m; extraction power not given | M-WIP report | Primary | Medium |
| O2 from water | ISS OGA about 7.75 kWh/kg O2 | sibling `space_processing_and_fabrication.md` 5 | (cited) | Medium |

#### F3c. Delta-v, propellant and fleet to bring oxygen to low Mars orbit (DERIVED unless marked)

All rows are circular-coplanar Hohmann lower bounds; "aero" assumes free aerocapture at Mars (never flown as a single pass;
sibling trucking F4). Propellant per tonne delivered (payload plus dry mass) from the rocket equation (D7).

| Source | dv aero / all-propulsive (km/s) | Hydrolox 452 s, t prop per t | SEP 2,890 s, t prop per t | Tug output, t per kW-yr (scaled) | Source of dv |
|---|---|---|---|---|---|
| Mars surface (own oxygen) | 0 / 0 (to orbit if needed: 3.41 km/s ideal, about 5 km/s with losses) | 0 | 0 | n/a | sibling `mars_venus_and_transfer.md`; D7 |
| Phobos to 300 km orbit | 1.21 / 1.21 (0.56 to an entry trajectory) | 0.31 | 0.043 | about 0.79 | D7 (JPL elements via sibling) |
| Lunar surface | 3.28 / 5.37 (no Oberth use) | 1.09 / 2.35 | 0.12 / 0.21 | about 0.18 | D7 |
| Main belt 2.2 to 3.2 AU | 1.91 to 3.28 / 3.76 to 6.10 | 0.54 to 1.09 / 1.33 to 2.96 | 0.07 to 0.12 / 0.14 to 0.24 | about 0.16 to 0.25 | sibling trucking D1 |
| LEO (Earth) | 3.57 / 5.66 | 1.24 / 2.58 | 0.13 / 0.22 | about 0.17 | sibling trucking D1 |
| Low Mercury orbit | 10.34 / 16.94 (surface: +3.5 ascent = 20.44) | 9.3 / 44.6 (surface 99) | 0.44 / 0.82 impulsive; **about 1.9 by low-thrust spiral (about 30 km/s)** | **about 0.032** | sibling trucking D1; D7 |
| Venus cloud deck | 11.82 / 15.19 ideal (13.53 / 16.90 with the studied 9 km/s ascent) | 13.4 / 29.7 (CO/LOX 250 s: 248 / 985) | 0.52 / 0.71 | not applicable (the ascent is chemical) | sibling trucking D1; D7 |

**What the sourced numbers say about importing oxygen to Mars at all.** Oxygen is the most abundant element in the rock under
any Mars base (about 43 wt%) and is in the air (1.75 x 10^16 kg) and the ice. Every import is a cost with no compensating
gain in grade: Mercury's rock is no richer in oxygen than Mars's (about 46 vs 43 wt% by stoichiometry, and Mercury's
measured surface value is lower), and Venus's CO2 is no different from Mars's CO2 except that there is 1.9 x 10^4 times more
of it at the bottom of a 9 km/s well. At 1 Mt of oxygen a year from Mercury by solar-electric tug, the scaled fleet is
about 28 GW of tugs burning about 1.7 Mt/yr of propellant (xenon output is about 65 t/yr) (D-extra). The comparison that
decides the question is therefore not Mercury against Venus but **any import against local extraction at 5.7 to 7.75
kWh/kg**. On these figures, oxygen import to Mars makes sense in no case found; the only case with a plausible argument
is Phobos or Deimos material delivered to Mars *orbit* (1.2 km/s), where it competes with lifting from the surface (about
5 km/s), and even that is for a customer in orbit, not for water on the ground.

### F4. Hydrogen from the Sun (checklist 4)

#### F4a. Collecting the solar wind

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Total solar-wind mass loss | **2 x 10^-14 M_sun/yr** (Cohen 2011) = 1.26 x 10^9 kg/s; 2.1 x 10^-14 M_sun/yr in cycle 23, about 10% lower in cycle 24 (Mishra 2019) = 1.32 x 10^9 kg/s (D3) | O. Cohen, arXiv:1107.2275 (2011), abstract; Mishra, Srivastava, Wang, Mirtoshev, Zhang, Liu, "Mass loss via solar wind and coronal mass ejections during solar cycle 23 and 24", MNRAS (2019), arXiv:1904.09898, doi:10.1093/mnras/stz1001 | Primary | Brief's known fact: 1.3 x 10^9 kg/s | High |
| Mass flux at 1 AU | Sibling (ecliptic): **3.09 x 10^-15 kg m^-2 s^-1**; sphere-averaged from the mass-loss rates: **4.5 to 4.7 x 10^-15** (D3). Flux falls as r^-2 | sibling `starlifting_synthesis.md` 2; D3 | (cited) / derived | each other within a factor 1.5 (Conflicts K2) | Medium |
| Composition | A_He = 100 n_He/n_H "rarely exceeds 5" in steady wind; about 4.5 in fast wind; photosphere about 8; CME plasma "A_He > 20" reported; A_He falls to zero at 259 km/s | Kasper, Stevens, Lazarus, Steinberg, Ogilvie, ApJ 660:901 (2007), https://lweb.cfa.harvard.edu/~jkasper/publications/Kasper-2007-ApJ-Helium.pdf | Primary | Brief's photospheric X = 0.7438 | High |
| Hydrogen mass fraction of the wind | **0.834 to 0.863** for A_He 4 to 5 (heavier ions ignored); hydrogen and helium are separable in principle by mass (factor 4) once captured (D3) | D3 | Derived | n/a | High (arithmetic) |
| Perfect-collector area per tonne of H per year | 1.524 AU (Mars): 19,000 to 28,500 km^2; **1 AU: 8,200 to 12,300**; 0.3 AU: 740 to 1,110; **0.1 AU: 82 to 123**; 0.0465 AU (Parker perihelion): 18 to 27 km^2 (D3) | D3 | Derived | Sibling starlifting areas for iron are larger by the H/Fe ratio (about 700), consistent | Medium (100% capture assumed; no device exists) |
| Flown yield (Genesis) | Goal "10 to 20 micrograms" of solar wind in total from a 636 kg spacecraft over about 29 months: about 4 to 9 x 10^-9 kg/yr, **about 10^-11 kg per kg of spacecraft per year** (D3). Sibling: 0.2 mg H/yr on 1.67 m^2 (in-tile implantation figure) | NASA/JPL, "Genesis Launch Press Kit", July 2001, https://www.jpl.nasa.gov/news/press_kits/genesislaunch.pdf | Primary | sibling starlifting 3E | High (DEMONSTRATED) |
| Electrostatic focusing (SWIFT concept) | "a cone diameter of 1 km could generate thrust on the order of 2 mN at 1 AU" with "~1000 km/s" exhaust, i.e. about 2 x 10^-9 kg/s of protons through a 0.79 km^2 inlet, the same as the geometric wind flux (2.4 x 10^-9 kg/s, D3): **about 0.06 kg per year** if it were stored instead of thrown out | Gemmer and Mazzoleni (NC State), IAC-14,C4,8 (2014), abstract, https://iafastro.directory/iac/archive/browse/IAC-14/C4/8/24646/ | Primary (conference abstract) | D3 geometric check | Low-medium (SPECULATIVE concept; abstract only) |
| Magnetic or electrostatic capture-and-store device | **None found** (rows 29, 30); the magnetic structures in the literature deflect the wind for thrust (sibling); a Bussard-type scoop is described in popular sources as producing more drag than useful mass | log rows 29-31; sibling `starlifting_synthesis.md` 2 | n/a | n/a | High that no design exists |
| Storage of what is caught | Neutralized hydrogen would have to be cooled to 20 K and liquefied or bound into a carrier (F6). The wind arrives at no less than about 259 km/s (the speed at which Kasper et al. find A_He falls to zero, "the minimum solar wind speed observed at 1 AU"), so a stopping collector absorbs at least 0.5 x (259 km/s)^2 = 3.4 x 10^10 J per kg caught as heat (derived) | F6; Kasper et al. 2007 | Derived | none | Low (no design) |

**Yield per unit of hardware (solar wind).** Demonstrated: about 10^-11 kg per kg of spacecraft per year (Genesis). Design
concept (SWIFT inlet, if stored): about 0.06 kg/yr per km-diameter inlet at 1 AU, about 6 kg/yr at 0.1 AU. Perfect
collector bound: 1 t/yr per 8,200 to 12,300 km^2 at 1 AU. **Nothing in the sources reaches gram-per-year hardware.**

#### F4b. Lifting hydrogen out of the photosphere

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Escape energy from the photosphere | GM/R = **1.908 x 10^11 J/kg** (GM 132,712 x 10^6 km^3/s^2, R 695,700 km) | NASA NSSDC, "Sun Fact Sheet", https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (9 May 2024) | Primary | Brief: 1.91 x 10^11 J/kg; escape speed 617.6 km/s | High |
| Per kg of hydrogen (He lifted with it, X = 0.7438) | **2.57 x 10^11 J**; ideal continuous power 8.1 MW per t/yr, **8.1 GW per kt/yr**, 8.1 TW per Mt/yr (D4) | D4 | Derived | n/a | High (ideal; no losses, no separation) |
| Literature on beamed or magnetic lifting | Life-extension concepts only (Criswell 1985; Lazarus Stars); "no engineering design"; one concept "needs as-yet uninvented materials" | sibling `starlifting_synthesis.md` 2 | (cited) | row 32 (no new design found) | High that none exists |
| Yield per unit hardware | **Undefined**: no hardware exists at any scale | — | — | — | — |

#### F4c. Intercepting coronal mass ejections

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| CME masses | 7,668 LASCO CMEs (1996-2009): range 10^11 to 10^17 g; histogram peak 3.4 x 10^14 g; 3.9 x 10^14 and 1.1 x 10^15 g in the two adjacent columns (labeled "Average" and "Median" in the extracted table) | Vourlidas, Howard, Esfandiari, Patsourakos, Yashiro, Michalek, ApJ (2010), arXiv:1008.3737, sec. 3.2 and Table 2 | Primary | A summary's "average 1.6 x 10^15 g" (row 24, unopened) | Medium (column labels in the extraction look swapped; see Conflicts K3) |
| CME mass flux | 1.8 x 10^15 g/day averaged over 1996-2009 (2.1 x 10^7 kg/s, 1.6% of the wind); peak monthly loss 3.5 x 10^17 g/month (1.3 x 10^8 kg/s) at cycle-23 maximum; CMEs about 5% of ecliptic wind mass flux at maximum, negligible at minimum | Vourlidas 2010 Table 2; Mishra et al. 2019 | Primary | Each other within the cycle variation | Medium |
| Composition | Helium-enriched: A_He above 20 reported (so a lower hydrogen fraction than the wind) | Kasper et al. 2007 | Primary | none | Medium |
| Catch per event | A 3.4 x 10^11 to 1.1 x 10^12 kg CME spread over a 20 to 120 degree cone at 1 AU deposits about 5 x 10^-12 to 5 x 10^-10 kg per m^2; to take one tonne from a single event needs about 2 to 200 million km^2 (D3) | D3 | Derived | none | Low-medium (uniform spreading assumed) |

**Reading.** CMEs are sporadic, helium-rich, spread over tens of degrees, and add 1 to 5% to what a wind collector already
sees. They are not a separate resource; at best a few-percent bonus on the same collector.

### F5. Hydrogen from elsewhere (checklist 5)

| Source | Inventory (H or water) | Distance and dv to Mars | Extraction | Source | Confidence |
|---|---|---|---|---|---|
| **Mars polar layered deposits** | South 1.6 x 10^6 km^3 (Plaut 2007, sibling) + north **821,000 km^3** (Putzig 2009) = 2.4 x 10^18 kg at 1,000 kg/m^3, **16.8 m** global layer (D-extra); sibling range 2.3 to 3.2 x 10^18 kg, 16 to 22 m | On Mars | Melt or mine ice; regolith water 1.5 to 18.5 kWh/kg (F3b) | NASA/JPL, "PIA12200: Radar mapping of icy layers under Mars' north pole", 22 Sep 2009, https://www.jpl.nasa.gov/images/pia12200-radar-mapping-of-icy-layers-under-mars-north-pole/ ; sibling `venus_as_extraction_site.md` 3.2 | High |
| Mars mid-latitude ice and soil water | Glacial ice "100s of meters thick"; soil 1.5 to 3 wt% water; ice within meters poleward of about 40 deg | On Mars | M-WIP cases (F3b) | M-WIP 2016; sibling `mars_venus_and_transfer.md` 3.4 | Medium-high |
| Solar wind reaching Mars naturally | About 0.04 kg/s of H on Mars's cross-section, 1.3 x 10^6 kg/yr; over 4 Gyr at today's rate about 0.3 m of global water (upper bound) (D11) | n/a | n/a | D11 | Low (today's flux and no escape assumed) |
| Phobos, Deimos | Phobos 1.06 x 10^16 kg, Deimos smaller; water content **unknown** until MMX (2026 launch, 2031 return) | 1.2 km/s to low orbit (D7) | unknown | Gautier et al. 2025; sibling 3.5 | Low |
| Ceres | Bulk density 2,162 kg/m^3; 40 km crust at about 1,300 kg/m^3; crust modeled as 30 vol% ice plus 40 vol% clathrate (Castillo-Rogez 2019); "up to 25%" water by NASA (sibling): up to about 2.3 x 10^20 kg of water | Mars-Ceres Hohmann v-inf 3.27 / 2.81 km/s, windows every 3.18 yr (sibling network F1); escape 516 m/s | Ice mining at 0.28 m/s^2 gravity | Formisano et al., MNRAS (2020), arXiv:2004.10504; sibling `belt_jupiter_saturn_and_deep_transit.md` 3A | Medium |
| Carbonaceous asteroids | CI about 20 wt% water, CM about 9 wt%; C-complex surfaces 4.5 wt% (0 to 11.5); water released below 600 C | Belt to Mars 1.91 to 3.28 km/s depart | Heating, 2 to 17 kWh/kg by microwave (Mars simulants) | sibling `belt_jupiter_saturn_and_deep_transit.md` 3A; `space_processing_and_fabrication.md` 1a | Medium |
| Comets and Kuiper-belt ice | **No inventory number obtained** (Choukroun et al. 2020 review: refractory-to-ice ratios show "wide ranges of plausible values"; full text behind bot walls) | Orbit-specific; no study found | n/a | log rows 44-46 | Gap |
| Moon polar ice | "at least ... 600 million metric tons" (north, radar); Cabeus 5.6 +/- 2.9 wt% | Lunar surface to low Mars orbit 3.28 / 5.37 km/s (D7) | Ice mining | sibling `moon_lagrange_and_comparables.md` A5 | Medium |
| Mercury polar ice | 2.1 x 10^13 to 3 x 10^15 kg of water (H 1.1 to 3.4 x 10^14 kg) | Low Mercury orbit to Mars 10.34 / 16.94 km/s | Ice in shadowed craters under 10 cm of dark lag | sibling `mercury_as_industrial_site.md` F5; `venus_as_extraction_site.md` 3.2 | Medium |
| Venus atmosphere and clouds | H 6.7 x 10^14 kg in the gas; about 2 x 10^12 kg in cloud droplets; 400 to 530 times less H than Mars's polar caps | 9 km/s ascent, 11.82 / 15.19 km/s to Mars | Acid cracking 97.5 MJ per kg H (sibling) | sibling `venus_as_extraction_site.md` 3.1-3.3 | Medium |
| Jupiter, Saturn, ice giants | Hydrogen atmospheres; orbital speed at 10 km altitude 41.9 (Jupiter), 25.5 (Saturn), 15.1 (Uranus), 16.6 km/s (Neptune); escape 59.5 and 35.5 km/s; mining studied only at the ice giants and only for fusion fuel; a gas-core aerospacecraft (unbuilt) with 20.5 km/s; "most captured gas is spent lifting the rest" | Jupiter to Mars Hohmann v-inf 4.27 depart / 5.88 arrive, 3.08 yr (sibling belt file) | Palaszewski studies | sibling `space_trucking_and_transport_infrastructure.md` F1b, F6; `belt_jupiter_saturn_and_deep_transit.md` 3B | Low (SPECULATIVE engines) |

### F6. Moving hydrogen (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Liquid hydrogen | Normal boiling point **20.37 K**, liquid density **70.85 kg/m^3**, heat of vaporization **448.7 kJ/kg**; triple point 13.96 K, critical point 33.15 K, 12.8 atm (normal hydrogen) | NIST Chemistry WebBook fluid tables, hydrogen (C1333740) (row 11) | Primary (dataset) | Sibling processing file: triple 13.95 K, critical 33.18 K | High |
| Passive boil-off in microgravity | Best passive MLI "below 3% per month"; a 50-layer MLI on a 200 m^2 tank in 240 K surroundings gives at least 15 W, **0.6% per month**; in 400 K surroundings 160 W, **6% per month** (lower bounds, no penetrations) | Muratov, Osipov, Smelyanskiy, NASA/TM-2011-215988, NTRS 20120011680 | Primary (NASA TM) | D13: 15 W boils 88 kg/month, matching the TM's "at least 90 kg/month" | Medium (model; no in-orbit LH2 storage rate has been measured in any source found) |
| Zero boil-off (ZBO) | ZBO beats passive storage after **60 days** for LH2 and 10 days for LO2 (670 kg LH2 / 4,000 kg LO2 model in LEO); flight 20 K coolers "limited to cooling capacities of <2 W" (2001); goal 2 W at 20 K, **15 kg**, 3 to 5% of Carnot; a 95 K cooler gives 1 W per 12 W input at >4 kg. A ground ZBO test held a tank 19 days with no venting using a reverse turbo-Brayton cooler at 10.6 to 12% of Carnot | Hastings et al., NTRS 20020016025 (2001); Plachta, Johnson, Feller, NTRS 20150023072 | Primary | each other | Medium (ground tests; the LH2 flight cooler goal is a 2001 goal) |
| Cooling penalty at 20 K (DERIVED) | 117 to 467 W of input per W of heat lifted at 20 K (300 K rejection, 3 to 12% of Carnot); 19 to 78 W per W at 90 K for LOX (D13) | D13 | Derived | n/a | High (thermodynamics) |
| Hydrogen carriers, mass fraction of H (stoichiometry) | H2 100%; **CH4 25.13%**; **NH3 17.76%**; LiH 12.68%; **N2H4 12.58%**; **H2O 11.19%**; MgH2 7.66% (D6) | CIAAW 2024; D6 | Derived | n/a | High |
| Hydrogen per m^3 of liquid at 1 atm | LH2 70.8; CH4 106.1 (111.7 K); NH3 121.0 (239.8 K); water 107 (373 K) to 112 (273 K) kg H/m^3 (D6). **Every common carrier stores more hydrogen per m^3 than liquid hydrogen does** | NIST tables; D6 | Derived | n/a | High |
| Handling (sourced only where shown) | CH4 boils at 111.7 K and NH3 at 239.8 K (NIST); water is a solid that needs no tank at Mars temperatures; hydrazine (toxic, monopropellant) is not in the NIST fluid database (row 12); hydride release temperatures not sourced | NIST; row 12 | Primary | none | Medium |
| Hydrogen versus water as cargo (DERIVED) | Shipping hydrogen moves 11.19% of the water's mass: **8.94 times less cargo** if Mars supplies the oxygen. Shipping water ice moves 8.94 times the mass but in a passive, dense, robust form that can also serve as reaction mass and radiation shielding (sibling trucking F6) | D5, D6 | Derived | n/a | High (stoichiometry) |
| Hydrogen versus methane or ammonia | A carrier made with Martian carbon or nitrogen is not available at the source (the carrier's heavy atom must be shipped from the source too). Methane carries 25% hydrogen by mass and stores at 112 K, which a passive radiator can reach far more easily than 20 K (inference from the boiling points and D13) | D6, D13 | Derived | none | Medium (inference) |

### F7. The chain as a whole (checklist 7)

| Water at Mars | H needed | O needed | Solar-wind collector, 1 yr, 1 AU (0.1 AU) | Photosphere lift, ideal power for 1 yr | O plant at Mercury (MRE 114 kWh/kg), 1 yr | Same O from Mars air (SOE 5.7 kWh/kg) |
|---|---|---|---|---|---|---|
| 1 kt | 112 t | 888 t | 1.33 x 10^6 km^2 (13,300 km^2) | 0.91 GW | 11.5 MW | 0.58 MW |
| 1 Mt | 1.12 x 10^5 t | 8.88 x 10^5 t | 1.33 x 10^9 km^2 (1.33 x 10^7) | 0.91 TW | 11.5 GW | 0.58 GW |
| 1 Gt | 1.12 x 10^8 t | 8.88 x 10^8 t | 1.33 x 10^12 km^2 = 0.87 times the Sun's cross-section (1.33 x 10^10) | 909 TW | 11.5 TW | 0.58 TW |
| 1 m global layer (1.44 x 10^17 kg) | 1.62 x 10^13 t | 1.28 x 10^14 t | 1.9 x 10^17 km^2 for one year, 68% of the entire 2.8 x 10^17 km^2 sphere at 1 AU; equivalently **0.45 years of the Sun's entire wind hydrogen** | 1.3 x 10^8 TW (4.1 x 10^27 J, **about 11 s of the Sun's total output**) | 1.7 x 10^9 GW | 8.3 x 10^7 GW |

(D5, D9, D10, D-extra; luminosity 3.828 x 10^26 W from sibling `mercury_as_industrial_site.md` D4.)

**Fleet and time.** From Mercury, oxygen moves at about 0.032 t per kW-yr by solar-electric spiral (scaled, D8): 28 MW of tugs
per kt/yr and 28 GW per Mt/yr, with about 1.9 t of propellant per t delivered at 2,890 s; Mercury-Mars windows recur every
100.9 days by Hohmann (sibling network F1), but spirals and flyby routes take years. Solar-wind hydrogen collected at 0.1 AU
must climb out of a 34.85 km/s departure to reach Mars (sibling trucking D1). **Compare simply delivering water:** Mars's own
ice: 0 km/s and 1.5 to 18.5 kWh/kg; Phobos (if it has water): 1.2 km/s to orbit; the belt: 3.8 to 6.1 km/s all-propulsive,
belt-to-Mars windows every 2.8 to 4.4 years (sibling trucking F4); Ceres: windows every 3.18 years. **No version of the
Mercury-Venus-Sun chain beats any of these on any figure found.**

### F8. Chemistry of making water at Mars (checklist 8)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| H2 + 1/2 O2 -> H2O(l) | dfH H2O(l) **-285.830 +/- 0.040 kJ/mol** (CODATA): **15.87 MJ per kg of water**, 141.8 MJ per kg of H2; to vapor 13.42 MJ/kg (dfH(g) -241.826) (D12) | NIST Chemistry WebBook, water, https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=3 | Primary | n/a | High |
| Heat released for the targets | 1.6 x 10^13 J per kt; 1.6 x 10^16 J per Mt; 1.6 x 10^19 J per Gt; 2.3 x 10^24 J for a 1 m global layer (D12) | D12 | Derived | n/a | High |
| Reaction control | The same reaction runs controlled in fuel cells and is what the oxygen and hydrogen "are" in energy terms: making water from H2 and O2 releases the energy that splitting it consumed (ISS OGA 7.75 kWh/kg O2 = 6.9 kWh per kg of water). Uncontrolled mixing of hydrogen and oxygen is an explosion hazard (flammability and detonation limits were not sourced this session; Open threads) | sibling processing 5; D12 | (cited) / derived | none | Medium |
| Water by reducing Martian CO2 (RWGS) | CO2 + H2 -> CO + H2O: **+41.15 kJ/mol** from NIST enthalpies (paper: "+9 kcal/mol"); **+2.28 MJ per kg of water**; consumes 2.44 kg CO2 and leaves 1.55 kg CO per kg of water; with electrolysis and recycling, "theoretically ... infinite leverage" of O2 per H2 brought | NIST (row 53); Muscatello and Santiago-Maldonado (NASA KSC), "Mars In Situ Resource Utilization Technology Evaluation", AIAA, NTRS 20120001775 (2012) | Primary | each other (Conflicts K4) | High |
| Water by Sabatier | CO2 + 4H2 -> CH4 + 2H2O: **-165.0 kJ/mol** (exothermic); ">99% CO2 conversion"; only 4.47 kg water per kg H fed (half the H leaves as methane) | NIST; Muscatello 2012 | Primary | n/a | High |
| Water by reducing Martian iron oxide | FeO + H2 -> Fe + H2O(g): **+30.2 kJ/mol** (FeO(s) -272.04, Chase 1998); 3.99 kg FeO per kg water; at 16.3 to 19.2 wt% FeO (total Fe as FeO), **21 to 25 kg of soil per kg of water** if all FeO were reduced; lunar hydrogen reduction runs at 900 to 1,050 C and reduces only about half the Fe2+ | NIST; Ehlmann 2017 (APXS); sibling `space_processing_and_fabrication.md` 1a | Primary / derived | none | Medium (the APXS FeO is total iron; Mars soil also holds Fe3+) |
| Limit of the Martian air as an oxygen source (DERIVED) | All the oxygen in Mars's atmospheric CO2 (1.75 x 10^16 kg) makes at most 1.97 x 10^16 kg of water by RWGS: **0.14 m of global layer**. A 1 m layer needs 7.3 times the atmosphere's oxygen, so beyond about 0.1 m the oxygen must come from rock or ice (D12) | D12 | Derived | n/a | High (arithmetic) |

## 4. Conflicts

- **K1. Mercury surface oxygen.** Measured GRS O/Si 1.2 +/- 0.1 (McCubbin 2017; earlier 1.4, Evans 2012) gives about 30 to 35 wt%
  O; stoichiometry for the measured cations gives about 42.5 to 47 wt%. Nittler et al. suggest the low value reflects
  near-surface smelting-like alteration, not the bulk lavas. For an oxygen budget this matters by a factor of about 1.4 at
  the surface and not at all for the whole planet (shell O by mantle models).
- **K2. Solar-wind mass flux at 1 AU.** 3.09 x 10^-15 kg m^-2 s^-1 (sibling, ecliptic) against 4.5 to 4.7 x 10^-15 (whole-Sun
  mass-loss rates spread over a sphere). Mishra et al. note that ecliptic 1 AU data "can represent the global mass flux ...
  is not perfectly valid"; Cranmer 2017 (via Mishra) has the sphere-averaged rate about 50% larger at maximum. Both are shown
  in D3; the areas differ by 1.45.
- **K3. CME mass statistics.** Vourlidas 2010 Table 2 as extracted lists 3.4 (peak), 3.9 ("Average") and 11 ("Median") x 10^14 g;
  a median above the mean is unusual for a right-skewed distribution, so the two labels may be swapped in extraction. A
  search summary gave an average of 1.6 x 10^15 g from another paper (not opened). Both 3.9 x 10^14 and 1.1 x 10^15 g were
  carried in D3.
- **K4. RWGS enthalpy.** NIST formation enthalpies give +41.15 kJ/mol (gas-phase water at 298 K); Muscatello gives "+9 kcal/mol"
  (+37.7 kJ/mol). The difference is likely the temperature or water phase basis; neither changes any conclusion.
- **K5. MMX launch date.** A search summary said MMX launched in September 2024 (row 40); the instrument team abstract says
  "will be launched in 2026" (row 41). The team abstract is used.
- **K6. Mars polar water.** Plaut 2007 via the sibling: both deposits 16 to 22 m global layer; this file's sum of SPLD 1.6 x 10^6 km^3
  and NPLD 821,000 km^3 at 1,000 kg/m^3 gives 16.8 m. Consistent; the NPLD contains some dust, so 16.8 m is an upper value for
  that sum.

## 5. Derived figures

Scripts: scratch folder `oxygen_and_hydrogen_supply_for_mars_water/calc/chain_calc.py` (output `chain_calc_output_run1.txt`)
and the one-off lines in `extra_output_run1.txt`. Constants: CIAAW 2024 atomic weights; NSSDC Sun (M 1.9884 x 10^30 kg,
R 695,700 km); JPL GM values and radii via the sibling files; g0 = 9.80665 m/s^2; year = 365.25 d. **Run note:** one line of
the extra run printed the polar-deposit total in kg/m^2 (16,769 kg/m^2) where meters were meant; 16,769 kg/m^2 of water is
16.8 m. Corrected in the text; no other figure depends on it.

- **D1. Oxygen from oxides.** O wt% = sum over oxides of (wt% x n_O x 15.999 / formula mass); elements, metal and FeS carry
  none. Key output: Mercury NSP lava 47.0, IcP-HCT lava 46.3, NSP mantle 46.8, IcP-HCT mantle 46.5; Mars Gusev 43.6,
  Meridiani 43.1, Rocknest 42.5, crust 42.8; H / L / LL chondrites 33.5 / 36.7 / 38.4 wt%. Mass fractions: O in CO2 0.7271,
  in H2O 0.8881, in ClO4- 0.6435. Mars air: CO2 mass fraction 0.951 x 44.009 / 43.49 = 0.962; O = 2.5 x 10^16 x 0.962 x
  0.7271 = 1.75 x 10^16 kg.
- **D2. Mercury whole-planet O.** Core (4/3) pi (2,020 km)^3 x 6,980 = 2.410 x 10^23 kg; shell (4/3) pi (2,440^3 - 2,020^3) km^3
  x 3,380 = 8.90 x 10^22 kg; shell O = 46.5 to 46.8 wt% x 0.92 (Nittler adds 1 wt% Fe and 7 wt% S) = 42.8 to 43.1 wt%;
  O = 3.81 to 3.83 x 10^22 kg = 11.5 to 11.6 wt% of 3.3010 x 10^23 kg.
- **D3. Solar wind.** 2 x 10^-14 x 1.9884 x 10^30 / 3.156 x 10^7 s = 1.260 x 10^9 kg/s; / (4 pi AU^2) = 4.48 x 10^-15 kg m^-2 s^-1
  (2.1 x 10^-14: 1.323 x 10^9 kg/s, 4.70 x 10^-15). X_H = 1.008 / (1.008 + A_He x 4.0026): 0.863, 0.848, 0.834 for A_He 0.040,
  0.045, 0.050. Area per t H per yr = 1,000 / (F1 r^-2 x X_H x 3.156 x 10^7): 1 AU 11,884 to 12,291 km^2 (F1 3.09e-15) and 8,195 to
  8,476 (4.48e-15); 0.3 AU 1,070 to 1,106 and 738 to 763; 0.1 AU 118.8 to 122.9 and 81.9 to 84.8; 0.0465 AU 25.7 to 26.6 and 17.7 to
  18.3; 1.524 AU 27,601 to 28,547 and 19,034 to 19,686. Genesis 10 to 20 ug / 2.3 to 2.4 yr = 4.2 to 8.7 x 10^-9 kg/yr; / 636 kg =
  0.7 to 1.4 x 10^-11 per kg per yr. SWIFT 2 mN / 10^6 m/s = 2.0 x 10^-9 kg/s; 1 km inlet x 3.09e-15 = 2.4 x 10^-9 kg/s; 0.063 kg/yr.
  CMEs: 1.8 x 10^15 g/day = 2.08 x 10^7 kg/s (1.6% of 1.323 x 10^9); peak 3.5 x 10^17 g/month = 1.33 x 10^8 kg/s; a cone of full
  width w at 1 AU has area 2 pi (1 - cos(w/2)) AU^2 = 2.14 x 10^21 (20 deg), 1.88 x 10^22 (60), 7.03 x 10^22 m^2 (120): 3.4 x 10^11 kg
  gives 1.6 x 10^-10 to 4.8 x 10^-12 kg/m^2; 1.1 x 10^12 kg gives 5.1 x 10^-10 to 1.6 x 10^-11 kg/m^2.
- **D4. Photosphere.** GM/R = 1.32712 x 10^20 / 6.957 x 10^8 = 1.908 x 10^11 J/kg; / 0.7438 = 2.565 x 10^11 J per kg H; per t/yr
  8.13 MW; per kt/yr 8.13 GW; 2,397 GW of world solar capacity (sibling synthesis) at 100% would lift 2.9 x 10^5 t H/yr.
- **D5. Water.** H2O 18.015 g/mol; H 11.19%, O 88.81%; 8.936 kg water per kg H. Mars area 4 pi (3,389.5 km)^2 = 1.4437 x 10^14 m^2;
  1 m layer 1.4437 x 10^17 kg (H 1.616 x 10^16, O 1.282 x 10^17 kg). Polar deposits 2.31 to 3.18 x 10^18 kg = 16 to 22 m; the
  1 m layer is 4.5 to 6.2% of them.
- **D6. Carriers.** H fractions from CIAAW; H per m^3 = liquid density x fraction: LH2 70.85 x 1 = 70.8; CH4 422.36 x 0.2513 =
  106.1; NH3 681.64 x 0.1776 = 121.0; water 958.37 x 0.1119 = 107.2 (373 K), 999.79 x 0.1119 = 111.9 kg/m^3 (273.16 K).
- **D7. Delta-v.** Moon: Earth-relative speed at 384,400 km for v-inf 2.945 km/s: sqrt(2.945^2 + 2 x 398,600 / 384,400) = 3.278;
  minus 1.022 = 2.256; with lunar escape 2.376: sqrt(2.256^2 + 2.376^2) = 3.28 km/s from the surface (no Oberth burn near
  Earth, so an upper value for this geometry). Phobos (a = 9,375 km, v = 2.137 km/s) to 300 km circular: 0.531 + 0.675 = 1.206 km/s;
  to a 130 km periapsis 0.558 km/s. Propellant per tonne = exp(dv / (Isp g0)) - 1. Mercury-Mars low-thrust estimate: circular
  heliocentric speeds 47.87 and 24.13 km/s (difference 23.74) + 2.89 (spiral out of low Mercury orbit) + 3.43 (spiral into 300 km
  Mars orbit) = 30.1 km/s; at 2,890 s: exp(30.06 / 28.34) - 1 = 1.89 t per t; at 4,022 s, 1.14.
- **D8. Tug productivity**, scaled as 0.279 t/kW-yr x 3.42 / dv (sibling trucking F3; linear in dv, ignores longer trip times and
  empty returns, so it flatters the long legs): Phobos 0.79; Moon 0.18; belt 0.16 to 0.25; Mercury spiral 0.032 t per kW-yr.
  1 Mt of O per year from Mercury: 0.888 x 10^6 / 0.032 = 2.8 x 10^7 kW = 28 GW of tugs; propellant 1.89 x 0.888 Mt = 1.7 Mt/yr.
- **D9. Oxygen plant power** = O mass x kWh/kg / 8,766 h: 1 kt of water (888 t O): MRE 114 kWh/kg 11.5 MW; SOE 5.7 kWh/kg 0.58 MW;
  water electrolysis 7.75 kWh/kg 0.79 MW. Scale linearly (x 10^3, 10^6, 1.44 x 10^11).
- **D10. Hydrogen supply** = H mass / (3.09e-15 x 0.863 x 3.156e7) per year at 1 AU: 1 kt 1.33 x 10^6 km^2; 1 Mt 1.33 x 10^9; 1 Gt
  1.33 x 10^12 km^2 (Sun's cross-section pi R^2 = 1.521 x 10^12 km^2); 1 m layer 1.92 x 10^17 km^2 (the whole sphere at 1 AU is
  2.81 x 10^17 km^2). Whole-wind H per year 1.323 x 10^9 x 0.863 x 3.156 x 10^7 = 3.60 x 10^16 kg; 1.616 x 10^16 / 3.60 x 10^16 =
  0.45 yr. Photosphere lift for the 1 m layer: 1.616 x 10^16 x 2.565 x 10^11 = 4.14 x 10^27 J; / 3.828 x 10^26 W = 10.8 s.
- **D11. Mars's natural intercept.** 3.09e-15 / 1.524^2 x pi (3,389.5 km)^2 x 0.863 = 0.041 kg/s = 1.31 x 10^6 kg/yr; x 4 x 10^9 yr =
  5.2 x 10^15 kg H = 4.7 x 10^16 kg water = 0.32 m (upper bound: today's flux, geometric cross-section, no losses).
- **D12. Chemistry.** 285.830 kJ/mol / 0.018015 kg/mol = 15.87 MJ/kg; / 0.002016 kg H2 = 141.8 MJ/kg. RWGS: (-110.53 - 241.826) -
  (-393.51) = +41.15 kJ/mol; Sabatier: -74.87 - 2 x 241.826 + 393.51 = -165.0 kJ/mol; FeO: -241.826 + 272.04 = +30.21 kJ/mol;
  FeO 71.844 / 18.015 = 3.99 kg per kg water. Air limit: 1.75 x 10^16 / 0.8881 = 1.97 x 10^16 kg water = 0.136 m.
- **D13. Cryogenics.** Boil-off = Q / 448.7 kJ/kg: 15 W 2.89 kg/day (88 kg/month); 160 W 30.8 kg/day. Cooler input per W lifted =
  (T_h - T_c) / T_c / (fraction of Carnot): 20 K, 300 K: 14 / 0.03 to 0.12 = 467 to 117; 90 K: 2.33 / 0.03 to 0.12 = 78 to 19.
- **D-extra.** M-WIP water energy: 8 kW x 24.66 h / 33.3 kg = 5.9 kWh/kg; 25 kW: 18.5; 2 kW: 1.5. Polar deposits:
  (0.821 + 1.6) x 10^6 km^3 x 10^9 m^3/km^3 x 1,000 kg/m^3 = 2.42 x 10^18 kg; / (1,000 kg/m^3 x 1.4437 x 10^14 m^2) = 16.8 m.

## 6. Constraints for any inhabitant

- **Oxygen is never the scarce half of water anywhere a base would sit**: rock is 33 to 47 wt% O (F3a). A settlement that has
  power has oxygen; the binding inputs are energy (5.7 to 135 kWh per kg O2 depending on the route, F1, F3b) and hydrogen.
- **At Mars, the water is already there**: 16 to 22 m of global-equivalent ice at the poles and thick buried glaciers at mid-latitudes
  (F5). Mining water from soils costs about 1.5 to 18.5 kWh per kg in the M-WIP cases, and that study rates buried glacial ice as having "certain advantages" over granular ores; any import has to beat that, and none found does.
- **The Martian air can supply only about 0.14 m of global water's worth of oxygen** (F8); large-scale water making from imported
  hydrogen would draw its oxygen from rock or ice, and each kg of water made from air leaves 1.55 kg of carbon monoxide to handle.
- **Liquid hydrogen is a hostile cargo**: 20 K, 70.85 kg/m^3, at least 0.6 to 6% lost per month without active cooling, and 117 to
  467 W of electric input per W of heat removed with it (F6). Ice and methane are far easier to keep.
- **Combining hydrogen and oxygen releases 15.9 MJ per kg of water**: the reaction is a power source (fuel cells) and an explosion
  hazard (F8).
- **Near-Sun collection means working where survivable hardware is bounded by what has flown** (Parker's shield, under 50 W
  admitted, sibling) and returning from a 35 km/s departure (0.1 AU) (F4, F7).
- **Venus-side and Mercury-side oxygen plants are bound to local use**: their product sits behind a 9 km/s ascent (Venus) or a
  10 to 17 km/s transfer (Mercury) (F2, F3c). A human-shaped machine working such a plant at Mercury works by night, in polar shade,
  or behind shields (sibling Mercury constraints); at Venus it works on a floating platform in acid cloud.

## 7. Candidate handwaves (flagged, not accepted; the developer decides)

- **H-1. Oxygen exported from Mercury or Venus to Mars at any scale.** Mars has the same oxygen locally at 0 km/s; the imports cost
  10.3 to 16.9 km/s (Mercury) or 11.8 to 16.9 km/s (Venus). Any design that does this needs a reason the sources do not supply.
- **H-2. Solar-wind or photospheric hydrogen at kilotonne-per-year scale or more.** 1 kt of water a year needs about 1.3 million
  km^2 of perfect collector at 1 AU (or 13,000 km^2 at 0.1 AU) with no capture device yet designed; a 1 m Martian ocean layer needs
  0.45 years of the Sun's entire wind hydrogen, or 11 seconds of the Sun's entire luminosity spent on lifting.
- **H-3. Liquid hydrogen stored for years in transit or at Mars without large active cooling.** The flown 20 K coolers are under
  2 W; passive storage loses 0.6 to 6% per month at best.
- **H-4. Making a global water layer at Mars from imported hydrogen plus Martian air alone.** The air holds oxygen for about 0.14 m.

## 8. Open threads

- **Comet and Kuiper-belt water inventories**: the Choukroun et al. 2020 review (Space Sci. Rev. 216) could not be read (bot walls
  at HAL and BORIS; DLR abstract has no numbers). Next: arXiv copy of the review; Rosetta 67P mass and porosity papers.
- **Phobos and Deimos water and oxygen content**: unmeasured; MMX returns samples in 2031. Next: Murchie or Fraeman spectral papers
  on 2.7 um band depths.
- **Any oxygen process on a high-sulfur, high-alkali feed (Mercury)**: none found twice (rows 62-63; sibling F10).
- **Non-rocket export from Venus**: none found twice (row 61; sibling row 76).
- **A capture-and-store solar-wind collector**: none found (rows 29-31). The SWIFT papers (IAC-14, IAC-15) were read as abstracts
  only; their full texts might give inlet mass per area.
- **In-orbit LH2 boil-off measured on a flight tank**: not found; only models and ground tests (rows 47-51). Next: CRYOTE and
  Starship propellant-transfer flight data when published.
- **Hydrogen and oxygen flammability and detonation limits** (for the safety row in F8): not sourced this session.
- **Water fusion and sublimation enthalpies** (for ice-melting energy): the NIST phase-change page did not return values (row 58).
- **Clathrate hydrate and hydrazine handling data**, and metal-hydride release temperatures: not sourced.
- **Iron(III) oxide reduction enthalpies**: NIST pages without values (row 54).
- **Mars mid-latitude ice volume**: only qualitative here ("100s of meters"); SHARAD volume papers not opened.
- **A low-thrust Mercury-to-Mars trajectory study**: none; D7's 30 km/s is an Edelbaum-style estimate.
- Found and not read: arXiv 1407.4258 (CME review), arXiv 1204.2776 (slow-wind helium), arXiv 2306.03164 (Metzger thermal extraction
  model), NTRS 20160013682 (M-WIP NTRS copy), NASA Mars ice drilling assessment, NTRS 20070014073 (lunar solar-wind volatile loss).

## 9. Rejected sources

- **Wikipedia, "Star lifting"** (row 32): states 1.6 x 10^13 J/kg to lift solar material to Mercury, 85 times the photospheric
  escape energy (1.91 x 10^11 J/kg from NSSDC GM and R). Wrong by about two orders of magnitude; not used.
- **Search-engine summaries** with numbers not traced to an opened page: OMNI means (row 17), Ulysses polar proton flux (row 20),
  CME average 1.6 x 10^15 g (row 24), Wasson and Kallemeyn O values (row 38, used only as a cross-check), MMX "launched September
  2024" (row 40, contradicted), Ceres GRaND 10 wt% (row 42), LH2 "2.3, 1.3 and 0.2 percent per day" (row 47), IMISPPS 1 kg/day
  (row 55).
- **Game forums, fandom wikis and a game issue tracker** on magnetic scoops (row 29): no physics content.
- **arXiv 2609.06496** (Lunar Sourcebook oxide table, via summary): not opened; Korotev's 41 to 45% used instead.
- **Popular and outreach pages on Phobos and Deimos** (row 40): leads only.
