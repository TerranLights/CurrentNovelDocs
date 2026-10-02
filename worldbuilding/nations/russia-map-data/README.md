# Russia — Map Data Package

**Stage 3, round-1 reorganization, 2026-09-27.** Built ahead of the usual pipeline order, on the author's
direct instruction — the companion Stage 2 material survey does not exist yet for Russia (see the Stage 1
survey's own "Open questions" section, which flags this explicitly). Treat this package as a solid territorial
skeleton, not a polished final map — several nations here are genuinely provisional judgment calls, not
researched conclusions, and are flagged as such throughout.

Follows the Stage 1 frameworks survey (`../../extractions/Russia - Federal Fractures and the Far Eastern
Question (survey).md`), which resolved the three border seams East Asia's own map left blank (Outer Manchuria,
Sakhalin/the Kurils, Buryatia/Tuva) and established the tiered-ethnic-identity method this package's original
nation list was built from.

## ⚠️ Round-1 reorganization, 2026-09-27 — supersedes the original Stage 3 first pass

After reviewing the original 20-nation first pass (via `render_map_russia_reference.py`/
`render_map_russia_woodard.py`, the bare nation-boundary review maps, and the separate cultural-regions
document below), the author gave direct restructuring instructions — a genuine political decision round, not
a research update. Full record: `y-files/Map Files/Russia/02 reorganization/01 follow-up/Russia -
Reorganization Decisions (round 1).md` and the exact old-nation→new-nation mapping in
`subdivisions-reorganized.csv` in that same folder. **12 nations now, down from 20**:

- **Country A** *(name not yet decided)* — merges the old Sakha + The Russian Far East + Irkutsk Oblast
  (moved out of the old Eastern Siberia). This resolves the Stage 1 survey's own open Buryatia question by
  folding it into this polity — one of the two options the survey left live.
- **Siberia** — merges the old Western Siberia + Eastern Siberia (minus Irkutsk, which went to Country A).
  The one new nation with a real, final, author-given name.
- **Tuva** — unchanged territory. New canon fact: an economic trade agreement with Mongolia (narrative,
  not a border change).
- **Country C** *(name not yet decided)* — merges the old Urals Republic + Bashkortostan + The Volga
  Republic (minus Volgograd/Astrakhan) + Tatarstan + The Northern Republic, plus four oblasts moved out of
  Russia's own core (Yaroslavl, Vladimir, Ivanovo, Kostroma). By far the largest nation on the map (27
  subdivisions) — extremely culturally/ethnically diverse **by design**: Volga-Ural Turkic, Finno-Ugric and
  Slavic-core territory in one polity, per author instruction. **Tatarstan loses separate-nation status**
  under this plan, worth a second look since it was the Stage 1 survey's strongest non-Caucasus economic
  secession case.
