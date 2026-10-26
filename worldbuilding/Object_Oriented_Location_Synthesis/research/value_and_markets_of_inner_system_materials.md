# Value and markets of inner-system materials: what a kilogram is worth, to whom, and what transport it can bear

*Research file, tranche 8, section 11. Started 2026-10-11 (resumed 23:41 PDT after a tool-limit interruption at row 8).
Complete: every checklist item is covered below or listed under Open threads with its reason.*

## Scope

What a kilogram of inner-system material (water and propellant, oxygen, nitrogen, structural metal, silicon, shielding
mass, platinum-group metals, helium and helium-3, power, computation) is worth at Earth's surface, in Earth orbit, at the
Moon, at Mars and near Mercury; the transport cost per kilogram on each route (Moon, near-Earth asteroids, main belt,
Mercury, Venus, solar wind) from the earlier files' delta-v, tug, mass-driver and sail figures; and the break-even
between the two. Prices are 2025 unless stated. Every price is from a source opened this session; none is invented.
Sibling files cited by tag: **[TR]** trucking, **[NW]** logistics network, **[PR]** processing, **[RM]** ramp
timelines, **[LEO]** orbital habitats, **[ML]** Moon, **[BT]** belt, **[SYN]** starlifting synthesis, **[ISM]**
inner-system mining synthesis. Arithmetic: `calc_value.py` and `calc_value_output.txt` in the scratch subfolder
`value_and_markets_of_inner_system_materials/`, numbered D1 to D16 below.

## SEARCH LOG

