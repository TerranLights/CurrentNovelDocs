# Maritime Southeast Asia Map Data — for Image Generation

2026-09-26. Machine-readable datasheets derived from
`../../extractions/Maritime Southeast Asia - the Austronesian Tier, the Melaka Diaspora and the Colonial Line (survey).md`
(the frameworks survey) and
`../material-base/Maritime Southeast Asia - Material and Economic Base (survey).md` (the material survey),
formatted so they can be handed to an image-generating model to draw a map.

**This is Stage 3 of this project's five-stage worldbuilding pipeline** (frameworks survey → material survey →
**map data** → generation → naming). See `../../STATUS - Cross-Session Progress Tracker.md` for the full
pipeline and this region's status. Stage 4 (actual rendering) has not happened yet — that's the web UI's job,
not this session's.

**This is a different kind of map from mainland Southeast Asia, which is itself already different from North
America or Latin America.** Five of this region's six polities (Philippines, Malaysia, Brunei, Singapore,
Timor-Leste) are, like the mainland countries, real present-day sovereign states kept whole — no "which nation
claims this territory" decision. **Indonesia is the one exception, and it is a real one**: the author has
decided Indonesia gets its own internal division, the way East Asia's Sinian Federation was drawn as a
federation of linguistic nations rather than one solid block. That decision is now made in full:

---

## The Two Author Decisions That Built This File (2026-09-26)

1. **Indonesia's internal division: island-group blocs, confirmed.** The frameworks survey's own
   recommendation (§3.1.5) — group the 38 provinces into island-group blocs rather than a finer,
   31-ethnicity-map-based division — is adopted as-is.
2. **Aceh and West Papua both get full separate hard-bordered blocks**, carved out of their island bloc, not a
   sphere/overlay treatment. This is a stronger, more visible distinction than the mainland package's Wa/Isan
   treatment — both are drawn as their own solid-color polity, not a hatch pattern inside someone else's color.

**Applying decision 2 required resolving one real ambiguity the frameworks survey left open, stated here so it
isn't rediscovered:** the survey uses "West Papua" two ways — as the name of the single administrative
province formally called *Papua Barat*, and as a political/civilizational shorthand for Indonesia's entire
Melanesian-populated Papua-island territory (all six current provinces). Headline 2, §1.1 and §3.1.3 all use it
in the second, broader sense — discussing "Papuans" and Indonesia's "hold on the territory" as a whole, citing
the Grasberg mine (which sits in Central Papua, not the administrative Papua Barat province) as the material
stake. **Resolution: the whole Papua bloc — all six provinces — is "West Papua" for this map.** There is no
separate "Papua bloc minus West Papua" remainder; see `subdivisions.csv`'s own notes on the Papua row. (The
survey's own §3.1.5 undercounts the Papua-region provinces as "four provinces post-2022, plus West Papua
province" — five. The real, current, correct total is six, post the second 2022-23 split that created Southwest
Papua from the former Papua Barat province. Corrected here, not silently — see the Southwest Papua row's own
note.)

**Indonesia's final bloc breakdown: 8 blocks, all 38 provinces accounted for, none split.**

| Bloc | Provinces | Note |
|---|---|---|
| Sumatra | 9 (all of Sumatra except Aceh) | |
| **Aceh** | 1 | Carved out per decision 2 — case rests on tier-2/religious-political grounds, not tier-1 ethnicity (Acehnese are ~70% Austronesian like their neighbors) |
| Java | 6 | Holds ~56% of Indonesia's population on ~7% of its land (frameworks survey headline 4) |
| Kalimantan | 5 | Indonesian Borneo |
| Sulawesi | 6 | |
| Maluku | 2 | The historical Spice Islands |
| Nusa Tenggara & Bali | 3 | |
| **West Papua** | 6 | Carved out per decision 2 — the whole Papua-region, per the resolution above |

**✅ Author-confirmed 2026-09-26**: this file's BARMM judgment call stands as originally drawn. The
frameworks survey names the **Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)** as directly analogous
to Bangsamoro-tier autonomy — headline 7 calls it "this survey's Myanmar — the one place the lines already
exist." **BARMM is drawn as its own distinctly-noted region within the Philippines** (subdivision_type =
Region, same as the other 17), **not** a full separate nation-tier block and **not** a sphere overlay.
Reasoning: BARMM is already a clean, first-order-subdivision-respecting unit (five whole provinces plus one
independent city) — structurally identical to how Myanmar's own ethnic states sit as ordinary colored
subdivisions within Myanmar on the mainland map, not carved out as separate nations. A sphere overlay would be
the wrong tool here too, since sphere/overlay elsewhere in this project (Isan, Zomia, Khmer Krom, the Tai
Continuum) is reserved for zones that *don't* respect clean province boundaries or that span *multiple*
countries — Bangsamoro does neither; it's a whole-province union entirely inside one country.

