# Russia — cities added for the new Russian territory (2026-09-30, second step of round 09)

**Author instruction**: "go ahead and add the cities" (after the mainland eastern-Ukraine slice was added to the Russia nation, entry below). Done in this folder (`09 follow-up/`); pre-edit scripts, `cyrillic_names.py` and the
three affected maps were archived first (`archive 03/`, `archive 04/`).

## What changed

- **West close-up**: five cities added, each with its Latin name and a Russian-language Cyrillic line under it, in the same two-line style as every other plain city: **Kharkiv / Харьков**, **Dnipro / Днепр**,
  **Zaporizhzhia / Запорожье**, **Donetsk / Донецк**, **Luhansk / Луганск**. The cluster is tight (the Rostov-on-Don label and the Donska-Kubania nation label sit right beside it), so the labels are fanned out with
  offsets, the same technique used for the North Caucasus capitals: Kharkiv to the right, Dnipro and Zaporizhzhia to the left and stacked apart, Donetsk up and to the left, Luhansk up and to the right.
- **Full overview and reference map**: three cities, **Kharkiv, Dnipro and Donetsk** (same Latin + Cyrillic treatment, same offsets on both maps). Zaporizhzhia and Luhansk are left off these two smaller-scale maps because
  there is no room (same reasoning the project already uses for Krasnodar and the North Caucasus: the West close-up carries the full detail).
- **Woodard map**: no city layer by design; re-rendered only to confirm it is unchanged.
- `cyrillic_names.py` (shared): six entries added (the five above plus Mariupol).

## Choices to confirm with the author

- **Names**: the Latin line follows the English spellings used across these maps (Kharkiv, Dnipro, Zaporizhzhia, Donetsk, Luhansk); the Cyrillic line uses the **Russian-language** forms (the territory is in the Russia nation). If the author
  would rather have Russian-style Latin transliterations (Kharkov, Dnepr, and so on) or Ukrainian-form Cyrillic, change them in `cyrillic_names.py` and the city dictionaries in the scripts.
- **Mariupol** is **not drawn**: its marker would sit under the Rostov-on-Don label. Its Cyrillic name is in `cyrillic_names.py` if the label is ever moved. No Crimean cities (Simferopol, Sevastopol) were added either; the
  zone's capital is undecided.
- **Which cities**: the five largest of the new territory's regional centers (Kharkiv 1.46 M, Dnipro 1.05 M, Donetsk 0.99 M, Zaporizhzhia 0.79 M, Luhansk 0.45 M, Natural Earth `pop_max`); none is a capital (Moscow remains
  Russia's).

## Verification

- Frame sizes identical to the pre-cities versions (full 6000x2800, West 4400x5555, reference 5200x3279); pixel comparison against `archive 04/` shows differences only inside the city-label areas (full x 4 to 10%, y 56 to 63%;
  West x 3 to 26%, y 75 to 82%; reference x 6 to 13%, y 57 to 63%); Center and East byte-identical to 08.
- Visually confirmed on all three maps: no label overlaps another label, a marker, or the Rostov-on-Don and Donska-Kubania labels. Three iterations were needed on the West map and two on the full map.

---

# Russia — the mainland eastern-Ukraine slice added to the Russia nation (2026-09-30)

**Author instruction** (Europe eastern-Ukraine session, 2026-09-30): "it would be Russia that gets those areas" — confirming the nation for the territory east of the agreed line: **Luhansk, Donetsk, Kharkiv,
Dnipropetrovsk and Zaporizhzhia oblasts in full, plus Kherson Oblast east of the Dnieper only**. This is a new round of work, so it was done in the **next free numbered folder, `09 follow-up/`** (copied from
`08 follow-up - including Crimea/`, which is left untouched), following this project's rule that new work goes in a new numbered folder unless the author names one; the author named 08 only for the Crimea round.
Rename or move it if another name is wanted. Full decision record in the Europe project:
`y-files/Map Files/Europe/02 reorganization/01 follow-up/DECISION LOG - Eastern Ukraine and Crimea.md` (the territory, the line, and why).

## What changed

- **`subdivisions.csv`**: six rows added to the **Russia** nation, type Oblast, same color (#3B6EA5): Luhans'k, Donets'k, Kharkiv, Dnipropetrovs'k, Zaporizhzhya and Kherson (names exactly as Natural Earth spells them, so they
  join with no other change). 84 to 90 rows; Russia 18 to 24 subdivisions; still 13 nations. **Kherson is a district-level exception to the whole-first-order-unit rule**: only the part east of the Dnieper
  (about 75% of the oblast by area) is Russian; its geometry comes from the new **`kherson_left_bank.geojson`** (made in the Europe project from the Natural Earth Dnieper centerline and the Natural Earth Kherson
  unit; the right bank, including Kherson city, stays Ukrainian neutral background). The exact raion-level cut is still to be checked.
