# East Asia Map Series — Current State

Rewritten 2026-09-24 after a verified cold-start render. **Read this first.** The `UPDATE INSTRUCTIONS - *.md`
files and `RENDER REPORT - 2026-09-24.md` are the provenance record (what was tried, what changed during
implementation, and why). This file is the one accurate snapshot of where everything stands.

**Status: verified reproducible.** Starting from nothing but this package, `bash setup.sh` followed by
`python3 ea_series.py` produced all six maps with no warnings, pixel-identical to the shipped `maps/`.
The six-map sequence (A–F) was rendered and verified in the eighth pass; the setup check is in the seventh.

---

## 0. Setup and running (start here on a new machine)

```
bash setup.sh                           # once: Python packages + Natural Earth data + fonts into ./assets/
python3 ea_series.py                    # all six maps -> maps/              (about 45 seconds)
python3 ea_series.py C F                # only those maps
python3 ea_series.py --sidebar-english  # alternate set  -> maps-sidebar-english/
```

- **What a good run looks like:** six `rendered <id> <file>` lines and **no `WARNING` lines**, then
  `ls maps | wc -l` reads 6. A `WARNING` means a font or `uharfbuzz` is missing. The maps still render but
  silently drop that script's native text, which is easy to mistake for success.
- **What `setup.sh` fetches** (all from GitHub raw URLs, listed in the script):
  - Natural Earth 10m (`nvkelso/natural-earth-vector`): admin-0 countries, admin-1 states/provinces,
    populated places (simple), and lakes. Each comes as `.shp .shx .dbf .prj .cpg`.
  - Crimson Text and Lato, Regular/Bold/Italic (`google/fonts`).
  - Noto Serif SC, TC, KR and JP (`notofonts/noto-cjk`, `Serif/SubsetOTF/`), plus Noto Serif (Cyrillic), Noto
    Serif Tibetan and Noto Naskh Arabic (`notofonts/notofonts.github.io`).
- **Where things live:** `assets/ne/` and `assets/fonts/` inside the package by default. Set `NE_DIR` and
  `FONT_DIR` to use copies elsewhere. `assets/` is not shipped in the zip (about 100 MB), because `setup.sh`
  recreates it.
- `data/province_assignments.csv` is regenerated on every run. It should come out byte-identical unless
  territory data changed.
- **Reference renders ship in the zip:** `maps/` (the default) and `maps-sidebar-english/`. Pixel-compare a
  new render against them to prove nothing drifted.

---

## 1. What's fully settled

### Sidebar: native-language text is ON by default
**Author decision, 2026-09-24:** the sidebar legend carries each polity's native-script name under its
English name, matching the map body. This **reverses** the earlier record that the author "chose
map-body-only." That record was wrong about what the author wanted, and it was the real reason the
"failed test run" looked broken (see §4).

| Folder | Sidebar | Command |
|---|---|---|
| `maps/` | English + native line (**the default**) | `python3 ea_series.py` |
| `maps-sidebar-english/` | English only (alternate, kept for comparison) | `python3 ea_series.py --sidebar-english` (or `SIDEBAR_NATIVE=0`) |

- Map-body native labels are on in both sets.
- `--sidebar-native` is still accepted but does nothing now, because it's the default.
- Row spacing is 0.046 in blocks carrying native lines (0.034 in the English-only set).
- Jeju-do's row (Map F only) always carries `제주도` as a third line under its two-line caption, in both sets.
- Checked on Map A (the most crowded legend, 20 rows) and Map F (with the Jeju row): everything fits, with
  clear space above the footer.
- `SIN` shows `震旦联邦` in the sidebar on E and F (where it's sovereign in the corrected six-map sequence —
  see §2 item 1). `KOR` shows `한국` on C, D, E and F (Korea unifies at C now, one map earlier than before).

### Naming
- `NCP` → **Zhongyuan**, `NW` → **Qin**, `NKO` → **North Korea**, `SKO` → **South Korea**. All four are now
  `name_status = ESTABLISHED` in `polities.csv` and `naming_worksheet.csv`. That column is bookkeeping only;
  the renderer doesn't read it.
- The rule that the Koreas must not use present-day names was explicitly overridden by the author. Mongolia and
  Japan keep present-day names with no conflict, so there's no structural reason the Koreas can't.
- Qin keeps its name after absorbing Qinghai (Map D onward, in the corrected six-map sequence — see §2 item
  1). Territorial growth doesn't require a rename, matching how historical Chinese states expanded.

