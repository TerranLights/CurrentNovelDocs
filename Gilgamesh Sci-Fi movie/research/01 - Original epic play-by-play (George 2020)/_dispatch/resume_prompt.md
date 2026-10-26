# Resume prompts (after a usage cutoff)

First run `bash _dispatch/check_status.sh` from the research folder. It prints each file's two checkpoint lines and how many files are fully done.

## Same session, agent still known
Send the agent this message (it resumes from its own transcript):

> The usage window has reset. Continue your assignment from where you stopped. Read the first two lines of each of your output files (STATUS and LINE REFS), read the last scene you wrote, and carry on from there under `_dispatch/brief.md`. Don't restart any file. When every file of yours reads `STATUS: COMPLETE` and `LINE REFS: CHECKED`, reply as the brief asks.

## New session, or the agent can't be reached
Start a fresh general-purpose agent with this prompt, filling in the letter. Take its files from `_dispatch/assignments.md`.

> You are replacing Agent <LETTER> on a research task that was cut off partway. Read your instructions in `<research folder>/_dispatch/brief.md` and your row (Agent <LETTER>) in `_dispatch/assignments.md`; both are binding. Some or all of your output files already exist.
> 1. For each of your files, read the first two lines (STATUS and LINE REFS) and the last scene written.
> 2. Continue from the STATUS line. Never restart a file, and never rewrite finished scenes except to correct line references against the `{l.…}` markers.
> 3. A file whose second line is missing, or reads `LINE REFS: NOT YET CHECKED`, needs its line references checked and corrected. Mark progress as `LINE REFS: CHECKING (done through scene …)`.
> 4. A file that doesn't exist yet: start it as the brief describes.
>
> The source text is in `<research folder>/_source_text (local only, not in git)/`; if it is missing, recreate it with the command in the brief. When every file of yours reads `STATUS: COMPLETE` and `LINE REFS: CHECKED`, reply with the file paths, the scene counts, and the five most easily missed details (or, for variant files, the five most important differences from the standard version).

## The rewrite phase (from 2026-10-25, about 18:45)
A file whose line 3 reads `REWRITE: NOT STARTED` or `REWRITE: IN PROGRESS (...)` is in the copyright rewrite pass. Its instructions are in `_dispatch/rewrite_brief.md`; the agents and their files are in the table there.

**Same session:** send the agent this message:
> The usage window has reset. Continue the rewrite pass under `_dispatch/rewrite_brief.md` from line 3 of each of your files. Don't redo finished scenes.

**New session:** start a replacement with this prompt:
> You are replacing Agent <LETTER> in the rewrite pass. Read `<research folder>/_dispatch/rewrite_brief.md` (binding) and `_dispatch/brief.md` for the file format. For each of your files in the rewrite brief's table, read line 3 (REWRITE) and continue from the next scene. Never redo finished scenes, and never cut content. When each file reads `REWRITE: DONE (SOURCE x%, FILE y%)` with both targets met, reply as the rewrite brief asks.

`<research folder>` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/Gilgamesh Sci-Fi movie/research/01 - Original epic play-by-play (George 2020)`
