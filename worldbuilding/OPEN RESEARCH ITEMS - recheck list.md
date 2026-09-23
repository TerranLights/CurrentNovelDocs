# Open Research Items — Recheck List

2026-09-22. Everything across the nation material-base research that **failed, could not be verified, or rests
on something weaker than a source.** Consolidated here so none of it has to be rediscovered by re-reading nine
files totaling ~129,000 words.

**Why this file exists:** material only graduates to the `TepenianUniverseTimeline` repo once every open
question is closed. This is the list that has to reach zero for the North American nations. It is organized by
**how to retry**, not by topic, because the retry method is usually the blocker.

**Source files** (all in `nations/material-base/`): Alaska Republic base + 3 supplements, Cascadia base +
1 supplement, Colorado Republic, Midwestland, Sonora.

---

## 1. Read This Before Re-Running Anything

Four research passes hit the same walls. Knowing them up front is worth more than any individual item below.

### Domains that refused every request

| Domain | Failure | Affects |
|---|---|---|
| `yukon.ca`, `data.geology.gov.yk.ca`, `emrlibrary.gov.yk.ca` | Cloudflare | **All Yukon data** — placer gold, minerals, oil and gas |
| `gov.nu.ca` | 403 | Nunavut food prices, government statistics |
| `agnicoeagle.com`, `baffinfisheries.ca`, `nunavutfisheries.ca` | 403 / refused | Nunavut fisheries, Meliadine/Meadowbank |
| `alaskarailroad.com` | 403/404 | Railroad freight tonnage |
| `poa.usace.army.mil`, USACE Omaha, USACE Detroit | 403 / SSL failure | Port data, Missouri navigation, Soo Locks tonnage |
| `commerce.alaska.gov` | 403 | Alaska Fuel Price Report |
| `pce.akenergyauthority.org` | geo-blocked | Power Cost Equalization |
| `alaskabeacon.com`, `alaskapublic.org`, `cbc.ca`, `alaskabusiness.com` | 403 | 2026 news items |
| `newmont.com`, `transmountain.com` | 403 | Brucejack, Trans Mountain terminal |
| `nomealaska.org`, `sullivan.senate.gov` | 403/404 | Port of Nome expansion |
| `portofoakland.com` facts page | 404 | Oakland TEU |
| **EIA state-profile narrative pages** | JavaScript shell | *Use the underlying data files instead — they work* |
| `dog.dnr.alaska.gov/CIGasDashboard` | JavaScript app | Cook Inlet gas |

### Search engines are effectively unavailable

**DuckDuckGo, Mojeek, Bing, Brave, Ecosia and Startpage are all captcha- or JavaScript-walled** from this
environment. Two of four passes had their WebSearch budget (200 calls) **completely exhausted before starting**
and still produced strong work — because the fallbacks are good:

- **Direct `curl` + `pdftotext`** against known primary-source URLs. The single most productive method.
- **Wikipedia HTML / REST API.**
- **Google News RSS** — `https://news.google.com/rss/search?q=...` — as a search substitute. Returns obfuscated
  redirect links, so use it to *locate* a story, then go to the publisher's own site.

**Sites that reliably worked:** USGS (MCS PDFs), EIA data files, USDA NASS PDFs, NOAA Fisheries CSVs, ADF&G,
Alyeska's own PDFs, `portofalaska.com` PDFs, `dot.alaska.gov`, `kyuk.org`, `cabinradio.ca` (including its site
search), NRCan, Canada Energy Regulator, `nutritionnorthcanada.gc.ca`, Alaska DGGS.

### One document-specific trap

The **FY2025 Power Cost Equalization Statistical Report** PDF uses per-page subsetted fonts with no usable
ToUnicode map — it extracts as gibberish. **FY2023 extracts cleanly** and was used instead.

---

## 2. Highest Priority — Items That Change Conclusions

These are not loose ends. Each one determines whether a stated conclusion holds.

### ⚠️ Can these nations make iron? — three files independently converge on this

This turned out to be the most important unanswered question in the whole body of research, and it was raised
separately by three different passes that were not in contact with each other.

1. **Colorado Republic** — iron ore in Utah (Iron County) and Wyoming, and **whether any metallurgical/coking
   coal exists in the territory** (the Trinidad/Raton field?). Flagged in that file as "the highest-value
   follow-up in this list."
