# North America — The Post-War Nations

A self-contained package that renders the North America political map for the post-war setting, a close-up
of the DMZ, and a dedicated national map of the Sovereign Republic of Hawaii. Everything a fresh session needs is here. No earlier conversation, and no other folder, is required.

The map began as the author's hand-drawn tentative map. It was rebuilt on real boundary data (Natural Earth,
1:10m) so borders follow actual state and province lines, then restyled to match the other regional maps in the
series (Latin America, East Asia).

---

## Quick start

```bash
bash setup.sh            # one time: Python packages, map data and fonts (pinned versions)
python3 na_nations.py    # about 20 seconds; writes the North America map, the DMZ close-up and nations-assignment.csv
python3 hawaii_nation.py # a few seconds; writes the dedicated Hawaii map, hawaii-nation.png
python3 verify.py        # should report all three maps PIXEL-IDENTICAL and the CSV IDENTICAL
```

- Use `bash setup.sh` rather than `./setup.sh`, because unzipping can drop the execute permission.
- If the render is started before setup, it stops with a message saying which data file is missing.
- Downloads come from `raw.githubusercontent.com` (Natural Earth, Google Fonts) and PyPI.
- Override any location with the environment variables `NE_DIR`, `FONT_DIR` and `OUT_DIR`. By default they are
  `natural_earth/`, `fonts/` and `output/` next to the script.

## Files

| File | What it is |
|---|---|
| `na_nations.py` | The North America renderer (main map, Hawaii inset, DMZ close-up, CSV). All decisions below are encoded in it |
| `hawaii_nation.py` | The dedicated Hawaii map renderer. Same data, fonts, color and house style (see "Eighth round") |
| `setup.sh` | Installs the packages and downloads the data and fonts, pinned to exact commits |
| `requirements.txt` | Python packages (`geopandas`, `shapely`, `pyogrio`, `pandas`, `numpy`, `matplotlib`, `pillow`) |
| `verify.py` | Compares a fresh run against `reference/`: both maps pixel by pixel, and the CSV exactly |
| `reference/north-america-nations.png` | What a correct run produces, the main map |
| `reference/north-america-dmz-detail.png` | What a correct run produces, the DMZ close-up |
| `reference/hawaii-nation.png` | What a correct run produces, the dedicated Hawaii map |
| `reference/nations-assignment.csv` | What a correct run produces: every state and province and the nation holding it (72 rows) |
| `reference/earlier-straight-cut-version.png` | An older image with a straight DMZ cut line north of Manitoulin. **Superseded**; kept for history |

Pinned sources (set in `setup.sh`):
- **Natural Earth**: `nvkelso/natural-earth-vector`, commit `ca96624`, the 2022-06-02 master. Four layers: admin-0
  countries, admin-1 states and provinces, lakes, populated places.
- **Fonts**: `google/fonts`, commit `23e54b5`, from 2026-09-24. Crimson Text (Regular, SemiBold, Bold, Italic)
  and Lato (Regular, Bold, Italic).

---

## The nations (canon)

Twelve polities plus Hawaii, a Demilitarized Zone, and a Neutral Scientific Territory. Each nation is made of
whole US states, Canadian provinces or territories, and Mexican states, with three documented exceptions —
Hawaii is a fourth, of a different kind: it's whole, but drawn in a separate inset rather than its true position
(see below).

| Nation (legend name) | Territory | Color |
|---|---|---|
| **Alaska** | Alaska (minus the Panhandle), Yukon, Northwest Territories, Nunavut (minus the Arctic exceptions below) | `#5A8BD0` |
| **The People's Democratic Republic of Cascadia** | Washington, Oregon, California, British Columbia, **the Alaska Panhandle**, Baja California, Baja California Sur | `#7CC9AA` |
| **Colorado** | Idaho, Montana, Wyoming, Nevada, Utah, Colorado | `#2B4F86` |
| **La República de Sonora** | Arizona, New Mexico, Sonora, Chihuahua | `#B59A45` |
| **The Prairie Federation** | Alberta, Saskatchewan, Manitoba, and Ontario north of the DMZ | `#E6D46A` |
| **The Midwest Republic** (colloquially "Midwestland") | North Dakota, South Dakota, Nebraska, Kansas, Minnesota, Iowa, Missouri | `#52AE84` |
| **Appalachia** | Wisconsin, Michigan, Illinois, Indiana, Ohio, Kentucky, West Virginia, Virginia, Maryland, Delaware, D.C. | `#2F6A3E` |
| **New England** | New York, Pennsylvania, New Jersey, Connecticut, Rhode Island, Massachusetts, Vermont, New Hampshire, Maine | `#8660B4` |
| **The CSA** | Texas, Oklahoma, Arkansas, Louisiana, Mississippi, Alabama, Georgia, Florida, South Carolina, North Carolina, Tennessee | `#DD7F3E` |
| **Quebec** | Québec, Newfoundland and Labrador, New Brunswick, Nova Scotia, Prince Edward Island | `#6BC3D8` |
| **Greenland** | Greenland, plus the Queen Elizabeth Islands | `#C166AE` |
| **The Sovereign Republic of Hawaii** | Hawaii (the whole state, incl. the uninhabited Northwestern Hawaiian Islands chain) — drawn in a corner-box inset, lower left, not its true position; also has its own dedicated map (`hawaii_nation.py`) | `#1E8A8A` |
| *Demilitarized Zone* | Southern Ontario (see below). Not a nation: drawn in hatched red | `#C9413B` |

