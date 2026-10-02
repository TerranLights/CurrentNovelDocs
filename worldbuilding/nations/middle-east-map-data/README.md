# Middle East, Turkey and Afghanistan Map Data — for Image Generation

2026-09-28. Machine-readable datasheets derived from
`../../extractions/Middle East - Sykes-Picot, Sect and the Kurdish Question (survey).md` (the frameworks
survey) and `../material-base/Middle East - Material and Economic Base (survey).md` (the material survey),
formatted so they can be handed to an image-generating model to draw a map.

**This is Stage 3 of this project's five-stage worldbuilding pipeline** (frameworks survey → material survey →
**map data** → generation → naming). See `../../STATUS - Cross-Session Progress Tracker.md` §4.8 for the full
pipeline and this region's status. Stage 4 (actual rendering) has not happened yet — that lands in
`y-files/Map Files/Asia (West)/01 initial generations/` per the author's own explicit folder instruction
(2026-09-28), not in this repo.

**Companion package**: `../central-asia-map-data/` (Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan,
Tajikistan) — built the same day, same schema. Two of this package's own four spheres (S3, S4, below) connect
directly to that package rather than staying self-contained; see "The Two Cross-Map Connectors" below.

**⚠️ Rendering update, 2026-09-29**: the actual rendered maps (in `05 follow-up - finalized maps/`) were cleaned
up to draw every region as one flat solid color — no hatching, no lighter-shade tier variants. Every mention of
"hatch," "lighter shade," or "domain-tinted" below and in `regions.csv`/`subdivisions.csv` describes the
internal tier/confidence *data*, which is fully preserved for the eventual wiki — it just isn't drawn on the
map itself anymore. **One deliberate exception, same day**: Khuzestan was recolored to Persia's own color and
given a diagonal hatch overlay specifically to keep signaling "not cleanly settled" — author's own instruction.
It's the one region on the map that still carries a drawn hatch.

**⚠️ Naming update, 2026-09-29**: "Georgia (Kartvelian/Orthodox)," "Armenia (Apostolic)," and "Azerbaijan
(Turkic/Shia)" were simplified to plain "Georgia," "Armenia," and "Azerbaijan" — author's own instruction. The
dropped parentheticals stay fully documented in `regions.csv` and the South Caucasus frameworks survey; only
the display labels changed.

**Sixteen real, present-day sovereign countries/territories, no partition or nation-naming decisions made** —
the same premise the mainland Southeast Asia package started from: every subdivision belongs to the country it
already, really belongs to. **What this package adds beyond an ordinary political map is four cross-border
spheres**, and a set of flagged-but-unresolved live disputes this project's "research proposes, the author
disposes" rule does not let this file settle on its own.

---

## The Model: Hard Borders Plus an Overlapping Sphere Layer

Same convention as every other regional map-data package in this project (see the mainland/maritime Southeast
Asia and Central Asia READMEs for precedent): **cores get hard borders; spheres overlap, and the overlaps are
correct rather than errors.**

