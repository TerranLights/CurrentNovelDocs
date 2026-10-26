# OOLSD Design Brief: the class template, the slots, the starting class list

**Created 2026-10-06. Status: proposal for developer review. Nothing here is canon, and no instance content is written.**
The model (Classes, Instances, Late Binding) was confirmed by the developer on 2026-10-06. Everything below is a
proposed way to make it concrete, and the class list is **explicitly non-exhaustive**: "there will be many, many, many
more Classes."

**Research rule.** No physical figure appears in this file. Every G2 section needs real, sourced data gathered under
`LAW 0-R`, and a recalled number is a guess in a confident tone. Where a physical *kind* of fact is needed, this brief
names the field and leaves it empty.

## 1. The class declaration template

One declaration per class. Fields in order.

| # | Field | What it holds | Binds |
|--:|---|---|---|
| 1 | **Name and parent class** | The class, and the one it specializes (or "root") | early |
| 2 | **ULM frame** | Primary type **by era** (it may change: see §6, answer 1); modifiers; population band as a *range*; status options | early |
| 3 | **Inheritance (ULM `01` §5.1)** | For each cultural element the class touches: Determined / Inflected / Originated / Aggregated, *and as of which Act or era* (the instrument is Act-blind, `M-157`) | early |
| 4 | **Invariants: G2 physical** | The physical fields the body and orbit fix. **Values: to be researched.** | early |
| 5 | **Invariants: G3 function** | What the class is *for*, in the network, whoever lives there | early |
| 6 | **Invariants: G5 network** | What it needs from elsewhere; what flows; in which direction. Relation, never comparison. | early |
| 7 | **Real-world comparables (G7)** | Mechanism only, tagged `[RW]` (`DR-15`) | early, researched |
| 8 | **Open slots** | Each: name · what binds it · status (`BOUND` / `PROVISIONAL` / `OPEN`) · what a pass writes meanwhile | late |
| 9 | **Registered assumptions** | The numbered provisional assumptions any instance may rest on (`01` §5.2 step 5) | late |
| 10 | **Requests** | What the class cannot get without new input, in the `05` §5 REQUESTED form | late |
| 11 | **Instance obligations** | Which phases and gates are mandatory for an instance of this class, and which are meaningless | early |

### Slot status values

- **`BOUND`**: a source exists and is cited.
- **`PROVISIONAL`**: filled by a tagged assumption, registered so a later pass reconciles against it. `01` §5.2 rule 4
  holds: **do not build an instance's strongest finding on a provisional slot.** Build on the invariants.
- **`OPEN`**: nothing fills it. The pass writes a null with its reason and states plainly that "none is sited here"
  is not "none is possible" (the Law of No Forced Fit).

## 2. What can be bound now, and what cannot

Derived from the generator ratings in `02` §2. This is the proposal that `README.md` summarizes.

| Early-bound (Package 1) | Late-bound (Package 2) |
|---|---|
| **G2** physical and environmental. The body, orbit, radiation, gravity regime, light, thermal, resupply geometry, signal delay. | **G8** composition: which neo-cultures, in what tier weights |
| **G3** function: the class's job in the network | **G6** defining events: not yet written for the interwar and Solar Colonization eras |
| **G5** network position: what it needs, what flows | **G4** who: which exile or migrant stock, under what pressure (the *mechanism* binds early) |
| **G7** research, as `[RW]` mechanism | local culture, name, symbol |

**The rule for the early column:** a statement goes in only if it would be true for any people at all, from any origin,
after any history. "Would this still be true if the settlers were from a different subnet?" is the test.

## 3. How composition binds (Package 2), and what Package 1 must not pre-empt

- **Stocks are Tepenian, not present-day.** A Mars instance's composition is expressed as **ancestry from Inner
  Tepenia's cities and subnets**, in the same tiers (Primary / Significant / Notable) the census uses. Tiers are
  weights, not headcounts (`DR-12`).
- **Origin names the stock; separation and environment produce the culture.** Apply the divergence operator
  (`00_RUNBOOK.md` §C.9d): **separation · local environmental setting · local struggles and hardships · local goals ·
  local sensibilities and habits.** Never reason from elapsed time, which is the same for every place.
- **Two bodies, not one.** Robots live, work and come online in orbit. Every class that has residents answers for
  both. The robot canon (`Robot_Physiology_and_Cultural_Practices.md`, `Robot_Universals/`) binds the whole universe
  (`00_RUNBOOK.md` §C.10), and orbit does not suspend it. Several of its claims were written for Antarctic cold and
  **must be re-derived for vacuum, radiation and microgravity**, not assumed to carry over.
- **Differentiate locally; converge nationally.** Whether a "national" layer exists above a Mars instance is itself open.
- **The data pack that fills these slots** is the 38-city corpus plus its downstream material (subnet regional
  personalities, the Founding Register, the Acts). Pointers are in `03_Pointer_Manifest.md`.

## 4. The starting class list (non-exhaustive)

Sources: the developer's account of the setting (2026-10-06), and the build order already in canon. **"Proposed" means
a class name and its ULM frame guess only.** No invariant is filled in.

