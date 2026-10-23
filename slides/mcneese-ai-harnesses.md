---
marp: true
theme: default
size: 16:9
paginate: true
html: true
style: |
  :root { --paper:#f3f1eb; --ink:#14202a; --blue:#244acb; --coral:#df6549; --muted:#52606a; --pale:#e6eaff; }
  section { background:var(--paper); color:var(--ink); padding:70px 90px; font-family:"Avenir Next",Arial,sans-serif; font-size:31px; line-height:1.32; }
  section::after { color:var(--muted); font-size:18px; }
  h1,h2 { letter-spacing:-.04em; line-height:1.06; margin:0 0 28px; }
  h1 { font-size:67px; max-width:1050px; }
  h2 { font-size:45px; }
  p { margin:0 0 22px; }
  li { margin:0 0 15px; }
  strong { color:var(--blue); }
  small { font-size:21px; color:var(--muted); }
  code { background:#e2e6f8; color:#142c81; padding:.05em .18em; }
  pre { background:#e6eaff; border-left:6px solid var(--blue); padding:22px 28px; font-size:24px; line-height:1.34; }
  pre code { background:transparent; padding:0; }
  blockquote { border-left:7px solid var(--coral); margin:10px 0; padding:10px 0 10px 28px; font-family:Georgia,serif; font-size:41px; }
  table { font-size:25px; }
  th { color:var(--blue); }
  section.dark,section.cover { background:var(--ink); color:#f5f7ff; }
  section.dark h1,section.cover h1 { color:#f5f7ff; }
  section.dark strong,section.cover strong { color:#98b1ff; }
  section.dark small,section.cover small { color:#c4d0e0; }
  section.dark::after,section.cover::after { color:#c4d0e0; }
  section.cover h1 { font-size:88px; }
  section.question h1 { color:var(--blue); font-size:78px; }
  section.compact { font-size:27px; }
  section.compact li { margin-bottom:11px; }
  section.prompt pre { font-size:27px; }
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Make the work visible.

AI harnesses for everyday work<br>McNeese faculty and staff workshop

<small>Joshua E. Lambert · Guided demo · Optional setup</small>

---

<!-- _class: question -->

# What would you bring to AI?

A question or recurring task is enough. No installation is required today.

---

# What we will do

**00–15** A model, a harness, and your control points<br>
**15–35** GitHub in 20 minutes<br>
**35–70** Build a small harness<br>
**70–95** Two workflows, including a bad answer<br>
**95–120** Your questions and live examples

---

<!-- _class: dark -->

# A model is not a workflow.

The **model** generates or analyzes.

The **harness** gives it files, instructions, tools, boundaries, and checks.

<small>A better tool can still deliver a polished wrong answer.</small>

---

# The context difference

| | Chat window | Project-aware tool |
|---|---|---|
| Source | What you paste | Files it can inspect |
| Change | You copy it back | Proposes edits to files |
| Check | Your manual test | Can run a test and show the result |

<small>More context removes obvious errors, not subtle judgment errors.</small>

---

<!-- _class: dark -->

# AI drafts. You decide.

The assistant can move the mechanical work along.

You define what correct means, inspect the evidence, and decide whether to keep the result.

---

<!-- _class: question -->

# Which file is really final?

`agenda_final.docx`<br>
`agenda_final_v2.docx`<br>
`agenda_USE_THIS.docx`

---

# Four questions filenames cannot answer

1. Which version is authoritative?
2. What changed?
3. Who changed it, and why?
4. Can we return to the earlier version?

---

<!-- _class: dark -->

# Git records the past. GitHub shares it.

A **repository** is a project folder with history.

A **commit** is a named checkpoint for the whole project.

A **diff** shows exactly what changed.

<small>Local commits do not reach GitHub until pushed. Check public/private visibility.</small>

---

# A 90-second repository tour

Open the sample project and find:

- The README: what is this and where do I start?
- One commit: what changed and why?
- The diff: which lines moved?
- The visibility setting: who can see this?

---

<!-- _class: dark -->

# Give the assistant a desk.

Our example: improve a one-page faculty workshop guide.

It may read the brief and agenda, draft the guide, and show the diff.

It may **not** invent logistics, email anyone, or publish.

---

# The project, in five files

```text
workshop-guide/
  README.md      what this project is
  brief.md       dates, audience, constraints
  agenda.md      current plan
  guide.md       participant draft
  AGENTS.md      standing instructions
```

---

# What the standing brief says

Read the brief and agenda first.

Edit only the participant guide.

Show the diff and check each logistical claim.

Do not send or publish without a separate decision.

<small>The Almanac Field Guide scales this same pattern to more roles and capabilities.</small>

---

<!-- _class: question -->

# What would make the answer wrong?

If you cannot name one failure condition, the task is not scoped yet.

---

<!-- _class: prompt -->

# Pass 1: explain before write

```text
Read README.md, brief.md, and agenda.md.
Tell me what facts they establish, what is missing,
and one way the guide could be wrong.
Do not edit or send anything yet.
```

---

<!-- _class: prompt -->

# Pass 2: act and verify

```text
Revise guide.md using only the brief and agenda.
Do not invent dates, venues, or attendance.
Do not email or publish. Show the diff.
Check each logistical claim against its source.
```

---

# Inspect the change

Did it use the right source files?

Did it edit only the requested file?

Are the dates and venue supported?

What remains uncertain?

<small>Keep, revise, or reject. A draft is not a sent announcement.</small>

---

<!-- _class: dark -->

# Demo 2: numbers need a check

A tiny synthetic attendance table says **120 attendees**.

Count the source rows. Identify duplicates. Calculate the total by hand.

The interesting moment is when the attractive summary fails that check.

---

# A request that can be falsified

“Read both tables. Report the join key's type in each. Preserve every order row. Show row counts before and after.”

<small>From BUS 751: name the files, target, constraint, and check.</small>

---

# Three habits worth keeping

**Explain before write:** understand the current work first.

**Test first:** make a bad result fail visibly.

**Alternatives, not an answer:** see tradeoffs before you decide.

---

<!-- _class: question -->

# What should we try together?

Offer a workflow. We will choose a safe stand-in, define the boundary, and test one small step.

---

<!-- _class: dark -->

# Your first harness can be tiny.

One task. A few source files. A standing brief. One check. A human decision.

<small>Handout and optional setup: jelambert.com/ai-harness-guide/</small>
