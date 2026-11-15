STATUS: CASCADIA SIGNS 1-3 DONE 2026-11-15 (Aries, Taurus, Gemini: 32 sheets, per-concept agents). Next: Cascadia Cancer. Open: cost/job shape and the pace (author has said three signs a day).

# Springboard scouting: start here

**What this is:** the author's request of 2026-11-15: go through every represented nation one at a time, each sign one at a time, with one subagent per concept, and write **springboard sheets**: surface data and "jumping-off points" for where to begin looking. **It is not research**; real research is a later task (about the next 6 to 10 months). The method is `<DM>/Shared/Springboard_Scouting.md`; the agent brief is `<DM>/_dispatch/SPRINGBOARD_BRIEF.md`; the sheet template is `<DM>/Templates/T_Springboard.md`.

`<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`
`<RESULTS>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation`

**Scale:** 84 nations × 130 sheets (118 concepts + 12 sign domains) = **10,920 sheets**. A sheet is about 250 to 450 words, written from the agent's own knowledge, no web.

**Output:** `<RESULTS>/Targets/<region>/<nation>/Springboards/NN - <Sign>/` (`00 - Domain and folkways.md`, `NN - <Concept>.md`).

**Status grid (read from the files):** `python3 -I "<DM>/_dispatch/springboard_status.py"` (all nations with any sheet) or `... springboard_status.py <Nation>` (per sign, with counts of done and in progress).

## Order
- **Nations, one at a time, in the master tracker's order:** Cascadia, Alaska, Sonora (the first novels), then Korea, Sinian Federation, Japan, and so on down the table.
- **Within a nation, signs one at a time, Aries to Pisces.** Within a sign, the domain and all concepts run in parallel (10 to 13 agents).

## Per-sign procedure (the run agent, or the main session, does this)
1. `python3 -I "<DM>/_dispatch/springboard_status.py" <Nation>` to find the first sign not complete.
2. List its jobs: `python3 -I "<DM>/_dispatch/concept_block.py" list <sign number>` (line 0 is the domain).
3. For each job not already `STATUS: done`, launch one agent with: *"Read and follow the brief `<DM>/_dispatch/SPRINGBOARD_BRIEF.md` exactly. Your job: NATION = <Nation>. SIGN = <n>, <Sign>. CONCEPT = <k> (<name>). Scouting only: no web, no research. Reply with one line."* A file whose first line says `in progress` is relaunched with the same prompt (the brief says to overwrite it).
4. When all return, re-run the status script. If any sheet is missing or not `done`, relaunch just those once.
5. Spot-check two sheets from the sign against the rules (below), then move on to the next sign.

## Pilot result (2026-11-15, Cascadia × Aries, 11 sheets)
- **Quality: good.** Real, well-known sources, everything marked *check*, no findings, standing rules mostly held (South Asian pointers set aside under "held for review"). Fixed: the brief's folder lookup (it missed most nations), a South Asian community named under "who to compare" (now forbidden outside the held line), and the length target (sheets run 700 to 900 words counting markup; the spec now says so).
- **Cost: about 57,000 tokens per agent, about 640,000 per nation × sign** (11 agents), because every agent re-reads the spec, brief and avenue block. At that rate the full 10,920 sheets would be about 640 million tokens. A cheaper shape (one agent per nation × sign writing all 10 to 12 sheets) would be about a tenth of that. **The author decides before anything beyond the pilot runs.**

## Spot-check rules (what a bad sheet looks like)
- **Findings** (statements about how the culture understands the concept): rewrite as a search term or cut.
- **Invented names:** a specific title, author, URL, statistic or institution that does not look real. Replace with the source *type* and a query.
- **Unmarked names:** anything named without *check*.
- **Standing-rule breaks:** "Indian" (other than a published title), South Asian pointers outside `held_for_review`, law outside Libra and Capricorn, national stereotypes, zodiac terms as pointers.
- **Too long or padded:** over about 450 words (650 for a domain).

## Resuming after a cutoff
The files are the truth. Run the status script, find the first nation with an incomplete sign, and continue from step 1. No timer or session state is needed.

## Run agent prompt (for an unattended run; launch as ONE background agent, and chain every step inside it)
> You are the run agent for DCI springboard scouting. Read `<RESULTS>/_dispatch/SPRINGBOARD_PROGRESS.md` (this file), then follow "Per-sign procedure" for the nation(s) the author named: <NATIONS>. Work sign by sign, Aries to Pisces, launching each sign's agents together, waiting for them, checking, and logging a line in the Run log for each sign. Never skip a sign; never launch the next nation until the current one has all twelve signs `done`. Touch only the Springboards folders and this file's Run log. If the usage window cuts you off, the status script resumes you. Stop after <NATIONS> and report: sheets done, sheets relaunched, rule breaks found, anything the author should know.

## Run log
- 2026-11-15: method, brief, template, extractor and status script written. Pilot (Cascadia × Aries, 11 sheets) launched from the main session.
- 2026-11-15 (later): Cascadia × Taurus (11 sheets) and × Gemini (10 sheets) run per the author's "next two signs, same depth". 32 sheets in all so far (Aries 11, Taurus 11, Gemini 10). About 60,000 tokens per agent. Rule scan: no breaks outside published titles; the five Aries lines that named Punjabi communities were rewritten category-only. Sheet length has crept up (Aries about 750, Taurus about 950 words by wc, Gemini about 870, Information 1,137); the brief's target is 450 to 750.
- The author's pace: three signs a day. That is about 11 months for 1,008 nation-signs; four a day is about 8.3 months; about 5.6 a day is 6 months.
