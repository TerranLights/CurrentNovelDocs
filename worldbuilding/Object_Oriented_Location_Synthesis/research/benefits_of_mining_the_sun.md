# Benefits of "mining" the Sun: matter, energy, light, gravity and environment

## Scope

The Sun treated as a resource in every physical sense: its matter (solar wind, coronal outflow, photosphere), its light
(power, process heat, radiation pressure), its gravity well (Oberth maneuvers) and its near-Sun environment (0.05 to 0.3 AU),
plus the stellar-scale proposals (starlifting, stellar engines, antimatter). Physics and engineering only; no setting assumed.

*Written in two runs on 2026-10-11. The first run logged rows 0 to 17 and was stopped by a search limit before writing
findings. The second run (rows 18 on) re-opened or re-read every source whose numbers are used below. Sibling files are cited
by key and not re-derived: **[SL]** `starlifting_physics_and_minimum_infrastructure.md`, **[SYN]** `starlifting_synthesis.md`,
**[IMS]** `inner_system_mining_synthesis.md`, **[MO]** `moon_lagrange_and_comparables.md`, **[BE]**
`belt_jupiter_saturn_and_deep_transit.md`, **[NW]** `inner_system_logistics_network.md`, **[ME]** `mercury_as_industrial_site.md`.*

## SEARCH LOG

