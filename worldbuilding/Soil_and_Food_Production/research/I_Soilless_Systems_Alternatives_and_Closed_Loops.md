## PROGRESS (tick after each question is fully written to this file)
- [x] Q1
- [x] Q2
- [x] Q3
- [x] Q4
- [x] Q5
- [x] Q6
- [x] FINAL

# I. Soilless Systems, Non-Cropland Food, and Closed-Loop Nutrient Cycling: Real-World Spec Sheet

Research date: 2026-10-25. Real-world data only; nothing about any fictional setting.
Status tags: **SOURCED** (number read in the cited source) · **COMPUTED** (arithmetic shown) · **UNVERIFIED** (seen only secondhand or in a snippet; not confirmed in the primary source) · **NOT FOUND**.

---

## 1. Findings summary and comparison table

**Summary.**
- Electric-light farming works commercially for leafy greens, herbs and strawberries. Median for lettuce: 62 kg/m²/yr, 18 kWh/kg, 15 L/kg (Karpe et al. 2026 preprint, 11 LCAs).
- Staples are possible under lights but cost a lot of energy. Dry staples take ≈250 kWh/kg dry matter (Lovat et al. 2025), and electricity-to-food efficiency is 1–2%.
- Potato is by far the cheapest calorie under lights in NASA data: ≈32 kWh per 1,000 kcal for lighting alone (computed), ≈65 for the whole facility. Wheat costs ≈143 for lighting alone because of its 115 mol/m²/d light requirement.
- The computed budgets (lighting only, 3.0 µmol/J LEDs, 2,500 kcal/day):
  - soilless crops only: ≈43 m² and ≈6.2 kW per person, i.e. ≈0.62 GW and 4.3 km² of growing area per 100,000 people;
  - adding hydrogen-bacteria SCP cuts this to ≈33 m² and ≈5.1 kW;
  - fish and insects fed on lit wheat raise it to ≈14 kW, or ≈7.2 kW if fed on lit potato.
  - Whole-facility loads are probably about 2× these lighting figures. That factor comes from one crop cross-check.
- Closed loops: Lunar Palace 365 recycled 100% of O2 and water, recovered 99.7% of urine N and 67% of solid waste, and grew 73% of food by dry weight on 30 m²/person. Biosphere 2 lost O2 to its concrete. ISS recovers 98% of water.
- One adult excretes ≈5.0 kg N and 0.75 kg P per year. Struvite recovers >90% of urinary P but only ≈4% of urinary N (computed).
- Seed genebanks follow the FAO standard (−18 °C, 15% RH). A one-year food reserve is ≈280 kg of wheat or 555–870 kg of packaged space food per person.
- In polar settings, energy per kg of fresh food ran from ≈11–15 kWh/kg of electricity (lit Finnish winter cucumber) to ≈100 kWh/kg (South Pole chamber) and 115–370 kWh/kg (EDEN ISS).

**Comparison table** (energy is electricity unless marked; "per 1,000 kcal" is COMPUTED with USDA SR Legacy energy values where the food is in that dataset).

| System | Yield | Energy per kg | Energy per 1,000 kcal | Water | Readiness | Source | Status |
|---|---|---|---|---|---|---|---|
| Vertical farm, lettuce | 62 kg/m²/yr cultivation area (7–97) | 18 kWh/kg (10–39) | ≈120 kWh (150 kcal/kg) | 15 L/kg (1.4–52) | Commercial; several bankruptcies 2023–25 | Karpe et al. 2026 (preprint) | SOURCED / COMPUTED |
| Plant factory vs greenhouse, lettuce | — | PF 247; NL greenhouse 70; Sweden lit 211 kWh/kg **dry** weight (≈12 / 3.5 / 10.6 per kg fresh at 95% water) | PF ≈82; NL GH ≈23 | PF uses less water than GH | Commercial | Graamans et al. 2018 | SOURCED / COMPUTED |
| PFAL, strawberry (Japan) | 20 kg/m²/yr | — (electricity $199/m²/yr) | — | — | Commercial | Zhuang et al. 2022 | SOURCED |
| EDEN ISS sealed module (Antarctica) | lettuce 0.08–0.11 kg/m²/d; tomato 0.045–0.053; whole module ≈27 kg/m²/yr | lettuce 115–310; tomato 310–368 kWh/kg | lettuce ≈770–2,070; tomato ≈1,720–2,040 | not tracked | Research analog | Zabel et al. 2020; DLR 2019 | SOURCED / COMPUTED |
| South Pole Food Growth Chamber | 2.8 kg/day edible on ~23 m² | ≈100 kWh/kg | — (mixed salad crops) | — | Operated since 2004 | Patterson et al. 2012 | SOURCED / COMPUTED |
| Lit greenhouse cucumber, Finland, winter | — | 10.6–15.3 kWh/kg electricity + 2.8–5.0 heat | ≈71–102 electricity | — | Commercial | Kaukoranta et al. 2014 | SOURCED / COMPUTED |
| Lit potato, NASA chamber rates | 105 g FW/m²/d ≈ 38 kg/m²/yr | lighting ≈25 kWh/kg fresh | **≈32 (lighting only); ≈65 whole facility** | 0.15 L per g dry biomass | Research (NASA) | BVAD 2018; Lovat 2025 | COMPUTED |
| Lit wheat | 7.0 (measured) to 19.4 (simulated) kg/m²/yr per layer | lighting 300–830 kWh/kg | ≈92–255 | 0.13 L/g DW | Research; "would not be commercially viable" | Asseng et al. 2020 | SOURCED / COMPUTED |
| Lit soybean | 5.04 g FW/m²/d | lighting ≈515 kWh/kg | ≈115 | 0.32 L/g DW | Research | BVAD 2018 | COMPUTED |
| H2-oxidizing bacteria SCP | >1.2 kg protein/m²/yr of land incl. PV | ≈28–42 kWh/kg DW (up to ~70; unresolved); 37–76 per kg protein | not computed (food-energy basis unknown) | ~10 L/kg protein (company claim) | Modeled; early commercial (Solar Foods) | Leger et al. 2021 | SOURCED / COMPUTED / UNVERIFIED |
| Microalgae, tubular PBR (Portugal) | 27.6 t/ha/yr = 2.76 kg/m²/yr | 50.8 kWh/kg DW (electricity + gas); 131 for another strain pair | — | — | Commercial, high-value (€53/kg) | Vázquez-Romero et al. 2022 | SOURCED |
| Spirulina, open raceway | 5.1–5.6 g/m²/d ≈ 1.9–2.0 kg/m²/yr | NOT FOUND | — | — | Commercial | Allmicroalgae study (summary only) | UNVERIFIED |
| Mealworm | FCR 2.2 (farm); 3.8–6.1 (by-product diets) | 34 MJ = 9.4 kWh/kg fresh (total LCA); 48 kWh/kg edible protein | — | — | Commercial | Oonincx & de Boer 2012; Oonincx et al. 2015 | SOURCED / COMPUTED |
| Black soldier fly larvae on waste | 170 kg fresh per t waste; ≈345 kg/m² facility floor/yr | NOT FOUND (tropical, unheated) | — | — | Commercial | Dortmans et al. 2021 | SOURCED / COMPUTED |
| Tilapia RAS | FCR 1.22; fillet 35.7% | 1.8–2.2 kWh/kg fish + 0–3.4 heat | ≈5–6 electricity + 0–10 heat per 1,000 kcal of fillet (feed energy excluded) | 38–238 L/kg | Commercial | Eding et al. 2009 via Martins 2010; Rutten 2004 | SOURCED / COMPUTED |
| Trout/bass RAS (LCA incl. feed) | — | 15–20 kWh/kg | — | conventional RAS 0.1–1 m³/kg feed | Commercial | Martins et al. 2010 | SOURCED |
| Salmon post-smolt RAS | — | 9.6 kWh/kg (≥⅓ heating) | — | — | Commercial | Ayuso-Virgili et al. 2023 (secondary) | SOURCED-secondary |
| Cultivated meat (2030 model, 10 kt/yr) | — | 147–264 MJ = 41–73 kWh/kg total; on site 21.7 e + 1.1 heat | — | — | Approved in SG/US; restaurant-scale | CE Delft 2021 | SOURCED / COMPUTED |
| Mycoprotein | 85 kcal, 11 g protein per 100 g | NOT FOUND | — | — | Commercial (Quorn) | Finnigan et al. 2019 | SOURCED |
| Broiler | FCR 1.44 (day 37, 2.5 kg) | — | — | — | Commercial | Aviagen 2022 | SOURCED |
| Rabbit / dairy | rabbit farm FCR 3.4; dairy 1.4–1.6 kg ECM/kg DMI | — | — | — | Commercial | summary / Penn State 2019 | UNVERIFIED / SOURCED |
| Mushrooms (*Agaricus*) | 25–43 kg/m² per crop | NOT FOUND | — | — | Commercial | Samp 2021 | SOURCED |

Per-person budgets (Q4, COMPUTED, lighting only, 3.0 µmol/J): (a) crops only 42.9 m², 6.19 kW; (b) + SCP 32.6 m², 5.05–5.09 kW; (c) + tilapia & mealworms, feed as lit wheat 53.4 m², 13.97 kW (feed as lit potato: 52.4 m², 7.19 kW). Multiply kW by 100,000 or 1,000,000 for MW: (a) 619 MW / 6.19 GW; (b) ≈505 MW / 5.05 GW; (c) 1.40 GW / 14.0 GW.

RESUMED/updated 2026-10-25 (progress checklist added mid-run on coordinator instruction; Q1–Q4 were already complete when added).

---

## 2. Findings by question

### Q1. Soilless crop systems

#### 1.1 Indoor vertical farms / plant factories with artificial lighting (PFAL), lettuce

**Primary source: Karpe, Martin, Muñoz-Liesa, Marcelis, Heuvelink, "Quantitative review of environmental life cycle assessments of vertical farms – aligning reported impacts, and energy outlook for 2050," Research Square preprint, posted 2026-09-09, DOI 10.21203/rs.3.rs-10962166/v1 (Wageningen / IVL / Agroscope). Read in full text (PDF). NOTE: preprint, not yet peer-reviewed.** Eleven lettuce vertical-farm LCA case studies, KPIs per kg fresh lettuce:

| KPI | Range | Median | IQR | Status |
|---|---|---|---|---|
| Annual productivity, kg lettuce per m² cultivation area | 7–97 | 62 | 44–69 | SOURCED |
| Annual productivity, kg per m² facility floor area | — | 124 | — | SOURCED (Table 2) |
| Energy use efficiency, kWh per kg lettuce | 10–39 | 18 | 15–25 | SOURCED |
| Energy per m² cultivation area per year | — | 1,012 kWh | 813–1,292 | SOURCED |
| Energy per m² floor area per year | — | 2,225 kWh | 1,452–3,566 | SOURCED |
| Irrigation water, L per kg lettuce | 1.4–52 | 15 | 9.1–24 | SOURCED |
| Carbon footprint, kg CO2eq per kg (harmonized, Dutch grid) | 4.8–16 | 7.6 | — | SOURCED |
| Cumulative energy demand, MJ per kg | 99–336 | 152 | — | SOURCED |

Further points read in the same preprint (SOURCED):
- Earlier literature (Martin et al. 2023, cited there) reported 2.4–1,000 kWh/kg and 45–1,204 kg/m² floor area; Karpe et al. attribute the high yields partly to reporting per floor area instead of per cultivation area (example: one farm = 74 kg/m² facility floor vs 311 kg/m² "cultivation room floor" vs 88 kg/m² cultivation area).
- Best case among the eleven: 10 kWh/kg (Martin et al. 2023). Other cited benchmarks: 10–18 kWh/kg for 18 operational and simulated farms (Miserocchi & Franco 2024); 10–33 kWh/kg within one farm depending on light/temperature/VPD (Talbot & Monfet 2024); 22–54 kWh/kg across four varieties (Cossu et al. 2023).
- Proposed theoretical floors: 4.4 kWh/kg with today's best LEDs and climate control, 3.3 kWh/kg with future technology (Stanghellini & Katzin 2024, as cited by Karpe et al.; original not opened, see open threads); 3.1–7.4 kWh/kg assuming 90% LED efficiency (Miserocchi & Franco 2024, as cited).
- Fluorescent-lit early farms were the least efficient; LEDs are "~45% more energy efficient" (Erekath et al. 2024, as cited).
- Economic failure mode: "several VF companies recently filed for bankruptcy, e.g., Infarm (modular cabinets, in 2023), Freight Farms (container farms, in 2025), and Plenty (large-scale farm, in 2025)."
- Electricity source dominates carbon: harmonized median 14.1 kg CO2eq/kg on the Chinese grid vs 1.2 on the Swedish grid.

