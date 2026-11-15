STATUS: SET UP 2026-11-15, NOT STARTED. Waiting for the author's "go", which depends on the weekly allotment.

# Cascadia Stage 1 run (waves 2–4): start here

**What this run does:** DCI Stage 1, the eleven lineage profiles, for each of Cascadia's eleven units. That is "Session A" of the road to Aries in `../Targets/North America/Cascadia/PROGRESS TRACKER.md`. Claude does the research: Hermes, Qwen and Strata were retired 2026-11-15, and their output is archived and never cited. The briefs were written 2026-11-03 and updated 2026-11-10. They are unchanged except for the overrides below.

**Budget:**
- About 45 web searches per unit, about 495 in all.
- The session cap is 1,000, shared by every agent, so the whole run fits in one fresh session if nothing else there searches heavily.
- It uses a lot of the weekly allotment; that's why the author starts it.

**How it runs** (the 2026-11-11 lesson: never rely on timers or the main session to move from step to step):
1. **One background run agent** launches each wave's research agents together, waits for them, checks their STATUS lines, logs, and goes on to the next wave.
2. **The main session** then runs Stage 7 verification (`<DM>/Templates/T7_Verification_Checklist.md`) on every output before it's marked VERIFIED.

`<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`
`<RESULTS>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation`

## Jobs

| Wave | Unit | Brief (in this folder) | Output folder (`<RESULTS>/Units/…`) | Agent | Status | Verified |
|---|---|---|---|---|---|---|
| 2 | S1 Left Coast (+ S1a) | `Cascadia_Left-Coast_S1.md` | `Left Coast/` | | not started | |
| 2 | S2 British Columbia coast | `Cascadia_British-Columbia-coast_S1.md` | `British Columbia coast/` | | not started | |
| 2 | S3 Far West | `Cascadia_Far-West_S1.md` | `Far West/` | | not started | |
| 3 | S4 El Norte | `Cascadia_El-Norte_S1.md` | `El Norte/` | | not started | |
| 3 | S5 Sudcalifornia | `Cascadia_Sudcalifornia_S1.md` | `Sudcalifornia/` | | not started | |
| 3 | I1 Northwest Coast peoples | `Cascadia_Northwest-Coast-peoples_S1.md` | `Northwest Coast peoples/` | | not started | |
| 3 | I2 Plateau peoples | `Cascadia_Plateau-peoples_S1.md` | `Plateau peoples/` | | not started | |
| 4 | I3 California peoples | `Cascadia_California-peoples_S1.md` | `California peoples/` | | not started | |
| 4 | I4 Yuman peoples | `Cascadia_Yuman-peoples_S1.md` | `Yuman peoples/` | | not started | |
| 4 | I5 Great Basin peoples | `Cascadia_Great-Basin-peoples_S1.md` | `Great Basin peoples/` | | not started | |
| 4 | I6 Subarctic Dene peoples | `Cascadia_Subarctic-Dene-peoples_S1.md` | `Subarctic Dene peoples/` | | not started | |

Parked, not part of this run: L6 and L7, the legal profiles. Law lives only in Libra and Capricorn.

## Overrides for every brief
- **Dates:** where a brief says `done 2026-11-03`, write the date you actually finish.
- **Never** read, cite or build on anything from Hermes, Qwen or Strata (`worldbuilding/Hermes_research/` findings, now archived). If a source trail leads there, drop it.
- The standing rules in `<DM>/RUNBOOK.md` apply in full:
  - American English.
  - Native, Indigenous or Aboriginal, never "Indian" (and First Nations, Inuit or Métis in Canada).
  - No South Asian works as sources.
  - No law outside Libra and Capricorn.
  - Short quotations only.

## The run-agent prompt (launch this as one background agent)

> You are the run agent for DCI Stage 1, Cascadia waves 2–4. You do not research yourself; you launch research agents, check their work, and keep the log.
> 1. Read `<RESULTS>/_dispatch/STAGE1_RUN_PROGRESS.md` (this file) and `<DM>/_dispatch/RESUME.md`.
> 2. For the first wave with a unit not marked done, launch one research agent per unfinished unit in that wave, all at once, each with this prompt: "Read and follow the brief `<RESULTS>/_dispatch/<brief>` exactly, with the overrides in the section 'Overrides for every brief' of `<RESULTS>/_dispatch/STAGE1_RUN_PROGRESS.md`. If the output folder already has files, read them: keep every file whose first line says `STATUS: done`, and continue from the first one that isn't. When finished, report the files written, the searches used, and any question for the author."
> 3. Record each agent's ID in the Jobs table. When an agent finishes, check its output: the unit README's first line, and the first line of each of the 11 profile files (`grep -m1 "^STATUS:"`). Mark the unit `done, not verified` only if all twelve say done. Otherwise mark it `stopped at profile N` and relaunch it once with the same prompt.
> 4. After each wave, append a dated entry to the Run log below: the units done, searches used (from the agents' reports), and the questions for the author, copied word for word. Then go on to the next wave.
> 5. If the session's search cap runs out, stop launching. Mark the remaining units `waiting for a fresh session`, log it, and end.
> 6. When all eleven are done or waiting, set this file's first line to `STATUS: RUN FINISHED <date>; verification pending` and end with a short report.
> Touch no files except this progress file. The research agents write only to their own unit folders.

## Resuming after a cutoff
- **Same session, run agent still known:** send it a message to continue from the Jobs table.
- **Otherwise:** launch a new run agent with the prompt above. It picks up from the table and from the STATUS lines in the unit folders.
- **To check by hand:** `grep -rn -m1 "^STATUS:" "<RESULTS>/Units"`.

## After the run (main session)
1. Stage 7 verification per unit; mark each `VERIFIED <date>` in the Verified column and in each file's STATUS line.
2. Update `../Targets/North America/Cascadia/PROGRESS TRACKER.md` (the Units table and the Stage 1 row) and `../MASTER TRACKER.md`.
3. Bring the agents' questions to the author.
4. Next: Session B (Stages 2 and 3), then Session C (Aries).

## Run log
- 2026-11-15: set up. Not started; the author says "go".
