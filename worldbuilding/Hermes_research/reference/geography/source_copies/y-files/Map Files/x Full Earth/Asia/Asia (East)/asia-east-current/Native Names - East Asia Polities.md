# East Asia — Native-Language Names

Started 2026-09-24. **Companion reference to `naming_worksheet.csv` and `UPDATE INSTRUCTIONS - Naming
Pass.md`, living in this same folder.** Lists every polity's English (map-legend) name alongside a name in
its own region's native language — Mandarin for the Sinian Federation's member states, and each frontier
polity's or sinosphere nation's own language otherwise.

⚠️ **These native-script renderings are drawn from general knowledge, not independently verified by research
this session.** Per the project's own rule (flag uncertainty loudly — an unflagged guess reads as settled
fact later), treat anything below as a proposal to check, not confirmed canon, until a verification pass is
run. Items needing the most scrutiny are called out per-row.

---

## The Sinian Federation and its nine Han states — Mandarin

| ID | English | Mandarin (Hanzi) | Pinyin | English name status | Note |
|---|---|---|---|---|---|
| SIN | The Sinian Federation | 震旦联邦 | Zhèndàn Liánbāng | Resolved 2026-09-24 | Researched, not guessed — see `UPDATE INSTRUCTIONS - Sinian Federation Naming Research.md`. "Sinian" (the real English geological term this coinage borrows) traces to Sanskrit Cīna via 震旦 (Zhèndàn), the actual Chinese term it comes from — not a generic gloss. `支那` (Zhīnà/Shina) was checked and rejected as a real-world ethnic slur. `震旦` isn't everyday vocabulary but is recognizable, roughly the way "Cathay" reads to an English speaker. |
| NCP | Zhongyuan | 中原 | Zhōngyuán | Named this session | This is the real Mandarin term the English name is a romanization of — no separate "native version" needed. |
| NW | Qin | 秦 | Qín | Named this session | Same as above — English name already is the romanized native name. Keeps this name after absorbing Qinghai at Map B1 (author decision 2026-09-24, no rename on territorial growth) — see `UPDATE INSTRUCTIONS - Naming Pass.md` entry 4. |
| BAS | Bashu | 巴蜀 | Bāshǔ | WORKING | Compound of Ba + Shu, matching the file's own `name_basis`. |
| JIN | Jin | 晋 | Jìn | WORKING | |
| WU | Wu | 吴 | Wú | WORKING | Precedent name in notes is Wuyue (吴越); the state itself is just Wu. |
| GAN | Gan | 赣 | Gàn | WORKING | |
| XIA | Xiang | 湘 | Xiāng | WORKING | `polity_id` is `XIA` in the CSV, but the polity and its name are Xiang, not Xia — don't confuse with Western Xia. |
| MIN | Min | 闽 | Mǐn | WORKING | |
| YUE | Yue | 粤 | Yuè | WORKING | |

A note on scope: Wu, Gan, Xiang, Min and Yue are literally the names of non-Mandarin Sinitic language
branches (Wu Chinese, Gan Chinese, Xiang Chinese, Min Chinese, Yue/Cantonese). Per the author's own framing
for this file, the "native language" column for every Sinian Federation member state is **Mandarin**
specifically, not each region's own topolect — so the readings above are Mandarin (Putonghua) pronunciations
of the state names, not Wu-dialect, Cantonese, etc. readings of them. That's a deliberate simplification, not
an oversight.

---

## Frontier polities and sinosphere nations — each region's own language