**Not assigned to any North American nation:**
- **Baffin Island** and its satellites are a **Neutral Scientific Territory**, drawn white. They are held open
  without prejudice or hostility for scientific and environmental research, shared among the four nations whose
  territory borders or surrounds them: Alaska, Greenland, the Prairie Federation and Quebec. This is not a nation.
  (Author-specified 2026-09-25. Before that, Baffin was simply "unclaimed".)
- The rest of Mexico is *Latin America*, labeled "see companion map" in the legend. It's covered by the
  companion Latin America map. This
  includes **Coahuila, Nuevo León and Tamaulipas**, which are not part of Sonora.

**Hawaii stays part of North America, not Oceania** (author-confirmed 2026-09-26) — political lineage over
geography, the same precedent as Greenland and Quebec. It has its own National Character Profile
(`worldbuilding/nations/Sovereign Republic of Hawaii - National Character Profile.md`), which ties it to two
load-bearing pieces of existing canon: U.R.U.K./En.Ki.Du (the robot birthplace) and Doris Morikawa's Hall of
Archives.

### Decisions made along the way (so no one undoes them)
- **Washington and Oregon are entirely Cascadia.** The hand-drawn original split them along the Cascades. That
  split was removed to obey the whole-subdivision rule.
- **Sonora is exactly four states: Arizona, New Mexico, Sonora and Chihuahua.** An interim version wrongly
  gave it five Mexican states.
- **The DMZ is a region, not a strip.** The original drew a long thin strip along the Quebec border. It is now
  the southern "belly" of Ontario, and north of it the Prairie Federation and Quebec share a direct border.

### The three exceptions to "whole subdivisions only"
1. **The Arctic archipelago.** Nunavut and the Northwest Territories are split island by island:
   - islands centered north of 74.7°N (the Queen Elizabeth Islands) → Greenland;
   - islands centered east of 82°W and north of 61.5°N (Baffin and its satellites) → Neutral Scientific Territory;
   - the rest → Alaska.
2. **The DMZ.** Ontario is cut along the historic canoe route. The waypoints were checked by the author against
   Google Maps on 2026-09-25:
   - the Mattawa River's mouth on the Ottawa (46.320N, 78.707W), which is on the real Ontario/Quebec border;
   - west along the Mattawa corridor, just north of North Bay;
   - across Lake Nipissing;
   - down the French River to its mouth on Georgian Bay (45.941N, 80.902W);
   - then, per an author correction on 2026-09-25, south through open water, clearing the small islands at the
     French River delta, and southwest past Manitoulin's southern shore and western end into Lake Huron.

   Everything in Ontario south of that line is DMZ. That includes the Ottawa Valley, the Windsor tip and the whole
   Bruce Peninsula, down to Cove Island off Tobermory.

   **Manitoulin Island and Fitzwilliam Island are Prairie Federation.** The line passes south of both.