**Second source: Graamans, Baeza, van den Dobbelsteen, Tsafaras, Stanghellini (2018), "Plant factories versus greenhouses: Comparison of resource use efficiency," *Agricultural Systems* 160:31–43, DOI 10.1016/j.agsy.2017.11.003 (abstract read on WUR repository).** Purchased energy per kg **dry weight** of lettuce (SOURCED):
- Plant factory: 247 kWh(e)/kg DW
- Greenhouse, Netherlands: 70; United Arab Emirates: 111; Sweden without supplementary light: 182; Sweden with supplementary light: 211 kWh(e)/kg DW
- Total energy including sunlight: plant factory 1,411 MJ/kg DW vs best greenhouse (Sweden, lit) 1,699 MJ/kg DW.
- Plant factories had higher productivity per unit water, CO2 and land; greenhouses win on purchased energy because sunlight is free. Climates studied: 24–68° N.
- COMPUTED conversion: lettuce is ~95% water (BVAD Table 4-97, below), so 1 kg DW ≈ 20 kg FW; 247 kWh/kg DW ≈ 12 kWh/kg FW. Assumption: 95% water content. Consistent with the 10–39 kWh/kg FW range above.

**Third source: Lovat, Noor, Milo (2025), "Vertical farming limitations and potential demonstrated by back-of-the-envelope calculations," *Plant Physiology* 198(3): kiaf056 (PMC12225668, read).** SOURCED:
- Electricity-to-edible-food energy conversion in vertical farms "≈1% to 2%" (range across studies 0.4–1.9%); theoretical future "roughly 10%."
- Dry staples (wheat, rice, soy): "≈250 kWh/kg of dry plant matter," electricity "≈$10/kg" vs farm prices "<$1/kg."
- Leafy greens/tomato: electricity "≈$0.5/kg," comparable with producer prices.
- Land for electricity: ≈0.01 m²·yr per kWh for PV; vertical-farm dry crops via PV need ≈2–3 m²·yr/kg of land, versus ≈3 m²·yr/kg for conventional wheat. I.e., counting the solar field, an indoor wheat farm uses about as much land as a field.
- Direct water: "on the order of 10 L/kg of fresh lettuce."

**Capital and operating cost: Zhuang, Lu, Shimamura, Maruyama, Kikuchi, Takagaki (2022), "Economies of scale in constructing plant factories with artificial lighting and the economic viability of crop production," *Frontiers in Plant Science* 13:992194 (read).** SOURCED (Japan, 26 facilities):
- Construction cost per m² of plantable area: US$893 to US$4,167; above-average 3,000 m² PFAL: US$1,808/m².
- Lettuce operating cost US$700/m²/yr (labor 279, electricity 166, seeds/nutrients 86, water/other 12, packaging/logistics 157); assumed yield 115 kg/m²/yr; revenue US$1,204/m²/yr.
- Strawberry operating cost US$791/m²/yr (labor 175, electricity 199); yield 20 kg/m²/yr.
- Note: Karpe et al. flag that the 115 kg/m² lettuce yield is about double the median observed in LCAs.

#### 1.2 EDEN ISS (DLR) Antarctic greenhouse, Neumayer III — closed, artificially lit, aeroponic/hydroponic

**DLR press release 2019-08-23 (read):** 268 kg of food on 12.5 m² over 9.5 months (2018 season, 7 Feb–20 Nov 2018): 67 kg cucumbers, 117 kg lettuce, 50 kg tomatoes (press-release figures). Average power 0.8 kW per m² cultivation area (vs 2.1 kW/m² previously assumed for space greenhouses). Crew time 3–4 h/day (two-thirds operation/maintenance, one-third sowing/harvest/plant care). SOURCED.