1. **`subdivisions.csv`** — the ordinary political layer. Sixteen countries/territories, each with hard,
   solid-fill national borders, built from their real first-order administrative subdivisions (province /
   governorate / region / emirate / municipality / district — whatever each country's own terminology is) —
   **whole units only, per this project's absolute rule: never split one.**
2. **`spheres.csv`** — four cross-border cultural/ethnic/sectarian zones drawn **on top of** the hard borders
   as a translucent or hatched overlay, **not** as redrawn borders. Same `core_territory` / `domain_territory`
   / `sphere_territory` convention used throughout this project. **Overlaps are expected and correct — do not
   resolve them into a single owner.**

---

## The Sixteen Countries/Territories

| Country | Subdivision type | Count | Color |
|---|---|---|---|
| Turkey | Province | 81 | `#2E5B8A` |
| Syria | Governorate | 14 | `#8A3E2E` |
| Lebanon | Governorate | 9 | `#4E8A3E` |
| Israel | District (+1 civil-administration area) | 7 | `#C9A227` |
| Palestinian Territories | Governorate | 16 (11 West Bank + 5 Gaza) | `#6B2E8A` |
| Jordan | Governorate | 12 | `#2E8A7A` |
| Iraq | Governorate | 19 | `#C4622D` |
| Iran | Province | 31 | `#4A4A8A` |
| Saudi Arabia | Region | 13 | `#B9975B` |
| Yemen | Governorate (+1 municipality) | 21 | `#6B8E4E` |
| Oman | Governorate | 11 | `#A65D57` |
| United Arab Emirates | Emirate | 7 | `#4F86C6` |
| Qatar | Municipality | 8 | `#8B5FBF` |
| Bahrain | Governorate | 4 | `#D4A017` |
| Kuwait | Governorate | 6 | `#4FA3A0` |
| Afghanistan | Province | 34 | `#C77B3E` |

**293 total subdivision rows.** ⚠️ **One color was changed from the two raw research passes that fed this
file**: Iraq's original color (`#8A2E5E`) was nearly indistinguishable from Syria's (`#8A3E2E`) — both dark
brick/maroon tones, and the two countries share a long land border. Iraq was reassigned `#C4622D` (a
distinguishable burnt orange) during the merge step; every other color is exactly as each research pass
assigned it. Raw pre-merge files are preserved at `archive 01 - raw subdivision parts/` for reference.

---

## The Four Spheres

| ID | Name | What it captures |
|---|---|---|
| **S1** | The Kurdish Nation | ~45 million Kurds split across Turkey (~half), Iran and Iraq (6-7M each) and Syria (~2.5M) — this package's most structurally complex sphere by far. **Read `spheres.csv`'s own note before drawing anything; the frameworks survey itself declines to propose a treatment.** |
| **S2** | Sunni-Shia Sectarian Geography | A demographic-distribution layer, not a political bloc — Iran and southern/central Iraq as the region's Shia-majority core, with real minority populations in Bahrain (~50%), Lebanon (28%), Yemen's Houthi north (~35%, Zaydi specifically), Syria's Alawite coast, and Saudi Arabia's Eastern Province. |
| **S3** | The Pan-Turkic Sphere | Turkey's own linguistic-family tie to Kazakh, Uzbek, Turkmen and Kyrgyz — labeled only here, drawn on the companion Central Asia map. |
| **S4** | The Persianate / Central Asian Bridge | Afghanistan's Tajik, Uzbek and Turkmen populations tie directly to three Central Asia map-data nations' own titular peoples, while its Dari language ties it to Iran's Persian core — Afghanistan's own "two bridges," per the frameworks survey's §7.4. |

Full detail, sourcing, and confidence levels for each sphere are in `spheres.csv` — read the `notes` column
before drawing; S1 and S2 in particular carry real, load-bearing caveats about what this file does and does not
decide.

---

## The Two Cross-Map Connectors (S3, S4)

**This is the first time in this project that a single frameworks survey names its own cross-map connection
explicitly**, rather than a connection being discovered independently on each side (the way the mainland/
maritime Southeast Asia "Patani Malay World" sphere was found from two separate surveys converging on the same
provinces). The Middle East frameworks survey's own §7.4 says outright: **Afghanistan "may be this region's
single strongest argument for treating West Asia as one connected map-data space rather than two entirely
separate ones."**

- **S3 (Pan-Turkic)** connects Turkey to `../central-asia-map-data/`'s Kazakhstan, Uzbekistan, Turkmenistan and
  Kyrgyzstan — a shared Turkic-language family tie, institutionally real (the Organization of Turkic States)
  but not independently researched this pass.
- **S4 (Persianate/Central Asian Bridge)** connects Afghanistan to the same companion package's Tajikistan,
  Uzbekistan and Turkmenistan specifically (shared titular ethnicities split by a modern border) **and**
  separately to Iran within this package (shared Dari/Farsi mutual intelligibility) — Afghanistan sits at the
  convergence of both bridges at once.

**Neither sphere is drawn as territory on the companion map from this side** — follow the same "label only,
continues onto the companion map" convention the mainland Southeast Asia package established for the Tai
Continuum's reach into southern China, applied here for the first time to two maps that are both this
project's own work rather than one reaching toward an already-settled region (East Asia).

**⚠️ Scoping question, not decided here**: whether "West Asia" should ultimately be one combined map-data
space or two separate ones (as currently built) is the author's call, flagged directly by the frameworks
survey itself, not resolved by this file. This package and `../central-asia-map-data/` were built as two
separate packages because that is what the two Stage 1/Stage 2 surveys already are — combining them into one
is a real, undertaken-later option, not a default this file assumes.

---

## Live Disputes and Dated Situations — Flagged, Not Resolved

Per this project's "research proposes, the author disposes" rule, and per how the frameworks survey itself
treats every one of these (it takes no position on any of them):

- **Israel/Palestine (Jerusalem and the West Bank).** `subdivisions.csv` deliberately records **two
  overlapping administrative layers** rather than picking one: Israel's own Jerusalem District plus its
  "Judea and Samaria Area" civil-administration zone, alongside the Palestinian Authority's own separate
  11-governorate West Bank structure (including its own "Jerusalem (al-Quds)" governorate over much of the
  same ground). Both are recorded; neither is asserted as the map's eventual answer. This mirrors how this
  file handles Iraq's Kirkuk (below) and how the East Asia map series handled Jeju-do's three-power
  condominium — overlapping claims recorded as overlapping claims, not silently resolved.
- **Iraq's Kirkuk governorate** is one of Iraq's constitutionally "disputed territories" under Article 140 — a
  real, live, unresolved status question between the federal government and the Kurdistan Regional
  Government. Flagged on its own row; not resolved.
- **Iraq's Halabja governorate's exact Kurdistan Region (KRI) membership date/status** could not be
  independently corroborated this pass against a primary source (one research source called it "officially
  approved April 2025," which conflicts with Halabja's own longer administrative history since 2014) — flagged
  as a genuine open uncertainty, not resolved.
- **Yemen's civil war** is recorded at the governorate level in `subdivisions.csv` as a **live, dated (September
  2026) control snapshot** — Houthi-controlled north/northwest, PLC/internationally-recognized-government-held
  south/east, several governorates flagged contested, and Socotra flagged as a genuinely distinct case (general
  PLC sovereignty, real reported outside/Emirati influence). **This is the same kind of dated situational
  layer the mainland Southeast Asia package's Myanmar civil-war snapshot was — real, sourced, but explicitly
  not built as a permanent base-map layer.** Consider it exactly as that package's README suggested for
  Myanmar: a candidate **optional second map** with an explicit "as of September 2026" caption, not folded into
  the region's one settled base map.
- **Syria's Kurdish integration** (the AANES/"Rojava" autonomous zone, dissolved and folded into the new
  Syrian state 20 August 2026) and **Turkey's PKK ceasefire** (declared 1 March 2025, disarmament pledged May
  2025) are both **very recent and explicitly flagged by the frameworks survey itself as fragile, not settled**
  — see S1's own note in `spheres.csv`. Any Kurdistan-sphere treatment chosen should account for the real
  possibility that either fact changes again before a map is actually drawn.
