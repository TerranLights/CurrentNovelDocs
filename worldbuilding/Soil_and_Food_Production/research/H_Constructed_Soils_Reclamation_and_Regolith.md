## PROGRESS (tick after each question is fully written to this file)
- [x] Q1
- [x] Q2
- [x] Q3
- [x] Q4
- [x] Q5
- [x] Q6
- [x] Q7
- [x] FINAL

# H — Constructed Soils, Reclamation and Regolith Agriculture (real-world research)

Research slice H for the Soil and Food Production spec sheet. Real-world sources only; nothing here describes the fictional setting.
Started 2026-10-25. Status labels: **SOURCED** (number read in the cited source), **COMPUTED** (arithmetic shown), **UNVERIFIED** (seen only in a secondary source or snippet, not confirmed).

---

## 1. Findings summary and recipe table

**Summary (real-world evidence only; details and sources in Section 2).**
1. **Nearly every documented rebuild of sterile ground paired three things:** a large one-off organic or nutrient dose (tens to hundreds of t/ha), something to fix or supply nitrogen, and water management (irrigation plus drainage in deserts, runoff capture in the Sahel). Water harvesting or crust-breaking without nutrients gave almost nothing (< 100 kg/ha sorghum; Q1e).
2. **Fast start, slow finish.** Soil carbon on sterile substrates climbs steeply for ~5–8 years and then flattens (Egypt 2.7–3.8 → ~0.5 t C/ha/yr; Iceland plateau after 8 years). Reaching the level of natural soil takes decades to centuries (Tengger: 23–245 years projected). Without continued inputs, added organic matter can return near baseline within ~10 years (Q1, Q7c).
3. **Salt and sodium are handled with water, drains and gypsum, all quantifiable:** one depth of water per depth of soil removes ~70–90% of soluble salts; ~1.7 t gypsum/ha (15 cm) per cmolc/kg of sodium replaced; drains 1–1.8 m deep at 30–150 m spacing (Q3).
4. **Regolith simulants become arable only when heavily amended:** compost or vermicompost at 30–75% by volume, plus nitrogen, microbes and (for Mars) perchlorate removal. Pure simulant supports plants briefly or poorly; the most accurate Mars simulant (MGS-1) failed, and real Apollo soil was more stressful than its simulant (Q5).
5. **The main failure modes are erosion of bare new surfaces (~10^2 t/ha/yr until ~40% plant cover), compaction from grading, organic-matter burn-off, salt build-up, and contaminants carried in by waste (metals, PFAS, microplastics, pathogens)** (Q7).

**Three most important figures (all SOURCED):**
- **SEKEM desert sand, Egypt:** compost ≈ 48–69 m3/ha per season twice a year took soil carbon (0–50 cm) from 3.9 to 28.8–31.8 t C/ha in 30 years, 2.7–3.8 t C/ha/yr in years 1–5, then ~0.5 t/ha/yr (Luske and van der Kamp 2009).
- **Sahel half-moons:** 14.6 t/ha manure gave 1,614 kg/ha sorghum on bare crusted ground that yielded nothing untreated; the half-moon alone gave 41 kg/ha (Zougmoré et al., INERA trial 1998).
- **Bare reclaimed slope erosion:** 131–292 t/ha/yr predicted on a bare 10% slope, cut from 185 to 27 t/ha/yr by 40% grass cover (So et al. 2018).

**Recipe table.** Status = status of the core figures in that row; see Section 2 for each number.

| # | Substrate | Amendment and rate | Time to first harvest / to stable fertility | Result | Source | Status |
|---|---|---|---|---|---|---|
| 1 | Acidic pyritic copper tailings, pH 2.5–4, arid Arizona | Biosolids 157–224 Mg/ha dry + ground green waste (C:N > 30) + lime 36.9 Mg/ha, plowed 25–30 cm; sprinkler irrigation | Grass/forage biomass in first 4–5 months; stability not studied | > 2,802 kg/ha summer biomass at 224 Mg/ha; control zero; 303 Mg/ha worse (mixing) | Rogers, Bengson & Thompson 1998 (ASMR) | SOURCED |
| 2 | Copper tailings, British Columbia | Biosolids 50–250 Mg/ha dry | 3-year study | Raised C, N, P; Zn above guideline at top rates; Mo risk | Gardner et al. 2012 (CJSS) | SOURCED (abstract) |
| 3 | Acid anthracite refuse bank, 75% slope, Pennsylvania | Excelsior mat + lime 2.8 t/ha + 2:1 sludge:fly ash, sludge 65 Mg/ha dry (≥ 1,000 kg N/ha), ~5 cm thick; hydroseed | Cover year 1 | 57% → 83% cover, 5.0 → 8.1 t/ha DM over 3 yr (control 7–15%) | Sopper 1993 (ASRS) | SOURCED |
| 4 | Coal fly ash lagoon | 50–100 mm cap of sandy topsoil or compost + mulch/fabric; halophytes | Not stated | Good germination and growth | Jusaitis & Pillman 1997 | SOURCED (abstract) |
| 5 | Coal spoil, Ohio | 25–30 cm stored topsoil re-spread; pasture or forest | Low biomass first 5–15 yr | SOC 21.8–26.1 → 58.9–62.7 Mg C/ha in 25 yr (0–30 cm) | Akala & Lal 2001 | SOURCED (stated rates inconsistent) |
| 6 | Eroded volcanic sand/gravel, Iceland, OM < 1% | Nootka lupine 5 kg seed/ha, rhizobium-inoculated, strip-sown, no fertilizer; ISK 30,000/ha | One-off; continued C gain where grass plots stalled | Cover and N gain; invasive — agency stopped in 2018 | WOCAT sheet 2020; Tanner et al. 2015 | SOURCED / UNVERIFIED (C rates) |
| 7 | Eroded Icelandic desert | ~300 kg/ha chemical fertilizer (aerial) or ~1.6 t/ha meat-and-bone meal + ~45 kg/ha grass seed | C gain 0.4–0.63 t/ha/yr first 7 yr, then plateau | ~55 t C/ha (0–30 cm) after 50 yr | Arnalds et al. 2013; Andryei 2015; Hunziker et al. 2019 | SOURCED / COMPUTED (rates per ha) |
| 8 | Hyper-arid desert sand, Egypt (SEKEM) | Compost 47.6–69 m3/ha per season, twice yearly (≈ 59 t/ha/yr fresh), flood/pivot then drip irrigation | Crops in year 1; C still rising at 30 yr | 3.9 → 28.8–31.8 t C/ha (0–50 cm); EC ~4,000 → 240–750 ppm; pH up to 8.5 | Luske & van der Kamp 2009 | SOURCED / COMPUTED (t/ha) |
| 9 | Sealed crusted bare glacis, Burkina Faso (630 mm rain) | Half-moons 417/ha + 14.6 t/ha manure or compost (± rock phosphate 20 kg P/ha) | First season | 875–1,614 kg/ha sorghum over 2 yr vs 0 control and 41 kg/ha unamended half-moon; SOM still < 3% | Zougmoré et al. (INERA) | SOURCED |
| 10 | Same, zai pits | 20,000–31,750 pits/ha; 0.3 kg manure/pit (~9.5 t/ha); 4–18 t/ha manure needed; 300–700 h/ha labor | First season | 300–1,600 kg/ha cereal | ECHO TN #78; Zougmoré et al. | SOURCED (secondary) |
| 11 | Shifting dunes, Tengger (180 mm rain) | Straw checkerboards + planted xerophytic shrubs, unirrigated | No SOC change first 14 yr; 60% of reference in 50 yr | SOC 0.33 → 5.08 g/kg in 57 yr; full recovery projected 23–245 yr | Li et al. 2007; Li, Liu & Li 2015 | SOURCED (abstracts) |
| 12 | Loess gullies, China | Check dams trap eroded topsoil; farm once filled | Time to fill NOT FOUND | 7,800 kg/ha vs 2,400 on slope | DESIRE project, Yanhe basin | SOURCED |
| 13 | Negev loess valleys (~100 mm rain) | Runoff from catchment 9–33× the field area (avg 18×); 35–40 m3/ha manure ± NPK | Crop only in 3 of 6 years | 600–4,380 kg/ha wheat in good years; 995 kg/ha 6-yr mean | Bruins 1986 (Evenari data) | SOURCED |
| 14 | Excavated urban subsoil (Technosol) | 70% subsoil + 30% compost (v/v), 30 cm (20% compost temperate; 40–50% dry) | Aggregation within 5 months; C stable in ~3 yr | Parks, urban farming use | Deeb et al. 2020 (SOIL) | SOURCED (review) |
| 15 | Crushed concrete Technosol | 70% crushed concrete + 10% green-waste compost (+ ~20% subsoil) | Not stated | Best tree survival and fauna colonization | Pruvost et al. 2018 via Deeb 2020 | SOURCED / UNVERIFIED (20%) |
| 16 | Mojave Mars Simulant MMS-1 | 30:70 or 70:30 simulant:green compost (v/v) | 19-day lettuce | 61–68 g/plant at 30:70; pure simulant ~20% less | Duri et al. 2020 (Plants) | SOURCED |
| 17 | JSC-1A Mars and lunar simulants | Fresh grass clippings + nutrient solution | One crop cycle | 9 of 10 crops harvested; Moon simulant lower biomass | Wamelink et al. 2019 | SOURCED (abstract; ratio NOT FOUND) |
| 18 | Lunar simulant | 25–75% simulant + vermicompost; AMF-coated seed | Germination 16 d; seed set | First chickpea yield in simulant | Atkin et al. 2024 preprint | SOURCED (secondary) |
| 19 | Glacial rock flour on Greenland grassland | 20 t/ha + 25% NPK (40 t/ha + NPK reduced yield) | One season | Yield up only with NPK; no soil pH change | Sukstorf et al. 2020 | SOURCED (abstract) |
| 20 | Basalt dust on U.S. cropland | 50 t/ha/yr × 4 yr | Annual crops | +12–16% yield; 10.5 t CO2/ha removed in 4 yr | Beerling et al. 2024 | SOURCED |
| 21 | Sodic soil | Gypsum 5–40 t/ha (≈ 1.7 t/ha per cmolc/kg Na, 15 cm) + good water + drainage | Not stated | ESP lowered | FAO Paper 29; UA FSA2199 | SOURCED / COMPUTED |
| 22 | Waterlogged saline soil, India | PVC drains 1.2–1.8 m deep, 30–150 m apart; ₹65,000–1,25,000/ha | Payback 3–5 yr | Wheat 3.6 vs 2.4 t/ha; yields +50–100% | ICAR-CSSRI 2016 | SOURCED |

---

## 2. Findings by question

### Q1. Reclamation of sterile or near-sterile substrates

#### Q1a. Iceland: eroded volcanic desert (Vitric Andosols / sandy gravel), Soil Conservation Service (Landgræðslan, now Land and Forest Iceland)