3. **The Alaska Panhandle → British Columbia, and so → Cascadia** (author-specified 2026-09-25). The real treaty
   line zigzags through several boundary peaks. It is simplified to a cut anchored on two of them:
   - **Mount Jetté** (59.994N, 139.053W), the BC/Yukon/Alaska tripoint;
   - **Mount Cook** (60.178N, 139.982W).

   Everything in Alaska south and east of the cut goes to Cascadia: all of Southeast Alaska from Yakutat to
   Ketchikan, about 85,000 km².

   **How the cut actually runs on the ground,** which differs from the code comment's description (see "Open
   question" below):
   - From Mount Cook it runs about 35 km east-southeast on the Malaspina bearing (115.3°), then northeast until it
     leaves Alaska near Mount Hubbard. Alaska keeps the high peaks north of that line.
   - On the west, the edge is **a straight line due south from Mount Cook (139.98°W) to the sea.** It crosses the
     eastern edge of the Malaspina Glacier foreland, west of Yakutat Bay.
   - The code comment's "Jetté ray" (due west from Mount Jetté) falls entirely inside the cut area, so it doesn't
     shape the border. The two rays don't actually meet at Disenchantment Bay.

---

## Design conventions (keep these consistent with the other regional maps)

- **Projection.** Lambert azimuthal equal-area, centered at 47°N 96°W.
- **Fills and borders.** Flat fill, one color per nation. Hard borders are a white casing under a thin dark line.
  **No present-day internal state or province lines are drawn**, because the old countries don't exist.
- **Lakes.** Lakes are drawn above the borders, so no border lines cross the Great Lakes.
- **Coastline.** The coastline is drawn from the *union* of all countries, so old international borders never
  show.
- **Type.** Crimson Text (serif) is used for titles and nation labels, and Lato (sans) for cities and small
  notes. Labels carry a white halo.
- **Layout.** The legend sits in a right-hand side panel. The DMZ gets its own legend class below the nations.

---

## Fixes made while packaging (2026-09-25)

The script supplied for packaging needed three changes. They are recorded here so no one reintroduces them.

1. **The DMZ polygon was closed wrong.** The "south of the cut" shape ended with a straight diagonal from
   (74°W, 40°N) back to the Mattawa mouth.
   - That **sliced off the entire Ottawa Valley**, handing Ottawa and the upper St. Lawrence to the Prairie
     Federation and cutting the DMZ off from Quebec.
   - Its western edge, at 82.5°W, also **missed the Windsor tip**.
   - It now runs west past 84°W and east past 73°W, then back along 46.32°N to the Mattawa mouth. Only
     Ontario is intersected with it, so its reach into neighboring countries has no effect.
2. **Session-specific paths were replaced with portable ones.** Data, fonts and output all live next to the
   script, overridable by environment variables. The script also reads the raw Natural Earth admin-1 shapefile
   directly; an old session had used a converted `adm1.gpkg` copy.
3. **City labels are clipped** at the close-up map's frame. A stray fragment of "Minneapolis" had been showing
   at its left edge.

## Settled: Manitoulin Island (2026-09-25)

The author decided that **Manitoulin stays with the Prairie Federation.** The cut line now dips south of the French
River delta before heading west, so the whole north shore of Georgian Bay and all of Manitoulin stay north of it.

## Fixes made in the second round (2026-09-25)

1. **Greenland was missing from `nations-assignment.csv`.** Greenland is built from its admin-0 outline, not from
   a subdivision list, so the CSV loop skipped it. Its only row was the Queen Elizabeth Islands. A row for the
   island itself has been added.
