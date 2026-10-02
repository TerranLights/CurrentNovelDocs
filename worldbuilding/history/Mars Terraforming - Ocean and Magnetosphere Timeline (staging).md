# Mars Terraforming — Ocean and Magnetosphere Timeline (staging)

> **Status: PROPOSED, not verified.** This is research/reasoning toward a physically-defensible timeline, not
> settled canon. Per `worldbuilding/README.md`, nothing here should be treated as final until every open
> question below is closed and it is promoted to `TepenianUniverseTimeline`. Written 2026-09-28, developed for
> **The Cryptograph Helix** (Mars is the primary setting for Books 1–4), but scoped here rather than in that
> book's own repo because Mars's terraforming status is a shared-universe fact — true regardless of which book
> is being read, per the folder's own inclusion rule ("if it would still be true with a given book deleted, it
> belongs here").

## Why this exists

`TheCryptographHelixDD/world/locations.md` already states Mars is "extensively developed and partially
terraformed" at series opening, with hab domes still in use (domes degrade from "Level V to Level IV" in one
city). That's consistent with the reasoning below, but it was asserted without a worked timeline behind it. This document works out *how long* partial terraforming plausibly
takes, so the "partial" in "partially terraformed" has a physically-grounded amount of elapsed time behind it —
and so that elapsed time can be checked against the gap between the Long Night War (2812) and the series'
fluid ~3000s–3100s opening.

## The three sub-problems

Mars terraforming isn't one process — it's three, and they don't have to run in strict sequence.

### 1. Magnetosphere — the fast one

Re-melting Mars's core to restore a natural dynamo is not viable on any human timescale — that's a geological
process. The physically real alternative is an **artificial shield**: a superconducting magnetic dipole station
positioned at the Mars–Sun L1 Lagrange point, deflecting solar wind before it reaches the planet and strips the
atmosphere. This is a genuine NASA-workshop proposal (Green et al., 2017), not invented for this universe.

Once the power generation and superconductor technology exist, deployment is an **installation** timescale, not
a geological one — plausibly **years to a few decades**. This is the cheap step. The expensive part is
everything downstream of it staying protected, and whether coverage is complete or still has gaps (a *partial*
shield is a legitimate intermediate state, not just "not started yet").

### 2. Atmosphere — the medium one

Mars already holds most of the raw material: CO2 frozen into the polar caps and regolith, plus subsurface
reserves. Engineered approaches — orbital mirrors to sublimate the poles, synthesized super-greenhouse gases
(PFC-class), imported volatiles from redirected asteroids/comets — could plausibly thicken the atmosphere to a
workable pressure in **100–300 years** given megascale industrial capacity (roughly the Zubrin-era estimate for
aggressive-but-physically-real terraforming).

A fully **breathable** O2 atmosphere is much slower if it depends on photosynthesis — that's a multi-thousand-year
process. But a **thick CO2/N2 atmosphere plus a magnetic shield holding it in place** doesn't require breathable
air — just enough pressure and greenhouse effect for liquid water and powered/suited habitation. That's almost
certainly the right regime for "partial" Mars, and it matches the existing canon detail that hab domes are still
necessary and still degrading.

### 3. Ocean — actually the fastest, once the other two exist

This is the pleasant surprise: Mars doesn't need imported water for a partial ocean. Existing estimates put
polar-cap and subsurface ice at roughly enough water to cover the whole planet **20–40 meters deep** if melted
and pooled — and there's a real destination for it, the ancient Vastitas Borealis basin in the northern
lowlands, which is where a genuine Martian ocean would naturally collect (it held one billions of years ago).