**Starting material.** Severely eroded volcanic soils; desert Vitrisols (Vitric Andosols and Leptosols) hold "less than 45 t C ha-1"; for comparison the intact Brown Andosols of vegetated land average 227 t C ha-1 (Óskarsson et al. 2004, as cited in Hunziker, Arnalds and Kuhn 2018/2019, SOIL; https://soil.copernicus.org/preprints/soil-2018-26/soil-2018-26.pdf, read 2026-10-25). **SOURCED** (secondary citation of Óskarsson 2004). Untreated eroded soil in the restoration plots held 0.1–0.3 kg C m-2 (= 1–3 t C ha-1) and surface carbon content < 0.3% (Arnalds, Orradottir and Aradottir 2013, *Geoderma* 193–194: 172–179, doi:10.1016/j.geoderma.2012.10.018; abstract read at https://iris.landsbokasafn.is/en/publications/carbon-accumulation-in-icelandic-desert-andosols-during-early-sta/, 2026-10-25). **SOURCED (abstract only).**

**Recipe 1 — Nootka lupine (Lupinus nootkatensis) seeding.** WOCAT SLM technology sheet (compiler Jan Reichert, resource person Sveinn Runólfsson, former head of the Soil Conservation Service; documented 2020-04-01, updated 2020-07-05; PDF https://www.wocat.net/documents/1047/Seeding_lupine_for_land_reclamation_against_wind_erosion_Iceland.pdf, read in full 2026-10-25):
- Seed rate: "Normally 5 kg of lupine seeds per ha." Seeded by machine, in strips, spring or very late autumn. **SOURCED.**
- Seed must be inoculated with rhizobium, produced in winter in the SCS lab at Gunnarsholt: "without this inoculation the plant wouldn't survive in the bare soil." **SOURCED.**
- "The lupine needs no fertilizer after planting." One-off operation; no maintenance listed. **SOURCED.**
- Cost: 30,000 ISK per ha establishment (= USD 217.39 at 1 USD = 138.0 ISK), Thorlákshöfn project. Year of the cost figure is not stated on the sheet (sheet dated 2020). **SOURCED.**
- Sites: topsoil organic matter "low (<1%)", very shallow (0–20 cm), coarse sandy; rainfall 501–1,000 mm. **SOURCED.**
- Failure: very invasive, displaces native vegetation, unpalatable to sheep once mature, stoppable at scale only by herbicide; "the Soil Conservation Service stopped using the lupine in 2018." **SOURCED.**
- Soil gain under lupine: a 15-site chronosequence (lupine present 10–40 years) in southern Iceland found soil C rising "about 0.1% (1300 kg/ha) and N 0.01% (120 kg/ha) per year", with about a tenfold difference between sites, and indications of net carbon LOSS where lupine invaded humus-rich dwarf-shrub heath in the north. **UNVERIFIED** — seen only in a search-engine summary of *Fjölrit RALA* (15 Jan 2001, p. 7, https://timarit.is/page/7316611); the page returned HTTP 403 when opened.
- Long-run: in experimental plots on eroded land near Gunnarsholt (established 1999), soil C in the top 10 cm rose substantially for the first eight years in all fertilizer-plus-grass treatments, then accumulation "declined to negligible" over the next five; "only plots seeded with lupine demonstrated continued long-term soil carbon accumulation" (Tanner, Nivison, Arnalds and Svavarsdóttir 2015, *Applied and Environmental Soil Science*, doi:10.1155/2015/205846). **UNVERIFIED** — abstract seen only through search summaries; DOAJ page 403, Wiley/Hindawi PDF returned an HTML wall.

**Recipe 2 — fertilizer plus grass seed (the classic SCS treatment).**
- Arnalds et al. 2013 (*Geoderma*): 24 one-hectare plots, nine treatments plus untreated controls. Surface (0–5 cm) carbon rose from < 0.3% to > 0.7% in some treated plots; accumulation 0.04–0.063 kg C m-2 yr-1 (= 0.4–0.63 t C ha-1 yr-1) over the first seven years, highest with grass seeding plus fertilizer; none in untreated controls. Authors project > 0.05 kg C m-2 yr-1 "can potentially be maintained over >100 yr" because Andosols are steadily buried by windblown material. **SOURCED (abstract).** Fertilizer rates of the nine treatments: **NOT FOUND** (full text paywalled).
- Gunnarsholt treatment records (Andryei 2015, UNU Land Restoration Training Programme final project, supervisors at Univ. of Iceland and the Soil Conservation Service, Table 1; https://www.grocentre.is/static/gro/publication/422/document/andryei2015.pdf, read 2026-10-25): 1991 aerial chemical fertilizer, 12,000 kg on 39.9 ha; 2013 tractor seeding with meat-and-bone meal 86,800 kg on 54 ha, plus seed 1,500 kg *Festuca richardsonii*, 800 kg *Lolium multiflorum*, 140 kg *Deschampsia beringensis*; 1962–1975 aerial chemical fertilizer 2,500 kg on 8.3 ha plus *Festuca* seed. **SOURCED.**
  - COMPUTED: 1991 aerial: 12,000 / 39.9 = **≈ 301 kg fertilizer/ha**. 2013: 86,800 / 54 = **≈ 1,607 kg meat meal/ha**; seed (1,500 + 800 + 140) / 54 = **≈ 45 kg seed/ha**. 1962–75: 2,500 / 8.3 = **≈ 301 kg/ha**. Assumes the whole recorded quantity went on the recorded area in one pass.
  - Result: two years on, the sown *Lolium* was not found in the 2013 plots and their total biomass did not differ from the untreated control; the fertilizer-only (1991) and old seed-plus-fertilizer (1962–75) sites had higher biomass, cover, bulk density and soil organic matter than degraded land. **SOURCED.** (Single-season student project, 2 plots per treatment; weak evidence.)
- Tunguheiði project (1997–2024): "an average of four treatments per hectare, each applying 200 kilograms of fertilizer" (spelling Americanized). **UNVERIFIED** — search summary of https://island.is/en/news/tunguheidi-saga-landgraedslu-1997-2024 only; page returned HTTP 503. COMPUTED if true: 4 × 200 = 800 kg fertilizer/ha in total over the project.
- 50-year outcome: grassland revegetated "using fertilizer and grass seeds 50 years ago" near Gunnarsholt had a median SOC stock (0–30 cm) 9 t C ha-1 above 50-year-old birch afforestation (Birch50 = 46 t C ha-1, so Grass50 ≈ 55 t C ha-1, COMPUTED 46 + 9); Snorrason et al. 2002 reported 54 t C ha-1 (0–30 cm) for comparable grassland; Aradóttir et al. 2000 found 28 t C ha-1 (0–20 cm) on a 46-year-old grassland (all from Hunziker et al. preprint, read 2026-10-25). **SOURCED.** Iceland's National Inventory Report uses 0.51 t C ha-1 yr-1 for conversion of severely degraded land to grassland or forest (Hellsing et al. 2016, as cited there). **SOURCED (secondary).**

**Recipe 3 — birch afforestation on degraded land.** SOC (0–30 cm) median 31 / 33 / 36 / 46 t C ha-1 at 15 / 20 / 25 / 50 years; 0.42 t C ha-1 yr-1 average over 35 years; first 25 years possibly a net carbon SOURCE (stocks below the barren reference); after 50 years still ~15 t ha-1 below natural birch woodland; potential further 20 t C ha-1. Most new carbon is labile particulate organic matter that "may be partly released" (Hunziker, Arnalds and Kuhn 2019, *SOIL* 5: 223, https://soil.copernicus.org/articles/5/223/2019/). **SOURCED.**

#### Q1b. Copper mine tailings, British Columbia, with biosolids

- Gardner, Naeth, Broersma, Chanasyk and Jobson 2012, *Canadian Journal of Soil Science* 92(1), doi:10.1139/CJSS2011-005 (abstract page read 2026-10-25, https://bioone.org/journals/Canadian-Journal-of-Soil-Science/volume-92/issue-1/CJSS2011-005/): 3-year field study, silt-loam and sandy copper tailings, southern-interior BC. Biosolids at **50, 100, 150, 200 and 250 Mg ha-1 dry weight**. Biosolids raised total C, Fe, Mg, Ni, N, P, S, Zn and available NH4, Fe, Mn, NO3, P, Zn. Highest rates pushed total Zn to 214 mg kg-1 (above guidelines). Total Cu 647 mg kg-1 (silt loam) and 1,291 mg kg-1 (sandy). Unamended silt-loam held 35 mg kg-1 Mo and vegetation 112 mg kg-1 Mo (a livestock molybdenosis concern). Conclusion: "Managed biosolids use in reclamation can ameliorate sites and facilitate vegetation establishment, with low environmental risk." **SOURCED (abstract).** Biomass by rate: **NOT FOUND** in the abstract (full text not opened).

#### Q1c. Acidic copper tailings, Arizona (arid), with municipal biosolids, green waste and lime

Rogers, Bengson and Thompson 1998, "Reclamation of acidic copper mine tailings using municipal biosolids," *Proc. American Society for Surface Mining and Reclamation* 1998: 85–91, doi:10.21000/JASMR98010085 (PDF https://www.asrs.us/wp-content/uploads/2021/09/0085-Rogers.pdf, read in full 2026-10-25). All **SOURCED** unless marked:
- Substrate: ~40-year-old pyritic tailings near Hayden, AZ; pH 2.5–4.0; very fine sand / silty; rainfall 12.5 in (31.75 cm)/yr.
- Recipe: biosolids at 20, 70, 100, 135 dry tons/acre (45, 157, 224, 303 Mg/ha), biosolids at 3% N (after a measured 50% N loss in 48 h of air exposure). N applied 1,345 / 4,708 / 6,725 / 9,079 kg/ha — the lowest rate was ~5× the agronomic N rate, the others ~17, 25 and 34×. Green waste ground to 4-inch minus, dosed to bring C:N above 30:1 (roughly equal to the biosolids by volume) to immobilize nitrate. Lime (CaCO3) 16.5 tons/acre (36.9 Mg/ha), enough to neutralize 50% of potential acidity to 12 in. Incorporated by moldboard plow to ~12 in (25–30 cm). Spread with a road grader and front-end loader.
- Irrigation needed: spring season 9.7 cm irrigation + 11.4 cm rain; summer 24.1 cm irrigation + 4.8 cm rain; pan evaporation 57.8 and 59.7 in per season.
- Results, first growing season (seeded January 1997, harvested May 1997, ~4–5 months): no biomass on untreated control; 20 tons/acre "highly limited"; best spring growth at 70–100 dry tons/acre (> 74 kg/ha alone; > 448 kg/ha with green waste plus lime at 100 tons/acre). Summer (perennial grasses, Bermudagrass dominant): > 2,802 kg/ha at 100 tons/acre. 135 tons/acre grew LESS (attributed to poor mixing). Biosolids raised tailings pH above 5.75; lime raised control pH from < 4 to > 6; pH drifted down again between January and August.
- Failures: oats and barley went chlorotic in mid-March and died back by late May; plant aluminum possibly phytotoxic. Irrigation system not working until late February, cutting germination. Green waste cut surface nitrate from 23 to 6 mg/kg; no nitrate leaching found below 30.5 cm. Arizona rules at the time capped biosolids at five times the agronomic N rate over five years and banned application to tailings below pH 6.5 — this project needed a regulatory exemption.
- COMPUTED: carbon applied in the paper's Table 1 equals the dry biosolids mass (e.g., 20 tons/acre → 20,000 lb C/acre), i.e. the table appears to assume 50% C on a dry basis (20 short tons = 40,000 lb; 20,000/40,000 = 0.5). Stated as the paper's assumption, not verified.

#### Q1d. Egypt: hyper-arid sandy desert, SEKEM biodynamic farm (compost plus irrigation)

Luske and van der Kamp 2009, *Carbon sequestration potential of reclaimed desert soils in Egypt*, Louis Bolk Instituut & Soil & More International, 35 pp. (https://orgprints.dk/id/eprint/16438/1/2192.pdf, read in full 2026-10-25). All **SOURCED** unless marked:
- Sites: SEKEM farm near Bilbeis (60 km NE of Cairo, founded 1977) and a Sinai farm near the Suez Canal. Rainfall 24.8 mm/yr; mean 21.7 °C; all water from the Nile or groundwater. Fields aged 0 (desert), 1, 4, 5 and 30 years.
- Recipe: compost from rice straw, water hyacinth, wood chips, organic waste, clay, chicken and cow manure; applied before each season, usually twice a year (May and September), plowed to 30 cm. Rates: Sinai new field 30 m3/feddan per season (60 m3/feddan = 138 m3/ha in its first year); SEKEM fields 20 m3/feddan (47.6 m3/ha) per season.
- Compost analysis (Annex 2): bulk density 624 kg/m3, moisture 21.8%, EC 3.2 dS/m, pH 7.6, total organic C 21.6%, organic matter 37.4%, ash 62.6%, total N 0.93%, C:N 23.3.
  - COMPUTED: 47.6 m3/ha × 0.624 t/m3 = **≈ 29.7 t/ha fresh per season, ≈ 59 t/ha/yr at two seasons**; dry ≈ 29.7 × (1 − 0.218) ≈ 23.2 t DM per season; C ≈ 23.2 × 0.216 ≈ 5.0 t C/ha per season. Assumes the annex compost is representative of all years and TOC is on a dry basis (the annex does not say).
- Organic C, 0–10 cm: desert 0.08% (SEKEM) / 0.05% (Sinai); 1 yr 0.24%; 4 yr 0.58%; 5 yr 0.79%; 30 yr 0.99% and 1.39%. 10–30 cm reached 0.32–0.39%; 30–50 cm unchanged.
- Carbon stock, 0–50 cm: SEKEM desert 3.9 t C/ha → 30-yr fields 28.8 and 31.8 t C/ha; Sinai desert 1.6 → 5.7 t C/ha after one year. Rate: 2.7–3.8 t C/ha/yr for the first 5 years, ≈ 0.5 t C/ha/yr from year 5 to 30; 30-year mean ≈ 0.9 t C/ha/yr; curve logarithmic; equilibrium "not yet reached after 30 years."
- Bulk density, 0–10 cm: 1.66 → 1.42 kg/l in 30 years (−14.5%).
- Salt: desert soil EC ~4,000 ppm with visible crystals; cultivated 4-, 5- and 30-year fields 240–750 ppm, the drop attributed to flood-irrigation leaching. Salinity and pH "stabilized more rapidly than carbon levels." pH ROSE from 7.9 to 8.5 (carbonates in irrigation water) — flagged as a phosphate-availability problem.
- Failures: compost floated to low spots under flood/pivot irrigation and was unevenly distributed; nematodes gave very low tomato/eggplant/bean yields on the 4- and 5-year fields; no replicates except the two 30-year fields; Walkley-Black misses charcoal (char from spontaneous windrow combustion found in fields).
- Time to first harvest: crops (peanuts after clover) were growing on the 1-year Sinai field, i.e., harvests began in year 1 under irrigation plus compost. **SOURCED (qualitative).** Yields: **NOT FOUND** in this report.
- SEKEM's own 2025 sponsored message (enterpriseam.com, 2025-11-24) states 725 ha reclaimed over "nearly five decades" and a target of 50,000 ha; no agronomic figures. Self-statement, not independent.

#### Q1e. Sahel: crusted bare "zipellé" ground, zai pits and half-moons (Burkina Faso, Niger)

**Half-moon and zai field trial.** Zougmoré, Zida and Kambou (INERA, Burkina Faso), "Réhabilitation des sols dégradés: rôles des amendements dans le succès des techniques de demi-lune et de zaï au Sahel," IRD/BEEP document (https://beep.ird.fr/collect/bre/index/assoc/19-536-5.dir/19-536-550.pdf, read in full 2026-10-25; trial 1998–1999, Pougyango, 125 km NW of Ouagadougou). All **SOURCED**:
- Substrate: sealed, crusted bare glacis on a 1% slope; shallow Ferric Lixisol, useful depth 25–30 cm; pH(water) < 5.0; organic matter 1.2%; N 0.6 g/kg; total P 0.66 g/kg; CEC 0.11 cmol/kg as printed. Rainfall 30-year mean 630 mm; 690 mm (1998), 747 mm (1999).
- Geometry: half-moons 4 m diameter, 2 m apart in the row, 4 m between rows → 417 half-moons/ha, 6.3 m2 cultivated each. Zai: 31,750 pits/ha (0.80 × 0.40 m spacing).
- Amendment rates: manure or compost 35 kg (one wheelbarrow) per half-moon = 14.6 t/ha; zai 0.3 kg manure per pit (stated as roughly 9.5 t/ha; COMPUTED 31,750 × 0.3 = 9,525 kg/ha). Straw mulch ~10 cm = 5 t/ha. NPK 100 kg/ha + urea 50 kg/ha; Burkina rock phosphate at 20 kg P/ha (25.4% P2O5).
- Sorghum grain (kg/ha) 1998 / 1999: half-moon + manure 1,614 / 1,104; + compost + rock phosphate 927 / 1,104; + compost 1,000 / 875; zai + mulch + rock phosphate 708 / 694; half-moon + mineral fertilizer 500 / 521; zai + mulch 438 / 181; zai alone 375 / 206; half-moon + mulch 83 / 146; half-moon alone 41 / 42; untreated control: zero ("les rendements sont nuls"). The zone's average yield is given as 800 kg/ha.
- Lesson: breaking the crust alone, even with good soil moisture, gave < 100 kg/ha. The water harvest only paid off when nutrients went in with it. Manure raised pH and organic matter; compost, mulch and mineral fertilizer ACIDIFIED this already very acid soil; soil organic matter stayed < 3% in every treatment after one season (highest ~1.70% with zai + mulch + rock phosphate).
- Snippet error caught: a search-engine summary of this paper said "900 to 1600 kg/ha … 20–39 times the yield" of unamended half-moons; the paper's own abstract says 600–1,600 kg/ha. The full text was used.

**Zai labor and inputs.** Motis, D'Aiuto and Lingbeek 2013, *ECHO Technical Note #78: Zai Pit System* (https://reforestation.me/wp-content/uploads/2020/01/tn-78-zai-pit-system.pdfecho.pdf, read 2026-10-25), a secondary compilation. **SOURCED (secondary; original studies cited)**:
- Pits 20–30 cm wide, 10–20 cm deep, 60–100 cm apart; 20,000–25,000 pits/ha; 200–600 g dung or compost per pit (two handfuls ≈ 300 g; Roose et al. 1993); 8–12 seeds per pit.
- Manure needed: "at least 4 tonnes (and up to 18 tonnes/ha)" per hectare of zai (INADES 1993; Kaboré et al. 1994; Sawadogo 1996).
- Labor: ~300 h/ha to dig (Barro et al. 2005); or 450 h/ha to dig plus 250 h/ha to fertilize (Kaboré et al. 1994; Maatman et al. 1997). Done in the dry season, usually by adult men a few hours a day.
- Yields: millet often < 350 kg/ha rising to 1,000–2,000 kg/ha with zai (anecdotal); fields "yielding virtually no grain" giving 300 kg/ha in low-rain years to 1,200 kg/ha in good years (Kaboré and Reij 2004); sorghum 319–642 kg/ha without zai versus 975–1,600 kg/ha with zai at 359–449 mm rain over three seasons (Sawadogo 2011).
- Failure: Fatondji et al. (2006) found zai did not always beat surface-applied organic inputs, partly from nutrient LEACHING out of the wetter pits. Weed seeds in uncomposted manure.

#### Q1f. Shifting sand dunes, Tengger Desert (Shapotou), unirrigated shrub revegetation behind straw checkerboards

- Site: barchan dune chains with vegetation cover < 1%; mean annual precipitation ~180 mm; 122 dust-event days/yr. Railway protection belt for the Baotou–Lanzhou line established 1956, expanded 1964, 1973, 1981 and later, "unirrigated," by planting xerophytic shrubs (Liu et al. 2017, *Biogeosciences Discussions* bg-2017-139, https://bg.copernicus.org/preprints/bg-2017-139/bg-2017-139.pdf, read 2026-10-25). **SOURCED.**
- Soil recovery: across sites revegetated in 1956, 1964, 1973, 1982 and 1991, silt and clay, topsoil depth, crust depth, organic C, K, total N and total P all rose with time. "Most characteristics of topsoil (0–5 cm) had recovered to 60%" of the native reference site by 50 years; exceptions — EC and contents of sand, silt, CaCO3 and organic C — "recovered to 20–40%." Best-fit asymptote models gave **23 to 245 years** for the 50-year site to match the reference (Li, He and Duan 2007, *Geomorphology* 88: 254–265; abstract read at https://cern.ac.cn/5lwycb/detail.asp?id=9362, 2026-10-25). **SOURCED (abstract).** Annual recovery was faster in the first 0–14 years than at 43–50 years (Li et al. 2007a as cited by Liu et al. 2017). **SOURCED (secondary).**
- SOC, 0–10 cm: 0.33 ± 0.11 g/kg in mobile dunes → 5.08 ± 0.11 g/kg in 57-year shrubland; "no significant changes in the first 14 years"; heavy (mineral-associated) fraction share fell from 85.15% to 41.52%, i.e., most new carbon is labile and vulnerable to disturbance (Li Xiaojun, Liu Yubing and Li Xinrong, AGU Fall Meeting 2015, poster B33D-0735; abstract read at https://studio.m-anage.com/agu/fm15/webprogram/Paper67768.html, 2026-10-25). **SOURCED (conference abstract).**
- Biological soil crust bacteria reached peak richness and abundance after ~15 years (Liu et al. 2017). **SOURCED.** Soil respiration rose rapidly 15–20 years after revegetation and stabilized after 25 years (FAO AGRIS record of a 50-year chronosequence study; search summary only). **UNVERIFIED.**
- COMPUTED: 5.08 − 0.33 = 4.75 g/kg gained over 57 years ≈ 0.083 g/kg/yr on average, but per the abstract essentially none of it in years 0–14.
- Kubuqi Desert (Inner Mongolia): the one paper opened (Dang et al. 2022, *Frontiers in Environmental Science* 10.3389/fenvs.2022.950196) is a 1990–2020 remote-sensing study of wind erosion; it attributes 81.14% of the drop in erosion intensity to change in sand type and 14.42% to ecological restoration, with no soil-formation figures. Kubuqi soil-building figures (amendment rates, SOC by age): **NOT FOUND.** Straw-checkerboard soil development (1, 2, 5, 10-year checkerboards: sand share falls, silt and clay rise, nutrients correlate with age; vegetation cover peaked in year 6) was seen only in search summaries of a Chinese journal abstract (journal12.magtechjournal.com abstract10485). **UNVERIFIED.**

#### Q1g. Loess Plateau, China (eroded loess: not sterile, but the largest documented rebuild)

- Grain for Green: SOC in the top 20 cm rising by 0.712 Tg C/yr across the Loess Plateau, projected over 60 years; forest gains stronger in the middle and south, grassland gains stronger in the drier north (Chang, Fu, Liu and Liu 2011, *Environmental Management* 48(6): 1158–1172; abstract read at https://pubs.usgs.gov/publication/70032230, 2026-10-25). **SOURCED (abstract).** Per-hectare rate: **NOT FOUND** in the abstract.
- Check dams (gully dams that trap eroded topsoil; farmed once filled): DESIRE project trial, Mazhuang watershed, Yanhe basin, 2009–2010, rainfall 400–1,100 mm (mean 560 mm): "the yield of check-dam land, terrace, slope crop land is 7800, 4500, 2400 kg per hectare respectively"; plot areas 6.27 ha check-dam land, 18.2 ha bench terrace, 24.5 ha slope cropland (https://desire-his.wur.nl/en/yan-river-basin-china/366-checkdams-and-terraces-experimental-results-and-conclusions.html, read 2026-10-25). **SOURCED.** COMPUTED: 7,800 / 2,400 = 3.25× slope land; 4,500 / 2,400 = 1.9×. A search summary also gave "6000–15000 kg per hectare … about 3–10 times that on the slope" and > 5,000 main check dams and 10,000 km2 of terraces by end of 2011 — **UNVERIFIED** (source not opened). Time to fill a dam, construction labor: **NOT FOUND.**

#### Q1h. Negev Desert, Israel: runoff agriculture on loess (ancient Nabataean/Byzantine systems; Evenari's Avdat farm)

Bruins 1986, *Desert environment and agriculture in the Central Negev and Kadesh-Barnea during historical times*, PhD thesis, Wageningen (https://edepot.wur.nl/201460, relevant chapters read 2026-10-25). All **SOURCED** (Avdat figures are Bruins's compilation of Evenari et al. 1963–1968):
- Ratio of cultivated (runoff-receiving) fields to runoff-producing catchment in the ancient runoff-farming district: average 1:18, range 1:9 to 1:33 (Kedar 1967). Receiving soils must be deep with good water-holding capacity. (A search summary gave "20:1 at Avdat" — **UNVERIFIED**.)
- Avdat experimental runoff farm, wheat: 1961/62 (64.7 mm rain): one flood wetted soil to 120 cm (= 2,000 m3/ha, 200 mm effective); 35 m3/ha manure only; yields 950 and 600 kg/ha. 1963/64 (183.3 mm rain): floods delivered 9,200 m3/ha (= 920 mm effective), soil wet > 3 m; 300 kg/ha ammonium sulfate + 800 kg/ha superphosphate; seed 130 kg/ha; yields 1,950 and 1,390 kg/ha. 1965/66 (91.5 mm): 500 kg/ha superphosphate + 400 kg/ha ammonium sulfate + 40 m3/ha manure; 2,670–4,380 kg/ha (published figures inconsistent). 1962/63, 1964/65, 1966/67: no crop (drought, late flood, or floods too small).
- Six-year average including failed years: **995 kg/ha** — i.e., 3 harvests in 6 years. Bruins estimates ancient unfertilized yields at 500–600 kg/ha (Nizzana papyri calculation: 646 kg/ha).
- Cost, labor: **NOT FOUND** here.

#### Q1i. Coal mine spoil, Ohio, USA (graded with topsoil versus ungraded spoil)

Akala and Lal 2001, "Soil carbon enhancement in graded and ungraded reclaimed minesoil under forest and pasture in Ohio, USA," pp. 494–498 in Stott, Mohtar and Steinhardt (eds.), *Sustaining the Global Farm* (10th ISCO meeting, 1999); peer-reviewed (https://topsoil.nserl.purdue.edu/nserlweb/isco99/pdf/ISCOdisc/SustainingTheGlobalFarm/P030-Akala.pdf, read in full 2026-10-25). All **SOURCED** unless marked:
- Graded (post-1972 law): stored topsoil re-spread at 25–30 cm over regraded spoil. Ungraded (pre-1972): spoil left as a topsoil–overburden mix.
- SOC, 0–30 cm: undisturbed forest 56.6, pasture 66.3 Mg C/ha. Graded: forest 21.8 → 58.9 and pasture 26.1 → 62.7 Mg C/ha after 25 years; the 25-year forest exceeded the undisturbed forest by 2.25 Mg C/ha. Ungraded: 51.5 → 54.9 (forest) and 58.9 → 61.5 (pasture) Mg C/ha from year 30 to 50; neither had reached the undisturbed level at 50 years.
- Rates as stated by the authors: graded 2.0 (forest) and 2.1 (pasture) Mg C/ha/yr; ungraded 1.7 and 1.9 Mg C/ha/yr.
  - COMPUTED check: graded (58.9 − 21.8)/25 = 1.48 and (62.7 − 26.1)/25 = 1.46 Mg C/ha/yr; ungraded year 30–50 (54.9 − 51.5)/20 = 0.17 and (61.5 − 58.9)/20 = 0.13. The ungraded "rates" match stock ÷ years since reclamation (51.5/30 = 1.7; 58.9/30 = 1.96), so they assume a zero starting stock. **The authors' stated rates do not follow from their own start and end values; treat them as upper bounds.**
- Graded-site problems: high compaction, very low aeration and possible anaerobic subsoil below 30 cm, low infiltration, low biomass in the early years "but may be high after 15–20 years"; vegetation establishment hurt in the first 5–15 years by grading compaction and low fertility (Powell 1988, cited). Spoil constraints: low pH, erosion, Al and Mn toxicity, no available N, P, K.
- Second source: total organic carbon in reclaimed coal-mine land rising at an average 0.52 Mg C/ha/yr in 0–30 cm over 26 years (FAO AGRIS record, "Accumulation and composition of total organic carbon in reclaimed coal mine lands"). **UNVERIFIED** — search summary only; record not opened.

#### Q1j. Coal fly ash lagoons

- Fly ash: no organic matter or nutrients, potentially phytotoxic boron, high pH, no ion-exchange complex, erodes when dry; toxicity and salinity are the main limits. A **50–100 mm overlay of local sandy topsoil or compost**, stabilized with coarse organic mulch, hydromulch or erosion-control fabric, gave good germination and growth by keeping the seedbed away from the ash; best plants were xerophytes and halophytes (Aizoaceae, Chenopodiaceae incl. *Atriplex*, Zygophyllaceae) (Jusaitis and Pillman 1997, *Waste Management & Research*; abstract at https://agris.fao.org/search/en/records/671222a07f591113e2a4505f, read 2026-10-25). **SOURCED (abstract).** Boron levels, rates: **NOT FOUND.**
- **Sludge plus fly ash as a topsoil substitute on acid coal refuse.** Sopper 1993, "Stabilization of steep coal waste banks with a sludge-fly ash amendment," ASRS proceedings (https://www.asrs.us/wp-content/uploads/2021/09/0741-Sopper.pdf, read 2026-10-25; the 2-year interim report is ASRS 0413). All **SOURCED**:
  - Substrate: abandoned anthracite refuse bank, eastern Pennsylvania, 75% slope, pH 4.0–4.5, black (very hot surface), low nutrients and water-holding capacity. Plots 6 m × 55 m, 3 replicates.
  - Recipe: excelsior matting stapled on (expands to ~4 cm when wet); lime 2,800 kg/ha to raise pH to 7.0; digested dewatered sludge cake mixed 2:1 by volume with fly ash, thrown into the matting ~5 cm deep by an aerial sludge-spreader truck (50–70 m throw), sludge at **65 dry Mg/ha**, a rate chosen to supply ≥ 1,000 kg/ha total N (the threshold earlier work found assured revegetation). Fly ash was added because sludge alone crusts and becomes impervious. Hydroseeded: tall fescue 22, orchardgrass 22, birdsfoot trefoil 11, crownvetch 11 kg/ha; straw mulch 2,240 kg/ha tacked with fiber mulch 1,350 kg/ha; 60 tree seedlings per plot. Control: lime + 10-10-10 fertilizer 2,240 kg/ha.
  - Results (cover %, dry matter kg/ha) 1989 / 1990 / 1991: sludge-fly ash 57.3 / 62.3 / 83.3% and 5,019 / 6,029 / 8,145 kg/ha; lime-plus-fertilizer control 6.9 / 10.6 / 15.2% and 799 / 824 / 1,285 kg/ha. Foliar trace metals higher on amended plots but below tolerance levels.
  - Companion greenhouse study: paper-mill sludge + fly ash (5 fly ash : 3 sludge by volume) mixed with coal refuse or spoil at 50% and 30% by volume; 50% mix recommended for field use (Sopper, ASRS 0448). **SOURCED (abstract).**

#### Q1k. Fresh glacial till / moraine (unamended natural succession — the "do nothing" baseline)

- Skaftafellsjökull and Breiðamerkurjökull forefields, SE Iceland: SOC accretion "reached the maximum values of 0.004–0.009 kg C m-2 yr-1" (= 0.04–0.09 t C ha-1 yr-1) (Vilmundardóttir, Gísladóttir and Lal 2017, *Geografiska Annaler A* 99(3): 207–221; abstract read at https://opinvisindi.is/handle/20.500.11815/1005, 2026-10-25). **SOURCED (abstract).** The highest rate, 9.1 g m-2 yr-1, was on the 120-year moraine at Skaftafellsjökull (Vilmundardóttir et al. 2015, *Geomorphology* 228: 124–133). **UNVERIFIED** (search summary). SOC in the top 20 cm rose from 0.9 to 13.5 t C ha-1 at sites up to 120 years old (Vilmundardóttir et al. 2015 as cited by Hunziker et al. 2018 preprint). **SOURCED (secondary).**
- COMPUTED comparison, same country: unaided moraine succession at 0.04–0.09 t C/ha/yr versus fertilizer-plus-grass reclamation of eroded desert at 0.4–0.63 t C/ha/yr (Arnalds et al. 2013) — roughly 5–15× faster with intervention (0.4/0.09 ≈ 4.4; 0.63/0.04 ≈ 16). Different substrates and depths; order-of-magnitude only.
- Review: initial forefield soils carry 0.1–40 mg C/g and 0.1–2 mg N/g across 20 studies; phosphorus rises from ~2 to ~8 µg/g (Bradley, Singarayer and Anesio 2014, *Proc. R. Soc. B*, https://pmc.ncbi.nlm.nih.gov/articles/PMC4213609, read to 100,000 characters 2026-10-25). **SOURCED.**

#### Q1l. Dutch polders (drained marine and lake sediment)

- Reed (*Phragmites*) was sown from aircraft on newly dry IJsselmeer polder beds in the 1940s–1950s to draw down water and begin "ripening" (dewatering and structural change) of the soft sediment, then burned off. Wieringermeer (21,000 ha, drained 1927–1930, with a 40 ha experimental polder in 1926–27) had saline soil requiring special reclamation (https://www.flevolandsgeheugen.nl/page/13349/the-wieringermeer-polder, read 2026-10-25). **SOURCED (qualitative only).**
- "After a period of up to 15 years, the polder is ready for growing crops … another ten years is required to bring the salt-saturated soil into a completely effective state of productivity"; reeds burned after ~3 years. **UNVERIFIED** — search summaries of popular sources (blog.uvm.edu page 404 when opened).
- Rates (reed seeding, drain spacing, years per stage, first crops): **NOT FOUND.** Opened: Herweijer 1957 (NJAS; policy, not soil), Wiggers (soil survey of Oostelijk Flevoland, Dutch; no ripening timeline), Nationaal Park Nieuw Land history page (engineering dates only). Unopened leads: Rijkswaterstaat open archive items "Vijftien jaar uitgifte van agrarische bedrijven in Oostelijk Flevoland" and "Ervaringen beginjaren opgedaan."

### Q2. Amendments, rates and effects

#### Q2a. Finished compost: maturity standard, rates, and how much of a mix it makes up

**CCQC Compost Maturity Index** (California Compost Quality Council, Buchanan, Brinton, Shields, West and Thompson, June 2001; https://woodsend.com/wp-content/uploads/2019/09/Compost-Maturity-Index_CA-Compost-Quality-Council_Buchanan_Brinton_2001.pdf, read 2026-10-25). All **SOURCED**:
- Mandatory gate: C:N ≤ 25. Then at least one Group A (stability) and one Group B (maturity) test.
- Group A thresholds (very mature / mature / immature): CO2 evolution < 2 / 2–8 / > 8 mg CO2-C per g volatile solids per day (Soil Control Lab method; Woods End method < 5 / 5–14 / > 14); O2 uptake (OUR) < 0.4 / 0.4–1.3 / > 1.3 mg O2 per g total solids per hour; Dewar self-heating rise < 10 / 10–20 / > 20 °C; Solvita index 7–8 / 5–6 / < 5. (The PDF's unit column abbreviates "mg CO2-C" to "C"; the mg prefix is the standard reading, not printed. **UNVERIFIED** detail.)
- Group B: NH4-N:NO3-N < 0.5 / 0.5–3 / > 3 (unreliable if both < 250 ppm); total NH3-N < 100 / 100–500 / > 500 ppm dry; volatile organic acids < 200 / 200–1,000 / > 1,000 ppm dry; seed germination or plant trial > 90 / 80–90 / < 80% of control.
- Uses: very mature for container mixes, alternative topsoil blends, turf top-dressing; mature for general field use; immature only on fallow land or as compost feedstock.
- Organic C is commonly estimated as organic matter × 0.5–0.58.
- "Compost is used as an additive that may range from 30 to less than 1 percent of the total media or soil volume."
- Field compost composition example (SEKEM, Egypt): C:N 23.3, TOC 21.6%, N 0.93%, EC 3.2 dS/m, bulk density 624 kg/m3 (Q1d).

**Rates.**
- Desert sand, Egypt: ≈ 47.6–69 m3/ha per season, twice a year (≈ 30 t fresh per season; COMPUTED in Q1d).
- Sahel half-moons: 35 kg compost or manure per pit = 14.6 t/ha (Q1e).
- Turf and landscape (U.S. utility guidance, San Antonio Water System, https://saws.org/your-water/water-recycling/compost/compost-application-rates): 2,000–6,000 lb per 1,000 ft2 (½–2 in) mixed into the top 4–6 in for establishment. **UNVERIFIED** (search summary; page not opened). COMPUTED for scale: 1 in over 1 ha = 0.0254 m × 10,000 m2 = 254 m3/ha; at the SEKEM bulk density (0.624 t/m3) ≈ 158 t/ha fresh.

#### Q2b. Biosolids (sewage sludge) — U.S. EPA 40 CFR Part 503 limits

All **SOURCED** from the regulation text (Cornell LII copies: https://www.law.cornell.edu/cfr/text/40/503.13, /503.32, /appendix-B_to_part_503, read 2026-10-25; the eCFR site redirected to a bot wall):
- Ceiling concentrations (mg/kg dry; no biosolids above these may be land-applied): As 75, Cd 85, Cu 4,300, Pb 840, Hg 57, Mo 75, Ni 420, Se 100, Zn 7,500.
- Cumulative pollutant loading rates (kg/ha, lifetime of a site): As 41, Cd 39, Cu 1,500, Pb 300, Hg 17, Ni 420, Se 100, Zn 2,800.
- "Exceptional quality" pollutant concentrations (monthly average, mg/kg dry): As 41, Cd 39, Cu 1,500, Pb 300, Hg 17, Ni 420, Se 100, Zn 2,800 (numerically identical to the cumulative-loading table, in different units).
- Annual pollutant loading rates (kg/ha per 365 days): As 2.0, Cd 1.9, Cu 75, Pb 15, Hg 0.85, Ni 21, Se 5.0, Zn 140.
- Class A pathogens: fecal coliform < 1,000 MPN/g total solids, or Salmonella < 3 MPN per 4 g. Class B: fecal coliform geometric mean < 2,000,000 MPN or CFU/g.
- Composting to Class A (PFRP): in-vessel or aerated static pile ≥ 55 °C for 3 days; windrow ≥ 55 °C for ≥ 15 days with ≥ 5 turnings. PSRP (Class B): ≥ 40 °C for 5 days with 4 hours > 55 °C. Alkaline: pH > 12 for 72 h, > 52 °C for 12 h, then air-dried to > 50% solids.
- COMPUTED consequence: at 250 Mg/ha (the top BC tailings rate, Q1b) a biosolid at the Zn annual limit could not be spread in one year if it carried more than 140 kg/250,000 kg = 560 mg/kg Zn; the BC study's tailings reached 214 mg/kg total Zn. One-time reclamation doses therefore depend on cumulative, not annual, limits plus state permits (Arizona needed a waiver; Q1c).
- Reclamation rates used: 45–303 Mg/ha (Arizona copper), 50–250 Mg/ha (BC copper), 65 Mg/ha with fly ash (Pennsylvania coal refuse; ≥ 1,000 kg N/ha rule of thumb) — Q1b, Q1c, Q1j.

#### Q2c. Biochar

- Jeffery, Abalos, Prodana, Bastos, van Groenigen, Hungate and Verheijen 2017, "Biochar boosts tropical but not temperate crop yields," *Environmental Research Letters* 12: 053001 (abstract read at https://hau.repository.guildhe.ac.uk/id/eprint/15639/, 2026-10-25): global meta-analysis (> 1,000 observations per publicity summaries — **UNVERIFIED** count); "no effect on crop yield in temperate latitudes, yet elicits a 25% average increase in yield in the tropics," the tropical gain coming through liming and fertilization of acid, low-fertility soils; high-nutrient biochars beat low-nutrient ones. **SOURCED (abstract).** Application-rate dependence: **NOT FOUND** in the abstract (full text PDF identified, not read).
- Energy trade-off of making char: biochar production "reduces liquid biofuel yield by at least 21 GJ Mg-1 C" (biofuel energy given up per tonne of biochar carbon; methanol synthesis route), and at least 33 GJ per Mg biochar C for gaseous-biofuel routes; slow pyrolysis is defined there as heating rate < 10 °C/s; char yields fall with rising temperature and heating rate (Woolf, Lehmann, Fisher and Angenent 2014, *Environmental Science & Technology* 48: 6492–6499; PDF from Cornell, read 2026-10-25). **SOURCED.** In other words, pyrolysis vapors normally carry enough energy to run the process, and the "cost" of char is the fuel not made.
- Char yield per tonne of feedstock (slow pyrolysis): "30–35%", maize residues 30.7–37.9% at optimum; "biochar retains approximately 20% of the weight and 30% of the energy of the biomass"; surplus 0.3–11 MJ of fuels per kg feedstock. **UNVERIFIED** — all from search summaries of lecture notes and unnamed sources; the Woolf PDF did not contain the 0.3–11 MJ figure. Treat as range indicators only.
- Biochar application rates with effect sizes: **NOT FOUND** (Jeffery 2017 full text not read).

#### Q2d. Rock dust: basalt and glacial rock flour

- **Field, U.S. Corn Belt:** crushed basalt 50 t/ha every fall for 4 years (2016–2020), maize–soybean rotation; yields +12 to 16% (P < 0.05); cumulative CO2 removal 10.5 ± 3.8 t CO2/ha over 4 years; higher K, Mg, Mn, P, Zn; no rise in trace metals in grain or soil exchangeable pools (Beerling et al. 2024, *PNAS* 121(9): e2319436121, doi:10.1073/pnas.2319436121; abstract read at https://eprints.whiterose.ac.uk/209862, 2026-10-25). **SOURCED.** COMPUTED: 4 × 50 = 200 t basalt/ha in total; 10.5 t CO2 / 200 t rock ≈ 0.05 t CO2 per t rock over 4 years.
- **Mesocosm, UK clay loam:** basalt 10 kg/m2 (= 100 t/ha); sorghum yield +21 ± 9.4% after 120 days without P or K fertilizer; shoot Si +26 ± 5.4%; CO2 removal estimated 2–4 t CO2/ha within 1–5 years (Kelland et al. 2020, *Global Change Biology* 26(6): 3658–3676; abstract at https://eprints.whiterose.ac.uk/160618). **SOURCED (abstract).**
- **Counter-evidence, UK soil cores under real weather:** 100 t basalt/ha on lime-rich, unirrigated cropland released alkalinity at 310 ± 30 eq/ha/yr = **10.2 ± 0.8 kg CO2/ha/yr**, "5- to 25-fold slower than previous modelled assessments," water-limited; "accumulation of undissolved basalt may also lead to large and irreversible changes to soil compositions following repeated application" (Buckingham, Henderson, Holdship and Renforth 2022, *Applied Geochemistry*; abstract at https://ora.ox.ac.uk/objects/uuid:1fd3be9d-9760-49dd-9058-90e566572dce, 2026-10-25). **SOURCED.**
  - COMPUTED contrast: Kelland's 2–4 t CO2/ha (1–5 yr) against Buckingham's 0.0102 t CO2/ha/yr at the same 100 t/ha is a ~40–400× spread at the upper and lower ends (2/0.0102/5 ≈ 39; 4/0.0102 ≈ 390). Weathering speed of rock dust in a given soil is not a settled number.
- **Glacial rock flour, South Greenland:** timothy grass field, summer 2019; 20 t GRF/ha alone: no significant biomass response; 20 t/ha + 25% NPK: "marked and significant increase"; 40 t/ha + 25% NPK: significant yield REDUCTION; no change in soil pH or nutrient availability versus control in one season; "needs to be further investigated before it can be recommended" (Sukstorf, Bennike and Elberling 2020, *Land* 9(6): 198; abstract at https://agris.fao.org/search/en/records/67598bf4c7a957febdfbc524). **SOURCED (abstract).**
- Glacial rock flour elsewhere: 10 and 50 t/ha on Danish sand (maize, potatoes); Ghana 50 t/ha raised maize grain and dry matter in all five seasons by 28–87% (Gunnarsen et al. 2023 and a 2025 *Nutrient Cycling in Agroecosystems* paper). **UNVERIFIED** — search summaries only; Springer pages redirect to a login.
- Review: Swoboda, Döring and Hamer 2022, "Remineralizing soils? The agricultural usage of silicate rock powders: A review" (*Science of the Total Environment*): of 48 crop trials, promise "as alternative K source and multi-nutrient soil amendment for tropical soils," temperate benefits "currently inconclusive"; best performers mafic and ultramafic rocks (basalt), nepheline- or glauconite-bearing rocks. **SOURCED (abstract via remineralize.org).** Rates and effect sizes from the 48 trials: **NOT FOUND** (bonndoc full text returned an access-denied bot wall).
- Grain size: silt-sized (< 45 µm) basalt weathers about twice as fast as sand-sized (150–500 µm); mm-sized basalt grains nearly completely broken down "on a decadal timescale" at a > 20-year site. **UNVERIFIED** (search summary of a 2023 *Applied Geochemistry* paper and others; not opened).

#### Q2e. Manure (rates actually used, and how long its effect lasts)

- Sahel: 0.3 kg per zai pit (≈ 9.5 t/ha) or 35 kg per half-moon (14.6 t/ha); 4–18 t/ha per hectare of zai (Q1e). **SOURCED.**
- Negev runoff farm: 35 m3/ha manure alone gave 600–950 kg/ha wheat in one flood year; 40 m3/ha plus mineral fertilizer in another (Q1h). **SOURCED.**
- **Duration of a single heavy dose, sandy nursery soil (New York):** Bickelhaupt 1987, "Use of sulfur to correct soil pH," USDA Forest Service GTR RM-151: 58–65 (https://npn.rngr.net/publications/proceedings/1987/bickelhaupt.pdf, read 2026-10-25). A single **6-inch (≈ 15 cm)** layer of composted, lime-treated horse manure on loamy sand (80–90% sand) in 1974 raised organic matter from 3.6% to 9.1% (1975), 8.4% (1976), 9.1% (1977), then fell to **4.5% by 1983**; pH rose 5.7 → 7.3 and stayed ~7 for 12 years (the stable floors had been limed daily), which then caused nursery problems (damping-off risk, nutrient imbalance). **SOURCED.** COMPUTED: about (9.1 − 4.5)/(9.1 − 3.6) ≈ 84% of the organic-matter gain lost in ~6 years after 1977. The 1973–77 applications elsewhere in the nursery were 2–12 in. **SOURCED.**

#### Q2f. Biological amendments: legume cover crops, rhizobia, mycorrhizae, biocrusts

- **Legume cover crops** (*Managing Cover Crops Profitably*, 3rd ed., SARE 2007, crimson clover chapter, https://sare.org/publications/managing-cover-crops-profitably/legume-cover-crops/crimson-clover, read 2026-10-25): crimson clover 3,500–5,500 lb dry matter/A and 70–150 lb N/A fixed by mid-May (USDA Zone 8); up to 7,800 lb DM and 180 lb N/A at Beltsville, MD (1996); seed 15–18 lb/A drilled or 22–30 lb/A broadcast. **SOURCED.** COMPUTED: 1 lb/A = 1.121 kg/ha, so 70–150 lb N/A ≈ 78–168 kg N/ha; 3,500–5,500 lb/A ≈ 3.9–6.2 t DM/ha. Hairy vetch: 4,000–7,000 lb/A biomass and > 150 lb N/A (SARE summary) and 186 kg N/ha aboveground in late November in one study. **UNVERIFIED** (search summaries; not opened).
- **Iceland lupine:** rhizobium inoculation was the condition of survival on bare sand (Q1a). **SOURCED.**
- **Rhizobia inoculants, soybean, field:** meta-analysis of 28 peer-reviewed field studies: grain yield change from **−34% to +109%** versus uninoculated controls; nodule number −28 to +178; grain N −6% to +176%; largest nodulation gains where indigenous rhizobia were absent or very low; indigenous strains "may be better adapted to local environmental stress" (Thilakarathna and Raizada 2017, *Soil Biology and Biochemistry*; abstract at https://agris.fao.org/search/ar/records/6765a06550e69ae818393ec2, 2026-10-25). **SOURCED (abstract).**
- **Arbuscular mycorrhizal fungi (AMF), rainfed field and pot:** inoculation raised yield 23.0% across 13 crops (546 paired observations, 1950–2021); N-fixing crops +29.4% (CI 16–43%), non-N-fixing +20.4% (CI 12–28%); wheat +34.1%; authors found no publication-bias pattern (Wu, Shi, Chen, Gao and Wang 2022, *PeerJ*; https://pmc.ncbi.nlm.nih.gov/articles/PMC8815364/, read to 100,000 of 148,244 characters, 2026-10-25). **SOURCED.** Caution: a separate study tested 28 commercial AMF inoculants under greenhouse and field conditions (Salomon et al. 2022, *Applied Soil Ecology*, doi:10.1016/j.apsoil.2021.104225); its results (how many products actually colonized roots): **NOT FOUND** — the record and repository pages gave no abstract or a 403.
- **Biological soil crusts (biocrusts), Colorado Plateau:** greenhouse-cultivated cyanobacterial crust applied to bare field plots "attaining ~82% cover in only one year," faster than field-collected crust, but field-collected crust gave more species, biomass and development; mosses and lichens did not establish well (Antoninka, Bowker, Chuckran, Barger, Reed and Belnap 2018, *Plant and Soil*; abstract at https://experts.nau.edu/en/publications/maximizing-establishment-and-survivorship-of-field-collected-and-/, 2026-10-25). **SOURCED.** Counter-result: field-cultivated inocula five months after inoculation showed "no significant increases in cyanobacterial abundance, soil chlorophyll a, or soil exopolysaccharide content"; most cyanobacteria needed habitat amelioration (Jech et al. 2025, *Applied Soil Ecology*; abstract at https://pubs.usgs.gov/publication/70268885). **SOURCED.** China review: cyanobacteria have been inoculated at "hundreds of ha"; mosses only at "several m2"; keeping the surface wet after inoculation (micro-sprinklers) and blocking moving sediment were crucial (Zhou, Zhao, Belnap et al. 2020, *Restoration Ecology* 28(S2): S45–S55; abstract at https://pubs.usgs.gov/publication/70209759). **SOURCED.** Inoculation rates (g/m2) and costs: **NOT FOUND.**

#### Q2g. Humic substances

- Meta-analysis: shoot dry weight +22 ± 4% and root dry weight +21 ± 6% on average; responses "inconsistent and relatively unpredictable when compared to inorganic fertilizers," driven mainly by source and rate; compost-derived humics significantly outperformed lignite- and peat-derived; rate effect non-linear (Rose, Patti, Little, Brown, Jackson and Cavagnaro 2014, *Advances in Agronomy* 124: 37–89; abstract at https://researchportal.scu.edu.au/esploro/outputs/journalArticle/A-Meta-Analysis-and-Review-of-Plant-Growth/991013134013802368, 2026-10-25). **SOURCED (abstract).** Application rates (kg/ha): **NOT FOUND** in the abstract.

#### Q2h. Zeolite (clinoptilolite)

- Single field studies (Iran, mostly) tested 0, 5, 10, 15 t/ha and 0, 2, 4, 8 t/ha; 10–15 t/ha raised CEC, soil total N, grain yield and N-use efficiency; one study's best yield at 80 kg N/ha + 4 t/ha zeolite. **UNVERIFIED** (search summaries of journals.scu.ac.ir and redalyc PDFs; not opened). No meta-analysis found. Effect sizes: **NOT FOUND.**

#### Q2i. Peat and coir (growing-media bases)

- Coir (coconut husk pith), compiled ranges (Minnesota Stormwater Manual, https://stormwater.pca.state.mn.us/Chemical_and_physical_properties_of_coir, read 2026-10-25, citing Abad et al. 2002, 2005 and others): pH 4.9–6.9 (median 5.9); CEC 31.7–130 cmol/kg (median 50); total C 42–49%; total N 0.24–0.5%; total K 0.4–2.39% dry wt; water-holding capacity 137–1,100% by weight (median 566); total pore space 85.5–98.3% (median 95.2); bulk density 0.025–0.132 g/cm3 (median 0.06). **SOURCED (secondary compilation).** EC is printed as "39–2900 (median 582) ds/m" — physically implausible for a growing medium (seawater is ~50 dS/m); probably µS/cm. **Units UNVERIFIED; do not use the EC figure.**
- Coir's high K and Na are typically removed by washing and by buffering with calcium and/or magnesium nitrate solutions. **UNVERIFIED** (search summary). Coir pith C:N ~100:1 so it supplies no N. **UNVERIFIED.**
- Peat properties and peat-free substitution ratios: **NOT FOUND** in this pass.

#### Q2j. Sulfur for alkaline soil (gypsum for sodic soil is under Q3)

Bickelhaupt 1987 (as above), all **SOURCED**:
- Rule-of-thumb rates quoted there: 500 lb/ac granular S lowers pH ~0.5 unit in the top 6 in of sandy nursery soil (White et al. 1980); to go from pH 7.5 to 6.5: 500 / 800 / 1,000 lb/ac S for sandy / loam / clay (Western Fertilizer Handbook 1980); silt loam 7.0 → 6.0 needs 870 lb/ac and 7.0 → 5.5 needs 1,525 lb/ac (Stoeckeler and Arneman 1960); do not exceed 750 lb/ac at once on sandy nursery soil (Armson and Sadreika 1979).
- Trial result on loamy sand: 890–3,560 lb/ac granular S and sulfuric acid; only **1,780 lb/ac S + 1,780 lb/ac S as sulfuric acid** reached the target (pH 6.5 → 5.5 at 8 months), and the effect faded: 5.6 at 12 months, 6.1 at 20 and 23 months (control 6.9). Sulfuric acid acted faster; granular S slower.
- COMPUTED: 1 lb/ac = 1.121 kg/ha; 500–1,000 lb/ac ≈ 560–1,120 kg S/ha; 1,780 + 1,780 lb/ac ≈ 4.0 t S/ha.
- MSU Extension table (lower pH to 6.5 at 7-inch depth: sandy 30, loam 35, clay 45 lb S per 1,000 ft2 from pH 8.0; effect 6–8 weeks; re-treat every 2–3 years). **UNVERIFIED** (search summary; MSU page and PDF both failed to load). COMPUTED if true: 30–45 lb/1,000 ft2 ≈ 1,307–1,960 lb/ac ≈ 1.5–2.2 t S/ha.

### Q3. Salt: flushing and neutralizing saline or sodic ground

#### Q3a. Leaching saline soil (FAO Irrigation and Drainage Paper 29, *Water Quality for Agriculture*, Ayers and Westcot)

Section 2.4 "Management of salinity problems" (http://www.fao.org/4/t0234e/T0234E03.htm, read 2026-10-25). All **SOURCED**:
- Leaching fraction: "the portion of the irrigation which should pass through the root zone to control salts at a specific level."
- Minimum leaching requirement: **LR = ECw / (5·ECe − ECw)**, where ECw is irrigation-water salinity and ECe the soil-extract salinity the crop tolerates. Annual applied water: **AW = ET / (1 − LR)**.
- Reclaiming an already-salty profile (section 2.4.6, Figures 19–20): continuous ponding removes "70–80 percent of the soluble salts initially present … with a depth of applied water equal to the depth of soil to be reclaimed"; intermittent ponding or sprinklers remove "80–90 percent" with the same depth of water, "but more time is required."
- COMPUTED, water volumes: 1 m of water over 1 ha = 10,000 m3. So reclaiming the top 1 m to ~70–80% salt removal by ponding needs ≈ 10,000 m3/ha (net of evaporation, and only if it drains). Top 30 cm: ≈ 3,000 m3/ha. Worked LR example (assumption: irrigation water ECw = 1.0 dS/m, crop threshold ECe = 2.0 dS/m): LR = 1.0 / (5 × 2.0 − 1.0) = 0.11; with ET = 800 mm/yr, AW = 800 / 0.89 ≈ 900 mm/yr, i.e., ≈ 100 mm/yr (1,000 m3/ha/yr) goes purely to flushing.
- Empirical leaching curve (Hoffman form): C/C0 = k / (Dw/Ds), with k ≈ 0.45 organic soils, 0.3 clay loam, 0.1 sandy loam; rule of thumb "a unit depth of water will remove nearly 80 percent of soluble salts from a unit soil depth." **UNVERIFIED** (search summaries of UC ANR Salinity pages and a LibreTexts course; the UC ANR page returned 404).

#### Q3b. Drainage (salt has to leave the field, not just go down)

ICAR–Central Soil Salinity Research Institute, *Reclamation of waterlogged saline soils through subsurface drainage technology*, Technology Folder 2016/02 (compiled by Sharma, Kaledhonkar, Thimmappa and Chaudhari; https://cssri.res.in/images/stories/pdf/dr16.pdf, read in full 2026-10-25). All **SOURCED**:
- Target soils: water table within 1.5–2.0 m, ECe > 4 dS/m, pHs < 8.2, ESP < 15.
- System: perforated PVC laterals (gravel or synthetic filter), slope 0.05–0.10% for 100–150 mm pipe, laid by hand or laser-guided trencher; gravity or pumped outlet.
- Design table: arid climate drainage coefficient 1–2 mm/day (optimum 1), drain depth 0.9–1.2 m, spacing 100–150 m (light soils); semi-arid 1–3 mm/day, 1.2–1.8 m deep, 50–100 m (medium); sub-humid 2–5 mm/day, 30–50 m spacing (heavy). Haryana practice: 66 m spacing, 1.5 m average lateral depth. Peninsular India: 30 m spacing, 1.2 m depth. Vertisols: 30 m, 1.0–1.5 m laterals, 2.0 m collectors.
- Cost (2015 prices): ₹65,000/ha (Haryana alluvial) to ₹1,25,000/ha (heavy Vertisols); materials ≈ 60–65%, labor and machinery 20–25%, land development 10–20%. Benefit–cost 1.5–3.2; IRR 17–58%; payback 3–5 years; operating cost "virtually nil" with a gravity outlet.
- Results: yields up > 50% (paddy) and > 100% (wheat, cotton); cropping intensity +40%; Gohana, Sonepat: water table 1.07 m drained vs 0.63 m undrained; wheat 3.6 vs 2.4 t/ha; pearl millet +64%; drainage effluent 1.23–3.03 dS/m (reusable for irrigation). ~66,500 ha reclaimed in India by 2016.
- Egypt, Ibshan subsurface-drainage assessment: yields of five crops +7% to +38%; 16.4% of saline area improved. **UNVERIFIED** (search summary of El-Hazek 2013; PDF not opened).
- SEKEM desert soils lost most salt within the first few years under flood irrigation (EC ~4,000 ppm → 240–750 ppm), but irrigation-water carbonates pushed pH up from 7.9 to 8.5 (Q1d). **SOURCED.**

#### Q3c. Sodic soils: gypsum and its equivalents

- FAO Paper 29, section 3.2.1 (http://www.fao.org/4/t0234e/T0234E04.htm, read 2026-10-25), all **SOURCED**: granular gypsum broadcast at **5 to 40 t/ha**, "40 t/ha rate is used as a one-time application for extremely sodic soils"; finely ground gypsum (< 0.25 mm) dissolves much faster; for water application, 1 meq/L Ca = 86 kg of 100% gypsum per 1,000 m3 water (worked example: 1,230 kg of 70%-pure gypsum to raise 5 ha × 100 mm of water by 2 meq/L). Amendment equivalents to 1 t of 100% gypsum (Table 12): sulfur 0.19 t, sulfuric acid 0.61 t, calcium chloride 0.86 t.
- Chemistry basis: 1 cmolc of gypsum weighs 0.86 g, so replacing 10 cmolc/kg exchangeable Na in 1 kg soil needs 8.6 g gypsum; the lab Schoonover method shakes soil in saturated gypsum solution (~29 cmolc/L) (Dellavalle and Walworth, *Crops & Soils*, 4 May 2020, https://www.sciencesocieties.org/publications/crops-soils/2020/may-june/determining-the-gypsum-requirement-for-reclamation-of-sodic, read 2026-10-25). **SOURCED.**
- Rule of thumb: "1.7 tons of gypsum are required to replace 1.0 cmolc/kg of sodium"; worked example CEC 20 cmolc/kg, ESP 15% → 5%: 0.1 × 20 = 2.0 cmolc/kg → 3.4 t, or 4.8 t at 70% purity; a good-quality water source and internal drainage are prerequisites. Mined gypsum is 70–90% pure; flue-gas-desulfurization gypsum ≥ 96% (Espinoza and Ismanov, University of Arkansas Extension FSA2199, *Gypsum as a Soil Amendment*; PDF read 2026-10-25). **SOURCED.** The sheet does not state the depth or area unit behind 1.7 t.
  - COMPUTED check: 0.86 g/kg per cmolc × soil mass of 1 ha to 15 cm at 1.33 t/m3 (1,500 m3 × 1.33 ≈ 1,995 t) ≈ **1.72 t gypsum per ha per cmolc/kg Na, for the top 15 cm**. The rule matches t/ha at ~15 cm depth (or roughly short tons per acre at ~30 cm). Assumption: bulk density 1.33.
- Phosphogypsum is restricted in U.S. agriculture because of radium (radioactivity limit). **SOURCED (FSA2199, qualitative).**
- Leaching water needed to carry the displaced Na out after gypsum: **NOT FOUND** as a sourced figure (Dellavalle and Walworth state none).

### Q4. Speeding formation in controlled conditions

#### Q4a. Thermophilic composting timelines

- FAO, *On-farm composting methods* (2003, Land and Water Discussion Paper; http://www.fao.org/4/y5104e/y5104e07.htm, read 2026-10-25; authors not shown on the page read): turned windrow "active composting stage generally lasts three to nine weeks … Eight weeks is usual for manure composting operations," turned daily at first for high-N mixes, then weekly; aerated static pile active phase "about three to five weeks," no turning; rectangular agitated beds "two to four weeks," turned daily or every other day; a bin example (Phnom Penh) reached 70 °C and took "about two months." **SOURCED.**
- Pathogen-kill floors for Class A biosolids compost: ≥ 55 °C for 3 days (in-vessel/static pile) or ≥ 15 days with ≥ 5 turnings (windrow) (Q2b). **SOURCED.**
- Passively aerated windrows 10–12 weeks plus 1–2 months curing; unmanaged passive piles ~1 year. **UNVERIFIED** (search summary of extension sources; Oregon State PDF returned HTML; BC factsheet socket hang-up).
- Stability after the active phase is judged by the CCQC tests (Q2a). **SOURCED.**

#### Q4b. Vermicomposting

Ndegwa, Thompson and Das 2000, "Effects of stocking density and feeding rate on vermicomposting of biosolids," *Bioresource Technology* 71: 5–12 (PDF https://www.lehighcountyauthority.org/wp-content/uploads/effect-of-stocking-density-feeding-rate-on-vermicomposting-of-biosolids-1.pdf, read 2026-10-25). All **SOURCED**:
- *Eisenia fetida* on biosolids with paper-mulch bedding (first two weeks 4 parts biosolids : 3 parts paper by dry weight, then biosolids only), 25 ± 6 °C, moisture 76.3 ± 1.6% wet basis, 8 weeks.
- Tested 0.80–2.00 kg worms/m2 and 0.75–1.25 kg feed/kg worm/day. Best worm growth: **1.60 kg worms/m2 at 1.25 kg feed/kg worm/day**; best vermicompost: **1.60 kg/m2 at 0.75 kg feed/kg worm/day**. Earlier literature: 1 g worm converts 4 g activated sludge in 5 days (≈ 0.8 kg/kg/day; Hartenstein and Hartenstein 1981); worms "can consume their own weight in 24 h" (Riggle and Holmes 1994). Whether the feed rate is on a wet or dry basis is not stated in the passages read.
- Total-solids reduction after 8 weeks 31–42%, total weight 19–37%; volatile-solids reduction "still low (at 12%) … probably still not stable."
- COMPUTED throughput: 1.60 kg worms/m2 × 0.75 kg feed/kg/day = 1.2 kg feed per m2 of bed per day ≈ 438 kg/m2/yr; one tonne of feed needs ≈ 833 m2·days of bed (e.g., 14 m2 for 60 days). Assumes the optimal rate is sustained.
- Vermicomposting efficiency 87–105 kg/m2 over 120 days on rice straw and grass. **UNVERIFIED** (search summary of an Egyptian journal paper).

#### Q4c. Black soldier fly (*Hermetia illucens*) frass

Basri, Azman, Ahmad, Suja, Jalil and Amrul 2022, "Potential applications of frass derived from black soldier fly larvae treatment of food waste: a review," *Foods* (https://pmc.ncbi.nlm.nih.gov/articles/PMC9455751, read to 100,000 of 137,546 characters, 2026-10-25). All **SOURCED (review)**:
- Larvae "can eliminate more than 50% of total organic waste in a short period (two weeks)"; frass harvested after 9–23 days.
- Yields: 1,000 kg food-and-vegetable substrate → 250 kg frass (25.0%) + 125 kg larvae (12.5%); 30 t/day food waste → 9,990 kg/day frass (33.3%) + 2,310 kg/day larvae (7.7%). (Search summaries also gave brewery waste 33.8% frass / 2.5% larvae, poultry manure 62.9% / 6.4% — **UNVERIFIED** as to source.)
- Frass: total N 0.6–4.8%, P 0.8–2.5%, K 0.2–2.1%; C:N 8:1 to 27:1; moisture 30–72%. Food-waste frass mostly > 45% moisture and immature; "there is the need for post-treatment." Some pathogens may persist even though larvae reduce *Salmonella*.
- Use: maize responded to composted frass at 2.5 t/ha.

#### Q4d. Bokashi (lactic-acid fermentation of food waste)

Christel, SARE Graduate Student grant GNE15-098, University of Vermont, 2015–2016 (https://projects.sare.org/project-reports/gne15-098/, read 2026-10-25). All **SOURCED**:
- Bran inoculant fermented 2 weeks; food-waste bokashi buckets 3 weeks sealed.
- Product: NH4-N 1,410 mg/kg, NO3-N 25.95 mg/kg, pH 4.21 (vermicompost: NH4 20.8, NO3 4,745 mg/kg; thermophilic compost: NH4 10.2, NO3 33.6 mg/kg).
- Field spinach at 112 kg N/ha from each amendment: bokashi 4.5 t/ha, vermicompost 3.0 t/ha, thermophilic compost 1.9 t/ha.
- Constraint: applied **two weeks before transplanting** to let soil pH recover from 4.2.

#### Q4e. Anaerobic digestate

- Solid digestate 26–49% of N as NH4+; liquid fraction more; trials at 120–140 kg total N/ha gave > 13 t/ha dry biomass, comparable to mineral fertilizer; risks of ammonia volatilization, nitrate leaching and sometimes higher N2O; digestion lowers C:N and leaves more recalcitrant carbon. **UNVERIFIED** — search summaries of a 2025 preprint and an Italian agronomy paper (research.unipd.it PDF identified, not opened). Application rates in m3/ha: **NOT FOUND.**

#### Q4f. Ratios of organics to mineral material in constructed growing media, and how fast they "work"

Deeb et al. 2020 (full author list not checked), "Using constructed soils for green infrastructure – challenges and limitations," *SOIL* 6: 413 (https://soil.copernicus.org/articles/6/413/2020/, read to 100,000 of 132,939 characters, 2026-10-25), and the authors' response to reviewers (soil-2019-85-AC1, read in full). All **SOURCED** (review; original studies cited):
- Excavated deep subsoil + compost: "a mix of 30% compost with 70% excavated deep horizon to a depth of 30 cm would be applicable for parks and urban farming," the same mix 1–2 m deep for street trees; "20% compost is suitable for open parks in temperate areas, 40–50% compost is needed in dry areas"; "even low ratios … (i.e., 10% compost with 90% excavated deep horizons) could be used as a B horizon." Recommendation for parks and lawns: 20–30% compost by volume.
- Demolition waste + compost tested at 0, 10, 20, 30, 40, 50% compost (v/v) (Deeb et al. 2016–2017).
- Street-tree profiles: 65% ground stone + 35% soil base layer (100–150 cm) under 30–50 cm organic material (Daunay 1999); growing horizon 60% crushed brick + 40% sewage sludge and green waste (Cannavo et al. 2018).
- Trees in parks: "10% green waste compost and 70% crushed concrete" (with 20% excavated deep horizon per a search summary — the 20% share is **UNVERIFIED**) gave the best tree survival, growth and fastest macrofauna colonization; the highest tree mortality was in excavated deep horizon + green waste compost (Pruvost et al. 2018).
- SITERRE project (France): binary mixes 0/100, 20/80, 50/50, 80/20, 100/0 (v/v); ternary mixes 60% coarse mineral + 40% organic-mineral mix (Rokia et al. 2014).
- Speed: aggregation after one wet–dry cycle (1 week in the lab); "after 5 months, the same Technosols showed a high ability to aggregate" (Deeb 2017); carbon released in the first months then "almost completely fixated in the next 3 years" (Shchepeleva et al. 2017, 2019).
- Early risks: erosion, runoff and compaction before structure forms; fresh organic waste can be phytotoxic; high mineralization of organic matter early, especially at high organic doses; metals accumulate with repeated organic additions; sewage-sludge compost adds microplastics.
- Compost as a share of growing media generally: "from 30 to less than 1 percent of the total media or soil volume" (CCQC 2001; Q2a).
- COMPUTED, "one tonne of rock fines plus organics": using the 70:30 subsoil:compost volume recipe and assumed bulk densities (subsoil fines 1.5 t/m3; compost 0.62 t/m3 per SEKEM), 0.7 m3 subsoil ≈ 1.05 t + 0.3 m3 compost ≈ 0.19 t → ≈ 1.24 t per m3 of mix, i.e., ~15% compost by mass. Structure forms within months (5 months for high aggregation; Deeb 2017); carbon stabilizes over ~3 years. For crushed basalt or other fresh rock (no clay, no microbes), no constructed-soil study giving a time-to-function was found: **NOT FOUND**.

### Q5. Regolith agriculture (Mars and Moon simulants)

**Review used as the spine:** Duri, Caporale, Rouphael, Vingiani, Palladino, De Pascale and Adamo 2022, "The potential for lunar and Martian regolith simulants to sustain plant growth: a multidisciplinary overview," *Frontiers in Astronomy and Space Sciences*, published 4 January 2022, doi:10.3389/fspas.2021.747821 (https://www.frontiersin.org/articles/10.3389/fspas.2021.747821/full, read to 100,000 of 159,315 characters, 2026-10-25). Its summaries are **SOURCED (secondary)**; primary papers opened directly are marked so.

#### Q5a. Wageningen (Wamelink et al.)

- **2014, unamended simulants** (Wamelink et al. 2014, *PLOS ONE*, doi:10.1371/journal.pone.0103138; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0103138, read 2026-10-25): JSC-1A Mars and JSC-1A lunar simulants versus a nutrient-poor, organic-matter-free Rhine subsoil from 10 m depth; 14 species (tomato, wheat, cress, carrot, four N-fixers, six wild Dutch species); 50 days from 8 April 2013; demineralized water only, no nutrients. Plants germinated and grew on both; Mars simulant gave significantly higher biomass than both other soils; germination highest on Mars, lowest on Moon simulant; three species flowered (field mustard, rye, cress), cress and mustard set seed. Problems: lunar simulant high pH; lunar simulant dried fastest (Mars held water best); aluminum possibly toxic; nitrogen limiting. **SOURCED.**
- **2019, simulant + organic matter** (Wamelink, Frissel, Krijnen and Verwoert, *Open Agriculture*, October 2019, doi:10.1515/opag-2019-0051; abstract read at https://research.wur.nl/en/publications/crop-growth-and-viability-of-seeds-on-mars-and-moon-soil-simulant/): simulants "mixed with organic matter to mimic the addition of residues from earlier harvests"; per the Duri review, the organic matter was "fresh mown grass of *Lolium perenne*" and "a nutrient solution was also added to mimic the addition of human feces and urine." Ten crops (garden cress, rocket, tomato, radish, rye, quinoa, spinach, chives, pea, leek): nine grew well, spinach failed; edible parts harvested from nine of ten; total biomass per tray highest for Earth control and Mars simulant, significantly lower on Moon simulant; radish seed from Moon simulant germinated significantly worse. **SOURCED.** Grass-to-simulant ratio and yields per tray: **NOT FOUND** (publisher page 405; WUR edepot PDF came back empty).

#### Q5b. University of Florida: real Apollo lunar regolith (Paul, Elardo and Ferl 2022)

"Plants grown in Apollo lunar regolith present stress-associated transcriptomes that inform prospects for lunar exploration," *Communications Biology* (May 2022; PDF copy read 2026-10-25 from https://static.poder360.com.br/2022/05/plants-grown-in-apollo-lunar-study.pdf). All **SOURCED**:
- 900 mg of regolith per well, over a 0.45 µm filter and Rockwool wick, in 48-well plates with subsurface irrigation; moistened daily with nutrient solution; 3–5 *Arabidopsis* seeds per well; harvested at 20 days. Samples: Apollo 11 (mature), Apollo 12 (submature), Apollo 17 (immature); control JSC-1A.
- Germination "close to 100%" in all lunar samples, indistinguishable from JSC-1A, beginning about 48 h after sowing. After ~8 days growth became slower and more variable; root growth weaker; some plants severely stunted and deeply pigmented.
- Differentially expressed genes: Apollo 11 = 465, Apollo 12 = 265, Apollo 17 = 113 — stress worsened with regolith maturity (longer space-weathering exposure, more agglutinate glass and nanophase iron). Genes indicated ionic stress like salt, metal and reactive-oxygen stress. One Apollo 11 plant died.
- UF/IFAS release (12 May 2022): "approximately a gram of lunar soil" per pot; "less mature soils" grew better plants. **SOURCED.**

#### Q5c. Naples: Mojave Mars Simulant + green compost (lettuce)

Duri et al. 2020, "Mars regolith simulant ameliorated by compost as in situ cultivation substrate improves lettuce growth and nutritional aspects," *Plants* 9(5): 628 (https://pmc.ncbi.nlm.nih.gov/articles/PMC7285329/, read to 100,000 of 118,632 characters, 2026-10-25). All **SOURCED**:
- MMS-1: alkaline, mostly plagioclase and amorphous material with zeolite, hematite and smectite; no organic matter, N, P or S; rich in Ca and Mg.
- Mixtures simulant:compost (v:v) 100:0, 70:30, 30:70, 0:100; vegetable-waste compost sieved to 2 mm; two butterhead lettuce cultivars; 19 days in a phytotron (24/18 °C).
- Fresh yield: best at **30:70** — 61.2 g/plant (green) and 68.0 g/plant (red); pure simulant ~20–21% lower; 70:30 intermediate and judged "a more realistic scenario" because compost would be scarce.
- Problems in pure simulant: alkaline pH, no biological fertility, salt stress, N, P, S deficiency, K shortage with Na substituting; plant Na 1.7–12.8 g/kg dry weight.
- (A search engine summary misattributed this paper to *Frontiers in Plant Science*; the journal is *Plants*.)
- Earlier compost precedent: JSC Mars-1 with municipal leaf compost at 1:0, 3:1, 1:1, 1:3, 0:1 (v:v) for Swiss chard; compost improved physical properties but nutrients were still insufficient (Gilrain et al. 1999, via Duri 2022). **SOURCED (secondary).**

#### Q5d. Florida Institute of Technology: Mars simulants and perchlorate

- Eichler et al. 2021 (*Icarus*) tested JSC-Mars-1A, Mars Mojave Simulant (MMS) and Mars Global Simulant (MGS-1) with lettuce and *Arabidopsis*: growth on JSC-Mars-1A and MMS with nutrients, "no growth on MGS-1" (the most mineralogically accurate simulant), toxic "despite various strategies to make it viable"; high alkalinity suspected. Simulants "enriched with calcium perchlorate (2% w/v)" "were unable to sustain plant growth, even with nutrient supply." All simulants lacked nitrogen. (Duri 2022 review; Florida Tech news release https://news.fit.edu/?p=69273, read 2026-10-25.) **SOURCED (secondary).**
- Perchlorate on Mars: "concentrations of 0.5–1%" (Duri 2022). **SOURCED (secondary).** Plants grown in regolith with > 1 wt% perchlorate would be stunted or halted and would accumulate perchlorate. **UNVERIFIED** (search summary).
- Perchlorate removal by washing: a student study compared deionized water, HCl, acetic acid and EDTA for removing 1 wt% perchlorate and sulfates from MGS-1, MGS-1S and JEZ-1 simulants (Roger Williams University symposium abstract, https://docs.rwu.edu/studentresearchsymposium/5, read 2026-10-25) — no removal percentages given. Water-to-regolith ratio and number of rinses needed: **NOT FOUND.** Other routes named in the Duri review: water rinses, phytoremediation, volatilization, perchlorate-reducing bacteria. **SOURCED (list only).**

#### Q5e. Texas A&M with UT Austin / Brown: lunar simulant + vermicompost + mycorrhizae (chickpea)

- Lunar regolith simulant at 25, 50, 75 and 100% mixed with vermicompost; seeds coated with arbuscular mycorrhizal fungi; "100% seed growth by day 16"; all plants in simulant showed chlorophyll deficiency, improving by week 7 attributed to AMF; "the first documented chickpea yield in an LRS mixture"; 120-day runs (Atkin et al., bioRxiv preprint 10.1101/2024.01.18.576311, 18 January 2024; summary at https://www.universetoday.com/articles/chickpeas-grown-in-lunar-regolith-are-stressed-but-reach-maturity, read 2026-10-25). **SOURCED (secondary; preprint returned HTTP 429).**
- Peer-reviewed version reported in *Scientific Reports*, 5 March 2026, growing chickpea to seed in mixes with up to 75% simulant. **UNVERIFIED** (search summary of trade-press items).
- Texas A&M Mars work (JSC-Mars-1 + brewing by-products + microbes, barley): announced project, no results (AgriLife Today, 20 Nov 2025). **UNVERIFIED** (search summary).

#### Q5f. Other

- Mars-analog desert soil, La Joya, Peru: 65 potato genotypes, about 40% survived and yielded 0.3–5.2 g tuber per plant; soil EC 19.3–52.6 dS/m (Ramírez et al. 2019, via Duri 2022). **SOURCED (secondary).**
- Lunar anorthosite analogue + bacterial consortium on marigold seeds (Kozyrovska et al. 2006); sweet potato in lunar and Martian simulants, anchorage only (Aglan et al. 1998; Mortley et al. 2000) (via Duri 2022). **SOURCED (secondary).**

#### Q5g. What made simulant arable (as reported, not recommended)

Across these studies: (1) added organic matter — compost, grass clippings or vermicompost — at 30–75% of volume in the successful trials, which lowered pH and added CEC, structure and water holding; (2) a nitrogen source (nutrient solution, compost, legumes with inoculant); (3) microbes (AMF, bacterial consortia) for nutrient release and stress; (4) removing perchlorate before planting on Mars material; (5) for the Moon, less space-weathered (immature) regolith was less stressful. Pure simulants supported plants only briefly or poorly. **SOURCED** as a synthesis of Q5a–Q5f and the Duri 2022 conclusion that "pure regolith simulants may be suitable media for plant growth (at least for limited periods)."
- Caution: simulants are not regolith. MGS-1, the most accurate Mars simulant, was the one that failed, and real Apollo soil was more stressful than JSC-1A. **SOURCED (Q5b, Q5d).**

### Q6. Time and labor

#### Q6a. Hand labor (Sahel water-harvesting pits)

- Zai: ~300 h/ha to dig (Barro et al. 2005), or 450 h/ha to dig + 250 h/ha to fertilize (Kaboré et al. 1994; Maatman et al. 1997); 20,000–25,000 pits/ha; manure 4–18 t/ha must be gathered, months ahead if composted (ECHO TN #78, Q1e). **SOURCED (secondary).** COMPUTED: 300–700 h/ha ≈ 38–88 eight-hour person-days/ha.
- Half-moons (demi-lunes), Niger: "The Nigerien Ministry of Environment recommends building 250–300 demi-lunes per hectare of degraded land. Each demi-lune costs about US$80 to construct, primarily due to labor costs, but once constructed, they do not require maintenance until three years later." In the randomized evaluation, intervention households used "an additional fifteen days of one family member's labor" (versus two days in comparison households); output rose 80–90 kg (mainly sesame and sorghum), revenue +US$34–37 (10–13%) in years 1 and 3, net profit ≈ +US$3 in year one (Aker and Jack, J-PAL evaluation, 2017–2019, surveys to 2021; https://www.povertyactionlab.org/evaluation/are-rainwater-harvesting-techniques-profitable-small-scale-farmers-adoption-and-impact, read 2026-10-25). **SOURCED.**
  - COMPUTED: 250–300 × US$80 = US$20,000–24,000/ha — implausibly high against the reported revenue gains; the "per demi-lune" wording may be an error in the summary page. **Flag: per-unit cost UNVERIFIED pending the working paper.** Hectares per household were not stated, so person-days per hectare cannot be derived.

#### Q6b. Machine hours (mine reclamation, U.S. OSMRE bonding handbook)

OSMRE Directive 1005, *Handbook for Calculation of Reclamation Bond Amounts*, Appendix B2 worked example (area mine) (https://www.osmre.gov/sites/default/files/pdfs/directive1005_AppendixA.pdf, read 2026-10-25). All **SOURCED** (illustrative example, Caterpillar Performance Handbook ed. 46 productivity):
- Topsoil replacement, 6 in over 40.5 acres (32,670 loose yd3, 1,000 ft haul): two CAT 637K push-loaded scrapers (29 yd3 average) at 667.5 loose yd3/h → **48.9 scraper-hours**, plus **25 pusher-dozer (D9R) hours**. Prime farmland in the same example receives 48 in of topsoil plus subsoil (6 in topsoil + 3.5 ft subsoil).
- Ripping regraded spoil (sandstone and shale) 2 ft deep before topsoiling, D7R with 3-shank ripper: 1,330 ft passes at 88 ft/min, 3.25 passes/h, 9.75 ft ripping width.
- COMPUTED per hectare: 40.5 ac = 16.39 ha → topsoil 15 cm: 48.9/16.39 ≈ **3.0 scraper-h/ha + 1.5 dozer-h/ha**; ripping: 3.25 × 9.75 ft × 1,330 ft ≈ 42,100 ft2/h ≈ 0.97 ac/h → **≈ 2.5 dozer-h/ha**. Per tonne: 32,670 LCY ≈ 24,980 m3 loose; at an assumed 1.3 t/m3 loose ≈ 32,500 t → ≈ 0.0015 scraper-h per tonne (≈ 5.4 s/t). Assumptions: example haul distance and grade; loose density assumed, not given.
- Note: the handbook's printed formula reads "acres / 43,560 acres/ft2"; the arithmetic is acres × 43,560 ft2/acre. Typo in source; volumes are consistent with multiplication.
- Cost benchmarks (Arkansas DEQ open-cut mine bond form, https://www.adeq.state.ar.us/mining/pdfs/open-cut-individual/open-cut-bond-determination-form.pdf, read 2026-10-25; date not on form): backfill $1.25/yd3 (< 500 ft) or $1.90/yd3 (> 500 ft); topsoil replacement (3 in) $4,000/acre; topsoil spreading $1,300/acre or $1.50/yd3; revegetation $1,450/acre; +20% engineering/administration; +2.5% mobilization. **SOURCED.** COMPUTED: $4,000 + $1,300 + $1,450 = $6,750/acre ≈ $16,700/ha before overheads (× 2.471).
- Western U.S. coal reclamation $860–7,200/acre (1976 data, U.S. Bureau of Mines IC 8737). **UNVERIFIED** (search summary).

#### Q6c. Composting labor (on-farm windrows, Wisconsin)

Butler, Connolly and Elefson (UW–River Falls), CIAS Research Brief #20, 1996 (https://cias.wisc.edu/crop-soil/windrow-composting-systems-can-be-feasable-cost-effective/, read 2026-10-25). All **SOURCED**: forming windrows ~6.8 min per ton of manure (+20 min setup); first turning 0.2 min/t (bulldozer), 0.8 min/t (compost turner), 1.5 min/t (front-end loader); later turnings about half that; 2 turnings with a turner, 4 with dozer or loader; reloading for spreading ~2.2 min/t (+20 min setup).
- COMPUTED, per tonne with a turner: 6.8 + 0.8 + 0.4 + 2.2 ≈ **10.2 machine-minutes per tonne** of manure (≈ 0.17 h/t), excluding setup and field spreading.

#### Q6d. Other labor and cost figures already recorded

- Iceland lupine: 30,000 ISK/ha (US$217) one-off establishment, machine-seeded, no maintenance (Q1a). **SOURCED.**
- Subsurface drainage, India: ₹65,000–1,25,000/ha (2015 prices), labor and machinery 20–25% of cost, payback 3–5 years (Q3b). **SOURCED.**
- Vermicomposting bed area: ≈ 833 m2·days per tonne of feed (Q4b, COMPUTED).
- Biosolids spread on Arizona tailings with a road grader and front-end loader; hours not reported (Q1c). Pennsylvania sludge–fly ash thrown by aerial spreader truck (50–70 m throw); hours not reported (Q1j).
- Person-hours or machine-hours per tonne of finished constructed soil (Technosol) production: **NOT FOUND.**

### Q7. Failure and degradation

#### Q7a. Erosion of new, bare constructed surfaces

So et al. 2018, "MINErosion 3: using measurements on a tilting flume–rainfall simulator facility to predict erosion rates from post-mining landscapes in Central Queensland, Australia," *PLOS ONE* (https://pmc.ncbi.nlm.nih.gov/articles/PMC5874007/, read 2026-10-25). All **SOURCED**:
- Measured single-storm losses on post-mining soil and spoil plots: 0.1–73.9 t/ha per event.
- Predicted annual erosion, bare, 10% slope: 131 t/ha/yr at 10 m slope length rising to 292 t/ha/yr at 50 m; at 20 m length, bare 185 t/ha/yr falls to 27 t/ha/yr under 40% stoloniferous grass cover; "40% of vegetation cover is required to provide the maximum erosion reduction."
- Target: erosion no greater than natural rates of surrounding land, ≈ 10.5 t/ha/yr in that reference.
- COMPUTED meaning: at a bulk density of 1.5 t/m3, 185 t/ha/yr = 185 / (1.5 × 10,000) m ≈ **12 mm of surface lost per year**; a 15 cm topsoil cap (Q6b) would be gone in ~12 years if left bare.
- Other bare-spoil figures (21 and 17 t/ha on fallow and crusted spoil; 4.9–14 t/ha on sodic spoils; 7.5 t/ha at 12% slope). **UNVERIFIED** (search summaries; sources not opened).
- Wind: Iceland's reclamation exists because of wind erosion; fertilizer-and-grass plots stalled after 8 years partly from "disruption by aeolian processes," while lupine plots kept gaining (Q1a). **SOURCED (abstract summary).** Constructed Technosols carry erosion, runoff and compaction risk "in the early stages" before structure forms (Deeb et al. 2020; Q4f). **SOURCED.**

#### Q7b. Compaction

- Ohio graded mine soils: "high" compaction, "very low" aeration with possible anaerobic subsoil below 30 cm, low infiltration, vegetation set back for the first 5–15 years (Akala and Lal 2001; Q1i). **SOURCED.**
- Indiana reclaimed mine: graded soil bulk density 1.74 g/cm3 versus loosely dumped 1.54 g/cm3, with root impairment on the graded soil. **UNVERIFIED** (search summary of an ASA/CSSA 2011 meeting abstract, scisoc.confex.com Paper66987; not opened).
- Forest Reclamation Advisory No. 3, *Low compaction grading to enhance reforestation success on coal surface mines* (Sweigard, Burger, Zipper, Skousen, Barton and Angel, July 2007; https://www.osmre.gov/sites/default/files/inline-files/FRA_No.3.pdf, read 2026-10-25). All **SOURCED**: dump surface material over the (compacted) subsurface to **4–6 ft** and grade lightly — "at least four feet deep," leveled with "one or, at most, two passes," preferably a single pass of a low-ground-pressure dozer; smooth multi-pass grading compacts the soil, cuts water and air storage and root growth, and is not required by SMCRA; reducing compaction "increased survival and growth of hardwood species and reduced soil erosion" (citing 1992 work).
- Compaction from repeated machine passes on a constructed soil therefore trades directly against the labor figures in Q6b (more passes = smoother = worse soil).

#### Q7c. Organic-matter loss and plateau (how fast added carbon goes away)

All **SOURCED** from earlier sections:
- One 15 cm dose of composted horse manure on loamy sand: OM 3.6% → 9.1% in a year, back to 4.5% after 9 years (≈ 84% of the gain lost within ~6 years of the peak; COMPUTED) (Bickelhaupt 1987; Q2e).
- Iceland fertilizer-plus-grass plots: soil C rose for 8 years, then flat for 5 once fertilizer stopped; only nitrogen-fixing lupine kept accumulating (Tanner et al. 2015; Q1a — abstract via summary, **UNVERIFIED** detail).
- Egyptian desert under continuous compost: 2.7–3.8 t C/ha/yr for 5 years, then ~0.5 t C/ha/yr; logarithmic; still rising at 30 years only because compost kept going on (Q1d).
- Tengger dunes: 57 years of shrubs raised SOC from 0.33 to 5.08 g/kg, but the mineral-protected share fell from 85% to 42%, i.e., the new carbon is labile and "vulnerable to disturbance" (Q1f).
- Birch afforestation on degraded Icelandic soil: SOC lower than barren reference for the first ~25 years (Hunziker et al. 2019; Q1a).
- Constructed Technosols: carbon released in the first months, then stabilized over ~3 years; "high mineralization of organic matter may occur in the early stages … especially when a high quantity of organic matter is used" (Deeb et al. 2020; Q4f).
- Nursery manure also raised pH 5.7 → 7.3 for 12 years — an amendment side effect that outlasted the organic matter (Q2e). Sulfur acidification decayed back toward control within ~20 months (Q2j).

#### Q7d. Salinization and alkalization

- Global extent: "more than 833 million hectares of salt-affected soils … (8.7% of the planet)"; "20 to 50 percent of irrigated soils in all continents are too salty" (FAO Global Map of Salt-Affected Soils launch, October 2021, as reported in FAO/UNCCD news items). **UNVERIFIED** (search summary; FAO newsroom page not opened). Annual loss rate of irrigated land to salinity: **NOT FOUND.**
- Mechanism seen in the sourced cases: irrigation without drainage raises the water table into the root zone (India: water table within 1.5–2 m; Q3b); irrigation water carbonates raised reclaimed desert pH 7.9 → 8.5 (SEKEM; Q1d); saline irrigation water sets a floor on how low soil EC can go (SEKEM; Q1d). **SOURCED.**
- Leaching needs a drain: in waterlogged land, drained fields kept the water table at 1.07 m vs 0.63 m undrained (Q3b). **SOURCED.**

#### Q7e. Contamination from waste-derived amendments

- **Metals:** EPA Part 503 cumulative loading limits (Q2b); BC copper tailings with 250 Mg/ha biosolids exceeded the Zn guideline (214 mg/kg) and the substrate itself carried Mo at levels putting forage at 112 mg/kg (Q1b); Technosol review: regular organic additions "may lead to the accumulation of heavy metals over time" (Q4f). Basalt at 50 t/ha/yr for 4 years did not raise grain or soil-exchangeable trace metals (Q2d). **SOURCED.**
- **PFAS ("forever chemicals") from sewage sludge, Maine, USA:** L.D. 1911 (passed April 2022) "completely prohibits the land application of biosolids and the sale of compost or other agricultural products and materials containing sludge and septage" (NACWA news, 20 April 2022, https://www.nacwa.org/news-publications/news-detail/2022/04/20/maine-legislature-passes-bill-prohibiting-land-application-of-biosolids-governor-expected-to-sign, read 2026-10-25); earlier screening levels 2.5 ppb PFOA and 5.2 ppb PFOS. **SOURCED.** Maine Department of Agriculture (DACF) PFAS response slides, 2026 (https://www1.maine.gov/dacf/ag/pfas/docs/pfas-response-ats-2026.pdf, read 2026-10-25): as of 31 Dec 2025, **111 farms "considered impacted by PFAS"**; 64 exceeded DACF's most conservative soil screening level (6.4 ppb PFOS); 25 exceeded the interim drinking-water standard; 22 exceeded both; investigation tiers by historic sludge volume — Tier 1 (> 10,000 yd3 sludge) 60 sites, 46 sites in the next tier, > 400 Tier 3 sites (< 5,000 yd3) about half done, > 500 unconfirmed; chicken-egg action level 4.7 ppb PFOS; "most farms have been able to" continue with management changes. **SOURCED.**
- **Microplastics:** sewage-sludge compost raises soil microplastics; recommended only at low ratios and tested first (Deeb et al. 2020 author response; Q4f). **SOURCED.**
- **Radium:** phosphogypsum restricted in U.S. agriculture (Q3c). **SOURCED.**
- **Lunar/Martian:** perchlorate at 0.5–1% on Mars; 2% calcium perchlorate in simulant stopped growth even with nutrients; mature lunar regolith induced metal- and salt-type stress genes (Q5). **SOURCED (partly secondary).**

#### Q7f. Pathogens in waste reuse

Mara (author-produced chapter on the WHO 2006 *Guidelines for the safe use of wastewater, excreta and greywater*, in *Efficient Management of Wastewater*; https://eprints.whiterose.ac.uk/5383/2/mara_who.pdf, read 2026-10-25). All **SOURCED**:
- Health target: tolerable additional disease burden ≤ 10−6 DALY loss per person per year; design rotavirus infection risk 10−3 per person per year.
- Unrestricted irrigation (e.g., lettuce): total pathogen reduction of **6–7 log units** — a 4-log reduction by treatment (from 10^7–10^8 to 10^3–10^4 *E. coli* per 100 mL; ≤ 10^4 *E. coli*/100 mL) plus 2–3 log die-off between irrigation and eating (~2 days in warm climates). A 4-log treatment also protects field workers.
- Helminths: wastewater for agriculture ≤ 1 human intestinal nematode egg per liter (not required for drip irrigation of high-growing crops; children under 15 need extra measures such as deworming). Excreta: ≤ 1 egg per g total solids. **SOURCED (Mara text for wastewater; the excreta figure is UNVERIFIED — search summary).**
- Biosolids: Class A/Class B pathogen limits and composting time-temperature rules (Q2b); black soldier fly frass may retain pathogens and needs post-treatment (Q4c). **SOURCED.**

#### Q7g. Biological failures specific to constructed or reclaimed soils

All **SOURCED** from earlier sections: nematodes cut tomato, eggplant and bean yields on 4- and 5-year reclaimed Egyptian desert fields (Q1d); sown *Lolium* vanished from 2013 Gunnarsholt plots (Q1a); oats and barley on Arizona tailings went chlorotic and died, possibly from aluminum (Q1c); highest tree mortality in excavated subsoil + green-waste compost Technosol (Q4f); biocrust inocula showed no gain after 5 months without habitat amelioration (Q2f); mosses and lichens failed to establish from inoculum (Q2f); the 40 t/ha glacial rock flour + NPK treatment *reduced* yield (Q2d); invasive lupine displaced native vegetation and was abandoned by the agency (Q1a).

#### Q7h. How fast constructed soils degrade — summary of what was and was not found

- Found: bare constructed surfaces can lose ~10^2 t/ha/yr to water erosion until ~40% plant cover; added organic matter decays to near baseline within ~5–10 years without new inputs (one sandy-soil case); pH amendments drift back within 1–2 years (sulfur) or persist > 10 years (limed manure).
- **NOT FOUND:** a long-term (> 10 yr) monitored decline curve for a deliberately engineered Technosol; a measured annual salinization rate for newly irrigated reclaimed land.

---

## 3. NOT FOUND / open threads

Each item: what is missing — where looked — where it died.

**NOT FOUND**
1. Fertilizer rates for the nine Icelandic restoration treatments (Arnalds et al. 2013) and Tanner et al. 2015 full text — IRIS abstract, UNU (503), DOAJ (403), Wiley/Hindawi (HTML wall). Died at sources.
2. Lupine soil C/N accumulation rates confirmed from the original (*Fjölrit RALA* 2001) — timarit.is 403. Died at source.
3. Kubuqi Desert soil-building rates (amendments, SOC by age) — one Frontiers paper opened (remote sensing only). Died at query/sources; needs Chinese-language literature.
4. Dutch polder ripening timeline (reed seeding rate, years per stage, drain spacing, first crops) — 5 English sources opened, none quantitative; Rijkswaterstaat Dutch archive items not opened. Open thread: search in Dutch ("rijping", "riet zaaien", "IJsselmeerpolders ontginning").
5. Loess Plateau per-hectare SOC rate and check-dam fill time and labor — USGS abstract, DESIRE page. Died at sources.
6. Negev and Egypt reclamation costs and labor — not in Bruins 1986 or the SEKEM report.
7. Biosolids biomass-by-rate on BC copper tailings — abstract only (full text not opened).
8. Biochar: application rate vs effect size, char yield % and surplus energy from a primary source — Jeffery 2017 abstract only; Woolf 2014 has energy penalty but not char yield; char-yield and MJ figures only in summaries.
9. Swoboda et al. 2022 rock-dust trial rates and effect sizes — bonndoc bot wall.
10. Glacial rock flour Denmark/Ghana trial numbers — Springer login redirect.
11. Salomon et al. 2022: share of commercial AMF products that failed to colonize — ZORA 403, Agroscope citation only.
12. Biocrust inoculation rates (g/m2) and costs.
13. Humic substance and zeolite application rates with effect sizes (no meta-analysis found for zeolite).
14. Peat properties and peat-free substitution ratios; reliable coir EC (compiled EC units implausible).
15. Anaerobic digestate application rates (m3/ha) from an opened primary source.
16. Wamelink 2019 grass:simulant ratio and per-tray yields — publisher 405, WUR PDF empty, DOAJ 403.
17. Perchlorate removal efficiency by washing (water volume, rinses, % removed) — RWU abstract had no numbers.
18. Time for crushed fresh rock (basalt) + organics to become a working medium — no constructed-soil study found on fresh rock fines without clay.
19. Person- or machine-hours per tonne of finished constructed soil (Technosol production).
20. Leaching-water volume required after gypsum on sodic soil (sourced figure).
21. Annual rate of irrigated-land loss to salinization; FAO 2021 global figures only from summaries.
22. Long-term (> 10 yr) monitored degradation curve for an engineered Technosol.
23. Half-moon person-days per hectare (J-PAL gives days per household, not per ha); J-PAL's "US$80 per demi-lune" looks inconsistent with its revenue figures — check Aker & Jack working paper.

**UNVERIFIED items carried in the text (seen only in summaries; verify before use):** Tunguheiði 4 × 200 kg fertilizer/ha; lupine 1,300 kg C/ha/yr; 0.52 Mg C/ha/yr coal-mine TOC; Loess 6,000–15,000 kg/ha check-dam yields; Avdat 20:1 ratio; straw-checkerboard 1–10 yr data; MSU sulfur table; zeolite rates; hairy vetch N; digestate N fractions; BSF brewery/poultry conversion figures; Indiana bulk density 1.74 vs 1.54; bare-spoil 7.5–21 t/ha figures; FAO 833 Mha / 20–50% irrigated salt-affected; passive composting durations; Hoffman leaching k-values; 2026 *Scientific Reports* chickpea paper details; excreta ≤ 1 egg/g TS.

**Errors caught in sources or summaries (kept as warnings):** half-moon yield range misreported by a search summary (900 vs 600 kg/ha); WebFetch paraphrase dropped organic C from the Tengger 20–40% list; Duri et al. 2020 misattributed to *Frontiers in Plant Science*; "1.7 t gypsum" rule attributed to the wrong article by a summary; Akala and Lal's stated C rates do not follow from their own stocks; OSMRE handbook prints "acres / 43,560" for a multiplication.

---

## 4. Full search log

Format: `query` → result (FOUND / PARTIAL / DEAD) ; where it died (query or sources).

**Q1 (2026-10-25)**
1. `copper mine tailings reclamation biosolids application rate Mg/ha vegetation establishment study` → FOUND (Gardner et al. 2012 CJSS; ASRS proceedings PDFs).
2. `Iceland Soil Conservation Service land reclamation fertilizer rate kg/ha lupine Nootka soil carbon accumulation` → PARTIAL (WOCAT sheet; Tunguheiði news page). No C rates.
3. `zai pits half-moons Sahel manure rate t/ha sorghum yield increase study` → FOUND (IRD half-moon trial; Fatondji zai; Kenya zai).
4. Fetch qcat.wocat.net permalink 5784 → redirect to wocat.net database → page shell only, DEAD at source. Fetched the WOCAT PDF instead → binary; converted locally with pdftotext → FOUND, read in full.
5. Fetch island.is Tunguheiði page → HTTP 503, DEAD at source (summary-only figure kept as UNVERIFIED).
6. `Iceland revegetation soil carbon sequestration rate g C m-2 yr-1 fertilizer grass seeding lupine Arnalds Aradottir` → FOUND (Arnalds 2013 Geoderma; Tanner 2015; Hunziker 2018 preprint; Gessesse thesis).
7. `Nootka lupine Iceland soil organic carbon nitrogen accumulation chronosequence sandy soil` → PARTIAL (Fjölrit RALA 2001 p.7 via timarit.is → HTTP 403, DEAD at source).
8. Fetch DOAJ SOIL 2019 article → 403, DEAD at source; fetched Copernicus preprint PDF → converted, FOUND.
9. Fetch grocentre gessesse_ta.pdf → exceeded 10 MB fetch limit, DEAD at tool. Not retried.
10. Fetch collections.unu.edu UNU:6378 → 503, DEAD at source; landsbokasafn IRIS record → FOUND abstract.
11. `"Carbon accumulation in Icelandic desert Andosols during early stages of restoration" Arnalds Geoderma fertilizer` → FOUND (record; fertilizer rates not in abstract).
12. `Applied and Environmental Soil Science 2015 Iceland restoration lupine soil carbon CO2 flux fertilizer grass plots aeolian` → FOUND (Tanner et al. 2015 identification; Andryei 2015 UNU report).
13. `Tanner Nivison Arnalds Svavarsdottir 2015 "Soil Carbon Accumulation and CO2 Flux in Experimental Restoration Plots" hindawi` → DOI found; curl Wiley PDF and Hindawi PDF → HTML wall, DEAD at source.
14. Fetch andryei2015.pdf → converted locally, FOUND (Table 1 treatment quantities).
15. Fetch onlinelibrary.wiley.com/doi/10.1155/2015/205846 → 403, DEAD at source (Tanner 2015 full text unreachable by three routes).
16. Fetch ASRS 0085-Rogers.pdf → converted, FOUND, read in full.
17. `Egypt new lands desert sandy soil reclamation organic matter compost rate ton per feddan years to productivity study` → PARTIAL (EKB journal PDFs not opened; SEKEM sponsored page opened → no numbers).
18. `Loess Plateau Grain for Green soil organic carbon accumulation rate terraces check dams yield increase study` → FOUND (USGS/Chang et al.; PMC papers) — see Q1 Loess section.
19. `Kubuqi desert sand stabilization straw checkerboard soil organic carbon development years study` → PARTIAL; opened Frontiers 2022 Kubuqi paper → wind-erosion remote sensing only, no soil numbers (DEAD at source for this purpose).
20. `Shapotou Tengger revegetation chronosequence topsoil thickness organic carbon biological soil crust 50 years Li Xinrong` → FOUND (bg-2017-139 etc.).
21. `reclaimed desert soils Egypt cultivation age chronosequence soil organic carbon increase years of cultivation sandy` → FOUND (Luske & van der Kamp 2009 orgprints PDF — downloaded with curl, read in full).
22. curl IRD half-moon PDF (Zougmoré et al.) → FOUND, read in full. Search summary had misstated its yield range (900 vs 600 kg/ha) — corrected from full text.
23. curl ECHO TN #78 zai PDF → FOUND, read.
24. curl bg-2017-139 Shapotou preprint → FOUND, site description and discussion read.
25. `Li 2007 "Recovery of topsoil physicochemical properties in revegetated sites in the sand-burial ecosystems of the Tengger Desert" topsoil depth cm organic carbon` → FOUND (CERN abstract page). First WebFetch paraphrase omitted organic C from the 20–40% list; re-fetched asking for verbatim text, which includes it. Paraphrase-error caught.
26. AGU FM15 abstract → redirect to m-anage.com → FOUND.
27. USGS record for Chang et al. 2011 → FOUND (abstract).
28. `Dutch polder reclamation newly drained marine sediment ripening years before arable farming Flevoland reed sowing soil ripening` → PARTIAL (popular sources only).
29. curl WUR NJAS article 17733 → opened; Herweijer 1957 policy lecture, no ripening data — DEAD at source for this purpose.
30. `IJsselmeerpolders soil ripening reed sown from aircraft years state exploitation before farmers allocated Flevoland Oostelijk Flevoland 1957` → PARTIAL (Rijkswaterstaat archive titles; not opened). curl edepot.wur.nl/251462 → Wiggers soil survey, no timeline — DEAD at source.
31. Wieringermeer page → FOUND (area, dates, qualitative).
32. `Zuiderzee polder reclamation reed Phragmites sowing aerial seeding first years state farm period before allocation soil ripening Noordoostpolder history` → PARTIAL; nationaalparknieuwland page → no soil content (DEAD at source); blog.uvm.edu → 404 (DEAD at source).
33. `coal mine spoil reclamation soil organic carbon accumulation rate years chronosequence topsoil replacement Mg C ha yr` → FOUND (Akala & Lal; AGRIS record not opened).
34. curl Akala P030 PDF → FOUND, read in full. Internal inconsistency in stated rates found and recorded.
35. `fly ash lagoon revegetation reclamation boron toxicity amendment sewage sludge topsoil cover depth study plant establishment` → FOUND (Jusaitis & Pillman 1997 AGRIS abstract opened).
36. `glacier forefield chronosequence soil development organic carbon accumulation rate years since deglaciation nitrogen` → PARTIAL; skemman.is → 403 (DEAD at source); PMC review → FOUND; EGU2019-2084 PDF → no numbers.
37. `Vilmundardóttir 2015 Skaftafellsjökull moraine soil organic carbon accretion 9.1 g m-2 yr-1 Catena` → FOUND (2017 Geografiska Annaler abstract on opinvisindi; 2015 paper record only).
38. `Loess Plateau check dam farmland crop yield compared slope farmland times higher sediment silted land study` → FOUND (DESIRE page opened).
39. `Negev runoff agriculture Avdat Evenari catchment to cultivated area ratio loess yield liman study` → FOUND; curl edepot.wur.nl/201460 (Bruins 1986 thesis, 231 pp.) → relevant chapters read.
40. curl ASRS Sopper 0413, 0448, 0741 → FOUND; 0741 read for methods and Table 8.
*Q1 closed 2026-10-25. Copper tailings, Iceland, Egypt, Sahel, Tengger, Loess, Negev, coal spoil, fly ash and glacial till have sourced recipes; Kubuqi and the Dutch polders are thin (see Section 3).*

**Q2 (2026-10-25)**
41. eCFR 503.13 → redirect to unblock.federalregister.gov bot wall, DEAD at source; Cornell LII 503.13, 503.32, Appendix B → FOUND.
42. `biochar meta-analysis crop yield response tropical temperate soils Jeffery 2017 Environmental Research Letters percent` → FOUND (abstract).
43. `compost maturity index CCQC standard C:N ratio respiration rate mg CO2-C/g OM/day ammonium nitrate ratio germination` → PARTIAL; OSU fact sheet → 403 and PDF curl → HTML wall, DEAD at source.
44. `CCQC "Compost Maturity Index" 2001 California Compost Quality Council pdf Group A Group B ammonium nitrate C:N 25` → FOUND; curl woodsend.com PDF → read.
45. `compost application rate cubic yards per 1000 square feet inches incorporated depth soil amendment extension tons per acre conversion` → PARTIAL (utility guidance, not opened).
46. `Swoboda 2022 review "silicate rock powders" agricultural usage application rates t/ha yield effects weathering` → abstract only; bonndoc → bot wall, DEAD at source.
47. `Beerling 2024 PNAS enhanced weathering basalt Corn Belt 50 t/ha yield increase maize soybean four years` → FOUND (White Rose abstract).
48. `Kelland 2020 Global Change Biology basalt 10 kg m-2 sorghum yield increase 21% weathering rate clay loam mesocosm` → FOUND (White Rose abstract).
49. `glacial rock flour Greenland soil amendment field trial barley yield application rate t/ha Gunnarsen 2023` → PARTIAL; Springer → login redirect (DEAD at source); KU Globe page → no numbers; AGRIS Sukstorf 2020 → FOUND.
50. `basalt rock dust field trial fraction dissolved per year percent weathered first year enhanced weathering measured dissolution rate field` → FOUND (Buckingham 2022 ORA abstract).
51. `slow pyrolysis biochar yield percent feedstock mass energy balance net energy Gaunt Lehmann 2008 Environmental Science Technology` → PARTIAL (paper identified: ES&T 42: 4152; only a summary of its GHG conclusion; char yield and energy numbers NOT read).
52. `meta-analysis field inoculation arbuscular mycorrhizal fungi crop yield response percent publication bias 2022 Salomon` → FOUND (Wu et al. 2022 PeerJ, read via PMC).
53. `biocrust inoculation restoration cyanobacteria cultivated dryland field establishment rate months Antoninka Faist review` → FOUND (three abstracts opened).
54. `Salomon 2022 "Global evaluation of commercial arbuscular mycorrhizal inoculants" viability propagules percent products failed` → PARTIAL; ZORA → 403, Agroscope → citation only. DEAD at source.
55. `elemental sulfur needed to lower soil pH table lb per 1000 sq ft sandy loam clay from pH 8.0 to 6.5 extension` → PARTIAL; MSU news page → empty, MSU PDF curl → HTML; Bickelhaupt 1987 PDF → FOUND, read in full.
56. `humic substances meta-analysis plant growth response Rose 2014 Advances in Agronomy shoot dry weight percent increase` → FOUND (abstract; Adelaide PDF curl → HTML wall).
57. `zeolite soil amendment meta-analysis crop yield nitrogen use efficiency application rate t/ha clinoptilolite` → PARTIAL (single studies, not opened).
58. `coconut coir pith substitute peat growing media properties pH EC potassium sodium water holding capacity air-filled porosity comparison study` → PARTIAL; CSIRO EA02128 → redirect then 404, DEAD at source.
59. `legume cover crop nitrogen fixation kg N/ha hairy vetch crimson clover biomass extension SARE Managing Cover Crops Profitably` → FOUND (SARE crimson clover page).
60. `rhizobia inoculation soybean yield response fields without prior soybean history meta-analysis new land percent increase` → FOUND (Thilakarathna & Raizada 2017 abstract).
61. `coir dust chemical properties high potassium sodium chloride electrical conductivity washing buffering calcium nitrate before use Abad 2002 Bioresource Technology Spain` → FOUND (MN Stormwater table; EC units suspect).
62. `biochar production slow pyrolysis char yield 25-35% dry feedstock exothermic self-sustaining energy surplus MJ per kg review` → PARTIAL (summaries only); curl Woolf 2014 SI and main paper from Cornell → FOUND energy-penalty figures; char-yield % and MJ surplus not in it.
*Q2 closed 2026-10-25.*

**Q3 (2026-10-25)**
63. fao.org/3/t0234e/T0234E03.htm → 301 to fao.org/4/ → FOUND (FAO 29 ch. 2).
64. `reclamation of saline soils depth of leaching water per unit soil depth Dw/Ds continuous ponding intermittent 70% salt removal Hoffman FAO` → PARTIAL; UC ANR salinity page → 404, DEAD at source.
65. fao.org/4/t0234e/T0234E04.htm → FOUND (gypsum rates, Table 12).
66. `gypsum requirement calculation exchangeable sodium cmol/kg tonnes per hectare 15 cm depth formula sodic soil reclamation 1.72 conversion` → FOUND; Crops & Soils article → FOUND (no 1.7 rule there; search summary had conflated two sources); UA FSA2199 PDF → converted, FOUND.
67. `subsurface drainage saline soil reclamation drain depth spacing meters soil salinity ECe decrease years crop yield increase Egypt Pakistan India study` → FOUND; curl CSSRI dr16.pdf → read in full.
*Q3 closed 2026-10-25.*

**Q4 (2026-10-25)**
68. `vermicomposting processing rate Eisenia fetida feed consumption kg per kg worm biomass per day stocking density kg/m2 Edwards` → PARTIAL; USCC Sherman PDF → curl failed (no file), DEAD at source.
69. `black soldier fly larvae bioconversion waste reduction percent frass yield per kg substrate larval period days Diener` → FOUND (PMC review read).
70. `constructed Technosol excavated subsoil green waste compost mixture ratio volume field experiment Séré 2008 soil construction` → FOUND; soil-2019-85-AC1 PDF read; Temis PDF → HTML (DEAD at source); Deeb et al. 2020 SOIL article read.
71. `Ndegwa Thompson Das 2000 stocking density feeding rate vermicomposting biosolids 0.75 kg-feed/kg-worm/day 1.60 kg-worms/m2` → FOUND; PDF via lehighcountyauthority.org read.
72. `On-Farm Composting Handbook NRAES-54 Rynk composting time windrow active composting weeks curing period passive aerated static pile typical durations table` → PARTIAL; OSU PDF → HTML (DEAD); BC factsheet → socket hang-up (DEAD); FAO y5104e → FOUND.
73. `bokashi fermentation food waste field study soil application compared compost nutrient days fermentation duration peer-reviewed` → FOUND (SARE GNE15-098 report).
74. `anaerobic digestate fertilizer value nitrogen ammonium fraction application rate m3/ha crop yield compared mineral fertilizer review solid digestate organic matter` → PARTIAL (summaries only; not opened).
*Q4 closed 2026-10-25.*

**Q5 (2026-10-25)**
75. PLOS ONE Wamelink 2014 → FOUND.
76. `Wamelink 2019 Open Agriculture crop growth viability seeds Mars Moon soil simulants organic matter grass added harvest tomato rye radish garden cress` → FOUND (WUR abstract); curl edepot 504571 → empty file; degruyter → 301 → degruyterbrill 405; DOAJ 403. Full text DEAD at source.
77. `Paul Elardo Ferl 2022 Communications Biology Arabidopsis Apollo lunar regolith grown stress genes JSC-1A comparison results` → FOUND; nature.com → login redirect; PDF copy (poder360) → read; UF/IFAS release → read.
78. `Eichler 2021 Icarus "Challenging the agricultural viability of martian regolith simulants" MGS-1 perchlorate lettuce radish alkalinity nutrients` → PARTIAL (title not confirmed; Florida Tech release and Duri review used).
79. Frontiers fspas.2021.747821 (Duri et al. review) → FOUND, read to 100k chars, plus a second targeted read.
80. `Caporale 2020 MMS-1 Mars simulant green compost lettuce Salanova fresh weight yield 30:70 70:30 Frontiers Plant Science results` → FOUND (PMC7285329); summary's journal attribution was wrong (it is *Plants*).
81. `Texas A&M Mars regolith simulant plant growth study AgriLife crops biochar vermicompost simulant 2022 2023` → FOUND (chickpea work); bioRxiv → 429; Universe Today summary read.
82. `perchlorate removal Martian regolith simulant water leaching rinse plant growth restored percent removed study` → PARTIAL; RWU abstract → no numbers.
*Q5 closed 2026-10-25.*

RESUMED-PROTOCOL NOTE 2026-10-25: coordinator added the PROGRESS checklist instruction mid-run; checklist added at top, Q1–Q5 ticked (already written). No work redone.

**Q6 (2026-10-25)**
83. `half-moon demi-lune construction labor person-days per hectare WOCAT Niger Burkina Faso cost` → FOUND (J-PAL page; re-fetched for verbatim sentences; per-unit cost looks inconsistent).
84. `mine reclamation cost per acre topsoil replacement regrading revegetation bond estimate dollars per acre OSMRE dozer hours per acre` → FOUND; curl OSMRE Directive 1005 Appendix → worked example read; curl Arkansas bond form → read.
85. `composting facility labor hours per ton processed windrow turner hours per 1000 cubic yards operating cost per ton study` → FOUND (CIAS brief opened).
*Q6 closed 2026-10-25.*

**Q7 (2026-10-25)**
86. `Maine PFAS biosolids farmland contamination ban 2022 number of farms affected PFOS soil standard` → FOUND; Maine DACF 2026 slides (WebFetch binary → pdftotext) read; NACWA page read. Search summary's "5.2 ppb upper limit" was the earlier screening level; DACF's current most conservative farm soil level is 6.4 ppb PFOS.
87. `reclaimed mine soil compaction bulk density 1.7 1.8 g/cm3 root growth limiting scrapers loose dumping forestry reclamation approach study` → FOUND; FRA No. 3 (binary → pdftotext) read; Indiana 1.74 vs 1.54 figure not opened.
88. `WHO 2006 guidelines safe use of wastewater excreta agriculture helminth eggs per gram per liter limit log reduction` → FOUND; curl Mara chapter PDF → read.
89. `FAO Global Map of Salt-Affected Soils 2021 percent of irrigated land salt-affected million hectares annual loss of irrigated land to salinization` → PARTIAL (summaries only).
90. `soil erosion rate newly reclaimed mine spoil slopes before vegetation t/ha/yr rainfall simulation topsoil versus spoil erosion measured` → FOUND (So et al. 2018 PMC read).
*Q7 closed 2026-10-25.*

