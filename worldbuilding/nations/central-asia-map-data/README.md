# Central Asia Map Data — for Image Generation

2026-09-28. Machine-readable datasheets derived from
`../../extractions/Central Asia - Steppe, Oasis and the Fergana Tangle (survey).md` (the frameworks survey) and
`../material-base/Central Asia - Steppe, Oasis and Aquifer - Material and Economic Base (survey).md` (the
material survey), formatted so they can be handed to an image-generating model to draw a map.

**This is Stage 3 of this project's five-stage worldbuilding pipeline** (frameworks survey → material survey →
**map data** → generation → naming). See `../../STATUS - Cross-Session Progress Tracker.md` §4.8 for the full
pipeline and this region's status. Stage 4 (actual rendering) has not happened yet — the author has specified
its destination as `y-files/Map Files/Asia (West)/01 initial generations/` once it does, but that's a Stage 4
concern, not this file's.

**Like Mainland Southeast Asia, and unlike North America or Latin America, this map makes no partition
decisions of its own.** Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan and Tajikistan are already five real,
present-day sovereign countries. Every subdivision below belongs to the country it already, really belongs to.
**What this map adds beyond an ordinary political map is the Fergana Valley's cross-border mosaic, its literal
point-enclaves, and (optionally) a Uyghur-diaspora sphere.**

**⚠️ Rendering update, 2026-09-29**: the actual rendered map (in `05 follow-up - finalized maps/`) was cleaned
up to draw every region as one flat solid color — no hatching, no lighter-shade tier variants (this removed the
Fergana Tangle's own hatch, the GBAO/Gorno-Badakhshan lighter-shade domain variant, and the Samarkand/Bukhara
historic-center dot-hatch). Every mention of "hatch," "lighter shade," or "domain-tinted" below and in
`regions.csv`/`subdivisions.csv` describes the internal tier/confidence *data*, which is fully preserved for
the eventual wiki — it just isn't drawn on the map itself anymore.

**⚠️ Naming update, 2026-09-29**: five of this package's seven regions were renamed to their real, current
country names, the same convention this project already used on the Middle East map (Levant→Syria/Jordan,
Kurdish Nation→Kurdistan, "Arabia"→United Arab Emirates, etc.). `kazakh_steppe`/"The Kazakh Steppe" is now
`kazakhstan`/"Kazakhstan"; `kyrgyz_highlands`/"The Kyrgyz Highlands" is now `kyrgyzstan`/"Kyrgyzstan";
`turkmen_desert_oasis`/"The Turkmen Desert-Oasis" is now `turkmenistan`/"Turkmenistan";
`uzbek_oasis`/"The Uzbek Oasis Civilization" is now `uzbekistan`/"Uzbekistan"; `persianate_tajik`/"The
Persianate Tajik Highlands" is now `tajikistan`/"Tajikistan." Colors and member subdivisions are unchanged for
all five. `karakalpakstan` was deliberately NOT renamed — it already carries its own real, current name (an
autonomous republic, not a sovereign country needing this fix).

**⚠️ Second naming update, same day**: `fergana_tangle`/"The Fergana Valley Tangle" was also renamed, but not
to a country name — it's now `fergana_uncertain`/"Fergana Valley (Uncertain Territory)," matching the exact
naming convention this project already uses for Khuzestan ("Khuzestan (Unstable Territory)") and Dhale ("Dhale
(Disputed Territory)") on the Middle East map. This region still doesn't correspond to any single country — the
same reason "Kurdistan" and "Balochistan" keep their own descriptive names on the Middle East map — but its
genuinely unresolved, split ground truth (Osh City itself near-even at 43% Kyrgyz/48% Uzbek) is now named for
what it is, not left as a neutral-sounding "Tangle." Color and member subdivisions unchanged.

---

## The Model: Hard Borders, One Broad Sphere, and a Set of Point-Enclaves That Are Neither

Following this project's established pattern (see the Mainland Southeast Asia and East Asia map-data READMEs),
this package has **three layers, not two**, because Central Asia's own geography needs one more than most prior
regions:

1. **`subdivisions.csv`** — the ordinary political layer. Five countries, each with hard, solid-fill national
   borders, built from their real first-order administrative subdivisions — **whole units only, per this
   project's absolute rule: never split a province.** 55 rows total (Kazakhstan 21, Uzbekistan 14, Turkmenistan
   6, Kyrgyzstan 9, Tajikistan 5).
2. **`spheres.csv`** — two cross-border cultural zones drawn **on top of** the hard borders as a translucent or
   hatched overlay, **not** as redrawn borders, using this project's standard `core_territory` /
   `domain_territory` / `sphere_territory` convention. **S1, the Fergana Valley Mosaic**, is grounded and
   settled; **S2, the Uyghur Diaspora**, is explicitly the author's call to include or omit (see the row's own
   notes).
