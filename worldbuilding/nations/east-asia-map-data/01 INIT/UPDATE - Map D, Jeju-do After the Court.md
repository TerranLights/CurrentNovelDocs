# UPDATE SHEET — Build Map D: East Asia After the Court

> ⚠️ **PARTLY SUPERSEDED, 2026-09-23.** Any instruction below to hatch the six southern subdivisions or
> to cross-hatch Qinghai is **out of date** — both questions are settled and **nothing on these maps is
> hatched any more.** See `UPDATE 03 - Qinghai Settled.md` and `UPDATE 04 - Southern Border Settled.md`.
> Everything else in this file still stands.

**Self-contained. Hand this over on its own**, together with `regions-main.csv` and the existing
`ea_nations.py`. Everything needed is below; the other files in this folder are background, not prerequisites.

2026-09-23. Follows the round that produced `asia-east-nations.png`, `asia-east-sinian-federation.png` and
`asia-east-early-era.png` in `y-files/Map Files/Asia (East)/02 follow-up/`.

---

## The Job, in One Line

**Copy the existing nations map and recolor one island.** That is genuinely the whole change.

There is now a **fourth map in the East Asia series**, set after the founding of the International Court of
Diplomacy at Jeju-do. It is identical to `asia-east-nations.png` except that **Jeju-do is drawn as its own
territory in its own color**, because by that point it is no longer simply Korean.

**Output filename:** `asia-east-post-court.png`

**Do not modify the three existing maps.** They remain correct for their own moments. This is an addition.

---

## The Canon Behind It

**Author, 2026-09-23:** upon the founding and establishment of the **International Court of Diplomacy at
Jeju-do**, Korea delegated Jeju-do as **neutral ground, to be legally shared among itself, Japan, and the
Sinian Federation.**

A stipulation of that arrangement: **Korean, Japanese and Mandarin are all equally valid before the Law**,
but **where a conflict-in-translation arises, the Korean text takes precedence** — the role English plays in
present-day international instruments.

So Jeju-do is a **three-power condominium with a standing international court on it**. It is not a fourth
nation and should not read as one.

---

## The Change, Precisely

### 1. Geometry

Draw **Jeju-do** as a separate filled region, subtracted from Korea.

It is **Jeju Special Self-Governing Province**, a **first-order subdivision** of South Korea — so this does
**not** break the project's whole-subdivision rule, which forbids splitting provinces. Jeju is a whole one.

⚠️ **Check the exact `name` value in the Natural Earth admin-1 shapefile before relying on it** — the layer
has used both **`Jeju`** and **`Cheju`** for this province across releases. Pull it the same way Chinese
provinces are pulled, but with `admin == 'South Korea'`. Then subtract it from the Korea polygon so the two
do not overlap:

```python
JEJU = a1[(a1.admin == 'South Korea') & (a1.name.isin(['Jeju', 'Cheju']))].geometry.iloc[0]
N['KOR'] = (2, N['KOR'][1].difference(JEJU))
```

Approximate extent, as a sanity check only: **33.10–33.60 N, 126.15–126.98 E.** Anchor settlements: Jeju City,
Seogwipo.

### 2. Color

| | Hex |
|---|---|
| **Jeju-do** | **`#F5C518`** — bright gold |
| *(Korea, unchanged)* | `#8E6FB8` purple |
| *(Japan, unchanged)* | `#D4527D` rose |
| *(the Sinian Federation, unchanged)* | `#3FA9C9` cyan |

**High brightness and high saturation are the requirement**, because Jeju renders at only about 13 × 8 pixels
— roughly 47 fill pixels, against Taiwan's 2,455. Gold is the furthest thing on the map from the pale
blue-grey sea around it. **Do not use a dark fill**, which merges with the island's own coastline stroke, and
**do not tint it toward any of its three parents** — the point is that it belongs to all three and to none.