| ID | English | Native name | Romanization | Language | English name status | Note |
|---|---|---|---|---|---|---|
| QH | Qinghai | 青海 | Qīnghǎi | Mandarin | WORKING | The English name is already the pinyin form; demographically plural (Han ~50-54%, Tibetan ~21%, Hui 16%, Tu 4%), so Mandarin is the administrative choice, not an ethnic claim. |
| IMO | Inner Mongolia | 内蒙古 (Mandarin, admin.) / ᠥᠪᠥᠷ ᠮᠣᠩᠭᠣᠯ ⚠️ (traditional Mongolian script) | Nèi Měnggǔ / Övör Mongol | Mandarin + Mongolian | WORKING | 78.7% Han population per the file's own notes, so Mandarin is the demographic reality; Mongolian given alongside since it's the ethnonymic source and IMO merges into Mongolia by Map B2. ⚠️ Traditional-script rendering unverified. |
| MAN | Manchuria | 满洲 (Mandarin) / ᠮᠠᠨᠵᡠ ⚠️ (Manchu, historic) | Mǎnzhōu / Manju | Mandarin (demographic reality) | WORKING | File notes 8.7M Han settlers 1891-1942 over a Tungusic substrate; Manchu is nearly extinct as a spoken language today, included only as the historic ethnonym behind the English name. |
| MON | Mongolia | Монгол Улс | Mongol Uls | Mongolian (Cyrillic) | ESTABLISHED | |
| ETK | East Turkestan | شەرقىي تۈركىستان ⚠️ | Sherqiy Türkistan | Uyghur | WORKING | ⚠️ Script unverified this session — worth a direct check before treating as final. |
| TIB | Tibet | བོད | Bö (Bod) | Tibetan | WORKING | |
| TWN | Taiwan | 臺灣 (Mandarin, official) / Tâi-oân ⚠️ (Hokkien/Southern Min) | Táiwān / Tâi-oân | Mandarin + Hokkien | WORKING | File explicitly notes Taiwanese is coastal Southern Min and cites this as the "hybridity finding" behind drawing Taiwan separately — Hokkien form included for that reason. |
| NKO | North Korea | 북한 (directional, common usage) / 조선 ⚠️ (state's own self-designation) | Bukhan / Joseon | Korean | Named this session | `Bukhan` ("north Han/Korea") is the everyday directional term, parallel to the English "North Korea"; `Joseon` is the DPRK's own formal self-designation and carries the same real-world political specificity flagged for `KOR` below — included for completeness, not recommended as the default. |
| SKO | South Korea | 남한 (directional, common usage) / 한국 ⚠️ (state's own self-designation) | Namhan / Hanguk | Korean | Named this session | `Namhan` ("south Han/Korea") is the everyday directional term, parallel to "South Korea"; `Hanguk` is the ROK's own formal self-designation, same caveat as `Joseon` above. |
| KOR | Korea | 한국 | Hanguk | Korean | Resolved 2026-09-24 | Author decision: derived by dropping the directional prefix from `NKO`'s `북한` (Bukhan) and `SKO`'s `남한` (Namhan) — both share the `한` root, so the unqualified form is `한국`. Chosen by internal consistency with the two pre-unification names, not by picking between the states' own self-designations (`Hanguk` vs. `Joseon`) — though it does coincide with the ROK's real-world self-designation as a byproduct of the derivation. |
| JPN | Japan | 日本 | Nihon / Nippon | Japanese | ESTABLISHED | |
| HAK | Hakka | 客家 | Mandarin reading: Kèjiā; Hakka's own reading: Hak-kâ | Hakka (own Sinitic branch, not Mandarin) | ESTABLISHED (non-territorial) | Ethnonym, not a state — per the file's own note, 44 million people and no ground in any era. Given as the Hakka-language reading since, unlike the nine Han states above, Hakka itself is the named language here, not a Mandarin label for it. |
| JEJ | Jeju-do | 제주도 | Jeju-do | Korean | ESTABLISHED | English name is already the romanized Korean name. |

---

## Open items this file surfaces (not yet resolved, flagged rather than guessed)

- **`SIN`'s Mandarin equivalent is resolved** (2026-09-24) — `震旦联邦` (Zhèndàn Liánbāng), replacing the
  earlier ad hoc `华夏联邦` guess. See `UPDATE INSTRUCTIONS - Sinian Federation Naming Research.md` for the
  full etymology, the rejected `支那` option, and the recognizability check.
- **`KOR`'s native name is resolved** (2026-09-24) — `한국` (Hanguk), derived from `NKO`/`SKO`'s shared `한`
  root rather than picked between the two states' self-designations. See the table above.
- **Script accuracy for Uyghur (`ETK`), traditional Mongolian (`IMO`), and Manchu (`MAN`)** is unverified this
  session — flagged with ⚠️ above. Worth a direct verification pass (WebSearch/WebFetch) before this file is
  treated as canon-ready, following the same "research proposes, author disposes" discipline used everywhere
  else in this project.
- **`NKO`/`SKO` now use their present-day state names** (author decision 2026-09-24, overriding the prior
  "no present-day names" rule — see `UPDATE INSTRUCTIONS - Naming Pass.md` entry 3). Their native-language
  rows use the everyday directional terms (`Bukhan`/`Namhan`), not the states' own formal self-designations
  (`Joseon`/`Hanguk`) — and `KOR`'s resolution above builds directly on that choice.

*(Update this file alongside `UPDATE INSTRUCTIONS - Naming Pass.md` as more polities get named this
session.)*
