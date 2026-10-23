---
marp: true
theme: default
size: 16:9
paginate: true
html: true
style: |
  :root { --ink: #17283d; --muted: #50647a; --paper: #f6f4ef; --teal: #076b69; --orange: #dc6a37; --navy: #102d49; }
  section { background: var(--paper); color: var(--ink); padding: 72px 92px; font-family: "Avenir Next", Avenir, "Segoe UI", sans-serif; font-size: 32px; line-height: 1.32; }
  section::after { color: var(--muted); font-size: 18px; }
  h1 { font-family: "Iowan Old Style", Georgia, serif; font-size: 60px; font-weight: 600; letter-spacing: -0.035em; line-height: 1.08; margin: 0 0 38px; }
  h2 { font-family: "Iowan Old Style", Georgia, serif; font-size: 40px; line-height: 1.16; margin: 0 0 24px; }
  p { margin: 0 0 22px; }
  li { margin: 0 0 18px; }
  strong { color: var(--teal); }
  small { color: var(--muted); font-size: 22px; }
  code { background: #e2ebe7; color: var(--navy); padding: 0.08em 0.22em; }
  pre { background: #e2ebe7; color: var(--navy); padding: 22px 30px; font-size: 23px; line-height: 1.4; border-left: 6px solid var(--teal); }
  pre code { background: transparent; padding: 0; }
  blockquote { border-left: 6px solid var(--orange); margin: 18px 0; padding: 8px 0 8px 24px; color: var(--navy); }
  section.cover, section.dark { background: var(--navy); color: #fffefa; }
  section.cover h1, section.dark h1 { color: #fffefa; }
  section.cover h1 { font-size: 76px; max-width: 1000px; }
  section.cover p, section.dark p, section.dark li { color: #dbe9ed; }
  section.cover small, section.dark small { color: #c8d9df; }
  section.dark strong, section.cover strong { color: #f2b26e; }
  section.dark::after, section.cover::after { color: #c8d9df; }
  section.question h1 { color: var(--teal); font-size: 72px; }
  section.compact { font-size: 29px; }
  section.compact li { margin-bottom: 13px; }
  section.prompt pre { font-size: 24px; }
  a { color: var(--teal); }
---

<!-- _class: cover -->
<!-- _paginate: false -->

# AI harnesses for everyday work

McNeese faculty and staff workshop<br>Joshua E. Lambert

<small>Guided demo · Optional setup · Two hours</small>

---

<!-- _class: question -->

# What work would you bring to AI?

One question or recurring workflow is enough. You can watch the demonstration without installing anything.

---

<!-- _class: compact -->

# Our two hours

- **0-15:** The mental model and control points
- **15-35:** GitHub, repositories, and saved changes
- **35-70:** Build a small harness, then look at the Almanac Field Guide
- **70-95:** Two short workflows from request to checked result
- **95-120:** Your questions and live examples

---

<!-- _class: dark -->

# A model and a harness

The **model** generates or analyzes content.

The **harness** supplies the working environment: files, tools, instructions, permissions, and checks.

<small>Codex and Claude Code are two ways to work inside a harness.</small>

---

# What changes when AI can use a project?

It can inspect the relevant files, draft an edit, and show the difference.

You can then run a check and decide whether to keep the work.

---

<!-- _class: dark -->

# The working loop

1. **Scope:** Name the result and the boundaries.
2. **Inspect:** Read the relevant context.
3. **Act:** Produce one bounded change or draft.
4. **Verify:** Check the result against your original request.

---

# Your control points

- Which files may the harness read?
- What may it change?
- Which actions need separate approval?
- What evidence would make the result usable?

<small>Use public or synthetic material in today's live examples.</small>

---

<!-- _class: dark -->

# Git and GitHub

**Git** records versions of files and shows what changed.

**GitHub** gives a repository a place to live online and supports review and collaboration.

<small>A repository may be private or public. Check visibility before adding material.</small>

---

# What we will inspect in a repository

1. The project files and a short README
2. A commit, which saves a checkpoint
3. A diff, which shows the exact change
4. The visibility setting

---

<!-- _class: prompt -->

# A small harness brief

```text
Goal: improve the event checklist.
Read: README and checklist.md only.
Change: draft a clearer checklist.
Do not: email anyone or publish the result.
Check: compare the draft to the original requirements.
```

<small>The brief makes the work repeatable and reviewable.</small>

---

# The Almanac Field Guide

The larger example keeps durable context in plain files and gives the agent a shared brief.

Capabilities can be added when needed. Review rules govern what happens before an action leaves the workspace.

<small>We are borrowing its structure, not building an Almanac during this session.</small>

---

<!-- _class: dark -->

# Demo 1: an event checklist

**Input:** A short, incomplete checklist in a sample repository.

**Task:** Draft a clearer version without sending or publishing it.

**Check:** Compare the diff with the original event requirements.

---

<!-- _class: dark -->

# Demo 2: a tiny dataset

**Input:** A synthetic CSV and a question about its totals.

**Task:** Inspect the columns and produce a short summary.

**Check:** Recalculate the key number from the source rows.

---

# Before you use a result

- Did the harness use the right source material?
- Did it change only what you asked?
- Can you reproduce or inspect its key claim?

If a check fails, revise or reject the draft.

---

<!-- _class: prompt -->

# A first prompt to try

```text
Here is my question or workflow: [describe it].
Before acting, tell me what you understand,
what information you need, and the smallest
useful first step. Do not edit or send anything.
Tell me how we could verify the result.
```

---

<!-- _class: question -->

# What should we try together?

Offer a question or workflow. We will pick a safe public or made-up example, define its boundaries, and test one small step.

---

<!-- _class: dark -->

# Your next step

Choose one workflow. Write down its source material, one boundary, and one success check.

The handout and optional setup paths are at **jelambert.com/ai-harness-guide/**
