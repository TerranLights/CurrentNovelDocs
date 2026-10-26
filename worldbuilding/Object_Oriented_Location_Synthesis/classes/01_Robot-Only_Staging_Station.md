# Class 01: Robot-only staging station

**DRAFT, 2026-10-11. Written to test the template in `02_Design_Brief.md` §1. Not canon. No instance content.**

**Status of every figure here.** Figures are **carried from the research files and not yet spot-checked** against their cited
sources (the review is pending). Each is tagged with where it came from: `[LEO §6]`, `[ROBOT §6]` and so on, meaning that
research file's §6 *Constraints* section. **Do not treat a tagged figure as settled.** `RESUME_HERE.md` has the review
steps, and its "Corrections to apply" table lists known errors in the first-tranche files.
**Canon source for the class itself:** the three-stage orbital build order (stage 1), from the project memory notes and
`TODO.md` ("Orbital infrastructure — logistics, mathematics, and dimensions"). I have not re-read `TODO.md` this session.

## 1. Name and parent

- **Robot-only staging station.** Parent: **Orbital habitat** (abstract; not yet written as a file).
- **Canon:** the first orbital structure. Small, light, low-tech. Occupied exclusively by robots, because a robot-only setting
  needs no breathable atmosphere, no food production and no sanitation. **Built about the mid-2300s** (per the Hana Jinn and
  Mallory Dufay character anchors), roughly 200 years before the 2564 Falkland Treaty, so it falls in the **First Interwar
  Period** and predates the arrival in Antarctica.
- **Developer ruling, 2026-10-11 (RL-1):** the station needs radiation shielding to the degree a human requires. See §4.

## 2. ULM frame

| Field | Declaration | Note |
|---|---|---|
| **Primary type, by era** | **Installation + Settlement (dual)**, proposed | Robots *live* aboard (Settlement), and it was built for a function (Installation). `01` §1.1 says a dual assignment is itself a finding. **Developer to confirm.** |
| **Modifiers** | **Orbital / extraplanetary** · **Enclosed**, in the sense of a *shielded volume only* | There is no pressurized envelope, so the usual Enclosed question ("what is the failure mode of the envelope?") becomes "what is the failure mode of the shield?" Flagged for `01` §1.2. |
| **Population band** | **not set** (range unknown) | Population is an open slot. **If the station holds 30 or fewer robots it is Band 1 (named individuals, no general population) and the general-population discipline inverts** (`01` §2.3). |
| **Status** | **Living** from its construction (mid-2300s, canon), in canon's First Interwar | Whether it later changed status (Growing, Declining, or absorbed by stage 2) is unwritten. |
| **Frame** | First Interwar (2083–2564). The Antarctic Acts do not apply. | The "Act 1 / Act 2" scheme is the Antarctic nation's timeline. A robot-only orbital community needs its own era notes. |

## 3. Inheritance (ULM `01` §5.1), as of the First Interwar

| Element | Class | Note |
|---|---|---|
| Physics, orbital mechanics, thermal and radiation environment | **Determined** | Fixed by the orbit. |
| Robot physiology and the robot Laws of Robotics | **Determined** | Universe-wide (`RB` §C.10). Several claims were written for Antarctic cold and must be re-derived for vacuum, radiation and microgravity. |
| Robot culture of this community | **Open** (a slot) | `Robot_Universals` seats identity in city and subnet structure. Here there is neither city nor subnet. Whether the Antarctic framework applies at all is open. |
| What the station *does* | **Originated** by the builders | Unknown (see §5). |

## 4. Invariants: G2, physical and environmental

All **[D]-free**: these hold for any robot community, in any LEO orbit, whatever their history.
**The orbit itself is an open slot (§8).** The numbers below depend on altitude and inclination.

**Environment** `[LEO §6]`
- **Heat leaves only by radiation.** A 300 K one-sided blackbody radiator sheds about **459 W/m²**, so radiator area scales with
  power. Radiators must avoid facing the Sun and the Earth.
- **Orbit about 93 min, about 36 min of darkness at 400 km.** Solar power needs storage and sees large thermal cycles. Arrays
  degrade **0.15–0.45 % per year** (measured at the ISS).
- **Radiation is a continuous dose plus bursts.** At the ISS about **0.2–0.5 mSv/day**, dose roughly **doubling between 360 and
  460 km**. The South Atlantic Anomaly is crossed several times a day. Outer electron belts reach the orbit at high latitude for
  about a fifth of each orbit. Large solar events can reach as much as 40 % of the orbit.
- **Electronics see cumulative dose plus single-event upsets.** An example LEO year is about **2 krad(Si)**, a polar year **6 krad(Si)**.
  Destructive latchup and burnout exist for any complex part.
