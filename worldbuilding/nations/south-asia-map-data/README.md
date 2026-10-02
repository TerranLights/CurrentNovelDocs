# South Asia — Map Data (Woodard-style initial cultural maps)

Stage 3 staging for the region's first-pass **cultural-region maps** (Woodard-style: regions defined by
culture, language and settlement history; present-day political borders are thin reference lines only).
Rendered maps live outside the repo at
`y-files/Map Files/Asia (South-Central)/01 initial generations/`.

**Status: initial generation, for consideration only. No nations are named, no borders are settled.**
Every assignment traces back to the Stage 1 surveys in `worldbuilding/extractions/`.

## Files
- `regions.csv` — the 39 working cultural regions (region_id, working name, structural tier).
- `spheres.csv` — 15 overlay spheres (cross-cutting identities, drawn as hatching over regions).
- `languages.csv` — language vocabulary (lang_id, family) for the language map.
- `units/units_<group>.csv` — the drawing units per research group (geoBoundaries gbOpen ADM2 2021 for India,
  Pakistan, Nepal, Bangladesh, Sri Lanka; ADM1 dzongkhags for Bhutan). Older than the surveys: districts
  created after 2021 (e.g., 6 new Nagaland districts) are folded into their parents.
- `classification/<group>.csv` — one row per unit: the cultural-region assignment and language/religion tags.

## Classification columns
`unit_id, unit, region_id, region_tier (core|domain), sphere_1, sphere_2, lang_primary, lang_secondary,
religion_primary, religion_secondary, breaks_first_order_rule (Y|N), confidence (1|2|3), evidence`

- **region_tier**: `core` = the region's identity is strongest here (typically the majority/plurality
  community and the historical heartland); `domain` = clear but lesser or mixed influence.
- **sphere_1/sphere_2**: overlay identities from `spheres.csv` (blank if none). A sphere is hatching over the
  region fill, meaning a significant (roughly 15%+ or politically decisive) minority identity or a claimed
  territory; overlapping spheres are intentional.
- **lang_primary / lang_secondary**: `lang_id` from `languages.csv` — plurality mother tongue of the unit,
  and the largest other language if it is 20%+ of the population.
- **religion_primary / religion_secondary**: choose from `Sunni`, `Shia`, `Hindu`, `Buddhist-Theravada`,
  `Buddhist-Vajrayana`, `Christian`, `Kirat-Animist`, `Sikh`, `Other`; secondary only if 20%+.
- **breaks_first_order_rule**: `Y` if the unit sits inside a first-order subdivision (province, state,
  division) whose culture is split across this unit and its neighbors so that assigning the whole parent to
  one region would be wrong, i.e., the region boundary runs *through* the parent. `N` otherwise.
- **confidence**: 3 = census/percentage evidence in the survey; 2 = solid qualitative evidence;
  1 = inferred or thin evidence.
- **evidence**: one short clause with the deciding number or survey section (no non-Latin script).

## Rules for all classification passes
1. Use the survey tables (`worldbuilding/extractions/`) as the source, not general knowledge; where a
   number is missing, say so and lower the confidence.
2. Every unit gets exactly one region_id.
3. American English; Latin script only, no Bengali/Devanagari/Arabic/Tibetan/etc. script anywhere.
4. Research proposes, the author disposes: these are proposed working assignments, not decisions.
