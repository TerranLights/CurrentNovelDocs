# Object-Oriented Location Synthesis and Derivation (OOLSD)

**Status: scaffolding and design brief. Created 2026-10-06 at the developer's direction. Not canon, and not worldbuilding.**
It is logistical management, so it can be worked at any hour. The deep-synthesis hours law (`05:00`–`14:59`) does not
apply to this folder. It would apply again the day anyone derives a *specific* location from it.

## What this is for

A proportion of Tepenia's population leaves Antarctica. Of everyone who leaves, the majority leave during peacetime,
and the rest flee during the Long Night War. (It is *not* that most of the country left.)
They settle low Earth orbit first, then Mars, Venus and the Asteroid Belt (the opening setting of the *Cryptograph
Helix* novels). Late in that series they begin light, essential orbital infrastructure around Jupiter and heads toward
Saturn (the settings of *Outer Tepenia 1* and *2*). None of that is Antarctica, so the ULM, the CST and the RWBEM must
be **handed over** to the repos that will write it, in a form they can run without asking this repo anything.

**The obstacle, and why it is not a blocker.** The ULM understands a location partly through its origins. For Mars,
the origins are the neo-races and neo-cultures that Inner Tepenia's own cities and subnets produce. What kind of
countries would descend from the Mirny subnet, or Halley, or Palmer, or Janbogo is not knowable until the 38-city
corpus exists. A mass culture from Zhongshan would not found "China on Mars": its people would be Zhongshanese.
Mirny's would be Mirnian, not Russian (`No_National_Stereotypes`; the divergence operator, `00_RUNBOOK.md` §C.9d).

**The answer is to separate what is known from what is not, and to write the known part now.** A class declares what
physics, function and network position force on *any* place of its kind. It leaves named slots open for the rest.

## The model

