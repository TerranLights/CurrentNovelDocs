# Donska-Kubania springboard run: report (2026-11-17, day 2, deeper brief)

**Result:** all 12 signs done, 130 of 130 sheets `STATUS: done 2026-11-17, not verified`. One sub-agent per sign, 12 in all, **0 relaunches**. **Whole-nation QA: 130 sheets scanned, 0 problems.** Sheets are unverified (every named item is marked *check*).

## Per-sign table
| # | Sign | Sheets | Agents | Relaunches | QA | Avg words (wc -w) | Longest | Pointers per sheet | Sub-agent tokens | Tool uses | Time |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11 | 1 | 0 | 0 | 1,059 | 1,234 (Domain) | 14 to 15 | 146,995 | 31 | 05:03 to 05:14 (11.1 min) |
| 2 | Taurus | 11 | 1 | 0 | 0 | 1,077 | 1,190 (Domain) | 14 | 173,373 | 30 | 05:15 to 05:25 (10.2 min) |
| 3 | Gemini | 10 | 1 | 0 | 0 | 1,096 | 1,216 (Domain) | 15 to 16 | 164,511 | 27 | 05:25 to 05:35 (10.0 min) |
| 4 | Cancer | 10 | 1 | 0 | 0 | 1,132 | 1,238 (Domain) | 15 to 16 | 183,652 | 42 | 05:35 to 05:48 (12.3 min) |
| 5 | Leo | 13 | 1 | 0 | 0 | 1,077 | 1,223 (Domain) | 13 to 14 | 196,475 | 40 | 05:48 to 06:03 (14.5 min) |
| 6 | Virgo | 10 | 1 | 0 | 0 | 1,142 | 1,243 (Domain) | 14 to 16 | 181,439 | 30 | 06:03 to 06:15 (12.1 min) |
| 7 | Libra | 11 | 1 | 0 | 0 | 1,155 | 1,250 (Domain) | 14 to 15 | 205,284 | 47 | 06:15 to 06:30 (14.4 min) |
| 8 | Scorpio | 11 | 1 | 0 | 0 | 995 | 1,170 (Domain) | 14 to 16 | 167,448 | 30 | 06:30 to 06:40 (9.7 min) |
| 9 | Sagittarius | 11 | 1 | 0 | 0 | 1,001 | 1,091 (Domain) | 14 to 16 | 173,080 | 29 | 06:40 to 06:51 (10.2 min) |
| 10 | Capricorn | 10 | 1 | 0 | 0 | 1,176 | 1,239 (Domain) | 13 to 15 | 185,844 | 37 | 06:51 to 07:02 (11.7 min) |
| 11 | Aquarius | 10 | 1 | 0 | 0 | 1,084 | 1,243 (Domain) | 14 to 16 | 189,306 | 31 | 07:03 to 07:15 (12.4 min) |
| 12 | Pisces | 12 | 1 | 0 | 0 | 1,093 | 1,232 (Domain) | 14 to 16 | 200,140 | 48 | 07:15 to 07:29 (14.0 min) |
| | **Total** | **130** | **12** | **0** | **0** | **1,089** | 1,250 | **13 to 16** | **2,167,547** | 422 | **05:03 to 07:30** |

## Tokens and wall-clock
- **Sub-agent tokens: 2,167,547** (sum of the 12 hand-backs; no relaunches). The run agent's own tokens are not visible to it; the main session adds them for the cost ledger.
- **Wall-clock: 05:03 to 07:30, about 147 minutes**, run in parallel with Russia, Künnarantaiga and Idelsk-Uralia. Sub-agent time per sign 9.7 to 14.5 minutes.
- Compared with day 1 under the same brief: a little under Japan (2.33M), Australia (2.28M) and Mongolia (2.45M).

## Rule breaks and fixes
- **None found.** QA 0 problems in every sign and for the whole nation; no relaunches and no hand edits.
- No zodiac, astrolog* or horoscope words; no "Indian" anywhere; no South Asian names (the "Held for review" lines name only the category).
- **Missing-scope note:** exactly once per sign, in the 12 Domain sheets only (the day-1 lesson held).
- **Law:** no law research outside Libra and Capricorn. One borderline item, kept: Leo "04 - Recognition" points to the regional *honors* statutes of Krasnodar Krai and Rostov Oblast with their recipient lists (who gets honored), which is award criteria, not law research. Ownership (Taurus) explicitly points law to Libra.
- **Process notes (no effect on the sheets):** (1) in Virgo (Domain) and Capricorn (Domain, Authority, Law) the sub-agent set `done` before its word check, found the sheet over 1,250, reset it to `in progress`, trimmed and set `done` again, so the status grid briefly showed a sheet as done that was still changing; (2) in Pisces (Dissolution, Boundary, Escapism) the sub-agent edited a duplicated "Languages needed" line after setting `done`; (3) a sub-agent wrote its own helper scripts into the nation's scratchpad folder and overwrote the run agent's check script; the run agent moved its helpers to a `_run` subfolder from Scorpio on. The checkpoint rule ("done is the very last write") is the one bent in (1) and (2).

