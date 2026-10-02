# Mainland Southeast Asia Map Data — for Image Generation

2026-09-26. Machine-readable datasheets derived from
`../../extractions/Mainland Southeast Asia - Mandalas, the Massif and the Tai Continuum (survey).md` (the
frameworks survey) and
`../material-base/Mainland Southeast Asia - Material and Economic Base (survey).md` (the material survey),
formatted so they can be handed to an image-generating model to draw a map.

**This is Stage 3 of this project's five-stage worldbuilding pipeline** (frameworks survey → material survey →
**map data** → generation → naming). See `../../STATUS - Cross-Session Progress Tracker.md` for the full
pipeline and this region's status. Stage 4 (actual rendering) has not happened yet — that's the web UI's job,
not this session's.

**This is a different kind of map from North America or Latin America.** Myanmar, Thailand, Vietnam, Laos and
Cambodia are already five real, present-day sovereign countries. There is no "which nation claims this
territory" decision to make the way there was for the post-war Americas — every subdivision below simply
belongs to the country it already belongs to in the real world. **What this map adds beyond a normal political
map is the mandala.**

---

## The Model: Hard Borders Plus an Overlapping Sphere Layer

Per the frameworks survey (§1.2, author's own decision): **"the mandala is carried natively rather than
flattened. Cores get hard borders; spheres overlap, and the overlaps are correct rather than errors."**

That means two layers, in two files:

1. **`subdivisions.csv`** — the ordinary political layer. Five countries, each with hard, solid-fill national
   borders, built from their real first-order administrative subdivisions (states/regions/provinces/
   centrally-run cities — **whole units only, per this project's absolute rule: never split a province**).
   This is the bulk of the visual weight of the map — five solid, differently-colored countries, borders drawn
   the normal way.
2. **`spheres.csv`** — four cross-border cultural/ethnic zones drawn **on top of** the hard borders as a
   translucent or hatched overlay, **not** as redrawn borders. Each sphere uses the same
   `core_territory` / `domain_territory` / `sphere_territory` convention already used throughout this project
   (see the Latin America and East Asia map-data READMEs for the same pattern): core = solid fill/strongest
   presence, domain = lighter fill or hatching, sphere = a dotted outline or faded edge. **Overlaps between
   spheres, and between a sphere and more than one country's hard territory, are expected and correct — do not
   resolve them into a single owner.**

**Expect fewer clean borders and more graduated edges than the North America or East Asia maps.** That's the
point, per the survey: "a reader should be able to see that this region's polities work differently, because
they did."

---

## The Four Spheres

| ID | Name | What it captures |
|---|---|---|
| **S1** | The Tai Continuum | The broadest layer — ~93 million Tai-Kadai speakers (Thai, Lao, Shan, and others) across the region. An ethnolinguistic backbone, not a political claim. |
| **S2** | Isan / the Lao Nation Cut by a Border | The sharpest finding in the survey: ~22 million ethnic Lao live in Thailand's Isan region, roughly three times Laos's own population. **See the ⚠️ note in `spheres.csv` — this one needs a real design decision, not just a fill color; read it before drawing.** |
| **S3** | Zomia / the Southeast Asian Massif | The highlands above ~300 m, cutting across all five countries' northern/interior terrain. Laos *is* this sphere (per the survey, not merely contains it); the other four countries contribute a highland domain each. |
| **S4** | The Khmer Krom | The smallest and most geographically precise sphere — ~1.32 million ethnic Khmer inside Vietnam's Mekong Delta, in specific provinces that absorbed the historically Khmer-majority areas in the 2025 reform. |

Full detail, sourcing, and confidence levels for each are in `spheres.csv` — read the `notes` column before
drawing; several rows flag a judgment call this file made that the surveys themselves didn't enumerate (see
"What's Sourced vs. What's This File's Own Judgment Call" below).

---

## The Wa — a Fifth Thing, and It Is Not a Sphere

**Do not draw the Wa Self-Administered Division, its second UWSA-held bloc, or the four other Self-Administered
Zones inside Shan State (Danu, Kokang, Pa Laung, Pa-O) as bordered territory of their own.** They are
second-order subdivisions of Shan State, and this project's whole-first-order-subdivision rule is absolute.
A fifth zone, **Naga**, is a second-order subdivision of **Sagaing Region** instead, not Shan State — corrected
2026-09-26 — and is subject to the same rule (see `subdivisions.csv`'s Sagaing row).

Instead, **follow the exact pattern the East Asia map series already established for Hakka** (44 million
people, no ground, drawn as scattered hatched circles with a leader line and its own legend entry, never a
border — see `../east-asia-map-data/02 maps/README.md`): give the Wa area a **labeled, non-bordered hatch
pattern within Shan State**, with a leader line reading something like *"Wa — de facto self-governing,
China-protected, not separatist"* (the frameworks survey §3.1 is explicit that this is not a secession claim
and should not read as one). Give it its own small legend entry, separate from Shan State's normal fill.

---

## What's Sourced vs. What's This File's Own Judgment Call

Per this project's "research proposes, the author disposes" rule, every place this file went beyond what the
two surveys themselves say is flagged in the relevant CSV row and summarized here:

- **Myanmar's 15 first-order units, their populations, the Wa's status, and the mid-2026 civil-war control
  snapshot** are all directly from the frameworks survey (§3.1) — no additional research needed or done.
- **Vietnam's 34-unit list, Laos's 18-unit list, and Thailand's 77-unit list** were not enumerated in full in
  either survey (only counts and a few named examples were) and were **researched fresh for this file**
  (Wikipedia, via `WebFetch`). Cross-check against the surveys' own partial lists found no conflicts.
- **⚠️ Cambodia's unit count: this file found 25 total (24 provinces + Phnom Penh), not the 26 the material
  survey states (§2.7, "25 provinces plus Phnom Penh... 26 units").** Independently verified via WebSearch
  against current sources. This reads as an off-by-one in the material survey's own arithmetic (24 provinces,
  not 25), not a new administrative change. **Flagging rather than silently fixing** — the material survey
  itself should probably be corrected to match, but that's a documentation change outside this file's scope.