- **Four scripts** (`full`, `West`, `reference`, `Woodard`): the admin-1 filter now also takes those six Ukrainian-named units; Kherson's geometry is replaced by the left-bank file; **Ukraine's neutral polygon has the
  ceded territory (this slice and Crimea) cut out**, so the old Russia-Ukraine border is not drawn across Russian territory and a new border shows along the slice's western edge; `full` and `West` footnotes gained a line
  naming the territory.
- **Frame and label-size fractions unchanged on purpose**: `core_all` excludes the slice and the Crimea zone (the same fix as in 08), so the hand-tuned layout of rounds 05 to 08 does not move.
- **Not changed**: `render_map_russia_central.py` and `render_map_russia_east.py` and their maps (neither includes the Russia nation; byte-identical to 08), `spheres.csv`, `cyrillic_names.py`, every label position, the Crimea
  Autonomous Zone treatment from 08.

## Verification

- 90 polygons matched (84 + 6), 13 nations, on all four scripts.
- **Pixel comparison against the pre-edit maps** (`archive 02/`): frame sizes identical (full 6000x2800, West 4400x5555, reference and Woodard 5200x3279); the only differing regions are the new territory and the footnote
  (full and West). Central and East are byte-identical to 08.
- Visually confirmed: the new territory joins Russia proper along the Sea of Azov; the Kherson left bank touches the Crimea Autonomous Zone at the isthmus; the Ukrainian border is redrawn along the slice's western edge;
  no label moved. (A stray "B" near the Rostov label on the full map is the clipped start of the "Black Sea" label and is identical in the pre-edit version.)

## Archives

- `archive 01/` — the pre-edit `subdivisions.csv`, `spheres.csv`, `cyrillic_names.py`, the four edited scripts, and a copy of the Russia `PROGRESS TRACKER` before this round's edit.
- `archive 02/` — the pre-edit PNG and SVG of the four re-rendered maps.

## Open (none of it built)

- ~~No cities~~ **Cities were added later the same day** (see the entry above).
- The Kherson left-bank district-level cut; population data for the new subdivisions (blank, like every other subdivision); whether the slice stays ordinary Russian oblasts or gets a designation of its own.
- Europe-side: this decision is not yet applied to the Europe cultural maps (1 to 4) in the Europe project.
- Run note: to regenerate, set `NE_DIR` to a folder holding `ne_10m_admin_1_states_provinces.geojson`, `ne_10m_admin_0_countries.geojson` and `ne_10m_populated_places_simple.geojson`, and `OUT_DIR` to this folder; `kherson_left_bank.geojson` must sit next to the scripts.

---

# Russia — Crimea and Sevastopol added to Donska-Kubania as an Autonomous Zone (2026-09-30)

**Author instruction** (Europe eastern-Ukraine session, 2026-09-30): Crimea goes to Donska-Kubania **as an Autonomous Zone** — the author's reason: during the Ukrainian period Crimea
was an autonomous unit through almost the whole time, so the designation continues what it already was. "Apply it to the region data for the Russia maps and re-render the map for
Donska-Kubania", in this folder (`08 follow-up - including Crimea/`, named by the author). Sevastopol is assumed to go with Crimea (the author spoke of Crimea only). Full decision record
in the Europe project: `y-files/Map Files/Europe/02 reorganization/01 follow-up/DECISION LOG - Eastern Ukraine and Crimea.md`.

## What changed