- **Atomic oxygen erodes polymers** on forward-facing surfaces: fluence 1–2 × 10²¹ atoms/cm² per year on a ram surface.
- **Debris of about 1–10 cm is the main hazard** at ISS altitude. Shields stop about 1 cm and below. Tracked objects of 10 cm and
  larger can be avoided by maneuvering.
- **Drag is a continuous tax.** The ISS needs periodic reboost; its drag is 0.3–1.1 N. Altitude trades drag against dose, debris
  and light-time.
- **Round-trip signal delay** is milliseconds to a quarter second for ground and relay paths.

**The body in this environment** `[ROBOT §6]`
- **Electronics:** untested commercial parts fail somewhere between **under 1 krad and 20 krad or more**. A tested lot is plausibly
  good to 20–30 krad. Hardened parts are rated **100 krad to above 1 Mrad**. Hardened processors are far slower and more
  expensive.
- **Belt crossings add up.** A body that crosses an elliptical belt orbit 270 times behind 200 mil of aluminum absorbs about 20 krad.
  Shielding returns diminish beyond about 5 mm of aluminum.
- **Mechanisms in vacuum** need vapor-pressure-safe lubricants and heating or insulation. Fluid-lubricated precision gears lasted
  26–62 hours of walking-equivalent in the one test found. Long-duration machines fail mostly at wheels, joints and motors,
  and are fixed by replacement.
- **No propulsion from limbs.** A human-shaped machine in vacuum or microgravity can only move by contact with structure or by
  expelling mass.
- **Thermal:** a humanoid-size body sheds no more than about 1.0–1.35 kW by radiation. A bare body in cold shade loses about 703 W
  (D5 of the file), and thermal limits of working humanoids are published but do not cover orbit shade without added heat or
  insulation.

### The shielding ruling (RL-1), and what it means in physics

The developer's ruling is that a robot would still suit up for a spacewalk, **for radiation protection**, and that the earliest station
must be shielded as a human would require. Two points make that a consistent design rule:

1. **It is a statement about the gel brain, not about the body's electronics.** The research puts electronics tolerance in the
   **tens to hundreds of krad**. Converting units roughly, **1 krad = 10 Gy**, so 20 krad is about 200 Gy, well above the dose that
   is dangerous to a human. [Absorbed dose and dose equivalent are different quantities, so this is an order-of-magnitude comparison
   only.] The body's circuitry alone would tolerate far more than a human. The ruling therefore **sets the gel brain's tolerance
   near a human's**. Canon says nothing else about it. That is the developer's call and it is now made.
2. **The shield is a mass-per-area requirement.** Shield mass = areal density × shielded surface area. A **small** station minimizes
   the shielded surface, which is consistent with canon's "small, light" description. The areal density required is a function of
   **orbit, dwell time and dose budget**, none of which is fixed yet (§8).

**What the research does not yet say, and the class must not assume:**
- **How much radiation protection a spacesuit gives.** The LEO file has dose and shielding-mass findings, and I did not find a
  figure for suit-wall protection. Until it is researched, the class does not credit the suit with significant protection, and a
  robot's EVA dose is an open item.
- **The numeric dose budget** for "to the degree a human requires" (for example an agency career limit, or a general-public
  limit). The deferred list has NASA-STD-3001 and the crew-dose figures (NASA's own numbers found: 40–90 mSv and 72 mSv per six
  months; the "80/160 mSv" claim is unverified).
- **The large-habitat shield figures** in the LEO file (4.5 t/m² for a general-population dose, 10 t/m² Earth-equivalent) are for
  **large L5-type habitats** and do not transfer to a small LEO station, which sits below most of the belts.

## 5. Invariants: G3 function, and G5 network position