- **The 2025 Vietnamese province-merger mapping for the three Khmer Krom source provinces** (which new unit
  absorbed Sóc Trăng, Trà Vinh and Kiên Giang) was **not** in either survey and was researched fresh: Sóc Trăng
  → Cần Thơ, Trà Vinh → Vĩnh Long, Kiên Giang → An Giang. Medium confidence — independently sourced, not
  cross-checked against a primary legal document.
- **Every specific province list assigned to Zomia/Massif (S3) beyond Laos** — Myanmar's Shan-State-only
  scoping, Thailand's eight Upper Northern provinces, Vietnam's seven northern-highland provinces — is **this
  file's own extrapolation** from the survey's generic language ("the Thai highlands," "northern Vietnam," "the
  Shan Hills"), not an enumerated list from the survey itself. Confidence is marked medium/low on these rows in
  `spheres.csv` for exactly this reason. **The author should treat these specific province boundaries as a
  proposal, not a finding.**
- **Whether Myanmar's other highland ethnic states (Kachin, Chin, Kayah, Kayin) belong in Zomia/Massif** is
  left as an **explicitly undrawn optional extension** — Scott's broader thesis (frameworks survey Part 2)
  would support it, but the survey's own Part 3 text names only "the Shan Hills" for Myanmar, so this file
  defaults to the narrower, survey-grounded reading.

---

## Rendering Conventions

**Match this project's established house style** (see `na_nations.py` and the Latin America `nations.py`
scripts for the concrete implementation, if useful as a reference — this is a different region, not a shared
codebase, so don't over-import their specifics):

- **Lambert azimuthal equal-area projection**, re-centered for this region — the other regional scripts use
  `+proj=laea +lat_0=<region center> +lon_0=<region center> +datum=WGS84 +units=m`; for mainland Southeast
  Asia something like `lat_0=15 lon_0=100` (roughly the geographic center of the five countries) is a
  reasonable starting point, not a fixed requirement.
- **Solid country fills, white-then-dark-line national borders** (a ~1.8pt white casing under a ~0.5pt dark
  line is the pattern used elsewhere in this project) for the hard-border layer.
- **Sphere overlay**: core = solid color at reduced opacity or a distinct hatch, domain = lighter/thinner
  version of the same, sphere = dotted outline only. Use a consistent hatch/color per sphere across the whole
  map, distinct from the five national fill colors in `subdivisions.csv` so the two layers read as separate
  systems (nations vs. spheres) rather than competing for the same visual vocabulary.
- **The Wa**: hatched, unbordered, leader-lined, its own legend entry — see above.
- **Serif display font for nation/sphere names, sans-serif for cities and captions** — matches the
  Crimson Text / Lato pairing used elsewhere in the project, though any comparable serif/sans pairing is fine.

**One map is expected, not a multi-map series — but this is a scoping question for the author, not a closed
one.** The frameworks survey's Part 3 is explicitly "a description of present ground, not a proposal" — a
single snapshot, not a designed post-collapse political timeline. Unlike East Asia, **neither survey contains
a decided sequence of post-collapse mergers, splits or unifications** for these five countries — the material
survey's own forward-looking material (§3–4) is about what infrastructure/food/economy survives a collapse,
not about how the five countries' borders might change over time the way East Asia's nine Han states
progressively unified into the Sinian Federation. That decided-sequence design work is what produced East
Asia's A→F six-map series, and it hasn't happened here yet.

**⚠️ That said, the author has already created `y-files/Map Files/Asia (Southeast)/` with a folder layout that
closely mirrors East Asia's finished structure** — including `03 official timeline years/` and
`04 timeline staging/` (with `Place_Name/` and `DISTILLED - ready for Timeline repo/` subfolders), the same
scaffolding East Asia ended up filling with its dated six-map series. That's a real signal the author may want
this region to eventually get the same dated multi-era treatment — but it is **not, by itself, proof of intent
distinct from the author's standard pre-made folder scaffolding** (North America's own `02 reorganization` has
eleven mostly-empty follow-up folders as of this same session, regardless of whether a timeline was ever
planned there). **This file was built as a single present-day map because that's what the two surveys
currently support — if the author wants a multi-era post-collapse timeline instead, that needs a dedicated
design pass first** (deciding what political changes happen, in what order, on what timeline — the same kind
of work East Asia's own map-data folder shows was done for that region), not something this map-data package
can retrofit on its own. Flagged for the author to decide before Stage 4 rendering, not decided here.

### An optional second map, not yet decided

The frameworks survey's §3.1 includes a dated (mid-2026), state-by-state Myanmar civil-war control snapshot
(junta ~21–33%, resistance/ethnic forces ~42%, contested remainder) that this file did **not** build into the
main map — it's a live, fast-changing situation the survey itself calls "dated and will be stale within a
year," and folding it into the region's one settled map would date the whole thing. **If the author wants it,
a second, Myanmar-only map showing that control snapshot (with an explicit "as of mid-2026" caption, the same
treatment the East Asia series gives no dates to at all, deliberately opposite) would be a natural companion
piece — but that's an open option, not built here.**

---

## The Files

| File | Rows | What it is |
|---|---|---|
| `subdivisions.csv` | 169 | Every first-order subdivision of Myanmar (15), Thailand (77), Vietnam (34), Laos (18) and Cambodia (25) — the hard-border layer |
| `spheres.csv` | 4 | The mandala overlay — Tai Continuum, Isan/Lao, Zomia/Massif, Khmer Krom |

## Column Reference — `subdivisions.csv`

| Column | Meaning |
|---|---|
| `nation` | One of the five countries. **The primary key for the hard-border fill.** |
| `subdivision_name` | The first-order unit's real name. |
| `subdivision_type` | State / Region / Province / Centrally-run city / Prefecture / Autonomous Municipality / Special Administrative Area / Union Territory — varies by country's own terminology. |
| `population` | Only sourced where the frameworks survey itself gave a figure (all of Myanmar, and Cambodia's largest provinces from the material survey). **Blank elsewhere — not researched at subdivision level for Thailand, Vietnam or Laos; only country-wide totals exist in the surveys.** |
| `color_hex` | One fixed color per country (five total) — solid fill for the hard-border layer. |
| `notes` | Sphere membership flags, dated-snapshot warnings (⚠️), historical notes, and judgment-call flags. **Read before drawing — this is where most of the actual content lives.** |

## Column Reference — `spheres.csv`

Same core/domain/sphere_territory convention as the Latin America and East Asia map-data files:

| Column | Meaning |
|---|---|
| `sphere_id` | S1–S4. |
| `sphere_name` | Display label. |
| `core_territory` | Strongest presence. **Draw as solid fill or a strong hatch.** |
| `domain_territory` | Clear but lesser presence. **Draw as lighter fill or finer hatching.** |
| `sphere_territory` | Named but out of this map's scope (usually China or India) — **label only if the map's extent reaches that far; do not draw territory for it.** |
| `source_section` | Which survey section grounds this row. |
| `confidence` | `high` / `medium` / `low` — same scale as the Latin America file. |
| `notes` | Design flags, caveats, and (for S2) a real open design question — read it. |

---

## Suggested Prompt

> Draw a map of mainland Southeast Asia (Myanmar, Thailand, Vietnam, Laos, Cambodia) showing each country's
> first-order administrative subdivisions with a solid hard border, colored by `color_hex` from
> `subdivisions.csv`. Then overlay the four spheres from `spheres.csv`: draw each sphere's `core_territory` as
> a strong fill or hatch, `domain_territory` lighter, and label `sphere_territory` without drawing it. Spheres
> are expected to overlap each other and to span more than one country — do not resolve the overlaps into a
> single owner. Give the Wa area within Shan State its own hatched, unbordered, leader-lined label (see the
> README's "The Wa" section) — do not draw it as a bordered region. One map only; this is a present-day
> snapshot, not a historical series.

---

## Caveats

- **Whole first-order subdivisions only** — this rule is absolute throughout the project and is followed
  exactly here; the fifteen-Myanmar-unit case, the Wa's non-territorial treatment, and the sphere overlay
  system are all designed specifically so nothing ever needs a province split to represent.
- **⚠️ UPDATED 2026-09-26 — this is no longer true.** This map originally made no partition decisions; every
  subdivision belonged to the country it already, really belonged to, and the only creative content was the
  sphere overlay and the Wa treatment. **That's changed**: Thailand's "Deep South" (Pattani, Yala, Narathiwat)
  is now author-settled to separate from Thailand after the 2083 war, in some form (independence or autonomy
  within Thailand — not yet decided which; see below). This is the mainland map's first-ever partition
  decision, and the map/CSVs need updating to reflect it — not yet done in this file.
- **A fifth sphere, S5, "The Patani Malay World," connects this map to the Maritime Southeast Asia map for
  the first time** — see `spheres.csv`. Core: Thailand's Pattani/Yala/Narathiwat. The domain (Malaysia's
  Kelantan and Terengganu) is real drawable territory, just not on this map — it's labeled as continuing onto
  the Maritime companion map, the same convention already used for the Tai Continuum's reach into
  southern China/Northeast India, just applied to another map in this same project for the first time.
- **Confidence varies row by row** — see "What's Sourced vs. What's This File's Own Judgment Call" above before
  treating any sphere boundary as settled.
- **The Myanmar civil-war control picture is dated (mid-2026) and explicitly not built into this map** — see
  "An optional second map" above.

## The Deep South / Patani Question (added 2026-09-26)

**Author-settled: Thailand's Pattani, Yala, and Narathiwat provinces separate from Thailand after the 2083
war, in some form.** This follows real-world research into the actual situation, prompted by the author
initially proposing the Deep South simply joins Malaysia — checked and found not well-supported, the same way
a parallel West Papua/Papua New Guinea merger proposal was checked on the Maritime map:

- **The actual insurgent movement (BRN, Barisan Revolusi Nasional) wants independence, not annexation by
  Malaysia** — a real, active goal since the 1960s, over 7,000 deaths pursuing it since 2004. Recent peace
  talks (as of 2026) show BRN signaling openness to **real autonomy within Thailand** instead (Yawi language
  recognition, local control over education/culture/economic development) — at no point does the movement
  itself seek union with Malaysia.
- **Malaysia's own government explicitly rules out annexation**: official policy states Malaysia "has no
  territorial claims on Southern Thailand and has consistently refused to support separatist aspirations by
  the local ethnic Malays, maintaining that the territory is an integral part of Thailand." Malaysia's real
  role, since 2013, is as a **peace-talk mediator** — driven by border-security concerns (the provinces abut
  Kelantan, Perlis, Kedah and Perak), not territorial ambition.
- **This is the same pattern found for West Papua/PNG**: real ethnolinguistic kinship and real neighborly
  involvement, but an explicit rejection of annexation from the neighboring state itself. **Settled the same
  way**: the Deep South separates on its own merits, with a later union with Malaysia left open as an
  undecided possible development (the same "start separate, leave a later merger open" pattern already used
  for West Papua/PNG and, earlier still, for Guyana/Suriname/French Guiana in the Latin America work) — not
  asserted as the outcome.
- **✅ SETTLED, 2026-09-26: independence, not autonomy** — researched to the same depth as Aceh's equivalent
  question, and the answer runs the *opposite* direction. Where Aceh had a real, already-functioning 20-year
  autonomy track record (the 2005 Helsinki Agreement) to draw on, **Thailand has never granted an ethnic
  minority region real autonomy anywhere in its modern history** — the only two special administrative regions
  it has ever created (Bangkok, 1972; Pattaya, 1978) are geographic, not ethnic, and neither has real fiscal
  autonomy. Precolonial Siam did leave Patani's rulers largely alone, but that ended hard with Chulalongkorn's
  centralizing "Thaification" reforms (1890s–1900s). The current peace process is real but fragile and
  unproven: a Feb 2024 roadmap missed its own end-of-2024 deadline, talks were then suspended a full year, and
  only resumed 8 December 2025 — the first time since 2013 BRN has even publicly stated a political objective
  (now "self-government"/a special administrative zone, not full independence — a real shift, but still just a
  demand). **A structural obstacle Aceh's case didn't have**: Thailand's civilian government doesn't fully
  control the policy — security in the Deep South has been under direct military martial-law control since
  2005, with the military holding an institutional interest in not devolving it, unlike Indonesia's
  civilian-led 2005 breakthrough with Aceh. Net: Thailand has zero successful autonomy precedent plus a
  military veto in the way, the reverse of Aceh's grounding — independence is the better-supported outcome.
- **⚠️ Kedah and Perlis are a separate, distinct connection, not folded into this**: both are heavily Muslim
  (78.5%/87.8%), but the real distinction from Kelantan/Terengganu is linguistic, not a difference in
  Siamese-era status — corrected 2026-09-26. The 1909 Anglo-Siamese Treaty transferred all four states
  (Kedah, Perlis, Kelantan, Terengganu alike) from Siam to Britain, so that treaty isn't what separates them.
  Kedah and Perlis speak Kedah Malay, a different dialect from Pattani/Yala/Narathiwat's shared
  Kelantan-Pattani Malay and Patani-sultanate history with Kelantan/Terengganu specifically. Not built into
  any sphere or partition decision here.

**Not yet applied to `subdivisions.csv`**: this file still shows Pattani/Yala/Narathiwat as ordinary Thailand
provinces. Updating the hard-border layer to draw them as their own independent nation is real Stage 3 rework —
the last open question (autonomy vs. independence) is now closed, so this is ready to build.