2. **The reference images didn't match the script.**
   - The references delivered with the Manitoulin correction showed **Fitzwilliam Island** (about 50 km², just
     off Manitoulin's eastern tip) as DMZ.
   - The script's final cut line passes south of Fitzwilliam, so a fresh run makes it Prairie Federation. That
     matches the correction's intent: Fitzwilliam belongs with Manitoulin.
   - The references were evidently rendered from an intermediate version of the line. They have been
     regenerated from the script.
3. **`verify.py` now checks all three outputs.** The earlier version only checked the main map.

---

## Third round (2026-09-25): Baffin becomes a Neutral Scientific Territory

- **Changes.** The map label, the legend entry and the CSV row now name Baffin as the Neutral Scientific
  Territory, and the CSV note records which four nations share it. The legend's Latin America entry now reads
  "(see companion map)".
- **Checks.** Both longer legend entries fit the side panel, and the three-line Baffin label fits on the island.
  The references were regenerated.
- **Open for the author.** The label *on the map* over Mexico still reads "LATIN AMERICA / unpartitioned · see
  companion map". The legend dropped "unpartitioned", and the two are now slightly out of step. Nothing was
  changed there, pending a decision on whether "unpartitioned" should go from the map label too.

## Fourth round (2026-09-25): the Alaska Panhandle joins Cascadia

- **Change.** The Panhandle is cut from Alaska and added to Cascadia (exception 3 above). The CSV splits Alaska
  into two rows, and now has 71 rows in all.
- **Fix.** The map's footer still listed only two exceptions ("except the DMZ and the Arctic archipelago"). It now
  names the Alaska Panhandle too, and still fits the side panel.
- **Checked.** A close-up of the Jetté–Cook area, and the main map. At map scale the result reads cleanly, with
  Cascadia running up the whole coast to the Alaska line. The references were regenerated.

### Open question for the author: where the Panhandle line meets the sea
The code comment describes two rays, from Mount Jetté and Mount Cook, converging on Disenchantment Bay. The
geometry that actually runs is different: its western edge is a straight line due south from Mount Cook. So the
strip between that line and Yakutat Bay goes to Cascadia. That strip is the eastern edge of the Malaspina Glacier
foreland, around Point Manby.
- If that is intended, nothing needs to change.
- If the border should instead come down **Yakutat Bay itself**, with Disenchantment Bay and then the bay's
  length to the sea as the natural line, the strip stays with Alaska and Yakutat town stays with Cascadia. That
  means routing the western edge of the cut shape down the bay instead of down the 139.98°W meridian.

## Fifth round (2026-09-25): two label positions

- **Sonora's label** moved north (30.4° → 32.0°N). It now sits in the middle of the country, straddling the old
  US–Mexico line, instead of down by Hermosillo.
- **Appalachia's label** moved east (86.6° → 85.0°W), which centers it better.
- **References regenerated.** The images delivered with this change were still the previous render: pixel-identical
  to the fourth round's, so they didn't show the moved labels. Nothing else changed: no geometry and no CSV.

## Sixth round (2026-09-25): Sonora's label, fine-tuned

- **Sonora's label** moved from (108.6°W, 32.0°N) to **(109.3°W, 32.6°N)**, slightly up and left. Before, its last
  letter crowded the corner where the CSA begins; it now sits clear of that border, centered between Phoenix and
  Hermosillo.
- **References regenerated.** As in the fifth round, the images delivered with the change were still the previous
  render, so they didn't show the moved label. Nothing else changed: no geometry, no CSV, and no other label.

## Seventh round (2026-09-26): Hawaii inset added

- **Author request:** "Add a little 'corner-box'-type thing in the Pacific Ocean to include the Republic of
  Hawaii" — the map previously omitted Hawaii entirely (see the sixth round's README, which said so outright).
- **Why an inset, not true position.** This map's projection is centered on the continental landmass (47°N,
  96°W). Hawaii sits roughly 4,000 km southwest of that center; drawing it in true position would either force
  the frame absurdly wide (shrinking every other nation) or place it far outside the current crop. A separate
  small "corner-box" inset — its own mini-map, its own Hawaii-centered projection, placed in open ocean — is the
  same convention real-world US maps use for Hawaii.
- **Placement.** The inset sits in the one stretch of open Pacific water on the main map large enough to hold it
  cleanly: southwest of San Francisco, figure-fraction roughly (0.02, 0.10) to (0.185, 0.35). Checked against a
  clean crop of that area before placing it — no label, graticule line, or landmass fell inside it.
- **Geometry.** Hawaii's full admin-1 polygon (Natural Earth) is used, including the Northwestern Hawaiian
  Islands chain — nothing is dropped from the data. The inset's own view is cropped to the main eight islands
  (Ni'ihau through Hawai'i Island); the uninhabited NW chain, which runs another ~1,500 km further northwest,
  would force the inset box absurdly wide for no visual gain if included in the crop. Same convention used to
  frame the Oceania region's own continental map past New Zealand's remote outlying islands.
- **Contents.** Honolulu is marked (the only city in the inset, at inset scale). The box has a plain dark border
  (its own axes spines, not a drawn rectangle), an "HAWAII" title, and a small note — "inset — not to scale or
  position relative to the main map" — so it can't be mistaken for a true-position placement.