- **The Golan Heights** (Israeli-held, bordering Syria's Quneitra governorate) is named by the frameworks
  survey (§2.3) as "a live, separate Israel-Syria border question outside the Israel/Palestine focus" — flagged
  on Quneitra's row, not otherwise researched or resolved here.

---

## What's Sourced vs. What's This File's Own Judgment Call

Per this project's "research proposes, the author disposes" rule, everywhere this package went beyond what the
two surveys themselves say is flagged in the relevant CSV row and summarized here:

- **All sixteen countries' current first-order subdivision counts and names** were independently verified via
  WebSearch/WebFetch against current sources (not simply assumed from background knowledge) — see each
  research pass's own report for country-by-country confidence. Turkey's 81-province list was diffed against
  a source list and one omission was caught and fixed before this file was assembled.
- **Turkey's 16 Kurdish-majority/plurality province flags** are sourced to general aggregator/Wikimedia
  material (a map of Turkish provinces with Kurdish majorities, plus Rudaw reporting), **not** per-province
  census percentages — medium confidence, flagged per-row.
- **Iran's ethnic-minority province flags** (Azeri in Ardabil/East Azerbaijan/West Azerbaijan; Kurdish in
  Kurdistan/Kermanshah/Ilam/West Azerbaijan; Arab in Khuzestan; Baloch in Sistan and Baluchestan) are from
  general demographic sourcing, **not independently verified this pass** — flagged per-row, feeding the
  Kurdistan sphere (S1) and noted as open items for a future pass.
- **Afghanistan's per-province ethnic-majority labels** are **mostly this file's own extrapolation** from the
  frameworks survey's general geographic pattern (Pashtun south/southeast, Tajik north/northeast/Kabul, Hazara
  central highlands, Uzbek north) — only **Balkh, Kunduz, Ghor and Jowzjan** are directly sourced to
  per-province percentage breakdowns this pass (marked ✅ in `subdivisions.csv`); every other Afghan province's
  label is marked low-confidence extrapolation, not a finding.