2. **Alaska Republic** — the state's own resource table **does not list iron at all**, and no cement plant
   could be verified. Also unresolved: **Klukwan iron-titanium** tonnage, grade and status (and note Klukwan is
   in the Panhandle, so Cascadian).
3. **NWT/Nunavut** — **whether Baffin Island or the eastern Arctic Islands hold workable coal.** Mary River is
   65–70% Fe direct-shipping ore but sits above the tree line with no fuel to smelt it. Called "the most
   consequential single unanswered question" in that file. Also: **Roche Bay**, a second Nunavut iron
   occurrence, never researched to resource level.
4. **Midwestland** — Minnesota's Mesabi Range is in-territory, but **Soo Locks tonnage and the Duluth-Superior
   cargo mix are unverified**, so the ore-movement picture is incomplete.

### ⚠️ Latin America — added 2026-09-23

- **The charcoal share of Brazilian pig iron.** The load-bearing question for whether South America can make
  iron without a coal industry. **Verified:** Brazil is the world's #1 charcoal producer (6.37 Mt, 2020, 11.8%
  of world output), 87.1% from plantations of which 98.8% is eucalyptus, and 82.8% of plantation charcoal comes
  from **Minas Gerais — the same state as the Iron Quadrangle**, with charcoal ironmaking still running in named
  towns. **Not verified:** the actual percentage of national pig iron made with charcoal rather than coke. The
  claim that Brazil leads the world in charcoal pig iron appears on pt.wikipedia **explicitly tagged as
  unsourced**; ResearchGate, MDPI, worldsteel and FAOSTAT all refused access. Try worldsteel's yearbook or
  Instituto Aço Brasil directly.
- **How the Panama Canal's gates and valves are actuated.** The locks themselves are **gravity-fed** from Gatun
  Lake with no pumping, including the Neopanamax reuse basins — but whether the machinery is electric,
  hydraulic or mechanical decides the canal's post-collapse fate, and it could not be established. *(Note the
  Panama Railroad crossed the isthmus for 59 years before the canal existed, so the crossing survives the locks
  either way.)*
- **Melissa Dell, "The Persistent Effects of Peru's Mining Mita" (2010).** PDF returned 403/404 on every mirror
  tried — scholar.harvard.edu, dash.harvard, MIT, the Econometric Society, Wiley. Abstract and effect sizes
  recovered via the **OpenAlex API** (~25% lower household consumption, ~6pp more child stunting inside the
  mita boundary). The full paper is the single best demonstration of colonial-institutional persistence across
  a sharp border and is worth obtaining properly.

### ⚠️ Other conclusion-changing items

- **TAPS full of crude.** What actually happens to a pipeline left holding **9,059,057 barrels** of waxy crude
  in an uncontrolled shutdown — restartability, timescale to permanent plugging. No source found anywhere.
  Named the most important gap in its file.
- **Colorado's ICBM basing and military target geography** — stated from general knowledge, **entirely
  unverified, and load-bearing for a nuclear-war premise.** This one decides which cities survive.
- **The American Nations cross-reference is now wrong.** Midwestland's §0 argues the re-scoped territory is not
  Woodard's Midlands but **Midlands + Yankeedom + Far West**. `extractions/American_Nations_to_New_North_America_Cross-Reference.md`
  needs amending. *(This is an action item, not a research gap.)*
- **Midwestland's post-collapse yield floor** rests on three numbers taken from model knowledge rather than
  documents: **legume nitrogen fixation rates (100–200 lb N/acre/yr)**, **draft-animal acreage limits (40–80
  acres per family, ~20–25% of cropland feeding the animals)**, and the **Beulah ND lignite-to-ammonia route**.
  Its own author flagged these as the load-bearing figures in §4.6.
- **⚠️ Yukon electricity — now the Alaska Republic's top research priority.** Whitehorse Rapids, Aishihik and
  Mayo hydro: capacity, age, operator, and how much of Whitehorse's load they carry versus diesel. **Whitehorse
  was settled as the national capital on 2026-09-22**, and whether the capital generates its own power or
  depends on imported diesel is the single most consequential unknown about it. Blocked by Cloudflare on
  `yukon.ca`; try Yukon Energy directly, NRCan, or the Canada Energy Regulator's territorial profile.
