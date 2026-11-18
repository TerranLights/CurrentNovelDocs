# Dagestan springboards: run report (2026-11-18, Day 3)

**Result:** 130/130 sheets `STATUS: done 2026-11-18, not verified`, Aries to Pisces. There were 12 sign sub-agents (one per sign) plus 1 single-concept relaunch. The whole-nation QA scan reports 1 problem, a false positive (see "Rule breaks and fixes"). The sheets have not been checked against sources; every named item is marked *check*.

**Wall-clock:** 05:03 to about 08:00 (about 177 minutes; the twelve signs ran 05:04 to 07:54, then the relaunch).
**Sub-agent tokens:** 2,345,778 in all: 2,271,897 for the twelve sign agents and 73,881 for the relaunch. The run agent's own tokens are not included; the main session adds them.

## Per-sign table
Words by `wc -w`. Pointers are rows in the "Where to look first" table.

| # | Sign | Sheets | Agents | Relaunches | QA problems | Avg words | Longest | Shortest | Pointers | Tokens | Tool uses | Time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11 | 1 | 0 | 0 | 1,143 | 1,230 (Domain) | 1,097 | 15 | 157,125 | 40 | 05:04-05:17 |
| 2 | Taurus | 11 | 1 | 1 (Security) | 0 | 1,124 | 1,228 (Domain) | 1,078 | 15-16 | 187,052 + 73,881 | 43 + 14 | 05:17-05:31; relaunch 07:54-07:57 |
| 3 | Gemini | 10 | 1 | 0 | 0 | 1,169 | 1,235 (Domain) | 1,091 | 14-15 | 178,418 | 33 | 05:31-05:43 |
| 4 | Cancer | 10 | 1 | 0 | 0 (1 repeated line, fixed by hand) | 1,160 | 1,226 (Domain) | 1,117 | 14-15 | 191,607 | 41 | 05:44-05:57 |
| 5 | Leo | 13 | 1 | 0 | 0 | 1,039 | 1,236 (Domain) | 960 (Joy) | 14-16 | 191,507 | 40 | 05:57-06:11 |
| 6 | Virgo | 10 | 1 | 0 | 0 | 1,176 | 1,247 (Domain) | 1,108 | 14-15 | 193,332 | 46 | 06:12-06:26 |
| 7 | Libra | 11 | 1 | 0 | 1 (false positive) | 1,148 | 1,228 (Domain) | 1,082 | 14-16 | 200,016 | 39 | 06:26-06:41 |
| 8 | Scorpio | 11 | 1 | 0 | 0 | 1,188 | 1,244 (Domain) | 1,129 | 14-15 | 198,119 | 47 | 06:41-06:55 |
| 9 | Sagittarius | 11 | 1 | 0 | 0 | 1,106 | 1,231 (Domain) | 1,041 | 15-16 | 183,268 | 42 | 06:56-07:10 |
| 10 | Capricorn | 10 | 1 | 0 | 0 | 1,076 | 1,232 (Domain) | 984 (Order) | 14-15 | 186,411 | 37 | 07:11-07:24 |
| 11 | Aquarius | 10 | 1 | 0 | 0 | 1,154 | 1,234 (Domain) | 1,059 | 14-15 | 198,521 | 42 | 07:24-07:38 |
| 12 | Pisces | 12 | 1 | 0 | 0 | 1,184 | 1,241 (Domain) | 1,081 | 14-15 | 206,521 | 50 | 07:38-07:54 |
| | **Nation** | **130** | **12 + 1** | **1** | **1 (false positive)** | **1,137** | **1,247** | **960** | **avg 14.9 (14-16)** | **2,345,778** | | **05:03-08:00** |

**Length:** no sheet is over 1,250. 111 of the 118 concept sheets run over the brief's 700 to 1,000 guide (most are 1,050 to 1,200). All the Domain sheets are 1,226 to 1,247. Per the author's open question, nothing about length was changed.