- **Afghanistan's mineral-claim geography**: Mes Aynak copper (Logar province) is directly sourced and is this
  package's most concrete Afghan mineral location (5.5-11.5 million tonnes of high-grade ore, described as the
  world's second-largest exploitable copper deposit — though per the material survey's own skepticism, real
  geology with essentially no realized extraction). The Ghazni/Herat lithium attribution named in this
  package's own research directive was **not verified to a credible source** — flagged on both provinces'
  rows, not asserted.
- **Yemen's per-governorate control status** (Houthi / PLC-government / contested) is this pass's own research
  synthesis of the current (September 2026) conflict situation, not drawn from either survey directly — several
  governorates (Al Bayda, Al Jawf, Dhale, Taiz) are marked contested/uncertain rather than assigned confidently
  to either side.
- **Oman's 11th governorate (Ad Dakhiliyah)** was added on medium confidence — the specific research pass's
  source snippet named only 10 of 11 governorates by name while stating the total is 11; Ad Dakhiliyah is
  Oman's well-established Interior governorate and the clear candidate, but this was not independently
  re-verified against a named primary source.
- **Population data availability varies enormously by country** — Turkey, Syria, Lebanon, Israel, Jordan, Iraq,
  Iran and Saudi Arabia all have real per-subdivision population figures (vintages ranging 2013-2024, each
  flagged per-row); **Qatar, Bahrain and Kuwait have no sourced per-subdivision population data at all** — only
  country-wide totals exist in the source surveys, and this pass could not find municipality/governorate-level
  breakdowns for any of the three. Several UAE emirates (Fujairah) and most Yemeni and Omani governorates are
  also blank for the same reason.
- **All four spheres' core/domain framing reflects legal status or population-share magnitude only**, never a
  claim about political alignment or legitimacy — see each sphere's own `notes` field, especially S1 and S2,
  where this distinction is most load-bearing.

---

## Rendering Conventions

Follows the same house style established across this project's other regional map-data packages (see the
mainland Southeast Asia and Central Asia READMEs for the concrete precedent):

- **Lambert azimuthal equal-area projection**, re-centered for this region — something like
  `+proj=laea +lat_0=28 +lon_0=48 +datum=WGS84 +units=m` (roughly the geographic center of the sixteen
  countries, weighted toward the Arabian Peninsula/Gulf where most of the map's area sits) is a reasonable
  starting point, not a fixed requirement. **Given the region's real east-west extent (Turkey to
  Afghanistan) and north-south extent (Turkey to Yemen), consider whether one map can hold acceptable
  distortion at both ends, or whether a full-region overview plus 1-2 regional close-ups (mirroring Russia's
  four-map treatment) serves this package better** — an open call, not decided here.
- **Solid country fills, white-then-dark-line national borders** (a ~1.8pt white casing under a ~0.5pt dark
  line is the pattern used elsewhere in this project) for the hard-border layer.
- **Sphere overlay**: core = solid color at reduced opacity or a distinct hatch, domain = lighter/thinner
  version of the same, sphere = dotted outline/label only. Given how sensitive S1 (Kurdish Nation) and S2
  (Sunni-Shia geography) are, consider a visually restrained treatment for both — a subtle hatch rather than a
  bold fill — so the overlay reads as "documented demographic fact" rather than "proposed political claim,"
  the same posture the frameworks survey itself takes.
