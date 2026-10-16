# AI Harness Guide

A two-hour, beginner-friendly workshop for McNeese faculty and staff. It introduces AI harnesses through a guided demonstration, with optional setup and practice. The public-facing handout is a standalone static HTML file at [`site/index.html`](site/index.html).

## What is an AI harness?

For this workshop, a harness is the working environment around a model: the project files it can inspect, the tools it may use, the instructions and permissions that guide it, and the human verification that closes the loop. Claude Code and Codex are two examples. The workshop is about the transferable workflow, not choosing a winner.

## Repo map

- [`site/index.html`](site/index.html): participant pre-work and live handout, designed to work as a static page on Josh's website.
- [`facilitator/run-of-show.md`](facilitator/run-of-show.md): two-hour teaching plan and demo checkpoints.
- [`facilitator/source-map.md`](facilitator/source-map.md): what was adapted from the earlier crash course and BUS 751, including distribution boundaries.
- [`PUBLISHING.md`](PUBLISHING.md): preview and proposed website placement. No website publication is included in this repo setup.

## Preview

Open `site/index.html` in a browser. It has no build step, external fonts, tracking, or runtime dependency. For a local HTTP preview, run `python3 -m http.server 8769 --directory site` and visit `http://127.0.0.1:8769/`.

## Editorial state

This is a private working repo. The guide is prepared for Josh's website but should not be copied to the public site until he reviews the content and confirms a URL and publication timing. Course-specific policies, pricing, and account eligibility must be checked with McNeese before distribution.