**At this size the island needs a magnified inset, not just a color.** See
`UPDATE 02 - Jeju-do Legibility.md`, which supersedes this section.

### 3. Label and legend

Label on the map:

> **JEJU-DO**

New legend entry, placed **below the nations block and above the hatching block**, with a divider rule above
it so it is visibly a different class of thing:

> **Jeju-do — neutral ground**
> *International Court of Diplomacy · shared by Korea, Japan and the Sinian Federation*

### 4. Caption

> **ASIA (EAST) — the Court years**
> *After the founding of the International Court of Diplomacy at Jeju-do*
>
> Jeju-do is neutral ground, submitted by Korea and legally shared with Japan and the Sinian Federation.
> Whole first-order subdivisions only. Hatching marks an undecided border. No dates are implied.

---

## Everything Else Stays Identical

Carry over from `asia-east-nations.png` without modification:

- **The Sinian Federation**, unified, with the six undecided subdivisions hatched.
- **Korea**, unified — now minus Jeju, but otherwise the same shape and the same purple.
- **Japan, Manchuria, Mongolia, Inner Mongolia, East Turkestan, Tibet, Taiwan** — unchanged.
- **Qinghai** — settled Federation territory, drawn solid. No cross-hatch.
- **The Tian Shan** — an internal dashed line inside East Turkestan, not a border.
- **The three unclaimed seams** — Outer Manchuria, Sakhalin and the Kurils, Buryatia and Tuva — in white.
- **Out of scope** in grey: Russia, and Southeast, South and Central Asia.
- Projection, extent, graticule, fonts, city dots, legend structure, footer note.

---

## Do Not

- **Do not put a date on the map.** Not the Court's founding, not 2318, not anything. The map is captioned by
  event, not by year.
- **Do not draw Jeju as a nation.** No entry in the nations block of the legend; it goes in its own class.
- **Do not split any province** to achieve anything here. Jeju works precisely because it is already whole.
- **Do not alter Korea's borders** other than removing Jeju.
- **Do not regenerate or overwrite** the three existing maps.

---

## Why This Is a Separate Map Rather Than a Correction

The existing nations map is **not wrong**. It depicts a real and reasonably long stretch of time during which
Korea is unified, the Sinian Federation exists, and the Court has not yet been founded — so Jeju is still
ordinary Korean ground.

| Map | Korea | The Federation | The Court | Jeju-do |
|---|---|---|---|---|
| `asia-east-early-era.png` | two states | does not exist | — | ordinary Korean ground |
| `asia-east-nations.png` | unified | exists | **not yet founded** | ordinary Korean ground |
| **`asia-east-post-court.png`** | unified | exists | founded | **neutral, shared three ways** |

That window is roughly **two generations** wide: Korea's reunification and the Federation's founding both
happened at least three and possibly four generations before the Court's April 27, 2318 ruling, while the
Court itself was established at least one full generation before it. **Both maps are correct. They are
correct at different times.**

---

## Optional, If There Is Appetite

Neither is required, and neither blocks the above.

**A. Two color collisions on the early-era map.** `asia-east-early-era.png` draws two pairs in identical hex,
because the palettes were assigned per source file and that map is the first to show both at once:

- **Jin `#E8963C`** and **Mongolia `#E8963C`**, separated only by Inner Mongolia's lighter orange
- **Wu `#8E6FB8`** and **Korea `#8E6FB8`**, separated by the Yellow Sea

Both read acceptably at full size. If corrected, **shift Jin and Wu, not Mongolia or Korea** — the latter two
are canon nations whose colors recur on other maps in the series.

**B. The domain/sphere distinction has never been rendered** on any map in the series. Every region is flat
`core` fill. The data carries `domain_territory` and `sphere_territory` for each region, intended as reduced
opacity and a dotted outline respectively. As it stands it is invisible that Manchuria's domain reaches into
eastern Inner Mongolia, or that Tibet's sphere covers Kham. If taken up, apply it across all four maps for
consistency.
