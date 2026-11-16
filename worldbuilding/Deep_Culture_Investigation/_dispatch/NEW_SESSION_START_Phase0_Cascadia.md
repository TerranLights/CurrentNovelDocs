STATUS: READY 2026-11-16, not started. Written for a new Claude session with a fresh web-search quota. The author pastes the prompt in section 1 to start it.

# Phase 0, step C1a: Cascadia depth tests (start here in a new session)

**Run this from the CurrentNovelDocs folder** (`/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs`) so the project memory loads. `<RESULTS>` = `worldbuilding/Deep_Culture_Investigation`; `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`.

**Do not touch the springboard survey** (`Targets/*/*/Springboards/`, the Run log and cost ledger in `_dispatch/SPRINGBOARD_PROGRESS.md`): another session runs it (Day 2 starts 05:02 on 2026-11-17, three more days follow). This session only reads those sheets. Web research is allowed here; the springboard runs use none.

## 1. The prompt to paste into the new session

> This is the start of the DCI full research, Phase 0 (calibrating the method on Cascadia). Read, in this order: `worldbuilding/Deep_Culture_Investigation/RESEARCH_SCHEDULE (draft).md` (the order, Phase 0, the depth and accuracy mechanisms, the limits protocol), then `worldbuilding/Deep_Culture_Investigation/_dispatch/NEW_SESSION_START_Phase0_Cascadia.md` (this plan), then `_dispatch/STAGE1_RUN_PROGRESS.md`, `<DM>/RUNBOOK.md` (especially "Research from the springboard") and `<DM>/_dispatch/RESUME.md`. Then do step C1a as laid out in section 2 of the plan. Priorities from the author: the highest-quality, most-accurate and deepest research possible; token cost is not a concern; depth never gives way to a limit. Follow the limits protocol: at about 1,000 searches this session, or at the weekly allotment, stop at a clean point, log the full research progress, tell me, and I will start a new session or wait for the reset; then pick up exactly from the logged state. Report to me when C1a is done, and do not go on to the full Stage 1 run until I say so.

## 2. The plan for C1a (proposed in `RESEARCH_SCHEDULE (draft).md`; the author may change it)
**Purpose:** find out how deep the research actually goes and what makes it go deeper, on a small slice of Cascadia, before the full Stage 1 run. Nothing here is committed to the final Cascadia output until the author accepts the method.

1. **Set up the logs first.** Create `<RESULTS>/_dispatch/PHASE0_LOG.md` (the session's running log: date and time, what was done, searches used so far this session, files written, the next step). Every research job keeps its own `research_log.md` (search ledger: each query, its language, what it returned, and *new finding / confirms / dead end*, plus any leads spawned) and `leads.md` (lead queue with hop depth and status; parked leads go to `leads_parked.md`). Update the logs as work goes, not at the end. Keep a running search count in `PHASE0_LOG.md`.
2. **Pick the test jobs.** Three Stage 1 jobs from `_dispatch/Cascadia_*_S1.md`, as a spread: one settler unit with rich data (proposed: Far West), one Indigenous-peoples unit (proposed: Plateau peoples) and one small or thin one (proposed: Subarctic Dene peoples). The author may swap them. Use the existing briefs, the overrides in `STAGE1_RUN_PROGRESS.md` and the research-from-the-springboard rules. Never read, cite or build on Hermes, Qwen or Strata output.
3. **Run the first test job to saturation with the depth mechanisms** (mechanisms 1 to 6, 10 of the draft): the stop test is evidence-based (the lead queue closed or parked with reasons, and the last 15 searches found nothing of substance), not a search budget; a blind search plan is written before reading the springboard sheet; a coverage grid is built from the concept and unit; citation-chasing and native-language and minority-language searches are used. Write findings to files as the work goes.
4. **Dose-response curve:** from the first job's ledger, plot new findings per search against search number (cumulative at 15, 30, 60, 120 and the end). This is read from one run, not four runs. Note where the curve flattens.
5. **Blind second agent** (mechanism 8): a second agent researches the same job blind (no access to the first agent's output), then compare the two source sets and findings: what share did each find that the other missed?
6. **Gap reviewer** (mechanism 7): an agent that did not do the research reads the output, the grid and the ledger, plays a skeptical specialist in that culture, and lists what is missing; run the list as new searches and count how many yield real findings.
7. **Repeat steps 3 to 6 on the other two test jobs only as far as needed** to see whether the pattern holds (the settler, Indigenous and thin cases may differ). Stop and report earlier if the first job already shows a clear result.
8. **Verification check** (Stage 7, `<DM>/Templates/T7_Verification_Checklist.md`): a different agent re-finds a sample of claims at their sources and compares. Record what fraction was confirmed, corrected or unsupported.
9. **Write the audit report** `<RESULTS>/_dispatch/reports/<date>_Phase0_C1a_report.md`: per job the searches, the curve, the miss rate against the second agent, the gap reviewer's yield, springboard use (pointers checked, leads beyond the sheet), verification results, source spread (recurring sources, native-language and minority sources), and the time. End with recommended settings (the floor, the stop test, which mechanisms earned their keep) and the questions for the author.
10. **Stop and report to the author.** The full Stage 1 run (the other eight units), Stages 2 and 3, and Aries wait for the author's acceptance of the calibration.

## 3. Rules that apply to everything in this session
- **Accuracy and depth first; token cost is not a concern.** Two independent sources for any claim that matters (mark single-source claims); every finding carries its source, date and a confidence note; nothing from memory enters a result unmarked; contradictions are kept with both sides; quotations and figures re-read at the source.
- **Standing rules** (RUNBOOK): American English; Native, Indigenous or Aboriginal and never "Indian" in our own words (First Nations, Inuit, Métis in Canada); no South Asian works as sources; no law research outside Libra and Capricorn; short quotations only. DCI is a cultural investigation, not an investigation of laws.
- **Hours:** research may run at any hour; derivation and worldbuilding of the Federation's successor nations is 05:00 to 14:59 only (not part of this step).
- **Limits protocol:** at the search cap (about 1,000 per session) or the weekly allotment (resets Saturday 23:00), stop at a clean point, log the full progress in `PHASE0_LOG.md` (every job's status, ledgers and queues current, the next step, the files touched), tell the author in plain words which limit was hit, and wait. The next session reads `PHASE0_LOG.md` and the STATUS lines and resumes from there, never restarting a job.
- **Commit and push only on the author's word**, naming explicit paths (never sweeping unrelated ULM or Symbolism drafts). End commit messages with `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.

## 4. Where the outputs go
- Unit research: `<RESULTS>/Units/<unit>/01 - Lineage/` (output files with `STATUS:` first lines; the unit README).
- Ledgers and queues: beside each job's output in its unit folder (`research_log.md`, `leads.md`, `leads_parked.md`).
- Session log: `<RESULTS>/_dispatch/PHASE0_LOG.md`. Audit report: `<RESULTS>/_dispatch/reports/`.
- The master and Cascadia trackers (`MASTER TRACKER.md`, `Targets/North America/Cascadia/PROGRESS TRACKER.md`) are updated at the end of the session, not mid-run.

## 5. Run log (append)
- 2026-11-16: written; not started.
