# South Caucasus Map Data — for Image Generation

2026-09-28. Machine-readable datasheets derived from
`../../extractions/South Caucasus - Three Churches, Two Pipelines and a Closed Border (survey).md` (the
frameworks survey) and `../material-base/South Caucasus - Material and Economic Base (survey).md` (the
material survey), formatted so they can be handed to an image-generating model to draw a map.

**This is Stage 3 of this project's five-stage worldbuilding pipeline** (frameworks survey → material survey
→ **map data** → generation → naming). Stage 4 (actual rendering) has not happened yet.

**Added to West Asia on the author's explicit instruction** ("add those to West Asia and do the necessary
research for them"), surfaced organically by the author's own work developing the Kurdish Nation region on the
Middle East map — Turkey's Kurdish-flagged eastern provinces border Armenia and Georgia directly, and Armenia
holds a real Yazidi/Kurdish population this project's data didn't previously carry. **Companion packages**:
`../central-asia-map-data/` and `../middle-east-map-data/`, both already built with the same schema.

**⚠️ Rendering update, 2026-09-29**: the actual rendered maps (in `05 follow-up - finalized maps/`) were cleaned
up to draw every region as one flat solid color — no hatching, no lighter-shade tier variants. Every mention of
"hatch," "lighter shade," or "domain-tinted" below and in `regions.csv`/`subdivisions.csv` describes the
internal tier/confidence *data*, which is fully preserved for the eventual wiki — it just isn't drawn on the
map itself anymore.

**Three real, present-day sovereign countries, no partition decisions made** — the same premise the mainland
Southeast Asia and Central Asia packages started from. **What this package adds beyond an ordinary political
map is the Woodard-style culture layer** (`regions.csv`, five regions, not three — Abkhazia and South Ossetia
are drawn as their own ethnically-distinct regions, not folded into Georgia) and **two sphere rows that
recommend, but do not yet apply, extensions to the already-built Middle East package.**

---

## The Model: Hard Borders, a Woodard-Style Culture Layer, and Two Cross-Package Recommendations

Same convention as the Central Asia and Middle East packages (see those READMEs for full precedent, and see
[[feedback_woodard_style_means_culture_not_political]] for why this matters): **cores get hard borders;
spheres overlap, and the overlaps are correct rather than errors.**

1. **`subdivisions.csv`** — the ordinary political/administrative layer. Three countries, 38 rows, real
   first-order administrative units — **whole units only, per this project's absolute rule.**
2. **`regions.csv`** — **this map's primary subject**, per the author's own correction earlier this session:
   culture/ethnicity/religion as the primary drawn layer, not political borders. **Five regions, not three**
   — see "The Five Regions" below for why Abkhazia and South Ossetia are split out.
3. **`spheres.csv`** — two rows, **both explicitly recommendations to extend the Middle East package's own
   S3 (Pan-Turkic) and S1 (Kurdish Nation) spheres**, not new self-contained spheres of this package's own.
   Neither has been applied to that package's actual files — see "The Two Cross-Package Recommendations"
   below.

---

## The Five Regions

| Region | Tier 1 | Status |
|---|---|---|
| **Georgia (Kartvelian/Georgian Orthodox)** | Kartvelian | Core, uncontested. Adjara included, with a distinct hatch for its real Muslim-Georgian religious minority. |
| **Abkhazia** | Northwest Caucasian (Abkhaz) | ⚠️ Contested — de facto independent, Russian-recognized, almost universally still regarded internationally as Georgian territory. |
| **South Ossetia (Tskhinvali Region)** | Iranic/Indo-European (Ossetian) | ⚠️ Contested — de facto independent, Russian-recognized. **A real formal-status asymmetry with Abkhazia**: Georgia does not currently recognize it as a constitutional Autonomous Republic the way it still formally does Abkhazia. |
| **Azerbaijan (Turkic/Shia-Muslim)** | Turkic | Core, uncontested territorially, but includes Nakhchivan, a genuine geographic exclave separated from the rest of the country by Armenian territory. |
| **Armenia (Armenian/Apostolic)** | Armenian | Core, uncontested territorially, but see Syunik's own flag — Armenia's most valuable open border and its most contested live infrastructure question, in the same province. |

