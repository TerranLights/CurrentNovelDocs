STATUS: CASCADIA COMPLETE 2026-11-15 (all 12 signs, 130 sheets; per-concept agents; nation-level). Overnight test day done: the full report is `reports/2026-11-15_Cascadia_test_day_report.md`. Next nation: Alaska (author to choose shape and pace).

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


## Overnight test day: Cascadia, signs 4 to 12 (author's go, 2026-11-15; weekly allotment at 2% when started)
**Goal:** finish Cascadia (Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces), per-concept agents, nation-level, scouting only. The author reads a full report in the morning: `reports/2026-11-15_Cascadia_test_day_report.md`. The point of the day is also to measure the real cost of a nation-day (about 5.8 million tokens expected: 9 signs, about 97 agents).

**Run agent prompt (saved so a cutoff loses nothing):**
> You are the run agent for DCI springboard scouting. Your nation is **Cascadia**, signs **4 (Cancer) to 12 (Pisces)**; signs 1-3 are done. Read `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation/_dispatch/SPRINGBOARD_PROGRESS.md` (this file) and the method `<DM>/Shared/Springboard_Scouting.md`. `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`. Chain everything yourself; no one is watching.
> **For each sign, in order, one at a time:**
> 1. List its jobs: `python3 -I "<DM>/_dispatch/concept_block.py" list <n>` (line 0 is the domain).
> 2. Launch one sub-agent per job (domain plus every concept) **all in one message, in the background**, each with exactly this prompt (fill the braces): *"Read and follow the brief `<DM>/_dispatch/SPRINGBOARD_BRIEF.md` exactly. Your job: NATION = Cascadia. SIGN = {n}, {Sign}. CONCEPT = {k} ({name}). Scouting only: no web, no research. Aim for about 750 words counting table markup; never over 1,000. Reply with one line."* If you cannot launch sub-agents, write the sheets yourself one at a time, following the brief exactly.
> 3. Wait for all to finish. Then run `python3 -I "<DM>/_dispatch/springboard_status.py" Cascadia` and `python3 -I "<DM>/_dispatch/springboard_qa.py" Cascadia <n>`.
> 4. Any sheet missing, not `STATUS: done`, or flagged by the QA: relaunch that one job once, adding the problem to its prompt. If it still fails, fix it by hand with the smallest edit (a South Asian line becomes the category-only held line; a URL is removed; a finding sentence becomes a search term or is cut). Log what you did.
> 5. Append one line per sign to the Run log in this file: the sheets done, agents launched, relaunches, QA problems found and how they were fixed, the average and longest word count (`wc -w`).
> 6. Only then start the next sign. Never skip a sign.
> **When all nine are done:** run the QA for all of Cascadia; then write the morning report to `<RESULTS>/_dispatch/reports/2026-11-15_Cascadia_test_day_report.md` (RESULTS = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation`): per-sign table (sheets, agents launched, relaunches, QA problems, avg and max words); totals (sheets, agents, wall-clock from your first launch to your last); every rule break and how fixed; anything odd (a sheet that read like research, an invented-looking name, a thin concept); what you would change in the brief; any question for the author. Touch only the Springboards folders for Cascadia, this file's Run log, and the report. If the usage window cuts you off, the status script resumes whoever continues.

## Resuming after a cutoff
The files are the truth. Run the status script, find the first nation with an incomplete sign, and continue from step 1. No timer or session state is needed.

## Run agent prompt (for an unattended run; launch as ONE background agent, and chain every step inside it)
> You are the run agent for DCI springboard scouting. Read `<RESULTS>/_dispatch/SPRINGBOARD_PROGRESS.md` (this file), then follow "Per-sign procedure" for the nation(s) the author named: <NATIONS>. Work sign by sign, Aries to Pisces, launching each sign's agents together, waiting for them, checking, and logging a line in the Run log for each sign. Never skip a sign; never launch the next nation until the current one has all twelve signs `done`. Touch only the Springboards folders and this file's Run log. If the usage window cuts you off, the status script resumes you. Stop after <NATIONS> and report: sheets done, sheets relaunched, rule breaks found, anything the author should know.

## Run log
- 2026-11-15: method, brief, template, extractor and status script written. Pilot (Cascadia × Aries, 11 sheets) launched from the main session.
- 2026-11-15 (later): Cascadia × Taurus (11 sheets) and × Gemini (10 sheets) run per the author's "next two signs, same depth". 32 sheets in all so far (Aries 11, Taurus 11, Gemini 10). About 60,000 tokens per agent. Rule scan: no breaks outside published titles; the five Aries lines that named Punjabi communities were rewritten category-only. Sheet length has crept up (Aries about 750, Taurus about 950 words by wc, Gemini about 870, Information 1,137); the brief's target is 450 to 750.
- The author's pace: three signs a day. That is about 11 months for 1,008 nation-signs; four a day is about 8.3 months; about 5.6 a day is 6 months.
- 2026-11-15 (overnight run) Cascadia x Cancer: 10/10 sheets done, 10 agents launched, 0 relaunches, QA 0 problems; avg 846 words, longest 919 (Shelter). Launched about 02:11; all returned within about 50 seconds.
- 2026-11-15 (overnight run) Cascadia x Leo: 13/13 sheets done, 13 agents, 0 relaunches. QA flagged 3 'Indian' lines: two are real published titles (Holm, Northwest Coast Indian Art; Culin, Games of the North American Indians) so QA false positives, left as is; one organization name (Union of BC Indian Chiefs) rewritten by hand to a generic description plus the search term UBCIC. Avg 833 words, longest 878 (Domain). Note: first status/wc read caught two sheets mid-rewrite (1,067 and 1,018 words); final versions 860 and 799.
- 2026-11-15 (overnight run) Cascadia x Virgo: 10/10 sheets done, 10 agents, 0 relaunches. QA flagged 1 'Indian' line (Work): three real published titles (Makuk, Authentic Indians, Indians at Work), QA false positive, left as is. Avg 833 words, longest 932 (Work). Three agents trimmed their own first drafts that ran over 1,000.
- 2026-11-15 (overnight run) Cascadia x Libra: 11/11 sheets done, 11 agents, 0 relaunches. QA flagged 1 'Indian' line (Balance): the published title Holm, Northwest Coast Indian Art, QA false positive (the allowlist lacks it), left as is. Avg 827 words, longest 923 (Diplomacy).
- 2026-11-15 (overnight run) Cascadia x Scorpio: 11/11 sheets done, 11 agents, 0 relaunches, QA 0 problems. Avg 855 words, longest 947 (Domain).
- 2026-11-15 (overnight run) Cascadia x Sagittarius: 11/11 sheets done, 11 agents, 0 relaunches, QA 0 problems. Avg 836 words, longest 887 (Domain).
- 2026-11-15 (overnight run) Cascadia x Capricorn: 10/10 sheets done, 10 agents, 0 relaunches. QA flagged 2 'Indian' lines in Discipline: one descriptive phrase for a federal report rewritten by hand to 'federal boarding school investigation reports'; one is the institutions' own names (Chemawa, Sherman Indian schools), QA false positive, left as is. Avg 834 words, longest 934 (Domain).
- 2026-11-15 (overnight run) Cascadia x Aquarius: 10/10 sheets done, 10 agents, 0 relaunches, QA 0 problems. Avg 858 words, longest 925 (Domain).
- 2026-11-15 (overnight run) Cascadia x Pisces: 12/12 sheets done, 12 agents, 0 relaunches. QA flagged 1 zodiac word (Domain: 'astrology items' as a survey topic), rewritten by hand to 'New Age belief items'. Avg 873 words, longest 999 (Surrender, just under the 1,000 cap).
- 2026-11-15 (morning check, main session): status 130/130; QA 0 problems after the allowlist and header fixes; independent sample audit of Scorpio Death, Capricorn Law and Sagittarius Faith found only real, well-known sources, all marked *check*, no findings. Applied the report's bug fixes (template header, QA allowlist, checkpoint order, Libra/Capricorn law line). Length and job-shape questions are left to the author.