All searches and page opens dated 2026-10-11 (rows 71 and 72 ran within minutes of midnight, 11 to 12 October).

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| 0 | Read (sibling files, read-only): `starlifting_synthesis.md`, `inner_system_mining_synthesis.md`, `starlifting_physics_and_minimum_infrastructure.md` (sections 3 to 9), grep of `moon_lagrange_and_comparables.md` (He-3), `belt_jupiter_saturn_and_deep_transit.md` (fusion), `inner_system_logistics_network.md` (sails), `mercury_as_industrial_site.md` (concentration) | useful | Cited as [SYN], [IMS], [SL], [MO], [BE], [NW], [ME]; not re-derived |
| 1 | Search: `Genesis solar wind helium-3 helium-4 ratio measured Heber 2009 noble gases` | useful | Led to Heber et al. 2009 (GCA) |
| 2 | Page: Caltech Authors record, Heber et al., "Noble gas composition of the solar wind as collected by the Genesis mission", GCA 73:7414 (2009), https://authors.library.caltech.edu/records/g1mba-xbv04 | useful | Abstract: 3He/4He, 4He/20Ne, 20Ne/36Ar, Kr, Xe ratios |
| 3 | Search: `solar wind elemental abundances Fe/O C/O Ne/O N/O ACE SWICS slow fast wind von Steiger 2000 composition` | useful (leads) | arXiv 2201.05535 (ACE SWICS cycle variations) surfaced; Ne/O by wind type in a summary (not used until opened) |
| 4 | Search: `D-3He fusion reaction 18.3 MeV energy per kg helium-3 reactor fuel requirement GW-year` | useful (leads) | Wurzel and Hsu (arXiv 2105.10954); Helion blog; no per-kg figure in any result (died at the query for that figure; derived instead) |
| 5 | Page: arXiv abstract 2105.10954 | thin | Abstract has no numbers; PDF opened next |
| 6 | Page (curl + pdftotext): Wurzel and Hsu, "Progress toward fusion energy breakeven and gain as measured against the Lawson criterion", Phys. Plasmas 29, 062103 (2022), arXiv 2105.10954v4 | useful | App. D: D-3He 18.3 MeV; ignition triple product 5.2e22 m^-3 keV s at 68 keV, 18 times D-T; He-3 "must be bred ... or mined from the moon" |
| 7 | Search: `first D-He3 fusion reactions measured experiment net energy not achieved helium-3 fusion status 2025` | thin | No primary statement of a D-3He gain record; a news summary on a TAE He-3 supply agreement (secondary, not used) |
| 8 | Page: Helion Energy blog, "Explaining Helion's fusion fuel: D-He-3", 27 Jun 2024 | useful (secondary, company) | He-3 bred from D-D and tritium decay; no net-electricity claim |
| 9 | Search: `LLNL National Ignition Facility record fusion yield 8.6 MJ target gain 2025` | useful | LLNL annual report |
| 10 | Page: LLNL Annual Report FY2025, "National Ignition Facility", https://annual.llnl.gov/fy-2025/national-ignition-facility-2025 | useful | 8.6 MJ from 2.08 MJ laser, target gain 4.13, 7 Apr 2025; fuel not stated on the page |
| 11 | Page: https://lasers.llnl.gov/science/icf/how-icf-works | dead (at the source: 301 redirect) | Re-fetched at the redirect |
| 12 | Page: LLNL, "How ICF works", https://lmf.llnl.gov/science/icf/how-icf-works | useful | D-T fuel; 5 Dec 2022: 2.05 MJ in, 3.15 MJ out; no grid-energy figure (sought, not there) |
| 13 | Search: `Bochsler 2007 "Minor ions in the solar wind" Astronomy and Astrophysics Review abundance table O/H solar wind` | useful (leads) | BORIS (Bern) PDF link and RERO record |
| 14 | Page (curl + pdftotext): Cardenas-O'Toole and Landi, "ACE SWICS observations of solar cycle variations of the solar wind", arXiv 2201.05535v1 (14 Jan 2022) | useful | C/O about 0.7 in all wind (photosphere 0.45 to 0.55, FIP enhancement 1.3 to 1.6); slow-wind C, N, O, Ne, Fe per H drop a factor 2 to 3 at minimum; fast-wind FIP bias 1 to 1.5; slow wind from closed loops can exceed 10; alpha/proton up to about 0.05; Ne/H varies over an order of magnitude |
| 15 | Page (curl): BORIS Bern, Bochsler 2007 PDF, https://boris.unibe.ch/25386/1/159_2006_Article_2.pdf | dead (at the source: HTML returned instead of PDF) | |
| 16 | Page: RERO DOC record 321527 (Bochsler 2007) | dead (at the source: HTTP 410 Gone) | Bochsler's table remains unread (Open threads) |
| 17 | Search (extended): `Genesis mission solar wind elemental abundances relative to hydrogen Mg Fe Na Ca "bulk solar wind" fluence Jurewicz Burnett 2019` | dead (at the tool: session search limit reached; resets 23:40 local) | Re-run after the reset |
| 18 | *Second run begins (2026-10-11, about 23:42 local, after the search reset).* Re-read this file's SEARCH LOG (rows 0 to 17), the brief, the common rules and section 10 of the dispatch file; re-read the permitted sibling files' relevant sections | useful | Every number used below is read in this run, from a source opened this run or from a sibling file cited by key |
| 19 | Search (extended, re-run of row 17): `Genesis mission solar wind elemental abundances relative to hydrogen Mg Fe Na Ca "bulk solar wind" fluence Jurewicz Burnett 2019` | useful | Leads: Lodders 2020 review (arXiv 1912.00844), Reisenfeld et al. 2007 (Space Sci. Rev.), Jurewicz et al. 2020 (Mg isotopes); search summary gives Genesis Mg and Fe fluences (not used until confirmed in an opened page) |
| 20 | Page (curl + pdftotext): Lodders, K., "Solar Elemental Abundances", Oxford Research Encyclopedia of Planetary Science (2020), arXiv 1912.00844 (Nov 2019) | useful | Table 5: solar-wind abundances normalized to Mg = 100 atoms for Genesis, bulk, slow, fast and CME wind (H, He, C, N, O, Ne, Na, Mg, Al, Si, P, S, Ar, K, Ca, Cr, Mn, Fe, Ni, Kr, Xe); FIP enrichment 2 to 4 for low-FIP elements in the corona |
| 21 | Page (WebFetch): Caltech Authors record g1mba-xbv04, Heber, Wieler, Baur, Olinger, Friedmann, Burnett, "Noble gas composition of the solar wind as collected by the Genesis mission", GCA 73(24):7414-7432 (15 Dec 2009), re-opened this run | useful | 3He/4He (4.64 +/- 0.09) x 10^-4; 4He/20Ne 656 +/- 5; 20Ne/22Ne 13.78; 20Ne/36Ar 42.1; 36Ar/84Kr 2390; 84Kr/132Xe 9.5 |
| 22 | Search: `solar wind 3He/4He ratio in situ Ulysses SWICS Gloeckler Geiss measurement 4.1 x 10^-4 fast slow wind` | useful (leads) | Gloeckler and Geiss 1998 (Space Sci. Rev. 84:275); search summary gives slow 4.08e-4 and fast 3.3e-4 (not used until confirmed) |
| 23 | Pages: deepblue.lib.umich.edu record 2027.42/43785 (WebFetch); Springer DOI 10.1023/A:1005095907503 (WebFetch); deepblue bitstream PDF (curl) | dead (at the sources) | HTTP 403; Springer login redirect; PDF URL returned HTML. Semantic Scholar and OpenAlex gave the bibliographic record only (abstract elided). The fast/slow He-3 split stays unconfirmed |
| 24 | Page (curl + pdftotext): Tranquille, Marsden, Sanderson, Hofer, "A survey of 3He enhancements at 2-20 MeV/nucleon: Ulysses COSPIN/LET observations", Ann. Geophys. 21:1245 (2003) | useful (cross-check) | "solar system value of ~0.0004" for 3He/4He; impulsive flare events raise it "by up to 10^4 times" |
| 25 | Local file re-read (downloaded by the first run, row 6): Wurzel and Hsu, arXiv 2105.10954v4, App. D | useful | D + 3He -> alpha (3.6 MeV) + p (14.7 MeV), 18.3 MeV; "not abundant on earth and must be bred ... or mined from the moon"; not completely aneutronic because of D-D; ignition triple product 5.2e22 m^-3 keV s at 68 keV, 18 times D-T; Qsci records: TFTR 0.27, JET 0.64 (D-T) |
| 26 | Search: `D-3He fusion experiment measured fusion power highest achieved tokamak JET TFTR helium-3 deuterium Q value paper` | useful | JET D-3He experiments (1991) |
| 27 | Pages (WebFetch): EUROfusion scipub record p=6694 (Jacquinot, Sadler, JET Team, 1 Dec 1991) and ANS Fusion Technology 21(4), July 1992 record a_29719 | useful | D-3He: 140 kW fusion power, 4.6 x 10^16 reactions/s, Q = 1.25% at 10 MW of ICRF heating |
| 28 | Search: `Energy Institute Statistical Review of World Energy 2025 total primary energy consumption exajoules 2024` | useful (leads) | 2025 edition: 592 EJ in 2024 (search summary; not used); a 2026 edition exists |
| 29 | Page (WebFetch): DieselNet news, "Energy Institute releases 2026 Statistical Review of World Energy" (July 2026) | useful (secondary) | "total energy supply (TES) exceeded 600 EJ in 2025, a rise of 1.7% over 2024" |
| 30 | Search: `energyinst.org Statistical Review of World Energy 2026 "total energy supply" EJ 2025 highlights` | useful (leads) | EI summary PDF URL; solar 10.12 EJ in 2025 (search summary; not used) |
| 31 | Page: EI 2026 Summary PDF (curl and WebFetch) | dead (at the sources) | curl returned an HTML bot page; WebFetch HTTP 403 |
| 32 | Dataset (curl): Our World in Data grapher `primary-energy-cons` CSV and metadata (source "Energy Institute - Statistical Review of World Energy (2026)", updated 30 Jun 2026) | useful | World total energy supply 166,753.6 TWh (2025), 164,494.1 TWh (2024); traditional biomass not included |
| 33 | Search: `NASA Office of Technology Policy and Strategy Space-Based Solar Power report 2024 Rodgers levelized cost mass per watt RD1 RD2` | useful | Found the report PDF |
| 34 | Page (curl + pdftotext): NASA OTPS, Rodgers et al., "Space-Based Solar Power", report dated 11 Jan 2024 (otps-sbsp-report-final-tagged-approved-1-8-24) | useful | Two 2 GW designs: RD1 heliostat swarm 5.9 Mkg, RD2 planar array 10 Mkg; LCOE 0.61 and 1.59 $/kWh vs terrestrial 0.02-0.05; launch 71% and 77% of cost; about 13% of incident sunlight delivered; source concepts SPS-ALPHA Mk III 7,500 t for 2 GW, Tethered-SPS 20,000 t for 0.75 GW average; an internal mass inconsistency (see Conflicts) |
| 35 | Search: `NASA State-of-the-Art Small Spacecraft Technology power chapter solar array specific power W/kg ROSA flexible blanket table` | thin | Small-spacecraft array figures (LISA-T, HaWK) in a summary; not the class of array needed; not used |
| 36 | Search: `"Solar Power Technologies for Future Planetary Science Missions" JPL D-101316 specific power W/kg UltraFlex ROSA` | useful | Found the JPL report PDF; UltraFlex and ROSA vendor figures in the summary (not used) |
| 37 | Page (curl + pdftotext): JPL D-101316, "Solar Power Technologies for Future Planetary Science Missions", Dec 2017, solarsystem.nasa.gov/system/downloadable_items/715_Solar_Power_Tech_Report_FINAL.PDF | useful | Table 3-3: rigid 80 W/kg, flexible 150 W/kg, 330 to 338 W/m^2 BOL at 1 AU; cells about 30% efficient; specific power improved 30 to 100 W/kg over 25 years; targets 150-200 and 200-250 W/kg |
| 38 | Page (curl + pdftotext): Wright, J. T., "Dyson Spheres", arXiv 2006.16734v3 (7 Oct 2020; accepted by the Serbian Astronomical Journal) | useful | beta = 1 (radiation force equals gravity) at 0.8 g/m^2 = L/(4 pi G c M); Sun could unbind Jupiter in under 1,000 years of output; energy storage as mass (antimatter) mentioned as a SETI possibility, not a design |
| 39 | Search: `Interstellar Probe study APL solar Oberth maneuver perihelion heat shield evaluated compared Jupiter gravity assist au per year result` | useful (leads) | Popular pages (JHU Hub, Centauri Dreams, Universe Today); "20 au per year" claim for solar-thermal propulsion in a summary (not used) |
| 40 | Search (extended): `McNutt "Interstellar Probe" Acta Astronautica 2022 Oberth maneuver "not" favorable solar thermal propulsion 3-4 solar radii trade study escape speed` | useful (leads) | arXiv 2601.02533, 2608.11113, 2307.12411, Bailer-Jones 2009.12659; AIAA-2001-3377 (McNutt, solar thermal) |
| 41 | Page (curl + pdftotext): Hibberd, Eubanks, Hein, "Catching 3I/ATLAS Using a Solar Oberth", arXiv 2601.02533v2 (21 Jan 2026), preprint | useful | SOM at 3.2 R_sun from the Sun's center; about 6 MW/m^2 there; spacecraft up to about 500 kg; heat shield needed from payload; intercept after 35-50 years; Project Lyra SOM 7.2 km/s at 6 R_sun |
| 42 | Page (curl + pdftotext): Maraqten, van Lynden, Gomez de Olea Ballester, Hein, "High-temperature photovoltaics for solar-electric Oberth maneuvers", arXiv 2608.11113v1 (11 Aug 2026), preprint | useful | Impulsive delta-epsilon = v dv + dv^2/2; Table 1 of 17 published SOM studies (chemical, sail, laser sail, solar thermal, nuclear thermal, electric): perihelia 2-11 R_sun for impulsive, sails 20-60 au/yr at 5-11 R_sun; solar-thermal 8 to 20 au/yr with 36 to 662 kg payloads; SEP-SOM at 0.3 AU gives 3 times the orbital energy per delta-v of a 1 AU spiral; HIHT cells about 400 C in the laboratory |
| 43 | Page: KISS Caltech copy of AIAA-2001-3377 (McNutt et al., solar thermal propulsion) | dead (at the sources) | Returned an HTML page, not the PDF |
| 44 | Page (WebFetch): Centauri Dreams, "Assessing the Oberth Maneuver for Interstellar Probe" (6 Oct 2021) | useful (secondary) | Quotes McNutt: the SOM "offers no advantage over prograde gravity assists ... for a 'technology horizon' in the 2030's"; "181 staging scenarios"; heat-shield assembly mass is the problem |
| 45 | OpenAlex API: abstracts of McNutt et al., "Interstellar probe - Destination: Universe!", Acta Astronautica (2022), DOI 10.1016/j.actaastro.2022.04.001, and Brandt et al., "Interstellar Probe: Humanity's exploration of the Galaxy Begins", Acta Astronautica (2022), DOI 10.1016/j.actaastro.2022.07.011 | useful | "solar system escape speeds of at least twice that of Voyager 1 (i.e., up to 7.2 au/yr)" with SLS B2 and Jupiter gravity assist; about 7 au/yr |
| 46 | Pages: ScienceDirect PDF of McNutt 2022 (curl) and Unpaywall record | dead (at the sources) | ScienceDirect returned an HTML page; the only OA location is the publisher. The SOM verdict is therefore read only through Centauri Dreams (secondary) |
| 47 | Search: `interstellarprobe.jhuapl.edu Interstellar Probe Study Report pdf 2021 "Solar Oberth" "no advantage"` | thin | Same secondary quote; the APL study report PDF was not surfaced. Died at the query for the primary |
| 48 | Page (curl + pdftotext): Hibberd, Hein, Eubanks, Kennedy, "Project Lyra: A Mission to 1I/'Oumuamua without Solar Oberth Maneuver", arXiv 2201.04240v1 (11 Jan 2022) | useful | SOM "allows huge velocity gains" but is "technically challenging"; a Jupiter Oberth with VEEGA matches it (15.8 km/s total, 115 to 241 kg payload) and omits the scaled Parker heat shield |
| 49 | Search: `Odeillo 1 MW solar furnace PROMES CNRS maximum temperature 3500 °C concentration 10000 suns flux 10 MW/m2` | useful (leads) | 3,300-3,500 C and "10,000 times" appear in popular pages (Wikipedia, Xataka; not used) |
| 50 | Page (WebFetch): PROMES-CNRS, "Solar Concentrators", https://www.promes.cnrs.fr/?p=3895 (no date on page) | useful | 1 MW furnace: 1,830 m^2 parabola, 63 heliostats 2,835 m^2, 1 MW on about 80 cm, maximum 10 MW/m^2; furnaces "over 3000 C"; 6 kW unit concentration about 4,500; 1.5-2 kW units about 15,000 on 1 cm |
| 51 | Page: Journal de Physique IV record jp4:1999309 (WebFetch) | dead (at the sources) | HTTP 403 |
| 52 | Search: `solar furnace PSA Almeria SF60 peak flux concentration 3000 suns temperature materials testing paper` | useful (leads) | DLR PSA page |
| 53 | Page (WebFetch): DLR, "Plataforma Solar de Almeria (CIEMAT)" research-infrastructure page (read 2026-10-11; no page date) | useful | SF-60: 60 kW, 3,000 suns; SF-40: 40 kW, 7,000; SF-5: 5 kW, 6,000 suns |
| 54 | Search: `NASA planetary protection dry heat microbial reduction specification temperature 125 °C time NASA-STD-8719.27 spore lethality` | thin | Summary numbers (104-125 C for up to 50 h; D-values) not confirmed in an opened page; not used |
| 55 | Pages (WebFetch): CORE record 4480126 (HTTP 403, dead at the sources); JPL Planetary Protection, W. Schubert biography page (thin: "dry heat from 115 C to 170 C" research); PMC376991, Bond et al., "Dry-Heat Inactivation Kinetics of Naturally Occurring Spore Populations", Appl. Microbiol. (1970) (useful: spacecraft-related spore tests at 125 C) | mixed | Dry-heat sterilization temperatures of about 115 to 170 C; no D-value read in an opened page |
| 56 | Search: `"harvesting antimatter from the Sun" cycling spacecraft preprint Research Square solar flare positrons` | useful (leads) | Research Square rs-10177321; popular pages on flare positrons (not used) |
| 57 | Pages: Research Square rs-10177321 (WebFetch: title only); Springer Nature Communities post (WebFetch: sign-in page, dead at the sources); then curl of the Research Square HTML, metadata and text parsed locally | useful | Borekci, H., "A Cycling Spacecraft for Harvesting Antimatter from the Sun ... (v4)", posted 30 Jun 2026, DOI 10.21203/rs.3.rs-10177321/v1: "This is a preprint; it has not been peer reviewed by a journal"; yield "≈ 12 µg (upper bound)" over 200 dives; "research-grade (microgram scale, upper bound) rather than energy-grade"; the ambient positron flux is "uncertain and is treated here as an optimistic upper bound" |
| 58 | Search: `number of positrons produced solar flare 511 keV annihilation line RHESSI 2003 October 28 Share Murphy positron production total` | thin | No total positron number in any result; led to the Gopalswamy review. Died at the sources for a number |
| 59 | Page (curl + pdftotext): Gopalswamy, N. (NASA GSFC), "Positron Processes in the Sun", review, accepted 16 Apr 2020 (Atmosphere), arXiv 2004.04280 | useful | Core positrons from the p-p chain "are immediately annihilated"; flare positrons annihilate in the flaring atmosphere at about 3-4 x 10^5 K and densities ≳ 10^15 cm^-3 (2003 Oct 28 event) |
| 60 | OpenAlex and Semantic Scholar APIs: abstracts of Caplan, "Stellar engines: Design considerations for maximizing acceleration", Acta Astronautica (2019), DOI 10.1016/j.actaastro.2019.08.027, and Svoronos and Caplan, "Comments on ...", Acta Astronautica (2021), DOI 10.1016/j.actaastro.2020.11.030 | useful | Passive Shkadov-type sail: accelerations of order 10^-12 m/s^2; active engine (collects solar wind, lifts more, fuses He): up to 10^-9 m/s^2, 10 pc deflection in about 1 Myr; the 2021 comment corrects the passive-engine prefactor from (1/2 + 1/6)e to (3/4)e |
| 61 | Search: `solar thermal propulsion hydrogen specific impulse heat shield integrated Oberth Benkoski NIAC 2019 "solar thermal" interstellar 1000 s` | useful (leads) | NASA NIAC study page; popular pages (not used) |
| 62 | Page (WebFetch): NASA NIAC, "Combined Heat Shield and Solar Thermal Propulsion System for an Oberth Maneuver", J. Benkoski (JHU APL), Phase I, 2022 | useful | Prototypes in "materials that can survive 2800 K at a 20 x 20 cm scale"; goal "> 10 astronomical units per year"; comparison "8 AU/yr for a ~1 tonne spacecraft payload" with a Jupiter assist; propellants H2, LiH, Li, CH4, NH3, H2O; no specific impulse given |
| 63 | Search: `solar thermal propulsion hydrogen specific impulse 800 s 900 s NASA NTRS test Shooting Star experiment concentrator` | useful (leads) | Summary claims "approaching 900 seconds, with 760 seconds already demonstrated in ground testing" (not found in an opened page; not used) |
| 64 | Pages (curl + pdftotext): NTRS 20020048434, Tucker and Salvail (NASA MSFC), "Solar-Thermal Engine Testing" (no date printed on the copy; NTRS record 2002); NTRS 20010020153, Leigh, Hamidzadeh, Tinker, "Dynamic Characterization of an Inflatable Concentrator for Solar Thermal Propulsion" | useful (first); thin (second, structures only) | SSE rhenium engine, electric-heater ground test: Isp 150 s with nitrogen at 1,760 F exit, "equivalent hydrogen" about 630 s; gas "approaching 4,500 F"; cavity 3,100 F (heater-limited); thrust about 1 lbf |
| 65 | Page (curl, parsed): IUPAC CIAAW, Abridged Standard Atomic Weights, https://www.ciaaw.org/abridged-atomic-weights.htm | useful | H 1.0080, He 4.0026, C 12.011, N 14.007, O 15.999, Ne 20.180, Na 22.990, Mg 24.305, Al 26.982, Si 28.085, P 30.974, S 32.06, Ar 39.95 (terrestrial), K 39.098, Ca 40.078, Cr 51.996, Mn 54.938, Fe 55.845, Ni 58.693, Kr 83.798, Xe 131.29 |
| 66 | Pages (curl): NIST, "Atomic Weights and Isotopic Compositions" for He, H and Ar (physics.nist.gov/cgi-bin/Compositions) | useful | 3He 3.0160293201, 4He 4.00260325413, terrestrial 3He fraction 1.34 x 10^-6; D 2.01410177812; 36Ar 35.967545, 38Ar 37.962732 (solar argon is 36Ar/38Ar, not terrestrial 40Ar, so its mean mass is computed from Heber's ratio) |
| 67 | Page (curl): NIST CODATA, atomic mass constant (physics.nist.gov/cgi-bin/cuu/Value?ukg) | useful | 1.66053906892 x 10^-27 kg |
| 68 | Local file re-read (downloaded by the first run, row 14): Cardenas-O'Toole and Landi, arXiv 2201.05535v1 | useful (cross-check) | "The relative C/O abundance ratio is constant at ≈0.7 along the solar cycle"; photospheric 0.45-0.55; enhancement 1.3-1.6 |
| 69 | Page (curl + pdftotext): OSTI 1625907, Jurewicz et al., "Magnesium isotopes of the bulk solar wind from Genesis diamond-like carbon films", Meteorit. Planet. Sci. 55(2):352-375 (2020) | thin | Isotopes and method only; the Mg and Fe fluences quoted in the row-19 search summary are not in this paper's text as read; not used |
| 70 | Local Python, scratch `py/calc.py` (output `calc_out.txt`): solar-wind mass fractions (two H normalizations), per-element yield per km^2 per year at six distances, He-3 fusion energy and fuel needs, irradiance and collector areas, Oberth gains, sail pressures, furnace concentrations, stellar-engine kinematics | useful | Output pasted in Derived figures |
| 71 | Search: `Kopp Lean 2011 "A new, lower value of total solar irradiance" 1360.8 W m-2 Geophysical Research Letters` | useful | Second angle on irradiance at 1 AU |
| 72 | Page (WebFetch): NASA ESPO record 30086, Kopp, G. and Lean, J., "A new, lower value of total solar irradiance: Evidence and climate significance", GRL 38, L01706 (2011) | useful | "1360.8 ± 0.5 W m−2" at the 2008 solar minimum (SORCE/TIM) |

## Findings

**Evidence levels:** DEMONSTRATED (flown, built or measured), ENGINEERING-STUDIED (a quantitative design study),
SPECULATIVE (concept paper, thought experiment or unreviewed preprint). DERIVED marks arithmetic on sourced inputs (section 5).

**Source keys (this file):**

- **[LO20]** Lodders, K., "Solar Elemental Abundances", Oxford Research Encyclopedia of Planetary Science (2020), arXiv 1912.00844 (Nov 2019), Table 5. Peer-reviewed review.
- **[HE09]** Heber, V. S. et al., "Noble gas composition of the solar wind as collected by the Genesis mission", GCA 73(24):7414-7432 (15 Dec 2009), https://authors.library.caltech.edu/records/g1mba-xbv04. Peer-reviewed.
- **[TR03]** Tranquille, C. et al., "A survey of 3He enhancements at 2-20 MeV/nucleon: Ulysses COSPIN/LET observations", Ann. Geophys. 21:1245 (2003). Peer-reviewed.
- **[CL22]** Cardenas-O'Toole, A. and Landi, E., "ACE SWICS observations of solar cycle variations of the solar wind", arXiv 2201.05535v1 (14 Jan 2022). Preprint of a peer-reviewed paper.
- **[WH22]** Wurzel, S. E. and Hsu, S. C. (ARPA-E), "Progress toward fusion energy breakeven and gain as measured against the Lawson criterion", Phys. Plasmas 29, 062103 (2022), arXiv 2105.10954v4. Peer-reviewed.
- **[JS92]** Jacquinot, J., Sadler, G. and the JET Team, "D-3He Fusion in the Joint European Torus Tokamak: Recent Experimental Results", Fusion Technology 21(4) (July 1992); EUROfusion record dated 1 Dec 1991. Peer-reviewed (abstract read).
- **[OWID]** Our World in Data, `primary-energy-cons` dataset, from Energy Institute, Statistical Review of World Energy (2026), updated 30 Jun 2026. Dataset (secondary compilation of a primary statistical source). **[DN26]** DieselNet news on the 2026 Review (July 2026), secondary.
- **[KL11]** Kopp, G. and Lean, J., "A new, lower value of total solar irradiance", GRL 38, L01706 (2011), via NASA ESPO record 30086. Peer-reviewed.
- **[JPL17]** JPL D-101316, "Solar Power Technologies for Future Planetary Science Missions" (Dec 2017). Agency report.
- **[OTPS24]** Rodgers, E. et al., NASA Office of Technology, Policy and Strategy, "Space-Based Solar Power" (11 Jan 2024), https://www.nasa.gov/wp-content/uploads/2024/01/otps-sbsp-report-final-tagged-approved-1-8-24-tagged-v2.pdf. Agency study.
- **[WR20]** Wright, J. T., "Dyson Spheres", arXiv 2006.16734v3 (7 Oct 2020), accepted by the Serbian Astronomical Journal. Peer-reviewed review.
- **[HI26]** Hibberd, A., Eubanks, T. M., Hein, A. M., "Catching 3I/ATLAS Using a Solar Oberth", arXiv 2601.02533v2 (21 Jan 2026). Preprint.
- **[MA26]** Maraqten, N. et al., "High-temperature photovoltaics for solar-electric Oberth maneuvers", arXiv 2608.11113v1 (11 Aug 2026). Preprint; its Table 1 summarizes 17 published SOM studies.
- **[HI22]** Hibberd, A. et al., "Project Lyra: A Mission to 1I/'Oumuamua without Solar Oberth Maneuver", arXiv 2201.04240v1 (11 Jan 2022). Preprint.
- **[MC22]** McNutt, R. L. Jr. et al., "Interstellar probe - Destination: Universe!", Acta Astronautica (2022), DOI 10.1016/j.actaastro.2022.04.001 (abstract via OpenAlex). Peer-reviewed. **[BR22]** Brandt, P. C. et al., "Interstellar Probe: Humanity's exploration of the Galaxy Begins", Acta Astronautica (2022), DOI 10.1016/j.actaastro.2022.07.011 (abstract). **[CD21]** Centauri Dreams, "Assessing the Oberth Maneuver for Interstellar Probe" (6 Oct 2021), secondary, quoting McNutt.
- **[NIAC22]** NASA NIAC Phase I, Benkoski, J. (JHU APL), "Combined Heat Shield and Solar Thermal Propulsion System for an Oberth Maneuver" (2022). Agency-funded concept study.
- **[TS02]** Tucker, S. and Salvail, P. (NASA MSFC), "Solar-Thermal Engine Testing", NTRS 20020048434 (no date printed on the copy). Agency test report.
- **[PROMES]** PROMES-CNRS, "Solar Concentrators", https://www.promes.cnrs.fr/?p=3895 (no date). Research institution. **[PSA]** DLR, "Plataforma Solar de Almeria (CIEMAT)" infrastructure page (no date). Research institution.
- **[BO70]** Bond, W. W. et al., "Dry-Heat Inactivation Kinetics of Naturally Occurring Spore Populations", Appl. Microbiol. (1970), PMC376991. Peer-reviewed. **[JPLPP]** JPL Planetary Protection, W. Schubert biography page. Agency, thin.
- **[BK26]** Borekci, H., "A Cycling Spacecraft for Harvesting Antimatter from the Sun ... (v4)", Research Square, posted 30 Jun 2026, DOI 10.21203/rs.3.rs-10177321/v1. **Not peer reviewed.**
- **[GO20]** Gopalswamy, N. (NASA GSFC), "Positron Processes in the Sun", review (Atmosphere, accepted 16 Apr 2020), arXiv 2004.04280. Peer-reviewed.
- **[CA19]** Caplan, M. E., "Stellar engines: Design considerations for maximizing acceleration", Acta Astronautica (2019), DOI 10.1016/j.actaastro.2019.08.027; **[SC21]** Svoronos, A. A. and Caplan, M. E., "Comments on ...", Acta Astronautica (2021), DOI 10.1016/j.actaastro.2020.11.030. Peer-reviewed (abstracts only read).
- **[CIAAW]** IUPAC CIAAW, Abridged Standard Atomic Weights. **[NIST]** NIST Atomic Weights and Isotopic Compositions (He, H, Ar) and CODATA atomic mass constant. Primary.

### F1. Solar-wind matter: composition, isotopes, flux and yield per collector area (checklist 1)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Whole solar-wind mass loss | about 1.3 x 10^9 kg/s (4.2 x 10^16 kg/yr) | [SL] 3C, D3 (Mishra 2019, Cranmer 2017) | Primary (via sibling) | [SL] Conflict 16: 1.0 to 1.3 x 10^9 kg/s in three sources | High |
| Solar-wind elemental abundance, Genesis sample return, atoms per 100 Mg | H 1.02 x 10^6; He 4.87 x 10^4; C 383; N 69; O 723; Ne 86; Na 6.1; Mg 100; Ar 1.90; K 0.31; Mn 0.89; Fe 85; Kr 1.24 x 10^-3; Xe 2.76 x 10^-4 | [LO20] Table 5, "Genesis" column (citing Burnett 2017, Heber 2009 and 2013, Jurewicz 2011 and 2019, Reisenfeld 2013 and others) | Primary (review of measurements) | [LO20] "bulk solar wind" column (Pilleri 2015, Reisenfeld 2013): H 1.51 x 10^6, He 5.94 x 10^4, C 428, N 103, O 687, Ne 75, Si 118, S 38, Fe 88. Rock-forming elements are "preliminary" | High for Mg-normalized metals; **medium for H** (factor 1.5 between columns; see Conflicts) |
| Elements not in the Genesis column (slow-wind averages, ACE and Ulysses), per 100 Mg | Al 8.1; Si 109; P 0.95; S 39; Ca 5.5; Cr 1.4; Ni 4.4 | [LO20] Table 5, "Slow Solar Wind" column | Primary (review) | Fast-wind column: Al 7.6, Si 104, S 41, Ca 5.7, Cr 1.4 | Medium-high |
| First-ionization-potential (FIP) fractionation | Low-FIP elements (Na, K, Mg, Al, Si, Fe; FIP below 10 eV) are "2-4 times more abundant in the corona than in the photosphere" relative to high-FIP elements (H, C, N, O, noble gases); fast wind is less fractionated than slow | [LO20] pp. 30-33 | Primary | [CL22]: C/O "constant at ≈0.7 along the solar cycle" against photospheric 0.45 to 0.55; [SL] 3E (Pilleri 2015): fFIP 1.6 to 2.3 | High |
| He-3 to He-4 ratio in the solar wind | (4.64 +/- 0.09) x 10^-4 (Genesis, bulk wind) | [HE09] abstract | Primary | [TR03]: "solar system value of ~0.0004"; impulsive flare particles can be enriched "by up to 10^4 times". A fast/slow split (Ulysses) was found only in a search summary and is not used (Open threads) | High |
| Other Genesis noble-gas ratios | 4He/20Ne 656 +/- 5; 20Ne/22Ne 13.78; 20Ne/36Ar 42.1; 36Ar/38Ar 5.47; 36Ar/84Kr 2390; 84Kr/132Xe 9.5 | [HE09] | Primary | [LO20] Genesis Ne/Ar = 86/1.90 = 45 (atoms, all isotopes) | High |
| He-3 share of terrestrial helium (for comparison) | 1.34 x 10^-6 of helium atoms | [NIST] He | Primary | none needed | High. The solar wind's ratio is **about 350 times** Earth's (DERIVED, calc C3) |
| **Mass composition of the solar wind** (per tonne collected) | H 820 to 871 kg; He 112 to 155; O 6.6 to 9.2; C 2.6 to 3.7; **Fe 2.7 to 3.8**; Si 1.8 to 2.4; Mg 1.4 to 1.9; Ne 1.0 to 1.4; S 0.7 to 1.0; N 0.55 to 0.77; Ni 0.15 to 0.21; Ca 0.13 to 0.18; Al 0.13 to 0.17; Na 0.08 to 0.11; Ar 0.039 to 0.055; **He-3 0.039 to 0.054 kg**; Kr 0.06 to 0.08 g; Xe 0.021 to 0.029 g. Everything heavier than helium: 1.8 to 2.5% by mass | DERIVED (calc C1) from [LO20], [HE09], [CIAAW], [NIST] | Derived | Photosphere: Z = 1.39%, Fe 1.19 kg/t ([SL] 3B) | Medium (range spans the two H normalizations) |
| Iron-to-hydrogen enrichment of the wind over the photosphere | Fe/H by number 5.8 x 10^-5 (bulk column) to 8.3 x 10^-5 (Genesis column), against 2.88 x 10^-5 photospheric (log eps 7.46): **2.0 to 2.9 times enriched** | DERIVED from [LO20] and [SL] 3B | Derived | Consistent with FIP factor 2-4 ([LO20]) and 1.6 to 2.3 ([SL] 3E) | Medium. **This answers the open item in [SYN] section 9:** the per-area iron yields there are high by a factor of 2 to 3 for this reason alone |
| Global-mean mass flux at distance r | 4.7 x 10^-15 kg m^-2 s^-1 at 1 AU (0.148 kg per km^2 per year), scaling as 1/r^2: 1.0 kg/km^2/yr at 0.387 AU (Mercury), 14.8 at 0.1 AU, 68.5 at 0.0465 AU | DERIVED (calc C2) = whole-wind loss / (4 pi r^2) | Derived | [SL] D3 used the slow-wind proton flux, 3.1 x 10^-15 at 1 AU; the global mean is 1.52 times higher (helium, fast wind and averaging) | Medium (the in-ecliptic flux varies by a factor of a few with wind type) |
| Yield per km^2 of intercepting area per year, by element | At 1 AU: H 0.12 to 0.13 kg; He 17 to 23 g; O 1.0 to 1.4 g; Fe 0.40 to 0.56 g; Ne 0.15 to 0.21 g; Ar 5.8 to 8.1 mg; He-3 5.8 to 8.1 mg; Xe 3.1 to 4.3 micrograms. Multiply by 100 at 0.1 AU, by 462 at 0.0465 AU | DERIVED (calc C2) | Derived | none | Medium |
| Collector area for **1 tonne per year** of each product | **at 0.1 AU**: H 78 to 82 km^2; He 430 to 610 km^2; O 7,300 to 10,000 km^2; C 18,000 to 26,000 km^2; Fe 18,000 to 25,000 km^2; N 88,000 to 122,000 km^2; Ne 49,000 to 68,000 km^2; Ar 1.2 to 1.7 million km^2; He-3 1.2 to 1.7 million km^2; Xe 2.3 to 3.3 billion km^2. **At 1 AU**: 100 times larger (H 7,800 to 8,200 km^2). At Mercury's mean distance: 6.7 times smaller than at 1 AU | DERIVED (calc C2) | Derived | [SL] 3C: 10,240 km^2 per tonne of wind at 1 AU (proton-only basis) | Medium (geometry high; assumes complete capture, which no device does: [SL] 3E) |
| Whole-wind totals per year, by element | H 3.4 to 3.6 x 10^16 kg; He 4.6 to 6.5 x 10^15; O 2.8 to 3.8 x 10^14; C 1.1 to 1.5 x 10^14; Fe 1.1 to 1.6 x 10^14; Ne 4.1 to 5.8 x 10^13; N 2.3 to 3.2 x 10^13; Ar 1.6 to 2.3 x 10^12; **He-3 1.6 to 2.3 x 10^12 kg**; Xe 0.9 to 1.2 x 10^9 kg | DERIVED (calc C2) | Derived | none | Medium. These are what the Sun releases into the whole sky, not what any collector could take |
| Making water from wind matter | Wind oxygen-to-hydrogen mass ratio 0.008 to 0.011; water needs 7.94 kg O per kg H. **Only 0.10 to 0.14% of the wind's hydrogen can be paired with the wind's own oxygen.** Hydrogen for one tonne of water per year (112 kg): about 9 km^2 of capture area at 0.1 AU, about 900 km^2 at 1 AU, with all the oxygen supplied from elsewhere | DERIVED from F1 rows and [CIAAW] | Derived | none | Medium-high (stoichiometry; capture assumed) |
| Which wind products are worth collecting, on these numbers | Hydrogen and helium (98% of the mass) at tens to hundreds of km^2 per tonne-year near 0.1 AU; everything else needs 10^4 to 10^9 km^2 per tonne-year. No device that captures and stores wind ions has been designed ([SL] 3E). Genesis returned about 0.46 mg of hydrogen from 1.67 m^2 in 853 days ([SL] D4) | [SL], DERIVED | Mixed | none | High that only H and He are even area-plausible; DEMONSTRATED at the milligram scale only |

### F2. Helium-3 and fusion fuel (checklist 2)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| D-3He reaction | D + 3He -> alpha (3.6 MeV) + p (14.7 MeV), 18.3 MeV; "not completely aneutronic because of D-D reactions" | [WH22] App. D | Primary | [JS92]: 140 kW / 4.6 x 10^16 reactions/s = 19.0 MeV per reaction (DERIVED; within 4%) | High |
| Ignition requirement, D-3He vs D-T | ni T tauE >= 5.2 x 10^22 m^-3 keV s at 68 keV, **18 times higher than D-T** | [WH22] App. D | Primary | none | High |
| Best D-3He result found | JET (1991): fusion power 140 kW, 4.6 x 10^16 reactions/s, **Q = 1.25%** at 10 MW of ion-cyclotron heating (3He tail on D plasma) | [JS92] | Primary (abstract) | [WH22]: scientific breakeven (Qsci = 1) "has not yet been achieved" by any magnetic approach; D-T records TFTR 0.27, JET 0.64 | High. D-3He net energy: **not demonstrated** |
| Laser fusion record (D-T, for context) | 8.6 MJ from 2.08 MJ of laser, target gain 4.13, 7 Apr 2025; D-T fuel | First-run rows 10, 12 (LLNL annual report FY2025; LLNL "How ICF works") | Primary (agency) | LLNL: 3.15 MJ from 2.05 MJ on 5 Dec 2022 | High; not re-opened in the second run, so cited as logged |
| Source of He-3 for fusion programs | "must be bred via other reactions or mined from the moon" | [WH22] | Primary | First-run row 8: Helion (company blog, 2024) breeds He-3 from D-D and tritium decay (secondary) | High |
| Energy per kg of He-3 burned with deuterium | **5.85 x 10^14 J/kg of He-3** (3.51 x 10^14 J per kg of D + He-3) | DERIVED (calc C3) from [WH22], [NIST] | Derived | [MO] (Crawford 2014): "about 5.8 x 10^14 J/kg" | High |
| He-3 per gigawatt-year of fusion heat | **54 kg** | DERIVED (calc C3) | Derived | none | High (physics); thermal, before any conversion loss |
| He-3 to supply all of the world's 2025 primary energy as fusion heat | about 1,030 t/yr (600 EJ; [OWID]) | DERIVED (calc C3) | Derived | none | High as arithmetic; it assumes a fusion technology that does not exist |
| He-3 concentration by medium (by mass) | **Solar wind 39 to 54 g per tonne** (calc C1); Jupiter's atmosphere 23 g/t ([SL] D6: 2.3 x 10^-5); a Uranus case 15 g/t ([SL] 3F, Palaszewski); lunar regolith about 0.0042 g/t (4.2 ppb, [MO] A5) | DERIVED and siblings | Mixed | none | Medium |
| Per unit of collecting effort | Moon: about 240,000 t of regolith per kg of He-3 ([MO]); Jupiter 43 t of atmosphere per kg; Uranus case 66 t; solar wind 18 to 26 t of wind per kg, **but at 1.2 to 1.7 million km^2 of capture area per tonne-year even at 0.1 AU** (F1) | DERIVED | Derived | none | Medium |
| Capture area for 54 kg/yr (one GW-year of fusion heat) | 67,000 to 93,000 km^2 at 0.1 AU; 6.7 to 9.3 million km^2 at 1 AU | DERIVED (calc C3) | Derived | none | Medium |
| Whole-wind He-3 vs world need | 1.6 to 2.3 million t/yr leave the Sun, about 1,600 to 2,200 times the 1,030 t/yr above; the limit is capture area and fusion, not supply | DERIVED | Derived | none | Medium |

**Reading.** The solar wind is the richest He-3 medium by mass found in any of these files, about twice Jupiter's
atmosphere and 10,000 times lunar regolith, but it is spread over the whole sky. The value of He-3 as fuel is conditional on
D-3He fusion producing net energy, which no experiment has approached (best Q 1.25%, ignition 18 times harder than D-T).

### F3. Sunlight as the inner system's energy resource (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Solar luminosity | 3.828 x 10^26 W | [SL] 3C ([NSSDC]) | Primary (via sibling) | none needed | High |
| Irradiance at 1 AU | 1,361 W/m^2 (derived from L) | [SL] 3D | Derived | [KL11]: measured **1,360.8 +/- 0.5 W/m^2** (2008 minimum) | High |
| Irradiance at stated distances | Venus 0.723 AU: 2,602 W/m^2 (1.91x); Mercury 0.387 AU: 9,084 (6.67x); 0.3 AU: 15,120 (11.1x); 0.1 AU: 136,100 (100x); 0.0465 AU: 629,500 (462x) | DERIVED (calc C4) | Derived | NSSDC fact sheets via [NW]: Venus 2,601.3, Mercury 9,082.7 | High |
| World primary energy, 2025 | 166,754 TWh = **600 EJ**, mean **19.0 TW** (traditional biomass excluded) | [OWID] (EI Statistical Review 2026) | Dataset | [DN26]: "exceeded 600 EJ in 2025, a rise of 1.7% over 2024"; [OWID] 2024: 164,494 TWh | High |
| World use as a share of the Sun's output | 5.0 x 10^-14 of L; the Sun emits 2.0 x 10^13 times world use | DERIVED (calc C4) | Derived | none | High |
| Sunlight Earth intercepts | 1.74 x 10^17 W, **about 9,100 times** world use | DERIVED (calc C4) | Derived | [SL] D7: 1.74 x 10^17 W | High |
| Collector area intercepting world use | 14,000 km^2 at 1 AU; 140 km^2 at 0.1 AU (sunlight only) | DERIVED (calc C4) | Derived | none | High (geometry) |
| Space solar cells and arrays, state of practice | Cells about 30% at 1 AU (38% expected mid-2020s); arrays: rigid 80 W/kg, flexible 150 W/kg, 330 to 338 W/m^2 at 1 AU BOL; largest flexible fold-out 120 kW; specific power rose from 30 to 100 W/kg over 25 years; targets 150-200 near term, 200-250 W/kg later | [JPL17] §3, Table 3-3 | Primary (agency) | [NW] F3 cell temperature limits near Mercury (130 to 230 C) | High. DEMONSTRATED (state of practice) |
| Array area and mass to supply world use as electricity at 1 AU | about 46,600 km^2 of 30% cells; at 150 W/kg, about 1.3 x 10^11 kg (130 Mt); areal density about 2.25 kg/m^2 | DERIVED (calc C4) | Derived | [SYN] 5: 1 Mt/yr is 313 times the 2025 world launched mass, so arrays of this mass would have to be made in space | Medium (state-of-practice arrays; no storage, pointing or radiator mass) |
| Space-based solar power to Earth (two NASA reference designs) | 2 GW delivered each: RD1 heliostat swarm 5.9 million kg, RD2 planar arrays 10 million kg (**2.95 and 5.0 kg per delivered kW**); about **13% of incident sunlight delivered**; LCOE **0.61 and 1.59 $/kWh** against 0.02-0.05 $/kWh terrestrial (12-31 and 32-80 times higher); launch 71% and 77% of cost; with optimistic launch and lifetime assumptions 0.03 and 0.08 $/kWh | [OTPS24] pp. 7, 13-14, App. | Primary (agency study) | Source concepts in [OTPS24]: SPS-ALPHA Mark III 7,500 t for 2 GW (3.75 kg/kW); Tethered-SPS 20,000 t for 0.75 GW average | High as a study; ENGINEERING-STUDIED. Internal mass inconsistency noted (Conflicts) |
| Dyson-swarm limits | A patch normal to the Sun is balanced by radiation pressure (beta = 1) at **0.8 g/m^2** (L/(4 pi G c M)), "comparable to the thinnest gold leaf"; the Sun's output could unbind Jupiter in under 1,000 years | [WR20] Eq. 23, §4 | Primary (review) | DERIVED: 0.77 g/m^2 from [SL] constants; [SL] 3F (Armstrong and Sandberg): a swarm at Mercury's orbit at 3.92 kg/m^2 from all of Mercury | High (physics). SPECULATIVE as engineering |

**Reading.** Sunlight is the one solar benefit that is available everywhere in the inner system at no lifting cost and with
hardware that already flies. Going sunward multiplies power per area (100 times at 0.1 AU), but hot cells lose efficiency and
flown designs throw much of the extra light away ([NW] F3, [ME] F6).

### F4. Radiation pressure, sails and solar-thermal propulsion (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Radiation pressure at 1 AU | Perfect reflector 9.1 µPa; lightness number independent of distance; beta = 1 at 1.5 g/m^2 (sail) | [NW] F3 (Bailer-Jones 2020) | Primary (via sibling) | DERIVED: 2S/c = 9.08 µPa (calc C5b); [WR20]: 0.8 g/m^2 for an absorbing patch | High |
| Solar-wind dynamic pressure at 1 AU (slow wind) | about 1.1 nPa, **about 7,900 times less** than radiation pressure on a reflector | DERIVED (calc C5b) from [SL] 3C | Derived | none | High. Wind-momentum devices (magnetic or electric sails) work only through very large effective areas ([SL] 3E, [NW] F3) |
| Sails flown and studied | Largest flown in deep space IKAROS 196 m^2 (lambda below 0.01); a 75,625 m^2 Mercury design at 5.9 g/m^2, 7.78 µN/m^2 at 1 AU, film at most 494.5 K against a 520 K polyimide limit | [NW] F3 | Primary (via sibling) | [NW] F2/F3 | High (flown); medium (design) |
| Near-Sun sail ("sundiver") escape speeds in the literature | Sail concepts at 5 to 11 R_sun perihelia reach **20 to 60 au/yr**: >20 au/yr needing a >10,000 m^2 sail (Davoyan et al.); about 15 au/yr with a 400 m, about 1 g/m^2 sail at about 0.25 AU and 25 kg of instruments (Liewer et al.); about 60 au/yr for 12-16 kg (Davoyan et al.); laser sails about 63 au/yr at gram-to-kg scale | [MA26] §2.1, Table 1 | Primary (preprint review of published studies) | [NW] F3: Bailer-Jones 2020 (Sun Diver), theory | Medium. SPECULATIVE (no sail has flown near the Sun) |
| Solar-thermal propulsion, demonstrated | Shooting Star Experiment rhenium engine, ground test with electric heaters: 150 s with nitrogen at 1,760 F exit, "equivalent hydrogen" about 630 s; gas "approaching 4,500 F"; about 1 lbf | [TS02] | Primary (agency test) | none for a flight test | Medium. DEMONSTRATED on the ground only, not with sunlight in space |
| Solar-thermal Oberth concepts | Materials surviving 2,800 K at 20 x 20 cm; goal "> 10 astronomical units per year"; propellants H2, LiH, Li, CH4, NH3, H2O | [NIAC22] | Primary (agency-funded study) | [MA26] Table 1: STP studies at 0.01 to 0.02 AU give 8 to 20 au/yr with 36 to 662 kg delivered (Lyman, Sauder, Benkoski); Benkoski's case uses 5,000 kg launched on SLS with a Jupiter assist | Medium. ENGINEERING-STUDIED (concept) |
| Solar-electric propulsion near the Sun | Concentrating thrust near a 0.3 AU perihelion gives **three times** the specific orbital energy per delta-v of a 1 AU spiral; reference case 15,189 kg launched, 1,551 kg payload, 9.03 au/yr, 200 AU in 24.3 years, assuming cells survive about 400 C (laboratory only) | [MA26] abstract, §5 | Primary (preprint) | [NW] F3: flown Mercury arrays hold cells to 130-230 C | Low-medium. ENGINEERING-STUDIED (preprint) |
| Benefit for trucking | Sails need no propellant and gain 1/r^2 thrust sunward; the Mercury-to-Earth sail convoy figures (369 d at 0.78 mm/s^2; 133 to 336 km^2 of sail per kt/yr) are in [IMS] 5 and [NW] F6 | [IMS], [NW] | via siblings | none | Medium (sail lifetime near the Sun unknown) |

### F5. Gravity and the solar Oberth maneuver (checklist 5)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Oberth relation | Impulsive prograde burn: delta-epsilon = v dv + dv^2/2, so a burn at high speed (deep in the well) adds the most orbital energy | [MA26] §2.1 | Primary (preprint stating a standard result) | none needed | High |
| Escape speed from the Sun at the burn point | 345 km/s at 3.2 R_sun; 252 at 6 R_sun; 197 at 9.86 R_sun (Parker); 133 at 0.1 AU; 77 at 0.3 AU; 42 at 1 AU | DERIVED (calc C5) | Derived | [SL] D1 constants | High |
| Hyperbolic excess speed from a burn dv at perihelion (falling in on a parabolic orbit) | **dv = 3 km/s:** 45.6 km/s (9.6 au/yr) at 3.2 R_sun; 34.5 km/s (7.3 au/yr) at 9.86 R_sun; 28.4 km/s (6.0) at 0.1 AU; 16.2 km/s (3.4) at 1 AU. **dv = 7.2 km/s** (Project Lyra's SOM): 70.9 km/s (15.0 au/yr) at 3.2 R_sun | DERIVED (calc C5) | Derived | [HI22]: SOMs give "huge velocity gains"; [MA26] Table 1: chemical SOMs 8.5 to 20 au/yr | High (two-body physics, no losses) |
| Reference speeds without a solar dive | Voyager 1 about 3.6 au/yr (half of 7.2); SLS Block 2 with a Jupiter assist "up to 7.2 au/yr", about 7 au/yr | [MC22], [BR22] abstracts | Primary | [NIAC22]: "8 AU/yr for a ~1 tonne spacecraft payload" with a Jupiter assist | High |
| Cost of reaching a low perihelion | From a 1 AU circular orbit directly: 24.7 km/s to 3.2 R_sun, 21.0 to 9.86 R_sun, 17.1 to 0.1 AU, 9.6 to 0.3 AU. Via Jupiter: a 3.2 R_sun perihelion needs an aphelion speed of 0.99 km/s against Jupiter's 13.06 km/s orbital speed, which a retrograde Jupiter flyby supplies | DERIVED (calc C5) | Derived | [HI26]: "E-J-SOM" sequences; Parker used repeated Venus flybys ([SL]) | High |
| Survivability at the burn | About 6 MW/m^2 at 3.2 R_sun; heat shield mass comes out of the payload; spacecraft up to about 500 kg; navigation errors at the burn map into large errors outbound | [HI26] abstract, §4; [MA26] §2 | Primary (preprints) | [SL] 3D: Parker's 73 kg shield at about 1,400 C, 9.86 R_sun, hours per pass | High that it is the limiting problem |
| The study verdict | APL's Interstellar Probe team: the SOM "offers no advantage over prograde gravity assists in rapid escape from the solar system for a 'technology horizon' in the 2030's", after "181 staging scenarios"; the problem is "the mass of the thermal shield assembly" | [CD21] quoting McNutt | **Secondary** (the APL report and the full McNutt 2022 paper could not be opened) | [HI22]: a Jupiter Oberth matches SOM performance for 1I/'Oumuamua without the heat shield | Medium |
| Cargo moving sunward | The well is a cost, not a benefit: a direct transfer to 0.1 AU costs 17 km/s for the first burn alone; [SYN] 3 gives 32.8 km/s to depart a 0.1 AU circular orbit for Earth (45.4 km/s all-propulsive) | DERIVED; [SYN] | Mixed | [NW] F3: sails spiral inward without propellant | High |

### F6. The near-Sun environment as a process resource (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Largest terrestrial solar furnace | Odeillo 1 MW: 1,830 m^2 parabola, 63 heliostats (2,835 m^2), 1 MW on about 80 cm, **maximum 10 MW/m^2**; furnaces "over 3000 C"; small units reach concentration about 15,000 on 1 cm | [PROMES] | Primary (operator) | DERIVED: 10 MW/m^2 = 7,350 suns at 1 AU; black-body stagnation temperature 3,644 K | High. DEMONSTRATED |
| Other materials-test furnaces | PSA SF-60: 60 kW, 3,000 suns; SF-40: 40 kW, 7,000; SF-5: 5 kW, 6,000 | [PSA] | Primary (operator) | [PROMES] | High. DEMONSTRATED |
| Upper limit on focused sunlight, at any distance | 6.29 x 10^7 W/m^2 (sun-surface brightness, sigma x 5,772^4); maximum concentration falls from 46,200 at 1 AU to 6,930 at Mercury's mean distance and 463 at 0.1 AU, so the product is the same everywhere | [ME] D5; DERIVED (calc C6) | Derived | Odeillo reaches 16% of the limit | High (thermodynamics) |
| What proximity does buy | Concentration needed for 1,923 K (1,650 C): 570 at 1 AU, 85 at Mercury, 51 at 0.3 AU, 5.7 at 0.1 AU; for 3,773 K (3,500 C): 8,440, 1,270, 760, 84. Mirror area per MW delivered to the focus: 735 m^2 at 1 AU, 110 at Mercury, 66 at 0.3 AU, 7.4 at 0.1 AU | DERIVED (calc C6); [ME] D5 | Derived | [ME] F6: 54 to 124 times for 1,923 K at Mercury | High (geometry). **Proximity cuts optics size and concentration, not the peak temperature** |
| Materials that survive | Highest measured melting point: HfC 4,232 K; a passive sun-facing plate passes it at about 1.4 to 1.9 R_sun; solar-thermal prototypes to 2,800 K; Parker shield about 1,400 C flown, 1,650 C tested | [SL] 3D, [NIAC22] | Primary (via sibling; agency) | none | High |
| Passive heating with no optics | Sun-facing black plate: 394 K (121 C) at 1 AU, 463 K at Venus's distance, 719 K at 0.3 AU, about 1,250 K at 0.1 AU | DERIVED (calc C6; [SL] D5 formula) | Derived | [SL] D5: 744 K at 0.28 AU | High |
| Sterilization | Spacecraft dry-heat microbial reduction studies run at about 115 to 170 C; spore kinetics measured at 125 C | [JPLPP], [BO70] | Primary (thin) | none (D-values only in a search summary, not used) | Medium. **Needs no near-Sun site**: a black plate at 1 AU reaches 121 C, and modest concentration exceeds it |

### F7. Stellar-scale options and exotic products (checklist 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Starlifting | Literature is life-extension only (5 x 10^19 kg/yr, about 1,200 times the wind, at least 8 x 10^-4 L); no engineering design; 1.9 x 10^11 J/kg to escape the photosphere | [SL] 3A, 3C, D1 | via sibling | [SYN] 2 | High. SPECULATIVE |
| Value of the natural mass loss | Wind 1.3 x 10^9 kg/s against 4.26 x 10^9 kg/s converted by fusion; at today's rate the wind removes 9.6 x 10^-5 of the Sun's mass in 4.6 Gyr | [SL] 3C; DERIVED (calc C7) | Derived | none | High. The wind is the only solar matter that leaves for free (F1) |
| Stellar engines | Passive (Shkadov-type mirror): accelerations of order 10^-12 m/s^2 (about 32 m/s per million years); active (collects solar wind, lifts more mass, fuses helium): up to 10^-9 m/s^2, "deflections of 10 pc in as little as 1 Myr"; the passive-engine prefactor was later corrected from (1/2 + 1/6)e to (3/4)e | [CA19], [SC21] abstracts | Primary (abstracts) | DERIVED: 10^-9 m/s^2 for 1 Myr gives 31.6 km/s and 16 pc | Medium. SPECULATIVE; no design |
| Solar antimatter: what the Sun makes | p-p chain positrons in the core "are immediately annihilated"; flare positrons annihilate in the flaring atmosphere (about 3-4 x 10^5 K, densities of order 10^15 cm^-3) | [GO20] | Primary (review) | none | High that the Sun makes positrons; no measurement of an escaping, collectable flux was found |
| Solar antimatter harvesting proposal | Cycling spacecraft with a 700 km effective-radius superconducting funnel and Penning-Malmberg traps; **upper bound about 12 micrograms over 200 dives**; "research-grade ... rather than energy-grade"; the positron flux is "uncertain and is treated here as an optimistic upper bound"; "This is a preprint; it has not been peer reviewed by a journal" | [BK26] | **Unreviewed preprint** | DERIVED: 12 µg annihilated with 12 µg of matter yields 2.2 x 10^9 J (0.6 MWh) | Low. SPECULATIVE. **No peer-review record (acceptance or rejection) found**; [SL] also rejected it as a source |
| Antimatter in the Dyson-sphere literature | Mentioned only as a hypothetical way a civilization might store starlight ("the production of antimatter is plausible activity that would result in little emission") | [WR20] §4 | Primary (review) | none | SPECULATIVE |

### F8. Costs and conditions (checklist 8)

Cited from [SL] and [SYN] without re-derivation, plus the figures above.

| Condition | Value | Source |
|---|---|---|
| Heat | 13 times Earth's sunlight at 0.28 AU; 650,000 W/m^2 at 9.86 R_sun; about 6 MW/m^2 at 3.2 R_sun; plate equilibrium about 1,250 K at 0.1 AU | [SL] 6, [HI26], calc C6 |
| Shield mass | Parker: 73 kg shield at about 1,400 C, admits under 50 W; a SOM shield "the real problem"; in one case about 300 kg on a 380 kg bus | [SL] 3D, [CD21], [MA26] Table 1 note a |
| Autonomy and communication | About 8 minutes of light time at 1 AU; Parker keeps itself in shadow without help | [SL] 3D |
| Collector area | Tens of km^2 per tonne-year of hydrogen at 0.1 AU, 10^4 to 10^9 km^2 per tonne-year for everything else (F1); no capture-and-store device designed | F1, [SL] 3E |
| Minimum infrastructure | Arrays of hundreds of watts, passive implantation collectors, a return capsule (Genesis); Genesis cost $164 M plus $45 M operations | [SL] 3E |
| Lifting energy (photosphere) | 1.9 x 10^11 J/kg; 190 GW continuous per kg/s at 100% | [SL] 7 |

### F9. Ranked benefits: who could use each, what it costs, and whether solar matter must be lifted (checklist 9)

Ranked by (benefit delivered) against (cost and readiness), on the figures above. "Lifts solar matter" means material must
be raised out of the Sun's gravity by the user; the wind is already lifted by the Sun.

| Rank | Benefit | Quantity | Who could use it | Cost to get it | Lifts solar matter? | Evidence |
|---|---|---|---|---|---|---|
| 1 | Sunlight as electric power | 1,361 W/m^2 at 1 AU to 136,000 at 0.1 AU; arrays 80 to 150 W/kg | Any vehicle, station, plant or settlement in the inner system | Arrays (2.25 kg/m^2 class), radiators, cooling near the Sun | **No** | DEMONSTRATED (F3) |
| 2 | Concentrated sunlight as process heat | Up to 10 MW/m^2 demonstrated; optics shrink 1/r^2 sunward | Refining, ceramics, vapor processing, sterilization | Mirrors (735 m^2 per MW at 1 AU, 7.4 at 0.1 AU) | **No** | DEMONSTRATED on Earth (F6) |
| 3 | Radiation pressure (sails, statites) | 9.1 µPa at 1 AU, x100 at 0.1 AU; no propellant | Cargo convoys, probes, station-keeping | Sail film at gram-per-m^2 scale; lifetime near the Sun unknown | **No** | DEMONSTRATED at 196 m^2; larger is ENGINEERING-STUDIED (F4) |
| 4 | Solar Oberth maneuver | 3 km/s at 3.2 R_sun gives 45.6 km/s outbound (9.6 au/yr) | Fast outbound probes | Heat shield (hundreds of kg), a Jupiter flyby or 21 to 25 km/s to get there; judged no better than a Jupiter assist for 2030s technology | **No** | ENGINEERING-STUDIED (F5) |
| 5 | Solar-thermal propulsion | About 630 s hydrogen-equivalent on the ground; materials to 2,800 K | Upper stages, Oberth burns | Hydrogen storage, concentrators | **No** | Ground-DEMONSTRATED (F4) |
| 6 | Solar-wind hydrogen and helium | 78 to 82 km^2 per t/yr of H, 430 to 610 km^2 per t/yr of He at 0.1 AU (x100 at 1 AU) | Volatile-poor sites (as hydrogen feed; oxygen must come from elsewhere) | A capture device that does not exist; km^2-scale structures at 1,250 K near 0.1 AU | No (the Sun has lifted it) | SPECULATIVE beyond Genesis's milligram (F1) |
| 7 | Solar-wind helium-3 | 39 to 54 g per tonne of wind; 67,000 to 93,000 km^2 per GW-year at 0.1 AU | D-3He fusion, if it ever gives net energy | Capture area plus an undemonstrated fusion cycle (best Q 1.25%) | No | SPECULATIVE (F2) |
| 8 | Solar-wind noble gases and nitrogen | Ne 49,000 to 68,000 km^2, N 88,000 to 122,000 km^2, Ar 1.2 to 1.7 million km^2 per t/yr at 0.1 AU | Propellant, inert gas | As rank 6, at 10^3 to 10^4 times the area | No | SPECULATIVE |
| 9 | Solar-wind metals | Fe 18,000 to 25,000 km^2 per t/yr at 0.1 AU | Nobody on these numbers ([IMS] 2 for better sources) | As rank 6 | No | SPECULATIVE |
| 10 | Photospheric starlifting | 1.9 x 10^11 J/kg; 841 t lifted per t of Fe | Not a material source on any figure | Dyson-swarm-class power; no mechanism | **Yes** | SPECULATIVE ([SL], [SYN]) |
| 11 | Stellar engines | 10^-12 to 10^-9 m/s^2 | Moving the whole Solar System over Myr | Star-scale mirror or jet; the active form lifts mass | Passive: no; active: **yes** | SPECULATIVE (F7) |
| 12 | Solar antimatter | At most about 12 µg over 200 dives (unreviewed) | Research only | Superconducting funnel, traps, laser propulsion | Collects escaping particles (flux unmeasured) | SPECULATIVE, unreviewed (F7) |

**Which benefits need no solar matter lifted:** ranks 1 to 5 (light and gravity), and all wind-based ranks 6 to 9 (the Sun
lifts the wind itself). Only photospheric starlifting and the active stellar engine require lifting matter out of the Sun.
**Plainly: every benefit that is real today comes from the Sun's light and gravity, not from its matter.**

## Conflicts

1. **Hydrogen normalization of the solar wind.** [LO20] Table 5 gives H = 1.02 x 10^6 per 100 Mg in its Genesis column and
   1.51 x 10^6 in its bulk-wind column (Pilleri 2015, Reisenfeld 2013). Every heavy-element mass fraction moves by about 40%
   between them, and He/H by number is 4.8% against 3.2%. Possible reasons: the Genesis hydrogen value is from implanted
   collectors (Koeman-Shields 2016) while the bulk column is in-situ spectrometry; the two cover different epochs. Both are
   carried as a range in F1.
2. **C/O in the wind.** [LO20]'s Genesis column gives C/O = 383/723 = 0.53 (bulk 0.62, slow 0.65, fast 0.69), while [CL22]
   finds ACE SWICS C/O "constant at ≈0.7". Different instruments and epochs; the in-situ value is the higher one.
3. **Helium abundance.** He/H by number: 4.8% (Genesis column), 3.2% (bulk column), "stable value between 4% and 5%" in fast
   wind ([SL] 3C, Alterman and Kasper 2019). Slow wind is depleted in helium ([SL] row 77), which may explain the bulk value.
4. **Collector flux basis.** This file uses the whole-wind loss spread over a sphere (4.7 x 10^-15 kg m^-2 s^-1 at 1 AU);
   [SL] D3 used the slow-wind proton flux (3.1 x 10^-15). The first includes helium and all wind types; the second is
   protons only. Areas here are about 1.5 times smaller than [SL]'s for the same product.
5. **Iron yield per area vs [SYN].** [SYN] 2 gives 86,000 km^2 per tonne of iron per year at 0.1 AU using photospheric iron
   and the proton flux; F1 gives 18,000 to 25,000 km^2. The factor of 3.5 to 4.8 is the flux basis (1.5) times the measured
   FIP enrichment of iron (2.0 to 2.9). [SYN] flagged this enrichment as unresolved; it is now resolved within the H-normalization
   uncertainty.
6. **NASA OTPS system mass.** The report gives 5.9 million kg (RD1) and 10 million kg (RD2) delivered for 2 GW (p. 7), but
   p. 13 says "1000 metric tons (MT) versus 585 MT" for the same comparison, and the source concepts are 7,500 t (SPS-ALPHA)
   and 5 x 20,000 t (Tethered-SPS, scaled 0.77 to 5 times). The 5.9 and 10 Mkg figures are used because they drive the
   report's launch count and cost; the p. 13 figures are likely a units error in the report.
7. **3He/4He.** [HE09] 4.64 x 10^-4 vs [TR03]'s rounded "~0.0004" "solar system value". Consistent within rounding; the
   protosolar value is lower than the wind's because deuterium has been burned to He-3 ([SL] 3F gives Jupiter 1.66 x 10^-4).
8. **Energy per D-3He reaction.** 18.3 MeV ([WH22]) against 19.0 MeV implied by [JS92]'s power and rate. The 4% difference
   is within the rounding of "140 kW" and "4.6 x 10^16"; not a real disagreement.
9. **Does the solar Oberth maneuver pay?** Two-body arithmetic (F5) and [HI26], [MA26] show large gains per km/s of burn;
   the APL study ([CD21] quoting McNutt) found "no advantage" over a prograde Jupiter assist. They answer different questions:
   the arithmetic ignores the heat-shield and kick-stage mass that APL found decisive, and the gain is real only after paying
   to get to perihelion (a retrograde Jupiter flyby or 21 to 25 km/s).
10. **Odeillo's peak temperature.** Popular pages (row 49) say 3,500 C; [PROMES] says "over 3000 C" and 10 MW/m^2, whose
    black-body stagnation temperature is 3,644 K (3,371 C). The 3,500 C figure is not used.
11. **A typo in [HI26].** Its §4 says the flux "at 3.2 au from the Sun's center" is about 6 MW/m^2; the abstract and the
    arithmetic (6.1 MW/m^2) show it means 3.2 solar radii.
12. **Irradiance at 1 AU.** 1,361 W/m^2 derived from L ([SL]) vs 1,360.8 +/- 0.5 measured ([KL11]): agree.

## Derived figures

Script: scratch folder `benefits_of_mining_the_sun/py/calc.py`; full output `calc_out.txt` there. Constants: GM = 1.32712 x
10^20 m^3/s^2, R_sun = 6.957 x 10^8 m, L = 3.828 x 10^26 W, M_sun = 1.9884 x 10^30 kg ([SL] from NSSDC); 1 AU = 1.495978707
x 10^11 m; 1 yr = 3.15576 x 10^7 s; atomic mass constant 1.66053906892 x 10^-27 kg ([NIST]); 1 eV = 1.602176634 x 10^-19 J
(SI exact); c = 299,792,458 m/s (SI exact); sigma = 5.670374 x 10^-8 W m^-2 K^-4; G = 6.674 x 10^-11.

**C1. Wind mass fractions.** w_X = n_X A_X / sum(n_i A_i) over the [LO20] abundances (Genesis column, slow-wind column for
Al, Si, P, S, Ca, Cr, Ni), with H = 1.02 x 10^6 or 1.51 x 10^6 per 100 Mg. Atomic weights [CIAAW]; solar argon's mean mass is
(5.47 x 35.9675 + 37.9627)/6.47 = 36.28 from [HE09]'s 36Ar/38Ar and [NIST] masses (the terrestrial 39.95 is 40Ar and would be
wrong for the wind). He-3: n_He x 4.64 x 10^-4 x 3.01603. Key output (Genesis H / bulk H):
```
H 0.8196 / 0.8705   He 0.1554 / 0.1115   O 9.22e-3 / 6.62e-3   C 3.67e-3 / 2.63e-3   Fe 3.78e-3 / 2.72e-3
Si 2.44e-3 / 1.75e-3  Mg 1.94e-3 / 1.39e-3  Ne 1.38e-3 / 0.99e-3  He3 5.43e-5 / 3.90e-5  Ar 5.49e-5 / 3.94e-5
Xe 2.89e-8 / 2.07e-8   heavier than He: 0.0251 / 0.0180   He/H by number 0.0477 / 0.0323
```
Fe/H by number: 85/1.02e6 = 8.33 x 10^-5 and 88/1.51e6 = 5.83 x 10^-5, against 10^(7.46-12) = 2.88 x 10^-5: 2.89 and 2.02.

**C2. Flux and area.** F(r) = 1.32 x 10^9 / (4 pi r^2): 4.694 x 10^-15 kg m^-2 s^-1 at 1 AU = 0.1481 kg km^-2 yr^-1;
0.2831 at 0.7233 AU; 0.9885 at 0.3871; 1.646 at 0.3; 14.81 at 0.1; 68.5 at 0.0465. Area for 1 t/yr of X = 1,000 /
(w_X F yr). Examples at 0.1 AU: H 77.6 to 82.4 km^2; He 434 to 606; Fe 17,800 to 24,900; He-3 1.24 to 1.73 x 10^6;
Xe 2.34 to 3.26 x 10^9. Water: O/(2H) mass = 15.999/2.016 = 7.94; usable fraction of wind H = (w_O/w_H)/7.94 = 0.0112/7.94
= 0.14% (Genesis) and 0.0076/7.94 = 0.10% (bulk); H per tonne of water = 1,000/8.94 = 112 kg.

**C3. He-3.** 18.3 MeV x 1.602e-19 / (3.01603 x 1.66054e-27 kg) = **5.854 x 10^14 J/kg**. One GW-year = 3.156 x 10^16 J,
so 53.9 kg. World 2025: 166,753.6 TWh x 3.6 x 10^15 J/TWh = 6.003 x 10^20 J (19.02 TW mean), so 1,025 t. JET check:
140 x 10^3 W / 4.6 x 10^16 s^-1 = 3.04 x 10^-12 J = 19.0 MeV. Terrestrial 3He/4He 1.34 x 10^-6; ratio 4.64e-4/1.34e-6 = 346.

**C4. Light.** S(r) = L/(4 pi r^2): 1,361; 2,602 (0.7233 AU); 9,084 (0.3871); 15,120 (0.3); 136,100 (0.1); 629,500
(0.0465) W/m^2. World power / L = 1.902e13 / 3.828e26 = 4.97 x 10^-14. Area at 1 AU for 1.902 x 10^13 W: 13,980 km^2 of
sunlight; 46,580 km^2 of 30% cells; mass at 150 W/kg = 1.27 x 10^11 kg. Earth's intercept: 1,361 x pi x (6.371 x 10^6)^2 =
1.736 x 10^17 W = 9,124 times world use. OTPS: 5.9 x 10^6 kg / 2 x 10^6 kW = 2.95 kg/kW; 10^7 / 2 x 10^6 = 5.0 kg/kW.
Statite: L/(4 pi G c M) = 0.766 g/m^2.

**C5. Oberth.** v_p = sqrt(2 GM / r_p) on a parabolic infall; after an impulsive dv, v_inf = sqrt(2 v_p dv + dv^2).
1 au/yr = 4.7405 km/s.
```
rp 3.2 Rsun  v_esc 345.3 | dv 1.0 -> 26.3 km/s (5.55 au/yr) | dv 3.0 -> 45.6 (9.62) | dv 7.2 -> 70.9 (14.95)
rp 9.86 Rsun v_esc 196.7 | dv 1.0 -> 19.9 (4.19)            | dv 3.0 -> 34.5 (7.27) | dv 7.2 -> 53.7 (11.33)
rp 0.1 AU    v_esc 133.2 | dv 1.0 -> 16.4 (3.45)            | dv 3.0 -> 28.4 (6.00) | dv 7.2 -> 44.4 (9.36)
rp 0.3 AU    v_esc  76.9 | dv 1.0 -> 12.4 (2.62)            | dv 3.0 -> 21.7 (4.58) | dv 7.2 -> 34.0 (7.18)
rp 1 AU      v_esc  42.1 | dv 1.0 ->  9.2 (1.95)            | dv 3.0 -> 16.2 (3.41) | dv 7.2 -> 25.7 (5.41)
```
Getting there: first Hohmann burn from 1 AU, dv = sqrt(GM/a_E) - sqrt(GM x 2 r_p / (a_E (a_E + r_p))): 24.68 km/s (3.2 R_sun),
20.96 (9.86 R_sun), 17.08 (0.1 AU), 9.55 (0.3 AU). At 5.2 AU, circular 13.06 km/s; aphelion speed for a 3.2 R_sun perihelion 0.99.

**C5b. Pressures.** 2S/c at 1 AU = 9.08 x 10^-6 Pa. Slow wind rho v^2 = 5 x 10^6 m^-3 x 1.67262 x 10^-27 kg x (3.7 x 10^5)^2
= 1.15 x 10^-9 Pa; ratio 7,931. Wind kinetic power 0.5 x 1.32e9 x (4 x 10^5)^2 = 1.06 x 10^20 W = 2.8 x 10^-7 L.

**C6. Furnaces.** C = sigma T^4 / S; C_max = 1/sin^2(R_sun/d); C_max x S = 6.29 x 10^7 W/m^2 at every distance.
```
r=1.000 AU: C(1923 K)=570  C(3773 K)=8442  Cmax=46239  mirror m^2 per MW 735
r=0.387 AU: C(1923 K)=85   C(3773 K)=1265  Cmax=6929   mirror m^2 per MW 110
r=0.300 AU: C(1923 K)=51   C(3773 K)=760   Cmax=4162   mirror m^2 per MW 66
r=0.100 AU: C(1923 K)=5.7  C(3773 K)=84    Cmax=463    mirror m^2 per MW 7.35
```
Odeillo 10 MW/m^2 = 7,347 suns at 1 AU, 15.9% of the limit; stagnation (10^7/sigma)^0.25 = 3,644 K. Plates (a/e = 1): 394 K
(1 AU), 463 K (0.723 AU), 719 K (0.3 AU); 0.1 AU = 394 x 10^0.5 = 1,246 K.

**C7. Stellar.** a t over 1 Myr (3.156 x 10^13 s): 10^-12 m/s^2 gives 31.6 m/s and 0.016 pc; 10^-9 gives 31.6 km/s and 16.1 pc
(0.5 a t^2, 1 pc = 3.0857 x 10^16 m). Antimatter: 2 x 12 x 10^-9 kg x c^2 = 2.16 x 10^9 J = 0.60 MWh. Wind over 4.6 Gyr:
1.32e9 x 4.6e9 x 3.156e7 = 1.92 x 10^26 kg = 9.6 x 10^-5 M_sun.

## Constraints for any inhabitant

- **Power is abundant and free to collect; matter from the Sun is not.** Arrays at 80 to 150 W/kg already fly (F3); every solar
  material product needs 10^1 to 10^9 km^2 of capture area per tonne-year with no capture device in existence (F1).
- **Sunward means hotter, not hotter-focusing.** Light per square meter rises 100 times at 0.1 AU, so optics and arrays shrink,
  but the peak focal temperature is the same everywhere and an unshaded black surface sits near 1,250 K at 0.1 AU (F6). Every
  operation there lives in shadow ([SL] 6).
- **A hydrogen-rich wind with almost no oxygen.** Wind matter is 82 to 87% hydrogen by mass; its own oxygen pairs with only
  0.10 to 0.14% of that hydrogen, so any water made from it needs oxygen brought from a rocky or icy source (F1).
- **Fusion fuel is abundant only on paper.** The wind is the richest He-3 medium by mass, but the fuel cycle that would burn
  it has never produced net energy (F2).
- **Fast outbound travel trades heat-shield mass against speed.** A solar dive multiplies a burn's effect several times but
  costs a Jupiter flyby or 21 to 25 km/s to reach, and hundreds of kilograms of shield (F5); the one detailed study preferred
  a Jupiter assist.
- **Cargo going sunward pays to fall.** Reaching 0.1 AU costs 17 km/s for the first burn alone; sails avoid propellant but have
  no measured lifetime near the Sun (F4, F5).
- **A human-shaped machine near the Sun** is in the position of Parker's instruments: inside a shield's shadow, rejecting its
  own heat from shaded radiators, acting on its own because control is minutes away ([SL] 6).

## Candidate handwaves

Flagged, not accepted. The developer decides.

1. **A device that captures and stores solar-wind ions** at km^2 scale (any wind-matter benefit, F1 ranks 6 to 9). Only
   deflecting structures and gram-scale passive collectors exist ([SL] 3E).
2. **D-3He fusion with net energy gain** (any He-3 benefit, F2). Best measured Q 1.25%; ignition needs 18 times the D-T
   triple product.
3. **Solar positron harvesting at any useful scale** (F7). The only proposal is an unreviewed preprint with a 12 µg upper
   bound and an unmeasured flux.
4. **Sails or collectors that survive months to years at 0.1 AU or closer** (about 1,250 K equilibrium, F6; [NW] HW-10).
   No sail has flown near the Sun and no lifetime figure was found.
5. **Solar-thermal hydrogen engines in flight at 2,800 K or more** (F4). Ground prototypes only.
6. **Any photospheric lifting or active stellar engine** ([SL] 7, [SYN] S-1; F7).

## Open threads

- **Gloeckler and Geiss (1998), Space Sci. Rev. 84:275** (Ulysses SWICS 3He/4He in slow vs fast wind): record found, every
  copy blocked (rows 22, 23). Next: an ADS full-text scan or a library copy.
- **Bochsler (2007), "Minor ions in the solar wind"** (A&A Rev.): both copies dead (first-run rows 15, 16). Would give a
  second compilation of wind abundances by regime.
- **Genesis Mg and Fe fluences (Jurewicz et al. 2019; Burnett et al. 2017):** appear only in a search summary (row 19); the
  2020 Jurewicz paper read (row 69) gives isotopes only. They would fix the absolute metal yield without the H normalization.
- **The APL Interstellar Probe study report and the full McNutt et al. 2022 paper:** the SOM verdict is read only through
  Centauri Dreams (rows 44 to 47). Next: the report on the APL Interstellar Probe site.
- **Solar-thermal propulsion flight Isp with hydrogen**; the "760 s demonstrated" claim is only in a search summary (row 63).
  Next: AIAA papers on the Solar Thermal Upper Stage; McNutt AIAA-2001-3377 (dead copy, row 43).
- **Sail degradation near the Sun** (polyimide limit 520 K, [NW]); next: McInnes, *Solar Sailing* (1999), and the Solar
  Cruiser materials data.
- **A measured escaping-positron flux in the corona or solar wind**: none found (rows 58, 59). Next: PSP or Solar Orbiter
  energetic-particle instrument papers on positrons.
- **Caplan (2019) and Svoronos (2020) full texts**: abstracts only.
- **NASA OTPS appendix tables** (mass by subsystem) were not read line by line; they would resolve Conflict 6.
- **Sources found but not read:** arXiv 2307.12411 ("Chasing Nomadic Worlds"); Energy Institute 2026 Review PDF (blocked);
  journaldephysique jp4:1999309 (blocked); Fleishman et al. (flare positrons, microwave detection).
- **Not searched:** UV dose for sterilization near the Sun (dry heat suffices, F6); the economics of any solar product
  (sibling `value_and_markets_of_inner_system_materials.md` covers markets).

## Rejected sources

- **Search-engine summary figures not found in an opened page:** Genesis Mg and Fe fluences (row 19); Ulysses 3He/4He
  4.08 x 10^-4 slow and 3.3 x 10^-4 fast (row 22); "592 EJ in 2024" (row 28); solar 10.12 EJ in 2025 (row 30); "760 seconds
  demonstrated", "approaching 900 seconds" (row 63); NASA dry-heat 104-125 C for up to 50 h and spore D-values (row 54);
  "20 au per year" solar-thermal (row 39); Odeillo "3,500 C" and "10,000 times" (row 49).
- **Popular pages** (Wikipedia, Xataka, Universe Today, JHU Hub, Space Explored, SyFy, Pop Sci, sci.news): leads only.
- **Centauri Dreams** (row 44): used only to report McNutt's quoted verdict, labeled secondary; no number taken from it.
- **Research Square preprint [BK26]:** reported as the evidence level of the antimatter proposal (F7), not used as evidence
  that solar antimatter is collectable.
- **Helion blog** (first run, row 8): company source; used only for the statement that He-3 is bred, which [WH22] confirms.
- **NTRS 20010020153** (row 64): structures of an inflatable concentrator; no propulsion figure used.