| # | Date | Search string or page opened (verbatim) | Result | Notes |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read sibling files (allowed read-only): `inner_system_mining_synthesis.md`, `starlifting_synthesis.md`; trucking F1 to F3 and F5; network F6 and F11; processing 5 and 6; LEO habitats D3 to D7 | useful | Anchors cited as [TR], [NW], [PR], [LEO], [SYN], [ISM]; not re-derived |
| 2 | 2026-10-11 | Downloaded by direct URL: USGS, *Mineral Commodity Summaries 2026*, chapters `mcs2026-iron-steel`, `-iron-ore`, `-aluminum`, `-silicon`, `-helium`, `-nitrogen`, `-platinum-group`, `-iron-steel-scrap`, `-magnesium-metal`, `-cobalt`, `-gallium`, `-germanium`, `-rare-earths`, `-lithium` (https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-<name>.pdf) | useful | `-platinum` and `-pgm` and `-platinum-group-metals` filenames 404 (dead at the query, URL guess); `-platinum-group` worked. `-titanium-sponge` 404 (not needed) |
| 3 | 2026-10-11 | WebSearch: `World Bank Commodity Price Data Pink Sheet annual 2025 aluminum iron ore platinum CMO historical data` | useful | Led to Pink Sheet Feb 2026 |
| 4 | 2026-10-11 | Downloaded: World Bank, *CMO Pink Sheet February 2026* (PDF), https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Pink-Sheet-February-2026.pdf | useful | 2023 to 2025 annual averages: aluminum, copper, iron ore, nickel, gold, platinum |
| 5 | 2026-10-11 | WebSearch: `NASA Kennedy liquid oxygen liquid nitrogen purchase contract price per pound Air Products Linde award` | thin | Contract tonnages and maximum values in search summaries only (2009 trade press); no unit price |
| 6 | 2026-10-11 | Opened: gasworld, "NASA awards gas supply contracts" | dead at the sources | HTTP 403 |
| 7 | 2026-10-11 | Opened: NASA press release "NASA awards contract for liquid hydrogen" | dead (tool) | WebFetch and WebSearch both returned "session limit, resets 11:40pm" at 21:47 PDT. Work continued with direct downloads and the public search APIs of NTRS, arXiv, Crossref and OSTI via curl |
| 8 | 2026-10-11 | curl: DuckDuckGo HTML search `Metzger economics lunar propellant` | dead at the query | HTTP 202 (bot check); search engines not usable from the shell |
| 9 | 2026-10-11 | arXiv API (curl): `search_query=abs:asteroid AND abs:mining AND abs:economic` (max 40) | useful | 7 hits: Hein et al. 2018 (1810.03836); "Will AstroForge Collapse the PGM Market?" (2607.06806, 2026); Calla et al. 2018 (1808.05099); four not relevant to price (rotating-asteroid stability, environmental benefits, meteoroid streams, space-weather architecture: not used) |
| 10 | 2026-10-11 | Downloaded and converted: arXiv 1810.03836 (Hein, Matheson, Fries 2018) and arXiv 2303.09011 (Metzger 2023) | useful | Read in full for checklist 2 (session resumed 23:41 PDT after the tool limit reset) |
| 11 | 2026-10-11 | Re-read sibling files after resumption: `inner_system_mining_synthesis.md`, `starlifting_synthesis.md`, [TR] F1 to F5 (lines 152 to 466), [NW] F3 to F6, F9 to F11, [LEO] D3 to D7, E, [PR] 5 to 7, [ML] A5, A6, B, [BT] 3A, [RM] (grep for price, DRA 5.0) | useful | Cited, not re-derived |
| 12 | 2026-10-11 | Extracted text from the 14 USGS MCS 2026 chapters and the World Bank Pink Sheet (pdftotext) and read the salient-statistics, price and world-production tables | useful | Numbers in Findings A. Helium chapter gives no rare-gas prices ("Price data for rare gases were unavailable") |
| 13 | 2026-10-11 | Downloaded and read: arXiv 2607.06806 (Nachtrieb and Smith, "Will AstroForge Collapse the PGM Market?", 2026) and arXiv 1808.05099 (Calla, Fries, Welch 2018/2019) | useful | Checklist 2 and 4 |
| 14 | 2026-10-11 | WebSearch: `SpaceX Rideshare price per kg 2026 Transporter SSO` | thin | Only trade press (newspaceeconomy.ca: $350k for 50 kg, $7k/kg extra, Feb 2026); not confirmed at the vendor |
| 15 | 2026-10-11 | WebFetch: https://rideshare.spacex.com/ and https://www.spacex.com/rideshare/ | dead at the sources | Script-rendered pages return no text |
| 16 | 2026-10-11 | WebSearch: `Falcon 9 list price 2025 "million" standard launch price SpaceX capabilities page 22,800 kg` | thin | Summaries quote $70M (2025) and $74M (2026) list prices from the vendor page via secondary sites; not used as primary |
| 17 | 2026-10-11 | WebFetch: https://aiaa.org/vehicle-guide/vehicles/falcon/nomenclature-cost-availability | dead at the sources | HTTP 404 |
| 18 | 2026-10-11 | WebSearch: `NASA OIG commercial resupply services cost per kilogram CRS-2 SpaceX Northrop Grumman audit report` | useful | Led to IG-18-016 |
| 19 | 2026-10-11 | Downloaded: NASA OIG, IG-18-016, "Audit of Commercial Resupply Services to the International Space Station", 26 Apr 2018, https://oig.nasa.gov/docs/IG-18-016.pdf | useful | Table 3: $63,200/kg (CRS-1) and $71,800/kg (CRS-2 projected) |
| 20 | 2026-10-11 | WebSearch: `NASA OIG audit Commercial Lunar Payload Services CLPS task order value payload mass kilograms cost per kilogram lunar surface` | useful | Search summary's "$3.84 M/kg failure-adjusted" is from a secondary site; not used |
| 21 | 2026-10-11 | Downloaded: NASA OIG, IG-24-013, "NASA's Commercial Lunar Payload Services Initiative", 6 Jun 2024 | useful | $1 M/kg (2019 estimate), about $1.2 M/kg (2023 task orders) |
| 22 | 2026-10-11 | WebSearch: `Mars Design Reference Architecture 5.0 ISRU oxygen production tonnes ascent vehicle propellant 22.7 t cargo lander payload 40 t NASA-SP-2009-566` | useful | My query's "22.7 t" and "40 t" were guesses; the 22.7 t matched only by coincidence to a later source's 22,728 kg O2 propellant figure (below); "40 t" not found and not used |
| 23 | 2026-10-11 | Downloaded: Kleinhenz and Paz (NASA GRC, JSC), "An ISRU Propellant Production System to Fully Fuel a Mars Ascent Vehicle", AIAA 2017-0423 slides, NTRS 20170005179 | useful | Ascent propellant 6,978 kg CH4 + 22,728 kg O2; "Mass savings in LEO is about 10kg per ever[y] 1 kg of propellant produced" |
| 24 | 2026-10-11 | WebSearch: `ULA Kutter cislunar economy propellant price $3,000 per kg LEO $500 per kg lunar surface "per kg" buy price water` | useful | Search summary's "$3,000 to $7,000/kg in LEO" not found in any opened primary; not used |
| 25 | 2026-10-11 | Downloaded: Sowers, House testimony (2017), democrats-science.house.gov; Kutter (ULA), "Cislunar-1000: Transportation supporting a self-sustaining Space Economy", AIAA Space 2016, via sciences.ucf.edu; ULA-UCF slides (4 Mar 2017) | useful | $500/kg lunar surface, $1,000/kg EML1 (Sowers); $3M/t LEO, $1M/t GEO, $0.5M/t Moon (Kutter); Earth propellant "a negligble $1/kg" |
| 26 | 2026-10-11 | WebSearch: `NASA liquid oxygen liquid hydrogen price per pound propellant cost Kennedy contract report "per pound" LOX LH2` | useful | Led to the Nov 2025 LH2 award |
| 27 | 2026-10-11 | WebFetch: NASA, "NASA Awards Liquid Hydrogen Supply Contracts", 21 Nov 2025, https://www.nasa.gov/news-release/nasa-awards-liquid-hydrogen-supply-contracts | useful | 36.5 M lb for up to $144.4 M; 0.48 M lb for $2.8 M (maximum values, 2025 to 2030) |
| 28 | 2026-10-11 | WebSearch: `NASA awards liquid oxygen supply contract pounds maximum value Kennedy Space Center` | useful | Led to the June 2024 LN2/LOX award; the Praxair "52,400 tons" item (gasworld) is undated in the summary and not used |
| 29 | 2026-10-11 | WebFetch: NASA, "NASA Awards Contracts for Acquisition of Liquid Nitrogen, Oxygen", 6 Jun 2024, https://www.nasa.gov/?p=669544 | useful | Quantities and six maximum values; LOX and LN2 are not priced separately (the per-kg figure is a bound, see Derived) |
| 30 | 2026-10-11 | curl: NIST Chemistry WebBook fluid data (saturated N2 and O2 at 1.01325 bar; Xe and He at 273.15 K, 1.01325 bar) | useful | LN2 806.2, LOX 1,141.6 kg/m^3; Xe gas 5.898, He gas 0.1785 kg/m^3 |
| 31 | 2026-10-11 | WebSearch: `DOE Isotope Program helium-3 price per liter 2025 Interlune Department of Energy purchase agreement liters` | thin | Summaries give "about $3,000 per liter" from trade press, not from DOE |
| 32 | 2026-10-11 | WebFetch: Interlune press release, 7 May 2025 | thin | Confirms 3 L, delivery by April 2029, "approximately today's commercial market price"; no number. Company release (secondary for price) |
| 33 | 2026-10-11 | WebSearch (extended): `helium-3 price per liter DOE National Isotope Development Center auction 2024 2025 "per liter" Congressional Research Service helium-3 shortage` | thin | Only market-report pages ($1,900 to $15,000 per liter; inconsistent); none used |
| 34 | 2026-10-11 | WebFetch: Congressional Research Service, Shea and Morgan, "The Helium-3 Shortage: Supply, Demand, and Options for Congress", R41419, 6 Oct 2011 (everycrsreport.com mirror) | useful | Auction price $40 to $85/L historically; allocated $365 to $1,000/L (2009 to 2011); commercial "$2,000 per liter or more"; supply about 8,000 L/yr (tritium decay); 2008 demand about 80,000 L |
| 35 | 2026-10-11 | curl: NIST CODATA 2022, molar volume of ideal gas at 273.15 K and 101.325 kPa | useful | 22.41396954 L/mol (exact) |
| 36 | 2026-10-11 | WebSearch: `NASA Office of Technology Policy and Strategy Space-Based Solar Power report 2024 levelized cost of electricity cents per kWh RD1 RD2 compared terrestrial` | useful | Led to the report PDF; [TR] F5 already cites its launch assumptions |
| 37 | 2026-10-11 | Downloaded: Rodgers et al., NASA OTPS, "Space-Based Solar Power", 11 Jan 2024, https://www.nasa.gov/wp-content/uploads/2024/01/otps-sbsp-report-final-tagged-approved-1-8-24-tagged-v2.pdf | useful | LCOE $0.61 and $1.59/kWh; terrestrial $0.02 to $0.05/kWh; RD1 $276B, 5.9 Mkg, 2 GW; combined-sensitivity $0.03 and $0.08/kWh |
| 38 | 2026-10-11 | WebSearch: `OMB Circular A-94 2023 revision real discount rate 2.0 percent appendix D discount rates 2025` | useful | My query's "2.0 percent" was a guess, unconfirmed and not used; led to M-25-23 |
| 39 | 2026-10-11 | Downloaded: OMB M-25-23, "Rescission and Reinstatement of Circular No. A-94", 8 Apr 2025 | useful | 2023 circular revoked; 1992 circular reinstated |
| 40 | 2026-10-11 | WebFetch: OMB Circular A-94 (1992), obamawhitehouse.archives.gov/omb/circulars_a094 | useful | Sec. 8.b(1): "a real discount rate of 7 percent" |
| 41 | 2026-10-11 | WebFetch: OMB M-25-08 (Appendix C, 2025 rates), bidenwhitehouse.archives.gov | dead at the sources | Scanned PDF; text not extractable by the tool; not needed |
| 42 | 2026-10-11 | WebFetch: Damodaran (NYU Stern), "Cost of Capital by Sector (US)", https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html | useful | January 2026 data: Aerospace/Defense 7.60%, Metals and Mining 8.20%, Power 5.01%, total market 6.96% (nominal cost of capital) |
| 43 | 2026-10-11 | WebSearch: `xenon propellant cost dollars per kilogram electric propulsion krypton argon cost comparison NASA paper NTRS` | thin | Summaries quote $7 to $15/kg argon, $2,100 to $4,800 krypton, $5,000 to $12,000 xenon (sets.space, a vendor blog) and another set ($5, $300, $1,000/kg); neither from a primary source; not used |
| 44 | 2026-10-11 | NTRS API: Herman (NASA GRC) and Unfried (Linde), "Xenon Acquisition Strategies for High-Power Electric Propulsion NASA Missions", NTRS 20150023080, June 2015, full text | useful, but the price is dead at the source | World xenon production about 53,000 kg/yr; 10 t is over 10% of it and "can disrupt the xenon market"; the price history is only in Fig. 8 (not in the text), so no xenon price is recorded |
| 45 | 2026-10-11 | WebFetch: EIA, *Electric Power Monthly*, Table 5.3, released 24 Sep 2026 | useful | 2025 US averages: industrial 8.62, all sectors 13.63 cents/kWh |
| 46 | 2026-10-11 | WebSearch: `Google Project Suncatcher paper space-based AI compute launch cost $200/kg mid-2030s comparable energy cost arXiv` | useful (lead) | My query's "$200/kg" came from trade-press memory; confirmed in the paper itself (row 47) |
| 47 | 2026-10-11 | arXiv API `ti:"space-based" AND ti:"AI infrastructure"`; downloaded arXiv 2511.19468v2 (Google, "Towards a future space-based, highly scalable AI infrastructure system design", Nov 2025) | useful | Table 1 launched-power prices; terrestrial data-center power spend $570 to $3,000/kW/yr; LOX $200/t, methane up to $700/t; propellant floor about $8/kg launched |
| 48 | 2026-10-11 | WebSearch: `NASA OIG Gateway Power and Propulsion Element contract value Maxar cost estimate mass kg IG-24 Gateway audit` | useful | My "IG-24" in the query was a wrong guess; the audit is IG-21-004. The "8 to 9 t" PPE mass came from Wikipedia in the summary; not used |
| 49 | 2026-10-11 | Downloaded: NASA OIG, IG-21-004, "NASA's Management of the Gateway Program for Artemis Missions", 10 Nov 2020 | useful | PPE contract $375 M at award (May 2019), $453,573,559 by 2020 |
| 50 | 2026-10-11 | WebSearch: `space solar array cost per watt "$/W" spacecraft solar array NASA report ROSA cost per watt 2020s` | thin | Only relative claims ("25%" cheaper); no absolute $/W from any primary |
| 51 | 2026-10-11 | WebSearch: `"Solar Power Technologies for Future Planetary Science Missions" JPL D-101316 pdf`; downloaded the report (Dec 2017) | dead at the sources (for cost) | The report gives no $/W figure |
| 52 | 2026-10-11 | Downloaded: Seager et al., NIAC Phase I final report, NTRS 20250005767 (rev. 14 Jul 2025), Table 12 | useful | Venus ascent vehicle: stage propellant 1,286 + 340 kg of 1,840 kg; non-propellant mass 214 kg for a 10 kg canister |
| 53 | 2026-10-11 | BLS public API v1: CPI-U, series CUUR0000SA0, annual averages 1975 to 1979 and 2017 to 2025 | useful | 1977: 60.6; 2018: 251.107; 2021: 270.970; 2022: 292.655; 2025: 321.943 |
| 54 | 2026-10-11 | WebSearch: `NASA Baseline Values and Assumptions Document BVAD 2022 crew consumables kg per crew member per day water food oxygen` | useful (leads) | Summary values (4.350 kg water, 0.84 kg O2, 0.62 kg food) came from secondary pages and are not used; led to two NTRS records |
| 55 | 2026-10-11 | Downloaded: Ewert and Stromgren (NASA JSC), "Astronaut Mass Balance for Long Duration Missions", ICES-2019-126, NTRS 20190027563 | thin | Background only (urine and drinking-water figures); not the supply rates needed |
| 56 | 2026-10-11 | NTRS full text: "Logistics Rates and Assumptions for Future Human Spaceflight Missions Beyond LEO" (NASA LaRC and JSC), NTRS 20230012635, submitted 28 Aug 2023, Tables 1, 2, 8 | useful | Per crew member-day (82 kg crew, in space): food 2.39 kg as delivered; O2 0.89; drinking water 2.79; rehydration 0.50; hygiene 0.40; flush 0.30 kg |
| 57 | 2026-10-11 | WebSearch: `Ember Global Electricity Review 2026 world electricity generation 2025 TWh total demand` | useful (summary only) | 31,779 TWh (2025) appears in the search summary of Ember's pages |
| 58 | 2026-10-11 | WebFetch and curl: ember-energy.org Global Electricity Review 2026, "2025 in review" | dead at the sources | HTTP 403 and a JavaScript bot check; the 31,779 TWh figure could not be read on the page itself |
| 59 | 2026-10-11 | WebSearch: `IEA Electricity 2026 report global electricity demand 2025 growth TWh` | thin | Trade press quoting IEA: demand up "about 3%", "about 800 TWh" in 2025; consistent with Ember's +849 TWh; IEA page not opened |
| 60 | 2026-10-11 | WebSearch: `OSIRIS-REx sample return capsule mass kg Bennu sample mass 121.6 grams NASA`; WebFetch blogs.nasa.gov (301 redirect, not followed); NTRS 20240010710 abstract | thin | Capsule mass (46 kg) only from secondary summaries; the NTRS abstract does not give the totals; not used |
| 61 | 2026-10-11 | WebSearch: `Kornuta et al. 2019 "Commercial lunar propellant architecture" REACH propellant price LEO $ per kg internal rate of return` | dead at the sources (for Kornuta) | Paywalled at ScienceDirect; its figures enter this file only through Metzger 2023. Led to NTRS 20200002704 |
| 62 | 2026-10-11 | Downloaded: Jones et al. (NASA LaRC), "Cost Breakeven Analysis of Lunar ISRU for Human Lunar Surface Architectures", IAC-19-D4.5.15, Oct 2019, NTRS 20200002704 | useful | Breakeven times 1.1 to 6.9 yr at 8.5 to 34 t/yr; none for 1-yr MREE plants; technology development cost excluded |
| 63 | 2026-10-12 | curl: https://physics.nist.gov/cuu/pdf/sp811.pdf | dead at the sources | Returned an HTML page, not the PDF |
| 64 | 2026-10-12 | curl: NIST, *Guide for the Use of the SI* (SP 811), Appendix B.9 conversion factors (web page) | useful | Troy ounce 3.110348 x 10^-2 kg; pound 0.4535924 kg; short ton 907.1847 kg; gallon from the gal/(hp h) entry |
| 65 | 2026-10-12 | Re-read Metzger 2023 reference list (refs. 5 and 6) to identify the "97% more expensive" study | useful | Ref. 6 is Jones, Klovstad, Judd, Komar, AIAA SciTech 2019, a different paper from row 62 by the same group; Charania and DePasquale, IAC 2007 |
| 66 | 2026-10-12 | Ran `python3 -I calc_value.py` (scratch subfolder) | useful | Output in `calc_value_output.txt`; key lines in *Derived figures* |

*Dates: rows 1 to 8 were run on the evening of 2026-10-11; rows 9 to 62 between 23:41 on 2026-10-11 and the early hours
of 2026-10-12 (the log keeps the start date for those rows); rows 63 onward on 2026-10-12.*

## Findings

Evidence marks: **DEMONSTRATED** (a price actually paid or a market actually observed), **ENGINEERING-STUDIED** (a
price or cost assumed or computed in a quantitative study), **SPECULATIVE** (a projection or a concept with no hardware),
**DERIVED** (arithmetic here from sourced inputs; formula in *Derived figures*).

### A. Terrestrial reference prices and market sizes (checklist 1, terrestrial part; checklist 4 market sizes)