### Visual label positions
`data/label_overrides.csv` holds per-map positions for the two polities whose shape changes mid-series, one
row per `(polity_id, map_id)`. Everything else is a single position in `polities.csv`. **Letters below use the
corrected six-map scheme (A–F); see §2 item 1 if this doesn't match an older reference.**

| Polity | Position |
|---|---|
| `NW`/Qin | `(108.7, 36.4)` on A, B and C, before Qinghai merges in (the base position in `polities.csv`); `(98.0, 37.0)` from D onward (override) |
| `MON`/Mongolia | `(106.9, 45.35)` on B through F, once Inner Mongolia merges in (overrides) |
| `KOR`/Korea | `(128.0, 36.6)`, in the open interior between Seoul and Busan, where both label lines fit |
| `ETK`/East Turkestan | latitude `39.7°`, which clears the `TARIM` sub-label |
| `JIN`/Jin | `(112.3, 37.8)` |
| `MAN`, `GAN`, `MIN` | `(127.2, 47.9)`, `(115.7, 27.6)`, `(118.2, 26.3)`: moved to make room for native lines |

The dashed Tian Shan line through East Turkestan is intentional. It's an internal divider between
Dzungaria and the Tarim Basin, not a border.

### Native-language text (map body and sidebar)
Source: `data/native_labels.csv`, one row per polity, used wherever `include_on_map = yes`.

- **Simplified Chinese** (Noto Serif SC): the nine Han states, Qinghai, Manchuria, Hakka, Inner Mongolia and
  the Sinian Federation (`震旦联邦`, Zhèndàn Liánbāng). "Sinian" traces through Sanskrit Cīna to 震旦. `支那`
  was checked and rejected as a real-world ethnic slur.
- **Traditional Chinese** (Noto Serif TC) for Taiwan: 臺灣, not 台湾.
- **Korean** (Noto Serif KR): `북한`, `남한`, `제주도`, and `한국` for unified Korea. `한국` comes from dropping
  the directional prefix the two pre-unification names share.
- **Japanese** (Noto Serif JP) for Japan, **Cyrillic** (Noto Serif) for Mongolia, **Tibetan** for Tibet and
  **Uyghur Arabic script** (Noto Naskh Arabic) for East Turkestan.
- **Map-body sizing:** 0.72× the English label, with a 7.5 pt floor and a 1.2 pt gap, anchored to the English
  label's rendered text box.
- **Sidebar sizing:** 8.5 pt, muted grey.
- **Uyghur and Tibetan are shaped with HarfBuzz** (`uharfbuzz`) and drawn as outlines.
  `arabic_reshaper`/`python-bidi` was tested and broke ە (U+06D5) and Tibetan vowel placement. Without
  `uharfbuzz`, those two fall back to English-only rather than rendering wrong.

---

## 2. Still open

1. **Merger order and map sequence — RESOLVED 2026-09-24, superseding the eight-map branch structure
   entirely.** Full order: **Mongolia unites → Korea unites → Qinghai joins Qin → the Sinian Federation
   forms.** Reasoning:
   - **Mongolia first** (within under five years of Map A) — an already-mobilized, century-old pan-Mongol
     reunification movement, freed from the great-power veto that blocked it twice pre-collapse. Slower than
     the ~11-month German-reunification precedent because the landmasses involved are larger than modern
     Germany.
   - **Korea second** — the same "artificial imposition, no deep basis" category as Mongolia (no
     founding-population/institutional/linguistic/ecological basis for the split), so also fast once free of
     external enforcement, but lands after Mongolia because Mongolia's movement was already organized and
     ready the instant central authority collapsed.
   - **Qinghai/Qin third and last** — incentive-driven, not mobilized by any national movement; only happens
     once it demonstrates itself as more beneficial than not, plausibly the slowest of the three.
   - **The Federation last of all**, roughly one (probably) to two (definitely) generations after Qinghai's
     merger — real-world federation-building precedent (US Continental Congress→Constitution: 15 years;
     German Zollverein→Empire: 37 years) both fit this window.

   **This required an actual new map render, not just relabeling.** The old eight-map branch structure
   (`A, B1, B2, B3, C, D, E, F`) only ever varied Mongolia vs. Qinghai's order, and always resolved both
   *together* before Korea's branch began — there was never a map showing "Mongolia united + Korea united +
   Qinghai still separate." **The corrected sequence is a plain six-map line:**

   `A (fragmented) → B (Mongolia unites) → C (Korea unites — NEW RENDER) → D (Qinghai joins Qin) → E (Federation founds) → F (post-court)`

   `B`, `D`, `E`, `F` reuse existing territory (old `B2`, old `C`, old `E`, old `F` respectively, relettered
   and `D` recaptioned around Qinghai instead of Korea). `C` is genuinely new — see
   `UPDATE INSTRUCTIONS - Corrected Merger Order and New Map C.md` for exactly what changed in every data file
   and what still needs rendering/verification. Old `B1`, old `B3` (a state that never actually occurs in this
   order), and the old Federation-before-Korea `D` are retired. `open_questions.csv` Q1 has the full writeup;
   Q2 is superseded by it. The years are now settled and on the maps; see item 4.

   **✔ Rendered and verified (eighth pass).** The new Map C is correct. The five reused maps have map bodies
   pixel-identical to their old counterparts, and the six-map set is complete.
