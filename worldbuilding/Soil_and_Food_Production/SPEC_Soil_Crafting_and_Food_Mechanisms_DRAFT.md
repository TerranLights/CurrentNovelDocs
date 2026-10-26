# Spec sheet: how usable soil is crafted, and the mechanisms by which a society makes food (DRAFT)

**Drafted 2026-10-25** at the developer's request: *"a spec sheet on how usable soil can actually be crafted so that we have mechanisms for how these various societies make their food."* **Status: DRAFT.** It is a menu of real mechanisms with real rates, so each settlement's food system can be derived from them instead of invented. It is not canon, and it is not for the timeline repo.

**Where the numbers come from.** Every figure below is taken from the three research files in `research/` (`G_…`, `H_…`, `I_…`) and keeps their status tag: **SOURCED** (read in the cited source), **COMPUTED** (arithmetic shown, assumptions stated), **UNVERIFIED** (seen only secondhand). Figures that this draft computed itself are marked **COMPUTED (this draft)** with the arithmetic. This draft was assembled from the three files' own summary tables; detailed sources, search logs and dead ends are in the files. **If a figure matters for a ruling, check it in the file first.**

---

## 1 · What "usable soil" means (targets)

| Property | Target | Source |
|---|---|---|
| Bulk density (roots restricted above) | below about 1.4 g/cm³ for loams; restriction above 1.47 (clay) to 1.80 (loam) | G #1, SDSU Extension 2023 |
| Air-filled porosity | at least 10% by volume | G #2, da Silva et al. 1994 |
| Available water | about 0.13 to 0.19 m³/m³ (loam, silt loam) | G #4, FAO-56 |
| Rooting depth | wheat 1.0–1.5 m; potato 0.4–0.6 m; lettuce 0.3–0.5 m | G #5, FAO-56 |
| Depth rated "highly suitable" | over 75 cm for cereals and vegetables | G #11 (UNVERIFIED against the original) |
| pH | about 6.0 for most crops; alfalfa 6.8; blueberry 4.8 | G #7, Univ. of Delaware 2024 |
| Salinity threshold (ECe, dS/m) | bean 1.0; maize 1.7; wheat 6.0; barley 8.0 | G #6, FAO Paper 29 |
| Cation exchange capacity | organic matter 200–400; sand 1–5; clay over 30 (meq/100 g) | G #8, UGA 2022 |
| Carbon to nitrogen of the microbes' diet | 24:1 (more carbon than that and microbes lock nitrogen up) | G #9, USDA NRCS |
| What counts as a built soil | a Technosol is 20% or more artefacts by volume in the top 100 cm; the WRB classes anything within 2 m of the surface, including soil in pots | G #12, IUSS WRB 2022 |
| Reference: terra preta | about 2.7 times the carbon of neighbouring soils | G #13, Glaser et al. 2001 |

Not found: a sourced target for organic matter percent in cropland (G, NOT FOUND list).

## 2 · The five things a crafted soil needs, and the real rates

| # | Need | How it is supplied | Real rate or limit | Source |
|---|---|---|---|---|
| 1 | **Mineral fines** (silt, clay) | Crushed rock, glacial flour, subsoil | Rock dust trials disagree by 40 to 400 times between studies; basalt dust at 50 t/ha/yr for 4 years raised yields 12–16% on existing farmland; glacial flour raised yield only with fertilizer | H #19, #20 |
| 2 | **Organic matter and carbon** | Compost, manure, biosolids, plant cover | The strongest real recipes use tens to hundreds of tonnes per hectare as a first dose | H #1, #8, #9 |
| 3 | **Nitrogen** | Legumes and other fixers, ammonia fertilizer, urine | Alfalfa fixes about 56–336 kg N/ha/yr; ammonia by electricity costs 12.2 MWh per tonne of N | G #24, #27 |
| 4 | **Living microbes** | Compost, inoculants, rhizobia-coated seed | Always came with the organic dose in the recipes found | H #6, #18 |
| 5 | **Water and salt control** | Irrigation, drains, runoff harvesting, gypsum | One depth of water per depth of soil removes about 70–90% of soluble salts; gypsum about 1.7 t/ha (15 cm) per cmolc/kg sodium replaced; drains 1.2–1.8 m deep at 30–150 m spacing | H #21, #22 |

**The pattern across the recipes** (H, summary): almost every documented rebuild of sterile ground paired a large one-off organic or nutrient dose, something to supply nitrogen, and water management. Water harvesting without nutrients gave almost nothing (under 100 kg/ha of sorghum).

**Fast start, slow finish.** Carbon on sterile substrates climbs steeply for about 5 to 8 years, then flattens. Without continued inputs, added organic matter can return near its starting level within about 10 years (H summary).

## 3 · The mechanisms

Each mechanism lists what it needs, what it gives, how long it takes, and what limits it. "Applies to" is design reasoning from the numbers, not research.

