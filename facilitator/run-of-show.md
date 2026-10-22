# McNeese AI Harnesses: two-hour run of show

Audience: faculty and staff beginners. Delivery: guided demo, with optional setup and practice. Primary outcome: participants can explain what a GitHub repository is, describe an AI harness, scope a useful task, inspect a proposed change, and decide whether the result is good enough to use.

| Minute | Segment | Observable check |
| --- | --- | --- |
| 0-10 | Welcome and show the guide. Poll for tool and Git familiarity; reassure observers that installation is optional. | Everyone can open the handout. |
| 10-30 | Explain Git versus GitHub, repositories, commits, and public versus private visibility. Show a small repository and its change history, then connect it to the harness permission and human-review loop. | Participants can identify where project files live, what changed, and what remains private. |
| 30-50 | Demonstrate a small, sanitized faculty/staff task in that repository. First ask the harness to inspect, explain, and propose a plan, without editing. | Audience can state the requested output and success criterion. |
| 50-70 | Let the harness make one bounded change. Show the diff or before/after, run or inspect the output, and reject one plausible but weak suggestion. Save only the accepted change. | Audience sees a human verification decision and a GitHub checkpoint, not just generation. |
| 70-80 | Break; optional GitHub account and desktop-app setup help. | Observers remain able to follow without accounts or installs. |
| 80-100 | Repeat the same task in the second harness, or show the equivalent workflow. Compare shared concepts rather than speed or model rankings. | Participants can translate the workflow between Codex and Claude Code. |
| 100-110 | Prompt repair exercise: turn a vague request into goal, context, boundaries, and a check. Invite participants to try it in their own tool or on paper. | Each participant has one concrete prompt they could reuse. |
| 110-120 | Debrief, optional setup paths, institutional data rules, and one next task. | Exit ticket: what changed, how would you verify it, and what must remain under human control? |

## Demo preparation

Use a synthetic, non-sensitive repository. Keep a known-good copy and a pre-recorded fallback. Before the session, test the exact task in both tools, GitHub access, network access, screen readability, and a clean reset. Keep the practice repository private unless its contents are intentionally public. Never screen-share a personal vault, student files, emails, or live credentials. If a tool fails, narrate the same inspect, scope, act, verify loop using the prepared before/after files.

The precise main task remains an audience choice. A staff-friendly default is revising a one-page event checklist with a missing approval step; a code variant is a tiny CSV summary script. Do not commit to a Python-heavy lab unless the audience asks for it.

## Next decisions for Josh

- Confirm the main demo lane: faculty/staff document, small code task, or a short comparison of both.
- Confirm whether this page serves as pre-work, live handout, or both.
- Confirm institutional laptop and data restrictions before inviting optional setup.
