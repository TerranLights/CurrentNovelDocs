# Resuming this pass

1. Run `bash _dispatch/check_status.sh` from `worldbuilding/Robot_Fundamental_Concepts/`.
2. For any agent whose files are missing or not `STATUS: COMPLETE`:
   - if its agent is still reachable, resume it with SendMessage: "You were cut off. Read the STATUS lines of your files and continue from where they say. Follow `_dispatch/brief.md`."
   - otherwise launch a replacement with this prompt: "Read and follow `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Robot_Fundamental_Concepts/_dispatch/brief.md`. You are agent <X> in `_dispatch/assignments.md`. Some of your files may already exist: read their STATUS lines and continue; never restart a completed file."
3. When all 14 are complete, update `PROGRESS TRACKER.md` and the `03 - Beyond the twelve/` README.
