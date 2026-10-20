# Reference notes: the *Graymatter* breakdown video (my summary, 2026-10-19)

**Source:** Corridor Crew, *"Something Scary Happens When You Break The Laws of Geometry"* (https://www.youtube.com/watch?v=GaGcLhhhbDs), the production breakdown of the short *Graymatter* (https://youtu.be/sibCmyoTkss), suggested by the author as a liminal-horror reference.

**What this is:** my summary in my own words, from YouTube's **automatic English captions** (the audio transcription has errors, for example "non-Euclidean" appears as "nonukan"). **I have not seen the video's images**, so anything about what the shots look like comes only from the narration. The full caption text is not saved in the repo (it is another party's content); the downloaded copy sits in my temporary working folder and can be re-fetched. Timestamps are approximate. Flags: **(video)** = from the narration; **PROPOSED** = my suggestion; ⚠️M = my memory.

## What the video says
- **Goal (0:00 to 0:35):** the director (Niko Pueringer) wanted a **liminal-space, SCP-style horror short** and was looking for the right inspiration; he points to **H. P. Lovecraft's description of R'lyeh as having "non-Euclidean" geometry** as a source of unease (video).
- **Non-Euclidean geometry in plain terms (0:35 to 1:07):** conventional geometry has laws (triangle angles add to 180 degrees, parallel lines never meet, the shortest path is a straight line); **non-Euclidean geometry breaks one of them**, and strange results follow (video).
- **The key idea, "the paradox of the curved straight line" (1:07 to 2:00):** in a **spherical non-Euclidean space** a straight line **comes back to where it started**; to the character it still looks straight, so they do not notice the curve. He compares it to a **nightmare where you run and run and end where you began, or a tunnel light that never gets closer**, and calls this "very stressful, very dramatic, perfect for a horror film." He also names **hyperbolic space** as another strange space (video).
- **Visual references (3:00 to 4:20):** **M. C. Escher** (the gallery print in which a man looks at a painting of a city that contains the gallery, a recursive loop) and the game **Portal** (video).
- **First, simpler technique: the "magic trick" loop (4:20 to 5:00).** Dress **two parts of a hallway identically** (same art, doors, lighting); when the character steps out of one section, you **reset the camera and actor to the same spot** and stitch the shots into a looping take. A second touch: the teammates **fall behind, then are suddenly standing next to him** when he blinks and looks back. He calls it effective but **subtle**, and wanted something that would "wow" people (video).
- **The main technique: an infinite hallway, shown head-on (5:00 to 13:00).** The end of the hallway **never gets any closer**. The steps:
  1. A 3D model or photo scan **failed**: reflections on the floor look painted on and do not move with the camera (video).
  2. **Gaussian splats** worked: a splat records **how light reaches the camera from different points of view**, so **reflections stay correct**. He says this was the first use of the technique in a narrative short at Corridor, and that it was too new to have been seen in TV or film (video, 2024).
  3. The first splat was **blurry**; he fixed it by running **about 600,000 iterations, 20 times the default**, over **a weekend (about 72 hours)** on a GPU (video).
  4. He **upscaled** the result with AI video upscaling for a **body-camera crispness** (video).
  5. The real hallway is only about **100 feet long**, so he shot the **running motion outdoors** along a straight line of old cobblestone on his street, tracked with a phone's AR camera tracking and imported into After Effects (video).
  6. He **stacked several splat renders as separate video layers**, and **attached the "end of the hallway" piece to the camera using position keyframes only** (rotation keyframes deleted) so it **stays the same distance away** and sticks to the scene; the camera "wiggles but the hallway doesn't" (video).
  7. The result "starts to feel like a loop"; the shot is **100% CGI** with the actor composited (video).

## What this offers the film (PROPOSED)
- **The wheel already is the "curved straight line."** The rim of a wheel station is a real loop: walk it and you come back to where you started. A tear that makes the loop **longer than the station**, or **never complete**, extends something already physical. This is the spherical-geometry idea in the video, and it matches the author's phrase "bend in onto itself."
- **Two levels of effect, as in the video:** a **subtle trick** (identical stretches of corridor, the person you left behind turning up at your shoulder) for most of the film, and **one big "never get closer" shot** held for a key scene.
- **"Hunting from multiple angles" fits the stitched-loop trick:** Garcelle can be **beside someone who has just turned around**, having been far behind a moment earlier.
- **A production route for a derelict station** (⚠️M, reasoning rather than the video): shoot real industrial corridors and turn them into splats, so reflections and sheen look real, with moving figures composited on top. The video shows the method on a **4-minute short by a visual-effects studio**; the cost and workload for a feature-length film are a separate question I have not researched.
- **A distinction for the film's rules:** the video's idea (**space whose geometry loops**) differs from a **wormhole** (two mouths joined). The author decides which the tear is built on; both can coexist, for example loops on the rim and mouths in the hub.

## OPEN (for the author)
1. Which parts of the video's approach do you want to borrow: the subtle loops, the infinite-hallway shot, or the visual references (Escher, Portal)?
2. Is the tear built on **loops/curved space**, **mouths**, or both?