3. **The Fergana Enclaves — a third thing, and neither a subdivision nor a sphere.** Eight small, specific
   points of territory (six individually named) where one country's population sits fully surrounded by
   another's — too small and too discrete to be first-order subdivisions, and too small and too precise to be
   a diffuse sphere like S1 or S2. **See the dedicated section below — read it before drawing anything in the
   Fergana Valley.**

**Expect this region to read visually closer to Mainland Southeast Asia than to East Asia or Latin America**:
five solid-colored countries, one broad sphere overlay across the valley, and — genuinely new to this
project's rendering vocabulary — a scatter of small point-markers where the enclaves sit.

---

## The Fergana Enclaves — a Third Thing, and It Is Not a Sphere

**Do not attempt to draw the eight Fergana Valley enclaves as bordered territory of their own, and do not fold
them into the S1 sphere overlay either.** They are sub-subdivision-level exclaves — smaller than a district,
belonging on paper to one country while sitting entirely inside another's territory — the same structural
category as Kaliningrad in this project's own Russia package (flagged there, unresolved there too), but
multiplied eightfold and interlocking three countries at once. The frameworks survey (§2) is explicit that this
project's whole-first-order-subdivision rule "cannot make this problem disappear," and that it "needs its own
design decision at Stage 3, not a default 'whole subdivisions only' treatment." **This file's own decision**:
treat them as **point markers with leader lines**, the same visual grammar this project's East Asia and
Mainland Southeast Asia packages already use for the Hakka and the Wa — a label and a dot, never a hatched
region and never a border.

| Enclave | Ethnicity | Surrounded by | Notes |
|---|---|---|---|
| Sokh | Uzbek | Kyrgyzstan (Batken Region) | One of four Uzbek exclaves inside Kyrgyz territory; among the largest. |
| Shakhimardan | Uzbek | Kyrgyzstan (Batken Region) | |
| Chon-Gara (Chon-Kara) | Uzbek | Kyrgyzstan (Batken Region) | |
| Tash-Tepa (Tash-Dobe) | Uzbek | Kyrgyzstan (Batken Region) | |
| Vorukh | Tajik | Kyrgyzstan (Batken Region) | ~30,000 people, fully engulfed; reduced from 19,000 to 14,500 hectares in a 2025 border agreement. |
| Kairagach (Western Kalacha) | Tajik | Kyrgyzstan (Batken Region) | |

**Eight enclaves total isolate roughly 100,000 people from their own central governments** (frameworks survey
§2) — this table individually names six; the remaining two were not separately named in either survey and are
not drawn here as a result. This is a **live, currently-dangerous border, not a historical curiosity**: roughly
20 armed conflicts between 1989 and 2009, 37 border incidents in 2014 alone, and a 2021–2022 flare-up (starting
over a water dispute around Vorukh specifically) that killed an unknown number in the hundreds and displaced up
to 136,000 people. **⚠️ A 2025 Kyrgyz-Tajik border agreement has resolved some of this** (the Vorukh reduction
above is one term of it) — treat the valley as still-live and currently de-escalating, not frozen or fully
resolved; neither survey verified how complete or durable the 2025 agreement is.

**Give each enclave a small, undecorated dot at its approximate real-world location, a leader line, and a
one-line label naming its ethnicity and enclosing country** — do not give any of them their own legend entry
beyond a single shared "Fergana Valley enclave" marker type, since drawing eight distinct legend entries for
sub-district territories this small would overweight them relative to every ordinary subdivision on the map.

---

## The Two Spheres

| ID | Name | What it captures |
|---|---|---|
| **S1** | The Fergana Valley Mosaic | The broad, diffuse ethnolinguistic and settlement continuity across the valley floor — Uzbek, Tajik and Kyrgyz populations living intermixed across a shared agricultural basin, spanning six regions across all three countries. **Settled and grounded** — draw this one. |
| **S2** | The Uyghur Diaspora / East Turkestan Reach | ~300,000+ Uyghurs in Kazakhstan and smaller populations in Uzbekistan and Kyrgyzstan, with their ethnic core (Xinjiang) already mapped as its own polity on this project's East Asia series. **Explicitly the author's call to include or omit** — see the row's own notes in `spheres.csv`; the frameworks survey raises this as an open question, not a settled design element. |

Full detail, sourcing, and confidence levels for each are in `spheres.csv` — read the `notes` column before
drawing either row.

---

## What's Sourced vs. What's This File's Own Judgment Call

Per this project's "research proposes, the author disposes" rule, every place this file went beyond what the
two surveys themselves say is flagged in the relevant CSV row and summarized here:

