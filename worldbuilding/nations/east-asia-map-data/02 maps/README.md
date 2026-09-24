# East Asia — The Six Finalized Maps

2026-09-23. **This folder supersedes everything in the parent directory.** Every border question is settled;
nothing here is provisional and nothing is hatched to mark an open question.

Hand over **this file plus `polities.csv` and `maps.csv`**. Together they specify all six maps completely.

---

## The Series

Six maps tracking East Asia from the fragmentation that followed the war of 2083 through to full unification.

```
A ─→ B ─┬─→ C ─┐
        │      ├─→ E ─→ F
        └─→ D ─┘
```

**A → B is sequential. C and D both branch from B, and converge at E.** They are two orders in which the same
two unions could have happened — Korea first, or China first. **The order is not established**, so both
intermediate states are drawn rather than one being chosen.

| Map | Title | What changed | Sovereign states |
|---|---|---|---|
| **A** | Fragmented | The starting position | **19** |
| **B** | Semi-Unified | Qinghai → the Northwest; Inner Mongolia → Mongolia | **17** |
| **C** | Semi-Unified | The two Koreas unify | **16** |
| **D** | Semi-Unified | The Han states unify into the Sinian Federation | **9** |
| **E** | Unified | C and D converge — both unions complete | **8** |
| **F** | Unified | Jeju-do becomes neutral ground | **9** — 8 nations + a condominium |

---

## The Files

| File | What it is |
|---|---|
| `polities.csv` | Every polity that ever exists, with its **status on each of the six maps** |
| `maps.csv` | The six maps — filenames, titles, captions, what changed |

### How to build a map from `polities.csv`

Each polity carries `status_map_a` … `status_map_f`, with four possible values:

| Value | Meaning |
|---|---|
| `SOVEREIGN` | Draw it as a country with a full external border |
| `MERGED:<id>` | Its provinces belong to `<id>` on this map. Do not draw it separately |
| `ABSENT` | It does not exist yet on this map. Draw nothing |
| `NON-TERRITORIAL` | It exists as a people but holds no ground — see Hakka below |

**The algorithm, for any map X:**

1. Take every polity whose `status_map_X` is `SOVEREIGN`.
2. Its territory is **its own `provinces` plus the provinces of every polity that has merged into it**,
   following `MERGED:` chains **transitively**.
3. Draw that union in the polity's `color_hex`.

**Transitivity matters.** On Map D, Qinghai is `MERGED:SIN` directly — but on Maps B and C it is `MERGED:NW`,
and `NW` is itself `MERGED:SIN` on D. Resolve chains fully before drawing, and the same set of provinces will
come out either way.

**`SIN` and `KOR` are pure containers.** Both have `provinces = "-"`. They exist only to receive merges, which
is why they are `ABSENT` on the maps where the merge has not happened.

---

## Per-Map Specification

### Map A — Fragmented

**Nineteen sovereign states.** The most crowded map in the series, and deliberately so.

- **Nine Han states:** the North China Plain, the Northwest, Bashu, Jin, Wu, Gan, Xiang, Min, Yue.
- **Qinghai stands alone** — its only appearance as a sovereign state.
- **Mongolia and Inner Mongolia are separate.**
- **Korea is two states.**
- Manchuria, East Turkestan, Tibet, Taiwan, Japan as on every map.

**Two colors are deliberately near-identical to their neighbors**, so a reader sees the coming merge before it
happens: **Qinghai** `#6FA8B8` against the Northwest's `#2E8CA8`, and **Inner Mongolia** `#F0B860` against
Mongolia's `#E8963C`. Keep them that way.

### Map B — Semi-Unified

**Two merges, and nothing else moves.** Qinghai into the Northwest; Inner Mongolia into Mongolia.

### Map C — Semi-Unified

**Korea becomes one.** China is still nine states. Jeju-do is ordinary Korean territory.

### Map D — Semi-Unified

**The Sinian Federation is founded** from the nine Han states — plus Qinghai, which arrives inside the
Northwest. **Korea is still two states**, because D branches from B, not from C.

