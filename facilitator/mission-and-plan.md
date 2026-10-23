# McNeese AI Harness Guide: mission and plan

Decisions confirmed by Josh on 2026-10-23: mission "one folder, one harness"; files first plus one live connector; all four vignettes, shown on one brief slide; most of the session spent working live in Claude Code and Codex; the coups and scholar demos cut.

## Why the previous deck missed

- **No thread.** Good pieces (harness vs model, Git as undo, verify before you trust), but the demos went deep in one narrow domain and did not answer what a faculty or staff member does differently on Monday.
- **Too much on slides.** Demo slides carried code, SQL and tables. The doing should happen in the tool, not on a slide.
- **Too narrow.** Research only, twice, when the point is breadth: email, teaching, research, data, all in one place.
- **It drifted from what already works.** The crash course and BUS 751 already found the right ideas: *make the harness your first point of entry*, *one top-level folder so it connects across everything*, *CLAUDE.md is a living brief*, *talk to it long and specific*, *Git is its undo button*, *the AI drafts, you decide*.

## Mission

**Put your work in one folder, and let an AI harness work across all of it.**

Faculty and staff juggle email, courses, research and service across a dozen apps. A chat window sees only what you paste. A harness (Claude Code, Codex) works in a folder: drop in an email, a syllabus, a paper, a spreadsheet, and it reads them together, drafts what you need, and shows exactly what it changed. You decide and you send.

Participants leave able to say:

1. A harness is a model plus a desk: my files, a standing brief, tools, and limits.
2. If it is in the folder, the harness can use it and connect it to everything else.
3. I describe the outcome in plain, specific language; it drafts; I check and decide.
4. I know my first step on Monday.

## Shape of the session: few slides, mostly live

About 12 slides, about 75 minutes working live in the tools.

| Minutes | Segment | Slides | Mode |
| --- | --- | --- | --- |
| 0-10 | Mission: one folder, one harness; the chat-window ceiling | 3 | Slides |
| 10-25 | The desk: what a harness is, CLAUDE.md, drafts-you-decide, how to talk to it | 3 | Slides, then a 2-minute look at a real CLAUDE.md |
| 25-35 | Git as the undo button | 2 | Slides, then one live commit and one live undo |
| 35-105 | The folder fills up: four vignettes and the payoff question | 1 | **Live** in Claude Code and Codex |
| 105-115 | Your turn: an audience workflow, on a safe stand-in | 1 | **Live** |
| 115-120 | Monday: your first folder, your first brief, where it grows (Field Guide) | 2 | Slides |

The one vignette slide stays on screen as a map: four tiles (email, syllabus, paper, spreadsheet), each a single line, plus the payoff question. Prompts live in the run sheet, not on slides.

## The live demo folder: `examples/my-semester/`

Starts nearly empty; fills up on stage. All content synthetic or open access.

```
my-semester/
  CLAUDE.md, AGENTS.md   standing brief (Claude Code reads one, Codex the other)
  inbox/                 a chair's email as an .eml file
  teaching/              catalog description, last year's syllabus, academic calendar
  research/              one open-access paper (PDF)
  data/                  a synthetic gradebook or survey export (CSV)
  notes/                 what the harness writes; opened in Obsidian
```

| # | Bring in | Ask for | Check |
| --- | --- | --- | --- |
| 0 | Nothing | "Set up this folder for my semester and write the brief." | Read the brief it wrote; fix one line out loud. |
| 1 | The chair's email | "What is being asked of me, and by when? Draft a reply. Do not send." | Every ask and date traced to the email; nothing sent. |
| 2 | Catalog text, old syllabus, calendar | "Build the spring syllabus that answers that email." | Dates match the calendar; policies flagged for me. |
| 3 | An open-access paper | "Write a reading note and link it to the week it fits." | One claim checked against the PDF; link visible in Obsidian. |
| 4 | A spreadsheet export | "Summarize it and chart the one thing I should look at." | Row count, and one value by hand. |
| 5 | Everything | "What do I owe whom this week, and what is ready?" | Every item points to a file in the folder. |
| + | One live connector | Same question, now reaching Gmail or Drive directly | Read-only; nothing sent. |

Show at least one vignette in Codex and the rest in Claude Code, on the same folder, to make the point that the pattern is not the brand.

## Build list

1. `examples/my-semester/`: the start state (brief only) and a finished reference copy as the stage fallback, with synthetic email, syllabus, calendar, CSV, and one open-access paper.
2. Dry-run all five vignettes in Claude Code and at least one in Codex; record timings and any friction.
3. The deck, rebuilt to about 12 slides on the mission, reusing the harness diagram, chat vs harness, the loop, "AI drafts. You decide.", the final_v2 Git slides, guardrails and the close.
4. A run sheet in `facilitator/run-of-show.md`: exact prompts, checks, timings, fallbacks, and the connector step.
5. Handout (`site/index.html`) aligned to the mission. Publishing it stays a separate decision.

## Cut

`examples/coups-paper/` and `examples/scholar-footprint/` are removed from the repo (recoverable from Git history).