- **Military infrastructure in Alaska** (JBER, Eielson, Fort Wainwright, Clear, Fort Greely, Coast Guard
  Kodiak) — never researched, and **load-bearing for the capital decision**, since the argument for Whitehorse
  rests partly on Anchorage and Fairbanks being counterforce targets in 2083.
- **"95% of Alaska's food is imported"** — widely cited, **could not be verified.**
- **Cook Inlet physical conditions** — tidal range, silt load, winter ice at NOAA station 9455920. Called "the
  most important unresearched physical fact about the territory's main port."
- **The Shakwak Project** — US funding for the Yukon section of the Alaska Highway. Confirmed real via headlines
  (lapsed ~2019, partly resumed 2024, $7.2M in June 2025) but **no article could be read.** Directly relevant to
  whether the Whitehorse–tidewater route is maintained.

---

## 3. By Nation

### Alaska Republic

**Never researched:** traditional food preservation (drying, smoking, fermentation, ice cellars, seal oil) and
the historical sled-dog share of the salmon catch · geothermal entirely (Chena Hot Springs, Makushin, Mount
Spurr) · modern reindeer herding · Yukon oil and gas (Eagle Plain, Kotaneelee) · Yukon electricity (Whitehorse
Rapids, Aishihik, Mayo) · military infrastructure (JBER, Eielson, Fort Wainwright, Clear, Fort Greely, Coast
Guard Kodiak — five are cited as critical Railbelt loads) · rural water and wastewater (the "honeybucket"
problem) · timber and forest products.

**Could not retrieve:** Yukon placer gold annual ounces and operation counts · Cook Inlet and Western
Arctic/Chicago Creek coal tonnages · Alaska limestone quarrying, cement or lime production · Alaska clay ·
Lost River/Seward Peninsula tin · Goodnews Bay total platinum · Iditarod district production · Red Dog port
lightering and shipping-season window · Faro remediation total cost · Eagle Gold pre-failure production and
slide volume · IPHC halibut limits by area · Togiak herring tonnages · the Yukon treaty's seven-year term ·
Alaska DOL nonresident-worker share · processing-plant dependencies (ammonia refrigeration, can/tinplate
sourcing, diesel volumes, water) · at-sea fleet vessel counts · Ambler Road permit standing · Willow and Pikka
primary documentation · Cook Inlet gas volumes and reserves · gasoline supply split (Kenai vs. imported) ·
Petro Star/ASRC ownership and the Flint Hills North Pole closure · the 2026 Permanent Fund Dividend · giant
vegetable records · frost dates and soil survey · statewide heating-oil consumption and tank-farm capacities ·
Alaska Village Electric Cooperative.

**Transport-specific:** Alaska Railroad freight tonnage (only "4.3 million tons, 2015," second-hand) ·
rail-barge service details · Anton Anderson Tunnel schedule · Valdez Marine Terminal berths and tanker calls ·
Seward and Whittier tonnages · **Port of Nome expansion — the $400M / 40 ft / Kiewit figures come from
Wikipedia and RSS headlines only, re-source before use** · Alaska Fuel Price Report · population share off the
road system (the ~25% figure is inferred) · **AMHS current fleet and service levels — route descriptions rest
on 2008 data; do not describe current service from that file** · Whitehorse–Watson Lake and Terrace–Prince
Rupert distances (the two unverified legs of the novel's route) · Bypass Mail and Essential Air Service funding
· rural air carriers · rural fuel distributors beyond Crowley and Vitus · road maintenance and pavement
ratings · winter closures and avalanche control (Thompson Pass is absent entirely) · the Parks and Richardson
Highways, the territory's actual internal spine, get one line each.

**NWT/Nunavut:** Gahcho Kué production and reserves · Snap Lake's post-2015 status · Mary River current NI
43-101 reserves and shipped tonnages · Norman Wells production volumes · **Nunavut commercial fisheries in
full — turbot and shrimp quotas, landings, value (the single largest evidentiary gap)** · Arctic char harvest ·
the Great Slave Lake commercial fishery · **herd estimates for Beverly, Qamanirjuaq, Bluenose, Cape Bathurst,
Ahiak and Porcupine — do not generalize the Bathurst collapse without these** · marine mammal harvest quotas ·
Nunavut food prices by community · **sealift operators, tonnages and per-community open-water windows** · Izok
Lake and High Lake resources · Nechalacho, NICO, Prairie Creek, Kiggavik, Roche Bay, Hackett River, Back
River/Goose, Chidliak · limestone, lime and cement · **DEW Line / North Warning System sites — a scavenging
economy's first stop, entirely unresearched** · agriculture and greenhouses · pre-contact population estimates
· Pine Point's current resource estimate · NWT/Nunavut **transport** (Mackenzie barge system,
Tibbitt-to-Contwoyto ice road, Arctic sealift, Iqaluit, beach-landing communities).