**Why Abkhazia and South Ossetia are their own regions, not shades of Georgia**: Abkhaz (Northwest Caucasian)
and Ossetian (Iranic/Indo-European) are genuinely separate ethnolinguistic families from Kartvelian Georgian —
this is the same logic that kept Karakalpakstan (a distinct Turkic ethnicity) separate from the Uzbek Oasis
Civilization in the Central Asia package, applied here to two real, contested, ethnically-distinct
territories rather than one settled, uncontested one. **This is a culture-map decision, not a political one**
— it says nothing about which flag should fly over either territory, only that the population living there is
not ethnically Georgian.

**Why Nagorno-Karabakh does NOT get its own region here, unlike the Central Asia package's Fergana Tangle or
the Middle East package's Kurdish Nation**: per the frameworks survey (§2.1), the territorial question is
**resolved** — Azerbaijan holds full control following the 2023 displacement of the territory's ethnic
Armenian population, and Azerbaijan's own 2021 administrative reform already folded the recovered territory
into two ordinary economic regions (Karabakh, East Zangezur — see `subdivisions.csv`). Unlike Abkhazia/South
Ossetia (unresolved) or the Kurdish Nation (a live, coherent, still-standing ethnic-national case), there is
no surviving population or contested administrative status here to draw as its own region — the population
that would have made it one has been displaced. Drawn as ordinary Azerbaijani territory, with the 2023
resolution flagged in `subdivisions.csv`'s own notes rather than erased.

---

## The Two Cross-Package Recommendations

**Neither of these has been applied to the Middle East package's actual `spheres.csv` file** — both are
recorded here as sourced recommendations, per this project's standing practice of flagging cross-region seams
for the author's own decision rather than resolving them unilaterally (the same posture the Central Asia
survey used for its own Kazakhstan-Russia and Xinjiang-diaspora seams).

- **S1, Pan-Turkic Reach — Azerbaijan**: the Middle East package's own S3 (The Pan-Turkic Sphere) already
  names Azerbaijan as a real, well-grounded Turkic relative of Turkey's, but leaves it entirely undrawn
  ("outside both this project's Middle East and Central Asia country scopes entirely"). This survey's §4
  finding (the "one nation, two states" formula, formalized in the 2021 Shusha Declaration) is the concrete
  anchor that was missing. **If the author wants this applied**, the Middle East package's S3 row would need
  its `sphere_territory` column updated to name Azerbaijan as real, drawable domain territory on this new
  South Caucasus map, connected via the same dashed-connector-arc convention the West Asia composite map
  already uses for S3/S4.
- **S2, Kurdish Nation's Yazidi Domain — Armenia**: Armenia's Yazidi population (31,079 self-identified per the
  2022 census; community estimates run over 50,000) is the largest by share anywhere in the world outside
  Iraq — a real population this project's existing Kurdish Nation region (Middle East package S1) does not
  reflect. **Flagged at LOW confidence, deliberately** — unlike S1 above, this isn't primarily a sourcing gap:
  whether Armenian Yazidis belong inside a pan-Kurdish cultural sphere at all is a live, unsettled question
  within Kurdish and Yazidi identity politics itself (Yazidism is its own distinct religion, not an Islamic
  sect), not something this survey's own research can resolve. If the author wants this drawn, it should
  probably be a visually lighter, more tentative marker than S1's Azerbaijan connection, not an equally
  confident sphere line.

---

## What's Sourced vs. What's This File's Own Judgment Call