- **A live-situation overlay (Yemen's control map) is a candidate optional second map**, not built into the
  base map — see "Live Disputes and Dated Situations" above.
- **Serif display font for nation/sphere names, sans-serif for cities and captions** — matches the Crimson
  Text / Lato pairing used elsewhere in the project, though any comparable serif/sans pairing is fine.

**One base map is expected, not a multi-era timeline series** — the same present-day-snapshot premise the
mainland Southeast Asia package used, since neither survey contains a decided sequence of post-collapse
mergers, splits or unifications for these sixteen countries/territories.

---

## The Files

| File | Rows | What it is |
|---|---|---|
| `subdivisions.csv` | 293 | Every first-order subdivision of all sixteen countries/territories — the hard-border layer |
| `spheres.csv` | 4 | The overlay — Kurdish Nation, Sunni-Shia geography, Pan-Turkic, Persianate/Central Asian Bridge |
| `archive 01 - raw subdivision parts/` | — | The two raw research-pass CSVs this file's `subdivisions.csv` was merged from, kept for reference |

## Column Reference — `subdivisions.csv`

| Column | Meaning |
|---|---|
| `nation` | One of the sixteen countries/territories. **The primary key for the hard-border fill.** |
| `subdivision_name` | The first-order unit's real name. |
| `subdivision_type` | Province / Governorate / Region / Emirate / Municipality / District / Civil Administration Area — varies by country's own terminology. |
| `population` | Filled where a real current figure could be sourced (vintages 2013-2024, noted per-row); blank and flagged in `notes` where it could not (see "What's Sourced" above). |
| `color_hex` | One fixed color per country (sixteen total) — solid fill for the hard-border layer. |
| `notes` | Sphere membership flags, disputed-territory flags (⚠️), ethnic/sectarian composition flags, dated-conflict-status flags, and judgment-call flags. **Read before drawing — this is where most of the actual content lives.** |

## Column Reference — `spheres.csv`

Same core/domain/sphere_territory convention as every other regional map-data package in this project:

| Column | Meaning |
|---|---|
| `sphere_id` | S1-S4. |
| `sphere_name` | Display label. |
| `core_territory` | Strongest presence / settled legal status. **Draw as solid fill or a strong hatch.** |
| `domain_territory` | Clear but lesser presence. **Draw as lighter fill or finer hatching.** |
| `sphere_territory` | Named but out of this map's scope (Central Asia, for S3/S4) — **label only; do not draw territory for it.** |
| `source_section` | Which survey section grounds this row. |
| `confidence` | `high` / `medium` / `low`. |
| `notes` | Design flags, caveats, and (for S1/S2 especially) real, load-bearing cautions — read them. |

---

## Suggested Prompt

> Draw a map of Turkey, Syria, Lebanon, Israel, the Palestinian Territories, Jordan, Iraq, Iran, Saudi Arabia,
> Yemen, Oman, the United Arab Emirates, Qatar, Bahrain, Kuwait and Afghanistan, showing each country's
> first-order administrative subdivisions with a solid hard border, colored by `color_hex` from
> `subdivisions.csv`. Then overlay the four spheres from `spheres.csv` as restrained hatching or dotted
> outlines, not bold fills: the Kurdish Nation (Iraq's KRI as the strongest presence, lighter hatching across
> the Kurdish-flagged provinces of Turkey, Iran and Syria), Sunni-Shia sectarian geography (Iran and southern/
> central Iraq strongest, lighter hatching across Bahrain, southern/eastern Lebanon, Yemen's Houthi north,
> coastal Syria and Saudi Arabia's Eastern Province), and the Pan-Turkic and Persianate/Central Asian Bridge
> spheres (Turkey and Afghanistan respectively) labeled as continuing onto a companion Central Asia map, not
> drawn here. Record Israel's and the Palestinian Authority's overlapping claims over Jerusalem/the West Bank
> as two layers, not one. Do not resolve Iraq's Kirkuk, the Golan Heights, or any other flagged live dispute
> into a single owner. One base map only; treat Yemen's civil-war control status as a candidate separate,
> dated overlay map, not part of this one.

---

## Caveats

- **Whole first-order subdivisions only** — this project's absolute rule, followed exactly here.
- **This package makes zero partition or nation-naming decisions** — every one of the sixteen entries is a
  real, present-day sovereign country or (for the Palestinian Territories) a real, internationally-recognized
  administrative geography; the only original content is the four-sphere overlay.
- **Several real, live, unresolved disputes are recorded as flags, not resolved** — see "Live Disputes and
  Dated Situations" above. This is deliberate and matches both surveys' own posture; do not treat any of these
  as settled when Stage 4 rendering begins.
- **Two spheres (S3, S4) reach into the companion `../central-asia-map-data/` package** — the first time this
  project's frameworks-survey material itself has flagged a cross-map connection explicitly, rather than one
  being found independently on each side. See "The Two Cross-Map Connectors" above.
- **Confidence varies enormously row by row** — see "What's Sourced vs. What's This File's Own Judgment Call"
  above before treating any subdivision's ethnic/sectarian flag, or any sphere's exact boundary, as settled.
