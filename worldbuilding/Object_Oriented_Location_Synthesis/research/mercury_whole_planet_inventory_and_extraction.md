# Mercury as a whole planet: inventory, layer order and physical excavation

*Research file, OOLSD library, tranche 8, section 2. Started 2026-10-11. Physics and engineering only; no setting assumed.*

## 1. Scope

Mercury as a whole body: its bulk elemental inventory, its layers (crust, mantle, possible sulfide layer, liquid outer core,
solid inner core) in the order an excavation would reach them, the interior's physical state and its response to unloading,
and the hardware, throughput, energy and waste that excavating it would imply. Surface environment, launch and transport are
in the sibling files `mercury_as_industrial_site.md` [ME] and `inner_system_mining_synthesis.md` [IS] and are cited, not re-derived.

## 2. SEARCH LOG

| # | Date | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read (allowed, read-only) siblings `inner_system_mining_synthesis.md`, `starlifting_synthesis.md`, `mercury_as_industrial_site.md` (whole), `space_processing_and_fabrication.md` (findings 1a-1e, 5, 7) | useful | Surface composition (F1), structure (F2), regolith (F3), thermal (F4), ice (F5), launch (F8), processing energies are cited, not re-derived |
| 2 | 2026-10-11 | Page (curl + pdftotext): arXiv 1712.02187, Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury" (ch. 2 of *Mercury: The View after MESSENGER*, Cambridge 2018); read §2.3.1 (volatiles), §2.4 (mantle), §2.5 (core), §2.6 (bulk), Tables 2.2 and 2.3 | useful (core source) | Mantle oxide estimates; 7-11 wt% S in mantle; core 69-77% of mass; CMB ~5.5 GPa; core Fe 75-95, Si 0-17(25), S 0-20; bulk-model recipe |
| 3 | 2026-10-11 | `Morgan Anders 1980 "Chemical composition of Earth, Venus, and Mercury" PNAS bulk composition Mercury` | thin | Located the paper; the search summary's element list (Fe 64.47 wt% etc.) is **not used** (not seen in an opened page) |
| 4 | 2026-10-11 | Pages: PMC350422 (curl, then WebFetch), Europe PMC `?pdf=render`, Europe PMC full-text API, pnas.org PDF | dead at the source | Captcha / HTML shells; WebFetch saw only page images |
| 5 | 2026-10-11 | Page: aanda.org 2014 aa22208-13 table T6 (WebFetch 403; curl "enable JS") | dead at the source | Possibly a table of bulk models; unread |
| 6 | 2026-10-11 | arXiv API query (script `scripts/axq.py`): `all:Mercury AND all:interior AND all:core` (27 results) | useful (leads) | Located Margot et al. 2018 "Mercury's Internal Structure" (arXiv 1806.02024). Session resumed here after an interruption (row 7 onward by the resuming agent) |
| 7 | 2026-10-11 | Re-read of the downloaded [NIT18] text §2.4-2.6 and Tables 2.2-2.3 (local copy in scratch `dl/nit18.txt`) | useful | Pre-melting mantle oxides (NSP, IcP-HCT), the §2.6 bulk recipe (core 2,020 km at 6,980 kg/m^3, shell 3,380, + 1 wt% Fe and 7 wt% S, core 1.5 wt% S, core Si 0-25 wt%), melting rate ~10 wt%/GPa, melt segregation ~60 km, adiabat 0.3 K/km, IcP-HCT melting starting at the CMB (400 km) |
| 8 | 2026-10-11 | Page (curl + pdftotext): arXiv 1806.02024, Margot, Hauck, Mazarico, Padovan, Peale, "Mercury's Internal Structure", ch. 4 of *Mercury: The View after MESSENGER* (2018); read §5-7, §8.3, §10, Tables 4-6 | useful (core source) | 1,479 best-fit models: layer radii, densities, masses (Table 5); PRMM mass split 0.5 / 73.4 / 23.5 / 2.5%; central pressure 35.77 GPa, CMB 5.29 GPa; Tcmb 1,945 K; basal mantle 1,600-1,900 K; surface 440 K; top of liquid core 400-440 km down |
| 9 | 2026-10-11 | `Mercury present-day surface heat flux mW/m2 thermal evolution model mantle convection Tosi 2013 core-mantle boundary temperature` | useful (leads) | Led to Tosi and Padovan 2019 (arXiv 1912.05207) and Knibbe et al. 2025 |
| 10 | 2026-10-11 | Page (curl + pdftotext): arXiv 1912.05207, Tosi and Padovan, "Mercury, Moon, Mars: Surface expressions of mantle convection and interior evolution of stagnant-lid bodies" (AGU Monograph, 2020); read §5.1, §6.2, Fig. 6 | useful | Dynamo theory; sub-adiabatic CMB flux and stratified core top; core adiabatic flux 12-19 mW/m^2; elastic thickness 30-35 vs 80-100 km at 3.9-3.8 Ga. **No present-day surface heat-flux number in the text** |
| 11 | 2026-10-11 | `Mercury "heat flux" present-day surface "mW m" estimate lithosphere thrust fault depth Egea-González OR Peterson OR "Hauck" 2018` (extended mode) | thin | Search summaries gave ancient (scarp-age) heat flows 18-50 mW/m^2 and a "6-29 mW/m^2" megaregolith range; **not used** (no page opened); they are ancient, not present-day |
| 12 | 2026-10-11 | `Mercury present-day mantle heat flow mW/m2 thermal evolution model arXiv Mercury interior today "surface heat flow" Padovan 2017 OR Knibbe 2025` | useful | Led to the open Knibbe 2025 PDF |
| 13 | 2026-10-11 | Page (curl + pdftotext): Knibbe, Rivoldini, Zhao, Van Hoolst, "On the thermal evolution and magnetic field generation of planet Mercury", Phys. Earth Planet. Inter. 363:107348 (2025), publi2-as.oma.be record 7922 | useful (core source for item 3) | Table 1 parameters (Namur 2016b solidus; mantle k 4 W/m/K, c 1,142 J/kg/K; radiogenic contents); Table 2 present-day CMB 1,690-1,923 K, center 2,019-2,224 K, inner core 896-1,491 km, CMB heat flow 570-781 GW (11-15 mW/m^2). Surface heat flux shown only in a figure (not read off) |
| 14 | 2026-10-11 | `McDonough Yoshizaki 2021 "Terrestrial planet compositions controlled by accretion disk magnetic field" Mercury bulk composition core mass fraction Fe wt%` | useful (leads) | Journal version open-access at Prog. Earth Planet. Sci. 8:39 (2021) |
| 15 | 2026-10-11 | Pages: springeropen "track/pdf" (curl), springeropen article page and link.springer.com (WebFetch) | dead at the source | HTML instead of PDF; redirect to a login (idp.springer.com) |
| 16 | 2026-10-11 | arXiv API: `au:McDonough AND au:Yoshizaki`; `ti:Mercury AND (ti:composition OR ti:bulk)` | useful | Found the preprint of the same paper (arXiv 2009.04311) |
| 17 | 2026-10-11 | Page (curl + pdftotext): arXiv 2009.04311, McDonough and Yoshizaki, "Accretion disk's magnetic field controlled the composition of the terrestrial planets" (preprint of PEPS 2021); Table 1 and Methods | useful (core source for item 1) | Bulk Mercury, mass %: O 18.3, Mg 11.8, Si 9.65, Fe 52.3, Ni 3.00, Al 1.16, Ca 1.25, S 2.50; method: silicate:metal:sulfide 40:53:7 by mass at 3,100 / 7,100 / 4,600 kg/m^3; O by difference |
| 18 | 2026-10-11 | arXiv API: `all:Mercury AND (all:origin OR all:formation) AND all:MESSENGER` | useful | Located Ebel and Stewart 2017 |
| 19 | 2026-10-11 | Page (curl + pdftotext): arXiv 1712.08234, Ebel and Stewart, "The Elusive Origin of Mercury", ch. 18 of *Mercury: The View after MESSENGER*; read §18.2.3, §18.5.1 | useful | Two bulk "cases" (A: 340 km mantle + 7 wt% S + 2 wt% C, 80 km FeS shell, 2,020 km core with 5% Ni, 1.5% S, 0.5% C, 8% Si; B: no FeS shell, core 3% S, 4% Si); states that Morgan and Anders (1980) assumed 5.5 wt% FeO in pyroxene and lunar values, and that "Results from MESSENGER invalidate such assumptions"; Fegley-Cameron vaporization model "not supported by the MESSENGER results" |
| 20 | 2026-10-11 | Page (curl + text strip): CIAAW, "Standard atomic weights" (ciaaw.org/atomic-weights.htm) | useful | Atomic weights for oxide-to-element conversions in D1 |
| 21 | 2026-10-11 | `UNEP International Resource Panel Global Resources Outlook 2024 global material extraction billion metric tons per year metal ores non-metallic minerals` | thin | Press coverage only (Down to Earth, Statista); "106 billion metric tons" lead |
| 22 | 2026-10-11 | Page: unep.org Global Resources Outlook 2024 (WebFetch) | dead at the source | 403 Forbidden |
| 23 | 2026-10-11 | `"Global Resources Outlook 2024" pdf metal ores extraction "billion metric tons" 2020 non-metallic minerals 45 resourcepanel.org` (extended mode) | useful (leads) | Led to the IRP press release and Schandl et al. 2024 (J. Ind. Ecol.) |
| 24 | 2026-10-11 | Page: Wiley, Schandl et al. 2024 "Global material flows and resource productivity: The 2024 update" (WebFetch) | dead at the source | 403 Forbidden |
| 25 | 2026-10-11 | Page: resourcepanel.org, "Global Resources Outlook 2024 - Press release" (WebFetch) | useful | "growth in resource use since 1970 from 30 to 106 billion metric tons"; no per-group tonnage in the release |
| 26 | 2026-10-11 | `World Mining Data 2024 total world mining production million metric tons 2022 Austrian Federal Ministry Reichl Schatz pdf` | useful | Led to the BMF PDF of World Mining Data 2026 |
| 27 | 2026-10-11 | Page (curl + pdftotext): Reichl and Schatz, *World Mining Data 2026* (Austrian Federal Ministry of Finance), bmf.gv.at WMD2026.pdf; §3 and Tables 6.1.1, 6.1.6 | useful | World mining production 2024: 19,442,935,209 t (recoverable content, not run-of-mine; excludes bauxite and construction minerals), of which mineral fuels 16,826,217,540 t and iron and ferro-alloys 1,635,733,704 t |
| 28 | 2026-10-11 | `Takraf Bagger 293 bucket wheel excavator daily capacity 240,000 m3 specifications weight Hambach` | thin | Wikipedia and media; the "218,880 t/day" and "16.56 MW" figures are Wikipedia-only (**not used**) |
| 29 | 2026-10-11 | Page: Guinness World Records, "Heaviest land vehicle" (WebFetch) | useful (secondary, record body) | Bagger 293: 14,196 t; TAKRAF 1995; 240,000 m^3 of earth per day; 220 m long |
| 30 | 2026-10-11 | `Caterpillar 797F mining truck specifications rated payload 363 metric tons gross machine operating weight cat.com` (domains: cat.com, caterpillar.com, scene7) | useful | |
| 31 | 2026-10-11 | Page (curl + pdftotext): Caterpillar, "Cat 797F Mining Truck Specifications" (AEXQ spec sheet, scene7 CM20190125-36969-04587) | useful (manufacturer) | Nominal payload 363 t; 2,983 kW; heaped 240-267 m^3; 67.6 km/h loaded |
| 32 | 2026-10-11 | `Rio Tinto Kennecott Bingham Canyon mine pit depth width kilometers metric tons of material moved per day` | thin | Trade press only |
| 33 | 2026-10-11 | Page: riotinto.com Kennecott operations (WebFetch) | thin | Mining since 1903; no dimensions on the page |
| 34 | 2026-10-11 | Page: Mining Technology, "Top ten deepest open-pit mines in the world" (26 Sep 2013) (WebFetch) | useful (secondary, trade press) | Bingham Canyon "more than 1.2 km deep", ~4 km wide; Chuquicamata >850 m; others 430-645 m |
| 35 | 2026-10-11 | `Kola superdeep borehole SG-3 12,262 m bottom-hole temperature 180 °C ICDP OR journal article deep drilling results` | thin | Popular pages only (12,262 m; 180 C); used once, labeled secondary, low confidence, for scale only |
| 36 | 2026-10-11 | `Mponeng mine depth below surface meters deepest mine in the world Harmony annual report virgin rock temperature` | useful (lead) | |
| 37 | 2026-10-11 | Page: Harmony Gold, Mponeng operation page (WebFetch) | useful (operator) | Mining at "3 160m – 3 740m below surface"; "the deepest mine in the world" |
| 38 | 2026-10-11 | `planetary scale excavation concept dismantling a planet crust stripping mass driver "Mercury" engineering study Criswell "planet engineering" mining entire planet` (extended mode) | thin | Wikipedia, blogs, a news piece; one self-published GitHub report (next row); no peer-reviewed planetary-excavation design |
| 39 | 2026-10-11 | Page (curl): GitHub RokoMijic/MercurialDyson `written_report.md` (last commits 3-4 Apr 2026), "Mercurial Dyson: Engineering the Rapid Disassembly of a Planet" | useful as a **SPECULATIVE, non-peer-reviewed** comparator only | 58 doublings from a 1,000 t seed; endgame 3.4 x 10^15 (kg/s implied) through 80,000 mass-driver tubes; ~150 kJ/kg surface mining heat; 20-50 m mined chunks; "~70% iron-nickel core". **Searched for "molten", "liquid core", "outer core", "decompress", "magma": no treatment of the molten core or of mantle decompression anywhere in the text** |
| 40 | 2026-10-11 | `Jull McKenzie 1996 effect of deglaciation on mantle melting beneath Iceland decompression melting rate increase unloading` | useful (leads) | Terrestrial unloading analog |
| 41 | 2026-10-11 | Page (curl): HAL insu-03597790, Maclennan et al. 2002 G-cubed PDF | dead at the source | HTML shell returned |
| 42 | 2026-10-11 | Page: EarthRef ERR 41250, abstract of Jull and McKenzie 1996, JGR, doi 10.1029/96JB01308 (WebFetch) | useful | Eruption rate up ~30 times steady state 10,000-8,000 yr ago as ice disappeared; 2 km ice sheet modeled; unloading over 1,000 yr |
| 43 | 2026-10-11 | `Alcock Itkin Horrigan 1984 vapor pressure equations for the metallic elements iron liquid log p coefficients` | useful | |
| 44 | 2026-10-11 | Page (curl + pdftotext): Caltech MMRC copy of the CRC table "Vapor pressure of the metallic elements" (Alcock, Itkin, Horrigan, Can. Metall. Q. 23:309, 1984) | useful (handbook) | Fe liquid log(p/atm) = 6.347 - 19,574/T; Fe melting 1,808 K in the table; valid 10^-15 to 10^-3 atm, +/-5% |
| 45 | 2026-10-11 | `Mercury nitrogen abundance bulk or surface MESSENGER nitrogen volatile inventory enstatite chondrite nitrogen Mercury magma ocean nitrogen partitioning` | dead at the sources | No measured nitrogen abundance for Mercury in any result (K, Th, U, S, Cl only); MESSENGER's instruments did not report N. Gap stated in F6 |
| 46 | 2026-10-11 | `Caloris basin diameter km MESSENGER Fassett 2009 "Caloris impact basin" exterior deposits interior plains thickness` | useful (leads) | Led to Meier et al. 2026 (arXiv 2608.26957) |
| 47 | 2026-10-11 | Page (curl + pdftotext): arXiv 2608.26957, Meier, Reinhardt, Jutzi, Stadel, "Three-dimensional SPH simulations of the Caloris basin-forming impact" (submitted to ApJ, 27 Aug 2026); read abstract, §2, §3.1.3, §3.2 | useful (preprint) | Caloris rim-to-rim ~1,550 km (Murchie 2008); ellipse 1,525 x 1,315 km, area-equivalent ~1,420 km (Fassett 2009); survey impact energies ~8 x 10^26 to 1 x 10^29 J, impactor masses 1.1-9.0 x 10^19 kg; mantle under the basin thinned from ~470 to ~330 km, core surface raised ~120 km; CMB ~1,800 K in their thermal models |
| 48 | 2026-10-11 | `global mine tailings production billion metric tons per year Global Tailings Review OR ICMM OR UNEP estimate` | thin | Summaries quote 8.85-14.4 Gt/yr and 13 Gt/yr; pages not yet opened |
| 49 | 2026-10-11 | Pages: Global Tailings Review ch. VII PDF (curl), UNDRR and PreventionWeb hazard sheets, mining.com (WebFetch) | dead at the source | HTML shell / 403 on all four; the 8.85-14.4 Gt/yr range is **not used** |
| 50 | 2026-10-11 | `icmm.com tailings "billion metric tons of tailings" generated each year` (domains: icmm.com, globaltailingsreview.org, unep.org) | useful | Led to the ICMM report PDF |
| 51 | 2026-10-11 | Page (curl + pdftotext): ICMM, *Tailings Progress Report: Implementing the Global Industry Standard* (2025), pimcore.icmm.com | useful (industry body) | "Globally, an estimated 13 billion metric tons of tailings are generated at mine sites each year" |
| 52 | 2026-10-11 | Local Python, run 1: `scratch/.../scripts/calc_mercury_whole.py` | thin | **Self-correction logged:** run 1 crashed on a string-format bug after section D1 (no numbers affected); fixed and rerun |
| 53 | 2026-10-11 | Local Python, run 2 (`calc_output_run2.txt`) | useful | D1-D6 |
| 54 | 2026-10-11 | `Elkins-Tanton Hager 2005 "Giant meteoroid impacts can cause volcanism" decompression melting excavation depth mantle melt volume` (second angle on unloading melt, row 40) | useful (lead) | |
| 55 | 2026-10-11 | Page: geologyscience.ru repository record, Elkins-Tanton and Hager, EPSL 239:219-232 (2005), doi 10.1016/j.epsl.2005.07.029 (WebFetch) | useful (abstract) | "A 300-km-radius crater in 75-km-thick lithosphere can create 10^6 km^3 of magma from instantaneous in situ decompression of mantle material with a potential temperature of 1300 °C" |
| 56 | 2026-10-11 | Local Python, run 3 (`calc_output_run3.txt`; D1-D6 identical to run 2, D7 added) | useful | Authoritative output for section 5 |
| 57 | 2026-10-11 | Page: cosmochemistry-papers.com repost of Tosi, Grott, Plesa, Breuer, "Thermochemical evolution of Mercury's interior", JGR Planets (2013), doi 10.1002/jgre.20168 (WebFetch) (second angle on present-day heat flow, rows 9-13) | thin | Convection ceases after 3-4 Gyr; contraction ongoing; **no present-day heat-flux number on the page**. Present-day surface flux therefore stays a derived figure (D4) |
| 58 | 2026-10-11 | arXiv API: `ti:Mercury AND (abs:"inner core" OR abs:"core composition" OR abs:"light element")` (second angle on core composition, rows 2, 7, 8) | thin | Six results; nothing newer on core light elements than [NIT18] and [MAR18]; not opened |
| 59 | 2026-10-11 | `BepiColombo 2026 first results Mercury interior moment of inertia core radius MORE radio science new estimate` (second angle on interior figures) | thin | Orbit insertion is scheduled for November 2026 (news page, secondary); no BepiColombo interior result exists yet, so MESSENGER-era figures stand |
| 60 | 2026-10-11 | Local Python, run 4 (`calc_output_run4.txt`; D1-D7 unchanged, D8 added) | useful | **Self-correction logged:** a draft inference that the solid inner core would melt as soon as the mantle is removed was wrong; D8 shows the bare core's own gravity keeps its central pressure near 30 GPa, so only the outer core decompresses fully when the mantle is gone. Corrected before writing F3 |
| 61 | 2026-10-11 | `McCubbin 2017 JGR Planets Mercury "smelting" degassing sulfur carbon reduced lavas "Si-rich metal" surface composition abstract` (open thread carried from [ME]: processing of graphite- and sulfur-bearing rock) | useful (lead) | |
| 62 | 2026-10-11 | Page (curl + pdftotext): NTRS 20170001343, McCubbin, Vander Kaaden, Peplowski et al., "Oxygen Depletion on the Surface of Mercury: Evidence of Silicon Smelting?" (LPSC 48, 2017) | useful | Revised O/Si 1.2 +/- 0.1; reaction 2C + SiO2(melt) -> 2CO + Si(metal); "confining pressures of more than 100 millibars of CO are needed to prevent the formation of Si metal in the presence of graphite" at lava liquidus ~1,320-1,360 C; model surface compositions 12.6-17.9 wt% metallic Fe-Si |
| 63 | 2026-10-12 | Final check of every figure against the log, plus an American English sweep | useful | **Self-corrections:** a draft F3 line attributed the liquid-core evidence to "Earth-radar librations" (wording not in the opened text) and was changed to the source's "Earth-based and MESSENGER observations"; British spellings inside quotations ("kilometres", "tonnes", "metres", "vapour") converted; HW-4 restated against the mean binding energy (5.4 MJ/kg, D6) |