**✅ RESOLVED 2026-09-26** — the BARMM/Sulu population discrepancy this file originally flagged is now closed.
The frameworks survey's original **5.69 million (2024 census)** figure for BARMM predates **Executive Order
No. 91 (30 July 2025)**, which formally excluded **Sulu** from BARMM (final Philippine Supreme Court ruling,
November 2024) and transferred it in full, including every municipality and barangay, to Region IX (Zamboanga
Peninsula). The post-exclusion BARMM population, **4,545,486** (already used in `subdivisions.csv`), and the
Zamboanga Peninsula row's population are now understood to be consistent — the ~1.1 million difference between
BARMM's two cited figures is Sulu's population moving to Zamboanga Peninsula, not a data error.

---

## The Model: Hard Borders Plus an Overlapping Sphere Layer

Same convention as the mainland package (frameworks survey §1.2, inherited from the mainland survey's own
decision, and confirmed as transferring "even more directly" here since the mandala's own founding examples —
Srivijaya, Majapahit — were already maritime): **cores get hard borders; spheres overlap, and the overlaps are
correct rather than errors.**

1. **`subdivisions.csv`** (91 rows, corrected 2026-09-26 from 90 — Atauro added as its own Timor-Leste
   municipality) — the hard-border layer. Thirteen politically distinct fill colors: eight
   for Indonesia's blocs (each a genuinely separate polity per the author's decision) plus one each for the
   Philippines (including BARMM, same color as the rest of the country — see above), Malaysia, Brunei,
   Singapore, and Timor-Leste.
2. **`spheres.csv`** (3 rows) — cross-border/cross-bloc cultural zones drawn on top, not as redrawn borders:
   the Maritime Mandala, the Overseas Chinese Commercial Diaspora, and Linguistic Wallacea. **One sphere fewer
   than the mainland package's four** — Bangsamoro and Sabah/Sarawak turned out to be better served by hard
   borders or ordinary subdivision notes than by the sphere mechanism, since (unlike the mainland's
   Isan/Zomia/Khmer Krom/Tai Continuum) neither genuinely cuts across a province line or spans multiple
   countries. Aceh and West Papua are full separate hard-bordered blocks by author decision, but Aceh is *also*
   in the Maritime Mandala's domain (added 2026-09-26) — a full block and sphere membership aren't mutually
   exclusive, since the sphere layer marks cultural/trade reach, not political sovereignty.

---

## The Three Spheres

