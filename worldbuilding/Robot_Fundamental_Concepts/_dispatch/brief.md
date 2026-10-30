# Brief: notes from the GDD's zodiac documentation (2026-10-30)

## The project
The author is building a system of **fundamental robot concepts** (the robot concept of justice, crime, trust, care, honor, duty and so on).
- Its starting frame is the zodiac's twelve signs, treated as twelve **meta-categories of human understanding**: areas of human life, psychology and behavior.
- **It is not astrology and not a robot zodiac.** The signs are only a ready-made set of categories.
- Each meta-category has a human-understanding layer (research) and a robot-understanding layer (developed later with the author).

**This pass fills the human-understanding layer from one source set:** the zodiac documentation already written in the Inner Tepenia GDD.
- Make notes on **every topic in that documentation that bears on the meta-category's area of human life.**
- Write in our own words, and cite each point.

## Hard limits
- **Research only.**
  - Do not write any robot understanding or robot concepts.
  - Do not propose anything for the author's world.
  - Do not touch layer `2 - Robot understanding (development)/`.
- **Leave out the Concordia design material.** The GDD files were written to design Concordia's districts. Skip or strip everything that is district application: design hooks, district behavior, socialization of newcomers into a district, district names, quest material.
  - Keep what the documentation says about the **sign and its area of human life**.
- **The zodiac is never treated as true or in-world.** Report it as human tradition and belief: "astrology associates Libra with ...", "Martin reads the seventh house as ...".
- **This repo is public.** The GDD files quote copyrighted astrology books.
  - Paraphrase.
  - Use at most three short quotations per file, each a phrase or one sentence, and only where the exact wording matters.
  - Tierney's book is an OCR'd scan; never quote it.
- **Write only your assigned files.** Run no git commands that change anything. Use American English and plain language. Mark uncertainty with ⚠️.

## The sources (read-only)
GDD root: `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/`
- **`Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/`**:
  - `00_Method_and_Sources.md`: read it first, for the corpus and its caveats;
  - one file per sign (`01_Aries.md` ... `12_Pisces.md`);
  - cross-cutting files: `A_Elements`, `B_Modalities`, `C_Polarity`, `D_Aspect_Geometry`, `E_Decans`, `F_Rulerships`, `G_Correspondences`;
  - `13_Ophiuchus_Hub.md` and `99_Application_to_Districts.md`.
- **`Reference/Real-World/Zodiac_Signs_Full_Attributes.md`:** positive and negative attributes per sign.
- **`Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md`:** a condensed table.
- **A further source,** used only by the cross-cutting agent: `Reference/Real-World/Jung_Extractions/aion_Extraction_Part0{1,2,3}_of_03.md` (the zodiac passages only).

**Citing:**
- Cite the GDD file and section, for example (Substrate `07_Libra.md` §13) or (Full Attributes, Libra).
- Where the GDD file names the book it took a point from, add it: (Substrate `07_Libra.md` §13, from Snodgrass).

## Output for a SIGN agent
Folder: `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Robot_Fundamental_Concepts/01 - The twelve meta-categories/<NN - Sign (label)>/1 - Human understanding (research)/`

### 1. Create `Notes - GDD zodiac documentation.md`
- The first line is `STATUS: IN PROGRESS (next: <section>)`. Update it as you go, and set it to `STATUS: COMPLETE` at the end.
- **Header:**
  - the title `# <Sign>: notes from the GDD's zodiac documentation`;
  - a "Sources read" list (the files, and for the cross-cutting files, which sections);
  - the line: "Research notes, 2026-10-30. What the GDD's zodiac documentation says about this area of human life, in our own words. Not robot understanding; not Concordia design."
- **Sections.** Use these; drop a section only if the documentation has nothing for it, and say so under Gaps:
  1. **Areas of life:** the domains astrology gives this sign and its natural house, as fully as the documentation allows.
  2. **Core meaning:** the archetype, the driving motive and the core need.
  3. **The area at its best:** light expressions, virtues and positive attributes.
  4. **The area gone wrong:** shadow, vices, failure modes and negative attributes. This is often the richest material; be thorough.
  5. **Behavior under pressure and over time:** how the sign is said to act under stress, in conflict, when secure, and as it matures. Keep only what describes people, not districts.
  6. **Myth, history and cultural associations:** the myths, figures, history and symbols behind the sign, and what each says about the area.
  7. **Structure:**
     - element, modality and polarity;
     - **the opposite sign and the axis the pair forms** (what the two ends of the axis are);
     - ruling planet(s) and what the planet means here;
     - squares and trines (which areas this one conflicts with or supports, and why).
     - Take these from the cross-cutting files' sections on your sign.
  8. **Decans:** the sub-themes the documentation gives within the sign, as sub-themes of the area. Leave out neighborhood texture.
  9. **Correspondences:** colors, stones, plants and so on. Brief, and only what the documentation gives. **No body-part correspondences** (which organs a sign rules, facial divisions, or the illnesses tied to them): the author ruled they can't serve as meta-categories of understanding. The body as an area of life or behavior stays.
  10. **Topics in this area:** a bulleted list of every distinct topic of human life that this material shows belongs to the meta-category. Give each a one-line gloss and a citation. **This list is the main deliverable;** make it complete.
  11. **Where the author's named concepts appear:** for each of justice, crime, trust, care, honor and duty, say what this material says that bears on it, or "nothing in this material."
  12. **Gaps:** what the documentation does not cover about this area (for example, thin material on the house), and any disagreements between its sources.

### 2. Update that folder's `README.md`
- Set its STATUS line to `STATUS: IN PROGRESS (notes from the GDD zodiac documentation done 2026-10-30)`.
- Under "## Sources added", replace the line that begins "None yet." with a bullet naming your notes file and the GDD files it draws on. Keep the explanation sentence after it.

## Output for the CROSS-CUTTING agent
1. **`01 - The twelve meta-categories/00 - Cross-cutting notes (GDD zodiac documentation).md`**, with a STATUS line as above. It covers how the documentation organizes the twelve as a system:
   - **Elements:** four families of areas, and what each family shares.
   - **Modalities:** three modes of approach.
   - **Polarity:** the six axes of opposite signs, and what each axis pairs.
   - **Aspect geometry:** which areas clash and which support each other, and why.
   - **Decans** as a system.
   - **Rulerships:** the planets as drives that cut across areas.
   - **Correspondences** as a system, without body-part correspondences (see sign section 9).
   - **The astrological ages** and any other zodiac material in Jung's *Aion* extraction, and which signs each part touches.
   - **The corpus's caveats** from `00_Method_and_Sources.md`.
   - **Topics that cut across several meta-categories:** a list.
   - **Where the author's named concepts appear across the system.**
   - **Gaps.**
2. **`03 - Beyond the twelve/Notes - Ophiuchus and the Hub (GDD zodiac documentation).md`**, with a STATUS line. It covers:
   - what `13_Ophiuchus_Hub.md` says about Ophiuchus as a sign;
   - anything the documentation says that bears on **neutrality as a phenomenon** (not getting involved, not taking sides). The author is weighing it as a candidate meta-category.
   - Keep out the Hub's Concordia design.

## Resuming
- Create each file early and update its STATUS line as you go.
- If you are resumed, or are a replacement agent, read your files' STATUS lines and continue from there. Never restart a completed file.

## When done, reply with
- your files and their STATUS;
- the five most important topics you found for each meta-category you covered;
- anything in the documentation that didn't fit the template;
- gaps a later source should fill.
