# Japan springboards: run report (2026-11-16, deeper brief)

Nation: Japan (`Targets/Asia/East Asia/Japan/Springboards/`). All twelve signs, one sub-agent per sign, run 05:03 to 07:29 (about 146 minutes of wall-clock, signs run one after another). No `00 - Scope.md` exists for Japan; the tracker records no pre-war land changes, so sheets were written for the core lands (main islands, Hokkaido with Ainu lands, Okinawa and the Ryukyu chain).

## Per sign

| Sign | Sheets | Agents | Relaunches | QA (non-length) | Avg words (wc -w) | Longest | Sub-agent tokens | Minutes |
|---|---|---|---|---|---|---|---|---|
| 1 Aries | 11 | 1 | 0 | 0 | 1,369 | 1,679 Domain | 182,680 | 13.9 |
| 2 Taurus | 11 | 1 | 0 | 0 | 1,164 | 1,237 Security | 202,216 | 13.5 |
| 3 Gemini | 10 | 1 | 0 | 1 finding-phrase, fixed | 1,181 | 1,244 Domain | 194,893 | 12.6 |
| 4 Cancer | 10 | 1 | 0 | 0 | 1,230 | 1,347 Domain | 180,622 | 9.5 |
| 5 Leo | 13 | 1 | 0 | 0 | 1,144 | 1,262 Domain | 189,873 | 11.1 |
| 6 Virgo | 10 | 1 | 0 | 0 | 1,181 | 1,261 Domain | 197,347 | 11.9 |
| 7 Libra | 11 | 1 | 0 | 1 zodiac word, fixed | 1,252 | 1,392 Domain | 192,761 | 10.5 |
| 8 Scorpio | 11 | 1 | 0 | 0 | 1,212 | 1,513 Domain | 188,777 | 10.7 |
| 9 Sagittarius | 11 | 1 | 0 | 0 | 1,405 | 1,758 Domain | 218,714 | 15.5 |
| 10 Capricorn | 10 | 1 | 0 | 0 | 1,231 | 1,408 Domain | 195,586 | 12.0 |
| 11 Aquarius | 10 | 1 | 0 | 0 | 1,153 | 1,245 Domain | 186,184 | 9.9 |
| 12 Pisces | 12 | 1 | 0 | 0 | 1,289 | 1,554 Domain | 202,013 | 12.7 |
| **Total** | **130** | **12** | **0** | | **1,235** | 1,758 | **2,331,666** | about 146 |

Tokens: sub-agents only, as reported by the harness (about 194,000 per sign on average). The run agent's own tokens are not visible to the run agent; the main session should add its estimate (the earlier runs used about 0.12M). At the ledger's 1.2M tokens per 1%, the sub-agents alone are about 1.9% of the weekly allotment, so the deeper brief costs roughly 1.5 times the old cost-minimizing runs (1.45 to 1.57M per nation).

## Rule breaks and fixes
- **Zodiac word (Libra, 08 Indecision):** a table row on "horoscope rankings and annual fortune guides" (a zodiac-derived pointer). Rewritten by hand to "Morning-show daily-advice segments and print guides to everyday choices". Rescan clean.
- **Finding-phrase (Gemini, 01 Communication):** the concept-definition line read "what the culture believes good communication is for" and tripped the findings scan. Rewritten to "what good communication is held to be for (a question to research, not an answer)". Rescan clean.
- **Jataka mention (Pisces, 03 Self-sacrifice):** a row on the Hōryūji Tamamushi Shrine panel carried the gloss "Jataka-derived", a South Asian work name outside the held line. Gloss removed by hand (the row keeps the Japanese object).
- **No "Indian"** anywhere in the nation; no South Asian terms outside the held line (Buddhist terms as Japanese traditions are not treated as South Asian pointers).
- **Law rule:** non-Libra, non-Capricorn sheets that touch law say "point to Libra or Capricorn" and keep to history, culture and statistics. Pisces 10 Crime was read in full: official crime statistics, fiction, film, folklore and rehabilitation volunteering, no legal research. Two soft cases left (Pisces 01 mentions the 1998 NPO Law as a dated event; Pisces 03 mentions court cases around Okinawa Notes), both as context for a cultural question, not as law pointers.
- **Length (the only remaining QA flags):** the whole-nation scan shows 45 problems, all "long" (over 1,250 words by `wc -w`, markup included): 9 domain sheets and 36 concept sheets. No sheet was relaunched for length because the brief's Priority block puts depth before length and says length is a guide. Note the target is "about 700 to 1,000 counting markup": all 118 concept sheets exceed 1,000 (mean about 1,218) and 11 of 12 domain sheets exceed 1,200 (longest: Sagittarius domain, 1,758). The author should decide whether the 1,250 flag or the 700-1,000 target is the real rule; the sheets fit neither.

## Thin, repetitive or generic sheets
- **Nothing is generic or padded.** No two table rows are identical across the nation (130 sheets; the only repeat is the header row). Every sheet has 13 to 20 pointers (Where to look first): Aries avg 15.6, Taurus 15.0, Gemini 15.9, Cancer 15.4, Leo 15.2, Virgo 14.5, Libra 17.1, Scorpio 14.4, Sagittarius 16.0, Capricorn 14.5, Aquarius 14.5, Pisces 14.9. Lowest: one Scorpio sheet at 13; no sheet under 13.
- **Thin by the sub-agents' own report:** the Ainu and Okinawan/Ryukyuan term rows in Sagittarius (all sheets; marked "not known" or *check*) and in Capricorn 07 Merit and 04 Discipline (dictionary or oral-tradition pointers instead of terms). Ainu in Pisces 10 Crime is a "query first" row. These are honest gaps, not inventions.
- **Recurring gateway sources (moderate repetition):** NHK appears in 63 of 130 sheets, the Cabinet Office opinion polls in 62, NDL Search in 59, Aozora Bunko in 54, Upopoy in 35, e-Stat in 29, JGSS in 23, the Okinawa Times in 23, the Ryukyu Shimpo in 19, Yanagita Kunio in 17, Yanagi in 19 (name matches overlap). These are legitimate entry points for Japan, but a later pass could diversify them; the per-sign content (classical texts, specific datasets, per-concept scholarship) is distinct.

## Does it exploit the nation's depth?
Yes, to a high degree. Every sheet carries Japanese-script terms with readings and glosses, Ainu and Okinawan/Ryukyuan term rows where the agents could give them, and pre-modern pointers (Kojiki, Engishiki, Heian diaries, Tsurezuregusa, Zeami, Edo records, Ryukyu court chronicles such as Chūzan Seikan and Kyūyō, Shinran and Dōgen, Motoori Norinaga). "Who to compare" regularly goes beyond the best-known pair: Hokkaido and the Ainu, Okinawa and the Ryukyu chain, Tohoku, Kansai, Kyushu, rural districts against the big cities, burakumin, Zainichi Koreans and foreign residents, generational cohorts, religious bodies. Weakest spots are minority-language terminology (Ainu, Ryukyuan languages), where the agents were honest rather than inventive.

## Notes for the main session
- Status check: 130/130 done; first line of SPRINGBOARD_PROGRESS.md untouched; Run log lines appended with `>>`.
- The status grid still shows the tracker's "Signs" column blank for Japan (the brief forbids touching the tracker); update it from the main session if wanted.