- **`subdivisions.csv`**: two rows added to Donska-Kubania, **Crimea** and **Sevastopol**, type **Autonomous Zone**, same nation color (#C77B3E), population blank like the others. 82 to 84 rows;
  Donska-Kubania 7 to 9 subdivisions; still 13 nations. The notes column carries the reason and the open questions (name, capital, powers, Crimean Tatar representation, Sevastopol's status).
- **Four scripts** (`full`, `West`, `reference`, `Woodard`): removed the filter that excluded Crimea and Sevastopol from the admin-1 units (Natural Earth carries both as Russian admin-1 units; the
  names match the new rows exactly, so they join with no other change). Added a **dashed outline** around the zone on top of the nation border (line width 1.6 on West, 1.0 on full, 1.1 on
  reference and Woodard). `full` and `West` also got a **legend entry** ("Autonomous Zone (Crimea)") and a footnote line.
- **West close-up only**: a label **CRIMEA / Крым / Autonomous Zone** in the open Black Sea just south of the peninsula, with a short leader (the peninsula is too small to label at this scale and the
  map's left edge runs close to its west coast, so a label to its west was clipped and was moved). The shared "Black Sea" sea label moved from lon 36.0/lat 43.5 to lon 38.6/lat 43.4 to make room.
  The footnote's old sentence ("Crimea and Sevastopol are excluded — treated as Ukrainian/European territory") was replaced.
- **Frame and label-size fractions are unchanged on purpose**: all four scripts now compute `core_all` (the frame and each nation's area fraction) **without** the zone, so the hand-tuned layout
  of rounds 05 to 07 does not move. (A first attempt without this fix widened the full map's frame and shrank the whole map by about 2%; caught by a pixel comparison and corrected before
  delivery.)
- **Not changed**: `render_map_russia_central.py` and `render_map_russia_east.py` and their maps (neither reaches Crimea; still byte-identical to 07), `spheres.csv`, `cyrillic_names.py`.

## Verification

- **Natural Earth data**: the pinned download these scripts were written against was no longer on disk, so a fresh Natural Earth 1:10m download (admin-1, admin-0, populated places; converted to geojson, used via
  `NE_DIR`) was used. **Check**: the unmodified West script rendered with it was compared to `07`'s `russia_west_map.png`: **0 differing pixels out of 24.4 million**, so the data is equivalent.
- **Regression check** of the four new maps against the archived pre-edit versions (`archive 05/`), pixel by pixel: the frame sizes are identical (full 6000x2800, West 4400x5555, reference and Woodard 5200x3279)
  and the only differing regions are Crimea, the legend entry and the footnote (full and West), and the Crimea label area (West).
- Visually confirmed: Crimea in Donska-Kubania's color with the dashed outline on all four maps, the West label clear of the Black Sea label and of the North Caucasus cluster, no other label moved.

## Archives (nothing overwritten without a copy first)

- `archive 04/` — the pre-edit `subdivisions.csv`, `spheres.csv`, `cyrillic_names.py`, the four edited scripts, and a copy of the Russia `PROGRESS TRACKER` before its 2026-09-30 edit.
- `archive 05/` — the pre-edit PNG and SVG of the four re-rendered maps (full, West, reference, Woodard).

## Open (none of it built)

- **The mainland eastern-Ukraine slice** (Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia, and Kherson east of the Dnieper) is **not** drawn on these maps: its nation is an unconfirmed assumption (Russia),
  so it is still neutral background here. Decision log in the Europe folder.
- The Crimea Autonomous Zone's name, capital, powers and Crimean Tatar representation; Sevastopol's own status; a Cyrillic label for the zone beyond the plain "Крым".
- Run note: to regenerate, set `NE_DIR` to a folder holding `ne_10m_admin_1_states_provinces.geojson`, `ne_10m_admin_0_countries.geojson` and `ne_10m_populated_places_simple.geojson`, and `OUT_DIR` to this folder.

---

# Russia — cities added to the plain reference map (2026-09-27)

**Author instruction**: make `russia_reference_map.png` show cities the same way `russia_full_map.png` does
— this map previously had no capitals/cities at all by design (see its own docstring: "no side panel, no
legend, no capitals"). Done in this folder (`07 follow-up/`) per the author's explicit instruction. Pre-edit
copy of `render_map_russia_reference.py` reconstructed from conversation context and saved to `archive 03/`
(the edit was made before archiving this round — a process slip; the reconstruction is byte-accurate since
the file had just been read in full immediately prior).

## What changed

- Ported `render_map_russia_full.py`'s exact `CAPS`/`CAPS_LATIN_ONLY`/`CITIES`/`DOT_ONLY` city set and
  capital/city/Latin-only/dot-only tiering into `render_map_russia_reference.py` — same cities, same
  distinction between capitals (bold, square marker) and plain cities (circle marker), same two-line
  Latin+Cyrillic treatment. Font and marker sizes scaled to ~87% of full.py's values, matching the ratio
  already established between this map's own nation-label range (9-20) and full.py's (11-23) — this map's
  smaller canvas (26in vs 30in wide) would otherwise make the same absolute point size read relatively larger.

## Collisions the added cities exposed, and how each was fixed

Adding a full city layer on top of this map's already-compact, legend-free design surfaced the same class of
problem seen when Cyrillic was first added to the other maps — this map had simply never had cities before,
so these collisions are new here, not regressions:

- **Russia/Moscow, Künnarantaiga/Yakutsk, Tuva/Kyzyl**: this script never had a `LABEL_OVERRIDE` mechanism
  before (it never needed one, with no cities to collide with). Added it, using the same coordinates already
  settled on the other maps (Russia: lon 29.0/lat 55.5; Künnarantaiga: lon 130.0/lat 65.3; Tuva: lon 94.6/lat
  52.55).
- **Donska-Kubania/Elista**: same provably-impossible-to-reposition problem already solved on the full map by
  making Donska-Kubania's nation label single-line Latin-only. Applied the same fix here.
- **The six North Caucasus capitals vs. their own already-tight nation-name cluster**: this cluster was
  already at capacity before cities were added (the six small republics' names are single-line Latin-only
  specifically because of this). Even single-line capital text didn't fit on top. Moved Grozny, Magas,
  Makhachkala, Vladikavkaz, Nalchik, and Cherkessk (plus Krasnodar, already dot-only on the full map) to
  plain unlabeled dots here — fully labeled on the West close-up, Latin-only-labeled on the full overview.

## Maps rebuilt

`render_map_russia_reference.py` re-rendered in this folder. Visually confirmed: all four fix areas above,
plus a full-image pass — no remaining new collisions. (The pre-existing North Ossetia-Alania/Ingushetia/
Chechnya nation-label tightness in that same cluster predates this round and is unchanged — same accepted
utility-map tolerance as before.)

---

# Russia — Künnarantaiga's capital set: Vladivostok (2026-09-27)

**Author instruction**: the author realized Künnarantaiga's capital had never been decided. Researched real
administrative/military/judicial/diplomatic infrastructure across the three population-leading candidates
(Vladivostok, Irkutsk, Khabarovsk, tied/close at 587K/587K/579K) — see
"Capital City Candidates - Künnarantaiga (research).md" in this folder for the full comparison. Pre-edit
copies of the two affected scripts (full, East — the only two showing Vladivostok) archived in `archive 02/`
first.

## Headline finding

A genuine civilian-vs-military split, similar in shape to Idelsk-Uralia's own three-way capital tradeoff:
**Vladivostok** is the real, current (since Dec 2018) civilian seat of the Far Eastern Federal District —
whose territory is a near-exact match for Künnarantaiga's own — plus the region's clear diplomatic hub
(~22 foreign consulates) and home to the flagship Far Eastern Federal University. **Khabarovsk** instead
holds the Eastern Military District headquarters (which did not move in 2018) and the Far Eastern District's
commercial/arbitration court. **Irkutsk**, despite tying on population, isn't part of the real-world Far
Eastern Federal District at all. Author's call: Vladivostok, on the strength of its civilian/administrative/
diplomatic case outweighing Khabarovsk's narrower military/judicial one.

## What changed

- `render_map_russia_full.py` and `render_map_russia_east.py` (the only two scripts showing Vladivostok —
  West and Center are out of its geographic range): Vladivostok promoted from `CITIES` to `CAPS` in both,
  now rendered bold with the square capital marker instead of a plain city dot.
- No territory, border, or subdivision changes — this is a pure capital designation, same category as the
  Nizhny Novgorod/Rostov-on-Don/Novosibirsk decisions before it.

## Maps rebuilt

Both scripts re-rendered in this folder. Visually confirmed on both: Vladivostok's label reads correctly as
a bold capital with no collisions on the East close-up and the full overview.

---

# Russia — Cyrillic sub-labels added to all six maps (2026-09-27)

**Author instruction**: add Cyrillic text underneath the Latin text for every nation and city name, at ~80%
of the Latin text's font size, with city text made a bit bigger to accommodate the two-line format. Special
case: Künnarantaiga (the only name with a non-ASCII Latin character, ü) gets three effective lines — the
ASCII-safe "Kunnarantaiga" as the primary/top line, then "Künnarantaiga / Күннарантайга" (proper-diacritic
Latin and Cyrillic, equal precedence) as the secondary line. Done in this folder
(`06 follow-up - Latin and Cyrillic text/`) per the author's explicit instruction. Pre-edit copies of all six
scripts archived in `archive 01/` first.

## New shared file: `cyrillic_names.py`

All six scripts now `sys.path.insert` this folder and import from one shared data file, rather than
duplicating the name dictionaries six times: `NATION_CYRILLIC`, `CITY_CYRILLIC` (real, standard Russian
names for real places — high confidence, common geographic knowledge), `NATION_ASCII_LATIN` (only one entry:
Künnarantaiga → Kunnarantaiga), and `CYR_SERIF`. Idelsk-Uralia's and Donska-Kubania's Cyrillic names are
straightforward letter-by-letter transliterations of the invented English names, not deep historical-Russian
equivalents — flagged as an author's-call point in that file's own docstring; easy to change in one place if
the author prefers something closer to the real 1918 Idel-Ural/Don-Kuban movements' own naming instead.

## Font problem and fix: Crimson Text has no Cyrillic glyphs at all

Checked via `fontTools` cmap inspection before writing any label code: Crimson Text (this project's serif
display font, used for nation-name labels) has zero Cyrillic coverage. Lato (already used for city labels)
does have full Cyrillic coverage, so city Cyrillic sub-labels just use Lato at a smaller size — no font
change needed there. For nation labels, switched the Cyrillic line to **Gentium Book Plus**, a system font
(not bundled in this project's `fonts/` folder) from the SIL Gentium project, built for genuine multilingual
text — confirmed via an actual render test (not just cmap inspection) that it correctly shows Cyrillic, ü,
and the em dash together in one string, needed for Künnarantaiga's combined second line and for "Северная
Осетия — Алания." Visually it pairs well with Crimson Text (both elegant serif book faces), noticeably
better than falling back to the sans-serif Lato for nation names would have looked.

## The two-line label mechanism

Added a `T2()` helper (nation labels) and inline two-`annotate()` calls (city labels) in every script: the
Latin line is placed with `va='bottom'` and the Cyrillic/secondary line with `va='top'`, both anchored to the
same point with a small **points-based** (not data-unit) vertical offset — this keeps the visual gap between
lines consistent regardless of a map's projection scale, unlike the meter-based `dx`/`dy` fan-out offsets
already used elsewhere in these scripts for capital positioning (which the two-line blocks still layer on
top of, for the labels that already needed hand-tuned positions).

## Collisions the doubled label height exposed, map by map

Doubling every label's height (a Latin line plus a same-size-footprint Cyrillic line) broke a large number of
positions that were only just fitting before, across every map. Each was fixed either by widening/redesigning
the existing hand-tuned offset (using exact pixel bounding-box measurements — see method below — not
eyeballing), or, where the math showed no position could work, by keeping that one specific label single-line
Latin-only (with a comment explaining why, and noting where the bilingual version *does* exist):

- **Full map**: Russia/Moscow (relabeled, moved further per exact pixel math than the West map's equivalent
  fix needed, since this map's zoom leaves less room), St. Petersburg/Arkhangelsk (flipped St. Petersburg's
  text direction), the North Caucasus capital cluster (all six kept single-line Latin-only — mathematically
  provable that six two-line blocks cannot fit in that cluster at this map's zoom; the West close-up carries
  the bilingual version), Donska-Kubania's nation label (also kept single-line Latin-only for the same
  proven reason — checked numerically that no position within its own territory clears Rostov-on-Don,
  Krasnodar, Elista and the North Caucasus row simultaneously), and Krasnodar (demoted to a plain dot, no
  text — sandwiched between Rostov's capital block and Donska-Kubania's label with ~7px of real clearance,
  too little for any label at all; still fully labeled on the West close-up).
- **West map**: Russia/Moscow, Donska-Kubania/Elista, Krasnodar/Cherkessk, and Nalchik/Магас — all fixed by
  repositioning (this map has enough zoom/room that nothing needed the Latin-only fallback).
- **Center map**: Tuva's label nudged to fully clear the Kyzyl capital marker dot.
- **East map**: no new collisions — Künnarantaiga was already the only label on this map.
- **Reference and Woodard maps**: the six North Caucasus republics (already the tightest cluster on these
  two unstyled reference maps, which have no spacing system at all beyond a smaller font floor) kept
  single-line Latin-only, matching the full map's fix for the same underlying reason.

## Method: exact pixel math instead of eyeballing crops

For every non-trivial fix, captured each script's real `xlim`/`ylim`/`W`/`H`/`MAP_FRAC`/`CRS` (via a
temporary debug print, immediately reverted) and used them to convert between lon/lat and the renderer's
actual pixel space (100 dpi — matplotlib's interactive-draw dpi, not the 200 dpi `savefig` uses, confirmed by
checking `fig.dpi` directly; using the wrong one silently doubles all distances). Real label bounding boxes
were read directly from `ax.texts[...].get_window_extent()` rather than estimated. For the North Caucasus
full-map cluster and Donska-Kubania specifically, this included a small spiral/candidate search to prove
numerically whether any non-overlapping position existed at all, before concluding it didn't and falling
back to the single-line treatment.

## Maps rebuilt

All six scripts re-rendered in this folder. Visually confirmed on all six, including close crops of every
crowded pocket listed above.

---

# Russia — third West/Center size increase + author-directed label repositioning (2026-09-27)

**Author instruction**: West and Center text needed to be "a bit bigger" still, and separately, the author
supplied five annotated copies of the current maps (in `physical text placement reference/`, one subfolder
inside this one) with hand-drawn red ovals — and on two of them, arrows — marking exactly where specific
nation-name labels should move to. Pre-edit copies of all five touched scripts archived in `archive 03/`
first.

## How the annotated positions were read

Rather than eyeball the ovals, each oval's pixel centroid was found programmatically (flood-fill to find the
enclosed interior, robust to the arrows also drawn on two of the images) and converted back to lon/lat through
each script's own exact projection parameters (CRS, axis limits, figure size — captured via a temporary debug
print, immediately reverted). This gave precise coordinates rather than approximate ones:

- **West map**: "RUSSIA" → lon 33.5, lat 56.5 (west-southwest of Moscow, toward Pskov/Novgorod).
- **East, full, and Woodard maps**: "KÜNNARANTAIGA" → lon 130.0, lat 65.3 (north of Yakutsk, in open interior
  territory) — computed independently on all three annotated images and landed within about a degree of each
  other (128.9–131.3 lon, 64.8–65.6 lat), confirming it's a real consistent target and not measurement noise.
- **Reference map**: no annotation was drawn on it — left untouched.

## What changed

- **West and Center scripts**: third size increase. Nation-name font `max(15, min(29, ...))` →
  `max(17, min(33, 17 + area_frac * 630))`. City/capital font 16pt/18pt → 18pt/21pt. Marker size `6.2/9.5` →
  `7.2/11`. Text clearance `28e3` → `32e3` meters. Halo stroke `4.2` → `4.6`.
- **West script**: "RUSSIA" label repositioned per the annotated coordinate above (its own centroid still sat
  on Moscow after the size increase — same recurring class of problem as the other centroid-vs-capital
  collisions in this project).
- **East and full scripts**: "KÜNNARANTAIGA" `LABEL_OVERRIDE` updated to the new author-specified coordinate
  (previously an assistant-chosen position southeast of Yakutsk; author wants it north of Yakutsk instead).
- **Woodard script**: had no `LABEL_OVERRIDE` mechanism at all (Künnarantaiga's centroid happened not to
  collide with anything on this smaller-scale reference map) — added the mechanism and the same
  Künnarantaiga coordinate, for consistency with the other three maps per the author's own annotation on this
  map specifically.

## Maps rebuilt

All five scripts (full, East, West, Center, Woodard) re-rendered in this folder. Visually confirmed: West's
Russia/Moscow area and North Caucasus cluster (still clean after the third size increase), East and full's
Künnarantaiga position (now north of Yakutsk, matching the annotation), Woodard's Künnarantaiga position, and
Center's full extent. No remaining collisions found.

---

# Russia — West and Center maps: second text-size increase (2026-09-27)

**Author instruction**: after the round below, the West and Center maps were still "basically unreadable" —
full and East were fine, so this round touched only those two scripts. Pre-edit copies archived in
`archive 02/` first.

## Why West/Center needed more than full/East did

Same point-size fonts as the round below, but West and Center cover a much larger, more elongated real-world
extent per map-inch (West runs from the Arctic coast down to the Caucasus; Center's figure is a tall portrait
extent too) than the full overview or East close-up. Same font size reads smaller when the underlying
geography-to-page ratio is more zoomed out.

## What changed (West and Center scripts only)

- Nation-name label font: `max(11, min(23, ...))` → `max(15, min(29, 15 + area_frac * 550))`.
- City/capital label font: 12pt/14pt → 16pt/18pt. Marker size `4.6/7.5` → `6.2/9.5`. Default text clearance
  `22e3` → `28e3` meters. Halo stroke `3.6` → `4.2`.

## New collisions the second increase exposed, and how each was fixed (West map only — Center's only cluster,
Tuva/Kyzyl, still had enough clearance from the round below)

- **Russia vs. Moscow**: Russia's centroid sits on Moscow, exactly the same class of problem as
  Künnarantaiga/Yakutsk and Tuva/Kyzyl in the round below. Added a `LABEL_OVERRIDE` (West didn't have this
  mechanism yet) moving "RUSSIA" north into open territory clear of both Moscow and Nizhny Novgorod.
- **Vladikavkaz vs. Makhachkala**: both labels' default text direction pointed toward each other (both
  extending west/left) and met in the middle once the font grew. Flipped Makhachkala's offset to extend
  east instead, into open space toward the Caspian coast.