- **Country D** *(name not yet decided)* — merges the old Southern Russia + Kalmykia, plus Volgograd and
  Astrakhan Oblasts (moved out of Country C's constituent set).
- **All six North Caucasus republics now fully independent**, `[P]` flags removed across the board:
  Chechnya, Ingushetia, Dagestan, North Ossetia-Alania, Kabardino-Balkaria, and Karachay-Cherkessia (the
  last three were provisional in the original pass; Karachay-Cherkessia was actually confirmed in a
  follow-up answer after being left off the initial round-1 list).
- **Russia (core)** — unchanged territory minus the four oblasts that moved to Country C.
- **Kaliningrad removed entirely.** No longer a Russian successor state — the author says it'll be absorbed
  into a not-yet-built European nation. Drawn as ordinary neutral background on every map now (the same gray
  as Poland or Lithuania), not colored or labeled as a nation.

**Cross-map seams this reorganization created**: Country C's territory now spans both the West close-up
(European Russia) and reaches into the Urals, which the Central close-up used to cover — since a hard-bordered
nation is drawn in full on only one close-up map in this project's convention, Country C is fully shown on the
West close-up, and its Urals-adjacent subdivisions are drawn on the Central close-up as neutral gray context
(with a "see West close-up" note) purely to avoid a blank gap at the seam. Same treatment for Irkutsk Oblast,
now part of Country A and shown in full on the East close-up, with the Central close-up carrying the same
gray-context treatment on its eastern edge.

## Six scripts, one package

| File | Content |
|---|---|
| `render_map_russia_full.py` | **1 of 4 decorated maps**: the whole country, all 12 nations. Outputs `russia_full_map.png`. |
| `render_map_russia_west.py` | **2 of 4**: European Russia, the North Caucasus (9 nations; Kaliningrad shown as neutral background). Outputs `russia_west_map.png`. |
| `render_map_russia_central.py` | **3 of 4**: Siberia and Tuva (2 nations; Country A/C's bordering territory shown as neutral context). Outputs `russia_central_map.png`. |
| `render_map_russia_east.py` | **4 of 4**: Country A (Sakha, the Russian Far East, and Irkutsk — 1 nation, enormous area). Crosses the antimeridian near the Bering Strait (Chukotka) — same `antimeridian_fix()` technique Oceania's maps established first. Outputs `russia_east_map.png`. |
| `render_map_russia_reference.py` | Bare, undecorated single-map nation-boundary review (no side panel/legend/capitals/sphere) — author-requested, for reviewing `subdivisions.csv`'s territorial decisions on their own, before production-map polish. Outputs `russia_reference_map.png`. |
| `render_map_russia_woodard.py` | Same bare presentation, plus the Mongolic World sphere overlay. Outputs `russia_woodard_map.png`. |
| `render_map_russia_woodard_regions.py` | A separate, earlier-stage document — a genuine Colin Woodard-style *cultural-region* reference (core/domain/sphere confidence shading, historical-basis blurbs, no nations named, no borders settled), matching the Latin America package's own `map-1-full-regions.png` template. Reflects the Stage 1 survey's own framework, not the hard-border political decisions above — **not affected by the round-1 reorganization, left untouched.** Outputs `russia_cultural_regions_map.png`. |
| `subdivisions.csv` | 82 rows — every Russian federal subject (Natural Earth's admin-1 layer) except Kaliningrad (removed, see above), resolved to 12 nations. Shared by all six scripts; each filters to its own subset. |
| `spheres.csv` | 1 row — The Mongolic World (Tuva as its own nation; Kalmykia inside Country D; Buryatia inside Country A). Shared by the four decorated maps plus the Woodard reference; each draws only the slice that falls on it. |
| `fonts/` | Crimson Text and Lato, this project's house typefaces (copied from the Oceania package). |

All scripts share the same `subdivisions.csv`/`spheres.csv` and near-identical drawing logic (generated from
shared templates to keep that logic consistent, then delivered as independent, self-contained scripts — no
runtime dependency between them, matching this project's standard delivery convention).

## The nation list — 12 nations, 82 subdivisions (round-1 reorganization)

**Well-grounded in the Stage 1 survey, unchanged territory** (not provisional): **Russia** (the core/rump
state, minus the four oblasts moved to Country C — Moscow and St. Petersburg, both real federal-budget donor
regions), **Tuva**, **Chechnya**, **Ingushetia**.

**Confirmed fully independent in the round-1 reorganization** (previously `[P]` provisional, flags now
removed): **Dagestan**, **North Ossetia-Alania**, **Kabardino-Balkaria**, **Karachay-Cherkessia** — none of
the last three were researched in the Stage 1 pass beyond being named as open items, and that hasn't changed;
what changed is the author's political decision that all six North Caucasus republics stand as independent
nations regardless.

**⚠️ Genuinely unnamed — the single biggest open item across this whole package**: **Country A**, **Country
C**, **Country D**. All three are real, final, hard-bordered nations on every map — not provisional in the
old political-uncertainty sense, just waiting on names. See the round-1 reorganization section above for
exactly what merged into each one, and `y-files/Map Files/Russia/02 reorganization/01 follow-up/Russia -
Reorganization Decisions (round 1).md` for the full reasoning, including the flagged concern that Country C
absorbing Tatarstan runs counter to the Stage 1 survey's own finding that Tatarstan was the strongest
non-Caucasus economic secession case in the country.

**Excluded entirely, not part of Russia on this map**: **Crimea and Sevastopol** (Natural Earth codes these
under Ukrainian ISO subdivision codes even where its `admin` field follows the real-world 2014 Russian
administrative claim — this project doesn't assert that annexation as settled) and **Kaliningrad** (removed
in the round-1 reorganization — see above, pending a future European nation).

## Kaliningrad — no longer part of this map's nation list

Originally drawn as its own single-subdivision nation in true position (Rosstat treats it as its own economic
region; unlike Hawaii on the North America map, it sits only a few hundred km from the rest of Russia,
comfortably inside the West close-up's own frame, so an inset was never needed). **Removed entirely in the
round-1 reorganization** — the author says it'll be absorbed into a not-yet-built European nation. It's still
drawn on every map (same true position, no inset), but as ordinary neutral background now, the same gray as
Poland or Lithuania — present and outlined, not colored or labeled as a Russian successor state.

## Fixed, 2026-09-27: the North Caucasus capital-label cluster

Grozny (Chechnya), Magas (Ingushetia), Vladikavkaz (North Ossetia), Nalchik (Kabardino-Balkaria), Cherkessk
(Karachay-Cherkessia) and Makhachkala (Dagestan) sit within roughly 150 km of each other in real life —
Vladikavkaz and Magas alone are only ~15km apart — six capital-city labels this close together overlapped
badly at this map's scale (and also collided with their own nations' auto-centroid name labels, e.g.
"CHECHNYA"/"DAGESTAN"), no matter the font size. Originally flagged here as a known, unfixed issue (the
shared four-file template only supported a left/right side flip per label, not enough room to fan six labels
apart); fixed by extending each script's capital-label loop to accept an optional custom horizontal offset and
a vertical offset (in meters) per label, letting this one cluster fan out radially on both the West close-up
and the full overview (the West close-up's own offsets, then scaled ~3x for the full map's wider extent) —
see the `CAPS` dict and the loop right after it in `render_map_russia_west.py` and `render_map_russia_full.py`
for the exact tuning. The Central close-up's own two collisions (Yekaterinburg/"The Urals Republic",
Kyzyl/"TUVA") were fixed the same way. Every capital and nation label across all four maps is now
independently legible; a couple of letter-edges still lightly touch in the West close-up's most crowded corner
(Grozny/CHECHNYA, Magas/Kabardino-Balkaria) but every word reads cleanly — accepted as good enough for a first
pass, the same bar every other region's maps were held to.

## Antimeridian handling — read before editing the East close-up

`render_map_russia_east.py` (and, defensively, all four scripts) shift every geometry's longitude (+360 to any
value < 0) before reprojecting, the same technique and even the same helper function names
(`shift_lon`/`antimeridian_fix`) Oceania's maps established first. Chukotka's own territory crosses 180°E/W
near the Bering Strait — verified correct in the rendered output (Chukotka appears as one contiguous shape,
not split across the frame). **Do not remove this step.**

## Design notes

- **Whole first-order subdivisions only** — the same absolute rule as every other map in this project.
- **Side-panel legend layout**, same `MAP_FRAC` pattern as Oceania and Southeast Asia's maps.
- **`[P]` provisional marker retired after round-1.** All six North Caucasus republics that used to carry it
  are now confirmed independent. **Unnamed nations now carry "— name TBD"** instead (Country A, C, D) —
  plain text, legend only on the four decorated maps, both on-map and legend on the two bare reference maps.
- **Cross-map "neutral context" pattern, new in round-1.** Where a hard-bordered nation now spans what used
  to be two different close-up maps (Country C into the old Urals-Central seam, Country A/Irkutsk into the
  old Eastern-Siberia-Central seam), the *other* map draws that territory in plain neutral gray with a
  "see [X] close-up" note, rather than leaving a blank gap or redundantly re-coloring it. See the round-1
  section above and the `CONTEXT_SUBDIVS` comment in `render_map_russia_central.py`.
- **Population is blank for every row** — not researched this pass, the same known gap Oceania's first Stage 3
  pass carried.
- Rendered and visually reviewed locally (all six scripts checked for label collisions, broken geometry, and
  — specific to round-1 — clean single-polygon unions at every merge, not fragmented pieces with stray
  internal borders left over) — **not yet through a Claude.ai web-UI round-trip.** Treat this as a solid
  pass, not a fully polished final render, the same caveat every other region's Stage 3 work has carried.

## How to run

Same `NE_DIR`/`OUT_DIR` environment-variable convention as every other region's package:

```
export NE_DIR=./ne OUT_DIR=./out
python3 render_map_russia_full.py
python3 render_map_russia_west.py
python3 render_map_russia_central.py
python3 render_map_russia_east.py
python3 render_map_russia_reference.py
python3 render_map_russia_woodard.py
python3 render_map_russia_woodard_regions.py
```

Reuse a pinned Natural Earth download from any other region's official package if a fresh, checksum-verified
copy is needed — no `setup_natural_earth.py` exists in this package yet.

## What's next

- **Names for Country A, Country C and Country D** — the single biggest open item now. Nothing else is
  blocked on this, but every map will need a re-delivery once names are picked (a cheap change: just the
  legend text, the on-map label stays the same short placeholder-free form already).
- **Stage 2 (material survey) for Russia** — genuinely more load-bearing here than for most prior regions,
  per the Stage 1 survey's own closing note. Would resolve most of this package's least-researched tier
  (the bulk of Country C and D's constituent territory) with real research rather than Rosstat-skeleton
  defaults — and might reasonably inform whether the round-1 mergers themselves hold up.
- The North Caucasus capital-label crowding on the West close-up and full overview — fixed to "every word
  reads cleanly," not pixel-perfect (see above); unaffected by round-1 since none of those six republics
  moved.
- Per-subdivision population research, if a future pass wants it.
- Whether Japan's East Asia map entry should carry a Kuril-dispute tension marker — flagged in the Stage 1
  survey as an author's call, not resolved here since it touches East Asia's own finished map.