## Rule breaks and fixes
- **QA false positive (kept as written):** Libra, `00 - Domain and folkways.md`, line 52. "sikhil" is the Latin spelling of the Lezgin clan term сихил, and it matches the scan's `sikh` pattern. This is the same false positive as Day 2's "Sikhote-Alin", so the line is left as is. A word-boundary fix to the scan pattern (`\bsikh(s|ism)?\b`) would stop both; that is for the author or the main session to decide.
- **Repeated line (Cancer):** one "Who to compare" bullet, a bare list of the southern peoples with no reason, was word for word the same in `04 - Nurture.md` and `09 - Motherhood.md`. It was fixed by the smallest edit: that bullet, four other bare bullets in Nurture and two in Motherhood each got a reason specific to the concept. No other sign has a repeated line of 60 characters or more across its sheets.
- **Relaunch (Taurus, `05 - Security.md`):** the run agent's own check found no search term in any Dagestani language, only Russian and Arabic. A single-concept relaunch rewrote the sheet (1,194 words, 15 pointers). It now has Avar, Kumyk, Azerbaijani and Chechen (Akkin) rows, all marked *check*, and one row that says Dargin, Lezgin, Lak, Tabasaran, Nogai and Juhuri terms are not known, pointing to each language's bilingual dictionary. The relaunch passed QA on its first run.
- **No other breaks:** the zodiac words, URLs, "Indo-", "Indian", South Asian names and findings phrases are all clean. Law outside Libra and Capricorn appears only as "goes to Libra or Capricorn" redirect lines in the Flags. The missing-scope note ("the nation's exact lands are still to be settled") appears once per sign, in the Domain sheet only. Nothing was taken from Hermes_research.
- **Housekeeping:** the Scorpio sub-agent left a helper script in the shared scratchpad root after another nation's agent overwrote a shared `qa.sh`. It was moved into this run's own subfolder, and from Sagittarius on sub-agents were told where to keep temporary files. Sheets were unaffected.

## Thin, repetitive or generic sheets (by name)
- **Thin on minority-language search terms** (only one row in a Dagestani language): Scorpio `05 - Control.md` (Kumyk only), Capricorn `04 - Discipline.md` (one Kumyk/Lezgin row), Capricorn `08 - Law.md` (one Kumyk/Lezgin row), Pisces `07 - Spirituality.md`, Pisces `08 - Surrender.md`. Gemini's Domain sheet folds five languages into one row, which is fine. Leo's sub-agent said it often pointed to Dargin, Lak, Tabasaran and Juhuri dictionaries rather than give a term it was unsure of. That is honest, but it leaves the smaller languages thin across the nation.
- **Shortest, and thin for the nation's depth:** Leo `11 - Honor.md` (971 words, 14 pointers). Honor is one of the deepest seams in Dagestan (namus, yakh, the feud and the oath), yet the sheet has only seven search-term rows and one general row for Dargin, Lak and Juhuri. Leo `12 - Joy.md` (960) and Capricorn `09 - Order.md` (984) are the other shortest sheets. They are still full, but they are the first places to deepen.
- **Terse "Who to compare" bullets:** across the nation, many bullets give only a few words of reason, and some in Aries to Cancer give none (for example Cancer `02 - Family.md`, `07 - Care.md` and `08 - Abandonment.md`: "**Kumyks** and **Nogais**.", "**Akkin Chechens**."). From Leo on, the prompt reminded sub-agents to give a reason on every line. Bullets got somewhat fuller, but short ones remain.
- **Recurring sources (no overuse):** the most frequent pointers across the 130 sheets are census tables (in about 22 sheets), Kubachi (20), Memorial (19), Rasul Gamzatov (18), the Spiritual Administration of Muslims (13), and Kemper, Ware and Kisriev, Shikhsaidov and the *Chernovik* newspaper (12 each). None fills more than about a sixth of the sheets, and no sign leans on the same few sources.

## Do the sheets exploit the nation's depth?
Mostly yes:
- **Languages and scripts:** the sheets work in the republic's real many-language setting: Russian, Avar, Dargin, Kumyk, Lezgin, Lak, Tabasaran, Nogai, Azerbaijani, Juhuri (Mountain Jewish), Akkin Chechen, and the smaller Andi, Tsez and Archi languages. They give Cyrillic forms and Arabic script, and they point to the ʿajam (Arabic-script local-language) manuscript tradition.
- **Pre-modern pointers:** these are consistent and specific, for example the Derbend-nameh, Hasan Alkadari's *Asari Dagestan*, the Shikhsaidov manuscript catalogs, the Arabic legal and Sufi texts taught in Dagestan, the Khochbar and Sharvili epics, and the nineteenth-century collections on the Caucasian highlanders.
- **Internal comparison:** this goes beyond the big two or three peoples. The sheets set the highland jamaats against the resettled lowland villages and the kutans (winter-pasture settlements). They also cover the Lezgic south split by the Azerbaijan border, the Nogai steppe, the Akkin Chechens and the Aukh land question, the Azerbaijanis and Mountain Jews of Derbent, the Terek and Grebensky Cossacks around Kizlyar, Sufi, Salafi and secular milieus, and migrants in Moscow and the oil north.

**Weak spots:**
- the smaller languages' search terms (often only "see the dictionary");
- the length of the "Who to compare" reasons;
- the five sheets named above.

**Sensitive subjects** are flagged throughout: the insurgency and counterterrorism regimes, feud and honor violence, female genital cutting, the 2022 mobilization protests, the 2023 airport riot, and LGBT and women's refuge.