| ID | Name | What it captures |
|---|---|---|
| **S1** | The Maritime Mandala (Srivijaya / Majapahit) | Precolonial thalassocratic authority radiating from Sumatra (Srivijaya) and Java (Majapahit) across the wider trade network — soft, overlapping, never a hard claim. **This file's own reasoned construction** — the frameworks survey confirms the vocabulary applies but does not propose geometry (§1.2); see confidence notes. **Domain updated 2026-09-26** to add Aceh (a central Malacca Strait trade node, Samudra Pasai/Aceh Sultanate) and Bali (Majapahit's living cultural heir) — both author-confirmed additions; the sphere originally omitted them entirely. |
| **S2** | The Overseas Chinese Commercial Diaspora | Singapore (~75.5%, the region's one Chinese-majority polity) and Malaysia (~23%, corrected 2026-09-26 from an earlier ~34%/1960s-vintage figure) as core/domain; Indonesia and the Philippines named as present but diffuse (~3% and ~1-2%), with no sub-national footprint sourced. |
| **S3** | Linguistic Wallacea | The one sphere with real, specific, peer-reviewed-sourced geography (Schapper 2015/2017) — East Nusa Tenggara, Timor-Leste, Maluku, and (added 2026-09-26) **Sumbawa specifically** as core; the Bird's Head/Neck/Cenderawasih Bay portion of the West Papua bloc as domain. **Does not** follow the 1859 biogeographic Wallace Line — explicitly excludes Lombok (and Sulawesi), extends further into New Guinea. Sumbawa shares a province with Lombok, so including one and not the other needs a schematic sub-province patch, not a whole-province swap — see the renderer's own approach. |

Full detail, sourcing, and confidence levels for each are in `spheres.csv` — read the `notes` column before
drawing.

---

## What's Sourced vs. What's This File's Own Judgment Call

Per this project's "research proposes, the author disposes" rule:

- **Indonesia's 38-province list and 2024/2025 provincial population figures** were not enumerated in either
  survey (only national totals and a partial ethnic breakdown were) and were **researched fresh for this file**
  (Wikipedia/`WebFetch`). Summing this file's bloc-level totals against the frameworks survey's own cited
  "~285 million (2026 estimate)" national figure lands within rounding (~284.4 million) — no conflict found.
- **The Philippines' 18-region list and 2024-census regional populations** were researched fresh the same way.
  The BARMM/Sulu population discrepancy (above) was found in the process, not silently smoothed over.
- **Malaysia's 13-state/3-federal-territory list and 2024 DOSM population estimates** were researched fresh;
  summed total (~34.06 million) matches the official "34.1 million" 2024 estimate within rounding.
- **Brunei's district-level and Timor-Leste's municipality-level populations are NOT individually sourced this
  pass** — both countries' 4/13-unit lists come directly from the frameworks survey (§3.4, §3.6), but
  per-district/per-municipality population breakdowns were not researched. Left blank in `subdivisions.csv`
  rather than estimated, per this project's own "flag the gap, don't fabricate" convention.
- **✅ The West Papua boundary resolution** (all six Papua-region provinces, not just the administrative Papua
  Barat province) — this file's own reasoned resolution of a real ambiguity in the frameworks survey's own
  language, **author-confirmed 2026-09-26**. No longer an open judgment call.
- **✅ BARMM's treatment as an ordinary Philippines subdivision, not a sphere or a full block** — this file's
  own judgment call, made by analogy to Myanmar's ethnic-state treatment on the mainland map,
  **author-confirmed 2026-09-26**. No longer open.
- **Sphere S1's geometry (Maritime Mandala)** is this file's own construction — the frameworks survey
  explicitly declines to propose specific sphere geometry for it. Confidence marked low-medium throughout.
- **Sphere S2's Indonesia/Philippines sub-national footprint** is a placeholder ("present but diffuse"), not a
  mapped concentration — the frameworks survey explicitly did not research the overseas-Chinese population's
  internal geographic distribution.

---

## Rendering Conventions

**Match this project's established house style**, same reference points the mainland package used
(`na_nations.py`, the Latin America `nations.py` scripts, and the mainland package's own README) — a different
region, not a shared codebase, so don't over-import their specifics:

- **Lambert azimuthal equal-area projection**, re-centered for this region — something like
  `+proj=laea +lat_0=-2 +lon_0=115 +datum=WGS84 +units=m` (roughly the geographic center of the six polities)
  is a reasonable starting point, not a fixed requirement. **This region spans both hemispheres and a very wide
  longitude range** (Sumatra to West Papua is over 5,000 km east-west) — check the projection doesn't distort
  badly at the map's own edges before finalizing.
- **Solid country/bloc fills, white-then-dark-line borders** (~1.8pt white casing under a ~0.5pt dark line, the
  pattern used elsewhere in this project) for the hard-border layer — applies to all thirteen fill colors,
  including the border between Aceh and Sumatra and between the West Papua bloc and the rest of Indonesia, which
  should read with the same visual weight as an international border despite both sides being "Indonesia" in
  the real world.
- **Sphere overlay**: core = solid color at reduced opacity or a distinct hatch, domain = lighter/thinner
  version, sphere_territory = label only (S3 has none to label; S1 and S2 both name out-of-scope reach, see
  `spheres.csv`). Use a consistent hatch/color per sphere, distinct from the thirteen fill colors so the two
  layers read as separate systems.
- **The Oecusse-Ambeno exclave**: draw as a detached, non-contiguous piece of Timor-Leste's color, sitting
  inside Indonesian West Timor (the East Nusa Tenggara province, in the Nusa Tenggara & Bali bloc) — do not let
  it read as a printing error or an accidental gap in Indonesia's territory. A small inset or callout box may
  help at this map's likely scale, the same way the DMZ got its own detail map in the North America package.
- **Serif display font for nation/bloc/sphere names, sans-serif for cities and captions** — matches the
  Crimson Text / Lato pairing used elsewhere in the project, though any comparable serif/sans pairing is fine.

**One map is expected, not a multi-map series**, for the same reason the mainland package gives: neither survey
contains a decided sequence of post-collapse political changes over time. Unlike the mainland region, this
region's own frameworks survey doesn't flag the same folder-scaffolding ambiguity — but the same underlying
question applies (check `y-files/Map Files/Asia (Southeast)/` for how the author is treating the mainland
region's timeline question before assuming this one should match or differ).

---

## The Files

| File | Rows | What it is |
|---|---|---|
| `subdivisions.csv` | 91 | Every first-order subdivision, at the bloc/country's chosen resolution: Indonesia (38 provinces across 8 blocs), Philippines (18 regions), Malaysia (16: 13 states + 3 federal territories), Brunei (4 districts), Singapore (1 — the whole country), Timor-Leste (14 municipalities, corrected 2026-09-26 from 13 — Atauro split from Dili in 2022) |
| `spheres.csv` | 3 | The Maritime Mandala, the Overseas Chinese Commercial Diaspora, Linguistic Wallacea |

## Column Reference — `subdivisions.csv`

| Column | Meaning |
|---|---|
| `nation` | The hard-border fill's primary key — one of Indonesia's 8 blocs, or one of the other 5 countries. |
| `subdivision_name` | The first-order unit's real name. |
| `subdivision_type` | Province / Region / State / Federal Territory / District / City-state / Municipality — varies by country's own terminology. |
| `population` | Sourced fresh this pass for Indonesia, the Philippines and Malaysia (see above); left blank for Brunei and Timor-Leste at this resolution, and given as one whole-country figure for Singapore. |
| `color_hex` | One fixed color per bloc/country (13 total) — solid fill for the hard-border layer. |
| `notes` | Bloc/sphere-membership flags, the West Papua/BARMM/Sulu judgment calls, dated-ruling and dated-data warnings (⚠️), and historical context. **Read before drawing.** |

## Column Reference — `spheres.csv`

Same core/domain/sphere_territory convention as the mainland, Latin America and East Asia map-data files:

| Column | Meaning |
|---|---|
| `sphere_id` | S1–S3. |
| `sphere_name` | Display label. |
| `core_territory` | Strongest presence. **Draw as solid fill or a strong hatch.** |
| `domain_territory` | Clear but lesser presence. **Draw as lighter fill or finer hatching.** |
| `sphere_territory` | Named but out of this map's scope — **label only if the map's extent reaches that far; do not draw territory for it.** (S3 has none.) |
| `source_section` | Which survey section grounds this row. |
| `confidence` | `high` / `medium` / `low-medium` / `low` — same scale as the other regional files. |
| `notes` | Design flags, caveats, and sourcing detail. |

---

## Suggested Prompt

> Draw a map of maritime Southeast Asia (Indonesia, the Philippines, Malaysia, Brunei, Singapore, Timor-Leste)
> showing thirteen politically distinct fills, colored by `color_hex` from `subdivisions.csv`: Indonesia is
> drawn as eight separate blocs (Sumatra, Aceh, Java, Kalimantan, Sulawesi, Maluku, Nusa Tenggara & Bali, and
> West Papua — each its own hard-bordered polity, not one country), and the other five countries are each drawn
> whole. Build each fill from the real first-order administrative subdivisions listed (province/region/state/
> district/municipality), grouped by the `nation` column. Then overlay the three spheres from `spheres.csv`:
> draw each sphere's `core_territory` as a strong fill or hatch, `domain_territory` lighter, and label
> `sphere_territory` without drawing it where named. Spheres are expected to overlap the hard borders and each
> other — do not resolve the overlaps into a single owner. Draw the Timor-Leste exclave of Oecusse-Ambeno as a
> detached piece of Timor-Leste's color sitting inside Indonesian territory, not a gap or an error. One map
> only; this is a present-day snapshot, not a historical series.

---

## Caveats

- **Whole first-order subdivisions only** — absolute rule, followed exactly: Indonesia's blocs are built from
  whole provinces, never a partial one, including Aceh and the West Papua bloc.
- **⚠️ OPEN, 2026-09-26 — the eight-polity partition below is under review, not settled.** This map draws
  Indonesia split into eight full successor nations, unlike the mainland package's five intact countries. The
  author has since said full 8-way fragmentation is unlikely — a smaller number of genuine breakaways from a
  unified core is more plausible — and real research is needed to settle which, expected to take real time.
  See `DESIGNATIONS - What Each Region on the Map Actually Is.md` for the reasoning and the strongest
  candidates (Aceh, West Papua; Maluku more weakly). **Treat this rendered map as provisional on that point**
  until the research resumes. Everything else on the map — the Philippines, Malaysia, Brunei, Singapore,
  Timor-Leste — belongs to the country it already, really belongs to, and isn't affected by this open question.
- **✅ The West Papua boundary resolution and BARMM's ordinary-subdivision treatment are author-confirmed
  (2026-09-26)** — no longer open. **Sphere S1's entire geometry remains this file's own construction**
  (low-medium confidence, per its own row in `spheres.csv`) — the one item from this list still worth flagging
  before treating it as settled.
- **✅ The BARMM/Sulu population figures are now reconciled** — resolved 2026-09-26 via Executive Order No. 91;
  see above.
- **Brunei's and Timor-Leste's population data is incomplete at this resolution** — see "What's Sourced" above.
