STATUS: OFFICIAL (author, 2026-11-18). No scheduled jobs: the author starts each day by hand, beginning Sunday 11-22. The session that is asked to run a day follows the daily procedure below.

# DCI springboards: the official schedule from Sunday 2026-11-22

**Pace (author):** 12 nations a day, in three waves of four run agents, from the start of the run window (05:00). **Order (author):** the Sinian Federation first, then by subnet: Mirny, Janbogo, Halley, Palmer, Mawson, Byrd. Each subnet takes the not-yet-done nations represented in its cities (`Representation by subnet and city (draft).md`), strongest presence in that subnet first (Primary 3, Significant 2, Notable 1, summed over its cities). Amundsen-Scott is a special case, sorted out later. After the Tepenia-represented nations come the relevant nations not represented in Tepenia (list still to be built).

## The schedule

| Subnet | Day | Wave | Nations |
|---|---|---|---|
| **Sinian Federation** (10) | Sun 11-22 | 1 | Zhongyuan, Qin, Bashu, Jin |
| | Sun 11-22 | 2 | Wu, Gan, Xiang, Min |
| | Sun 11-22 | 3 | Yue, Hakka |
| **1. Mirny** (47) | Sun 11-22 | 3 | Indonesia, New Zealand |
| | Mon 11-23 | 1 | Taiwan, Vietnam, Germany, Philippines |
| | Mon 11-23 | 2 | Thailand, Kazakhstan, United Kingdom, Malaysia |
| | Mon 11-23 | 3 | South Africa, West Papua, Aceh, Patani |
| | Tue 11-24 | 1 | Finland, CSA, Manchuria, East Turkestan |
| | Tue 11-24 | 2 | Tibet, Austro-Bavaria, France, Belarus |
| | Tue 11-24 | 3 | Appalachia, New England, Bulgaria, Lithuania |
| | Wed 11-25 | 1 | Estonia, Latvia, Hungary, Quebec |
| | Wed 11-25 | 2 | Midwest Republic, Colorado, Romania, Chile |
| | Wed 11-25 | 3 | Northern Ireland, Hawaii, Ukraine, Demilitarized Zone |
| | Thu 11-26 | 1 | Prairie Federation, Meridia, Magna Lombardia, Araucanía-Patagonia |
| | Thu 11-26 | 2 | Argentina, Sweden, Norway, Spain |
| | Thu 11-26 | 3 | Netherlands, Sicilia, Serbia, Croatia |
| **2. Janbogo** (11) | week of 11-29, after Kunlun | 1 | Czechia, Poland, México, Slovakia |
| | | 2 | Slovenia, Catalonia, Yucatán, Basque Country |
| **3. Halley** (5) | week of 11-29, after Kunlun | 3 | Brazil, Amazonia, Uruguay, Denmark |
| | | 4 | Iceland (with Greenland) |
| **4. Palmer, 5. Mawson, 6. Byrd** (0) | | | none left: every nation in their cities comes earlier |
| **No subnet** (1) | week of 11-29, after Kunlun | 4 | Greenland |

**Budget:** about 1.5% of the weekly allotment per nation (author's planning figure), so 18% a day; Sunday to Thursday is 60 runs, about 90%. Janbogo, Halley and Greenland (14 runs, about 21%) go in the week of 11-29 to 12-05, **after** the Kunlun ULM run, which opens that week with nothing else running. The rest of that week goes to tuning the full Cascadia investigation, if allotment remains.

## Daily procedure (when the author starts a day)

1. Check the time. Read the first line of `SPRINGBOARD_PROGRESS.md` and every author note added since the last report; follow any ruling found there.
2. Run `springboard_status.py` for each of the day's nations. A nation with sheets done or in progress is **resumed**, never restarted.
3. Append a start line to the progress file's Run log with `>>`.
4. **Wave 1:** launch four background run agents at once, one per nation, each with the saved per-nation run-agent prompt in `SPRINGBOARD_PROGRESS.md` ("THE FULL RUN", the paragraph after "Per-nation run-agent prompt"), with {NATION} filled, the report path `reports/<date>_{NATION}_report.md`, the nation's folder named, and the operational lessons below added.
5. When all four of a wave have reported back: check each (status 130/130, the QA scan), note their tokens (the sub-agent total from the hand-back plus the run agent's own from its task notification), then **launch the next wave at once**. No wave starts after 14:00; a wave that cannot start by then moves to the start of the next day (on Thursday, to the week of 11-29), and the author is told.
6. After the day's last wave: verify every nation yourself (status script, QA scan, word and pointer counts, a sample read), add the rows to the Cost ledger, update the progress file's first line, and report to the author in plain text: sheets done, rule breaks, quality, cost, the window used so far at 1.5% per nation, and whether the next day still fits.
7. If the window's use (at 1.5% per nation, plus the ULM's share if the author has given it) would pass about 95%, launch nothing more and ask the author.
8. Commit and push only on the author's word.

## Operational lessons to add to each run-agent prompt (they do not change the brief)

1. The QA scan rejects the words zodiac, astrolog* and horoscope anywhere, so use other words for native almanacs and divination traditions. Add this sentence to each sub-agent prompt.
2. The missing-scope-file note goes once, in the Domain sheet, not in every sheet. Add this sentence to each sub-agent prompt.
3. Use your own scratchpad subfolder named for the nation (spaces as underscores) for temporary files, with your own helper scripts in its `_run/` subfolder; tell each sub-agent to keep its temporary files in that folder's `tmp/`, never in the scratchpad root or `_run/`. Never use a shared file; other run agents run in parallel.
4. Do not add length instructions of your own to the sub-agent prompts. The brief's Length line is the rule (author, 2026-11-18: aim for about 1,000 words; a little over is fine, up to about 1,200; the scan flags over 1,300).
5. Never take the nation's lands, a unit list or any other content from `Hermes_research` (dropped by the author; never used or cited); tell each sub-agent not to open it. Where the tracker header lists the lands (the Sinian member states' provinces, the Hakka communities), write for those, as a working list the author still confirms; otherwise follow the brief's missing-scope rule and add no unit list of your own.
6. The no-reuse rule also covers the "Who to compare" bullets: each gives a reason specific to that sheet's concept, and none is copied between sheets. Add this sentence to each sub-agent prompt.
7. Do not restate the concept as what the culture believes or values (the QA scan flags that as a finding); state the concept neutrally. Add this sentence to each sub-agent prompt.
8. Diaspora pointers stay as comparison only (author, 2026-11-18): the nation's findings apply to its diaspora.
9. Known false positives: the scan's "sikh" pattern also matches words such as Sikhote-Alin, Lezgin *sikhil* and Ingush *sikho*; a non-South-Asian word caught this way is kept as written and noted in the report.

## Paths
- `<RESULTS>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation`
- `<DM>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/DCI [Deep Culture Investigation]`
- Status and QA: `python3 -I "<DM>/_dispatch/springboard_status.py" "<Nation>"` and `python3 -I "<DM>/_dispatch/springboard_qa.py" "<Nation>" [sign]`. The scripts find each nation by its folder name (all 60 for 11-22 to 11-26 checked 2026-11-18: present, 0/130).