- **All 55 first-order subdivision names, types and counts** were **not** enumerated in either survey at this
  level of detail (the frameworks survey's own "Open questions" section names this exact gap: "Administrative
  subdivision counts for Kazakhstan, Kyrgyzstan and Turkmenistan... this pass did not compile full first-order
  subdivision lists for any of the five countries"). All five countries' lists were **researched fresh for this
  file** via WebSearch (Wikipedia's Regions-of-X articles and Kazakhstan's own national statistics agency,
  stat.gov.kz). Tajikistan's five-unit breakdown and Karakalpakstan's status **were** already given in the two
  surveys (frameworks §3.5; material §2.3, §6) and are carried forward unchanged.
- **Population figures are genuinely incomplete, by design rather than oversight.** Kazakhstan (all 21 units)
  and Tajikistan (all 5 units) are fully sourced. Uzbekistan, Turkmenistan and Kyrgyzstan are **partially**
  sourced — several of Uzbekistan's viloyats, all of Turkmenistan's welayat, and Batken/Osh City in Kyrgyzstan
  have no population figure in this pass and are flagged ⚠️ in `subdivisions.csv` rather than estimated.
  **Turkmenistan's blank column is itself a finding, not a gap in this file's effort**: the country's own
  statistical opacity (frameworks survey §3.3's "most isolated of all former Soviet states" finding) appears to
  extend to basic sub-national demographic publishing — this pass could not find a single disaggregated welayat
  population figure from any source, which is unusual relative to how readily the other four countries'
  region-level data surfaced.
- **The Fergana Valley's treatment as one broad sphere (S1) plus eight separate point-enclaves, rather than
  either alone**, is this file's own design decision, made explicitly because the frameworks survey (§2) flags
  the problem but does not prescribe a solution ("this needs its own design decision at Stage 3"). The
  alternative this file rejected: folding the enclaves into S1's own territory description rather than drawing
  them separately. Rejected because the enclaves' whole significance is that they are **not** contiguous with
  their own country's territory — collapsing them into a regional sphere would erase the exact geographic fact
  that makes them worth drawing at all.
- **S1's exact regional membership** (which of Uzbekistan's, Kyrgyzstan's and Tajikistan's first-order units
  count as "the valley") is this file's own reading of the frameworks survey's generic references to "the
  Fergana Valley" and its specific enclave locations, not an enumerated region list from either survey. Medium
  confidence, flagged as such in `spheres.csv`.
- **S2 (the Uyghur diaspora sphere) is included as a drawable option, not a settled recommendation** — the
  frameworks survey (§8.2) raises the question explicitly without deciding it, the same "flagged, not resolved"
  posture the survey uses throughout. This file takes no position on whether the author should draw it.
- **Kazakhstan's 2022 three-way region split** (Abai from East Kazakhstan, Jetisu from Almaty Region, Ulytau
  from Karaganda) was **not** mentioned in either survey and was confirmed fresh via WebSearch — flagged in each
  affected row's `notes` so the split's recency is visible on the map data itself, not just in this README.
- **Baikonur's inclusion as its own first-order unit** is this file's own judgment call, grounded in its real,
  distinctive Russian-leased legal status (through 2050) — genuinely unlike an ordinary Kazakh city, and
  arguably closer in kind to an enclave than a subdivision. Included as a subdivision rather than a point-marker
  because, unlike the Fergana enclaves, it is not surrounded by a *different* country's population living under
  Kazakh sovereignty — it is the reverse (a piece of Kazakh sovereign territory administered by a different
  country) — a distinct enough case that treating it identically to the Fergana enclaves would blur two
  different phenomena. Flagged for the author's own drawing-convention decision at Stage 4.

---

## Rendering Conventions

**Match this project's established house style** (see the Mainland Southeast Asia and Russia map-data
packages' own render scripts for concrete implementation reference, if useful — this is a different region, not
a shared codebase):

- **Lambert azimuthal equal-area projection**, re-centered for this region — something like
  `+proj=laea +lat_0=45 +lon_0=65 +datum=WGS84 +units=m` is a reasonable starting point (roughly the geographic
  center of the five countries), not a fixed requirement.
- **Solid country fills, white-then-dark-line national borders** (a ~1.8pt white casing under a ~0.5pt dark
  line is the pattern used elsewhere in this project) for the hard-border layer.
- **Sphere overlay**: S1's core = solid color at reduced opacity or a distinct hatch across all six named
  regions; S2 (if drawn) = a lighter, more diffuse treatment appropriate to a diaspora rather than a homeland
  population, distinct from S1's own visual weight.
- **The Fergana enclaves**: small unbordered dots with leader lines and one shared legend entry — see the
  dedicated section above. Never a hatched region, never a border.
