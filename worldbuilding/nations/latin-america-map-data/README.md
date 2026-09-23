# Latin America Map Data — for Image Generation

2026-09-23. Machine-readable datasheets derived from
`../../extractions/Latin America - Regional Frameworks and Colonial Origins (survey).md`, formatted so they
can be handed to an image-generating model to draw approximate regional maps.

**These are FOR CONSIDERATION ONLY.** No nations have been named, no borders settled. This is a first-pass
division offered to be argued with, and every row names its own merge candidate so rejecting one is an
informed choice.

## The Files

| File | Rows | What it is |
|---|---|---|
| `regions-main.csv` | 13 | The main continental division, Mexico-south-of-Sonora through Tierra del Fuego |
| `regions-brazil.csv` | 5 | Darcy Ribeiro's five Brasis — Brazil's internal cultural regions, which cut across state lines |
| `regions-optional.csv` | 6 | Candidates deliberately excluded from the 13, listed so they can be drawn if wanted |

Brazil is **not** in `regions-main.csv`. It is its own file because its internal division rests on a separate
scholarly source and is more confident than anything in the main list.

## Column Reference

| Column | Meaning |
|---|---|
| `region_id` | Stable number. 1–13 main, 14–18 Brazil, O1–O6 optional. |
| `region_name` | Display label. |
| `ribeiro_tier` | The coarse four-way grouping, for a simplified version of the map. See below. |
| `modern_countries` | Present-day countries the region touches. **The primary key for placing it.** |
| `core_territory` | Where identity is strongest. **Draw this as solid fill.** |
| `domain_territory` | Clear but lesser influence. **Draw as lighter fill or hatching.** |
| `sphere_territory` | Wide, mild, overlapping with neighbors. **Draw as a dotted outline or faded edge — overlaps between spheres are correct, not errors.** |
| `anchor_cities` | Specific places to hang the shape on. Most useful single column for accuracy. |
| `lat_north`, `lat_south`, `lon_west`, `lon_east` | Approximate bounding box, decimal degrees. Negative = south / west. **Rough guides, not boundaries.** |
| `color_hex`, `color_name` | Suggested palette, chosen to be distinguishable and roughly grouped by tier. |
| `founding_population` | One-line summary, for a legend or caption. |
| `characteristic_institution` | The institution that defined it. |
| `confidence` | `high` / `medium` / `low` — how solid the case for this being its own region is. |
| `merge_candidate` | Which region it would fold into if the map is simplified. |
| `notes` | Anything a map-maker should know. |

## The Coarse Grouping

If thirteen regions is too many, `ribeiro_tier` collapses them into four, following Darcy Ribeiro (1970) and
Charles Wagley (1957), who arrived at nearly the same scheme independently:

- **Indo-America** (Povos Testemunho) — surviving Indigenous civilizations under a colonial layer: regions 1, 2, 7, 8, parts of 3
- **Plantation America** (Povos Novos) — populations created by colonial mixing and the plantation: regions 4, 5, 6, 10, Brazil's Crioulo
- **Euro-America** (Povos Transplantados) — European settlement that displaced rather than absorbed: regions 11, 12, Brazil's Sulino
- **Terrain-defined** — never effectively colonized; defined by what defeated settlement: regions 9, 13

That fourth tier is the survey's own addition, not Ribeiro's, and is the weakest-supported part of the scheme.

## Suggested Prompts

**For the full map:**
> Draw a map of Central and South America showing 13 cultural regions. Use `core_territory` as solid fill in
> `color_hex`, `domain_territory` as the same color at reduced opacity, and `sphere_territory` as a dotted
> outline. Spheres are expected to overlap between regions — do not resolve the overlaps. Label each region
> with `region_name`. Include a legend. Leave northern Mexico (Sonora, Chihuahua, Coahuila, Nuevo León,
> Tamaulipas) and both Baja California peninsulas **unshaded and labeled as belonging to other nations.**

**For the simplified map:** same, but color by `ribeiro_tier` instead — four colors, not thirteen.

**For Brazil:** draw `regions-brazil.csv` over Brazil alone, and if possible show the IBGE administrative
regions as thin gray lines underneath, since **the mismatch between the two is the point.**

## Two Hard Constraints for Any Map

These are settled canon in the wider setting and must not be redrawn:

1. **Northern Mexico is taken.** Sonora, Chihuahua, Coahuila, Nuevo León and Tamaulipas belong to an existing
   nation (the Republic of Sonora) and are **out of scope** — leave them unshaded.
2. **Both Bajas are taken.** Baja California and Baja California Sur belong to Cascadia. Leave them unshaded.
   This makes the Gulf of California an international frontier rather than an internal sea.

## Caveats

- Bounding boxes are **approximate**, derived from the described core/domain/sphere geography. They are guides
  for placement, not borders to trace.
- ⚠️ Region 10 (Llanos and Orinoco) is the weakest of the thirteen and the first to cut.
- ⚠️ Region 8 (Altiplano) should be the **last** merge made, not the first — the colonial mita boundary
  running through it is the only *measured* institutional discontinuity in the hemisphere.
- ⚠️ Region 5 (Plantation Caribbean) deliberately treats all the islands as one, which flattens the sharpest
  internal distinction in the survey. Haiti in particular is arguably its own object.
