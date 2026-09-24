# UPDATE SHEET — Make Jeju-do Readable

> ⚠️ **PARTLY SUPERSEDED, 2026-09-23.** Any instruction below to hatch the six southern subdivisions or
> to cross-hatch Qinghai is **out of date** — both questions are settled and **nothing on these maps is
> hatched any more.** See `UPDATE 03 - Qinghai Settled.md` and `UPDATE 04 - Southern Border Settled.md`.
> Everything else in this file still stands.

**Self-contained. Hand this over on its own**, with `asia-east-post-court.png` and its `ea_nations.py`.

2026-09-23. Follows `y-files/Map Files/Asia (East)/03 follow-up/`.

---

## The Problem, Measured

Jeju-do came out in dark slate `#3D4A5C` and is **not distinguishable from Korea or the Sinian Federation at
map scale.** The cause is not really the hue. It is the size:

| | Rendered size | Fill pixels |
|---|---|---|
| **Jeju-do** | **13 × 8 px** | **47** |
| Taiwan | 44 × 107 px | 2,455 |

**Jeju has 47 pixels to work with, on a map 3,360 pixels wide. Taiwan has fifty-two times more.**

And only **45% of Jeju's own bounding box is fill** — the island's black coastline stroke eats the rest. So a
**dark** fill was close to the worst possible choice: it merges with the very outline that surrounds it, and
the whole feature reads as one dark smudge.

**The earlier instruction to make it dark so it "reads as a special case" was wrong.** That reasoning holds for
large regions. Small features need the opposite: **high brightness and high saturation**, plus separation from
their own outline.

---

## Fix 1 — Change the color

| | |
|---|---|
| **Was** | `#3D4A5C` dark slate |
| **Now** | **`#F5C518` — bright gold** |

Gold is the furthest thing on the map from the pale blue-grey sea it sits in, which is what matters for a
feature this small. It is also semantically right for a court — institutional, a seal, a standard — where a
dark slate read as nothing in particular.

**Check against Map D's palette:** nothing else is a saturated gold. The nearest neighbor is Inner Mongolia's
muted `#F0B860`, which is far away geographically and much lower in chroma. **If gold still reads poorly,
the fallback is vivid red `#E8332C`** — no true red exists anywhere on this map.

## Fix 2 — Stop the outline eating the island

At 13 × 8 px the standard coastline stroke consumes more than half the shape.

- **Thin Jeju's own stroke** to roughly half the standard coastline weight, or drop it to a mid-grey.
- **Add a white casing** — a 2–3 px white halo *outside* the island — so it separates cleanly from the sea
  rather than blending into the coastline clutter of the southern archipelago.

These two changes alone roughly double the readable fill area.

## Fix 3 — Give it an inset. **This is the real fix.**

**Forty-seven pixels cannot carry a three-power condominium that hosts the most consequential court in the
setting.** No color will make it carry that. This is exactly the situation atlases solve with a magnified
callout, and it should be solved the same way here.

**Add a circular inset** in the open sea southeast of Korea — there is clear empty water between the peninsula
and Japan, and the existing Taiwan leader line shows the visual idiom is already in use.

- **Magnify Jeju roughly 8×**, so it renders at about 100 px across.
- Draw the island in `#F5C518` with its coastline, and label **Jeju City** and **Seogwipo**.
- Ring the inset with a thin dark circle and connect it to the real island with a fine leader line.
- **Title the inset "JEJU-DO"**, and beneath it, small: *"neutral ground — Korea · Japan · the Sinian
  Federation."*

**Optional, and a nice touch if it can be done cleanly:** ring the inset circle with **three equal arcs** in
the three parent colors — Korea `#8E6FB8`, Japan `#D4527D`, the Sinian Federation `#3FA9C9`. That states the
condominium visually, in the one place on the map where there is room to state it. Keep the island's own fill
gold; the arcs go on the ring, not the land.

---

## Everything Else Stays As It Is

`asia-east-post-court.png` is otherwise correct and should not be rebuilt from scratch. Unchanged:

- Korea unified, minus Jeju, in `#8E6FB8`.
- The Sinian Federation with the six undecided subdivisions hatched.
- Japan, Manchuria, Mongolia, Inner Mongolia, East Turkestan, Tibet, Taiwan.
- The Tian Shan as an internal dashed line. **Qinghai is now settled Federation territory — no cross-hatch.**
- The three unclaimed seams in white; out-of-scope grey.
- Projection, extent, graticule, fonts, city dots, caption, and the rest of the legend.

**The legend entry stays where it is** — its own class, below the nations block — but **update its swatch to
gold**. Text unchanged:

> **Jeju-do — neutral ground**
> *International Court of Diplomacy · shared by Korea, Japan and the Sinian Federation*

---

## Do Not

- **Do not enlarge Jeju itself on the main map.** Its true size is correct; the inset carries the detail.
  Inflating the island would be a false map.
- **Do not put a date on the map.**
- **Do not draw Jeju as a nation** — it stays in its own legend class, not in the nations block.
- **Do not regenerate the other three maps** in the series.