- **All three countries' first-order administrative unit lists and types** were researched fresh via WebSearch
  (Wikipedia's Administrative divisions of Georgia/Azerbaijan/Armenia articles, Statoids). Armenia's ten
  marzer plus Yerevan and Georgia's nine mkhare plus Adjara/Tbilisi are both real, current, uncontested
  structures.
- **⚠️ Azerbaijan's subdivision tier is this file's own tractability judgment call, flagged explicitly in the
  material survey (§1.4) and repeated here**: Azerbaijan's actual first-order units are 64 rayons plus 11
  cities of republican significance (comparable in scale to Turkey's 81 provinces in the Middle East package)
  — this file uses the coarser, 14-region "economic region" categorization instead, to avoid a severe scale
  imbalance against Georgia's 13 units and Armenia's 11. This is a real, current, presidentially-decreed
  (2021) Azerbaijani administrative categorization, but it is NOT the country's most granular tier. If the
  author wants rayon-level precision for a future border decision, that's a real, available, more
  time-consuming research pass this file did not attempt.
- **Abkhazia and South Ossetia's inclusion as their own subdivisions.csv rows**, despite South Ossetia
  specifically lacking Abkhazia's formal constitutional-republic status, is this file's own judgment call —
  made for the same reason this project has given other real, de facto, geographically-precise disputed
  entities their own row before (Kirkuk, Israel/Palestine's overlapping claims in the Middle East package).
  Both are flagged ⚠️ DISPUTED, NOT RESOLVED in their own rows.
- **Population data is genuinely incomplete for Georgia and Azerbaijan**, by the same "flagged, not
  estimated" convention every prior package in this project has used. Armenia is fully sourced (all eleven
  units, 2025 estimates). Georgia's nine ordinary regions and Azerbaijan's fourteen economic regions have no
  disaggregated population figures found this pass — only country-wide totals exist. Abkhazia and South
  Ossetia ARE sourced, from their own de facto governments' figures (243,897 and 57,528 respectively,
  2025 estimates) — flagged as a different source basis than the Georgian-government-recognized national
  total, not directly comparable to it.
- **The five-region Woodard-style split (regions.csv)**, especially Abkhazia and South Ossetia's separation
  from Georgia, is this file's own reading of the frameworks survey's own ethnic-distinctness findings (§1,
  §2.2) — grounded in real, sourced linguistic-family facts (Northwest Caucasian, Iranic/Indo-European, and
  Kartvelian are three genuinely separate language families), not an enumerated region list from either
  survey. High confidence on the linguistic-family facts themselves; the decision to draw them as separate
  regions rather than hatched sub-zones within Georgia is this file's own call, flagged as such.
- **The two spheres.csv rows are recommendations only**, not applied edits to the Middle East package — see
  "The Two Cross-Package Recommendations" above.

---

## Rendering Conventions

Follows the same house style as the Central Asia and Middle East packages:

- **Lambert azimuthal equal-area projection**, re-centered for this region — something like
  `+proj=laea +lat_0=41.5 +lon_0=44.5 +datum=WGS84 +units=m` (roughly the geographic center of the three
  countries) is a reasonable starting point.
- **Solid region fills, white-then-dark-line borders** for the culture-region layer (this map's primary
  subject); **thin first-order-subdivision boundary lines** within each region's fill, matching the polish
  round already applied to the Central Asia and Middle East standalone maps; **modern political/country
  borders as thin dashed gray reference lines**, secondary to the culture-region fills.
- **Abkhazia and South Ossetia**: a distinct, clearly-different contested-territory treatment from ordinary
  core fills (e.g. the cross-hatch "contested/disputed ground" convention the Middle East map already uses
  for Kirkuk) — and the two should be visually distinguishable from EACH OTHER too, given the real
  formal-status asymmetry between them (Abkhazia's constitutional-republic status vs. South Ossetia's lack of
  it).
- **Nakhchivan**: draw as genuinely disconnected territory, physically separated from the rest of Azerbaijan
  by Armenian land — the same "draw the real geometry, including the gap" requirement as any other true
  exclave.
- **Existing out-of-scope neighbors**: Russia (already mapped, borders Georgia directly per frameworks survey
  §7.4) and Iran (already partly mapped on the Middle East package, borders both Armenia and Azerbaijan) should
  render as cross-hatched gray with a label, matching every other regional package's convention.
- **Cross-package connectors**: if the author applies the two spheres.csv recommendations, use the same
  dashed-connector-arc convention the West Asia composite map already established for S3/S4 between the
  Middle East and Central Asia packages.

**One base map is expected**, a present-day snapshot, matching every other regional package's own scoping.

---

## The Files

| File | Rows | What it is |
|---|---|---|
| `subdivisions.csv` | 38 | Every first-order subdivision of Georgia (13), Azerbaijan (14), Armenia (11) — the administrative layer |
| `regions.csv` | 5 | The Woodard-style culture layer — this map's primary subject |
| `spheres.csv` | 2 | Two recommended extensions to the Middle East package's existing spheres — not yet applied there |

## Column Reference — `subdivisions.csv`

| Column | Meaning |
|---|---|
| `nation` | One of the three countries. |
| `subdivision_name` | The first-order unit's real name. |
| `subdivision_type` | Region (mkhare) / Autonomous Republic / Economic Region / Province (marz) / Capital City — varies by country. |
| `population` | Sourced where available (all of Armenia, Abkhazia, South Ossetia); blank and flagged elsewhere (Georgia's ordinary regions, Azerbaijan's economic regions). |
| `color_hex` | One fixed color per country — but note `regions.csv`, not this column, is the map's primary color scheme; this file's own coloring is a secondary administrative-layer convention. |
| `notes` | Dispute flags (⚠️), cross-reference flags, and judgment-call flags. **Read before drawing.** |

## Column Reference — `regions.csv` and `spheres.csv`

Same schema as the Central Asia and Middle East packages' own `regions.csv`/`spheres.csv` — see those
READMEs' own column references if needed; not repeated here.

---

## Suggested Prompt

> Draw a map of Georgia, Azerbaijan and Armenia showing five culture/ethnicity regions as the primary colored
> layer: Georgia (Kartvelian/Georgian Orthodox, including Adjara with a distinct hatch for its Muslim-Georgian
> minority), Abkhazia (contested, Northwest Caucasian, cross-hatched as disputed), South Ossetia (contested,
> Ossetian/Iranic, cross-hatched as disputed but visually distinguishable from Abkhazia), Azerbaijan
> (Turkic/Shia-Muslim, including the disconnected Nakhchivan exclave), and Armenia (Armenian/Apostolic, with
> Syunik flagged for its dual role as Armenia's Iran border and the contested Zangezur Corridor route). Show
> real first-order administrative subdivisions as thin lines within each region. Show modern political borders
> as thin dashed gray reference lines. Cross-hatch Russia and Iran as existing out-of-scope neighbors. Do not
> draw a Nagorno-Karabakh region — that question is resolved (Azerbaijani control) per the frameworks survey,
> reflected instead in Azerbaijan's own Karabakh/East Zangezur economic-region names.

---

## Caveats

- **Whole first-order subdivisions only** — followed exactly, with the flagged Azerbaijan
  economic-region-vs-rayon tractability tradeoff noted above.
- **Abkhazia and South Ossetia's status is genuinely unresolved** — this package takes no position beyond
  recording the real, current, sourced facts. Do not treat either as settled when Stage 4 rendering begins.
- **The two spheres.csv rows are recommendations to the Middle East package, not applied edits** — see "The
  Two Cross-Package Recommendations" above before assuming the Kurdish Nation or Pan-Turkic sphere already
  reaches this package's territory anywhere else in this project's files.
- **Georgia's and Armenia's own material resource bases (beyond the transit-corridor and closed-border
  findings) were not researched this pass** — real, named gaps in the material survey, not settled
  "nothing to find" conclusions.