- **Nalchik vs. Cherkessk**: fixing each one's clearance from its *own* dot in isolation pushed them toward
  *each other's* dot instead — the classic problem with a tightly packed six-point cluster, where moving one
  label to clear one collision creates a new one with its neighbor. Redesigned both offsets together instead
  of independently: Cherkessk now pushes northwest into open Donska-Kubania territory (away from the rest of
  the cluster), Nalchik pushes west and slightly south (away from Cherkessk above it).

## Maps rebuilt

Both scripts re-rendered in this folder. Visually confirmed on both: West's full extent plus a close crop of
the North Caucasus cluster and the Moscow area; Center's full extent plus a close crop of Tuva/Kyzyl. No
remaining collisions found.

---

# Russia — map adjustments: bigger text, label collision fixes (2026-09-27)

**Author instruction**: make the nation and city text bigger on the full overview, West, Center and East
maps (previous size was "basically unreadable"), with particular care to keep Künnarantaiga's name label
clear of the Yakutsk city label on the East and full maps. Done in this folder
(`05 follow-up - map adjustments/`) per the author's explicit instruction — **not** `04 follow-up/`, which
stays untouched as the prior authoritative state. Pre-edit copies of the four touched scripts archived in
`archive 01/` before any changes, per this project's own archive-before-overwrite rule.

