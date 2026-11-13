# Dedicated Hawaii map added (2026-09-26, eighth round)

**Author request**: two sets of instructions: one that makes the North America map *including* the Republic of
Hawaii, and another that makes **a separate, dedicated map of the Republic of Hawaii itself**. The seventh round
(below) delivered only the first.

## What changed
- **New:** `north-america-nations/hawaii_nation.py`, which renders `output/hawaii-nation.png`: the eight main
  islands with names, channels, cities, summits, graticule and scale bar; an inset of the whole archipelago out to
  Kure Atoll; and a side panel with legend, measured island areas and a locator against North America.
- **New:** `reference/hawaii-nation.png`.
- **Updated:** `verify.py` checks all three maps; README has a new "Eighth round" section, an updated quick start
  and files table, an open question about Midway Atoll, and a note on text anti-aliasing differences between
  environments.
- **Unchanged:** `na_nations.py`, `setup.sh`, `requirements.txt`, and the North America references and CSV.

Run: `bash setup.sh && python3 na_nations.py && python3 hawaii_nation.py && python3 verify.py`

---

# North America — Hawaii inset added (2026-09-26)

**Author request**: "Add a little 'corner-box'-type thing in the Pacific Ocean to include the Republic of
Hawaii." Built from `.../03 follow-up/archive 01/north-america-nations/`, the most up-to-date version at the
time of the request — the map previously omitted Hawaii entirely.

## What changed

`north-america-nations/na_nations.py` only. No changes to the twelve continental nations, the DMZ, the Arctic
exceptions, the Alaska Panhandle cut, or the DMZ-detail close-up map — verified pixel-identical to the new
reference except for the new inset itself.

Hawaii gets its own small "corner-box" inset (a separate mini-map with its own Hawaii-centered projection),
placed in the one stretch of open Pacific water on the main map large enough to hold it cleanly — southwest of
San Francisco — the same convention real-world US maps use for Hawaii. The full Hawaii subdivision (Natural
Earth admin-1), including the uninhabited Northwestern Hawaiian Islands chain, is drawn; the inset's own view
is cropped to just the main eight islands (Ni'ihau through Hawai'i Island), the same convention this project
used to frame the Oceania continental map past New Zealand's own remote outlying islands. Honolulu is marked.
Color `#1E8A8A` (teal), not used by any other nation on this map. A legend entry and a `nations-assignment.csv`
row were added by hand (Hawaii isn't part of the main `geo`/`COL` rendering pipeline, so it can't go through
the loops the other twelve nations use).

**Hawaii stays part of North America, not Oceania** — author-confirmed earlier this session, political lineage
over geography, the same precedent as Greenland and Quebec.

See `north-america-nations/README.md`'s new "Seventh round" section for the full detail, and its updated
nations table. `reference/` inside that folder has been regenerated and `verify.py` confirmed both maps
pixel-identical and the CSV identical against a fresh local run before delivery.