- **Color.** `#1E8A8A`, a teal not used by any other nation on this map.
- **Legend and CSV.** Hawaii is not part of the main `geo`/`COL` rendering pipeline (it never appears in the
  main map's own coordinate space), so its legend swatch and its `nations-assignment.csv` row are both added by
  hand rather than through the loops that handle the twelve continental nations — see the comments in
  `na_nations.py` at the "Hawaii inset" and CSV sections. The DMZ-detail close-up map is unaffected: it never
  references Hawaii.
- **References regenerated.** `nations-assignment.csv` grew from 71 to 72 rows.

## Eighth round (2026-09-26): a dedicated map of the Republic of Hawaii

- **Author request.** Two outputs, not one: the North America map *including* Hawaii (done in the seventh round,
  as the corner-box inset), **and a separate, dedicated map of the Republic itself.** The seventh round delivered
  only the first. This round adds the second. `na_nations.py` and its outputs are untouched.
- **New script, `hawaii_nation.py`.** Kept separate from `na_nations.py` so each map has its own set of
  instructions. It needs nothing new: the same Natural Earth layers and fonts that `setup.sh` already fetches, and
  `pyproj`, which comes with `geopandas`. Output: `output/hawaii-nation.png`, the same 20 × 13.5 in, 160 dpi frame
  as the North America map, with the same right-hand side panel, so the two read as one series.
- **Main map.** The eight main islands, Ni'ihau to Hawai'i Island, in a Lambert azimuthal equal-area projection
  centered at 20.5°N 157.5°W (the same one the inset uses). Flat `#1E8A8A` fill with the house border style
  (white casing, thin dark line). It shows:
  - island names, and the principal channels (Kaulakahi, Ka'ie'ie Waho, Kaiwi, Kealaikahiki, 'Alenuihāhā);
    the three narrow channels around Lāna'i are left unlabeled because their names collide with the islands;
  - every Natural Earth 10m populated place on the islands (Honolulu, Wahiawā, Līhu'e, Wailuku, Kailua-Kona,
    Hilo), in Hawaiian spelling;
  - four summits at their real positions: Mauna Kea (4,207 m), Mauna Loa (4,169 m), Haleakalā (3,055 m), Kīlauea;
  - a 1° graticule with edge labels, and a km/mi scale bar.
- **"The Whole Archipelago" inset (lower left).** The Republic is the whole former state, which runs about 2,400 km
  to Kure Atoll, so the full chain is shown in its own inset. The Northwestern Hawaiian Islands are too small to
  see at that scale, so each is ringed and named. A dashed box marks the main map's area.
- **Side panel.** Title, a two-entry legend, a table of island areas, and a locator showing the Republic against
  the North American mainland with the Honolulu–San Francisco great-circle distance (3,857 km · 2,397 mi).
  Island areas are *measured*, not typed in: they come from the same 1:10m polygons, in the equal-area
  projection. Total 16,848 km², slightly above the official ~16,635 km² because 1:10m outlines are generalized;
  the panel says so.
- **No new lore.** The map shows only geography and the canon already in this README. Nothing from the National
  Character Profile (capital, government, symbols) was added, because it isn't in this package. If the author wants
  any of that on the map, it's a small addition to the side panel.
- **Typography.** Crimson Text has no ʻokina (U+02BB); Lato does. Serif labels (islands, channels) use ‘ (U+2018),
  the standard typographic fallback, and sans labels (cities, peaks, the island table) use the true ʻokina.

### Open question for the author: Midway Atoll
Midway sits in the middle of the chain (between Kure and Pearl and Hermes) but was never part of the state of
Hawaii; in Natural Earth it's under "United States Minor Outlying Islands". Canon says the Republic is "the whole
state", so Midway is drawn **outside the Republic**, in neutral gray, and labeled that way. If the Republic should
hold Midway too, it's a one-line change in `hawaii_nation.py` (and the North America inset, which crops it out
anyway, wouldn't change).

### Verification note: text anti-aliasing differs between environments
Rendering this package in a different environment (the claude.ai sandbox, matplotlib 3.10.8) reproduced every
border, fill and the CSV exactly, but the two North America images differed from their references in **text
anti-aliasing only**, about 2% of pixels, all in glyph edges. That's a font-rasterizer version difference, not a
content difference. `reference/hawaii-nation.png` was made in that sandbox, so a run elsewhere may show the same
kind of text-only difference for it. If `verify.py` reports DIFFERS, check whether the box covers only labels
before treating it as a real change. Pinning `matplotlib` in `requirements.txt` would remove this; it wasn't done
here because the North America references' matplotlib version isn't recorded.

## Verification record (2026-09-25, all six rounds)

In an empty folder containing only this package's files, the following was run, with nothing reused from
earlier sessions:

```
bash setup.sh && python3 na_nations.py && python3 verify.py
```

- The setup downloaded everything.
- The render took about 20 seconds and produced both maps and the CSV.
- Both maps were **pixel-identical** to their references, and the CSV was **identical**. The second round was
  checked the same way.