## What changed (all four scripts: full, East, West, Center)

- **Nation-name label font**: `fs = max(7, min(15, 7 + area_frac * 400))` → `max(11, min(23, 11 + area_frac *
  500))` — roughly 1.5x bigger across the size range.
- **City/capital label font**: 8pt/9.5pt (city/capital) → 12pt/14pt. Marker dot size and halo stroke width
  bumped to match (`ms=3.4/6` → `4.6/7.5`; halo linewidth `3` → `3.6`). Default text-to-dot clearance (`dx`)
  increased `16e3` → `22e3` meters to keep the bigger text off the dot.
- **Reference and Woodard-sphere maps left untouched** — the author only asked about the full overview, West,
  Center and East maps.

## Label collisions the bigger text introduced, and how each was fixed

- **Künnarantaiga vs. Yakutsk (East and full maps)**: Künnarantaiga's own centroid sits right on top of
  Yakutsk. Added a manual `LABEL_OVERRIDE` dict (previously the nation-label loop was purely centroid-based)
  and relocated Künnarantaiga's label southeast to open territory between Yakutsk and the Sea of Okhotsk
  coast, clear of Magadan/Khabarovsk/Irkutsk too. **Deliberately generous open space left around the new
  position** — the author flagged that a Cyrillic sub-label (~75-80% of the Latin text's size) will likely be
  added below these name labels in a future pass, so tight placements were avoided even where the English-only
  label alone would have fit.
- **Tuva vs. Kyzyl (Center and full maps)**: same issue, smaller scale — Tuva's centroid sits on its own
  capital. Same `LABEL_OVERRIDE` mechanism, nudged the "TUVA" label north, clear of the capital dot and the
  "Kyzyl" text below it.
- **The six North Caucasus republics (West map only)**: at this map's closer zoom, all six small nations'
  auto-centroid name labels (Chechnya, Ingushetia, Dagestan, North Ossetia-Alania, Kabardino-Balkaria,
  Karachay-Cherkessia) collided with each other and with their own capital labels — no font size avoids this
  in geography this dense. Skipped their on-map name labels entirely (`SKIP_NAME_LABEL`), relying on the
  color-coded legend instead — the same tiny-nation philosophy the full map's `TINY_SKIP` threshold already
  uses, just applied explicitly here since West's smaller extent doesn't trigger that threshold naturally.
  Also widened the hand-tuned capital-label `dx`/`dy` fan-out offsets (e.g. Cherkessk `15e3`→`22e3`,
  Grozny `75e3`→`110e3`) to give the bigger capital text room to clear each other.
- **Cherkessk vs. Elista (full map only)**: bigger text turned a previously-fine tight fit into a head-on
  collision (both labels' default text direction pointed at each other). Flipped Elista's side from `'r'` to
  `'l'` (text now extends east, away from Cherkessk) and Cherkessk's from `'l'` to `'r'` (text now extends
  west, away from Elista).

## Maps rebuilt

All four scripts re-rendered in this folder. Visually confirmed on all four: full overview, West close-up
(North Caucasus cluster specifically), Center close-up (Tuva/Kyzyl specifically), and East close-up
(Künnarantaiga/Yakutsk specifically) — no remaining label/marker collisions found in this pass.

---

# Russia — naming update: Country A → Künnarantaiga (2026-09-27)

**Author instruction**: name "Country A" (Sakha/Yakutia + the old Russian Far East + Irkutsk Oblast). Done in
this folder (`04 follow-up/`) specifically per the author's own instruction — **not** `02 follow-up/`, which
stays untouched as the round-2 authoritative state up through the prior capital/naming decisions. This folder
now holds the current authoritative map set going forward; see the PROGRESS TRACKER for the folder-status note.
Full research trail: `Country A - Indigenous Language Nature Vocabulary (research).md` (same folder).

## What changed

- **`subdivisions.csv`, `spheres.csv`, and all six render scripts brought up to date from `02 follow-up/`
  first** (this folder's copies had gone stale, predating the Idelsk-Uralia/Donska-Kubania/Siberia capital
  decisions), **then** "Country A" renamed to "Künnarantaiga" ("Land of the Sunlit Taiga") throughout. Author's
  own invented compound: Yakut күн ("sun/day") + Buryat наран ("sun") + taiga, honoring the territory's two
  genuinely major indigenous languages. Literal construction is "sun-sun-taiga," not "sunlit taiga" — a
  deliberate creative gloss, not a literal translation; see the research doc for the full linguistic
  background.
- **No territory, border, subdivision, or capital changes** — this is a pure naming update. Künnarantaiga
  still has no declared capital.
- **`NAME_TBD` cleared** in every script that listed `'Country A'` there (`render_map_russia_full.py`,
  `render_map_russia_east.py`, `render_map_russia_reference.py`, `render_map_russia_woodard.py`) — the
  "— name TBD" legend marker no longer applies.

## Maps rebuilt

All six scripts re-rendered in this folder (`/tmp/mapvenv` pipeline, pinned Natural Earth data) to replace
every "Country A" label/legend entry with "Künnarantaiga." Visually confirmed on the full overview and East
close-up: label and legend both read "Künnarantaiga" legibly, no overlap/collision from the longer name, no
stray "— name TBD" marker.

---

# Russia — round 2: Karelia split (2026-09-27)

**Author instruction**: split Karelia and Murmansk out of Idelsk-Uralia into their own new "semi-stable
proto-country." Full context and reasoning: `../01 follow-up/Russia - Karelia, Murmansk and Finland (pending
future decision).md` — read that first, this file only covers what changed in this round's build.

## What this is (and isn't)

This is **Stage 1 of a longer-term plan only**: the split itself. The eventual merge into Finland, and the
"encouraged" ethnic-Russian population transfer that would follow it, are **not built here** — Finland
doesn't exist as a drawn nation anywhere in this project (Europe hasn't been started). Nothing on any of
these maps references Finland. The new nation is treated exactly the way Kaliningrad's split from Russia's
own nation list was handled in round 1: pulled out now, its eventual destination left as a documented pending
note, nothing drawn for that destination.

## What changed

- **New nation: "Karelia"** (name not yet decided — same placeholder treatment as Countries A/C/D).
  Color `#4A7A9E`. Two subdivisions: Karelia (Republic) and Murmansk (Region), both pulled out of Idelsk-Uralia.
  Renders as one contiguous region — Karelia and Murmansk share a real border, so the split produces a clean
  single polygon, not two disconnected pieces.