| OO term | Meaning here | Where the ULM already has the machinery |
|---|---|---|
| **Class** | A kind of location, with everything true of every instance | `01` §1 (Type), §1.2 (modifiers: *Orbital / extraplanetary*, *Enclosed*, *Mobile*), §2 (Band), §3 (Status) |
| **Inheritance** | A subclass specializes a parent class | `01` §5.1: **Determined** (fixed by the parent), **Inflected** (parent's form, local version), **Originated**, **Aggregated** |
| **Invariant** | Fixed by the class, whatever the instance | the early-bound generators: G2 physical, G3 function, G5 network position |
| **Slot** | A named field the class leaves open | `05` §1: **PROVIDED**, **RESERVED**, **REQUESTED** |
| **Instance** | One specific place (a named Mars nation, a named habitat) | a ULM pass on one location |
| **Late binding** | An instance binds its open slots when their data exists | `01` §5.2 (provisional-inheritance protocol) and Gate P (the parent must reconcile against children's registered assumptions) |

**Late binding is not new.** `01` §5.2 already says writing a child before its parent is "the normal case, not the
exception". It requires every dependent finding to carry a numbered provisional assumption, registered where the
parent's eventual pass will see it. This library applies that rule at the scale of a class library.

### Slots, and when each binds

Proposal, to be confirmed in `02_Design_Brief.md` §3.

| Generator | Binds | Because |
|---|---|---|
| **G2** Physical and environmental | **early** | It depends on the body and the orbit, not on who lives there |
| **G3** Function and purpose | **early** (mostly) | An infrastructure's job is fixed by the class; only what it is *for locally* is open |
| **G5** Network position | **early** | Where it sits in the supply, signal and transit network |
| **G7** Real-world inspiration | **early**, as research | Comparables enter as mechanism only, tagged `[RW]` (`DR-15`) |
| **G4** Founding condition | **split**: mechanism early, *who* late | Who sent them, by what route, under what pressure |
| **G6** Defining event | **late** | Events in the interwar and Solar Colonization eras are not yet written |
| **G8** Demographic composition | **late** | It needs the neo-cultures that the 38-city corpus produces |
| **G1** Symbolic substrate | **deferred** | `DR-8` defers it at city scale; the same deferral is assumed here until a ruling says otherwise |

## Two packages

- **Package 1, now.** The method with its Antarctic data separated out. The class library: declarations, invariants,
  open slots and what each slot binds from. Provisional assumptions and requests, registered. **No instance content.**
- **Package 2, after the 38-city ULM.** The origin data pack. It holds the neo-culture and neo-race findings, the
  composition weights and the founding data that fill the slots. Instance passes run only then.

## Pointers now, copies later

**Now:** every dependency is a pointer, an absolute path in `03_Pointer_Manifest.md`. **At handoff:** the cited data is
copied in, so the receiving repo is self-contained. The manifest is the copy list.

## Order of consumers

1. **`CurrentNovelDocs`**: low Earth orbit. It is closest to the origins, and its people are one removal from the
   Antarctic cities.
2. **`The Cryptograph Helix series`**: Mars and its orbit, Venus, the Asteroid Belt, early Jovian infrastructure.
3. **Later, the Outer Tepenia games.** *(Noted at the developer's direction, 2026-10-06.)* The library will eventually
   serve the Jovian and Saturnian settings, and New Centauri's much later interstellar setting. Classes should
   therefore not assume the Solar System's boundaries.

## What is established, and what is not

- **LEO:** very little is established. `Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/` already exists as the
  shared source for the novel and TV repos. It holds **one file**, a 40-line README that is scaffolding only. This
  library points at it and does not duplicate it. That README held its "planned structure" until the developer said
  so, and the developer has now said so for the library. Nothing has been built in that folder yet. (The sibling
  `Upper-Earth/` holds a 7-line `Timeline.md` and an empty `Geography.md`.)
- **The three build stages** (robot-only staging stations, then O'Neill Cylinders, then Von Braun Wheels with
  Cylinders) are canon. See `03_Pointer_Manifest.md`. The cause of the orbital population's human-heavy tilt is
  **open**; this library does not settle it.
- **Mars, Venus, the Belt, Jupiter, Saturn:** only the timeline's outline exists. Nothing about their societies does.

## Rules this folder inherits

- **No instance content.** No named Mars nation, no culture, no composition, no demonym.
- **Origin is not identity.** Stock names come from Inner Tepenia's cities and subnets. They never map to a
  present-day nation, and no stereotype is licensed (`No_National_Stereotypes`).
- **Research before numbers.** Package 1's G2 sections need real, sourced physical data (`LAW 0-R`). **No physical figure
  in this library is written from recall.**
- **Physics fidelity.** Anything not on the handwave register obeys known physics (`02_Design_Brief.md` §8).
- **No level-scaling**, as in every game design under this developer.
- **American English.**

## Files

| File | What it is |
|---|---|
| `README.md` | this file |
| `01_Inventory_Universal_vs_Antarctic.md` | what in the ULM, CST and RWBEM is universal and what is Antarctic-specific, with the handoff action for each |
| `02_Design_Brief.md` | the class declaration template, the slot taxonomy, the starting class list (non-exhaustive), the binding rules and the open questions |
| `03_Pointer_Manifest.md` | every pointer, verified or not, and the copy list for handoff |
| `04_Handwave_Register.md` | the enumerated handwaves (nanotech gel-brain consciousness is H-1). Anything not on it obeys known physics. |
| `classes/` | class declarations, one file per class, drafted from the template in `02_Design_Brief.md` §1. `01_Robot-Only_Staging_Station.md` is the first (a test of the template). |
| `research/` | the sourced physics data per body group, with search logs. `_BRIEF.md` is the shared research brief; `_inputs/` holds downloaded transcripts and other source material. |
| `research/DEFERRED_RESEARCH.md` | searches to run again later, with what to try next. Separate from the shopping list. |
| `research/SHOPPING_LIST.md` | sources the research agents could not open, grouped by who can get them. Anything obtained goes in `research/_inputs/`. |