### M1 · Bulk organic dose on sterile ground (the compost or biosolids route)
- **Real case:** Egyptian desert sand (SEKEM): compost about 48–69 m³/ha per season, twice a year (about 59 t/ha/yr fresh). Soil carbon (0–50 cm) rose from 3.9 to 28.8–31.8 t C/ha in 30 years: 2.7–3.8 t C/ha/yr in years 1–5, then about 0.5. Crops in year 1. (H #8, SOURCED/COMPUTED)
- **Real case:** acid copper tailings in Arizona: biosolids 157–224 t/ha dry plus ground green waste and lime; grass biomass in 4–5 months; control zero. (H #1, SOURCED)
- **Needs:** thousands of tonnes of organics per square kilometer, continuous water, irrigation and drainage.
- **Limits:** erosion of bare new surfaces (131–292 t/ha/yr predicted, falling from 185 to 27 with 40% grass cover); contaminants carried in waste (metals, PFAS, microplastics, pathogens). (H #Q7)
- **Applies to:** anywhere with an outside organic supply and water.

### M2 · Water harvesting plus manure (the half-moon and zai pit route)
- **Real case:** Burkina Faso crusted ground: half-moons with 14.6 t/ha of manure gave 1,614 kg/ha sorghum; untreated gave 0; half-moons without manure gave 41. Zai pits take 300–700 labor hours per hectare. (H #9, #10, SOURCED)
- **Needs:** some rain or runoff, manure, hand labor.
- **Limits:** low yields; not a route to a large city's food.

### M3 · Nitrogen-fixing plant cover (the slow, cheap route)
- **Real case:** Iceland's lupine seeding, 5 kg seed/ha, no fertilizer; cover and nitrogen gain, but the lupine turned invasive and the agency stopped in 2018. Eroded desert reached about 55 t C/ha in 50 years with fertilizer or meat-and-bone meal; gains of 0.4–0.63 t C/ha/yr in the first 7 years, then a plateau. (H #6, #7)
- **Needs:** seed and rhizobia, a little time.
- **Limits:** decades; side effects.

### M4 · Engineered mix (the Technosol recipe)
- **Real case:** 70% excavated subsoil plus 30% compost by volume, 30 cm deep (20% compost in temperate climates, 40–50% in dry ones). Aggregation within 5 months; carbon stable in about 3 years. (H #14, review)
- **Needs:** a mineral source plus compost in the stated ratios.
- **Applies to:** small, intensive plots; it is the model for "cupped" soil in protected spaces.

### M5 · Regolith or barren rock made arable
- **Real cases:** Mars simulants grew lettuce at 30–70% compost by volume; lunar simulant grew chickpea at 25–75% simulant with vermicompost. The most accurate Mars simulant (MGS-1) failed, and so did simulant dosed with perchlorate. (H #16–#18, Q5)
- **Limits:** needs 30% to 75% organics; **no confirmed case of crushed rock with no existing soil becoming cropland** (G and H, NOT FOUND).
- **Status:** the closest analogs are heavy-organic mixtures, not true rock-to-soil conversion.

### M6 · Soilless protected cultivation (hydroponics, vertical farms, plant factories)
- **Real cases:** lettuce in vertical farms: median 62 kg/m²/yr, 18 kWh/kg, 15 L/kg across 11 studies (a 2026 preprint, not yet peer reviewed). Potato under lights: about 32 kWh per 1,000 kcal for lighting alone, about 65 for the whole facility (COMPUTED from NASA crop rates). Wheat: about 143. Dry staples: about 250 kWh/kg of dry matter. (I summary)
- **In Antarctica:** EDEN ISS used 115–370 kWh/kg; the South Pole chamber about 100 kWh/kg; none of the polar facilities grows staple calories. (I summary; G Q4)
- **Needs:** large, steady electricity; nutrient solution; pumps and spares. Several commercial vertical farms went bankrupt in 2023–25.
- **Applies to:** anywhere with cheap power and little arable ground.

### M7 · Food that does not need cropland
- Hydrogen-oxidizing bacteria protein: about 28–42 kWh/kg dry weight (unresolved up to about 70); early commercial. Microalgae in tubular reactors: 2.76 kg/m²/yr at 50.8 kWh/kg dry weight. Mealworm: about 9.4 kWh/kg fresh. Tilapia in recirculating tanks: 1.8–2.2 kWh/kg fish plus heat. Cultivated meat: about 41–73 kWh/kg in a 2030 model. (I table)
- **Not found:** energy per kg for aquaponics, mycoprotein, raceway spirulina, mushrooms and heated insect farms.

### M8 · Closed loops (recycling waste back into food)
- **Real cases:** Lunar Palace 365 (a 2021 preprint) recycled 100% of oxygen and water, recovered 99.7% of urine nitrogen and 67% of solid waste, and grew 73% of its food by dry weight on 30 m² per person. Biosphere 2's soils pulled oxygen down to about 14%. The ISS recovers 98% of water. (I summary; G failure cases)
- **Waste as input:** one adult excretes about 4.4–4.6 kg N and 0.55–0.58 kg P a year; urine diversion with fecal separation recovers about 60% of N, 46% of P and 43% of K; phosphorus can be recovered at 60–90% from sewage-sludge ash. (G #17, #22, #23)
- **Phosphorus cannot be made.** World phosphate rock reserves are 73,000 Mt; potash over 5,900 Mt K₂O (USGS 2026). (G #29, #30)

## 4 · Budgets: what feeding people costs

| Quantity | Value | Basis |
|---|---|---|
| Nutrients in the food of 100,000 people per year | about 437–455 t N, 55–58 t P, 120–180 t K | G #20, COMPUTED |
| Fertilizer-equivalent at world-average efficiency, 100,000 people | about 1,250–1,300 t N, 343–365 t P, 630–950 t K | G #21, COMPUTED |
| Biosolids from one person | about 21 kg dry solids per year | G #19, National Research Council 2002 |
| Land per person, soil-based | 250 m² for 81% of the diet (Biosphere 2); 1,300–10,800 m² on real US diets | G #35, #36 |
| Land per person, electric-lit closed systems | 40–56 m² | G #37, #38 |
| Soilless crops only, lighting only | about 43 m² and 6.2 kW per person: 4.3 km² and 0.62 GW per 100,000; 6.2 GW per million | I, COMPUTED |
| With hydrogen-bacteria protein | about 33 m² and 5.1 kW per person | I, COMPUTED |
| With fish and insects (fed on lit wheat / lit potato) | about 14 kW / 7.2 kW per person | I, COMPUTED |
| Whole facility | probably about twice the lighting figure (one-crop cross-check) | I, inference |

**Worked arithmetic from these numbers (COMPUTED (this draft), assumptions stated):**
- *How much of a city's own waste builds how much soil.* If a dose of 157–224 t/ha dry biosolids is needed to start (H #1) and a person yields 21 kg of dry solids a year (G #19), one hectare costs 157,000–224,000 kg ÷ 21 kg = about **7,500 to 10,700 person-years of sewage per hectare**. A town of 100,000 people makes 2,100 t a year, which covers about **9 to 13 hectares a year**. A city's own waste alone builds soil far more slowly than a city can eat.
- *The organic bulk for a soil-based district.* At the SEKEM rate (about 59 t/ha/yr fresh compost), 1 km² (100 ha) takes about 5,900 t of compost a year; 25 km² (the Biosphere 2 area for 100,000 people at 250 m²) takes about 147,500 t a year.

## 5 · How to derive a settlement's food system from this sheet

1. **Fix the population and calories** (2,500 kcal/day is the figure used by the research).
2. **List the constraints:** power available (MW); water; organic supply from outside; mineral source on site; temperature and light; how supplies arrive and how much per season.
3. **Pick a mix of mechanisms** from section 3 (usually M1 or M4 for a soil district, M6 for protected crops, M7 for protein, M8 for recycling).
4. **Compute the required area and power** with section 4, and the nutrients with section 4's N, P, K table.
5. **Compute the imports** (organics, fertilizer, phosphorus, seed, starter cultures) and check them against the settlement's real supply route.
6. **Check the time.** Section 2's fast-start, slow-finish curve says when the soil is productive.
7. **Name the failure modes** (section 3) that the settlement will have lived through.
8. **Mark anything unproven** (section 6) as unproven.

## 6 · What the research could not find (treat as unproven or open)

- A confirmed case of crushed rock with no existing soil becoming cropland (G and H).
- How long fresh crushed rock plus organics takes to work as soil, and hours per tonne of constructed soil (H).
- A sourced organic-matter target for cropland (G).
- Per-hectare nitrogen fixation for grain soybean and rice-field cyanobacteria (the ~30 kg/ha figure stays UNVERIFIED) (G).
- Biochar yield and energy from a primary source; perchlorate-washing efficiency; long-term degradation curves; the salinization rate of newly irrigated land (H).
- Water use of EDEN ISS; heating energy per m² for polar greenhouses; composting at any Antarctic station (F and I).
- Energy per kg for aquaponics, mycoprotein, raceway spirulina, mushrooms and heated insect farms; the split between lighting and climate control (I).
- Any confirmed case of nuclear heat for greenhouses (I).

## 7 · Source map

| File | Covers |
|---|---|
| `research/G_Soil_Targets_and_Nutrient_Budgets.md` | soil targets, classification of built soils, nutrient removal and waste, N P K supply, water, land per person (39-row key table) |
| `research/H_Constructed_Soils_Reclamation_and_Regolith.md` | 22 recipe rows from real reclamation, amendments, salt, speeding up formation, Mars and Moon simulants, labor, failure |
| `research/I_Soilless_Systems_Alternatives_and_Closed_Loops.md` | soilless crops, non-cropland protein, closed loops, per-person budgets, storage, power and heat |
| `research/_RESUME_PROTOCOL.md` | how the research agents recover from interruption |

The Relung Panen-specific research (the oasis ground, water and light; polar greenhouse precedents) is in the GDD's `Cities/Research_Logs/`: `Relung_Panen_Soil_Research_2026-10-25_E_…` and `…_F_…`.
