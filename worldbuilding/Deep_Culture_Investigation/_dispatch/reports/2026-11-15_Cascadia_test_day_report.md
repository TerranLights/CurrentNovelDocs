# Cascadia test day report: signs 4 to 12 (2026-11-15, overnight)

**Result:** Cascadia is complete. All twelve signs are `done` (130 sheets in all; this run wrote signs 4 to 12, 98 sheets). `springboard_status.py Cascadia` shows 11, 11, 10, 10, 13, 10, 11, 11, 11, 10, 10, 12, every one done. Every sheet's first line is `STATUS: done 2026-11-15, not verified`. Every sheet carries the "Held for review" line. No sheet contains a URL.

## Per-sign table (this run)

| Sign | Sheets | Agents launched | Relaunches | QA problems flagged | Fixed by hand | Avg words | Max words |
|---|---|---|---|---|---|---|---|
| 4 Cancer | 10 | 10 | 0 | 0 | 0 | 846 | 919 (Shelter) |
| 5 Leo | 13 | 13 | 0 | 3 | 1 | 833 | 878 (Domain) |
| 6 Virgo | 10 | 10 | 0 | 1 | 0 | 833 | 932 (Work) |
| 7 Libra | 11 | 11 | 0 | 1 | 0 | 827 | 923 (Diplomacy) |
| 8 Scorpio | 11 | 11 | 0 | 0 | 0 | 855 | 947 (Domain) |
| 9 Sagittarius | 11 | 11 | 0 | 0 | 0 | 836 | 887 (Domain) |
| 10 Capricorn | 10 | 10 | 0 | 2 | 1 | 834 | 934 (Domain) |
| 11 Aquarius | 10 | 10 | 0 | 0 | 0 | 858 | 925 (Domain) |
| 12 Pisces | 12 | 12 | 0 | 1 | 1 | 873 | 999 (Surrender) |
| **Total** | **98** | **98** | **0** | **8** | **3** | **844** | **999** |

Word counts are `wc -w`, which counts every table pipe as a word. 82,722 words across the nine signs. Sub-agent self-reports of tokens ran from about 53,000 to 67,000 each (about 61,000 on average), so the nation-day cost about **6.0 million tokens** in sub-agents (98 agents), plus the run agent's own overhead (mostly the "agent finished" notices, which arrive in bulk). That matches the 5.8 million estimate.

## Wall-clock

First launch about 02:10:40, last agent returned about 02:27:00 (system clock): **about 17 minutes** for nine signs, about 1.5 to 2 minutes per sign. Each agent took 28 to 63 seconds; the sign is gated by its slowest agent. Nothing waited on a usage window.

## Rule breaks and how they were fixed

QA scanned all 130 Cascadia sheets at the end: 5 flags remain, all false positives (see below). Nothing was relaunched.

1. **"Indian" in a published title (QA false positives, left as is):** Holm, *Northwest Coast Indian Art* (Leo Creativity; Libra Balance); Culin, *Games of the North American Indians* (Leo Play); Lutz *Makuk* / Raibmon *Authentic Indians* / Knight *Indians at Work* (Virgo Work); the institutions' own names Chemawa and Sherman Indian schools (Capricorn Discipline). Their standing rule allows published titles and a body's own name, so I kept these. The QA allowlist (`INDIAN_OK`) simply does not know these titles.
2. **"Indian" in an organization's name, rewritten (Leo Leadership):** "Union of BC Indian Chiefs" became "the provincial First Nations chiefs' union (search 'UBCIC')". One could argue the original is the body's own name; I took the cautious reading.
3. **"Indian" in a descriptive phrase, rewritten (Capricorn Discipline):** "Interior Department Indian boarding school investigation reports" became "... federal boarding school investigation reports".
4. **Zodiac word (Pisces Domain):** "astrology items" as a survey topic became "New Age belief items".
5. Rule scans I ran myself: no URLs anywhere; every sheet has the Held for review line; no law words outside Libra and Capricorn except three incidental mentions (BC "court files" for the Doukhobor and Bountiful records, a "not statute texts" search instruction in Aquarius Reform, "ceremonial and legal knowledge" in a sensitivity flag). Pisces Crime explicitly sends law to Libra and Capricorn, which is the intended behavior. I did not do a line-by-line audit of all 98 sheets for findings or invented names; I read Pisces Crime and Libra Justice in full (both clean: terms, real-looking surveys and bodies all marked *check*, no findings).

## Anything odd

- **Length.** Every agent was told "about 750, never over 1,000"; the average came out at 844 and one landed at 999. At least five agents wrote a first draft over 1,000 words (for example 1,019, 1,067, 1,086, 1,100) and trimmed it themselves. The cap held; the aim did not. The agents are probably counting prose words, while `wc` counts pipes.
- **Status can lie for a minute.** Several agents wrote the file with `STATUS: done` first and then trimmed it, so a status or `wc` check made the moment the grid reads full can catch a draft (my Leo check read 1,067 and 1,018 words; the final files were 860 and 799). I now re-run after the agents return. A "done" in the grid is not proof the agent has finished.
- **Stray column.** Many "Where to look first" tables have an empty header cell (`| Pointer | What it is | What it would give | Reach | |`) with *check* in it. It looks like the template, not the agents; every sheet shows it.
- **Scratch files.** Two agents (Scorpio Crisis, Aquarius Reform) used `/tmp` for a scratch file instead of the scratchpad; harmless.
- **Thin concepts.** Where agents were unsure of Indigenous-language terms they wrote "terms only as each nation publishes them" (Pisces Crime, Libra Justice) or admitted thin coverage in the Flags (Scorpio Crisis, Leo Play). That is the intended behavior; the Indigenous-language columns are therefore the weakest part of the whole nation.
- **Invented-looking names:** none seen in the two sheets I read in full and in the Indian-title lines I looked at. A name-by-name check is exactly what the later research phase is for.

## What I would change in the brief

1. State the length as **table-pipes-included words** or ask for "prose words under 650", and tell agents `wc` is the measure; or accept about 850 as the real target.
2. Fix the template's empty table header cell.
3. Add the published titles in item 1 above (and "Indian" inside an institution's own name) to the QA allowlist, so that a clean run reads 0 problems.
4. Tell agents to write `in progress` first and `done` only on the very last write, so the status script is a reliable "finished" signal.
5. Keep per-concept agents for now: cost per sheet is about 61,000 tokens, dominated by re-reading the spec and brief. A per-sign agent writing 10 to 13 sheets would be roughly a tenth of that, as the progress file already says.
6. For Libra and Capricorn, add one line to the brief naming which half of the law split the agent is on (letter or spirit), so Libra Justice and Capricorn Law do not overlap.

## Questions for the author

- Is the 844-word average acceptable, or should the next nation be held to a tighter limit (and should the QA enforce it)?
- Is an organization's own name containing "Indian" (for example the Union of BC Indian Chiefs) to stay as published, or always be replaced as I did? I replaced it.
- Is "astrology" as a belief-survey item a zodiac-derived pointer, or only the zodiac as a research classifier? I treated the QA's flag as correct and rewrote the line.
- Pace: with 17 minutes and about 6 million tokens per nation-day, the open question is the token budget, not time. Say which cost shape you want for Alaska (per-concept as here, or one agent per sign).

## What I touched

Only the nine Cascadia Springboards folders under `Targets/North America/Cascadia/Springboards/` (signs 04 to 12), the Run log in `SPRINGBOARD_PROGRESS.md` (nine lines appended; its earlier uncommitted modification is untouched), and this report. Nothing was committed or pushed.