Short names: **USGS MCS 2026** = U.S. Geological Survey, *Mineral Commodity Summaries 2026* (Feb 2026), chapter named,
https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-<chapter>.pdf. **Pink Sheet** = World Bank, *Commodity Markets
Outlook Pink Sheet*, February 2026 (annual averages 2023 to 2025). Conversions by NIST SP 811 App. B.9 (D1).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Iron ore | **$0.100/kg** (62% Fe fines CFR China, $100.2/dmt, 2025); $120.6 (2023), $109.4 (2024) | Pink Sheet | Primary (dataset) | USGS MCS 2026 iron-ore: US mine unit value $89/t (2025e), CFR Tianjin $99.07/t Jan to Sep 2025 | High |
| Raw steel (value) | **about $1.82/kg** (DERIVED: US raw steel 82 Mt sold for about $149 billion, 2025) | USGS MCS 2026 iron-steel | Primary | Scrap No. 1 HMS $319/t delivered (USGS iron-steel-scrap); producer price index 290 (1982 = 100) | Medium (a sales value, not a quoted price) |
| World steel and iron output | Raw steel 1,900 Mt, pig iron 1,300 Mt (2025e) | USGS MCS 2026 iron-steel | Primary | none sought | High |
| Aluminum | **$2.63/kg** (LME, 2025 average $2,632/t); US spot 180 c/lb = $3.97/kg | Pink Sheet; USGS MCS 2026 aluminum | Primary | each other (the US spot carries tariffs and premiums) | High |
| World primary aluminum | 74,000 kt (2025e) | USGS MCS 2026 aluminum | Primary | none | High |
| Silicon metal | **$2.87/kg** (130 c/lb, US 2025e); ferrosilicon 75% $3.09/kg | USGS MCS 2026 silicon | Primary | none | High |
| Magnesium | $7.06/kg (US spot, $3.20/lb); $2.50/kg (Europe, $2,500/t), 2025 | USGS MCS 2026 magnesium-metal | Primary | the two regional prices differ by 2.8x | High (as stated) |
| Copper, nickel | $9.95/kg; $15.16/kg (LME 2025) | Pink Sheet | Primary | none | High |
| Cobalt | $46.3/kg (US spot cathode, $21/lb, 2025e) | USGS MCS 2026 cobalt | Primary | LME cash $15/lb | High |
| Gallium | $580/kg (import unit value, 2025e) | USGS MCS 2026 gallium | Primary | none | Medium (unit value, export controls in force) |
| Platinum | **$41,090/kg** ($1,278/troy oz, 2025 average); December 2025 $1,893/oz, January 2026 $2,434/oz | Pink Sheet | Primary | USGS MCS 2026 platinum-group: $1,200/oz (2025e) = $38,580/kg | High for 2025; the price rose 90% between 2025 average and January 2026 (volatile) |
| Palladium, iridium | $35,370/kg ($1,100/oz); $141,460/kg ($4,400/oz), 2025e | USGS MCS 2026 platinum-group | Primary | none | High |
| PGM world mine output | Platinum 170 t, palladium 190 t (2025e); reserves above 76,000 t; resources above 100,000 t | USGS MCS 2026 platinum-group | Primary | Nachtrieb and Smith 2026 quote 179/170 t Pt, 208/190 t Pd (2023/2024), same agency | High |
| PGM market size | Pt about $7.0 B/yr, Pd about $6.7 B/yr (DERIVED D4) | from rows above | Derived | none | Medium |
| Gold | $110,660/kg ($3,442/oz, 2025) | Pink Sheet | Primary | none | High |
| Helium | **about $70.8/kg** (Grade-A base price about $12 per m^3, 2025, excluding delivery; USGS volume basis 27.737 m^3 at 15 C = 0.0047 t, i.e. 0.1694 kg/m^3); world production 190 million m^3 = about 32,200 t/yr (2025e); world market about $2.3 B/yr (DERIVED D2, D4) | USGS MCS 2026 helium | Primary | none found for price | High for production; medium for price ("producers posting surcharges") |
| Xenon, krypton prices | **Not available**: USGS states "Price data for rare gases were unavailable"; NASA's 2015 xenon paper gives the price history only as a figure | USGS MCS 2026 helium; Herman and Unfried, NTRS 20150023080 | Primary | Vendor-blog figures found but rejected (Rejected sources) | n/a (gap) |
| Xenon world production | 12 million L/yr (2025) = **70.8 t/yr** at 5.898 kg/m^3 (NIST, 0 C, 1 atm; D4); about 53 t/yr (2015 paper); 65 t/yr ([TR] F3, Lindner 2023) | USGS MCS 2026 helium; Herman and Unfried 2015 | Primary | three sources, 53 to 71 t/yr, rising | High |
| Helium-3 price | Historic auction $40 to $85 per liter (STP); DOE allocated $365 to $1,000/L (2009 to 2011); "commercial prices rising to $2,000 per liter or more"; **$2,000/L = $14.9 million/kg** (7,432 L/kg at STP, D2) | Congressional Research Service, Shea and Morgan, R41419, 6 Oct 2011 | Primary (CRS) | Interlune/DOE purchase (May 2025): 3 L at "approximately today's commercial market price", no figure | Medium (2011 data; current price unconfirmed by a primary source) |
| Helium-3 supply | About 8,000 L/yr from tritium decay (2011); 2008 demand about 80,000 L; world production 40,000 L in 2024 and 2025 (= 5.4 kg/yr) | CRS R41419; USGS MCS 2026 helium | Primary | two dates, two agencies | Medium-high |
| Liquid hydrogen (delivered, US government) | **$8.72/kg** (Air Products, up to 36.5 million lb for up to $144.4 M) and $12.86/kg (Plug Power, 0.48 million lb for $2.8 M), maximum values, Dec 2025 to Nov 2030 | NASA, "NASA Awards Liquid Hydrogen Supply Contracts", 21 Nov 2025 | Primary | none | Medium (maximum contract values, not unit prices) |
| Liquid oxygen and nitrogen (delivered, US government) | **about $0.44 to $0.47/kg** combined average (six awards, $153.0 M maximum, about 243,000 tons plus 2.1 M gal of LOX and 30.4 M gal plus 656.8 tons plus 740,000 L of LN2, Jul 2024 to Jun 2029; D3) | NASA, "NASA Awards Contracts for Acquisition of Liquid Nitrogen, Oxygen", 6 Jun 2024 | Primary | Google 2025 preprint assumes LOX at $200/t ($0.20/kg); ULA (Kutter 2016): Earth-surface LO2/LH2 "a negligble $1/kg" | Medium (a bound: maximum values, LOX and LN2 not separated, "tons" undefined) |
| Fixed nitrogen | Ammonia $0.50/kg (Gulf Coast, $450/short ton, 2025) | USGS MCS 2026 nitrogen | Primary | none | High |
| Electricity | US 2025 averages: industrial **8.62 c/kWh**, all sectors 13.63 c/kWh | EIA, *Electric Power Monthly* Table 5.3, released 24 Sep 2026 | Primary (dataset) | NASA OTPS 2024: terrestrial renewables $0.02 to $0.05/kWh (2050 projections) | High |
| World electricity | 31,779 TWh in 2025 (+2.8%, +849 TWh) | Ember, *Global Electricity Review 2026* (figure from the search summary; page blocked) | Secondary access to a primary dataset | IEA via trade press: about +3%, about +800 TWh | Medium |

