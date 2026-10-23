# AI Harness Guide

A two-hour, beginner-friendly workshop for McNeese faculty and staff. It introduces AI harnesses through a guided demonstration, with optional setup and practice. The public-facing handout is a standalone static HTML file at [`site/index.html`](site/index.html).

## What is an AI harness?

For this workshop, a harness is the working environment around a model: the project files it can inspect, the tools it may use, the instructions and permissions that guide it, and the human verification that closes the loop. Claude Code and Codex are two examples. The workshop is about the transferable workflow, not choosing a winner.

## Repo map

- [`site/index.html`](site/index.html): participant pre-work and live handout, designed to work as a static page on Josh's website.
- [`slides/mcneese-ai-harnesses.md`](slides/mcneese-ai-harnesses.md): editable Marp source for the two-hour workshop slides.
- [`slides/mcneese-ai-harnesses.html`](slides/mcneese-ai-harnesses.html): browser presentation, kept in this private repo for review.
- [`slides/mcneese-ai-harnesses.pdf`](slides/mcneese-ai-harnesses.pdf): offline presentation copy.
- [`examples/workshop-guide/`](examples/workshop-guide/): public-safe demo repository with a source brief, agenda, flawed starting draft, standing agent brief, and a tiny CSV with a duplicate row.
- [`facilitator/run-of-show.md`](facilitator/run-of-show.md): two-hour teaching plan and demo checkpoints.
- [`facilitator/source-map.md`](facilitator/source-map.md): what was adapted from the earlier crash course and BUS 751, including distribution boundaries.
- [`PUBLISHING.md`](PUBLISHING.md): how the handout is published to JELambert.com.

## Preview

Open `site/index.html` in a browser. It has no build step, external fonts, tracking, or runtime dependency. For a local HTTP preview, run `python3 -m http.server 8769 --directory site` and visit `http://127.0.0.1:8769/`.

Open `slides/mcneese-ai-harnesses.html` for a full-screen browser deck, or use the PDF offline. To regenerate both exports after editing the Markdown source:

```bash
marp --html slides/mcneese-ai-harnesses.md -o slides/mcneese-ai-harnesses.html
marp slides/mcneese-ai-harnesses.md -o slides/mcneese-ai-harnesses.pdf
```

## Editorial state

This is a private working repo. The participant handout is live at https://jelambert.com/ai-harness-guide/. The slides remain here for Josh's review and are not published to the website. Course-specific policies, pricing, and account eligibility must be checked with McNeese before distribution.