## Length
- Average 1,089 words; concept sheets mostly 1,000 to 1,200, above the brief's 700-to-1,000 guide but under the 1,250 flag; Domain sheets 1,091 to 1,250. No length hint was added to any prompt (as instructed). Libra's Domain sat exactly on the 1,250 scan limit.
- Several sub-agents appear to have trimmed toward the 1,250 flag themselves (Virgo, Capricorn).
- The shortest signs, Scorpio (995) and Sagittarius (1,001), ran shorter with no prompt difference; their sheets are not thin on inspection (Scorpio Trust, 928 words, has 14 specific pointers from Khan-Girey and *kunachestvo* to the lost-wallet experiment and defrauded home-buyers).

## Thin, repetitive or generic sheets
- **No sheet reads thin.** Lowest: Scorpio Trust 928, Sagittarius Education 950, Sagittarius Honesty 954, Scorpio Betrayal 955 and Control 956, all with 14 pointers.
- **Repetition inside a sign:** the shared-line scan finds only the "Languages needed" or "Held for review" flag lines repeated (2 to 10 sheets per sign; Capricorn's "Held for review" line is identical in all 10). No table row or sentence is repeated.
- **Somewhat generic, by name:** Sagittarius **Education** leans on the institution list (five universities, seminaries, cadet corps), with the depth in the Adyghe-alphabet, Greek-school and Ukrainization-era pointers. The national survey series turn up often across the nation (eLibrary as a query route in 51 sheets, Rosstat 47, Sholokhov's *Тихий Дон* 27, Levada 21), though they never fill a whole sheet.
- **Pre-modern pointers:** a rough scan found 11 sheets with no dated pre-modern marker (Aries Identity and Competition, Taurus Self-worth, Gemini Connection, Leo Being seen, Virgo Usefulness, Sagittarius Honesty and Education, Capricorn Responsibility and Merit, Pisces Empathy). Four spot-checks all had one in another form: Bosporan inscriptions (Identity), Bersey's 1853 Circassian primer (Education), Don and Adyghe laments (Empathy) and the early Don *duvan* files (Merit).

## Pointers per sheet
13 to 16 in every sheet, counted as section-2 table rows. Most sheets have 14; Gemini, Cancer and Aquarius run 15 to 16. Two Leo sheets and one Capricorn sheet (Law) have 13.

## Do the sheets exploit the nation's depth?
Largely yes. The sheets treat Donska-Kubania as a plural Don-Kuban-Adyghe space, not as "southern Russia":
- **Native-script and minority terms:** search-term tables have Adyghe rows in 116 of 130 sheets and Armenian in 117. Greek (often Pontic) is in 93, Ukrainian or Kuban *balachka* in 104, Turkish or Meskhetian in 56 and Kalmyk in 33.
- **Minorities beyond the best-known two or three:** Shapsugs (82 sheets), Pontic Greeks (89), Hamshen Armenians (68), Meskhetian Turks (100), Old Believers (68) and Nekrasovite Cossacks (27). Also Molokans (29), Kurds (32), Roma (27), Koreans (20), Germans and Mennonites (17), Jews (15), Yezidis (10) and Assyrians (4). Don Kalmyks are named in 61 sheets.
- **Pre-modern layer:** Bosporan and Tanais inscriptions, the *Lay of Igor's Campaign*, the Azov tale (1637), the Nart epic, Khan-Girey, and Don *duvan* and Posolsky Prikaz files.
- **Regional archives and scholarship:** the archives of Krasnodar Krai and Rostov Oblast, the Adyghe Republican Institute (ARIGI), Southern Federal, Kuban State and Adyghe State universities, and Listopadov, Felitsyn and Shcherbina.
- **Gaps:** Abaza, Nogai, Tatars, Georgians and Dukhobors are nearly or wholly absent (Nogai 3, Tatar 3, Abaza 0, Georgian 0, Dukhobor 0). The Kuban Cossack Host as a present-day organization is rarely named (1 sheet). Stavropol is not treated as core, because the tracker header says only "Russia" and no scope file exists. If Stage 0 places Stavropol or Karachay-Cherkess lands in this nation, the Nogai, Abaza and Turkmen (Trukhmen) pointers will need adding.
- **Sensitive topics flagged throughout:** the Circassian expulsion of the 1860s, decossackization, the 1932-33 famine in the Kuban, the Lienz repatriations, the deportations of Meskhetians, Greeks and Germans, and current war recruitment.