**Zabel, Zeidler, Vrakking, Schubert (2020), "Implications of different plant cultivation techniques for food production in space based on experiments in EDEN ISS," 50th ICES, ICES-2020 (elib.dlr.de/135982, full PDF read).** SOURCED:
- Itemized 2018 harvest to 20 Nov 2018: 67 kg cucumber, 46 kg tomato, 19 kg kohlrabi, 8 kg radish, 15 kg herbs, 56 kg lettuce, 51 kg leafy greens, 1.5 kg sweet pepper (sum COMPUTED = 263.5 kg; differs slightly from the press release's 268 kg and its category split — both recorded).
- Lettuce productivity, kg FW per m² per day: full harvest 0.043 (Othilie) and 0.080 (Waldmann's Green); spread (continuous leaf) harvest 0.111 and 0.097. Light: ~330 µmol/m²/s, 7 h dark per day.
- Dwarf tomato: 0.045–0.053 kg/m²/d across 120-, 200- and 286-day cycles; 300–400 µmol/m²/s.
- Power (time-averaged): lighting 0.121 kW/m² for lettuce, 0.279 kW/m² for tomato; other subsystems per m²: nutrient delivery 0.013, atmosphere management 0.268, thermal control 0.080, control/data 0.049 kW/m². Total 0.532 kW/m² (lettuce), 0.690 kW/m² (tomato).
- Electrical energy per kg edible FW: lettuce 114.8–310.5 kWh/kg; dwarf tomato 309.8–367.9 kWh/kg.
- Crew time: total ~36 min/day maintenance for whole facility (2 min 56 s per m² per day); per kg lettuce 0:41–1:24 h; per kg tomato 0:21–0:46 h.
- COMPUTED annualized whole-greenhouse yield: 268 kg / 12.5 m² = 21.4 kg/m² in 9.5 months → × 12/9.5 = 27.1 kg/m²/yr (all crops mixed).
- Interpretation (from source structure, not a claim of the paper): EDEN ISS's energy per kg is ~10× a commercial vertical farm's, because the atmosphere management subsystem alone draws more than the lights in a small sealed module.

#### 1.3 NASA controlled-environment staple-crop data (BPC and BVAD)

**NASA Life Support Baseline Values and Assumptions Document, NASA/TP-2015-218570 Rev1, January 2018 (PDF read; Tables 4-96 to 4-100).** Nominal hydroponic productivities under the listed light (SOURCED, Table 4-97/4-96):

| Crop | PPF mol/m²/d | Photoperiod h | Edible g DW/m²/d | Edible g FW/m²/d | Harvest index % | Growth period d |
|---|---|---|---|---|---|---|
| Wheat | 115 | 20–24 | 20.00 | 22.73 | 40 | 75–90 |
| White potato | 28 | 12 | 21.06 | 105.30 | 70 | 132 |
| Sweet potato | 28 | 12 | 24.7 | 51.72 | 60 | 85 |
| Soybean | 28 | 12 | 4.54 | 5.04 | 40 | 97 |
| Rice | 33 | 12 | 9.07 | 10.30 | 30 | 85 |
| Dry bean | 24 | 18 | 10.00 | 11.11 | 40 | 85 |
| Peanut | 27 | 12 | 5.63 | 5.96 | 25 | 104 |
| Lettuce | 17 | 16 | 6.57 | 131.35 | 90 | 28 |
| Tomato | 27 | 12 | 10.43 | 173.76 | 45 | 85 |
| Strawberry | 22 | 12 | 7.79 | 77.88 | 35 | 100 |
| Pepper | 27 | — | 10.43 | 148.94 | 45 | 85 |

- "Highest" total-biomass values (Table 4-98): wheat 150 g DW/m²/d vs nominal 50; potato 50 vs 30; soybean 20 vs 11.34; rice 39 vs 30.23.
- Diet growing area (Table 4-99): salad-only diet 1.35 m² per crew member; salad + carbohydrate crops 19.50 m²/CM; **diet using all ELS crops 65.29 m² per crew member** (of which soybean alone 46.43 m²). SOURCED.
- Water and nutrient use (Table 4-100, from Wheeler et al. 1999): water 0.32 (soy), 0.13 (wheat), 0.15 (potato), 0.34 (lettuce) L per g dry biomass; stock solution 0.021–0.034 L/g DW; nitric acid for pH 0.043–0.074 g/g DW.
- Fertilizer: "90 to 100 kg of fertilizer salt might be required per person per year" to supply 2,500 kcal/person/day; ">50% of these nutrients could be recycled from inedible biomass" (BVAD citing Lunn et al. 2017 and Strayer et al. 2002). SOURCED. (Used again in Q3.)
- Nutrient solution management (BVAD text): replenishment added by electrical conductivity "regardless of which ions are depleted"; pH controlled by nitric acid; sodium or boron build-up means "the nutrient solution is often replaced at regular intervals"; N lost by microbial volatilization. SOURCED.

**R. M. Wheeler, "NASA's Contributions to Vertical Agriculture," presentation, 2015 (PDF read via simoc.space).** SOURCED:
- Biomass Production Chamber (KSC, 1987–2000): 20 m² growing area, 113 m³, 96 × 400 W HPS lamps, two 52 kW chillers, two 30 kW blowers, 100 kW air reheat — "Not designed for energy efficiency!!"
- High-light CEA records: wheat "3–4 × world record," potato "2 × world record." Wheat 61 g DM/m²/d (RUE 1.44 g/mol PAR) and 130 g DM/m²/d (0.67 g/mol) at Utah State; potato 45 g DM/m²/d (12→24 h photoperiod) and 38 (12 h).
- Radiation conversion 0.4–0.6 g DM per mol applied PAR across crops (search-snippet summary of Wheeler et al. 1996; the slide shows the chart, not the number — UNVERIFIED as a quote).
- BPC totals (NTRS 20040089951 abstract via search snippet): 481 kg dry biomass, 196 kg edible biomass, 540 kg O2, 94,700 kg condensed water, 739 kg CO2 fixed over 5 wheat, 3 soybean, 5 lettuce, 4 potato crops. UNVERIFIED (snippet; abstract page not opened).

**Indoor wheat: Asseng et al. (2020), "Wheat yield potential in controlled-environment vertical farms," *PNAS* 117(32):19131–19135 (PMC7430987, read).** SOURCED:
- Measured: 14 ± 0.8 t/ha per 70-day harvest → 70 ± 4 t/ha/yr (5 harvests/yr), single layer.
- Simulated: 114 ± 13 t/ha/yr standard; 194 ± 23 t/ha/yr max per layer; 1,940 ± 230 t/ha/yr for 10 layers. World average 3.2 t/ha/yr.
- Conditions: up to 2,000 µmol/m²/s, 24 h/d, 1,200 ppm CO2, 23 °C.
- Economics: more than half of current costs are lighting electricity; cost-to-return 46:1 today, ~6:1 in future, "still would not be commercially viable."
- COMPUTED lighting energy for that regime: 2,000 µmol/m²/s × 86,400 s = 172.8 mol/m²/d. Assumed LED efficacy 3.0 µmol/J (ASSUMPTION; high-end current fixtures, not sourced here) → 57.6 MJ = 16.0 kWh/m²/d → 5,840 kWh/m²/yr lighting only. At measured 7.0 kg/m²/yr: 834 kWh/kg grain; at simulated maximum 19.4 kg/m²/yr: 301 kWh/kg. Same order as Lovat et al.'s ≈250 kWh/kg dry matter.

#### 1.4 Greenhouses (sunlit, heated, with or without supplementary light)

- Netherlands sector average energy use 0.8 GJ/m²/yr in 2022 (-29% vs 2021, i.e. ≈1.13 GJ/m² in 2021 COMPUTED from the stated drop), total 85 PJ, crop-growth CO2 31.5 kg/m² after temperature correction; renewable share "ruim 15%"; geothermal (aardwarmte) and biofuels are the main renewable sources. Source: Smit, P. (2023), *Energiemonitor van de Nederlandse glastuinbouw 2022*, Wageningen Economic Research Rapport 2023-138 (edepot.wur.nl/641047, read). SOURCED. COMPUTED: 0.8 GJ = 222 kWh/m²/yr.
- Dutch tomato yield: >60 kg/m²/yr in the 2000s vs ~30 in the 1980s, citing KWIN (search snippet of a J-STAGE Horticulture Journal review; not opened) — UNVERIFIED. FAO-derived national 2020 average 48.66 kg/m² (hortidaily summary; not opened) — UNVERIFIED.
- Energy in lit tomato at two Dutch farms 25.4–37.8 m³ natural gas equivalent per m² per year; a WUR concept reached 12 m³/m²/yr (hortidaily / edepot snippets) — UNVERIFIED.
- Year-round lit tomato "2.73 GJ/m² or 761 kWh/m²" (snippet attributed to New Zealand EECA "Energy Benchmarking in Covered Cropping") — UNVERIFIED.

#### 1.5 Aquaponics

- UVI commercial system (J. Rakocy, University of the Virgin Islands; UVI web page read): 5 metric tons tilapia per year, harvest every 6 weeks; optimum feeding-rate ratio for raft hydroponics 60–100 g feed per m² of plant area per day; "at least 25% of feed given to fish becomes solid waste" (dry basis); pH 7.0 as fish/plant compromise. SOURCED.
- FAO small-scale guidance (Somerville et al. 2014, FAO Fisheries and Aquaculture Technical Paper 589, as reproduced at learn.farmhub.ag): 40–50 g feed/m²/day for leafy greens, 50–80 g/m²/day for fruiting vegetables; fish density 10–20 kg per 1,000 L; feed 1–2% of body weight per day; lettuce 20–25 plants/m². SOURCED (secondary reproduction of the FAO manual; original PDF not opened).
- UVI production numbers from search snippets (tilapia 61.5 and 70.7 kg/m³ for Nile and red tilapia; basil 25.0 kg/m³-equivalent batch; okra 13.37 kg/m² projected annual; 1,404 cases lettuce/yr; 3.0 hp total motors) — UNVERIFIED: the ISTA-6 paper (cales.arizona.edu …/676.pdf) returned 404 and the UVI archive PDF returned 401; SRAC 454 PDF failed with an SSL error.
- Energy per kg for aquaponics: NOT FOUND in a read source.

#### 1.6 Hydroponic variants (NFT, DWC, drip on inert media, aeroponics)

- Head-to-head yield by technique for the same crop under the same light: the read sources report by crop and facility, not by technique. NOT FOUND as a peer-reviewed numeric comparison in a source I opened.
- Potato minitubers, aeroponics vs NFT vs deep-flow (search snippets only, Brazilian *Horticultura Brasileira* abstract and Iranian journal): aeroponic 49.3 minitubers/plant and 874.4 per m² vs NFT 39.5 and 246.6 vs DFT 41.6 and 458.0; another study reports +58% yield and +277% tuber number for aeroponics vs hydroponics. UNVERIFIED (scielo returned 502).
- Failure mode, root pathogens in recirculating solution: zoospores (Pythium) "pumped past every other root system on the line within minutes"; in an inoculation study all plants in a recirculating unit died within 5–6 weeks of inoculating one plant without surfactant; a commercial case lost ~50% of 30,000 plants in 2 weeks; controls: UV, 0.5 µm filtration (removes zoospores), nonionic surfactants. Source: search summary of APS *Plant Disease* 1998 82(7):831 and a University of Kentucky extension sheet E706 — UNVERIFIED (APS page returned 403; E706 not opened).
- Other failure modes from read sources: ion build-up (Na, B) forcing solution replacement (BVAD); power dependence — EDEN ISS lighting plus atmosphere control is 100% electric (Zabel 2020); business failure of large vertical farms 2023–2025 (Karpe et al.).

#### 1.7 Which crops work, which do not scale (from the read sources)

- Work commercially indoors: lettuce and leafy greens, herbs, strawberries (Zhuang 2022: 20 kg/m²/yr), microgreens; tomatoes, cucumbers, peppers in greenhouses (Dutch sector) and in sealed modules (EDEN ISS).
- Grown successfully in NASA chambers but uneconomic at scale under electric light: wheat, potato, sweet potato, soybean, rice, peanut, dry bean (BVAD; Wheeler 2015; Asseng 2020).
- The scaling limit is lighting energy per kcal: dry staples ≈250 kWh/kg dry matter (Lovat 2025); indoor wheat 300–830 kWh/kg COMPUTED above. Low harvest index (rice 30%, wheat/soy 40%, BVAD) multiplies the light needed per edible kg.

**Q1 search-log lines are in Section 4.**

### Q2. Calories and protein without cropland

#### 2.1 Single-cell protein (SCP) from gases

**Leger, Matassa, Noor, Shepon, Milo, Bar-Even (2021), "Photovoltaic-driven microbial protein production can use land and sunlight more efficiently than conventional crops," *PNAS* 118(26) e2015025118, PMC8255800 (read).** Modeled, based on laboratory data. SOURCED:
- Protein yield per land area: >1,200 g protein/m²/yr for all three routes (H2 via Calvin cycle; methanol via RuMP; formate via serine cycle), vs soybean ≈115, wheat 51, rice 31 g protein/m²/yr.
- Crop calorie yields for comparison: sugar beet ≈4,520, maize ≈2,640, oil palm ≈2,650 kcal/m²/yr. SCP gives "at least twice the caloric yield compared with any staple crop" per land area.
- Overall sunlight-to-food efficiency 0.4% (food), 0.8% (feed) at the optimum; component efficiencies: PV 4.1–5.6% (30th–70th percentile, includes land between panels), electrolysis to H2 65–75%, formate 30–50%, methanol 50–60%; microbial growth on H2 32% ± 5%.
- Supporting processes take 17–36% of total electricity; direct air capture 6–9 MJ per kg CO2; bioreactor operation 7.7–15.6 MJ/kg DW; food-grade downstream 10.5–21 MJ/kg DW.
- Biomass heat of combustion assumed 20 MJ/kg DW; protein content 55–75% of DW.
- 1 ha example at 2,000 kWh/m²/yr irradiance: 6,650 m² PV + ≈3,300 m² for other processes feeds "more than 500 people" (protein basis) vs 40 people/ha for soybean.
- Human-food caveat: nucleic acids must be removed (uric acid, gout risk); food processing adds bead-milling and microfiltration.
- **COMPUTED electricity per kg DW, H2 route:** 20 MJ ÷ (0.65 to 0.75 electrolysis × 0.32 growth) = 83–96 MJ into electrolysis; dividing by (1 − 0.17 to 0.36) for supporting loads gives 100–150 MJ = **28–42 kWh per kg dry biomass**, i.e. **37–76 kWh per kg protein** at 55–75% protein. Assumptions: the paper's stated component efficiencies combined multiplicatively; no other losses.
- Cross-check discrepancy: dividing the paper's overall 0.4% by its PV efficiency (≈5%) implies ≈8% electricity-to-food efficiency, i.e. ≈70 kWh per 20 MJ — higher than my 28–42 kWh/kg DW. I could not resolve which energy basis (combustion vs protein) the 0.4% uses. Treat SCP electricity as **≈30–70 kWh per kg DW, range unresolved**.

**Hydrogen-oxidizing bacteria, commercial (Solar Foods, Solein).** Xanthobacter-genus bacterium; gas feed CO2:O2:H2 = 1:2:7 by volume (priceplow.com blog, secondary, UNVERIFIED). Company LCA claims ~10 L water and ~2 m² land per kg protein (search summary only, UNVERIFIED). **Measured electricity per kg Solein: NOT FOUND** (company reports and Sillman et al. 2019, *Global Food Security* 22:25–32, located by title only).

**Methanotroph SCP (Calysta FeedKind, *Methylococcus capsulatus* Bath).** Industrial plant in Chongqing, China, opened 2022, 20,000 t/yr capacity (Wikipedia, via search; UNVERIFIED). Protein 75.14% (Frontiers in Marine Science 2021 snippet; UNVERIFIED). Maximum yield 0.65 g cells per g methane; another study 0.49 g SCP/g CH4 over 240 days (snippets; UNVERIFIED). Feed product, not approved here as human food (not checked).

#### 2.2 Mycoprotein (*Fusarium venenatum*, Quorn)

**Finnigan, Wall, Wilde, Stephens, Taylor, Freedman (2019), "Mycoprotein: The Future of Nutritious Nonmeat Protein, a Symposium Review," *Current Developments in Nutrition* 3, DOI 10.1093/cdn/nzz021 (PMC6554455, read).** SOURCED:
- Per 100 g wet: protein 11 g, fat 2.9 g, fiber 6.0 g, 85 kcal. Dry: ~45% protein, ~25% fiber.
- Process: continuous fermentation on glucose (Leger et al. say wheat-derived glucose), then steaming (RNA reduction), chilling, freezing.
- Footprint claim: "≥10 times less embedded carbon, land, and water use" than beef (no absolute numbers in the review).
- Energy per kg mycoprotein: NOT FOUND (RSC Green Chemistry 2021 LCA, d1gc01021b, returned 403).
- Note: mycoprotein still needs a sugar feedstock, i.e. cropland or another carbohydrate source upstream.

#### 2.3 Precision fermentation

- Perfect Day non-animal whey (beta-lactoglobulin; *Trichoderma reesei* per FoodNavigator 2021): company-commissioned LCA by WSP (report dated 20 Aug 2021, ISO 14067 review): vs total milk protein, 91–97% lower GHG, 29–60% lower non-renewable energy, 96–99% lower blue water; feedstock corn-derived glucose. Source: perfectday.com LCA blog (read). Relative values only; **absolute MJ/kg NOT FOUND.**

#### 2.4 Microalgae and cyanobacteria

- **Tubular photobioreactor, industrial, south Portugal (Vázquez-Romero, Perales, Pereira, Barbosa, Ruiz 2022, "Techno-economic assessment of microalgae production, harvesting and drying for food, feed, cosmetics, and agriculture," *Science of the Total Environment* 837:155742; read via edepot.wur.nl/570707).** SOURCED: *Nannochloropsis* year-round 27.61 t/ha/yr (1 ha), cost €53.32/kg DW; *Tisochrysis + Phaeodactylum* 13 t/ha/yr, €105/kg DW. Energy (electricity + natural gas) 131.30 kWh/kg (TISO+PHT) and 50.82 kWh/kg DW (NAS); centrifuge 28.53 vs ultrafiltration 25.83 kWh/kg; spray dryer 36.45 vs freeze-dryer 22.29 kWh/kg; Tredici et al. (2016) reported 5.96 kWh/kg for a similar process with equipment not run 24 h (as cited there). Photosynthetic efficiency NAS 1.02%, PHT 0.81%, TISO 0.38%. PBRs ≈67–71% of equipment cost; investment €7.72 M per 1 ha facility. COMPUTED: 27.61 t/ha/yr = 2.76 kg/m²/yr = 7.6 g/m²/d.
- **Spirulina (*Limnospira platensis*) in open raceways, Allmicroalgae, Portugal, 1,000 and 4,000 m² ponds:** annual mean 5.1–5.6 g/m²/d; April–September peak 7.5–7.6 g/m²/d; winter productivity decline >60%; protein 58.4–64.7% year-round; phycocyanin 10.4% (winter) to 15.2% (summer); 30% biomass loss in harvest/post-processing. Source: "Impact of seasons on industrial cultivation of Limnospira platensis (Spirulina): a year-round case study…" (search summary; repository returned a login page) — UNVERIFIED. COMPUTED if accepted: 5.1–5.6 g/m²/d × 365 = 1.9–2.0 kg/m²/yr ≈ 1.1–1.3 kg protein/m²/yr.
- Ruiz et al. (2016), *Energy & Environmental Science* (100 ha in six locations): €3.4/kg DW cost in Spain, projected €0.5/kg in ten years (search summary; RSC PDF blocked) — UNVERIFIED.
- Raceway energy per kg: NOT FOUND in a read source.

#### 2.5 Mushrooms on waste substrates

- *Agaricus bisporus*, Dutch system: compost fill ~85–90 kg/m², yield 25–33 kg/m² per crop; US system: fill ~125–130 kg/m², ~37–43 kg/m² in 3 flushes; compost of straw, stable bedding, gypsum, poultry manure. Source: R. Samp, "Comparison of Dutch and US mushroom growing strategies," Mushroom Business, 2021-07-15 (read; trade press). SOURCED. Crops per year and energy per kg: NOT FOUND.
- Oyster mushroom (*Pleurotus*) biological efficiency 48.9–82% (kg fresh mushrooms per 100 kg dry substrate) across studies (search snippets; AMB Express tables not opened) — UNVERIFIED.
- Note: mushrooms add little energy (BVAD Table 4-96 lists mushroom with 0 light requirement) but are mainly a protein/flavor complement; nutrient composition not researched here.

#### 2.6 Insects

**Mealworm LCA: Oonincx & de Boer (2012), "Environmental Impact of the Production of Mealworms as a Protein Source for Humans – A Life Cycle Assessment," *PLoS ONE* 7(12):e51145 (PMC3526541, read; Dutch commercial farm).** SOURCED:
- Per kg fresh mealworms: 2.7 kg CO2eq, 34 MJ energy, 3.6 m²·yr land. Per kg edible protein: 14 kg CO2eq, 173 MJ, 18 m².
- FCR 2.2 kg feed per kg live weight (feed: carrots + mixed grain).
- Gas heating 26% and electricity 17% of energy for fresh mealworms (rest is mostly feed production).
- Energy per kg edible protein: milk 21–83%, chicken 46–88%, pork 55–137% of the mealworm value; beef 1.02–1.58×. Land: milk 1.81–3.23×, chicken 2.30–2.85×, pork 2.57–3.49×, beef 7.89–14.12× mealworm.
- Composition: *T. molitor* 38% DM, 53% crude protein in DM.
- COMPUTED: 34 MJ = 9.4 kWh per kg fresh; 173 MJ = 48 kWh per kg edible protein (total LCA energy, not only on-farm).

**Feed conversion by species: Oonincx, van Broekhoven, van Huis, van Loon (2015), "Feed Conversion, Survival and Development, and Composition of Four Insect Species on Diets Composed of Food By-Products," *PLoS ONE* 10(12):e0144601 (PMC4689427, read).** SOURCED (FCR range across diets; basis as defined in the paper, which I did not confirm as DM-feed per fresh-weight gain):
- Black soldier fly larvae: FCR 1.4–2.6; development 21–37 days; survival 72–86%.
- Yellow mealworm: FCR 3.8–6.1; 83–227 days; survival 15–93%.
- House cricket: FCR 2.3 (control) to 4.5; 48–167 days; survival 6–55%.
- Argentinean cockroach: FCR 1.5–2.7; 200–294 days.
- Paper's livestock comparison (concentrate to edible product): poultry 2.3, pork 4.0, cereal beef 8.8.

**Black soldier fly biowaste processing: Dortmans, Egger, Diener, Zurbrügg (2021), *Black Soldier Fly Biowaste Processing – A Step-by-Step Guide*, 2nd ed., Eawag, ISBN 978-3-906484-75-4 (PDF read).** SOURCED:
- Indonesian facility: 1 t waste (25% DM) → 170 kg fresh larvae → 45 kg dried larvae.
- Larvae 10–20% and frass 20–40% of waste wet weight; waste reduction 60–85% (dry weight); up to 80% wet weight.
- Treatment footprint 31.25 kg biowaste per m² per day with units stacked six high.
- Facility sizes: 5 t/d ≈ 900 m² total (121 rearing, 678 conversion, 105 processing); 2 t/d ≈ 400 m²; 1 t/d ≈ 250 m². Daily schedule for 35 t/wk needs 23 workers.
- COMPUTED: 5 t/d × 0.17 = 850 kg fresh larvae/day on ≈900 m² → ≈0.94 kg/m²/d ≈ **345 kg fresh larvae per m² facility floor per year** (tropical climate, no heating). Energy for a heated (cold-climate) BSF facility: NOT FOUND.

#### 2.7 Cultivated meat

**Sinke & Odegard (CE Delft, Feb 2021), *LCA of cultivated meat: Future projections for different scenarios*, report 21.190107.019, for GAIA and GFI (PDF read).** SOURCED:
- Modeled 2030 plant producing 10 kton/yr.
- Energy use 147–264 MJ/kg product (sensitivity 124–445); carbon footprint 2.5–13.5 kg CO2eq/kg (2.1–22.6). Earlier LCAs: Mattick et al. 2015 106 MJ/kg; Tuomisto et al. 2014 35–61; Tuomisto & Teixeira de Mattos 2011 25–32.
- Facility energy, baseline: 2.17 × 10⁸ kWh electricity and 1.08 × 10⁷ kWh heat per year. COMPUTED: ÷ 10,000,000 kg = **21.7 kWh electricity + 1.1 kWh heat per kg** on site (the rest of the 147–264 MJ is upstream, chiefly culture medium).
- Impact "largely driven by energy use; primarily electricity," and medium.
- The peer-reviewed version (Sinke et al. 2023, *Int J LCA*) was located by title only, not opened.

**Status (FoodNavigator, D. Ataman, 2026-02-18, read):** Singapore 3 products approved (Good Meat chicken, Vow quail, Parima chicken); United States 5 (Upside chicken, Good Meat chicken, Wildtype salmon, Mission Barns pork fat, Believer poultry; Believer "shuttered in December 2025"); UK pet food only (Meatly). "Most companies are launching through limited restaurant testing." Production volumes not disclosed. SOURCED. Conflict: a search summary says Australia approved sales via FSANZ in 2025, while this article lists Australia as under review — UNRESOLVED. GOOD Meat's first retail product was 3% cultivated cells, 97% plant ingredients (search summary; UNVERIFIED).

#### 2.8 Recirculating aquaculture (RAS)

**Martins et al. (2010), "New developments in recirculating aquaculture systems in Europe: A perspective on environmental sustainability," *Aquacultural Engineering* 43(3):83–93 (author draft read via Archimer).** SOURCED:
- Water classes: flow-through >50 m³/kg feed; reuse 1–50; conventional RAS 0.1–1; "next generation" RAS <0.1 m³/kg feed. Refreshment 30–300 L/kg feed/day (African catfish); eel 200–300 L/kg feed; tilapia as low as 30 L/kg feed.
- Energy (Table 3, LCA incl. feed): trout flow-through 10–12 kWh/kg; trout or sea bass RAS 15–20 kWh/kg (build 6–7, feed 5–6, operation 3–6); RAS 63,202 MJ/t = 16 kWh/kg (Roque d'Orbcastel et al. 2009); mussel 0.7; cod fishing 5–21; tilapia RAS operation 5.2 (conventional) / 2.2 (with denitrification).
- Table 4, 100 t/yr intensive tilapia farm (Eding et al. 2009): feed 1.22 kg/kg fish; electricity 1.8 / 2.2 kWh/kg; heating 3.4 / 0.0 kWh/kg; water 238 / 38 L/kg; oxygen 1.18 / 1.26 kg/kg; bicarbonate 252 / 107 g/kg; labor 12.5 / 13.1 h per t; nitrogen retained 32% of input, phosphorus 43% (conventional / denitrification RAS).
- Salmon post-smolt RAS 9.586 kWh/kg; pumps 45.48% of demand; heating freshwater ≥ one-third (Ayuso-Virgili, Jafari, Lande-Sudall, Lümmen 2023, *Aquacultural Engineering*, as reported by aquahoy.com; secondary, not opened) — SOURCED (secondary).
- Norwegian smolt RAS 5.1–12.8 kWh/kg (mean 8.8), grow-out 6–10 kWh/kg (NTNU study "Current and Future Energy Use for Atlantic Salmon Farming in RAS in Norway"; page 404) — UNVERIFIED.
- Stocking density in RAS: NOT FOUND in a read source (aquaponics guidance 10–20 kg/1,000 L, Q1 §1.5, is for small-scale systems).

#### 2.9 Poultry, rabbits, dairy under cover

- **Broiler (Aviagen, *Ross 308/308 FF Broiler: Performance Objectives 2022*, PDF read):** as-hatched, day 37: 2,496 g, cumulative intake 3,584 g, FCR 1.437; day 42: 2,998 g, FCR 1.531. FCR "does not account for mortality" (breeder targets, not farm averages). SOURCED.
- **Rabbit:** whole-farm FCR in European intensive farms improved from 3.8 to 3.4 over 15 years; 3.0 thought reachable (search summary of a Padova/INRA paper; pages 403) — UNVERIFIED.
- **Dairy:** feed efficiency benchmarks 1.4–1.6 lb ECM per lb DMI for all cows 150–225 DIM; early multiparous 1.6–1.8; problem herds <1.3 (Heinrichs & Ishler, Penn State Extension, 2019-01-29, via dairyproducer.com, read). Ratio is unit-free, so same in kg/kg. SOURCED.
- Energy per kg for housed poultry/rabbit/dairy: NOT FOUND (not searched in depth; feed dominates).

#### 2.10 Readiness (as found)

- Commercial now: RAS (tilapia, salmon smolt), mealworm and BSF farms, mycoprotein (Quorn), mushrooms, microalgae (high-value), broilers/dairy/rabbits, methanotroph feed SCP (China plant).
- Approved, very small volume: cultivated meat (Singapore, US); Solein (Solar Foods; approval status not checked here).
- Modeled only: PV-to-SCP at farm scale (Leger 2021).

**Q2 search-log lines are in Section 4.**

### Q3. Closed-loop recycling of N, P, K and water

#### 3.1 What one person excretes per year (the recoverable pool)

**Viskari, Grobler, Karimäki, Gorbatova, Vilpas, Lehtoranta (2018), "Nitrogen Recovery With Source Separation of Human Urine—Preliminary Results of Its Fertiliser Potential and Use in Agriculture," *Frontiers in Sustainable Food Systems* 2:32, DOI 10.3389/fsufs.2018.00032 (PDF read). Table 1, citing Weckman 2005, Udert et al. 2006, Finnish Ministry of the Environment 2017.** SOURCED, kg per person per year:

| Stream | N | P | BOD |
|---|---|---|---|
| Urine | 4.13 | 0.40 | 1.83 |
| Faeces | 0.52 | 0.21 | 5.48 |
| Other (greywater) | 0.37 | 0.15 | 10.95 |
| Total | 5.02 | 0.75 | 18.25 |

- Alternative estimate (Vinnerås & Jönsson 2002, as cited there): 3.7 kg N, 0.34 kg P, 1.2 kg K per person per year recoverable from urine if fully separated.
- Share in urine: ~90% of N, 50–65% of P, 50–80% of K (Lapid 2008, as cited).
- Urine N up to 9 g/L, P ~0.7 g/L; N mainly urea/ammonium, P and K inorganic and plant-available.
- Hygiene: storage recommendation 6 months at >22 °C; a study cited there found 2 months at >20 °C sufficient when N >2 g/L and pH >8.8. About 2/3 of pharmaceuticals leave the body in urine.
- Field result: urine was "as efficient as a mineral fertiliser" for barley in Finland.
- Humans excrete 1.6–1.7 g P per day, ~60% in urine (Etter et al. 2011, citing Schouw et al. 2002). COMPUTED: 1.6–1.7 g/d × 365 = 0.58–0.62 kg P/yr — consistent with the 0.75 kg total above.

**Crop-side demand (BVAD 2018, Q1 §1.3):** a hydroponic diet supplying 2,500 kcal/person/day needs **90–100 kg of fertilizer salt per person per year**, of which ">50%" could be recycled from inedible biomass (BVAD citing Lunn et al. 2017 and Strayer et al. 2002). SOURCED. The gap between ~5 kg N in excreta and the salt mass reflects that inedible biomass (harvest index 25–70%) also holds nutrients, plus counter-ions in the salts.

#### 3.2 Recovery technologies and their efficiencies

- **Struvite precipitation from urine (Etter, Tilley, Khadka, Udert 2011, "Low-cost struvite production using source-separated urine in Nepal," *Water Research* 45:852–862, DOI 10.1016/j.watres.2010.10.007; author PDF read):** reactor with external filtration removed **>90% of phosphorus** at 1.1 mol Mg per mol P, nylon filters ~160 µm, one hour treatment; sedimentation-only reactor 50%. Collecting spontaneously precipitated struvite/calcium phosphate could raise overall P recovery by ≥40%. Nitrogen and potassium stay in the effluent. SOURCED.
  - COMPUTED N captured by struvite: struvite holds N:P = 1:1 molar = 14:31 by mass. Recovering 90% of 0.40 kg urinary P = 0.36 kg P → 0.16 kg N = **~4% of the 4.13 kg urinary N**. Struvite alone is a phosphorus route, not a nitrogen route.
- **Nitrification (MELiSSA compartment III): Garcia-Gragera, Arnau, Peiro, Dussap, Poughon, Gerbi, Lamaze, Lasseur, Gòdia (2021), "Integration of Nitrifying, Photosynthetic and Animal Compartments at the MELiSSA Pilot Plant," *Frontiers in Astronomy and Space Sciences* 8:750616 (read).** SOURCED: packed-bed bioreactor with *Nitrosomonas europaea* and *Nitrobacter winogradskyi* on polystyrene beads; ammonium conversion maintained at **100%** over the 276-day liquid-connection phase and **99%** in the 110-day gas+liquid phase; outlet nitrate 274.8–289 ppm N; feeding the cyanobacterium *Limnospira indica* (photobioreactor, 0.9–2.2 g/L); O2 production 1.4–2.76 g/h (up to 3.4–3.8); rats as crew mock-up. No whole-loop closure percentage reported.
- **Composting nitrogen losses (search summaries; primary pages 403):** unamended poultry manure NH3 loss 47–62% of total N; chicken litter composting >half (59%) of initial N; food-waste composting ~50% of initial N; pig manure 20.7–28.2%. UNVERIFIED. If accepted, composting is the leakiest N route found.
- **Anaerobic digestion:** total N little changed by digestion, organic N mineralized to ammonium; K unchanged; P mostly precipitates in the particulate fraction (search summary of Möller & Müller 2012, *Engineering in Life Sciences* 12:242–257, DOI 10.1002/elsc.201100085; Wiley 403). UNVERIFIED.
- **Urine distillation (Lunar Palace, below): 99.7% N recovery** — SOURCED.

#### 3.3 Real closed systems: what closed and what leaked

**BIOS-3, Krasnoyarsk (Institute of Biophysics web page, ibp.ru, read):** 315 m³ steel structure, 4 compartments, up to 3 crew; 20 kW xenon lamps per compartment; facility "used 400 kW of electricity"; 8 m² of exposed Chlorella per person balanced O2/CO2; by 1968, "99% by recycling the air, 85% by recycling water and about 50% by recycling food and nutrients"; trace gases burned "at 600°C in the presence of a catalyst"; 10 manned closures, longest 180 days with 3 crew (1972–73); "dried meat was imported"; "urine and feces were partially recycled and partially dried and stored." SOURCED. Nelson & Dempster (1996, below) add: hydroponic cropping area "about 400 square feet" (≈37 m², COMPUTED), crops met "about half" of nutritional needs, human wastes except some urine were exported. Wikipedia (not used as a source) gives 95% water; Lunar Palace authors cite 48% food regeneration for a 90-day BIOS-3 run.

**Biosphere 2, Arizona, 1991–1993 (Nelson & Dempster, "Living in space: results from Biosphere 2's initial closure, an early testbed for closed ecological systems on Mars," 1996, AAS/Case for Mars proceedings; PDF read via gwern.net):** SOURCED:
- 8 crew, 2 years; 2,000 m² agriculture produced "about 80%" of nutritional needs; with 3 months of pre-closure stored food, intake averaged ~2,200 kcal, 73 g protein, 32 g fat per person per day; 10–20% weight loss, mostly in year one.
- Light was limiting: glass and structure cut incident light 50–60%; El Niño cloud years; artificial lights were added later.
- Oxygen fell from 20.9% to ~14% after 16 months; oxygen was injected (jump to ~19%). Cause: microbial respiration in organic-rich soils, with the CO2 sequestered by the structural concrete (Severinghaus et al. 1994): CO2 + Ca(OH)2 → CaCO3 + H2O. CO2 scrubber accounted for only ~1.6% of O2.
- Air leak rate ~5–10% per year (NASA's BPC leaked 10% per day, per the Biosphere Foundation summary).
- Wastes treated by microbial + constructed-wetland systems; water from the "ocean" condensed for drinking (Biosphere Foundation, *Scientific and Engineering Accomplishments 1991–1993*, read; advocacy document by participants).
- Labor: agriculture/food was "the largest component requiring about 45% of total work hours" (Nelson & Dempster 1996). SOURCED.

**Lunar Palace 1 "Lunar Palace 365," Beihang University (Fu, Yi, Du, Liu, Xie, Liu, "Establishment of a closed artificial ecosystem to ensure human long-term survival on the moon," bioRxiv preprint 10.1101/2021.01.12.426282, posted 2021-01-14; PDF read).** SOURCED:
- 370 days, 4 crew in the cabin at a time (8 volunteers in two rotating groups: 60 + 200 + 105 days); facility 160 m², 500 m³; gas leak 0.043%/day.
- Plant area 120 m² (three tiers), 35 species (5 food crops, 29 vegetables, 1 fruit); one cabin lit 24 h at 300–800 µmol/m²/s.
- Yellow mealworms fed on straw/leaves supplied animal protein.
- **O2 and water: 100% regenerated, "no external water input."** Crew water consumption 74.37 kg/d per 4-person group; plant transpiration 724.26 L/d = 6.13 L/m²/d.
- **Urine: 99.7% recovery** (distilled under low pressure after biological pretreatment; residual "urine slag" stored). **Solid waste: 67%** (fermentation of straw, feces, mealworm frass; vs 41% earlier).
- **Food: 73% regenerated by dry weight, 83% by fresh weight, 100% of plant food**. Comparison given by the authors: earlier 105-day run 55%; a 4-person 180-day Chinese experiment with 260 m² 55%; BIOS-3 90-day 48%; Japanese 2-person 28-day CEEF with 150 m² 92–95%.
- **System material closure degree 98.2%.**
- Simulated power-loss tests: CO2 rose, recovered 12–24 h after power restored.
- COMPUTED: 120 m² ÷ 4 people = 30 m² of lit growing area per person for 73% of food (dry weight).

**International Space Station water (NASA, "NASA Achieves Water Recovery Milestone on International Space Station," 2023-06-20, read):** total water recovery 98% with the Brine Processor Assembly vs 93–94% before; "Let's say you collect 100 pounds of water on the station. You lose two." Each crew member needs about 1 gallon of water daily (as stated in the article). SOURCED. BPA by May 2024: 41 runs, 612 days, ~741 kg water recovered from urine brine (search summary of a 2024 ICES paper; repository 403) — UNVERIFIED.

#### 3.4 Make-up inputs per person per year (COMPUTED, with stated assumptions)

These are arithmetic illustrations from the sourced recovery rates above, not measurements.

- **Nitrogen, excreta loop only.** Assumption: steady-state adult excretes what they eat, 5.02 kg N/yr (Viskari Table 1).
  - Lunar Palace urine route (99.7%) on the 4.13 kg urinary N, plus 67% recovery on the 0.89 kg faecal + greywater N: loss = 4.13 × 0.003 + 0.89 × 0.33 = 0.012 + 0.29 = **≈0.30 kg N/yr make-up**.
  - Composting everything at ~50% N loss (UNVERIFIED rate): 5.02 × 0.5 = **≈2.5 kg N/yr**.
  - Struvite only: ≈4.9 kg N/yr not captured (only ~0.16 kg N captured).
- **Phosphorus:** struvite at 90% on urinary 0.40 kg P plus no recovery from faeces/greywater (0.36 kg): loss = 0.04 + 0.36 = **≈0.40 kg P/yr**; with 67% solid-waste recovery as in Lunar Palace: 0.04 + 0.36 × 0.33 = **≈0.16 kg P/yr**.
- **Whole-diet fertilizer:** BVAD 90–100 kg salt/person/yr with ">50%" recyclable → **< 45–50 kg fertilizer salt/person/yr make-up** at 50% recycling (upper bound on make-up).
- **Water:** applying ISS's 2% loss to Lunar Palace's domestic use (74.37 kg/d ÷ 4 = 18.6 kg/person/d): 18.6 × 0.02 × 365 = **≈136 kg water/person/yr** make-up. Lunar Palace itself reported zero external water over 370 days.
- **Oxygen/atmosphere:** depends on leak rate and on unplanned sinks (Biosphere 2 concrete). Lunar Palace 0.043%/day leak = COMPUTED ~15.7%/yr of cabin air volume (0.043 × 365, simple sum, ignoring compounding).

**Q3 search-log lines are in Section 4.**

### Q4. Per-person budgets (computed)

#### 4.1 Daily needs (SOURCED)

- Protein: safe level 0.83 g per kg body weight per day for adults (97.5th percentile of requirement; 133 mg N/kg/d) — FAO/WHO/UNU (2007), *Protein and amino acid requirements in human nutrition*, WHO Technical Report Series 935 (iris.who.int/handle/10665/43411; value confirmed in search summaries of the report, report itself not opened → treat as SOURCED-secondary).
- Energy: NASA BVAD (2018) uses 12.707 MJ = 3,037 kcal per crew member per day for current planning (raised from 11.82 MJ); its fertilizer projection uses 2,500 kcal/person/day; its RDA goal column lists 2,000 kcal and 50 g protein. Biosphere 2 crew averaged ~2,200 kcal, 73 g protein, 32 g fat and lost 10–20% body weight (Nelson & Dempster 1996). FAO derives country-specific minimum dietary energy requirements by age, sex and activity (FAO SOFI methodology notes; no single number taken).
- BVAD's "Diet Using All ELS Crops" (65.29 m² per crew member, Q1 §1.3) supplied only 7.74 MJ/day (≈1,850 kcal) and 54.91 g protein against an 11.82 MJ goal (BVAD Table 4-65). SOURCED. COMPUTED: scaled to 2,500 kcal (10.46 MJ): 65.29 × 10.46 / 7.74 = **88 m² per person** on the BVAD crop list.

#### 4.2 Assumptions for the computed budgets (all stated; change any one and rerun)

| Item | Value | Basis |
|---|---|---|
| Energy intake | 2,500 kcal/person/day | BVAD fertilizer-projection basis |
| Protein target | 60 g/person/day | ASSUMPTION: 0.83 g/kg/d × 72 kg body mass |
| Crop productivity | BVAD Table 4-97 nominal edible g FW/m²/d | SOURCED |
| Light per crop | BVAD Table 4-96 PPF, mol/m²/d (potato 28, wheat 115, soy 28, lettuce 17, tomato 27) | SOURCED |
| Food composition | USDA SR Legacy (Apr 2018): potato 77 kcal & 2.05 g protein/100 g; wheat (hard red winter) 327 & 12.61; soybean 446 & 36.49; lettuce (green leaf) 15 & 1.36; tomato 18 & 0.88; tilapia raw 96 & 20.08 | SOURCED (dataset downloaded and parsed) |
| LED efficacy | 3.0 µmol/J (best blue+red commercial fixture), sensitivity 2.78 µmol/J (best white+red) | SOURCED: Kusuma, Pattison & Bugbee (2020), "From physics to fixtures to food: current and potential LED efficacy," *Horticulture Research* 7:56 (PMC7105460, read). HPS 1,000 W fixture 1.72 µmol/J; technology limits 3.4 (white+red) and 4.1 (blue+red) |
| Electricity counted | **Lighting only** for crops, plus listed process loads for SCP/RAS/insects | HVAC, pumps, dehumidification, processing NOT included — see cross-check |
| Harvest/processing losses | none | ASSUMPTION (understates area) |
| Diet mix (a) | kcal: potato 70%, wheat 15%, soybean 10%, lettuce 2.5%, tomato 2.5% | ASSUMPTION (illustrative) |
| Diet mix (b) | 40 g/d protein from H2-oxidizing SCP (65% protein, 28–42 kWh/kg DW, Q2 §2.1); SCP counted as 160 kcal (4 kcal/g protein, ASSUMPTION); crops supply the remaining 2,340 kcal as potato 80%, wheat 15%, vegetables 5% | ASSUMPTION |
| Diet mix (c) | 20 g/d protein from tilapia fillet + 10 g/d from mealworms; crops supply remaining kcal (potato 80%, wheat 15%, vegetables 5%) | ASSUMPTION |
| Tilapia | fillet yield 35.7% (Rutten, Bovenhuis & Komen 2004, *Aquaculture* 231:113–133, abstract read); feed 1.22 kg/kg fish; RAS electricity 1.8–2.2 kWh/kg; heat 0–3.4 kWh/kg (Eding et al. 2009 via Martins 2010) | SOURCED |
| Mealworm | 0.197 kg edible protein per kg fresh (COMPUTED from Oonincx & de Boer 2012: 34 MJ/kg fresh ÷ 173 MJ/kg edible protein); FCR 2.2; on-farm gas+electricity = 43% of 34 MJ/kg fresh | SOURCED / COMPUTED |
| Animal feed | grown as wheat-equivalent by mass under lights (main case); potato-equivalent by dry matter (sensitivity) | ASSUMPTION |
| Floor area | growing area ÷ 5 tiers | ASSUMPTION (BVAD crop heights 0.25–0.65 m make multi-tier racks physically plausible, but no tier count was sourced) |

#### 4.3 Per-crop lighting cost (COMPUTED, 3.0 µmol/J; in parentheses 2.78)

Arithmetic: lighting kWh/m²/d = PPF (mol/m²/d) ÷ efficacy (µmol/J) ÷ 3.6. kcal/m²/d = g FW/m²/d × kcal/100 g ÷ 100.

| Crop | kcal/m²/d | g protein/m²/d | Lighting kWh/m²/d | Lighting kWh per 1,000 kcal |
|---|---|---|---|---|
| Potato | 81.1 | 2.16 | 2.59 (2.80) | **32.0 (34.5)** |
| Wheat | 74.3 | 2.87 | 10.65 (11.49) | 143.3 (154.6) |
| Soybean | 22.5 | 1.84 | 2.59 (2.80) | 115.3 (124.5) |
| Lettuce | 19.7 | 1.79 | 1.57 (1.70) | 79.9 (86.2) |
| Tomato | 31.3 | 1.53 | 2.50 (2.70) | 79.9 (86.3) |

Whole-facility cross-checks (all electricity, SOURCED inputs, COMPUTED conversion):
- Potato via Lovat et al. 2025 (≈250 kWh per kg dry matter) and BVAD potato dry-matter fraction 21.06/105.30 = 0.20: 770 kcal/kg FW ÷ 0.20 = 3,850 kcal/kg DM → **65 kWh per 1,000 kcal**, i.e. about **2× the lighting-only figure**. Per person at 2,500 kcal/d: 59,300 kWh/yr = 6.8 kW.
- Lettuce via Karpe et al. median 18 kWh/kg and USDA 150 kcal/kg: **120 kWh per 1,000 kcal** (whole facility).
- EDEN ISS lettuce 115–310 kWh/kg → 770–2,070 kWh per 1,000 kcal (small sealed module; not a scale reference).

#### 4.4 Results per person and scaled (COMPUTED; lighting-only for crops unless stated)

Script: `q4.py` in the session scratchpad (inputs exactly as in 4.2). Values at 3.0 µmol/J; 2.78 µmol/J in parentheses.

| Scenario | Growing area m²/person | Crop protein g/d | Electricity kW/person (continuous) | 100,000 people | 1,000,000 people |
|---|---|---|---|---|---|
| (a) Soilless crops only | 42.9 | 90 | 6.19 (6.68) | 619 MW (668); 4.29 km² growing, 0.86 km² floor at 5 tiers | 6.19 GW (6.68); 42.9 km² growing, 8.6 km² floor |
| (b) Crops + H2-SCP (40 g protein/d) | 32.6 | 72 (+40 from SCP) | 5.05–5.09 (5.44–5.48) | 505–509 MW (544–548); 3.26 km², 0.65 km² floor | 5.05–5.09 GW (5.44–5.48); 32.6 km², 6.5 km² floor |
| (c) Crops + tilapia RAS + mealworms, feed as lit wheat | 53.4 | 74 (+30 animal) | 13.97 (15.08) + 346 kWh/yr heat | 1.40 GW (1.51); 5.34 km², 1.07 km² floor | 14.0 GW (15.1); 53.4 km², 10.7 km² floor |
| (c′) same, feed as lit potato (dry-matter basis) | 52.4 | 74 (+30 animal) | 7.19 | 719 MW; 5.24 km² | 7.19 GW; 52.4 km² |

Breakdown notes (COMPUTED):
- (a): potato 21.6 m², 56.0 kWh/d; wheat 5.05 m², 53.7 kWh/d; soybean 11.1 m², 28.8 kWh/d; vegetables 5.2 m², 10.0 kWh/d. **Wheat gives 15% of calories but takes 36% of the lighting; soybean gives 10% of calories but 26% of the area.**
- (b): SCP 22.5 kg DW/person/yr × 28–42 kWh/kg = 629–943 kWh/yr (0.07–0.11 kW). SCP's electricity is small next to crop lighting; its saving comes from removing soybean (low kcal/m²) from the crop mix.
- (c): 101.8 kg whole tilapia/yr (124.2 kg feed) and 18.5 kg mealworms/yr (40.8 kg feed) need 19.9 m² of lit wheat-equivalent (211.8 kWh/d lighting) — the feed, not the RAS (183–224 kWh/yr) or the insect farm (75 kWh/yr), dominates.
- Adding non-lighting loads: if the whole-facility ratio found for potato (≈2× lighting) holds generally, multiply the electricity column by ~2 (e.g. (a) ≈ 12–13 kW/person, ≈1.2–1.3 GW per 100,000 people). This doubling is an inference from one crop's cross-check, not a sourced factor.
- Comparison with sourced closed-system practice: Lunar Palace 365 used 30 m²/person for 73% of food (DW); BIOS-3 ~37 m² for 3 people for ~half of food; Biosphere 2 250 m²/person (2,000 m² ÷ 8, sunlit soil) for ~80%; BVAD all-crop diet 88 m²/person scaled to 2,500 kcal.
- Nutritional completeness of (a)–(c) was not checked beyond energy and total protein (fat is low in (a)/(b); micronutrients not assessed).

**Q4 search-log lines are in Section 4.**

### Q5. Storage, seed and reserves

#### 5.1 Seed (orthodox seeds): FAO international standard

**FAO (2014), *Genebank Standards for Plant Genetic Resources for Food and Agriculture*, rev. ed., Rome (i3704e.pdf, read via pdftotext).** SOURCED:
- 4.2.1 Dry seeds "to equilibrium in a controlled environment of 5–20 °C and 10-25 percent of relative humidity, depending upon species."
- 4.2.2 Seal in airtight containers after drying.
- 4.2.3 Base collections (most-original samples and safety duplicates): **–18 ± 3 °C, 15 ± 3% RH.** 4.2.4 Active (medium-term) collections: **5–10 °C**, 15 ± 3% RH.
- Avoid exposure above 30 °C or 85% RH during handling.
- Initial germination should exceed **85%**; regenerate when viability drops below **85% of initial**.
- Minimum accession size: **1,500 seeds for self-pollinated, 3,000 for cross-pollinated species**; ≤50 acceptable for small wild accessions.
- Distribution (4.8.4): "a minimum of 30–50 viable seeds" per sample for most species; ship "carefully packed and sealed in airtight envelopes"; phytosanitary certificate and import permits as the recipient requires.
- Safety duplicate of every accession stored at a second, distant site (4.9).
- Cryopreservation (seeds, embryos, shoot tips, pollen) "usually that of liquid nitrogen (LN) at –196 °C"; vapor-phase storage at a maximum of –140 °C is described as more expensive and less safe.
- Seed longevity rule cited in a search summary ("for every 1% reduction in water content … longevity may double," Roberts & Ellis 1989 via a Frontiers 2020 paper) — UNVERIFIED.

**Svalbard Global Seed Vault (Crop Trust web page, read):** −18 °C; capacity 4.5 million samples; "more than 1.4 million seed samples from 134 institutions"; average 500 seeds per sample; "custom-made three-ply foil packages"; opened 2008; ICARDA withdrew samples in 2015–2019 after losing access to its Syrian genebank, regenerated them and re-deposited duplicates. SOURCED. Permafrost at −3 to −4 °C keeps samples frozen without power (search summary; UNVERIFIED).

#### 5.2 Breeding stock: animal germplasm

**FAO (2012), *Cryoconservation of animal genetic resources*, FAO guidelines, Rome (series number not checked; i3017e.pdf, read via pdftotext).** SOURCED:
- Storage in liquid nitrogen at −196 °C; transport in dry shippers (sanitizing protocol given).
- As few as 20–30 semen doses can have a rapid impact when introgressing a specific allele.
- Working collection for a single breed: 50–200 animals and 500–1,000 insemination doses.
- To reconstitute a breed of cattle, small ruminant or horse (Table 7): e.g. 100 founder females at 0.5 pregnancy rate need 564 doses (effective population 22); 200 females at 0.4 need 1,029 doses (Ne 23); 400 females at 0.4 need 2,058 (Ne 46).
- At least 20 doses per male for small-population management; "at least 100 doses per sire" in another use case.
- "Freezing the oocytes of avian and fish species has not been successful" (large, lipid-rich, polarized ova); poultry and fish rely on semen, primordial germ cells (recent success in chickens) or live populations. Somatic-cell banking (e.g. ear tissue) as a backup for cloning.

#### 5.3 Grain and dry food shelf life

- **Wheat in No. 10 cans, low oxygen:** samples stored at ambient temperature from <1 to 32 years; well-sealed cans held <2% oxygen; kernel moisture 4.50–9.96%; bread acceptability 6.5–7.3 on a 9-point scale; "All samples maintained >70% acceptance for everyday use and >97% acceptance for use in emergency situations." Source: Green, Rose, Ogden, Pike (2005), IFT annual meeting poster, BYU ScholarsArchive facpub/32 (abstract read). SOURCED.
- **Wheat flour, low oxygen, No. 10 cans, 13–27 °C, 0.5–11 years:** oxygen <1%; moisture 12.0–14.3%; >90% (flour) and >88% (bread) emergency-use acceptance; free fatty acids rose with age. Dickey, Rose, Ogden, Pike (2004), IFT poster, BYU facpub/66 (abstract read). SOURCED.
- BYU's general finding that wheat and white rice "can last more than 30 years" when canned and stored properly (Church News/Deseret News 2008 reports, search summary only) — UNVERIFIED.
- **Bulk grain:** recommended long-term storage moisture "13.5 percent for wheat and corn, 12 percent for barley, 11 percent for soybeans"; allowable storage time "is reduced by approximately one-half for each 10-degree [°F] increase in grain temperature"; corn at 15% moisture keeps ~9 months at 60 °F, 5 at 70 °F, 3 at 80 °F. K. Hellevang, NDSU Extension, 2010-06-01 (read). SOURCED. Implication (from the rule, not a source statement): cold storage lengthens safe storage.

#### 5.4 Mass of a one-year food reserve per person

- **Space-food basis (BVAD 2018, Table 4-66, early Mars diets, 12.71 MJ ≈ 3,037 kcal/day):** dry mass 0.71–0.72 kg/CM-d; "as shipped" 0.99–1.48 kg/CM-d; packaging 0.26–0.29 kg/CM-d; locker 0.27–0.37 kg/CM-d. SOURCED. COMPUTED per year: as-shipped **361–540 kg** + packaging 95–106 kg + lockers 99–135 kg ≈ **555–781 kg per person-year** including containers (dry mass alone 259–263 kg).
- ISS observed: 1.83 kg/CM-d (Phase II containers) and up to 2.39 kg/CM-d (max 6-month rate) → COMPUTED **668–872 kg/person-year**. SOURCED inputs (BVAD text).
- **Bulk dry staple basis (COMPUTED):** 2,500 kcal/d × 365 = 912,500 kcal/yr. Hard red winter wheat 327 kcal/100 g (USDA SR Legacy) → **279 kg wheat/person-year**; long-grain white rice 365 kcal/100 g → 250 kg; dry soybeans 446 kcal/100 g → 205 kg. Packaging excluded. A grain-only reserve is not a complete diet (not assessed).
- Scaled (COMPUTED, wheat basis): 100,000 people → 27,900 t; 1,000,000 people → 279,000 t. At 13.5% moisture storage limits above.

#### 5.5 Starter materials for non-crop systems (shipping/storage)

- Insects: BSF facilities keep a breeding colony and produce "5-DOL" (5-day-old larvae) for each waste batch; a 35 t/week facility produces about 50 million 5-DOL per week; one egg weighs about 29 µg (Dortmans et al. 2021, read). SOURCED. Shipping/storage of insect eggs or pupae: NOT FOUND.
- Microbial cultures (SCP, mycoprotein, nitrifiers): storage method of production strains NOT FOUND in a read source (MELiSSA nitrifiers are immobilized on polystyrene beads in the reactor; Garcia-Gragera et al. 2021).
- Fish: FAO 2012 states fish oocyte freezing does not work; fish semen and live broodstock are the routes. Live fish/egg shipping specifics: NOT FOUND.

**Q5 search log (2026-10-25)**

1. `FAO Genebank Standards for Plant Genetic Resources 2014 orthodox seeds drying 10-25% relative humidity storage -18°C long-term moisture content` -> summary hit; two FAO PDFs found were 2021/2024 working documents (not the standards); then fetched i3704e.pdf from openknowledge.fao.org directly and read.
2. `Svalbard Global Seed Vault storage temperature -18 C permafrost capacity 4.5 million samples seeds per sample packaging foil` -> HIT; Crop Trust page read.
3. `FAO 2012 Cryoconservation of animal genetic resources guidelines semen doses embryos liquid nitrogen -196 shipping dry shipper storage per breed number of doses` -> HTML TOC only; full PDF (i3017e.pdf) downloaded and read.
4. `Brigham Young University study long-term storage hard white wheat 32 years sensory acceptability shelf life stored food rice 30 years Pike Jefferies` -> HIT; BYU facpub/32 and facpub/66 abstracts read; ndfs.byu.edu research list read (no shelf-life numbers). Full papers not opened.
5. `safe storage moisture content wheat corn bulk storage allowable storage time temperature extension table 13% moisture years` -> HIT; NDSU 2010 release read. Full AST tables (Missouri, Sukup PDFs) not opened.
6. BVAD 2018 re-read for packaged-food masses (Tables 4-53, 4-66 text).

### Q6. Power and heat at high latitudes

#### 6.1 Measured energy loads, cold-climate and polar food production (kWh per m² per year)

| Site / system | Latitude band | Heat | Electricity | Basis | Status |
|---|---|---|---|---|---|
| Netherlands, whole greenhouse sector, 2022 | ~52° N | — | — | **0.8 GJ/m² total = 222 kWh/m²** (≈1.13 GJ = 314 kWh/m² in 2021) | SOURCED (Smit 2023, Q1 §1.4) / COMPUTED conversion |
| Finland, all greenhouse enterprises, 2021 | 60–64° N | 1,087 GWh → **290 kWh/m²** | 619 GWh → **165 kWh/m²** | total 1,706 GWh over 375 ha → **455 kWh/m²** | SOURCED totals (Luke, *Horticultural statistics 2021: energy consumption in greenhouse enterprises*, 2022-03-15; area from *Horticultural statistics 2021*, 2022-02-24) / COMPUTED per m² (assumes all reported energy is for the 375 ha) |
| Finland, lit cucumber (Kaukoranta, Näkkilä, Särkkä, Jokinen 2014, *Agricultural and Food Science* 23(3); abstract read) | ~60° N | 10–25 MJ/kg (spring), 3–8 (summer), 10–18 (autumn–midwinter) | 20–50, 17–30, 38–55 MJ/kg | per kg cucumber; lamps 170 W/m² above rows + 60 W/m² inter-row | SOURCED. COMPUTED: 38–55 MJ = 10.6–15.3 kWh/kg electricity in winter |
| Chena Hot Springs, Alaska, 6,000 ft² (557 m²) hydroponic NFT greenhouse (Mager, *Economics of greenhouse production in Alaska…*, Univ. Alaska Fairbanks, NRF Open Assembly 2008; PDF read) | ~65° N | heating "approximately 500,000BTU/h" Oct–Mar (=146.5 kW); annual heat cost $23,650 at $9.38/MMBtu → 2,521 MMBtu = 739 MWh → **1,327 kWh/m²** | 62 kW, 16 h/day, 48 × 1,000 W lamps; $30,200/yr at 10¢/kWh → 302 MWh → **542 kWh/m²** (756 per m² of the 4,300 ft² production area) | inside 78 °F with outside −56 °F | SOURCED inputs / COMPUTED per m² |
| Friðheimar, Iceland, tomatoes | ~64° N | geothermal hot water | HID lamps, grid from hydro and geothermal plants | 4,200 m², ~10,000 plants, "about one ton of tomatoes a day, 365 days a year" | SOURCED (hortidaily article, read). COMPUTED: ≈365 t / 4,200 m² ≈ 87 kg/m²/yr. Energy per m²: NOT FOUND. "1,200 kWh/m²" for Icelandic greenhouses and "216 GWh/yr" geothermal: search summaries only → UNVERIFIED |
| South Pole Food Growth Chamber (Patterson, Giacomelli, Kacira, Sadler, Wheeler 2012, *Acta Horticulturae* 952:589–596; abstract read) | 90° S | inside station envelope | **281 kWh/day** (1,012 MJ) | 2.8 kg edible/day, CO2 1.1 kg/d, fertilizer salts 0.21 kg/d, O2 0.52 kg/d (Jan–Oct 2006) | SOURCED. COMPUTED: 281 ÷ 2.8 = **100 kWh/kg**; production room ~23 m² (Giacomelli slides, read) → ~12.2 kWh/m²/d ≈ **4,460 kWh/m²/yr**. Giacomelli: "10 – 13 g per kWh" edible (SPFGC vs lunar greenhouse prototype) |
| EDEN ISS, Neumayer III, Antarctica (Q1 §1.2) | 70.7° S | included in electric (thermal control 0.080 kW/m²) | 0.8 kW/m² average (season), 0.532–0.690 kW/m² by crop | COMPUTED: 0.8 × 8,760 = **≈7,000 kWh/m²/yr**, all electric | SOURCED / COMPUTED |
| Salmon post-smolt RAS, Norway | ~60° N | "at least one-third" of demand is heating freshwater | 9.586 kWh/kg fish total | — | SOURCED (secondary, Q2 §2.8) |

- Claimed Nordic heating bands ("430 to 650 kWh/m²/y" at 50–60° latitude; "1,900 MJ/m²" = 528 kWh/m² for Scandinavia) came only from search summaries; the AIDIC paper the search pointed to is about Italian nurseries and contains neither figure → **UNVERIFIED, not used.**
- Greenland, Svalbard, Canadian Arctic (e.g. Nunavut) greenhouse heating loads: NOT FOUND (not searched in depth; see open threads).

#### 6.2 Power sources actually used (as found)

- **Geothermal (heat and electricity):** Chena Hot Springs: buildings heated with geothermal water; greenhouse heat from 155 °F water from a shallow well; electricity from a **400 kW geothermal power plant** that replaced a 400 kW diesel generator and cut power cost "from 30¢/kW to approximately 6¢/kW" (Mager 2008, SOURCED; "¢/kW" as written, i.e. per kWh). Iceland (Friðheimar): geothermal hot water heat, lighting from "the island's 42 hydro and geothermal power plants" (SOURCED, trade press). Netherlands: geothermal (aardwarmte) and biofuels the main renewable sources; renewables "ruim 15%" in 2022 (Smit 2023, SOURCED).
- **Natural-gas CHP:** dominant in Dutch greenhouses; growers sold CHP electricity and used the heat (Smit 2023, SOURCED).
- **Biomass:** Finland 2021: wood "energy chips" 311 GWh = most common heating fuel; purchased heat 274 GWh, half renewable; renewables 56% of heating energy; light fuel oil 54 GWh, heavy fuel oil 11 GWh (Luke 2022, SOURCED).
- **Diesel + wind (Antarctic station):** Neumayer III reportedly runs four 160 kW diesel generators (three in normal use; each 160 kW electric + 190 kW thermal) plus a 30 kW wind turbine (search summary of AWI material; the AWI page did not render the text) → **UNVERIFIED**. EDEN ISS drew on the station's supply.
- **Hydropower:** Iceland grid (above). Norway/Sweden hydro-supplied greenhouses: NOT FOUND in a read source.
- **Solar PV, Alaska:** a hydroponic business installed a 96 kW PV array in 2022 producing >89,000 kWh/yr (USDA Rural Development success story, search summary only) → UNVERIFIED. COMPUTED if accepted: 89,000 / (96 × 8,760) ≈ 10.6% capacity factor.
- **Nuclear:** Ågesta (Sweden) supplied Farsta district heating 1964–1974 (12 MW electric, 68 MW heat) and Bilibino (Chukotka) units are 12 MWe each with district heat up to 25 Gcal/h (search summaries) — **no read source shows nuclear heat used for greenhouses**. Pevek (Chukotka) greenhouse complex for floating-nuclear-plant workers, 210 t vegetables/yr, launch "autumn 2024" (ERDC news, read): its energy source is **not stated**. Nuclear-heated greenhouses: NOT FOUND.

#### 6.3 Heat recovery note (sourced mechanisms only)

- Mager (2008) frames greenhouses as a "productive use for the waste heat rejected from the power cycle," i.e. combined heat and power (SOURCED, as a proposal).
- In electrically lit sealed rooms, the lighting load is the dominant energy input (EDEN ISS atmosphere management 0.268 kW/m² exceeded lighting 0.121 kW/m² for lettuce; Zabel et al. 2020), so in closed systems heat is removed rather than added; in sunlit polar greenhouses (Chena, Finland) heat is the larger term.

**Q6 search log (2026-10-25)**

1. `greenhouse heating energy demand kWh per m2 per year Finland Norway Sweden Nordic greenhouse tomato cucumber year-round lighting energy use statistics` -> summaries; AIDIC PDF downloaded and read: wrong subject (Ancona nurseries) — the latitude-band figures are unsourced; Kaukoranta 2014 abstract read; MDPI Energies 2023 (16:6788) 403 -> DEAD AT SOURCE.
2. `Iceland geothermal greenhouses area hectares Friðheimar tomatoes energy use electricity lighting kWh per kg` -> hortidaily Friðheimar article read; ThinkGeoEnergy 2018 article read (no numbers); rafhladan.is PDFs (UNU-GTP SC-18-23, S14Paper071) 403/curl failure -> DEAD AT SOURCE.
3. `Alaska greenhouse heating energy study kWh per square foot year Alaska Center for Energy and Power hydroponic container farm energy use rural Alaska` -> Mager 2008 PDF read via pdftotext; USDA RD PV story snippet only.
4. `Chena Hot Springs geothermal greenhouse Alaska lettuce tomatoes power plant 400 kW organic rankine cycle greenhouse size` -> OIT GHC bulletin PDF 403 (DEAD AT SOURCE); 400 kW figure confirmed in Mager 2008.
5. `South Pole Food Growth Chamber Amundsen-Scott power consumption kW area m2 hydroponic University of Arizona CEAC Patterson Giacomelli` -> Patterson et al. 2012 abstract read; CEAC page read (no numbers); Giacomelli slides PDF read via pdftotext.
6. `Neumayer III station power supply diesel generators wind turbine kW EDEN ISS greenhouse energy supplied by station` -> summaries only; AWI page fetched twice (WebFetch and curl+parse) without the power text -> UNVERIFIED.
7. `Luke Finland greenhouse energy use 2021 survey electricity GWh heat GWh per hectare greenhouse area energy sources share` -> Luke energy statistics page read.
8. `Luke horticultural statistics 2021 greenhouse production area hectares Finland tomato cucumber area square metres` -> Luke 2021 statistics page read (375 ha).
9. `Orkustofnun geothermal direct use Iceland greenhouses 2015 TJ per year greenhouse area 194,000 m2 lighting electricity` -> no usable read source; Orkustofnun PDFs failed to download; south.is page read (no numbers). The "194,000 m2" in my query was my own guess at a search term, not a sourced figure, and is not used.
10. `nuclear power plant waste heat used for greenhouses example Bilibino Chukotka greenhouse OR "Ågesta" OR Kola nuclear greenhouse district heating vegetables` -> summaries; ERDC Pevek article read (energy source not stated).

---

## 3. NOT FOUND and open threads

**NOT FOUND (looked, nothing usable read):**
1. Peer-reviewed, same-crop, same-light yield comparison of NFT vs deep water culture vs drip-on-media vs aeroponics (Q1). Looked in: general searches; the potato minituber comparison (scielo 502) was the only lead.
2. Aquaponics energy per kg (Q1). UVI and SRAC primary PDFs failed (404/401/SSL).
3. Measured electricity per kg for Solar Foods' Solein and Calysta's FeedKind (Q2). Only company/news pages and the Sillman 2019 title were found.
4. Energy per kg for mycoprotein, precision-fermentation whey (absolute), raceway spirulina, mushrooms, and heated BSF facilities (Q2).
5. RAS stocking density from a read source (Q2).
6. Lighting vs HVAC split for commercial vertical farms, which is needed to replace the "≈2× lighting" inference in Q4 (Karpe preprint gives totals only).
7. Absolute recovery/leak rates for composting and anaerobic digestion from a read primary source (Q3). Pages returned 403.
8. Shipping and storage specifics for insect eggs/pupae, fish eggs or broodstock, and microbial production strains (Q5).
9. Per-m² energy for Icelandic, Norwegian, Greenlandic, Svalbard and Canadian-Arctic greenhouses (Q6). Orkustofnun/UNU-GTP PDFs failed to download.
10. Any read source showing nuclear heat used for greenhouses (Q6).

**Open threads (located, not opened, or unresolved):**
- EDEN ISS dedicated energy paper ("Energy and Power Demand of Food Production in Space based on Results of the EDEN ISS Antarctic Greenhouse," DLR elib 186936). It would refine §1.2.
- Stanghellini & Katzin (2024) original paper. Its 4.4 / 3.3 kWh/kg lettuce floors are carried only as cited by Karpe et al.
- Pennisi et al. 2025 (*Agronomy for Sustainable Development*, s13593-025-01055-w): 403/login.
- Sinke et al. 2023 (*Int J LCA*), the peer-reviewed version of the CE Delft cultivated-meat LCA.
- Leger et al. 2021: my bottom-up 28–42 kWh/kg DW does not reconcile with the paper's overall 0.4% efficiency (implying ≈70). The energy basis needs checking in the paper's SI.
- Cultivated-meat approval in Australia: a search summary and the FoodNavigator article disagree.
- Oonincx et al. 2015 FCR basis (dry-matter feed per fresh gain or otherwise) was not confirmed.
- WHO TRS 935 (protein 0.83 g/kg/d) was confirmed only through secondary summaries.
- Neumayer III power plant figures (4 × 160 kW diesel, 30 kW wind) are UNVERIFIED. The AWI page did not render.
- The ISS Brine Processor 2024 ICES paper (741 kg recovered, 612 days) returned 403.
- The Biosphere 2 figures come from participant-authored sources (Nelson & Dempster 1996; Biosphere Foundation). Severinghaus et al. 1994 (*Eos*) was not opened.
- Lunar Palace 365 is a bioRxiv preprint (2021). Its peer-reviewed version was not checked.
- Karpe et al. is a Research Square preprint posted 2026-09-09, not yet peer-reviewed.

---

## 4. Full search log

Format: `exact query` -> result (hit / dead end; if dead, died at QUERY or at SOURCES).


### Q1 search log (2026-10-25)

1. `vertical farm lettuce yield kg per m2 per year energy kWh per kg peer-reviewed` -> HIT (pointed to Karpe et al. preprint and an Agronomy for Sustainable Development 2025 review). Springer link (10.1007/s13593-025-01055-w) -> DEAD AT SOURCE (redirect to login). Pennisi et al. 2025 PDF at cris.unibo.it -> DEAD AT SOURCE (403). Its figures (60–105 kg FW/m²/yr; 0.08–0.13 kg/kWh; 140 g/L) seen only in snippet: UNVERIFIED, not used in tables.
2. `EDEN ISS Neumayer III greenhouse 2018 harvest kg total yield energy consumption results` -> HIT; DLR press release read.
3. Fetch elib.dlr.de/135982 -> HIT; PDF downloaded; WebFetch could not parse; extracted locally with pdftotext and read.
4. `Zabel "EDEN ISS" energy and power demand food production space kWh per kg edible biomass` -> partial; the dedicated energy paper (elib 186936, "Energy and Power Demand of Food Production in Space…") found by title only, NOT OPENED (see open threads).
5. `Graamans 2018 "Plant factories versus greenhouses" energy kWh per kg dry weight lettuce Sweden Netherlands UAE` -> HIT; WUR abstract read.
6. `quantitative review vertical farming productivity energy use efficiency median 62 kg m-2 lettuce 2025` -> HIT; Research Square HTML page empty to fetcher (DEAD AT SOURCE for HTML); PDF version downloaded and read with pdftotext.
7. arXiv 2507.18419 (Ceccanti et al., vertical-farm benchmark, Trondheim/Shanghai/Dubai) -> abstract read; only "lowest yields of 55 kg/m²" number in abstract; full text not read.
8. `Stanghellini Katzin 2024 "dark side of lighting" vertical farm greenhouse energy kWh per kg lettuce` -> partial; hortidaily article read: no numbers; links to OSF.
9. `Stanghellini Katzin "The dark side of lighting" Journal of Cleaner Production DOI` -> DEAD AT QUERY (no match). Original paper not located; its 4.4 and 3.3 kWh/kg figures carried only as cited by Karpe et al.
10. `Dutch greenhouse tomato yield kg per m2 per year lit vs unlit energy use m3 gas per m2 Wageningen` -> snippets only (25.4–37.8 m³/m²; 12 m³/m²); not opened -> UNVERIFIED.
11. `Asseng 2020 PNAS wheat yield potential controlled-environment vertical farms t/ha energy` -> HIT; PMC full text read.
12. `NASA Biomass Production Chamber wheat potato yield g m-2 day Wheeler Kennedy Space Center CELSS` -> HIT (titles, BPC totals in snippet).
13. `Wheeler "crop productivities and radiation use efficiencies" bioregenerative life support wheat potato soybean lettuce g m-2 d-1 edible` -> HIT; Wheeler 2015 slide PDF downloaded and read with pdftotext.
14. `indoor vertical farm wheat grain electricity kWh per kg calories energy analysis staple crops artificial light` -> HIT; Lovat et al. 2025 (PMC12225668) read. Substack/blog figures (650 kWh/kg wheat at 44% LED efficiency) seen in snippet only: not used.
15. `NASA Baseline Values and Assumptions Document BVAD crop growth area per crewmember m2 edible productivity table wheat potato soybean` -> HIT; BVAD 2018 PDF downloaded (simoc.space mirror) and Tables 4-96 to 4-100 read.
16. `KWIN glastuinbouw tomato production kg/m2 2020 high-wire greenhouse Netherlands average yield 70 kg` -> snippets only; KWIN itself not accessible (book) -> UNVERIFIED.
17. `aquaponics productivity kg fish kg vegetables per m2 per year UVI system Rakocy lettuce yield energy kWh per kg` -> snippets; ISTA-6 PDF 404 (DEAD AT SOURCE); UVI archive PDF 401 (DEAD AT SOURCE).
18. `Rakocy Masser Losordo 2006 SRAC 454 ...` -> found; okstate PDF failed SSL in both curl and WebFetch (DEAD AT SOURCE).
19. `FAO small-scale aquaponic food production Somerville 2014 feed rate ratio leafy greens ...` -> HIT; farmhub reproduction read; UVI principles page read.
20. `vertical farm capital cost per square meter growing area USD plant factory construction cost Japan Kozai` -> HIT; Zhuang et al. 2022 read. The "$277–347/m²" for a 48,000 m² Japanese factory in the search summary comes from a LEDinside news item: not opened, not used.
21. `Pythium root rot hydroponic NFT recirculating nutrient solution disease spread crop loss review` -> snippets; APS page 403 (DEAD AT SOURCE) -> UNVERIFIED.
22. `Dutch greenhouse horticulture energy use GJ per m2 per year Energiemonitor 2022 Wageningen average tomato heating` -> HIT; Energiemonitor 2022 PDF read with pdftotext. EECA NZ benchmarking PDF not opened.
23. `aeroponic potato minituber production tubers per plant compared hydroponic substrate study yield` -> snippets; scielo 502 (DEAD AT SOURCE) -> UNVERIFIED.

### Q2 search log (2026-10-25)

1. `Leger 2021 PNAS photovoltaic-driven microbial protein production land sunlight efficiency kWh per kg protein` -> HIT (press releases). Europe PMC REST lookup by DOI -> PMC8255800; full text read (two passes; final ~20k chars not read).
2. `Solar Foods Solein electricity consumption kWh per kg protein hydrogen-oxidizing bacteria life cycle assessment Järviö` -> DEAD AT QUERY for the LCA paper (no hit); company/blog pages only. Electricity per kg Solein NOT FOUND.
3. `Sillman 2019 bacterial protein renewable energy direct air capture land water use electricity MWh per tonne hydrogen-oxidizing bacteria` -> title/abstract only; full text not opened.
4. `Calysta FeedKind methanotroph Methylococcus capsulatus protein methane per kg yield commercial plant capacity tonnes` -> snippets (Wikipedia, Frontiers) -> UNVERIFIED.
5. `methanotroph single cell protein biomass yield g dry weight per g methane oxygen demand Norferm U-loop review` -> snippets only -> UNVERIFIED.
6. `Quorn mycoprotein Fusarium venenatum production energy LCA kg CO2 per kg Finnigan 2017 carbon footprint glucose conversion` -> PMC6554455 read (citation confirmed via Europe PMC); RSC Green Chem 2021 LCA -> DEAD AT SOURCE (403).
7. `spirulina microalgae open raceway pond areal productivity g m-2 day commercial annual t/ha energy kWh per kg` -> snippet; sapientia.ualg.pt PDF -> DEAD AT SOURCE (login page).
8. `"Spirulina" industrial productivity "5.1" g m-2 d-1 raceway seasonal annual Portugal commercial plant paper` -> title + summary only -> UNVERIFIED.
9. `microalgae photobioreactor commercial biomass production cost energy consumption kWh per kg dry biomass review Ruiz 2016 techno-economic` -> Tredici 2016 (flore.unifi.it) 403 and RSC Ruiz 2016 blocked (curl returned HTML) -> DEAD AT SOURCE; edepot.wur.nl/570707 (Vázquez-Romero 2022) read via pdftotext.
10. `Oonincx de Boer 2012 mealworm life cycle assessment energy use MJ per kg edible protein ...` -> HIT; PMC3526541 read.
11. `Oonincx 2015 feed conversion efficiency insects reared on diets composed of food by-products ...` and `"Feed Conversion, Survival and Development, and Composition of Four Insect Species" ...` -> HIT; PMC4689427 read (first 100k chars).
12. `black soldier fly larvae industrial rearing life cycle assessment energy kWh per kg larvae heating Smetana 2016 production per m2` -> DEAD AT QUERY for Smetana; only drying-energy snippets.
13. `black soldier fly larvae yield per square meter tray rearing density kg larvae per m2 per cycle waste reduction bioconversion rate` -> snippets; SLU link redirected (DEAD AT SOURCE).
14. `Diener Zurbrügg 2009 black soldier fly larvae feeding rate ...` -> Diener et al. 2009 (Waste Manag Res 27(6):603–610) located by citation only; Eawag BSF manual (2021) downloaded and read.
15. `Sinke 2023 ex-ante life cycle assessment cultivated meat 2030 energy MJ per kg ...` -> CE Delft 2021 report PDF read via pdftotext; Sinke 2023 Int J LCA not opened.
16. `recirculating aquaculture system energy consumption kWh per kg fish produced review Badiola 2018 salmon smolt RAS` -> Badiola 2018 review (Aquacult Eng 81:57–70) located; AZTI repository 404 and research.science.eus SSL error -> DEAD AT SOURCE; Badiola's 29.40 kWh/kg cod pilot RAS figure seen in snippet only (UNVERIFIED).
17. `"Current and Future Energy Use for Atlantic Salmon Farming in Recirculating Aquaculture Systems in Norway" kWh per kg` -> snippet; NTNU page 404; SINTEF 2024 report abstract read (no numbers); aquahoy news on Ayuso-Virgili 2023 read; munin.uit.no redirect -> DEAD AT SOURCE.
18. `Martins 2010 "New developments in recirculating aquaculture systems in Europe" ...` -> tepbac 404; Archimer author draft PDF downloaded and read.
19. `Ross 308 broiler performance objectives 2022 feed conversion ratio at 2.5 kg live weight days` -> Aviagen PDF downloaded and read.
20. `intensive rabbit meat production feed conversion ratio kg feed per kg live weight gain whole-farm FCR review` -> snippets; unipd 403 -> UNVERIFIED.
21. `dairy cow feed efficiency kg milk per kg dry matter intake typical 1.4 confined dairy high-producing review Journal of Dairy Science` -> Penn State extension (via dairyproducer.com) read.
22. `cultivated meat regulatory approvals list 2025 Singapore United States Australia ...` -> FoodNavigator 2026-02-18 read; Australia conflict unresolved.
23. `oyster mushroom Pleurotus biological efficiency ...` -> snippets; Mushroom Business article read.
24. `precision fermentation whey protein beta-lactoglobulin life cycle assessment energy MJ per kg Perfect Day 2021 study` -> Perfect Day blog read (relative values only).

### Q3 search log (2026-10-25)

1. `NASA ISS water recovery 98 percent Brine Processor Assembly 2023 Environmental Control Life Support System milestone` -> news hits; ICES 2024 BPA paper (ttu-ir.tdl.org) 403 -> DEAD AT SOURCE.
2. `nasa.gov "98%" water recovery space station Brine Processor Assembly June 2023 article` -> HIT; NASA page read.
3. `Lunar Palace 1 370-day experiment closure degree 98% food recycling Fu Liu 2016 Environmental Science Technology bioregenerative` -> HIT (bioRxiv). Full-text HTML returned 429 twice; PDF downloaded with curl and read via pdftotext. The 2016 ES&T paper on the 105-day run not opened.
4. `Jönsson Vinnerås 2004 guidelines on the use of urine and faeces in crop production nitrogen phosphorus potassium kg per person per year excreted` -> guideline PDF link not found on SLU page (DEAD AT SOURCE for the guideline itself); Viskari et al. 2018 (Frontiers) downloaded and read, which tabulates the figures.
5. `struvite precipitation from source-separated urine phosphorus recovery efficiency percent nitrogen recovery only small fraction Etter Udert` -> HIT; Etter 2011 author PDF read via pdftotext.
6. `BIOS-3 Krasnoyarsk closed ecosystem experiments 1972 180 days water oxygen food closure percent Gitelson results` -> HIT; ibp.ru page read. SIMOC-hosted 1997 BIOS-3 book PDF not opened.
7. `MELiSSA pilot plant compartments loop closure nitrogen recovery nitrifying compartment III conversion efficiency rat crew demonstration results` -> HIT; Frontiers 2021 (Garcia-Gragera et al.) read (first 100k chars). MELiSSA Foundation downloads not opened.
8. `Biosphere 2 oxygen decline 21% to 14.5% concrete carbonation Severinghaus 1994 food production crew diet calories 1991-1993` -> HIT; Biosphere Foundation PDF and Nelson & Dempster 1996 PDF read via pdftotext. Note: the "14.5%" figure in the query and in search summaries is not what Nelson & Dempster wrote ("around 14%"); the latter is used.
9. `composting nitrogen loss percent of initial nitrogen ammonia volatilization review manure food waste 16-74%` -> snippets; Tiquia & Tam (deepblue) 403 -> DEAD AT SOURCE -> UNVERIFIED. (The "16–74%" range in my query was my own phrasing, not a sourced figure; it is not used.)
10. `anaerobic digestion digestate nutrient fate nitrogen phosphorus potassium conserved mineralization ammonium fraction increase review Möller Müller 2012` -> citation confirmed (Hohenheim record); Wiley full text 403 -> DEAD AT SOURCE -> UNVERIFIED.

### Q4 search log (2026-10-25)

1. BVAD 2018 (already downloaded) re-read for crew energy and protein (Tables 4-63, 4-65, 4-67; text on 11.82 → 12.707 MJ/CM-d).
2. `WHO FAO UNU 2007 protein and amino acid requirements safe level 0.83 g/kg body weight per day adults technical report 935` -> HIT (summaries citing TRS 935; WHO IRIS record located, report PDF not opened).
3. `FAO minimum dietary energy requirement kcal per person per day world average 1,800 prevalence of undernourishment methodology average dietary energy requirement 2,300` -> methodology only; no single global figure taken. The "1,800" and "2,300" in my query were my own phrasing and are not used.
4. USDA FoodData Central API (DEMO_KEY) -> one result (potato), then OVER_RATE_LIMIT (DEAD AT SOURCE); WebFetch of the API -> 429. Workaround: downloaded the full SR Legacy CSV release (FoodData_Central_sr_legacy_food_csv_2018-04.zip) and parsed food.csv + food_nutrient.csv locally (nutrient IDs 1008 energy kcal, 1003 protein). "Sweet potato, raw, unprepared" not matched by exact description (not used).
5. `horticultural LED fixture photosynthetic photon efficacy µmol/J state of the art 2024 Kusuma Pattison Bugbee 2020 maximum` -> HIT; PMC7105460 read. MSU 2024 "Update on LED efficacy" PDF returned empty to the fetcher (DEAD AT SOURCE); its 2.71 µmol/J example not used.
6. `Nile tilapia fillet yield percent of whole body weight study 30-37%` -> HIT; Rutten et al. 2004 abstract read on WUR repository. (The "30–37%" in my query was my own bracket, not a source figure.)

### Q5 and Q6 search logs

Written inline at the end of the Q5 and Q6 sections in Section 2 (headed "Q5 search log" and "Q6 search log"), not repeated here.

### Tools note

PDFs that WebFetch could not parse were downloaded (WebFetch binary save or curl) to the session scratchpad and read with `pdftotext -layout`. USDA food composition came from the SR Legacy CSV release, parsed locally. The Q4 arithmetic script is `q4.py` in the session scratchpad.