- **Serif display font for nation/sphere names, sans-serif for cities and captions** — matches the
  Crimson Text / Lato pairing used elsewhere in the project, though any comparable serif/sans pairing is fine.

**One map is expected, not a multi-map series** — neither survey contains a decided sequence of post-collapse
mergers, splits or unifications for these five countries, the same present-day-snapshot scoping this project
settled on for Mainland Southeast Asia rather than East Asia's dated multi-era approach.

---

## The Files

| File | Rows | What it is |
|---|---|---|
| `subdivisions.csv` | 55 | Every first-order subdivision of Kazakhstan (21), Uzbekistan (14), Turkmenistan (6), Kyrgyzstan (9) and Tajikistan (5) — the hard-border layer. |
| `spheres.csv` | 2 | S1 (Fergana Valley Mosaic, settled) and S2 (Uyghur Diaspora, author's call). |

## Column Reference — `subdivisions.csv`

| Column | Meaning |
|---|---|
| `nation` | One of the five countries. **The primary key for the hard-border fill.** |
| `subdivision_name` | The first-order unit's real name. |
| `subdivision_type` | Region (oblys/viloyat/welayat/oblast) / City of republican significance / Independent city / Autonomous republic / Autonomous region / Capital city / Republican-subordination district group / City with special status — varies by country's own terminology; see individual rows. |
| `population` | Sourced where a current figure was found (all of Kazakhstan and Tajikistan; part of Uzbekistan and Kyrgyzstan). **Blank and ⚠️-flagged elsewhere** — see "What's Sourced" above, especially Turkmenistan's total absence of regional figures. |
| `color_hex` | One fixed color per country (five total) — solid fill for the hard-border layer. |
| `notes` | Sphere/enclave membership flags, dated-event references, historical notes, and judgment-call flags. **Read before drawing** — this is where most of the actual content lives, especially for Karakalpakstan, Baikonur, and every Fergana-adjacent region. |

## Column Reference — `spheres.csv`

Same core/domain/sphere_territory convention as every other regional map-data package in this project:

| Column | Meaning |
|---|---|
| `sphere_id` | S1–S2. |
| `sphere_name` | Display label. |
| `core_territory` | Strongest presence. **Draw as solid fill or a strong hatch.** |
| `domain_territory` | Clear but lesser presence. **Draw as lighter fill or finer hatching.** |
| `sphere_territory` | Named but out of this map's scope — **label only if the map's extent reaches that far; do not draw territory for it.** |
| `source_section` | Which survey section grounds this row. |
| `confidence` | `high` / `medium` / `low` — same scale as every other regional package. |
| `notes` | Design flags, caveats, and (for S2 especially) a real open design question — read it. |

---

## Suggested Prompt

> Draw a map of Central Asia (Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan) showing each
> country's first-order administrative subdivisions with a solid hard border, colored by `color_hex` from
> `subdivisions.csv`. Overlay the Fergana Valley Mosaic sphere (S1) from `spheres.csv` across its six named
> regions as a broad, diffuse fill or hatch — do not draw it as a hard border. Then place eight small,
> unbordered point-markers with leader lines for the named Fergana Valley enclaves (see the README's dedicated
> table), each labeled with its ethnicity and enclosing country, sharing one legend entry rather than eight.
> Optionally, if the author has decided to include it, add the Uyghur Diaspora sphere (S2) as a lighter,
> diaspora-appropriate overlay across Kazakhstan, Uzbekistan and Kyrgyzstan, labeling but not drawing Xinjiang
> itself. One map only; this is a present-day snapshot, not a historical series.

---

## Caveats

- **Whole first-order subdivisions only** — this rule is absolute throughout the project. The Fergana
  enclaves are the one genuine exception the frameworks survey itself flags as unresolvable by that rule alone
  (§2) — resolved here by drawing them as point-markers rather than territory, not by bending the subdivision
  rule itself.
- **Population data is more incomplete here than in any prior regional package** — see "What's Sourced" above.
  Turkmenistan in particular has zero sourced sub-national population figures, which this file treats as a
  finding about the country's own statistical opacity rather than a gap in research effort.
- **S2 (the Uyghur Diaspora sphere) is explicitly optional** — see its own row in `spheres.csv` and the
  "What's Sourced" section above. This is the first sphere in this project's map-data history offered as a
  take-it-or-leave-it option rather than a settled recommendation.
- **The 2025 Kyrgyz-Tajik border agreement and the Karakalpakstan question are both flagged as live and
  unresolved** — neither survey verified the border agreement's durability, and Karakalpakstan's political
  weight (stay ordinary Uzbek territory, or become its own drawn case like Tuva) is an open author decision,
  not a research gap.
- **Not yet rendered.** Stage 4 (generation) happens later, per the author's own stated destination:
  `y-files/Map Files/Asia (West)/01 initial generations/`.
