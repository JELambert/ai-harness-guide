# AI Harness Guide

Materials from a McNeese faculty and staff workshop on AI harnesses: tools like Claude Code and Codex that work inside a folder on your computer instead of a chat window.

**The idea: put your work in one folder, and let an AI harness work across all of it.** An email, a syllabus, a paper, a spreadsheet: once they sit in one folder, the harness can read them together, draft what you need, and show you exactly what it changed. You check it, and you decide.

## What is here

| File | What it is |
| --- | --- |
| [`slides.html`](slides.html) | The workshop deck. Download and open in any browser. Arrow keys to move, `f` for full screen. |
| [`handout.html`](handout.html) | The participant handout and setup links. |
| [`prompts.md`](prompts.md) | Every prompt from the session, ready to paste. |
| [`AGENTS.md`](AGENTS.md) | The standing brief the harness reads every time it opens this folder. `CLAUDE.md` points to it, so Claude Code and Codex share one brief. |
| [`semester/`](semester/) | A sample faculty folder to practice on. Everything in it is synthetic or open access. |

## Try it

1. Install [Claude Code](https://code.claude.com/docs/en/quickstart) or the [Codex app](https://developers.openai.com/codex/app) and sign in.
2. Download this folder (green **Code** button, then **Download ZIP**) and unzip it.
3. Open the harness in the folder, and paste the first prompt from [`prompts.md`](prompts.md).
4. Run `semester/research/get-paper.sh` once (or ask the harness to) to download the reading.

When it writes something, read it before you trust it. That part stays yours.

## Next step

Make your own folder for one real piece of work, ask the harness to write its brief, and give it one task with one thing you will check. When that works, grow it: one larger folder holding your repositories, notes, PDFs and data, so the harness can connect all of it. The [Almanac Field Guide](https://github.com/JELambert/almanac-field-guide) is one way to build that.

## Before you use your own files

Keep student records, human-subjects data, and anything held in confidence out of the folder unless your institution's policy and an approved tool allow it.