- **Idelsk-Uralia loses two subdivisions**, now 25 instead of 27. Still by far the largest nation on the map.
  Verified its remaining territory still unions cleanly — no gaps or stray fragments where Karelia/Murmansk
  used to sit.
- **13 nations total now** (up from round 1's 12): `subdivisions.csv` — 82 rows.
- Added Petrozavodsk and Murmansk city markers to the West close-up (plain city dots, not capitals — the new
  proto-country doesn't have a declared capital any more than Countries A/C/D do).

## Maps rebuilt

Only the maps that actually show Idelsk-Uralia's territory needed changes, confirmed by checking each script's
own `NATIONS_HERE` list before touching anything:
- `render_map_russia_full.py` — rebuilt (Karelia added to `NATIONS_HERE` and `NAME_TBD`).
- `render_map_russia_west.py` — rebuilt (same, plus the two city markers, plus header/footer text updated to
  round-2).
- `render_map_russia_reference.py`, `render_map_russia_woodard.py` — rebuilt (same `NATIONS_HERE`/`NAME_TBD`
  change; these two show every nation regardless of size, no legend, so no further changes needed).
- `render_map_russia_central.py` (Siberia + Tuva only) and `render_map_russia_east.py` (Country A only) —
  **unchanged**, verified pixel-identical to round 1's versions after a fresh render, since neither shows any
  Idelsk-Uralia territory. Carried over unmodified for a complete, self-contained package.

All six scripts tested locally (`/tmp/mapvenv` pipeline, pinned Natural Earth data) before delivery — verified
clean geometry (no fragmented unions), correct legend/footer text, and no new label collisions.

`spheres.csv` is unchanged from round 1 — Karelia and Murmansk were never part of the Mongolic World sphere,
so this split doesn't touch it.

## Earlier rounds

- Round 1 (`../01 follow-up/`): the 20→12 nation reorganization (Countries A/C/D, North Caucasus
  independence, Kaliningrad's removal).
- The original 20-nation package (`y-files/Map Files/Russia/01 initial generations/`) is the untouched
  source-of-truth original — this and round 1 are both iterations on top of it, not replacements for it.
