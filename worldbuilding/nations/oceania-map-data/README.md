# Oceania — Map Data Package

**Stage 3, first pass, 2026-09-26.** Follows the Stage 1 frameworks survey
(`../../extractions/Oceania - Coastal Cohesion and the Import Lifeline (survey).md`) — that survey settled
Australia's and New Zealand's cohesion questions; this package turns those findings, plus the real-world
borders of every other Pacific nation, into an actual map-data package, matching the pipeline every other
region in this project has gone through. No Stage 2 material survey exists yet (only Australia got that level
of depth, inside the Stage 1 survey itself) — flagged, not a blocker for this stage.

## What's settled, and what's still open

**Settled, by the frameworks survey:**
- **Australia stays unified.** No partition case found — the coastal settlement pattern (87-95% of the
  population within 50-100km of the coast) argues strongly against a breakaway piece surviving on its own,
  even though real historical secessionism exists (Western Australia's 1933 referendum). See the survey's §1.
- **New Zealand stays independent and unified.** Declined the 1901 Australian Federation on purpose (a
  century-old, deliberate choice, not an accident); "South Island nationalism" is a real 160-year-old
  sentiment but has never had serious secession traction. See the survey's §2.

**Not a partition question at all, just inherited real-world fact**: the other 14 sovereign Pacific nations
(Fiji, Kiribati, Marshall Islands, Micronesia, Nauru, Palau, Papua New Guinea, Samoa, Solomon Islands, Tonga,
Tuvalu, Vanuatu) are each already their own separate, real, sovereign country — unlike Indonesia on the
Maritime Southeast Asia map, none of these needed a fracture-or-unify decision. They're drawn here at their
real-world borders.

**⚠️ Genuinely open, flagged in every affected row of `subdivisions.csv`**: nine pre-war territories whose
colonial metropole isn't an established successor-state anywhere in this project yet —
- **French-administered**: New Caledonia, French Polynesia, Wallis and Futuna
- **US-administered**: Guam, Northern Mariana Islands, American Samoa
- **UK-administered**: Pitcairn Islands
- **NZ-associated (self-governing, not fully sovereign pre-war)**: Cook Islands, Niue

Every one of these is drawn as its own provisional nation, defaulted to independence post-2083 (its distant
metropole can't administer it across a global collapse — the same reasoning this project has applied to other
remote colonial holdings elsewhere), but **none of this is asserted as settled**. **Guam is the single
highest-priority flag** — real-world strategic significance (Andersen AFB, Naval Base Guam, the "tip of the
spear" of US Pacific power) makes this a bigger creative decision than the others, worth its own dedicated
pass before treating as final.

**Folded into Australia, not drawn separately**: Norfolk Island (has a real population, ~2,169 pre-war, but
no separatist case found — lower-confidence fold than the next two, worth a second look), and the
uninhabited/near-uninhabited Ashmore and Cartier Islands and Coral Sea Islands (both already Australian
external territory, no population, no reason to treat separately).

## Files

**⚠️ Delivered as two companion maps, split 2026-09-26 (author-requested)** — matching the Southeast Asia
region's own Mainland/Maritime split. `render_map_oceania.py` (the original single map) is kept as a
reference/reproducibility copy; it isn't part of the two-map delivery and doesn't need to be re-run.

**Continental map framing fixed 2026-09-26 (author-requested, round 2)**: the crop window now excludes
New Zealand's remote sub-antarctic/equatorial dependencies (Chatham Islands, Kermadec Islands, Tokelau,
Auckland/Campbell/Antipodes Islands, the Snares, Three Kings Islands) from the bounds calculation that
sizes the frame — those outliers were forcing the window thousands of km east of New Zealand's main
islands, which left Australia stranded in the left third of the frame. Nothing was removed from the
map itself; every subdivision still draws wherever it falls. See `render_map_oceania_continental.py`'s
`NZ_REMOTE` list and its surrounding comment for the detail.

**Both maps switched to flat, plain colors 2026-09-26 (author-requested, round 3)**: the crosshatch/dot
sphere-fill pattern (Melanesia/Micronesia/Polynesia) is removed from both scripts — it was the only
textured, non-flat element on either map. Each sphere keeps its colored dashed/dotted boundary outline
(a thin line, not a fill texture); the legend's separate hatch-swatch row per sphere was folded into
its line-swatch row. National fill colors are unchanged (already flat solid tints via `lighten()`).

| File | Rows | Content |
|---|---|---|
| `subdivisions.csv` | 167 | Every first-order subdivision (Natural Earth's own admin-1 level) across 26 real countries/territories, resolved to 23 nations. Shared by both maps below — each script filters to its own nation subset. |
| `spheres.csv` | 3 | Melanesia / Micronesia / Polynesia — the standard, real, uncontested Pacific ethnographic three-region model. Unlike most of this project's spheres, this one isn't a reasoned construction; it's textbook anthropology. Also shared by both maps — each draws only the slice of each sphere that falls on it. |
| `render_map_oceania_continental.py` | — | **Map 1 of 2**: Australia, New Zealand, Papua New Guinea. Outputs `oceania_continental_map.png`. |
| `render_map_oceania_islands.py` | — | **Map 2 of 2**: the other 20 nations/territories (11 sovereign + 9 provisional). Outputs `oceania_islands_map.png`. Still crosses the antimeridian; the continental map does not. |
| `render_map_oceania.py` | — | The original single-map renderer, superseded by the two scripts above for delivery purposes. Kept for reference. |
| `fonts/` | — | Crimson Text and Lato, this project's house typefaces (copied from the Southeast Asia package). |

**Cross-map spheres**: Papua New Guinea's slice of Melanesia and New Zealand's slice of Polynesia are drawn
on the continental map; the rest of each sphere is drawn on the islands map, with each map labeling the
other's portion as continuing onto the companion map — the same convention the Southeast Asia maps
established for the Patani Malay World sphere. Micronesia is unaffected (fully on the islands map, no
Micronesian nation is on the continental map).

## Antimeridian handling — read before editing the script

This is the first region in this project whose real extent crosses 180°E/W. Fiji, Tonga, Kiribati, New
Zealand's outer islands, and most of the Polynesian chains sit on or near the dateline, and Natural Earth's
raw longitude values split across it (e.g. Fiji's own bounding box comes back as -180 to +180, which is
nonsense — it should be a compact ~7° span). The script shifts every geometry's longitude (+360 to any value
< 0) into a continuous range *before* reprojecting, verified against a standalone test render that confirmed
Fiji renders as one contiguous shape rather than two disconnected fragments on opposite edges of the frame.
**Do not remove the `antimeridian_fix()` step** — every downstream calculation (bounds, sphere unions, label
placement via `P()`) depends on geometries already being in the shifted, continuous frame.

## Design notes

- **Whole first-order subdivisions only** — the same absolute rule as every other map in this project.
- **Side-panel legend layout** (map occupies the left ~76% of the figure, a dedicated panel on the right holds
  title/legend/footer) — adopted from the Southeast Asia maps specifically because a flat, in-map legend
  covering 23 nations is too large to float over the map without colliding with content; an earlier draft of
  this script did exactly that, covering Papua New Guinea, before this layout replaced it.
- **Provisional nations get the same visual tier as settled ones** (their own hard border, their own color) —
  the legend's "Provisional — author review needed" heading is the only visual distinction. This was a
  judgment call: giving them a different hatch/border treatment would have implied a settled "autonomous
  zone"-style design decision this package hasn't actually made yet, so a plain color-plus-flag was the more
  honest choice until the author resolves each one.
- **Population is blank for every row.** Natural Earth's admin-1 layer doesn't carry population for this
  region the way it partially did for Southeast Asia's, and researching per-subdivision population for 167
  rows across 23 nations was out of scope for this pass — flagged as a real, known gap, not an oversight.

## How to run

Same `NE_DIR`/`OUT_DIR` environment-variable convention as every other region's official package:

```
export NE_DIR=./ne OUT_DIR=./out
python3 render_map_oceania.py
```

No `setup_natural_earth.py` exists in this package yet — reuse the pinned Natural Earth download from the
Southeast Asia official package (`y-files/Map Files/Asia (Southeast)/03 official timeline years/`) if a fresh,
checksum-verified download is needed; the same pinned commit was used to build and verify this package's own
data (see the sourcing note in `subdivisions.csv`'s own generation — every subdivision name was checked
against that exact Natural Earth vintage before being written into the CSV).

## What's next

- Author review of the nine provisional-nation flags, Guam first.
- A dedicated Pacific Islands material-base pass (the frameworks survey's own flagged gap) — PNG, Fiji,
  Solomons, Vanuatu, Samoa, Tonga, and the Micronesian/Polynesian small-island states likely each need
  individual treatment given how differently "import-dependency fragility" plays out at very different
  population/economy scales.
- NZ-Australia integration depth (CER, Trans-Tasman Travel Arrangement, ANZUS) — the frameworks survey's own
  flagged gap, relevant to whether these two nations deserve a sphere/closer-tie treatment beyond just being
  two separate hard-bordered neighbors.
- Per-subdivision population research, if a future pass wants it.
- This package has been rendered and visually reviewed once, locally, by this session (label collisions
  around Guam/Hagåtña, French Polynesia/Papeete, Palau/Ngerulmud, New Zealand/Wellington, and Solomon
  Islands/Honiara were all found and fixed this way) — but it has **not** yet been through the Claude.ai
  web-UI round-trip review every other region's map went through. Treat this as a solid first pass, not a
  fully polished final render.