- **G3, function.** Canon: a *staging* station, first orbital structure. What it stages is **not stated in any file I have read**.
  The nearest inference [D]: it stages robot-led construction of later orbital structures (stage 3's wheels exist "to build
  further orbital infrastructure"). **Developer to confirm.**
- **G5, network.** What it needs from elsewhere, as relation:
  - **Everything it cannot make.** Stage 1 is robot-only and low-tech, so spares, propellant and power hardware come from Earth.
    `C-9` applies: no real habitat has run without resupply or spares (the ISS spares-to-system-mass ratio is 7.1 for one
    subsystem over 1,200 days).
  - **How material reached orbit.** Canon dates stage 1 to the mid-2300s and the Amundsen Tower's completion to about 2688.
    So the Tower did not lift stage 1, **unless an earlier lift system existed.** Open question (§8).
  - **Signal.** A relay path to the surface, with delay in milliseconds (above).

## 6. Real-world comparables (G7, mechanism only, `[RW]`)

The ISS as a long-running orbital structure with no breathable-atmosphere requirement for its *external* hardware; the
Hubble and similar free-flyers for thermal-cycling and degradation records. **Mechanism only, never a fact about the fiction.**
The `moon_lagrange_and_comparables.md` file holds the ISS maintenance-burden material; its crew-time shares are planning
figures, not measured fractions.

## 7. Candidate handwaves that touch this class

C-1 (shedding a working body's heat), C-2 (surviving shade without a heat source), C-4 (years without servicing joints), C-5
(partly answered by RL-1), C-7 (charging cold cells), C-9 (no resupply), C-24 (dust, if any), C-25 (a radiator-free heat sink)
and C-32 (answered: a robot is **not** radiation-immune). The class declares **none accepted**. Each instance must
state which it relies on.

## 8. Open slots

| Slot | Binds from | Status | Until then, a pass writes |
|---|---|---|---|
| **Orbit** (altitude, inclination) | developer / canon | OPEN | a null; all dose, drag and light-time figures stay conditional on it |
| **Station size and robot population** | developer | OPEN | a null; band is a range, and Band 1 inverts the discipline |
| **Dwell time** (permanent residence vs rotation) | developer | OPEN | a null; the shield areal density depends on it |
| **Dose budget** for "to the degree a human requires" | research + developer | PROVISIONAL (RL-1) | the budget is stated as a sourced agency limit once chosen |
| **Gel-brain tolerance** | developer | BOUND by RL-1 at human-equivalent | no figure beyond RL-1 |
| **Composition of the robot community** (who built them, from where) | Package 2 (origin data) | OPEN | a null; origin is **Upper Earth** in canon and the Antarctic subnets do not apply |
| **Founding event** | developer | OPEN | a null |
| **Local culture** of an orbital robot community | developer / Package 2 | OPEN | a null |
| **What the station stages** | developer | OPEN (inference in §5) | a null with the inference marked [D] |
| **How it reached orbit** | developer | OPEN | a null |
| **Name** | developer | OPEN | a null |

## 9. Registered assumptions

- **PA-S1.** LEO ("low Earth orbit, primarily", per the Orbital-Infrastructure README). *Overturned by:* the orbit slot.
- **PA-S2.** A robot's radiation tolerance, for shielding, equals a human's (RL-1). *Overturned by:* a developer correction.
- **PA-S3.** The shield is passive mass. No plasma or magnetic shield (SP-413 calls the plasma core "speculative").
- **PA-S4.** No resupply-free operation (C-9).

## 10. Requests

- **R-S1.** The orbit (altitude, inclination), or the instruction to leave it open.
- **R-S2.** The number of robots aboard, or the instruction to leave it open.
- **R-S3.** What "radiation-shielded to the degree a human requires" means numerically: an agency crew limit, a general-public limit, or a
  dose per year.
- **R-S4.** A researched figure for **suit-wall radiation protection**, so a robot's EVA dose can be bounded.
- **R-S5.** How material reached orbit before the Tower (if the Tower did not lift stage 1).
- **R-S6.** What the station stages.

## 11. Instance obligations (which ULM phases apply to a pass on one of these)

| Phase | Applies? | Note |
|---|---|---|
| 1, Spine | yes | G2 is overwhelmingly the generator; the capability frame needs a fresh reading for a no-atmosphere setting |
| 2, Composition and arrival | yes | Robots only; arrival means *coming online* (`DR-11`) and being brought aboard |
| 3, Surface and texture | **largely meaningless** | No climate, weather or atmosphere. Replace with the radiation, thermal and light environment of §4. |
| 4, Ordinary life | yes | Charging, rest, leisure (robot leisure is canon), the stop |
| 5, Relation | yes | Earth, ground launch, other stations as relation only |
| 6, Meaning | yes | "No faith sited" is a result; robot religions are an open roster |
| 7, Order | yes | Who decides, with Laws of Robotics and no living human |
| 8, Making | yes | Cuisine reduces to siligel and coolant supply; clothing and EVA suits |
| 9, Populations | yes | **Band 1–2: named individuals; the general-population discipline inverts** |
| 10, Catalog | yes | Physical referents only |

## 12. What this draft tested in the template

- **Worked:** the invariants/slots split. Almost all of the class is early-bound physics, and almost every open item is one line in §8.
- **Needed a change to the template:** field 2 asks for an *orbit* as a slot, because every physical figure depends on it. The template had
  no place for a slot that parameterizes the invariants. Add a "parameters" row.
- **Raised for `01`:** "Enclosed" does not fit a shielded-but-unpressurized volume (§2).
- **Exposed an unwritten canon fact:** how stage 1 reached orbit before the Tower.