**Manchuria, East Turkestan, Tibet and Taiwan do not join the Federation, on this map or any later one.**

### Map E — Unified

**C and D converge.** Korea is one and the Federation exists. **Jeju-do is still ordinary Korean territory** —
the Court has not been founded.

### Map F — Unified

**Identical to E except that Jeju-do detaches from Korea** and becomes neutral ground, legally shared among
Korea, Japan and the Sinian Federation. See the Jeju section below — it needs more than a fill color.

---

## Constant Across All Six Maps

**Do not change these between maps.** Same projection, extent, graticule, palette, typography, city set and
legend structure throughout — the series only reads as a series if everything not changing stays still.

- **Whole first-order subdivisions only.** Never split a province, autonomous region or municipality.
- **Russia is deferred.** Three seams are **white and unclaimed** — not Russian, not anyone's: **Outer
  Manchuria** (north of the Amur, east of the Ussuri), **Sakhalin and the Kurils**, and **Buryatia and Tuva**.
  The rest of Russia is out-of-scope grey.
- **Out of scope, in grey:** Southeast, South, Central Asia and the Middle East.
- **Nothing is hatched** except Hakka. There are no undecided borders left in East Asia.
- **No dates on any map.** Captions name events, not years.

### Hakka — on every map, in every era

**Forty-four million people and no ground, ever.** Draw as **scattered hatched circles** in the hills where
Guangdong, Fujian and Jiangxi meet, with a leader line labeled **"Hakka (no territory)"** and its own legend
entry. **Never give it a border.** On Maps D–F it sits inside the Federation and is still drawn.

### The Tian Shan — on every map

An **internal dashed line** inside East Turkestan, labeling **TARIM** south and **DZUNGARIA** north. It marks
a real seam — a 95% non-Han south against a Han- and Kazakh-majority north — that the whole-subdivision rule
forbids turning into a border. **It is not a border. Do not draw it as one.**

### Jeju-do — Map F only

It renders at roughly **13 × 8 pixels**, against Taiwan's 44 × 107. Color alone cannot carry it.

1. **Fill `#F5C518` bright gold.** Not a dark color — a dark fill merges with the island's own coastline stroke.
2. **Thin its stroke** to about half the standard coastline weight, and **add a 2–3 px white casing** outside
   the island so it separates from the archipelago clutter.
3. **Add a magnified inset** — a circular callout in the open sea southeast of Korea, **Jeju at roughly 8×**,
   labeled **JEJU-DO** with *"neutral ground — Korea · Japan · the Sinian Federation"* beneath, and a fine
   leader line back to the real island.
4. **Optional and recommended:** ring the inset with **three equal arcs** in Korea `#8E6FB8`, Japan `#D4527D`
   and the Sinian Federation `#3FA9C9`. That states the condominium in the one place with room to state it.
   The island itself stays gold; the arcs go on the ring.
5. **Its legend entry goes in its own class**, below the nations block, with a divider above it. **Jeju is not
   a nation.**

---

## Do Not

- **Do not hatch anything but Hakka.** Every border question is settled. A surviving hatch is a bug.
- **Do not draw Qinghai, Inner Mongolia, the two Koreas or Jeju-do as separate on maps where their status is
  `MERGED`.** Resolve the chains first.
- **Do not let Manchuria, East Turkestan, Tibet or Taiwan join the Federation** on any map.
- **Do not extend Tibet beyond the TAR** on any map.
- **Do not put a date on any map.**
- **Do not draw region "Yungui."** It never forms — Yunnan and Guizhou are Bashu provinces, then Federation
  provinces.
- **Do not re-letter the maps.** A–F are referred to by letter throughout the project's notes.

---

## One Known Refinement, Not Required

**The domain/sphere distinction has never been rendered.** Every region is flat core fill. The parent folder's
data carries `domain_territory` and `sphere_territory` per region, intended as reduced opacity and a dotted
outline. As things stand it is invisible that Tibet's sphere covers Kham, or that Manchuria's domain reaches
into eastern Inner Mongolia. If taken up, **apply it across all six maps** so the series stays consistent.