### B. What space delivery actually costs, and the prices published analyses assume (checklist 1, space part)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Launch to LEO, list prices | Falcon Heavy $1,500/kg (2021 $) = $1,782/kg in 2025 $ (D5); 2025 average across all launchers $3,868/kg (2024 $); learning rate 21.2% per doubling (DEMONSTRATED) | [TR] F5 (CSIS/OWID); [RM] F2 (Terzi and Nicoli 2026) | Primary (via siblings) | Google 2025 preprint uses $3,600/kg as today's reference and about $1,800/kg for Falcon Heavy | High |
| Launch to LEO, study assumptions | NASA: $1,000/kg baseline ($850 with block discount), $500 ($425) low case; trend $615/kg in 2040 (ENGINEERING-STUDIED) | [TR] F5 (NASA OTPS 2024) | Primary | Google: "≲$200/kg by the mid-2030s" if a ~20% learning rate holds, needing about 370,000 t more cumulative launched mass (about 1,800 Starship launches); ≲$60/kg at 10x reuse, ≲$15/kg at 100x; propellant floor about $8/kg (SPECULATIVE) | Medium (assumptions) |
| Cargo actually delivered to a station | **$63,200/kg** (CRS-1, 93,800 kg capability for $5.93 B) and **$71,800/kg** (CRS-2 projected, 87,900 kg for $6.31 B); about $81,000 to $92,000/kg in 2025 $ (D5, indicative) (DEMONSTRATED) | NASA OIG, IG-18-016, 26 Apr 2018, Table 3 | Primary | Calla et al. 2018 assume $3,000/kg for water in LEO | High. **Delivered-and-integrated cargo costs 16 to 40 times the bare 2025 launch price ($1,782 to $3,868/kg); the contract prices are in their own years' dollars** |
| Cargo actually delivered to the lunar surface | **about $1 million/kg** (NASA's 2019 estimate) and **about $1.2 million/kg** (2023 task orders), small payloads (DEMONSTRATED prices) | NASA OIG, IG-24-013, 6 Jun 2024 | Primary | gear-ratio floor $14,000 to $31,000/kg (D6) | High |
| Price of propellant offered in space (a buyer's bid) | ULA's offer: **$3,000/kg in LEO, $1,000/kg in GEO, $500/kg on the Moon** ($3M, $1M, $0.5M per t), set so that its business case closes (ENGINEERING-STUDIED; a published bid, never transacted) | Kutter (ULA), "Cislunar-1000", AIAA Space 2016; Sowers, House testimony, 2017 ("$500/kg" lunar surface, "$1000/kg" at EML1) | Primary (company paper; testimony) | ULA slides (4 Mar 2017) chart: $0.001k/kg on Earth to $35k/kg in low lunar orbit if shipped from Earth | Medium |
| Price of water in space assumed by techno-economic studies | Hein et al.: water **$20,000/kg**, transport $35,000/kg; Calla et al.: LEO $3k, GTO $7.5k, GSO $21.5k, cislunar $35k per kg (ENGINEERING-STUDIED) | Hein, Matheson, Fries, IAC-18, arXiv 1810.03836, Table 1; Calla, Fries, Welch, arXiv 1808.05099 (2019), Table 6 | Primary (conference and preprint) | Kutter's bid is 7 to 40 times lower | Low (the studies equate the price of space water with the cost of launching it, at pre-2018 prices) |
| Transport gear ratios (LEO mass per unit delivered) | L5: "roughly 4 times the payload"; L2 or lunar surface: 8 times (falling to about 2 and 3.3 with oxygen from L5); Mars surface: "about 10kg per ever[y] 1 kg" of propellant made there; GTO payload fraction about 2% from Earth vs about 48% from the Moon | SP-413 Ch. 6 via [LEO] D7; Kleinhenz and Paz, AIAA 2017-0423, NTRS 20170005179; Metzger 2023 Sec. 3.1 | Primary | ULA: "about 4 tons of propellant to transport 1 ton to LEO" from the Moon | Medium-high |
| Floor price of Earth-launched mass at each destination (launch price x gear ratio, propellant only) | GEO/L5 $7,100 to $15,500/kg; lunar surface $14,300 to $30,900; low Mars orbit $6,400 to $13,900; Mars surface $17,800 to $38,700; **low Mercury orbit $22,400 to $48,500**; at a $200/kg launch price: $800, $1,600, $720, $2,000, $2,500 (DERIVED D6) | from rows above and [TR] D1 | Derived | real delivered prices are far above these floors (CRS 16 to 40x launch; CLPS 32 to 84x the lunar floor) | Medium (floors, not prices) |
| Elasticity of launch demand | Threshold below which launch demand becomes price-elastic: $2,200/kg (Andrews and Andrews) to $6,100/kg (Ross et al.) in 2022 $ ($2,420 to $6,710 in 2025 $); implied elasticity about 1.9 since 2005, about 3.8 if the post-2019 trend is real; orbital mass added about 140 t/yr (1980 to 2005), about 280 t/yr (from 2005), about 550 t/yr (from 2019) | Metzger 2023, Sec. 4.7 to 4.8 (citing the originals) | Secondary (a preprint quoting primary studies, which were not opened) | none | Medium-low ("crude", in the author's word) |
| Propulsion hardware first-unit cost | Gateway Power and Propulsion Element: **$375 M at award (May 2019), $453.6 M by 2020** (60 kW arrays, 48 kW of electric propulsion, [TR] F2), about $7.6 M per kW of array (DEMONSTRATED contract value, first unit) | NASA OIG, IG-21-004, 10 Nov 2020 | Primary | Hein et al. specific cost $10,000/kg (mass-production) to $1,000,000/kg (SMAD) of spacecraft | Medium (development plus one unit; no production-rate figure exists) |
| Spacecraft specific cost used for transport capital | **$10,000/kg** (optimistic, OneWeb-like mass production) to **$1,000,000/kg** (conservative, SMAD) | Hein et al. 2018, Tables 1 and 2 | Primary (conference preprint) | Calla et al.: first unit $113.6 M for a sub-500 kg craft (over $227,000/kg) | Low-medium: a 100-fold range is the honest state of knowledge |

### C. Published break-even analyses: assumptions, results, sensitivities, disagreements (checklist 2)

| Study | Assumed prices and market | Break-even result | Sensitivity (as the study reports it) | Source | Primary or secondary | Confidence |
|---|---|---|---|---|---|---|
| **Sonter 1998** (NEA volatiles) | Initial LEO market "about 1000 tonnes per year"; launch then $10,000/kg, expected to fall to "something like $500/kg"; mass payback "factors above 100" as the aim | "economically feasible, using present technology" for a teleoperated miner (ENGINEERING-STUDIED) | The forecast LEO market "by 2010" did not appear (world launched mass was 3,193 t in 2025) | [TR] F5, F7 | Primary (via sibling) | Low for the market; medium for the method |
| **SP-428 IV-2, 1977** (asteroid retrieval) | 10^6 t asteroid captured; Shuttle-era launch costs | **$24/kg** of captured mass, $4/kg excluding RDT&E (1977 $); **$128/kg and $21/kg in 2025 $** (D5) | Its launch-cost basis did not happen (Shuttle reached $61.7 k/kg in 2018 $) | [TR] F5 | Primary (via sibling) | Low |
| **Hein, Matheson, Fries 2018** (NEA water and platinum) | Water $20,000/kg in space; platinum $70,000/kg and $30,000/kg cases; transport $35,000/kg; production cost $10,000 to $1,000,000/kg of spacecraft; 10% discount rate in the NPV part | Water: 5.9 yr (conservative) or 0.26 yr (optimistic) to break even at a throughput of 2.3 x 10^-4 kg/s per kg; platinum (ore grade 10^-5): 5.5 or 0.25 yr, but only at 0.35 kg/s per kg, i.e. the spacecraft "would need to be able to process the equivalent of its own mass within 3 seconds"; at $30,000/kg platinum, the conservative case breaks even within 10 yr only with ten small craft per mission (ENGINEERING-STUDIED) | Halving throughput "would render [it] not profitable"; supply-demand model: "only a slim range" of elasticity and supply-response values is profitable, "an even slimmer range" breaks even within 30 years; Earth-return cost taken as twice launch cost | arXiv 1810.03836 (IAC-18), Tables 1 and 2, Secs. 3.3, 4.1 | Primary (conference preprint) | Medium-low |
| **Calla, Fries, Welch 2019** (NEA water, small craft) | Water priced at Earth-launch cost: $3k (LEO) to $35k/kg (cislunar); first spacecraft $113.6 M; Falcon Heavy $90 M | About **200 spacecraft (about $7 B up front)** to break even within 10 years; "does not become profitable in less than 8 years and does not significantly profit from decreasing launch prices" (ENGINEERING-STUDIED) | Profit rises with water price, but launch cost rises with it in their model; learning-curve slope dominates at large fleet sizes | arXiv 1808.05099 v2, Secs. 4 and 5 | Primary (preprint) | Medium-low |
| **Metzger 2023** (review of six lunar-propellant TEAs plus his own model) | Launch $2,000/kg falling to $30/kg (optimistic, 436 kt/yr up-mass by year 30), $119/kg (moderate), $436/kg (pessimistic); discount rate 21.7% falling to 12% (baseline) or 12% constant (public-private) | Competitiveness is set by the capital transport "gear ratio" G and the production mass ratio φ (product per unit of capital mass per year); competitive when φ is about 35 or more; tent sublimation φ = 441.8 (Kornuta) and 534 (Sowers); "Lunar-derived rocket propellant can outcompete rocket propellant launched from Earth, no matter how low launch costs go"; Sowers' fully commercial IRR 8.84% against the 21.7% "thought necessary" (ENGINEERING-STUDIED) | Market size has "negligible effect until about 10 years of operation and only a minor effect after that"; at 12% all studies except two reach absolute advantage in GTO by year 10; reliability is the decisive open question ("proof of operability for years in the lunar environment and especially the dust") | arXiv 2303.09011, Secs. 3.1, 4.7, 4.8, 4.13, 6.4, 7, Table A-1 | Primary (preprint; the author argues a position) | Medium |
| **The six TEAs Metzger reviews disagree** | Charania and DePasquale (IAC 2007; Metzger's text spells it "DePascuale", his reference list "DePasquale"): lunar propellant to GEO "does not provide an attractive alternative"; Jones et al. (AIAA SciTech 2019): "97% more expensive than Earth-based propellant"; Bennett et al.: "well below" Jones's cost; Kornuta and Sowers: viable | n/a | Shisko (quoted): "the wide range of quantitative results is a consequence of the different assumptions, parameters, and analysis methods" | Metzger 2023 Sec. 1 | Secondary (quotes; originals not opened, except Jones 2019 below) | Medium |
| **Jones et al. 2019** (NASA LaRC, lunar surface ISRU vs delivery from Earth) | Demand 8.5, 17.0, 34.0 t/yr of propellant on the lunar surface (17.0 t per crewed sortie of a reusable lander) | Break-even after 1.1 to 6.9 yr depending on plant and demand; MREE plants with a 1-yr life never break even; with 5-yr life, 62 to 66% of the trade space breaks even, only 3 to 28% "breaks even well" (cost ratio below 0.5); **"the costs of developing the necessary technologies to support a highly reliable and autonomous lunar ISRU system were not included"** (ENGINEERING-STUDIED) | ISRU lifetime is the strongest lever | Jones et al., IAC-19-D4.5.15, NTRS 20200002704, Tables 3 and 4 | Primary | Medium-high (as a NASA model) |
| **NASA OTPS 2024** (space solar power to Earth) | Launch $1,000/kg (baseline), $500/kg (low); 2 GW systems; 10-yr hardware life, 30-yr system | LCOE **$0.61/kWh** (RD1) and **$1.59/kWh** (RD2), 12 to 31 and 32 to 80 times terrestrial renewables' 2050 projections ($0.02 to $0.05/kWh); launch 71 to 77% of cost (ENGINEERING-STUDIED) | Lower launch cost or electric orbit raising alone: about $0.20 and $0.50/kWh; all favorable assumptions together: $0.03 and $0.08/kWh (cost competitive) | Rodgers et al., NASA OTPS, 11 Jan 2024 | Primary | Medium-high (as a NASA study) |
| **Google 2025** (computation in orbit) | Launch $3,600/kg now, ≲$200/kg by about 2035 | At $200/kg, "launched power price" about $810/kW/yr (Starlink v2 class) to $7,500/kW/yr, against $570 to $3,000/kW/yr spent on power by US terrestrial data centers; at $3,600/kg, $14,700 to $135,800/kW/yr (SPECULATIVE) | "learning curve estimates are highly sensitive to input assumptions"; reaching $200/kg needs about 180 Starship launches a year | arXiv 2511.19468 v2, Sec. 2.4, Table 1 | Primary (company preprint) | Medium-low |
| **Nachtrieb and Smith 2026** (asteroid PGM flood) | Market 400 t/yr at $60 M/t; gross margin 0.1 now, 0.8 for early asteroid miners | Price falls toward the asteroid cost: **$60 M/t to $11 M/t (a factor of 5.5)**; market revenue $24 B/yr to $4.4 B/yr; total market profit peaks at eight times today's before falling (SPECULATIVE: a back-of-envelope and system-dynamics sketch; asteroid costs assumed, not derived) | Demand held constant in the sketch; the simulation adds demand growth at lower price | arXiv 2607.06806 (MIT Sloan, 2026), Table III | Primary (preprint; non-peer-reviewed) | Low |

**Where they agree:** volatiles sold in space are the first product that closes in every study that models it; platinum
returned to Earth is the hardest; throughput per kilogram of equipment, equipment lifetime and reliability decide the
result more than the market price does. **Where they disagree:** the sign of the lunar-propellant result (Charania and DePasquale, IAC 2007; Jones, Klovstad, Judd,
Komar, "Cost breakeven analysis of cis-lunar ISRU for propellant", AIAA SciTech 2019, the "97% more expensive" result;
vs Kornuta, Sowers, Bennett, Metzger). **The same NASA Langley group's later IAC-19 paper (row above) finds lunar-surface
ISRU breaking even at high demand and multi-year plant life.** The scope (propellant delivered to cislunar space vs used
on the lunar surface) changes the answer. Metzger and Shisko attribute the spread to architecture choices (G, φ) and
assumptions rather than to physics. No published study prices any material from Mercury, Venus or the solar wind.

### D. Demand sinks in space, and a demand curve by scale of enterprise (checklist 3)

Masses below are from the earlier files and two new primary sources; none is re-derived. "Open loop" means no recycling.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Crew consumables, open loop, per crew member-day (82 kg crew, in space) | Food 2.39 kg as delivered (of which 0.40 packaging); metabolic oxygen 0.89; drinking water 2.79; rehydration water 0.50; hygiene 0.40; flush 0.30 kg; **total 7.27 kg/day = 2.66 t per person-year** (DERIVED D14) | NASA LaRC/JSC, "Logistics Rates and Assumptions for Future Human Spaceflight Missions Beyond LEO", NTRS 20230012635 (2023), Tables 1, 2, 8 | Primary | ISS reserve rule: 45 days of food, 290 kg O2, 1,034.5 L water ([NW] F11) | High (as NASA planning rates) |
| Mars ascent propellant (one crewed ascent) | 6,978 kg CH4 + 22,728 kg O2 = **29.7 t** (from 15,701 kg water and 19,190 kg CO2) | Kleinhenz and Paz, AIAA 2017-0423, NTRS 20170005179 | Primary | DRA 5.0 three-mission mass 2.5 to 3.8 kt to LEO ([RM] D7) | High as a study |
| Lunar sortie propellant | 17.0 t per mission on the lunar surface (reusable lander, crew of two) | Jones et al. 2019, NTRS 20200002704 | Primary | none | Medium |
| Lunar propellant business case | 210 t/yr delivered to LEO from 1,050 t made on the Moon from 1,575 t of water (three ACES flights a year) | Kutter 2016 Table 1 | Primary (company) | Metzger optimistic market: 436 kt/yr up-mass equivalent by year 30 | Medium |
| One rotating habitat for 10,000 (SP-413 torus) | Structure 150 kt, **shield 9.9 Mt**, air 44 kt: about 98% unprocessed shielding | [LEO] D3, D6; [PR] 6 | Primary (via siblings) | Kalpana One: about 7 Mt with regolith shielding for 3,000 people | High as a design |
| One O'Neill-type cylinder (820,000 people) | Structure 42.3 Mt, shield 23.3 Mt, air 14.6 Mt (about 80 Mt) | [LEO] D3 | Primary (via sibling) | none | High as a design |
| Solar power satellites | 34,000 to 51,000 t per 5 GW (DOE/NASA 1978); 5.9 Mkg (RD1) or 10 Mkg (RD2) per 2 GW (NASA 2024); SP-428: 9% terrestrial chemical feedstock per SPS | [PR] 6; NASA OTPS 2024; [RM] F3 | Primary | each other within about 2x per GW | Medium |
| Earth-orbit receiver capacity | One SP-413 catcher 0.32 Mt/yr; five installed for 11 Mt in 10 yr | [TR] F4 | Primary (via sibling) | none | Medium |
| Today's whole demand for mass in orbit | 3,193 t launched in 2025; 16,185 t cataloged in orbit | [TR] F3 (McDowell 2026) | Primary (via sibling) | Metzger: orbital mass added about 550 t/yr since 2019 | High |

**Demand curve by scale (DERIVED from the rows above; open-loop consumables are an upper bound, since the ISS recycles
most of its water and oxygen):**

| Scale of enterprise | Consumables (open loop) | Propellant | Structure and shielding | Order of the yearly bulk demand |
|---|---|---|---|---|
| Crewed outpost, 4 people | 11 t/yr | 17 to 34 t/yr (lunar sorties) | ISS-class station, 420 t, once | 10 to 100 t/yr |
| Mars landing campaign, one ascent per 2.1 yr | small | 29.7 t per ascent (about 297 t of LEO mass avoided at 10:1) | 2.5 to 3.8 kt to LEO per three missions | about 100 t/yr at Mars |
| Small base, 20 people; survival-minimum colony, 110 | 53 t/yr; 292 t/yr | tens to hundreds of t/yr | 280 t of hardware for 20 people ([SYN] 6) | 100 to 1,000 t/yr (Sonter's "about 1000 tonnes per year" first market) |
| One SP-413 torus over 10 years | 26,600 t/yr for 10,000 people (open loop) | ship-scale | 10.1 Mt, of which 9.9 Mt shield (about 1 Mt/yr) | about 1 Mt/yr |
| One SPS a year | n/a | refueling dominates the launches (12 of 13 in NASA's case) | 34 to 51 kt per 5 GW | 10 to 100 kt/yr |
| One O'Neill cylinder over 10 years | 2.7 Mt/yr at 1 million people (open loop) | n/a | about 80 Mt | about 8 Mt/yr |

**Reading:** the first thousands of metric tons a year are propellant and consumables (water first); everything above about
10^5 t/yr is **shielding and structure**, i.e. the cheapest material by value. **The material the big sinks need most is
worth least per kilogram:** shielding has no market value beyond "not having to launch it", so its price ceiling is the
destination's floor price of Earth-launched mass (B, D6), and at Mt/yr no Earth launch can supply it at all (1 Mt/yr is
313 times the 2025 world launched mass, [TR] F3).

### E. Demand on Earth: what could earn a return on the ground (checklist 4)

| Product | Earth market (2025) | Value per kg on Earth | What a space source must beat | What a flood does | Source and confidence |
|---|---|---|---|---|---|
| **Platinum-group metals** | Pt 170 t + Pd 190 t, about $14 B/yr (D4); reserves above 76,000 t | $35,000 to $41,000/kg (Pt, Pd); Ir $141,000/kg | Earth return: Hein take twice the launch cost; ore grade 10^-5 needs 0.35 kg processed per second per kg of spacecraft (C) | Nachtrieb and Smith: price falls 5.5-fold toward the asteroid cost once supply shifts; Hein: profitable only in "a slim range" of elasticity; Pt is also "a speculative asset" (Hein), and its price rose from a $1,278/oz average in 2025 to $2,434/oz in January 2026 (Pink Sheet), a 90% move with no space supply at all | USGS, World Bank (high); flood models (low) |
| **Helium-4** | 190 million m^3 = about 32,000 t/yr, about $2.3 B/yr | about $71/kg | Any space return costs far more than $71/kg (Earth-return floor alone exceeds launch price) | n/a: no space source supplies helium-4 at a competitive price on any figure found | USGS (high) |
| **Helium-3** | 40,000 L/yr = **5.4 kg/yr** (2025); demand about 80,000 L in 2008 | $0.3 M/kg (historic auction) to **$14.9 M/kg** at $2,000/L | A market of about $80 M/yr at $2,000/L (D4): one lunar regolith plant at 4 to 20 ppb ([ML] A5) would process 50,000 to 250,000 t of regolith per kg | The market is so small that kilograms per year would saturate it; the CRS report shows the price itself was set by DOE allocation, not a free market | CRS 2011, USGS 2026 (medium) |
| **Electric power from space** | World about 31,779 TWh; at US industrial 8.62 c/kWh, indicatively $2.7 T/yr (D4) | n/a | NASA: $0.61 to $1.59/kWh baseline against $0.02 to $0.05/kWh terrestrial; each kg of RD1 hardware in GEO earns at most $1,800 to $4,500 over 30 years at terrestrial prices (undiscounted; D13) | n/a (a new supply, priced against terrestrial LCOE) | NASA OTPS (medium-high) |
| **Computation in orbit** | US data-center power spend $570 to $3,000 per kW per year (Google, citing others) | n/a | Launched power $810 to $7,500/kW/yr at $200/kg launch; $14,700 to $135,800 at $3,600/kg | n/a | Google 2025 preprint (medium-low) |
| **Bulk metals, silicon, oxygen, nitrogen, water** | Steel about 1,900 Mt/yr; aluminum 74 Mt/yr | $0.10 (iron ore) to $10 (copper) per kg; LOX $0.20 to $0.47/kg | Earth return of any bulk material: **impossible to compete**; terrestrial prices are about 180 to 39,000 times below today's launch price ($1,782 to $3,868/kg against $0.10 to $10/kg), and Hein et al. price the trip down to the surface at twice the launch cost (their stated "rough estimate") | n/a | USGS, World Bank (high) |
| **Xenon** (as a market a space industry would consume, not supply) | 53 to 71 t/yr world production | price unavailable from any primary source | n/a | NASA (2015): a single 10 t purchase is over 10% of world output and "can disrupt the xenon market, driving up pricing" | NASA, USGS (high for supply) |

**Reading:** on the sourced numbers, only materials worth tens of thousands of dollars per kilogram or more can even in
principle pay for a return to Earth's surface (PGMs at $35,000 to $141,000/kg, helium-3 at up to $14.9 M/kg), and both
markets are small enough (about $14 B/yr and about $0.08 B/yr) that the supply needed to make a profit is the supply
that collapses the price. Power (via beaming) and computation are the two products whose Earth market is large; neither
is a *material* delivered to Earth, and both currently cost 10 to 80 times their terrestrial equivalents in the studies.

### F. Transport cost per kilogram on each inner-system route (checklist 5)

**Basis (all DERIVED; arithmetic D7 to D11, D16).** Capital per kg delivered = hardware mass x specific cost x capital
recovery factor / yearly delivered mass. Inputs: tug dry mass 68 kg/kW and cargo productivity per kW-year from [TR] D3
and [NW] F6; tug life 6.34 yr (AEPS 50,000 h design life, [TR] F2, at the 90% duty of [NW] F6); hardware specific cost
$10,000/kg (optimistic) to $1,000,000/kg (conservative) (Hein et al.); discount rates 7%, 12%, 21.7% (section H).
Operations, insurance, development and the receiving node are **not** included, so every figure is a **lower bound** on
cost. Propellant is priced, where needed, at the LEO launch price ($1,782 to $3,868/kg), also a lower bound (it excludes
moving it from LEO to where the tug refuels, and the propellant's own price, which for xenon has no primary source).

| Route and carrier | Energy or propellant per kg delivered (sourced) | Capital per kg delivered, hardware at $10k/kg | Same at $1M/kg | Status of the inputs |
|---|---|---|---|---|
| Lunar surface to L2, mass driver plus catchers, 1 Mt/yr of ore (SP-413 base: 17,050 t from Earth, 402 t/yr imports) | 2.88 MJ = 0.80 kWh/kg ([TR] F2); $0.07/kg at 8.62 c/kWh (scale only) | **$29 to $110/kg** (emplacement at 8 x LEO price of $200 to $1,782/kg; 10-yr life; 7 to 21.7%) | **$5,800 to $10,000/kg** (emplacement at CLPS $1.2 M/kg) | ENGINEERING-STUDIED masses (1975); never built |
| Moon or cislunar to LEO-class orbit, solar-electric tug, 3.4 km/s leg | 0.18 kg propellant per kg ([TR] D4) = $321 to $696 at LEO price | $489 to $743/kg | $48,900 to $74,300/kg | ENGINEERING-STUDIED tug (Cassady 2022); no return leg counted |
| Lunar propellant by reusable chemical vehicles (Metzger's architectures) | one of his cases: propellant gear ratio LEO to lunar surface G = 10 (with extra refueling in low lunar orbit) | not re-derived; Metzger: competitive for φ ≥ about 35 | n/a | ENGINEERING-STUDIED (preprint) |
| Near-Earth asteroid water to cislunar space, small craft | 437 m/s per one-way trip (Calla) | published: 200 craft, about $7 B, to break even in 10 yr (Calla); 0.26 to 5.9 yr at $20,000/kg (Hein) | | ENGINEERING-STUDIED |
| Main belt 2.2 AU to low Mars orbit, solar-electric tug (3.76 km/s, 464 d; scaled by trip time from the Cassady case) | about 0.18 kg/kg (similar delta-v) | **$625 to $949/kg** one way; **$1,250 to $1,900/kg** with an empty return | $62,500 to $190,000/kg | DERIVED by crude scaling; no belt cargo-fleet study exists ([ISM] 6) |
| Low Mercury orbit to Earth vicinity, solar-electric spiral (22.4 km/s each way) | **2.4 kg propellant per kg** ([NW] F6) = $4,300 to $9,300 at LEO price; xenon fails at 1 kt/yr (37 x world output) | **$3,300 to $10,900/kg** (capped-1/r^2 to flat power) | $333,000 to $1,090,000/kg | DERIVED from [NW] F6 |
| Low Mercury orbit to Earth vicinity, photon sail (0.78 to 2.0 kg of sail per kg/yr of flow) | none | **$1,100 to $21,400/kg** (sail life 10 to 1 yr; no measured life exists) | $111,000 to $2,140,000/kg | DERIVED from [NW] F6(c); sail lifetime unknown |
| Low Mercury orbit to Earth vicinity, solar-electric with flybys | about 63 t xenon per kt (about 0.063 kg/kg); 9.8 yr in flight | capital not derivable (no stage cost); the time cost alone multiplies cargo value by 1.9 to 6.8 (H) | | STUDY reversed ([NW] F6(a')) |
| Mercury surface to Mercury escape, mass driver | 9.03 MJ = 2.51 kWh/kg ([TR] D5); $0.22/kg at 8.62 c/kWh (scale only) | no Mercury launcher design exists to cost ([ISM] 3) | | DERIVED energy only |
| Venus cloud deck to orbit, expendable two-stage rocket (Seager VAV) | 162.6 kg propellant and **20.4 kg of vehicle hardware per kg** to orbit | **$204,000/kg** (hardware only; building and delivering the vehicle to the clouds not counted) | **$20.4 M/kg** | ENGINEERING-STUDIED vehicle (sample-return scale) |
| Solar wind, passive collection | yield ceiling 0.146 mg/m^2/yr at 1 AU, 1.6 at 0.3 AU, 14.6 at 0.1 AU (from 1.3 x 10^9 kg/s; Genesis measured 0.12 mg H/m^2/yr) | collector at even a sail's 5.9 g/m^2 costs $59/m^2; at the most generous price ($3,000/kg, all matter sold, no transport) it earns $0.044/m^2/yr at 0.1 AU: **payback about 1,350 years** | | DERIVED; no collector design exists ([SYN] 2) |

### G. The break-even table (checklist 6)

What each destination will pay is set by **its cheapest alternative**, which for every in-space destination is
Earth-launched mass at the floor prices of B (D6): LEO $1,782 to $3,868/kg today ($200 to $1,000/kg in the study
futures); GEO/L5 $7,100 to $15,500 ($800 at $200/kg launch); lunar surface $14,300 to $30,900 ($1,600), with observed
small-payload prices of $1.0 to 1.2 M/kg; low Mars orbit $6,400 to $13,900 ($720); Mars surface $17,800 to $38,700
($2,000); low Mercury orbit $22,400 to $48,500 ($2,500). On Earth's surface it is the terrestrial price (A).
"Delivered" is the lower-bound transport cost of F; mining and processing cost is **not** added, so a FAIL here is a fail
before any mining is paid for.

| Material, source to destination | Delivered cost, lower bound (F) | Value at destination | Verdict on the sourced numbers | Uncertainty |
|---|---|---|---|---|
| Lunar regolith or slag as shielding, Moon to L2 or L5 | $29 to $110/kg (optimistic hardware) | $7,100 to $15,500 (today); $800 (at $200/kg launch) | **PASS** by about 7 to 500 times with mass-produced hardware; **FAILS against the $200/kg future** if hardware costs $1 M/kg ($5,800 to $10,000) | 100-fold hardware cost range; SP-413 masses from 1975 |
| Lunar water or propellant to LEO, solar-electric tug | about $810 to $1,440/kg (optimistic) | $1,782 to $3,868 today; ULA bid $3,000 | **PASS today** (optimistic hardware only); **FAIL at $200 to $1,000/kg launch** | Metzger's chemical architecture claims a pass "no matter how low launch costs go" (Conflicts) |
| Lunar propellant used on the lunar surface | Jones et al. 2019: ISRU cheaper than delivery after 1.1 to 6.9 yr at 8.5 to 34 t/yr | $14,300 to $30,900 floor; $1.0 to 1.2 M/kg observed small-payload price | **PASS** at 17 t/yr or more with a 3 to 5-yr plant life; FAIL for 1-yr MREE plants | development cost excluded by the study |
| NEA water to cislunar space | studies' own models | Hein assume $20,000/kg; ULA bids $1,000 to $3,000 | **PASS only at the studies' assumed prices**; at ULA's bid no study was found that closes | the studies price water at Earth-launch cost of 2017 |
| NEA platinum to Earth's surface | Hein: needs 0.35 kg processed per second per kg of craft | $35,000 to $41,000/kg, falling 5.5-fold under a flood (Nachtrieb) | **FAIL on demonstrated throughput** (the study's own words: "very high"); a pass needs both that throughput and a price that the success itself erodes | SPECULATIVE |
| Belt material to low Mars orbit | $625 to $1,900/kg (optimistic hardware) | $6,400 to $13,900 today; $720 at $200/kg | **PASS today** with mass-produced tugs; **marginal to FAIL** at a $200/kg Earth launch; FAIL at $1 M/kg hardware | crude scaling; windows every 2.8 to 4.4 yr |
| Mercury material to Earth orbit, solar-electric spiral | $7,600 to $20,200/kg (optimistic hardware plus Earth-launched propellant) | $1,782 to $3,868 | **FAIL** by 2 to 11 times today, and further at any lower launch price | propellant source unresolved (xenon fails, water thruster unflown) |
| Mercury material to Earth orbit, photon sail | $1,100 to $21,400/kg | $1,782 to $3,868 | **FAIL** except one corner: sails lasting about 10 years at mass-production cost ($1,100 to $2,800) would pass today's price but **fail** at $200 to $1,000/kg | no sail lifetime near Mercury has been measured |
| Mercury material used in the Mercury region | launch to orbit 2.51 kWh/kg; no launcher design | $22,400 to $48,500 floor | **PASS on transport** by a wide margin; the open cost is the surface plant (heat, 88-day nights), for which no study exists | [ISM] 3 |
| Venus cloud-level carbon, nitrogen or argon to any orbit | $204,000 to $20.4 M/kg (expendable vehicles, hardware only) | at most $48,500 (Mercury orbit floor) for bulk | **FAIL everywhere** by 4 to 400 times on hardware alone | no reusable or non-rocket Venus launch has a study |
| Solar-wind matter, anywhere | payback about 1,350 yr at 0.1 AU | any | **FAIL** | the yield ceiling is physics (the wind's mass flux), not engineering |
| Lunar helium-3 to Earth | 50,000 to 250,000 t of regolith per kg at 4 to 20 ppb ([ML] A5) | $0.3 to 14.9 M/kg; market 5.4 kg/yr (about $80 M/yr) | **Market-limited:** even at $14.9 M/kg, 5.4 kg/yr is about $80 M/yr of revenue for a plant moving 270,000 to 1,350,000 t of regolith a year | price unconfirmed since 2011; no fusion demand exists |
| Space solar power to Earth | NASA LCOE $0.61 to $1.59/kWh | $0.02 to $0.05/kWh (2050 terrestrial projections) | **FAIL baseline** by 12 to 80 times; **PASS** only with every favorable assumption together ($0.03 to $0.08) | NASA's own framing |
| Computation in LEO | $14,700 to $135,800/kW/yr at $3,600/kg; $810 to $7,500 at $200/kg | $570 to $3,000/kW/yr terrestrial power spend | **FAIL today; overlaps** only at $200/kg launch for Starlink-class mass per kW | company preprint |

**The pattern:** the only routes that pass on the sourced numbers are **short and shallow** (Moon to cislunar space,
lunar surface use, belt to Mars) and carry the **lowest-value bulk** (shielding, water, propellant) to places where
the alternative is Earth launch. Mercury passes only for use near Mercury. Venus and the solar wind fail everywhere.
Every route that passes today becomes marginal or fails if Earth launch reaches $200/kg, **unless** the hardware is
mass-produced near $10,000/kg or less, which no space hardware has demonstrated except at satellite-constellation scale.

### H. Value of time and capital (checklist 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| US federal real discount rate for benefit-cost analysis | **7% real** (Circular A-94 of 1992, reinstated 8 Apr 2025; the 2023 revision was revoked) | OMB M-25-23 (8 Apr 2025); OMB Circular A-94 (1992) Sec. 8.b(1) | Primary | none | High |
| Market cost of capital by sector (US, nominal, January 2026) | Aerospace/Defense **7.60%** (equity 8.17%); Metals and Mining 8.20%; Power 5.01%; whole market 6.96% | Damodaran (NYU Stern), "Cost of Capital by Sector (US)" | Primary-grade (dataset widely used in finance) | OMB 7% real | High for established firms; **not** for a first-of-a-kind space venture |
| Rates used in space-resource studies | Hein et al. 10% ("generously low given how risky"); Metzger baseline 21.7% falling to 12% over 30 yr, 12% for a public-private partnership, 27.2% in one case; Charania and DePasquale's 21.7% "minimally viable" WACC; Sowers' venture IRR 8.84% | Hein 2018; Metzger 2023 Secs. 4.13, 6.4, 7 | Primary (preprints) | each other: a 2 to 4x spread | Medium |
| Pipeline inventory | Little's Law: cargo in flight = flow x trip time; at 1 Mt/yr from Mercury, 0.8 to 2.1 Mt on sails, 2.3 to 5.2 Mt on spiral tugs, about 9.8 Mt on flyby routes | [NW] F11 (Little 2011) | Primary (via sibling) | n/a (theorem) | High |

**DERIVED D12: what time in flight does to break-even.** Cargo is worth nothing until delivered; capital spent at
departure grows by (1 + r)^T before it earns. Multiplier on the value the cargo must reach to repay its departure cost:

| Route (trip time) | r = 5% | 7% | 12% | 21.7% |
|---|---|---|---|---|
| Moon to LEO (5 d) | 1.001 | 1.001 | 1.002 | 1.003 |
| Mercury direct (105 d) | 1.01 | 1.02 | 1.03 | 1.06 |
| Mercury by sail (369 d) | 1.05 | 1.07 | 1.12 | 1.22 |
| Belt to Mars (464 d) | 1.06 | 1.09 | 1.16 | 1.28 |
| Mercury spiral, loaded (2.3 to 5.2 yr) | 1.12 to 1.29 | 1.17 to 1.42 | 1.31 to 1.80 | 1.59 to 2.76 |
| Mercury flybys (9.8 yr) | 1.61 | 1.94 | 3.03 | **6.84** |

**Reading:** time costs nothing on lunar routes and little on one-year routes, but the propellant-saving flyby route from
Mercury (38 times less propellant, [NW] F6) **doubles to septuples** the value its cargo must reach, at the discount
rates actually used for space ventures. At 1 Mt/yr the flyby pipeline holds about 9.8 Mt of cargo; valued only at the
launch cost it displaces ($200 to $3,868/kg), that is $2 to $38 trillion of inventory in flight, carrying $0.2 to 4.5
trillion a year at 12% (D12). Time-in-flight and window bunching (one good Mercury-Earth window a year, belt-Mars every
2.8 to 4.4 yr, [NW] F1, [TR] F4) also force stock at both ends: the ISS rule is 45 days of food plus a lost-ship margin
([NW] F11).

### I. Non-monetary value: capability and survival, stated as mass (checklist 8)

| Capability enabled | Mass cost or mass saved (sourced) | Why it is not a price | Source | Confidence |
|---|---|---|---|---|
| Leaving the surface of Mars with a crew | 29.7 t of ascent propellant per ascent (6,978 kg CH4 + 22,728 kg O2) made locally from 15.7 t of water and 19.2 t of CO2, by 1.7 to 2.2 t of ISRU hardware (13.5 to 17.7 kg of propellant per kg of hardware); **about 10 kg of LEO mass saved per kg made**, "on the order of 300 mT" per mission | The alternative is not buying propellant at Mars; there is none to buy. It is launching about 300 t more from Earth on a 26-month window | Kleinhenz and Paz, NTRS 20170005179 | High as a NASA study |
| Crewed Mercury visit (no landing) | Refueling with Mercury polar-ice hydrogen cuts LEO mass from about 3,900 t to 1,520 t (Isp 800 s) | Same logic: local propellant turns a 3,900 t mission into a 1,520 t one | [TR] F1b (Palaszewski, NTRS 20170009136) | Medium |
| Surviving radiation in a habitat | 4.5 t/m^2 of passive shield for 0.5 rem/yr; 9.9 Mt for one torus of 10,000 people | Shielding has no resale value; its worth is the dose avoided, and Earth cannot launch Mt/yr | [LEO] D6; [PR] 6 | High as a design |
| Surviving a lost shipment | ISS: 45 days of food, 290 kg O2, 55 days of water kept in reserve; one failure cost 690 kg of supplies and a 3.48 t upmass shortfall | Local supply of water and oxygen shortens the reserve a site must hold | [NW] F11 (IG-16-025) | High |
| Life support from local material at a settlement | 2.66 t per person-year open loop (7.27 kg/day); water and oxygen are 4.9 of the 7.27 kg | A closed or locally fed loop is a capability (independence from windows), not a market | NASA 2023 logistics rates | High |
| Mars independent of Earth for chips, magnets and lithium | magnets alone 1.07 to 1.61 Mt of carbonaceous material per 1,000 robots, against 2 to 3 t imported | The cheapest import by mass is the costliest dependence to end | [SYN] 4 | Medium |

**Reading:** where the benefit is survival or capability, the honest unit is **mass not launched from Earth** (about 10
kg per kg of propellant made on Mars; a 2.6-fold cut in LEO mass, 3,900 t to 1,520 t, in the crewed Mercury case) and
**time not spent waiting for a window**. Neither has a market price in the sources, and none is claimed here.

## Conflicts

- **C1. Lunar propellant vs Earth launch at low launch prices.** Metzger 2023: lunar propellant outcompetes Earth-launched
  propellant "no matter how low launch costs go" (tent sublimation, φ about 440 to 530). This file's tug lower bound
  (F, G): lunar material to LEO by electric tug passes today but **fails** at $200 to $1,000/kg launch. Jones et al.
  (SciTech 2019): lunar propellant "97% more expensive". **Why they differ:** architecture, not physics. Metzger's
  case makes the transport itself run on lunar propellant (low capital gear ratio G) and assumes a very high production
  mass ratio; this file's tug case buys its propellant at the Earth-launch price and uses generic hardware cost.
  Metzger says that some prior TEAs chose high-G transport architectures and capital with low φ; which of them did so I
  did not check in the originals. He states that the remaining question is reliability in lunar dust. Not resolved.
- **C2. What water is worth in space.** Hein et al.: $20,000/kg; Calla et al.: $3,000 (LEO) to $35,000/kg (cislunar);
  ULA's bid: $3,000 (LEO), $1,000 (GEO), $500/kg (Moon). **Why:** the studies set the price equal to what it costs to
  launch water from Earth to that place (a ceiling); ULA set the price at which its own transport business closes (a
  bid). A seller cannot assume the ceiling while the only named buyer bids 7 to 40 times less.
- **C3. Platinum price and market size.** World Bank 2025 average $1,278/oz ($41,090/kg) vs USGS 2025 estimate $1,200/oz
  ($38,580/kg): estimation date (USGS is an early-year estimate). Nachtrieb and Smith's "initial" market of 400 t/yr at
  $60 M/t ($60,000/kg, $24 B/yr) is above both the 2025 Pt price and the 2025 Pt+Pd mine output (360 t, about $14 B):
  their table is a rounded sketch of the whole PGM basket, not a dataset. Hein's 2018 $70,000/kg is above any 2023 to
  2025 annual average found here. Platinum then reached $2,434/oz ($78,250/kg) in January 2026: price level depends on
  the month chosen.
- **C4. Helium-3 supply.** CRS (2011): about 8,000 L/yr of new He-3 (US tritium decay); USGS (2026): world production
  40,000 L in 2024 and 2025 (Canada, Russia, US). Different scope (US vs world) and epoch.
- **C5. Xenon supply.** 53 t/yr (NASA/Linde, 2015), about 65 t/yr (Lindner 2023, [TR]), 70.8 t/yr (USGS 2025, D4): growth
  over a decade, plus the USGS liters-to-metric-tons conversion done here at 0 C and 1 atm (USGS does not state the
  reference conditions for rare-gas liters; at 15 C the mass would be about 5% lower).
- **C6. NASA space-solar LCOE.** Report: $0.61/kWh for RD1. Check here: $276 B / (2 GW x 30 yr x 8,766 h) = $0.525/kWh
  undiscounted (D13). The report's methodology (discounting, availability, delivered vs nameplate power) was not read in
  full; the 16% difference is not resolved.
- **C7. "Today's" launch price.** $1,500/kg (Falcon Heavy, 2021 $, list price at full expendable payload), $1,800/kg
  (Google, Falcon Heavy), $2,000/kg (Metzger, Falcon 9, 2023), $3,600/kg (Google's current reference), $3,868/kg
  (2025 average of all launchers, Terzi and Nicoli). **Why:** vehicle, base year, and list price at maximum payload
  versus fleet average. This file carries $1,782 to $3,868/kg (2025 $) as the range.
- **C8. CRS cost per kilogram is per kilogram of capability, not of cargo delivered** (the OIG table says "Upmass
  Capability"); the cost per kilogram actually delivered is higher. The OIG also notes Dragon 1 never exceeded 2,100 kg
  of pressurized upmass against a 2,500 kg assumption.

## Derived figures

Script: `calc_value.py`; output: `calc_value_output.txt` (scratch subfolder `value_and_markets_of_inner_system_materials/`),
run with `python3 -I`. Key lines are reproduced; sources of every input are in Findings.

- **D1. Conversions.** 1 troy oz = 31.10348 g; 1 lb = 0.4535924 kg; short ton = 907.1847 kg (NIST SP 811 B.9). US
  gallon = 1.410089 x 10^-9 m^3/J x 2.684520 x 10^6 J = 3.7854 L (from two NIST B.9 entries).
- **D2. Prices per kg.** Price per toz / 0.03110348; price per lb / 0.4535924. Helium: USGS 27.737 m^3 = 0.0047 t ->
  0.1694 kg/m^3, so $12/m^3 = $70.8/kg. Helium-3: 3.0160293 g/mol / 22.41397 L/mol = 0.13456 g/L at STP, 7,432 L/kg;
  $2,000/L = $14.86 M/kg; $40 to $85/L = $0.30 to $0.63 M/kg. Liquid hydrogen: $144.4 M / (36.5 M x 0.4536 kg) = $8.72/kg.
- **D3. LOX and LN2 bound.** Total maximum value $153.0 M. LOX = 243,000 tons (short: 220,400 t; metric 243,000 t) +
  2.1 M gal x 3.7854 L x 1.1416 kg/L (9,075 t); LN2 = 656.8 tons + 30.4 M gal x 3.7854 x 0.80617 (92,770 t) + 740 m^3 x
  806.17 (597 t). Result $0.442 to $0.473/kg.
- **D4. Market sizes.** Pt 170,000 kg x $41,089 = $6.99 B; Pd 190,000 x $35,366 = $6.72 B; He 190 x 10^6 m^3 x
  0.1694 = 32,195 t, x $12/m^3 = $2.28 B; He-3 40,000 L / 7,432 = 5.38 kg, x $2,000/L = $80 M; Xe 12 x 10^6 L x 5.898 g/L
  = 70.8 t.
- **D5. Inflation (BLS CPI-U annual averages).** 1977 60.6; 2018 251.107; 2021 270.970; 2022 292.655; 2025 321.943.
  Factors to 2025: 5.313, 1.282, 1.188, 1.100. SP-428 $24/kg -> $128/kg; FH $1,500 -> $1,782/kg.
- **D6. Floor price of Earth-launched mass.** Floor = LEO price x LEO mass per unit delivered. Multipliers: 4 (L5,
  SP-413), 8 (L2 or lunar surface, SP-413), 10 (Mars surface, Kleinhenz and Paz), and for propellant-only hydrolox floors
  exp(dv / (452.3 s x 9.80665)): low Mars orbit dv 5.66 km/s -> 3.58; low Mercury orbit dv 11.22 km/s -> 12.55 ([TR] D1).
  At $1,782 / $3,868 / $1,000 / $200 per kg: GEO-L5 $7,129 / 15,472 / 4,000 / 800; lunar surface $14,257 / 30,944 /
  8,000 / 1,600; Mars surface $17,822 / 38,680 / 10,000 / 2,000; low Mars orbit $6,385 / 13,857 / 3,582 / 716; low
  Mercury orbit $22,363 / 48,536 / 12,548 / 2,510.
- **D7. Tug capital per kg.** Life = 50,000 h / (0.9 x 8,766 h) = 6.34 yr. Capital recovery factor CRF = r / (1 - (1 +
  r)^-n). Capital per kg = 68 kg/kW x specific cost x CRF / (productivity t/kW/yr x 1,000). Lunar leg (0.279): $489 /
  571 / 743 at r = 7 / 12 / 21.7% and $10k/kg; x100 at $1 M/kg. Mercury (0.041 capped, 0.019 flat): $3,329 to $10,908
  at $10k/kg. Propellant 0.18 and 2.4 kg/kg x $1,782 to $3,868 = $321 to $696 and $4,277 to $9,283.
- **D8. Sails.** Capital per kg = sail mass per (kg/yr) x specific cost x CRF(7%, life). 0.78 kg: $8,346 (1 yr), $1,902
  (5 yr), $1,111 (10 yr) at $10k/kg; 2.0 kg: $21,400, $4,878, $2,848.
- **D9. Lunar mass driver base.** Capex = 17,050 t x (specific cost + emplacement); yearly imports 402 t x emplacement;
  per kg = (capex x CRF(r, 10 yr) + imports) / 10^9 kg. Optimistic ($10k/kg, 8 x $1,782): $414 B capex, $5.73 B/yr
  imports -> $64.61 (7%) to $110.12 (21.7%) per kg; at 8 x $200: $28.80 to $50.57; conservative ($1 M/kg, CLPS $1.2 M/kg):
  $5,823 to $9,951. Energy: 2.88 MJ/kg = 0.80 kWh/kg.
- **D10. Venus ascent.** 1,840 - 1,286 - 340 - 10 = 204 kg of hardware per 10 kg canister: 20.4 kg/kg; propellant
  162.6 kg/kg.
- **D11. Solar wind.** Flux at r = 1.3 x 10^9 kg/s / (4 pi r^2) x 3.156 x 10^7 s/yr: 0.146 mg/m^2/yr at 1 AU; 1.62 at
  0.3 AU; 14.6 at 0.1 AU. Check: Genesis 0.2 mg/yr on 1.67 m^2 = 0.120 mg/m^2/yr (hydrogen only). Value at $3,000/kg:
  $4.4 x 10^-4, 4.9 x 10^-3, 4.4 x 10^-2 per m^2 per yr. Collector at 5.9 g/m^2 x $10,000/kg = $59/m^2; payback 1,348 yr
  at 0.1 AU.
- **D12. Time.** Multiplier (1 + r)^T (table in H). Inventory = flow x time (Little's Law): 9.8 Mt x $200 to $3,868/kg =
  $1.96 to $37.9 T; at 12%, $0.24 to $4.55 T/yr.
- **D13. Space solar earnings per kg.** 2 GW x 30 yr x 8,766 h = 526 billion kWh; x $0.02 / 0.05 / 0.0862 = $10.5 /
  26.3 / 45.3 B; per kg of RD1's 5.9 Mkg: $1,783 / 4,457 / 7,684; RD2 (10 Mkg): $1,052 / 2,630 / 4,534. Undiscounted; at
  7% the 30 years are worth 12.41 years of revenue today, so discounted earnings are 41% of these.
- **D14. Consumables.** 2.39 + 0.89 + 2.79 + 0.50 + 0.40 + 0.30 = 7.27 kg per person-day = 2.66 t per person-year; 4 people
  11 t/yr; 110 people 292 t/yr; 10,000 people 26,554 t/yr (open loop).
- **D15. Platinum flood.** Nachtrieb and Smith's sketch: price 60 -> 11 M$/t (5.5x), revenue 24,000 -> 4,444 M$/yr at
  400 t/yr.
- **D16. Belt to Mars.** Productivity 0.279 x 363.1 / 464 = 0.218 t/kW/yr one way (0.109 with an equal empty return);
  capital $625 / 729 / 949 per kg (one way) and $1,250 / 1,459 / 1,899 (with return) at r = 7 / 12 / 21.7%, $10k/kg.

## Constraints for any inhabitant

- **Bulk comes from the nearest shallow well, or it does not come.** Shielding, water and structural mass pass the
  break-even only on short routes (Moon to cislunar space, belt to Mars) or for use where they are mined (G). A site far
  from such a source pays Earth-launch floor prices for every kilogram: $14,000 to $31,000/kg on the Moon, $18,000 to
  $39,000 on Mars, $22,000 to $49,000 near Mercury at today's launch prices (B, D6), and real small-payload delivery has
  cost $1.0 to 1.2 million/kg to the lunar surface (B).
- **Water, oxygen and propellant are the first local products and the first things anyone pays for.** Every published
  analysis that closes, closes on volatiles (C). A person needs 7.27 kg/day of food, oxygen and water open loop, 4.9 kg of
  it water and oxygen (D, D14): life support is the first market and the first dependency.
- **The most-needed material is the least valuable.** Above about 10^5 t/yr, demand is shielding and structure (D),
  whose only value is the launch it avoids (I). Its price ceiling falls whenever Earth launch gets cheaper (G).
- **Exports to Earth's surface are limited to tiny, price-fragile markets.** Platinum-group metals (about $14 B/yr) and
  helium-3 (about 5 kg/yr) are the only materials whose price could in principle pay for the trip down; a supplier large
  enough to profit is large enough to collapse the price (E, Nachtrieb and Smith).
- **Distance costs money even when it costs no propellant.** Ten years in flight on the Mercury flyby route doubles
  to septuples the value the cargo must reach (H); one-year routes add 5 to 28%.
- **Mercury's material is for use near Mercury; Venus's stays at Venus; the solar wind yields nothing usable.** On the
  sourced numbers, Mercury-to-Earth-orbit cargo fails by 2 to 11 times, Venus export by 4 to 400 times on hardware
  alone, and a solar-wind collector would take about 1,350 years to repay itself at 0.1 AU (F, G).
- **Cheap Earth launch competes with space mining.** Every route that passes today becomes marginal or fails if Earth
  launch falls to $200/kg (G), unless space hardware is mass-produced near $10,000/kg.
- **Reserves are a cost of distance.** Window gaps (Mercury-Earth about once a year for the cheap windows, belt-Mars
  every 2.8 to 4.4 years) and lost shipments must be covered by stock at the receiving end (H, I).
- **Capability, not price, is the reason to make propellant at Mars or Mercury.** About 10 kg of Earth launch avoided per
  kg of Mars-made propellant; a 2.6-fold cut in a crewed Mercury mission's launch mass with Mercury hydrogen (I).

## Candidate handwaves

Flagged for the developer; none is accepted here.

- **V-1. Space-sourced bulk material (metal, oxygen, water, silicon) sold at a profit on Earth's surface.** Terrestrial
  prices are about 180 to 39,000 times below today's launch price, and Hein et al.'s rough estimate puts the trip down at
  twice the launch cost (E).
- **V-2. Mercury as a supplier to Earth orbit at today's or lower launch prices.** Lower bound 2 to 11 times the Earth-
  launch alternative before any mining cost; only 10-year sails at mass-production cost reach today's price, and none
  reaches $200 to $1,000/kg (G).
- **V-3. Platinum-group metals or helium-3 as a large, stable source of revenue.** Markets of about $14 B and $0.08 B a
  year, with price collapse modeled at 5.5-fold for PGMs; Hein et al. need throughput they themselves call very high (C, E).
- **V-4. Venus as an exporter of anything to orbit.** Expendable ascent costs $204,000 to $20.4 M per kilogram in
  hardware alone; no reusable or non-rocket Venus launch has a study (F, G; [ISM] M-2).
- **V-5. Solar-wind collection as a material source.** Payback about 1,350 years at 0.1 AU at the most generous price,
  with zero transport cost assumed (D11; [SYN] S-1).
- **V-6. Space hardware at $10,000/kg or less for miners, tugs, sails and catchers.** Demonstrated first units: $113.6 M
  for a sub-500 kg craft (Calla), $453.6 M for the 60 kW PPE; $10,000/kg is a mass-production assumption (B). Every
  "PASS" in G depends on it.
- **V-7. Launch at $200/kg or less treated as a given.** Google's own projection needs about 370,000 t more cumulative
  launched mass (about 180 Starship launches a year to 2035) and the authors say they are "not trying to predict the
  actual future price" (C). Note that it cuts both ways: it makes space activity cheaper and space-sourced bulk less valuable.
- **V-8. A discount rate at or below 7% for a first-of-a-kind space-resource venture.** The rates actually used in the
  field are 10 to 27.2% (H); established aerospace firms' cost of capital is 7.6% (Damodaran).
- **V-9. Space solar power at a terrestrial-competitive price without every favorable assumption at once** (launch
  $500/kg, electric orbit raising, 15-yr hardware, $100 M servicers, 85% learning curves together) (C).

## Open threads

- **Xenon, krypton and argon prices.** USGS publishes none; NASA's 2015 paper shows the history only in a figure.
  Next: the original Betzendahl or Linde market reports, or Lindner 2023's price slide ([TR] source), read directly.
- **Current helium-3 price.** Only the 2011 CRS figure is primary. Next: the DOE Isotope Program (isotopes.gov) price list
  or a NIDC auction notice.
- **Current vendor launch prices.** SpaceX's capabilities and rideshare pages are script-rendered and returned no text
  (rows 15, 17). Next: an archived copy (Internet Archive) or a GAO or NASA OIG report quoting the contract price.
- **Space solar-array cost per watt.** No primary source found (rows 50, 51). Next: AFRL ROSA program reports, or NASA
  OTPS 2024 Appendix B (its manufacturing cost inputs), which I did not read.
- **Mass-produced spacecraft cost per kg** (Starlink, OneWeb): no primary source found; Hein's $10,000/kg rests on it.
- **Studies cited only through Metzger:** Kornuta et al. 2019 (paywalled, row 61), Jones et al. SciTech 2019, Charania and
  DePasquale 2007, Bennett et al., Shisko's review, Ross et al. 2009 and Andrews and Andrews (elasticity). Not opened.
- **Earth-return mass fraction for valuable cargo** (capsule mass per kg returned): only secondary figures found (row 60).
- **A historical analog of a supply flood** (for example aluminum's price after electrolytic production, USGS Data
  Series 140 historical statistics): not searched; it would test Nachtrieb and Smith's 5.5-fold collapse against history.
- **World electricity 2025** read only from a search summary (row 58); IEA *Electricity 2026* not opened.
- **No study prices any material from Mercury, Venus or the solar wind**, and none sizes a receiving and processing node
  ([NW] F5). Every Mercury, Venus and solar-wind figure in F and G is this file's derivation.
- **NASA OTPS LCOE method** (C6): the discounting and availability assumptions behind $0.61/kWh not read in full.
- **Mars-surface delivered price**: no observed price exists (no commercial Mars delivery); the floor in D6 is
  propellant-only.

## Rejected sources

- **newspaceeconomy.ca** ("SpaceX rideshare pricing as of February 2026"): trade press restating a vendor page that could
  not be opened; not used.
- **sets.space** (xenon, krypton, argon $/kg) and an unnamed second set in the same search summary: a vendor blog and an
  unattributed summary; no primary behind either.
- **Helium-3 market-report pages** (visualcapitalist, dataintelo, 24chemicalresearch, edelgasgroup, yigasgroup,
  akapenergy): mutually inconsistent ($1,900 to $15,000 per liter), commercial, no primary citation visible.
- **Wikipedia via search summaries** (PPE mass 8 to 9 t; OSIRIS-REx capsule 46 kg): secondary; not used.
- **nextbigfuture, spacenexus, greenlaunch, orbitalradar** (Falcon 9 cost and price): blogs; not used.
- **spaceodysseyhub** ("failure-adjusted $3.84 M/kg" for CLPS): secondary; the OIG figures were used instead.
- **Search-summary claim "ULA would pay $3,000 to $7,000/kg in LEO"**: not found in any opened ULA document; the opened
  ULA paper gives $3,000/kg (Kutter 2016).
- **BVAD values in a search summary** (4.350 kg water, 0.84 kg O2, 0.62 kg food per day): from secondary pages; the NASA
  2023 logistics-rates document was used instead.
- **gasworld** (Praxair LN2/LOX contract, "52,400 tons"): undated in the summary and HTTP 403 earlier (row 6); not used.
- **Four arXiv hits in row 9** (rotating-asteroid stability, environmental benefits, meteoroid streams, space-weather
  architecture): not about price or markets.