### Cascadia

Uses inline `[UNVERIFIED]` / `[SOURCES DISAGREE]` flags rather than a gap list — **~90 flags across the two
files.** Concentrations worth a dedicated pass:

- **Population** — no single reconciled total across four jurisdictions and two countries was computed. BC, WA
  and OR figures are all individually flagged.
- **Baja California** — nearly everything: Boléo copper status, reserve figures, aqueduct capacity, CONAPESCA
  fishery tonnages, SIN grid interconnection, generation capacities. Baja is the least-verified part of the
  nation.
- **Ports** — Oakland TEU, current NWSA TEU (only a "12.4% YTD decline" datapoint), Prince Rupert post-2019,
  Ensenada, lower-Columbia grain tonnage.
- **Forestry** — BC annual allowable cut and harvest volumes, mill counts, log export figures.
- **Industry** — NASSCO San Diego, Vigor's post-2026 ownership, aerospace employment, current California fab
  list, Boeing 2024 strike scale.
- **Agriculture** — Washington hop acreage share, wheat class split, Willamette seed acreage, Klamath served
  acreage, Dungeness crab value, the Census-vs-CDFA billion-dollar discrepancy.
- **Hydro** — The Dalles capacity, Site C/John Horgan Dam farmland trade-off ("sources disagree, and badly"),
  BC Hydro facility totals.

### Colorado Republic

**Sources disagree:** Colorado River natural flow (13.5 / 14.6 / 15.0 / 16.4 MAF) · Colorado–Big Thompson
annual volume (215k / 260k / 310k acre-feet) · Great Salt Lake dust health risk · Las Vegas and Salt Lake City
metro populations (differ by up to a million) · Bingham Canyon output (nominal vs. actual).

**Stale:** Stillwater PGM figures are 2013-era · Climax capacity is nameplate only · cattle inventory is
January 2024 and covers only CO and WY · Montana wheat comparisons mix baselines · precipitation from a
secondary aggregator · lake levels from a tracker, not Reclamation.

**Could not verify:** the 2024 Idaho ESPA curtailment order · whether White Mesa Mill is the only operating
conventional uranium mill in the US · EVRAZ Pueblo's current status · Montana and Idaho hydro capacity · Green
River oil shale in-place figures · rangeland stocking rates (AUMs/acre) · San Luis Valley aquifer specifics ·
**1900 and 1930 census figures for the six states (would materially sharpen the carrying-capacity estimate)** ·
nitrate/saltpeter deposits for black powder.

**Deliberately excluded:** what the 2083 war itself does to climate, precipitation and snowpack. Everything
assumes present-day hydrology. Any nuclear-winter shift would hit the snowpack — the territory's entire water
supply — first and hardest.

### Midwestland

**Rests on model knowledge, not sources** (highest risk): nuclear plant names · refinery names and capacities ·
nitrogen plant capacities (Wever IA, Port Neal IA, Beulah ND) · legume N fixation rates · draft-animal acreage
limits.

**Unverified:** world corn production total (so the world-share figure is unusable as stated) · Garrison Dam
capacity (515 vs. 583.3 MW) · Oahe storage · "no navigation locks on the Missouri mainstem" · Missouri River
barge tonnage · Upper St. Anthony Falls Lock closure · Kansas City as second-largest US rail hub · Soo Locks
tonnage · Duluth-Superior cargo mix · North Dakota lignite tonnages · Duluth Complex copper-nickel resources ·
Minorca Mine ownership.

**Stale data:** ERS crop-specific fertilizer series ends 2018 · USGS irrigation data is 2015 (Circular 1441).

### Sonora