| Class (proposed) | Parent | ULM frame (proposed) | Status of what exists |
|---|---|---|---|
| **Orbital habitat** | root | Settlement or Structure; **Orbital**, **Enclosed** | abstract parent for the next three |
| **Robot-only staging station** | Orbital habitat | Installation or Structure; Orbital. No residents of the human body. | **canon stage 1.** Little else. |
| **O'Neill Cylinder** | Orbital habitat | Settlement + Structure; Orbital, Enclosed | **canon stage 2.** The primary long-term residence in orbit. |
| **Von Braun Wheel** | Orbital habitat | Vessel + Structure; Orbital, Enclosed, Mobile | **canon stage 3.** A mobile construction-and-transit type, "not a competing permanent-residence type". |
| **Orbital transit route** | root | Corridor or Interstitial | open: see §6 question 1 |
| **Surface settlement, low-gravity body** | root | Settlement; Enclosed; possibly subterranean | **nothing established** |
| **Surface settlement, Mars** | the one above | Settlement; Enclosed; Band **range** unknown | **nothing established beyond the timeline outline.** This is the case the developer named. |
| **Mars orbital infrastructure** | Orbital habitat | Structure; Orbital | **nothing established** |
| **Venus-region habitat** | root | Settlement; Enclosed; atmospheric rather than surface | **nothing established** |
| **Asteroid Belt works** | root | Installation or Settlement | **nothing established** |
| **Jovian orbital infrastructure unit** | Orbital habitat | Installation; "light, essential" | **timeline only** (late *Cryptograph Helix*). Fully developed in *Outer Tepenia 1*, not here. |
| **Saturn-bound expedition vessel** | root | Vessel | **timeline only**, very early stage |
| **Orbital network node** | root | Network locus | open: Solarnet exists as a canon term. Its nodes' placement does not. |
| **Station-built-by-others / inherited structure** | root | Resettled | open: a general case of `01` §1.2 *Resettled* in space |

A new class needs one of three things: a canon stage, a developer statement, or a physical distinction that changes the
questions a pass must ask.

## 5. Inherited open items that block specific classes

These are already open in canon. The library records them and does not settle them.

1. **The population figures.** The novel's founding figure ("12 million Tepenians who left during the later Second
   Interwar Period") against Census II's orbital population (10,104,964 combined). Same people counted two ways, or
   two populations? (`Orbital-Infrastructure/README.md`.)
2. **Why the orbital population is slightly human-heavy** (about 50.8 % human). The build order does not explain it,
   and the leading candidate is migration behavior. This is a creative call. It blocks the composition slots of every
   residential orbital class.
3. **Which station types exist beyond the three stages** by the novel series' later timeframe.
4. **Whether orbital settlements are individually named**, as the Antarctic cities are.
5. **The reserved folder** `Neo-Races-and-Cultures/Orbital_Cryptograph_Helix_Era/` exists and is empty. It is the
   natural home for Package 2's orbital material.

## 6. Questions for the developer, and the answers so far

Answered 2026-10-06.

1. **Corridors versus Interstitials: Interstitial.** An Earth–Mars transfer route is an **Interstitial** for most of the
   span. As time nears the opening era of the *Cryptograph Helix* setting it may become a **Corridor**.
   **Consequence:** a class's ULM type can **change by era**. The template (§1, field 2) therefore takes a *type by era*
   list, not one type. `01` §3 (Status) already lets a place change state over time. A change of *type* is new, and
   `01` should say whether it is a new instance or the same instance in a new frame. **Open; flagged for the
   inventory's §4.**
2. **Class granularity: undecided, and deliberately.** "We can decide that as we go. It might be too early to tell."
   The brief carries both options. Each body's research file (see `research/`) records the physics once, so either
   choice can be made later without redoing it.
3. **G2 research now: yes.** As much real, sourced physics as can be gathered. Isaac Arthur's subtitle files, which the
   developer will download, are an input. See §8.
4. **Naming the library's units: not yet raised.** Class and Instance are kept for now.
5. **The Federation above orbit: still open.**

## 7. What Package 1 must never contain

- A named Mars nation, culture, demonym, or composition.
- A present-day nation or ethnicity used as a stock label.
- A stereotype, even as an inherited flavor.
- A physical figure written from recall.
- A legislature, court, currency or office. The currency law (`DR-3`) and the justice docket (`H42`) are
  project-wide, and the library inherits them.
- Any level-scaling of encounters, enemies or loot. That law is permanent, in every project.

## 8. The physics fidelity rule, and the handwave register

**Developer ruling, 2026-10-06:** there will always be some magical handwaving at some level. The example given is the
nanotech gel brain that gives a robot full consciousness and sentience. *How it works: who knows.* That is acceptable.
**What is not acceptable** is a robot who can "flap her humanlike arms and fly away".

**The rule.**
- **Anything that is not an enumerated handwave must satisfy known physics.** This covers every G2 field: gravity,
  radiation, thermal balance, orbital mechanics, light and signal delay, resupply, and structure.
- **A handwave is allowed only if it is on the register** (`04_Handwave_Register.md`), with a one-line statement of
  what is waved and what is *not*. A handwave covers its own mechanism. It does not cover physics around it.
- **A handwave never licenses a consequence by itself.** A robot's consciousness is waved. Her body is not: she is
  human-shaped and obeys mass, thrust, heat and radiation like any other body.
- **A candidate handwave is proposed to the developer.** It does not enter a class silently.

**Sources.** Real data first: space agencies, peer-reviewed papers, engineering handbooks. Isaac Arthur's videos are a
**popular-science secondary source**. They are good for scope and for leads. Every number taken from them is checked
against a primary source before it enters a class. Subtitle files go to `research/_inputs/` (see
`03_Pointer_Manifest.md` §G).
