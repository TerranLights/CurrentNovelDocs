# Resume protocol for the soil and food research agents

**Written 2026-10-25.** Problem: on 2026-10-25 three research agents were cut off by the 5-hour usage window ("session limit") and had saved nothing. This protocol makes any interruption recoverable: progress is saved to disk after every question, and any agent (the same one or a fresh one) can pick up exactly where the last one stopped.

## 1 · The three research tasks

| Letter | Output file (this folder) | Questions |
|---|---|---|
| **G** | `G_Soil_Targets_and_Nutrient_Budgets.md` | Q1 target soil properties · Q2 built-soil classification · Q3 nutrient removal and waste streams · Q4 nitrogen, phosphorus, potassium supply · Q5 crop water · Q6 cropland area per person |
| **H** | `H_Constructed_Soils_Reclamation_and_Regolith.md` | Q1 reclamation cases · Q2 amendments and rates · Q3 salt · Q4 speeding formation · Q5 regolith agriculture · Q6 time and labor · Q7 failure and degradation |
| **I** | `I_Soilless_Systems_Alternatives_and_Closed_Loops.md` | Q1 soilless crop systems · Q2 non-cropland calories and protein · Q3 closed-loop recycling · Q4 per-person budgets · Q5 storage and reserves · Q6 power and heat |

## 2 · What every agent must do (saved progress)

1. **First action:** create the output file. Its first block must be:

```
## PROGRESS (tick after each question is fully written to this file)
- [ ] Q1
- [ ] Q2
... one line per question
```

2. **After each question:** append that question's findings and its search-log lines to the file, then tick its box in the PROGRESS block. A question is ticked only when its findings are in the file, not before.
3. **If the file already exists when you start** (you are resuming): read the whole file first. Do not redo any ticked question. Start at the first unticked question. If a question is half written (findings present, box unticked), finish it by reading what is there and adding what is missing; do not duplicate.
4. Do not spawn sub-agents. Do not delete or rewrite earlier sections. Add a line `RESUMED <date> <time>` to the file when you resume.
5. At the end: fill in the summary table at the top of section (1), add the NOT FOUND list, and tick `- [ ] FINAL` at the bottom of the PROGRESS block.

## 3 · What the main session does when an agent fails

1. A failure notice whose error says "session limit" or "rate_limit" gives a reset time. **Do not re-dispatch before that time.** The session continues by itself at the reset.
2. At the reset, resume the **same agent** by sending it a message (it resumes from its transcript): *"Resume. Read your output file's PROGRESS block, skip ticked questions, continue from the first unticked one, and follow the resume protocol in `_RESUME_PROTOCOL.md`."*
3. If that agent cannot be resumed, dispatch a **fresh agent** with the original task prompt plus this line: *"The output file may already exist with partial progress. Follow section 2, item 3 of `_RESUME_PROTOCOL.md`."*
4. Never delete a partial file. Check each file's PROGRESS block before reporting anything as done.
5. Report to the developer: which questions are ticked, which are not, and when the next attempt is scheduled.

## 4 · Original task prompts

The full prompts are in the session that launched them; they cover exactly the questions listed in section 1, with these binding rules: research fully, never report from snippets, every number sourced and dated and marked SOURCED / COMPUTED / UNVERIFIED, never fill a gap with a guess (write NOT FOUND and where you looked), keep a search log with exact strings and dead ends, real-world facts only, American English.