**La Caridad** — no verifiable public profile; tonnages, grades and smelter capacity all unverified ·
**Sonora lithium / Bacadéhuachi — ownership and legal status after the 2022 nationalization unverified, and
USGS does not list Mexico among named lithium reserve holders. Flagged as "the territory's weakest mineral
claim."** · AHMSA Monclova's 2026 status · US primary copper smelter count (USGS says two; Hayden, Miami and
Kennecott would make three) · Ray mine's 1.73% Cu grade looks anomalously high for a porphyry · the 1944
treaty's 1,750,000 acre-feet obligation not checked against IBWC · Tamaulipas coastline length · NREL GHI/DNI
values · Ford Hermosillo, Saltillo/Ramos Arizpe, Tesla Santa Catarina · port tonnages for Guaymas, Altamira,
Tampico · New Mexico dairy ranking · pecan world ranking · rangeland stocking rates · CONAGUA overexploited
aquifer counts · maquiladora employment · **precise combined territory population** · population figures mix
2020 census years with 2024–26 estimates and are not internally consistent.

**Recommended primary sources nobody could reach without search budget:** Servicio Geológico Mexicano
(sgm.gob.mx) · CONAGUA (gob.mx/conagua) · IBWC/CILA (ibwc.gov) · SIAP (gob.mx/siap) · NREL NSRDB
(nsrdb.nrel.gov) · INEGI (inegi.org.mx) · CIMMYT.

---

## 4. Known Errors and Corrections Already Made

Recorded so they are not silently reintroduced.

- **"Anchorage handles 90% of goods entering Alaska" is a misreading.** The port handles about **half** of
  inbound freight; 90% is the *population share* served. Corrected in the Alaska base file.
- **Cascadia's north-south fragility thesis was backwards.** Three of four no-substitute chokepoints are
  **east-west**; every north-south pinch point has a sea bypass. "A ladder, not a chain." Corrected in the
  supplement, and the parent file's dangling Section 5 references now resolve.
- **The map territories were initially briefed wrong** for four of five nations (Cascadia missing California,
  Baja and the Panhandle; Alaska missing NWT/Nunavut and wrongly holding the Panhandle; Midwestland given the
  Ohio Valley instead of the plains; Sonora wrongly given Texas). Corrected mid-flight; see
  `nations/New North America - Territory Definitions (read from map).md`, which is now the single authority.
- **DGGS SR78 Appendix E contains an arithmetic error**: Johnson Tract indicated at 384,595,959 short tons @
  0.156 oz/t Au for 598,000 oz is off by ~100×. Real figure likely ~3.85 million short tons.
- **Wikipedia's Mackenzie River page gives "166 billion barrels"** for the Mackenzie Delta region, which is
  almost certainly wrong as stated. Deliberately not used.
- **Nunavut's "18.3 billion barrels" and "181.4 Tcf"** are CER **resources, not reserves** — undeveloped,
  unpermitted, offshore-licensing-banned.

---

## 5. Standing Cautions

- **Wikipedia is the backbone of several sections**, particularly NWT/Nunavut Parts 1, 2, 4, 5, 6 and 8. It is
  well-cited and the numbers cross-check, but **every Wikipedia-attributed figure should be confirmed against a
  company filing, NRCan, or the CER before being treated as settled.**
- **"Cantung and Mactung hold 15% of the world's tungsten"** is a 2007 company statement made by a CEO in a
  promotional context. Not independently assessed.
- **Units are not consistent across sources.** Alaska state sources use **short tons**; Canadian and NI 43-101
  sources use **metric tonnes**; airport cargo rankings use metric tonnes; Canadian road sources use
  kilometers. Every file preserves and labels the source's own unit — do not assume.
- **Alaska crude production has three legitimate different figures** for 2025 — EIA 422,000 bbl/d (crude and
  condensate), Alyeska 462,821 (pipeline input including NGLs), Alaska DOR 468,000 (fiscal-year North Slope).
  Not contradictions, but they are quoted interchangeably in the press.
- **TAPS minimum flow is a litigated number with money on both sides** — 300,000–350,000 (Alyeska 2011) vs.
  ~200,000 (Alyeska 2021, with investment) vs. 70,000 (BP, upheld by the Alaska Superior Court) vs. 45,000
  (with a 20-inch replacement line). **Do not present any one of them as settled.**