Once (a) atmospheric pressure is enough to keep liquid water stable and (b) there's enough heat/greenhouse
effect to melt the ice, filling that basin is a matter of **decades**, not centuries — the fastest of the three
steps, and it happens *after* the atmosphere work, not before. Redirected comets/ice asteroids are optional
bonus mass, not a requirement, and would run in parallel with the atmosphere-building phase (orbital redirection
of icy bodies is itself a decades-long project, so there's no scheduling cost to doing it concurrently).

## Rolled together

| Approach | Magnetosphere | Atmosphere | Ocean | Total (partial terraforming) |
|---|---|---|---|---|
| Conservative (near-future engineering, no exotic tech) | 20–50 yrs | 300–1000 yrs | +50–100 yrs after atmosphere | ~500–1200 yrs |
| Aggressive (megascale industry, synthesized super-GHGs, orbital mirrors) | 10–20 yrs | 100–300 yrs | +20–50 yrs after atmosphere | ~150–400 yrs |
| **Tepenian-tier** (post-DNA-computing, orbital infrastructure, genetic/nano engineering already routine) | ~10 yrs | 100–200 yrs | +20–30 yrs, overlapping | **~150–250 yrs** |

The Tepenian-tier row is a judgment call, not a derived number — it assumes the DNA-computing and genetic/nano
engineering baseline already established for this universe compresses the "aggressive" row somewhat further,
without inventing new physics to do it.

## Cross-check against the existing timeline

Per `TepenianUniverseTimeline`, the Long Night War is dated 2812. The Cryptograph Helix opening date is
currently fluid, ~3000s–3100s (see `TheCryptographHelixDD/TODO.md`'s open item reconciling the "nearly 900
years" line). That puts the gap between the Long Night War and series-opening at roughly **200–300 years** —
which sits almost exactly inside the Tepenian-tier aggressive band above.

That's a useful signal, not a coincidence to force: it means **a partial ocean (filling the northern lowlands,
not a planet-covering sea) plus a partial/artificial magnetosphere (an L1 shield installed but not necessarily
at full coverage)** at series-opening is the physically honest outcome of "how much progress is achievable in
~200–300 years," even with strong post-scarcity tech. A *fully* oceaned, fully shielded, breathable-air Mars
would actually be too fast for this timeline, and would undercut the frontier/fragility texture Mars needs at
series open — struggles like dome integrity and incomplete atmospheric/water coverage only make sense if
terraforming is *visibly incomplete*, not finished.

## Open questions (must close before promotion)

- [ ] Exact founding date for when Tepenian Mars terraforming *began* — needs to be fixed before "~200–300
      years of progress" can become a specific in-world claim rather than a range.
- [ ] Whether the L1 magnetic shield is framed as a Tepenian invention/deployment, or as some inherited/scavenged
      Upper Earth infrastructure repurposed by the exile population — affects who gets credit/blame for it
      in-story and whether Upper Earth factions have any leverage over it.
- [ ] Whether "partial ocean" means the Vastitas Borealis basin is fully filled to some stable shoreline, or
      still filling/unstable at series-opening — affects whether coastal settlement is possible yet.
- [ ] How this reconciles with the "nearly 900 years" line in `series-overview/themes-and-structure.md`
      (tracked separately in Cryptograph Helix's own TODO — this document assumes that gets resolved toward the
      ~200–300 year end, not the ~900 year end, since ~900 years would blow well past the Tepenian-tier estimate
      above and imply Mars *should* be much further along than the existing "hab domes still needed" canon
      shows).
- [ ] Whether other Tepenian-era Mars settlement (if any predates the exile) affects the starting conditions, or
      whether terraforming begins from scratch with the post-Long-Night-War diaspora.

## Sources referenced (real-world, for the physical reasoning above)

- Green, J. L. et al. (2017) — NASA Ames workshop proposal for an artificial magnetic dipole shield at the
  Mars–Sun L1 point.
- Zubrin, R. — *The Case for Mars*, terraforming-timescale estimates (the ~100–300 year "aggressive" figures
  for atmospheric thickening via engineered greenhouse gases).
- Standard planetary-science estimates of Martian polar-cap and subsurface ice volume (the 20–40 m
  global-equivalent-ocean figure).