## 3. Findings

Every number below was read in a source opened this session (log rows) or is derived in section 5 (D-numbers) from such
numbers. Source tags are expanded in the Source key at the end of this section. Evidence level: **DEMONSTRATED** (measured,
flown or built), **ENGINEERING-STUDIED** (a quantitative design or study), **SPECULATIVE** (no design; thought experiment
or inference), **MODEL** (a published geophysical or geochemical model, which is the only kind of evidence that exists for
a planetary interior), **DERIVED** (this file's arithmetic).

**Plain statements for the premise, with the numbers that decide them.**

1. **About three quarters of Mercury is metal core and the first quarter is magnesium silicate.** In 1,479 best-fit
   interior models the core holds 73.9% of the mass (73.7 to 74.3%) and the crust plus mantle 26.1% (25.7 to 26.4%); the
   top of the liquid core is 377 to 430 km down (median 418 km) ([MAR18]; D2). The silicate quarter is almost iron-free
   (Fe about 1 wt%) and carries 7 to 11 wt% sulfur in the mantle ([NIT18]).
2. **Nobody has measured the bulk composition; every whole-planet number is a model.** Published and recipe-based models
   put bulk iron between about 50 and 69 wt% (1.7 to 2.3 x 10^23 kg) and bulk silicon between about 6 and 24 wt%. The
   spread is set mainly by how much silicon is dissolved in the core (0 to 25 wt%), then by the silicate fraction and the
   sulfur budget (F1; D1).
3. **The deep interior is hot, and removing the overburden would melt it.** The base of the mantle is at 1,600 to
   1,900 K and the core-mantle boundary at about 1,690 to 1,945 K ([MAR18]; [KNI25]; [MEI26]). The mantle's solidus at zero
   pressure is 1,421 K ([KNI25] citing Namur 2016b), so the lower roughly 60 to 130 km of mantle is hotter than its own
   zero-pressure melting point and would partially melt if unloaded (D3). The outer core is liquid metal at about
   1,700 to 1,950 K. **No excavation concept found addresses either fact** (F3, F4).
4. **The scales are not industrial; they are astronomical.** Taking the whole planet in 31, 100 or 1,000 years means 3.4 x
   10^14, 1.0 x 10^14 or 1.0 x 10^13 kg/s: 550 million, 170 million or 17 million times the world's entire 2024 mining
   production, and the processing energy alone (at sourced terrestrial and lunar-study rates) is 5 to 37 times Mercury's
   gravitational binding energy (D5, D6).

### F1. Bulk composition of the whole planet (checklist item 1)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Published bulk model, mass % (McDonough and Yoshizaki) | **O 18.3, Mg 11.8, Si 9.65, Fe 52.3, Ni 3.00, Al 1.16, Ca 1.25, S 2.50** (sum 99.96). Atomic Fe/Si 2.72, Fe/Al 21.8, Mg/Si 1.42; mantle Mg# ~0.99. Method: geodetic mass, density and moment of inertia; silicate:metal:sulfide **40:53:7** by mass at 3,100 / 7,100 / 4,600 kg/m^3; atomic Mg/Si and Al/Si projected from Earth and Mars; chondritic Ca/Al and Fe/Ni; S 2.5 +/- 0.5 wt% from K/Th; O by difference. "This model ... does not specify the distribution of elements between the core and mantle" | [MY20] Table 1 and Methods | Primary (preprint of Prog. Earth Planet. Sci. 8:39, 2021) | Recipe models below give lower Mg and O (Conflict K1) | Medium (one published table; its silicate fraction disagrees with geophysics) |
| Recipe for a bulk model (Nittler et al.) | Silicate shell = mean of two pre-melting mantle estimates (Table 2.2) **plus 1 wt% Fe and 7 wt% S**; core radius 2,020 km at 6,980 kg/m^3, shell 3,380 kg/m^3, planet radius 2,440 km; **core S fixed at 1.5 wt%, core Si varied 0 to 25 wt%**, optional 100 km FeS layer at the base of the mantle. The chapter plots ratios only (Fig. 2.7), no element table | [NIT18] §2.6 | Primary (review chapter) | [ES17] uses the same mantle with two cases | High as a recipe |
| Bulk from that recipe (this file) | Core Si 0%: **Fe 69.4, O 11.2, Si 6.0, Mg 5.4, Ni 3.7, S 2.9**, Al 0.56, Ca 0.53, Na 0.29 wt%. Core Si 12.8% (PRMM's value): **Fe 59.9, Si 15.4**, O 11.2, Mg 5.4, Ni 3.7, S 2.9. Core Si 25%: **Fe 50.9, Si 24.4**, O 11.2, Mg 5.4 (layer masses from [MAR18] medians; core Ni 5 wt% as assumed in [NIT18] Table 2.3) | D1 | Derived | [NIT18] geometry gives the same to within 1 wt% | Medium (the core's light elements are not measured) |
| Ebel and Stewart "case A" | Mantle 340 km thick (mean Table 2.2 mantle + 7 wt% S + 2 wt% C), FeS shell 80 km, core 2,020 km (5% Ni, 1.5% S, 0.5% C, 8% Si, rest Fe). Bulk computed here (densities assumed, see D1): **Fe 64.8, Si 10.8, O 9.4, S 4.8, Mg 4.6, Ni 3.6, C 0.8** wt%. Case B: no FeS shell, core 3% S and 4% Si. Even case B gives a "high planetary Si/Mg mass ratio" | [ES17] §18.2.3; D1 | Primary (review chapter) + derived | none | Medium-low (densities not given by the source) |
| Range across models, as masses | **Fe 1.68 to 2.29 x 10^23 kg; O 3.1 to 6.0 x 10^22; Si 2.0 to 8.1 x 10^22; Mg 1.5 to 3.9 x 10^22; Ni 0.99 to 1.22 x 10^22; S 0.83 to 1.58 x 10^22; Al 1.6 to 3.8 x 10^21; Ca 1.5 to 4.1 x 10^21**; Na about 0.8 to 1.0 x 10^21; K about 2.5 to 3.0 x 10^19; C 0 to 2.7 x 10^21 (only case A includes C); Ti about 1 x 10^20 | D1b | Derived | none | Medium for Fe (factor 1.4); low for Si (factor 4) and C |
| Core light elements (why models disagree, 1) | Core Fe ~75-95 wt%, Ni ~5 (assumed), Si >0 to 17 (geophysics), >5 (metal-rich chondrite model), >1 (core-formation experiments), C up to a few wt%, S 0-20, or <1.5 from S-solubility experiments. "The identity and abundance of that light-element component is poorly constrained"; "growing consensus ... that Mercury's core is likely Si-bearing" | [NIT18] §2.5 and Table 2.3 | Primary | [MAR18] Fig. 9: Hauck 2013 models with S 0-20 and Si 0-17 wt%; PRMM uses 12.83 wt% Si | High that the range is this wide |
| Silicate fraction (why models disagree, 2) | Geophysical shell 26.1% of mass ([MAR18]) vs 40% silicate in [MY20]'s density-matching mix; [NIT18] recipe 27.0% (2,020 km core at 6,980) | [MAR18]; [MY20]; D1 | Primary + derived | — | See Conflict K1 |
| Sulfur budget (why models disagree, 3) | Mantle 7-11 wt% S at IW-5.4 +/- 0.4 (Namur 2016b); a thin (<90 km) FeS-rich layer may sit at the core-mantle boundary "depending on Mercury's bulk S content"; [MY20] bulk S 2.5 +/- 0.5 wt% vs case A 4.8 wt% | [NIT18] §2.4-2.5; [MY20]; D1 | Primary | [MAR18]: solid FeS layer "consistent with but not required" | Medium |
| Pre-MESSENGER models | Morgan and Anders (1980) used lunar values for Mercury and assumed pyroxene FeO of 5.5 wt%; "Results from MESSENGER invalidate such assumptions." The Fegley-Cameron vaporization model (70-80% of an original silicate mantle evaporated) "is not supported by the MESSENGER results" | [ES17] §18.5.1 | Primary (review) | [ME] F1: surface FeO "no more than ~3-5 wt%, and possibly much less" | High that these older bulk tables should not be used |
| Volatiles in the bulk | Mercury is "the most volatile-rich planet (e.g., Na)" among the terrestrial planets by its silicate composition; bulk K/Th 6,000-8,000 | [NIT18] §2.6; [MY20] | Primary | [ME] F1, F5 | High (qualitative) |
| Hydrogen and nitrogen | Hydrogen: only the polar ice is known, 2.1 x 10^13 to 3 x 10^15 kg of water ([ME] F5), i.e. **2.4 x 10^12 to 3.4 x 10^14 kg of H, at most about 1 x 10^-9 of the planet's mass** (D6). **Nitrogen: no measured abundance found anywhere** (row 45) | [ME] F5; D6 | Primary (via sibling) + derived | none | High for H scarcity; nitrogen is a gap |

### F2. Layer structure, masses and the order of excavation (checklist item 2)

Listed from the surface down, which is the order an excavation reaches them.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Whole planet | Mass 3.301110 (+/-0.00015) x 10^23 kg; radius 2,439.36 km; density 5,429.30 kg/m^3; C/MR^2 0.346 +/- 0.009; Cm+cr/C 0.425 +/- 0.016 | [MAR18] Table 4 | Primary | [ME] F2 uses NSSDC 0.33010 x 10^24 kg, 2,439.7 km; C/MR^2 0.333 (Genova 2019): Conflict K2 | High |
| **Layer 1: crust** | Thickness 35-53 km adopted in [MAR18] models (density 2,700-3,100 kg/m^3); regionally 19 +/- 3 km (northern volcanic plains) to 50 +/- 12 km (high-Mg region) ([ME] F2). Mass **8.0 x 10^21 kg (2.4%)**, model range 0 to 4.7% | [MAR18] Tables 4-5; [ME] F2 | Primary | PRMM: crust 2.5% | Medium |
| Crust composition | Mg-rich silicates (forsterite, enstatite, sodic plagioclase), Fe 1-2 wt%, S 2-4, C ~1-4 (graphite; up to ~5 in low-reflectance material), Na ~3 wt% ([ME] F1). Interpreted in part as "remnants of a primary graphite-rich crust" | [ME] F1 | Primary (via sibling) | — | High |
| Regolith (top of layer 1) | 3.7 to 4.6 m median vs 25 to 40 m (disputed); bulk density not measured ([ME] F3) | [ME] F3 | — | — | Low |
| **Layer 2: mantle** | From the crust's base to the core (with crust: "the ~400 km thickness of the silicate mantle and crust"); mass **7.8 x 10^22 kg (23.6%)**, range 21.1 to 26.1%; mantle density 3,206-3,593 kg/m^3 (median 3,334); crust+mantle mean 3,286 kg/m^3 | [MAR18] Table 5, §11.1 | Primary (model ensemble) | PRMM mantle 23.5% | High |
| Mantle composition (pre-melting estimates) | NSP source: SiO2 53.67, TiO2 0.24, Al2O3 4.57, FeO 0.02, MgO 36.89, CaO 2.26, Na2O 1.97, K2O 0.05 wt%. IcP-HCT source: 51.98, 0.21, 4.24, 0.03, 37.64, 3.84, 1.29, 0.04. Residue 45 wt% forsterite, 55 wt% enstatite. **Plus 7-11 wt% S not included in these oxides.** As elements (mean, before S): O 46.6, Si 24.8, Mg 22.6, Al 2.3, Ca 2.2, Na 1.2, Ti 0.14, K 0.04, Fe 0.02 wt% (D1) | [NIT18] Table 2.2, §2.4 | Primary (petrologic models from MESSENGER lavas) | Close to the silicate of E and CB chondrites with 20% of SiO2 reduced into the core | Medium ("these mantle estimates are highly uncertain, especially for minor elements") |
| **Layer 2b (possible): FeS-rich layer at the core-mantle boundary** | Solid or molten FeS-rich layer **< 90 km thick** (Namur 2016b), modeled at 80-100 km in some bulk cases; its existence depends on the bulk S content; Knibbe and van Westrenen (2015) question whether solid FeS can float there. **If present, it is the first iron-rich material an excavation reaches**, at roughly 330-420 km depth; FeS is 63.5 wt% Fe (from atomic weights) | [NIT18] §2.5-2.6; [MAR18] §7.4; [ES17] | Primary | — | Low (existence unresolved) |
| Depth to the liquid core | **377 to 430 km (median 418 km)** in [MAR18]'s ensemble; "400 and 440 km beneath the surface" across published models; magnetic induction consistent with 400-440 km; Genova 2019 radii (1,967-1,985 km) give 454-472 km ([ME] F2) | [MAR18] §7.4 and Table 5; D2 | Primary | [ME] F2: 420-470 km | High (about 400-470 km) |
| Volume and mass to remove to reach the core | **2.62 x 10^10 km^3** (median core radius) to 2.89 x 10^10 km^3 (Genova's 1,967 km); **8.6 x 10^22 kg**, i.e. 26% of the planet; the core is 52-57% of the volume | D2 | Derived | — | High |
| **Layer 3: liquid outer core** | Outer radius 2,009-2,063 km (median 2,021 km; PRMM 2,015 km); outer-core density median 7,010 kg/m^3; mass median 2.35 x 10^23 kg; PRMM outer core 73.4% of the planet | [MAR18] Table 5 | Primary | [ME] F2: 1,967-2,020 km | High |
| Top-of-core stratification | Thermal evolution models have the CMB heat flux below the core adiabat, so "the top of the liquid core [becomes] thermally stratified"; present-day dynamo requires a convecting layer beneath a stratified one; [KNI25] present-day models: stratified layer down to 1,365-1,661 km radius | [TP19] §5.1; [KNI25] Table 2 | Primary | [MAR18] | Medium |
| **Layer 4: solid inner core** | Radius poorly known: [MAR18] ensemble 0 to 1,791 km (median 623 km; "inner core properties are unknown"; PRMM illustrative 369 km, 0.5% of mass); [KNI25] present-day thermal models 896 to 1,491 km; Genova 2019 ratio 0.3-0.7 of the core ([ME] F2) | [MAR18] Table 5; [KNI25] Table 2 | Primary | each other | Low |
| Pressures | **Core-mantle boundary 5.29 GPa; center 35.77 GPa** (PRMM); [NIT18]: CMB ~5.5 GPa (Hauck 2013); overburden near the base of the mantle by rho g z ~5.1 GPa (D3) | [MAR18] §10; [NIT18] §2.5; D3 | Primary | each other | High |
| Temperatures with depth | Surface boundary condition 440 K (model mean); base of mantle 1,600-1,900 K (Rivoldini 2013, Tosi 2013 via [MAR18]); PRMM core-mantle boundary 1,945 K; [KNI25] present-day CMB 1,690-1,923 K, center 2,019-2,224 K; [MEI26] thermal models: CMB ~1,800 K. A linear interpolation between 440 K and the basal value gives a mean gradient of **2.9 to 3.7 K/km** (D3; the real profile is not linear) | [MAR18] §8.3, Table 6; [KNI25] Table 2; [MEI26] §2 | Primary (models) | three independent model sets agree within ~250 K | Medium |
| What the first ~26% of the mass is | Crust (2.4%) and mantle (23.6%): a **forsterite-enstatite rock with sodic plagioclase in the crust, almost free of iron, rich in sulfur**: shell composition (N18 recipe) O 42.9, Si 22.8, Mg 20.8, S 7.0, Al 2.2, Ca 2.0, Na 1.1, Fe 1.0, Ti 0.12, K 0.03 wt%, i.e. about 3.7 x 10^22 kg O, 2.0 x 10^22 kg Si, 1.8 x 10^22 kg Mg, 5.5-8.6 x 10^21 kg S (at 7-11 wt% in the mantle), 1.9 x 10^21 kg Al, 0.9 x 10^21 kg Fe | D1, D2 | Derived | — | Medium |
| What the core is | Iron-nickel alloy with dissolved Si (0-25 wt%), some S (0-20, possibly <1.5) and possibly C: **1.8 to 2.3 x 10^23 kg of Fe+Ni** at 75-95 wt% (D1b). Already reduced metal; liquid in its outer part | [NIT18] Table 2.3; D1b | Primary + derived | — | Medium |

### F3. Physical state of the interior and its response to unloading (checklist item 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Outer core is liquid | "Mercury's core is not solid but rather at least the outer part is molten (Margot et al., 2007)"; a light-element component is required to keep it liquid. **DEMONSTRATED** (Earth-based and MESSENGER observations: librations, geodesy, tidal Love number k2 = 0.455 +/- 0.012) | [NIT18] §2.5; [MAR18] Table 4, §8 | Primary | [MAR18]: the tidal response "confirm[s] the presence of a molten outer core" | High |
| Magnetic dynamo | Present field weak, axisymmetric, dipolar, magnetic equator offset north by ~20% of the planet's radius; crustal magnetization shows a field active at least until 3.7 Ga; "a conclusive dynamo theory for Mercury ... [is] yet to be established"; favored models have a stably stratified layer at the top of the core | [TP19] §5.1 | Primary (review) | Surface field 0.0025-0.007 G ([ME] F7) | High (observations); low (mechanism) |
| Present-day heat flow out of the core | **570 to 781 GW** (11.2 to 15.4 mW/m^2 at the CMB) in seven present-day thermal-evolution scenarios; core adiabatic flux band 12-19 mW/m^2 | [KNI25] Table 2; [TP19] Fig. 6 | Primary (model) | each other | Medium |
| Present-day surface heat flow | **About 14 to 17 mW/m^2 (1.0 to 1.2 TW)** from CMB flow plus radiogenic heating of the shell (464 GW at [KNI25]'s K, Th, U contents), excluding secular cooling, so a lower bound (D4). No present-day surface value was found stated in an opened source (rows 9-13, 57) | D4 | Derived | Ancient (scarp-age) values of 18-50 mW/m^2 appeared only in search summaries (row 11, not used) | Low-medium |
| Mantle convection | "Most of the models predict mantle convection to cease after 3-4 Gyr"; [KNI25]: "Convection in the thin mantle may even have entirely stopped" | row 57 (Tosi 2013 abstract); [KNI25] abstract | Primary | [MAR18] §11.1 | Medium |
| Mantle solidus | **Tsol(P) = 1,421 K + 177 K/GPa x P - 12.2 K/GPa^2 x P^2** (Namur 2016b): 1,421 K at 0 GPa, 1,547 K at 0.75 GPa, 1,726 K at 2 GPa, 2,016 K at 5.29 GPa (D3); Mercury lavas' liquidus ~1,320-1,360 C | [KNI25] eq. 9 citing Namur 2016b; [MCC17] | Primary | [MAR18]: basal temperatures above ~1,900 K "would result in partial melting at the base of the mantle" | Medium-high |
| Melting behavior on decompression | "For Mercury lavas the melting rate is about 10 wt% per GPa change in pressure"; melts segregate at ~0.75 GPa (~60 km); high-Mg lavas began melting at the core-mantle boundary (~400 km), northern-plains lavas at ~200 km; adiabat 0.3 K/km | [NIT18] §2.4 (Namur 2016a) | Primary | none | Medium |
| **What happens as overburden is removed (mantle)** | Rock at 1,600 to 1,900 K at the base of the mantle crosses its own solidus when its confining pressure falls to **1.1 to 3.6 GPa**; on the linear profile, everything below about **270 to 340 km** is hotter than the zero-pressure solidus. At ~10 wt%/GPa that is of order **10 to 36 wt% melt** if fully unloaded (D3). **This is an inference from sourced inputs, not a published model of excavation**, and the melt-rate figure was derived for adiabatic ascent | D3 from [KNI25], [MAR18], [NIT18] | Derived | Analogs below show unloading melts mantle in nature | Low-medium (order of magnitude) |
| Unloading analog 1 (Earth, DEMONSTRATED in the geologic record) | Removal of ~2 km of ice from Iceland over ~1,000 years coincided with eruption rates **about 30 times** the steady value (10,000-8,000 years ago); modeled as decompression melting | [JM96] | Primary (abstract) | none opened | Medium |
| Unloading analog 2 (impact, MODEL) | A 300 km-radius crater in 75 km lithosphere "can create 10^6 km^3 of magma from instantaneous in situ decompression" (mantle potential temperature 1,300 C) | [ETH05] | Primary (abstract) | Analog 3 | Medium |
| Unloading analog 3 (Mercury, MODEL) | The Caloris impact (survey energies 8 x 10^26 to 1 x 10^29 J; impactors 1.1-9.0 x 10^19 kg) **thinned the mantle under the basin from ~470 to ~330 km and raised the core surface ~120 km**; it did not expose the core | [MEI26] §3.1, §3.2 | Primary (preprint, submitted to ApJ) | none | Medium-low (one simulation family) |
| Outgassing from processed or exposed melt | In graphite-bearing low-FeO melt in vacuum, 2C + SiO2 -> 2CO + Si(metal) proceeds unless CO pressure exceeds ~100 mbar near the liquidus: Mercury lavas are thought to have "smelted" themselves; surface O/Si 1.2 +/- 0.1 (oxygen deficit); model surfaces carry 12.6-17.9 wt% metallic Fe-Si | [MCC17]; [NIT18] §2.3.3 | Primary (abstract) | [ME] F1 (O/Si, "industrial smelting") | Medium. **Implication (inference):** decompression melts of the S- and C-bearing mantle would release CO and sulfur species into vacuum |
| **What the unconfined core would do** | When the mantle is gone, the top of the core goes from 5.29 GPa to vacuum. Liquid Fe has a vapor pressure of **3.4 Pa at 1,808 K, 11 Pa at 1,900 K, 37 Pa at 2,000 K** ([ALC84]); maximum free evaporation 2.6 to 27 g/m^2/s; a black surface at 1,900 K radiates 0.74 MW/m^2 (D4). The exposed surface would therefore skin over with solid metal by radiation (inference) | D4 from [ALC84], [KNI25] | Derived | none | Medium for the numbers; the behavior is inference |
| Core heat content | **3.6 to 4.7 x 10^29 J** to cool the core from its present temperatures to 300 K including latent heat (c = 840 J/kg/K, L = 300 kJ/kg); **20 to 26% of Mercury's binding energy**; radiating from a fully molten surface at 1,900 K it would take at least ~340 years (D4, D7) | D4, D7 from [KNI25], [MAR18] | Derived | none | Medium |
| The bare core's own gravity | Core alone: surface gravity **3.99 m/s^2 (higher than Mercury's 3.70 today)**, escape 4.02 km/s (8.1 MJ/kg); uniform-sphere central pressure 28 GPa (D8). The inner core therefore stays compressed when the mantle is removed; only the outer parts of the core decompress fully. Center temperatures of 2,019-2,224 K ([KNI25]) exceed liquid iron's 1-atm melting point (1,808 K, [ALC84]), so **the inner core would melt as the core itself is excavated down to it** (inference) | D8 | Derived | none | Medium (uniform-sphere approximation) |

### F4. Excavation: hardware anchors, published concepts and the required rates (checklist item 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| World mining production, 2024 | **19,442,935,209 t** of recoverable content (not run-of-mine ore), of which mineral fuels 16.8 Gt, iron and ferro-alloy metals 1.64 Gt; excludes bauxite and construction minerals. 1984: 9.33 Gt. **DEMONSTRATED** | [WMD26] §3, Table 6.1.1, 6.1.6 | Primary (government dataset) | [IRP24] | High |
| World material extraction, all kinds | "growth in resource use since 1970 from 30 to **106 billion metric tons**" (biomass, fossil fuels, metal ores, non-metallic minerals) | [IRP24] | Primary (UN panel release) | Press coverage (rows 21, 23) | High |
| World tailings | "an estimated **13 billion metric tons** of tailings are generated at mine sites each year" | [ICMM25] | Primary (industry body report) | 8.85-14.4 Gt/yr in summaries, not opened (row 48) | Medium |
| Largest excavator | Bagger 293 (TAKRAF, 1995): **14,196 t**, "capable of shifting **240,000 m^3** ... of earth per day", 220 m long | [GWR] | Secondary (record body) | Wikipedia (not used) | Medium |
| Largest haul truck class | Cat 797F: nominal payload **363 t**, 2,983 kW, heaped body 240-267 m^3, 67.6 km/h loaded | [CAT797] | Primary (manufacturer) | none | High |
| Deepest open pit | Bingham Canyon "more than 1.2 km deep" and "approximately four kilometers wide"; next Chuquicamata >850 m; most of the ten deepest 430-645 m (2013) | [MT13] | Secondary (trade press) | Rio Tinto page: mining since 1903, no dimensions | Medium |
| Deepest mine | Mponeng, mining at **3,160-3,740 m** below surface, "the deepest mine in the world" | [HAR] | Primary (operator) | Mining Technology (row 36) | High |
| Deepest borehole | Kola SG-3, 12,262 m (1989), ~180 C at bottom | row 35 (popular pages) | Secondary only | none primary | Low (scale only) |
| **Published planetary-scale excavation concept** | Only whole-planet disassembly: Armstrong and Sandberg's 31-year exponential case (SPECULATIVE; built on a "30% silicate and 70% metal" bulk; [ME] F9, owned by section 1 of this tranche). One self-published 2026 report ([MD26]) proposes 3.5-5 years with a 1,000 t self-replicating seed and an endgame of **3.4 x 10^15 kg/s** through 80,000 mass-driver tubes, 20-50 m mined "chunks", vertical conveyors to a fixed shell, and the remnant "fragmented and launched in bulk". **Neither treats the molten core, decompression melting, or the 26% silicate overburden as a distinct engineering problem** (row 39 text search) | [ME] F9; [MD26] | Primary (via sibling) / **non-peer-reviewed** | none | SPECULATIVE |
| Impactor or explosive stripping | No engineering study found. The natural benchmark: the Caloris basin (1,525 x 1,315 km) took 8 x 10^26 to 1 x 10^29 J, i.e. **0.05 to 6% of the binding energy**, and did not reach the core (F3; D7) | [MEI26]; D7 | Primary (model) + derived | none | Low as an excavation method |
| Required rates, 31 / 100 / 1,000 years (whole planet, constant rate) | **3.37 x 10^14 / 1.05 x 10^14 / 1.05 x 10^13 kg/s**; **5.5 x 10^8 / 1.7 x 10^8 / 1.7 x 10^7 times world mining production 2024**; 1.0 x 10^8 / 3.1 x 10^7 / 3.1 x 10^6 times all world material extraction (D5) | D5 | Derived | [MD26] endgame 3.4 x 10^15 kg/s (10 times the 31-year mean) | High (arithmetic) |
| Machines | **3.7 x 10^10 / 1.15 x 10^10 / 1.15 x 10^9 Bagger-293 equivalents** working every day of the year (at 3,286 kg/m^3); their mass 5.3 x 10^17 / 1.6 x 10^17 / 1.6 x 10^16 kg (1.6 x 10^-6 to 4.9 x 10^-8 of Mercury); 9.3 x 10^8 / 2.9 x 10^8 / 2.9 x 10^7 797F loads **per second** (D5, D7). Machine count is not the binding limit; energy and heat are (F5, D6) | D5, D7 | Derived | none | High (arithmetic) |
| Depth reached per year | Stripping evenly over the whole surface: first-year depth **43 / 13 / 1.3 km**; the silicate shell is gone after **8.1 / 26 / 261 years** (mean descent 52 / 16 / 1.6 km per year). If only the shell is taken in the stated time: 13.5 / 4.2 / 0.42 km per year (D5) | D5 | Derived | Earth's deepest mine 3.7 km, deepest borehole 12.3 km, in total | High (arithmetic) |
| Area stripped per year | At a 10 km strip depth: 4.3 / 1.3 / 0.13 times Mercury's entire surface per year; at 1 km, 43 / 13 / 1.3 times (D5). **Any of these cases is planet-wide, not a mine** | D5 | Derived | — | High |
| At today's world rate | Mercury's mass at 2024 world mining production: 1.7 x 10^10 years; the silicate shell alone 4.4 x 10^9 years (D5) | D5 | Derived | — | High |

### F5. Processing the output at planetary throughput (checklist item 5)

Process energies are in sibling `space_processing_and_fabrication.md` [PR] §5 and `mercury_as_industrial_site.md` [ME] F10 and
are cited, not re-derived.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Energy per kg, cited chains | Water electrolysis ~7.75 kWh/kg O2 (DEMONSTRATED); Alcoa chloride cell 9 kWh/kg Al (cell only); SP-413 aluminum refinery ~18.7 kWh(e) + 12.3 kWh(th) per kg Al; molten regolith electrolysis plant ~56 kWh/kg of total product (~114 kWh/kg O2); carbothermal ~34 kWh(th)/kg O2; terrestrial silicothermic magnesium 8.1-13 kWh(th)/kg Mg (reduction stage only) | [PR] §5; [ME] F10, D9 | Primary (via siblings) | — | Medium (none is a Mercury process) |
| Whole-planet processing energy | At 8.1 / 18.7 / 56 kWh/kg: **9.6 x 10^30 / 2.2 x 10^31 / 6.7 x 10^31 J**, i.e. **5.4 / 12 / 37 times the binding energy (1.79 x 10^30 J)**. Even a notional 1 kWh/kg (3.6 MJ/kg) gives 1.2 x 10^30 J, 0.7 times the binding energy (D6) | D6 | Derived | — | Medium (assumes the cited rates apply to every kilogram) |
| Power implied | Lifting energy alone over 31 / 100 / 1,000 years: **1.8 x 10^21 / 5.7 x 10^20 / 5.7 x 10^19 W, i.e. 10,800 / 3,300 / 330 times all the sunlight Mercury intercepts (1.70 x 10^17 W)**. With processing at 8.1 kWh/kg: 1.2 x 10^22 / 3.6 x 10^21 / 3.6 x 10^20 W = 3.0 x 10^-5 / 9.5 x 10^-6 / 9.5 x 10^-7 of the Sun's luminosity (D6) | D6 | Derived | [MD26] reaches the same conclusion qualitatively (Mercury's own sunlight saturates "in roughly the low-30s doublings") | High (arithmetic) |
| Waste heat | Rejecting that power at 300 K (emittance 0.9, 413 W/m^2, [ME] F11) needs radiator areas of **10^3 to 10^6 times Mercury's surface** depending on the case (D6). At 8.1 kWh/kg: 3.8 x 10^5 (31 yr), 1.2 x 10^5 (100 yr), 1.2 x 10^4 (1,000 yr) Mercury surfaces | D6; [ME] F11 | Derived | — | High (physics); the conclusion is that heat must be rejected far from the planet or at much higher temperature |
| Separating the shell | Shell rock is ~99% silicate and sulfide with ~1 wt% Fe; metal grains, if any, are magnetic and need liberation by fine crushing; troilite follows metal only by intergrowth ([PR] 1b). Melting it in vacuum with its own graphite self-reduces SiO2 to Si metal plus CO unless CO is held above ~100 mbar ([MCC17]) | [PR] 1b; [MCC17] | Primary | [ME] F10 (vacuum pyrolysis vaporizes simulant fully at 1,400 C) | Medium |
| Sulfur at planetary scale | Mantle S 7-11 wt% = **5.5 to 8.6 x 10^21 kg** of sulfur in the mantle alone (D1). Any thermal process releases sulfur species ([ME] F10); at Mercury's fO2 sulfur partitions into silicate, not metal | D1; [NIT18] §2.4-2.5; [ME] F10 | Derived + primary | — | Medium. **No processing study of high-sulfur rock found** ([ME] Open threads) |
| Core metal | Fe-Ni-Si(-S-C) alloy, already metallic: **the reduction step that dominates lunar oxygen and metal chains ([PR] 1a, 5) is not needed for core metal** (inference); what remains is handling and refining a liquid or hot solid alloy with 0-25 wt% Si. Melting and casting of metal is industrial practice; no study of handling planetary-scale liquid metal exists | [NIT18] Table 2.3; [PR] | Inference | none | Low (no study) |
| Tailings and waste | On Earth, 13 Gt/yr of tailings ([ICMM25]) against 19.4 Gt/yr of recoverable mineral content ([WMD26]). At the 31 / 100 / 1,000-year rates the material flow is 8.2 x 10^8 / 2.5 x 10^8 / 2.5 x 10^7 times Earth's tailings (D5). If the planet itself is consumed, no "back-fill" exists: what is not product must be stored in orbit, returned to the shrinking remnant, or used as unprocessed mass such as shielding ([PR] 1e). **No study of planetary-scale tailings disposal found** | [ICMM25]; [WMD26]; D5 | Primary + derived | — | Low (no study) |

### F6. What the material is good for, layer by layer (checklist item 6)

| Layer | What it supplies in quantity | What it has little or none of | Source |
|---|---|---|---|
| Regolith and crust (0 to ~35-50 km; 2.4% of mass) | Mg-rich silicates and plagioclase for sintered blocks, glass, ceramics and refractories ([PR] 1d); O, Si, Mg, Al (~6.7 wt%), Ca, Na; graphite carbon ~1-4 wt% as reductant; S 2-4 wt%; unprocessed mass for shielding | Fe 1-2 wt% (by-product only); Ti ~0.3, Cr and Mn each <1 wt%; K 0.13 wt% | [ME] F1, F10; [PR] 1d, 1e |
| Mantle (to ~400-470 km; 23.6%) | Forsterite and enstatite: Mg 22.6, Si 24.8, O 46.6 wt% before S; magnesia and forsterite refractories; sulfur 7-11 wt%; total 1.8 x 10^22 kg Mg, 2.0 x 10^22 kg Si | Al only ~2.3 wt% (less than the crust), Fe ~0.02 wt% as FeO, Ca 2-3, Na 1-1.5 wt% | [NIT18] Table 2.2; D1 |
| Possible FeS layer (<90 km) | Iron sulfide: 63.5 wt% Fe, 36.5 wt% S | — | [NIT18] §2.5; D1 |
| Liquid outer core and solid inner core (73.9%) | Iron and nickel, 1.8-2.3 x 10^23 kg; silicon in the alloy (ferrosilicon composition at 10-25 wt% Si); possibly carbon (up to a few wt%) and sulfur | Oxygen (a body of Mercury's size "would not be predicted" to have significant O in the core); lithophile metals (Al, Mg, Ca) | [NIT18] §2.5, Table 2.3 |
| Polar cold traps | Water ice 2.1 x 10^13 to 3 x 10^15 kg; possible sulfur and organics in the dark cover layer | — | [ME] F5 |
| **Whole planet: what Mercury has too little of** | — | **Hydrogen** (only the polar ice; at most ~3 x 10^14 kg H, ~1 x 10^-9 of the planet); **nitrogen** (no measured abundance at all); noble gases (no data found); carbon beyond the crust (only modeled: 0.5 wt% core and 2 wt% mantle in case A; none in other models) | F1; D6 |

### F7. Surface features that matter to operations (checklist item 7; only what is new beyond [ME])

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Polar volatile deposits, high-Mg region, thermal environment | Cited, not repeated: [ME] F1 (terranes), F2 (crust 19-50 km), F4 (88-day day and night, 100 K cold traps, 82% best-lit polar point), F5 (ice) | [ME] | — | — | — |
| Caloris basin size | Rim-to-rim ~1,550 km (Murchie 2008); best-fit ellipse **1,525 x 1,315 km**, area-equivalent diameter ~1,420 km (Fassett 2009); candidate rings to ~3,700 km | [MEI26] §3.1.3 | Primary (preprint citing primaries) | search summaries (row 46) | High |
| Mantle under Caloris | Model: mantle column under the basin center thinned from ~470 km to **~330 km**, core surface raised ~120 km; positive gravity anomaly (~100 mGal mascon) consistent with mantle uplift | [MEI26] §3.2 | Primary (preprint) | none | Medium-low. **If the model is right, the shortest overburden to the core is under Caloris** (inference) |
| Shallow crust regions | Northern volcanic plains crust 19 +/- 3 km vs 50 +/- 12 km in the high-Mg region ([ME] F2); the high-Mg region has the highest surface Fe/Si but the thickest crust | [ME] F2 | Primary (via sibling) | [ME] Conflict K3 | Medium |
| Where the deep rock is hottest | Thermal models put the high CMB heat flux at the cold poles and low flux under the hot equatorial longitudes (Tosi 2015, from the 3:2 resonance insolation pattern) | [TP19] §5.1 | Primary (review) | [MD26] tidal-lock proposal (not used) | Low-medium |

### Source key

- **[MAR18]** Margot, Hauck, Mazarico, Padovan, Peale, "Mercury's Internal Structure", ch. 4 of *Mercury: The View after MESSENGER* (Cambridge, 2018), arXiv 1806.02024 (June 2018). Primary.
- **[NIT18]** Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", ch. 2 of the same book, arXiv 1712.02187 (Dec 2017). Primary.
- **[ES17]** Ebel and Stewart, "The Elusive Origin of Mercury", ch. 18 of the same book, arXiv 1712.08234 (Dec 2017). Primary.
- **[MY20]** McDonough and Yoshizaki, "Accretion disk's magnetic field controlled the composition of the terrestrial planets", arXiv 2009.04311 (Sept 2020); published as "Terrestrial planet compositions controlled by accretion disk magnetic field", Prog. Earth Planet. Sci. 8:39 (2021). Primary (preprint read).
- **[KNI25]** Knibbe, Rivoldini, Zhao, Van Hoolst, "On the thermal evolution and magnetic field generation of planet Mercury", Phys. Earth Planet. Inter. 363:107348 (2025), publi2-as.oma.be record 7922. Primary.
- **[TP19]** Tosi and Padovan, "Mercury, Moon, Mars: Surface expressions of mantle convection and interior evolution of stagnant-lid bodies", AGU Monograph (2020), arXiv 1912.05207 (Dec 2019). Primary (review).
- **[MEI26]** Meier, Reinhardt, Jutzi, Stadel, "Three-dimensional SPH simulations of the Caloris basin-forming impact", arXiv 2608.26957 (27 Aug 2026, submitted to ApJ). Primary (preprint).
- **[MCC17]** McCubbin, Vander Kaaden, Peplowski et al., "Oxygen Depletion on the Surface of Mercury: Evidence of Silicon Smelting?", LPSC 48 (2017), NTRS 20170001343. Primary (abstract).
- **[JM96]** Jull and McKenzie, "The effect of deglaciation on mantle melting beneath Iceland", JGR (1996), doi 10.1029/96JB01308, abstract at EarthRef ERR 41250. Primary (abstract).
- **[ETH05]** Elkins-Tanton and Hager, "Giant meteoroid impacts can cause volcanism", EPSL 239:219-232 (2005), doi 10.1016/j.epsl.2005.07.029, abstract via geologyscience.ru repository. Primary (abstract).
- **[ALC84]** Alcock, Itkin, Horrigan, Canadian Metallurgical Quarterly 23:309 (1984), vapor-pressure table as reproduced (CRC format) at mmrc.caltech.edu. Primary (handbook table).
- **[CIAAW]** IUPAC Commission on Isotopic Abundances and Atomic Weights, standard atomic weights, ciaaw.org. Primary.
- **[WMD26]** Reichl and Schatz, *World Mining Data 2026*, Austrian Federal Ministry of Finance (bmf.gv.at, WMD2026.pdf). Primary (dataset).
- **[IRP24]** UNEP International Resource Panel, "Global Resources Outlook 2024 - Press release", resourcepanel.org (1 Mar 2024). Primary (agency).
- **[ICMM25]** International Council on Mining and Metals, *Tailings Progress Report: Implementing the Global Industry Standard* (2025), pimcore.icmm.com. Primary (industry body).
- **[GWR]** Guinness World Records, "Heaviest land vehicle" (Bagger 293). Secondary.
- **[CAT797]** Caterpillar, "Cat 797F Mining Truck Specifications" (spec sheet CM20190125-36969-04587). Primary (manufacturer).
- **[MT13]** Mining Technology, "Top ten deepest open-pit mines in the world" (26 Sep 2013). Secondary (trade press).
- **[HAR]** Harmony Gold, Mponeng operation page (harmony.co.za, FY25 figures). Primary (operator).
- **[MD26]** Mijic (GitHub RokoMijic/MercurialDyson), "Mercurial Dyson: Engineering the Rapid Disassembly of a Planet", written_report.md (commits 3-4 Apr 2026). **Secondary, non-peer-reviewed, SPECULATIVE.**
- **[ME]** sibling `mercury_as_industrial_site.md`; **[PR]** sibling `space_processing_and_fabrication.md`; **[IS]** sibling `inner_system_mining_synthesis.md`. Their own sources are listed there.

## 4. Conflicts

- **K1. Silicate fraction and bulk Mg and O.** [MY20] gives bulk Mg 11.8 and O 18.3 wt% from a 40:53:7 silicate:metal:sulfide
  mix chosen to match the *uncompressed* density with nominal phase densities (3,100 / 7,100 / 4,600 kg/m^3). The geophysical
  ensemble ([MAR18]) has the silicate shell at 26.1% of the mass, and recipe models built on it give Mg ~5.4 and O ~11.2 wt%
  (D1). Likely causes: [MY20] does not place elements in layers, assigns no Si to metal explicitly, and uses uncompressed
  densities rather than an equation of state; [MAR18] fits mass, radius and moments of inertia directly. The geophysical
  layer masses are the better-constrained quantity; [MY20]'s Mg and O are probably too high for a 26% shell.
- **K2. Moment of inertia.** [MAR18] uses C/MR^2 = 0.346 +/- 0.009; Genova 2019 (in [ME] F2) gives 0.333 +/- 0.005, which moves
  the core radius down to 1,967-1,985 km and the depth to the core to 454-472 km (vs 377-430 km here). Different obliquity
  and libration inputs. Both are carried; the depth to the core is stated as about 400 to 470 km.
- **K3. Inner core size.** [MAR18] ensemble 0-1,791 km (median 623 km; "unknown"); [KNI25] thermal models 896-1,491 km; Genova
  ratio 0.3-0.7 of the core. Geodesy barely constrains it; thermal models depend on the light-element liquidus depression.
- **K4. Core-mantle boundary temperature.** PRMM 1,945 K; [KNI25] present-day 1,690-1,923 K; [MEI26] ~1,800 K. Different
  thermal-evolution assumptions; all within ~250 K.
- **K5. Sulfur in the core.** Geophysical models allow 0-20 wt% S; S-solubility experiments (Namur 2016b) say <1.5 wt%; core
  formation experiments allow up to 20 wt% with a trade-off against Si ([NIT18] Table 2.3; [MAR18] Fig. 9). Hauck's
  best-fitting Fe-S-Si models and the experimental predictions "do not generally overlap" ([MAR18]).
- **K6. Bulk sulfur.** [MY20] 2.5 +/- 0.5 wt% (from K/Th) vs ~2.9 wt% (N18 recipe) vs 4.8 wt% (ES17 case A with an FeS layer).
  Depends on the FeS layer and the mantle's 7-11 wt% S.
- **K7. World tonnage bases.** [WMD26] 19.4 Gt counts recoverable content of mineral commodities (mostly fuels); [IRP24] 106 Gt
  counts all extracted materials including biomass and construction minerals; [ICMM25] 13 Gt counts tailings. None counts
  total rock moved including waste rock. The ratios in F4 are given against each base.

## 5. Derived figures

Script: scratch `mercury_whole_planet_inventory_and_extraction/scripts/calc_mercury_whole.py`; authoritative output
`calc_output_run4.txt` (run 1 crashed on a formatting bug before any affected number; runs 2-4 agree on every shared line).
Constants: G = 6.67430 x 10^-11, sigma = 5.670374419 x 10^-8, R = 8.314462618 (CODATA); year = 365.25 d.

- **D1. Bulk compositions.** Mean of the NSP and IcP-HCT pre-melting mantles ([NIT18] Table 2.2) converted to elements with
  [CIAAW] atomic weights: O 46.64, Si 24.82, Mg 22.59, Al 2.34, Ca 2.19, Na 1.22, Ti 0.14, K 0.04, Fe 0.02 wt%.
  N18 shell = 0.92 x that + 1% Fe + 7% S (the "add 1 wt% Fe and 7 wt% S" of §2.6 taken as shares of the shell: an
  interpretation). Core = 1.5% S, Si (0, 12.83, 25%), 5% Ni, Fe balance. With [NIT18]'s own geometry (core 2,020 km at
  6,980 kg/m^3 = 2.410 x 10^23 kg; shell 3,380 kg/m^3 = 8.897 x 10^22 kg; total 3.2996 x 10^23 kg, core 73.0%) or with
  [MAR18]'s median masses (core 2.441 x 10^23, shell 8.611 x 10^22 kg). Results in F1. ES17 case A: core 2,020 km at
  6,980; FeS shell 2,020-2,100 km at **4,600 kg/m^3 (assumed, [MY20]'s sulfide density)**; mantle 2,100-2,440 km at 3,380
  (assumed, [NIT18]) with 0.91 silicate + 7% S + 2% C: total 3.352 x 10^23 kg (1.5% above the true mass; shares used):
  core 71.9%, FeS 5.9%, mantle 22.2%. FeS = 63.5 wt% Fe.
- **D1b. Element masses** = bulk wt% x 3.30111 x 10^23 kg. Shell element masses = N18 shell composition x 8.611 x 10^22 kg:
  O 3.69 x 10^22, Si 1.97 x 10^22, Mg 1.79 x 10^22, S 6.0 x 10^21, Al 1.86 x 10^21, Ca 1.74 x 10^21, Na 9.6 x 10^20,
  Fe 8.8 x 10^20, Ti 1.1 x 10^20, K 3.0 x 10^19 kg. Mantle S at 7-11 wt% of 7.789 x 10^22 kg: 5.45-8.57 x 10^21 kg.
- **D2. Layers.** [MAR18] Table 5 medians: core 2.441 x 10^23 kg (73.9%; range 73.7-74.3%), shell 8.611 x 10^22 (26.1%),
  crust 8.02 x 10^21 (2.4%), mantle 7.789 x 10^22 (23.6%). Depth to core = 2,439.36 km - Roc = 377 to 430 km (median 418).
  Shell volume 4/3 pi (R^3 - Roc^3) = 2.621 x 10^10 km^3 (median Roc), 2.804 x 10^10 (1,985 km), 2.892 x 10^10 (1,967 km).
  Surface area 7.478 x 10^7 km^2.
- **D3. Pressure, temperature, melting.** g = GM/R^2 = 3.703 m/s^2; rho g z with 3,286 kg/m^3: 0.73 GPa at 60 km, 2.43 at 200,
  5.09 at 418 km (PRMM CMB 5.29 GPa). Namur solidus: 1,421 / 1,547 / 1,726 / 1,934 / 2,016 K at 0 / 0.75 / 2 / 4 / 5.29 GPa.
  Linear profile 440 K -> Tb at 400 km: gradient 2.90 (Tb 1,600), 3.21 (1,725), 3.52 (1,850), 3.65 K/km (1,900); depth below
  which T > 1,421 K: 338, 305, 278, 269 km. Pressure at which basal rock meets its solidus: 1.09, 1.99, 3.08, 3.60 GPa; x 10
  wt%/GPa = 11, 20, 31, 36 wt% melt if fully unloaded (order of magnitude; ignores latent-heat cooling).
- **D4. Heat.** Shell radiogenic heat = 8.611 x 10^22 kg x (400 ppm K x 3.247 x 10^-9 + 50 ppb Th x 2.8998 x 10^-5 +
  0.2016 ppb 235U x 5.765 x 10^-4 + 27.80 ppb 238U x 9.079 x 10^-5) W/kg = 464 GW ([KNI25] Table 1 values, applied to the
  whole shell). Plus CMB 570-781 GW = 1.03-1.25 TW; / 7.478 x 10^13 m^2 = 13.8-16.7 mW/m^2. Core heat to 300 K =
  2.441 x 10^23 x (840 x (T - 300) + 3.0 x 10^5) = 3.58 x 10^29 (1,690 K), 4.06 x 10^29 (1,923 K), 4.68 x 10^29 J (2,224 K).
  Fe(l) vapor pressure 10^(6.347 - 19,574/T) atm: 3.36 Pa (1,808 K), 11.2 (1,900), 36.8 (2,000), 108 Pa (2,100 K).
  Maximum evaporation flux (Hertz-Knudsen, sticking coefficient 1, standard kinetic theory) p sqrt(M/(2 pi R T)):
  2.6, 8.4, 26.9, 76.8 g/m^2/s. Blackbody sigma T^4: 606, 739, 907, 1,103 kW/m^2.
- **D5. Rates.** M/T for T = 31, 100, 1,000 yr: 1.065 x 10^22, 3.301 x 10^21, 3.301 x 10^20 kg/yr = 3.37 x 10^14, 1.05 x 10^14,
  1.05 x 10^13 kg/s. / 1.944 x 10^13 kg/yr (WMD 2024) = 5.5 x 10^8, 1.7 x 10^8, 1.7 x 10^7; / 1.06 x 10^14 (IRP) = 1.0 x 10^8,
  3.1 x 10^7, 3.1 x 10^6; / 1.3 x 10^13 (ICMM) = 8.2 x 10^8, 2.5 x 10^8, 2.5 x 10^7. Volume at 3,286 kg/m^3: 3.24 x 10^18,
  1.00 x 10^18, 1.00 x 10^17 m^3/yr; / (240,000 m^3/d x 365.25 d) = 3.70 x 10^10, 1.15 x 10^10, 1.15 x 10^9 Bagger-293-years
  per year. Shell gone after 0.261 T = 8.1, 26.1, 261 yr; 418 km / that = 51.7, 16.0, 1.60 km/yr. First-year even depth =
  volume / area = 43.3, 13.4, 1.34 km. World rate: 3.30 x 10^23 / 1.944 x 10^13 = 1.70 x 10^10 yr.
- **D6. Energy and heat.** Mercury-intercepted sunlight 9,082.7 W/m^2 x pi R^2 = 1.698 x 10^17 W (5.36 x 10^24 J/yr); solar
  luminosity 3.828 x 10^26 W ([ME] via NSSDC). Processing energy = e x 3.6 x 10^6 J/kWh x M. Mean power = (processing +
  1.79 x 10^30 J) / T. Radiator area at 300 K, emittance 0.9 = P / 413 W/m^2; / 7.478 x 10^13 m^2. Polar-ice hydrogen:
  H mass fraction of water 2 x 1.00798 / 18.015 = 11.19%.
- **D7. Extras.** Bagger-293 fleet mass = count x 1.4196 x 10^7 kg. Core radiative lower-bound time = 4.06 x 10^29 J /
  (5.134 x 10^13 m^2 x sigma x 1,900^4 = 3.79 x 10^19 W) = 339 yr. Caloris energies / binding energy = 4.5 x 10^-4 to 0.056.
- **D8. Bare core.** g = G x 2.441 x 10^23 / (2,021.3 km)^2 = 3.99 m/s^2; v_esc = 4.02 km/s (8.06 MJ/kg) vs 4.25 km/s today;
  uniform-sphere central pressure 3GM^2/(8 pi R^4) = 28.4 GPa (the same formula gives 24.5 GPa for today's Mercury against
  PRMM's 35.77, so it understates; the bare core's center stays at tens of GPa).

## 6. Constraints for any inhabitant

- **Whatever is dug first is iron-poor silicate.** The top ~400-470 km (26% of the mass) holds about 1 wt% Fe; iron in bulk
  begins only at a possible sulfide layer near the base of the mantle and at the core (F2).
- **Below roughly 270-340 km the rock is hot enough to melt if the weight above it is taken away**, and it carries 7-11 wt%
  sulfur and some carbon, so deep workings would face partial melt and CO and sulfur-gas release (F3).
- **The core is a liquid metal sea at about 1,700-1,950 K under 5 GPa**, whose exposed surface would radiate ~0.6-0.9 MW/m^2
  and evaporate iron at up to grams per square meter per second until it skins over (F3).
- **Gravity does not relax as the planet is consumed:** the bare core has stronger surface gravity (3.99 m/s^2) than
  Mercury has today; escape speed falls only from 4.25 to 4.02 km/s (D8).
- **Energy and heat set the pace, not machines.** Even the 1,000-year case needs hundreds to thousands of times the sunlight
  falling on Mercury and radiators of thousands of Mercury surfaces at room temperature; the work and its heat must be spread far
  beyond the planet (F5, D6).
- **Hydrogen and nitrogen must come from elsewhere.** Mercury's only known hydrogen is the polar ice, and it has no measured
  nitrogen (F1, F6).
- **The surface conditions in [ME] apply throughout:** 88-day equatorial days at ~700 K, 100 K polar cold traps, ~0.4-0.5
  kW/m^2 heat rejection at body temperature. **A human-shaped machine** working at a deep face would sit beside rock at
  hundreds of kelvin to above 1,400 K and would need the same shielding and cooling as on the dayside surface (F2, F3; [ME] F11).

## 7. Candidate handwaves

Flagged, not accepted. The developer decides.

- **HW-1. Whole-planet removal in decades.** 31 years needs 3.4 x 10^14 kg/s (5.5 x 10^8 times world mining) and, with any
  sourced processing energy, ~10^22 W (3 x 10^-5 of the Sun's output; 70,000 times Mercury's intercepted sunlight). The only
  sources are a speculative exponential-replication paper and a non-peer-reviewed report (F4, F5).
- **HW-2. Digging through the lower mantle as if it were cold rock.** Physics says unloaded rock at 1,600-1,900 K partially
  melts (F3). Any design that ignores melt, outgassing and the magma at the face bends this.
- **HW-3. Mining the core like an ore body.** It is liquid metal at ~1,700-1,950 K; its handling at planetary scale has no
  study (F3, F5).
- **HW-4. Processing every kilogram at a few MJ/kg or less.** All sourced chains are 8-56 kWh/kg (29-200 MJ/kg), against a
  mean binding energy of 5.4 MJ/kg (1.79 x 10^30 J / 3.30 x 10^23 kg); only unprocessed mass (shielding, bulk rock) or
  already-reduced core metal plausibly comes in below that (F5).
- **HW-5. Rejecting planetary-scale waste heat locally.** Needs 10^3-10^6 Mercury surfaces of 300 K radiator (D6).
- **HW-6. Mercury as a hydrogen or nitrogen source** (F1, F6).
- **HW-7. "Mercury is 70% iron-nickel."** True only of the core's mass share (73.9%) with 0-25 wt% Si and other light
  elements dissolved; bulk Fe is 50-69 wt% (F1).

## 8. Open threads

- **Measured bulk composition:** none exists; BepiColombo enters Mercury orbit in November 2026 (row 59) and may tighten C/MR^2,
  the core radius and the inner core. Re-search after its first interior results.
- **Morgan and Anders 1980 table:** could not be opened (rows 3-4); [ES17] states its assumptions are invalidated, so it was
  not pursued further.
- **Hauck et al. 2013 (JGR Planets), Namur et al. 2016a/b, Knibbe and van Westrenen 2015/2018, Brown and Elkins-Tanton
  2009:** cited inside the reviews read; full texts not opened. Next: arXiv or institutional repositories.
- **Present-day surface heat flux:** only derived here (13.8-16.7 mW/m^2); [KNI25] Fig. 2c plots it but was not read off.
  Next: Tosi 2013 full text; Peterson 2021.
- **Temperature profile with depth:** only boundary values found; the linear interpolation in D3 is a stand-in. Next: PRMM
  temperature table, Tosi 2015 3-D models.
- **Melt fraction on unloading:** needs a thermodynamic melting model (pMELTS-type) for Mercury mantle compositions under
  instant unloading; none found.
- **Low-pressure liquidus of Fe-Si-S alloys and their vapor pressures (Si, S):** not searched beyond pure Fe (time spent on
  the bulk models instead). Next: Fe-Si phase-diagram handbooks.
- **Nitrogen and noble gases on Mercury:** no measurement found (row 45).
- **Total rock moved on Earth per year including waste rock:** not found; only recoverable content, all materials and
  tailings.
- **Primary source for Bagger 293 capacity** (TAKRAF document) and for the Kola borehole: only secondary pages.
- **Any engineering study of planetary-scale excavation, liquid-metal handling, or tailings disposal:** none found (rows 38-39).
- **Sources found but not read:** Schandl et al. 2024 (J. Ind. Ecol., 403); UNEP GRO 2024 full report (403); Global Tailings
  Review ch. VII (HTML shell); Maclennan 2002 (HTML shell); Tosi et al. 2013 full text.

## 9. Rejected sources

- **Search-engine summary numbers not traced to an opened page:** Morgan and Anders bulk Fe "64.47 wt%" (row 3), Bagger 293
  "218,880 t/day" and "16.56 MW" (row 28), ancient heat flows 18-50 and "6-29 mW/m^2" (row 11), tailings 8.85-14.4 Gt/yr
  (row 48).
- **[MD26] as evidence of feasibility:** self-published, not peer-reviewed, assumes a "~70% iron-nickel core" without treating
  its liquid state or the silicate overburden; used only as a speculative comparator.
- **Wikipedia pages** (Bagger 293, Caloris Planitia, Kola, star lifting): leads only.
- **Morgan and Anders 1980 and Fegley-Cameron 1987 bulk models:** superseded per [ES17].