2. **Broader naming tweaks** (Q3): the author said some `WORKING`/`ESTABLISHED` names may change, but the
   scope isn't specified. Ask which ones before changing anything.
3. **Wu/Korea color collision** (Q4): both are `#8E6FB8` and both are sovereign on Map C. They don't touch,
   but the legend shows identical swatches. Earlier guidance was to shift Wu's hex, not Korea's.
4. **Dates: SETTLED and rendered (ninth pass).** The timeline is 2083 (the war), then A 2094–2097,
   B 2098–2110, C 2111–2130, D 2131–2178, E 2179–2266 and F 2267–present. **F begins with the Court's founding
   in 2267**, when Jeju-do becomes neutral ground. The landmark 2318 ruling falls *within* F; it doesn't start
   it (corrected in the tenth pass). The reasoning is in `10 follow-up - timeline years/TIMELINE - East Asia Map
   Series.md`, which sits outside this package. The old "no dates" convention is retired (Q5 superseded).

   **The header design:**
   - **Sidebar, top.** The series title "ASIA (EAST)" is on the left. In the top-right corner are `Map {m}` and,
     under it, `year_range` from `maps.csv`.
   - **Top-center of the map, over a semi-opaque panel** (`#F5F2EA` at 82%, no text halo):
     - the epoch name (the `era` half of `map_title`), in large bold type;
     - under it, `epoch_summary`, wrapped at 100 characters.
     - The panel is **sized from the measured text** and centered on the map area, so any future epoch name or
       summary fits without retuning numbers.
   - `map_subtitle` is no longer drawn; it stays in `maps.csv` as reference only.
   - The footer no longer says "No dates are implied." Map F's original caption wording is preserved in
     `caption_original`.

   **✔ Resolved (tenth pass).** Map E's caption says the Court *"has not yet been founded."* The ninth pass
   flagged that this contradicted E's old range, which ran into the Court's era. With E now ending in 2266, the
   caption is accurate for the whole period.
5. **Low priority:**
   - Q7: the Outer Manchuria seam includes all of Khabarovsk Krai.
   - Q10: domain/sphere shading has never been rendered.
   - Q11: Shandong/Qilu is parked as a possible fourth northern Han state.

---

## 3. File map

- `setup.sh`: one-time environment setup, described in §0.
- `ea_series.py`: the renderer. It reads only `data/` plus the assets.
- `requirements.txt`: Python packages, including `uharfbuzz`.
- `maps/` and `maps-sidebar-english/`: reference renders of both sets, six maps each (A–F).
- `data/polities.csv`: source of truth for territory, color, English names and label positions.
- `data/label_overrides.csv`: per-map label positions.
- `data/native_labels.csv`: native-script text, script code and inclusion flag.
- `data/maps.csv`, `naming_worksheet.csv`, `series_graph.csv` and `open_questions.csv`: supporting data.
  `province_assignments.csv` is generated.
- `HANDOFF.md`: the original handoff. Where it differs from this file, this file wins.
- `UPDATE INSTRUCTIONS - *.md` and `RENDER REPORT - 2026-09-24.md`: provenance only. `UPDATE INSTRUCTIONS -
  Fix Failed Test Run.md` is closed (see §4).

---

## 4. What happened with the "failed test run"

A 2026-09-24 solo test produced only 4 of 8 maps and appeared to show `SIN` missing its sidebar native text.
**Neither problem reproduces.** Clean runs produce the full set every time (then eight maps, now six). In the sidebar-native set, `SIN`'s
native line renders on D, E and F.

The underlying mismatch was the default: the code (and the docs) made the English-only sidebar the default,
while the author wanted native text there. That is now fixed at the source. The 4-of-8 result is most likely
a timeout partway through the roughly 60-second run.

Also fixed in this pass: two malformed CSV rows that parsed with the wrong field count.
- `naming_worksheet.csv`, NCP's `name_notes` field.
- `open_questions.csv`, Q3's `state` field.

The renderer reads neither file, so no map changed, but any tool that rewrites those CSVs would have mangled
them.
