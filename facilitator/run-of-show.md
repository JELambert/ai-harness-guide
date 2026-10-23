# McNeese AI Harnesses: two-hour run of show

Audience: faculty and staff beginners. Delivery: mental model, GitHub primer, one continuous workshop-guide example, short end-to-end demos, and audience-led practice. Primary outcome: participants can explain what a repository and harness are, describe a workflow they want AI to help with, and decide whether an AI-produced result is good enough to use.

| Minute | Segment | Observable check |
| --- | --- | --- |
| 0-15 | Introduce model versus harness and the BUS 751 division of labor: AI drafts, the person decides. Contrast pasted chat context with a project-aware tool. Invite participants to hold onto one question or workflow. | Participants can say what the harness may inspect or change and what remains their decision. |
| 15-35 | Start with the familiar `final_v2` file problem from the Git teaching material. Explain repository, commit, diff, push, and public versus private visibility. Do a 90-second tour of the example repository. | Participants can find the README, one commit, a diff, and the visibility setting. |
| 35-70 | Build `workshop-guide/` with `README.md`, `brief.md`, `agenda.md`, `guide.md`, and `AGENTS.md`. Show the standing brief, an explain-before-write pass, the proposed edit, and the no-send boundary. Use the Almanac Field Guide only to show how the pattern scales. | Participants can outline source files, standing instructions, boundaries, and a check for their own workflow. |
| 70-95 | Run the workshop-guide revision and a synthetic attendance-table check. Show the diff and reject an unsupported logistics or attendance claim. Tie the table check to the BUS 751 habit of inspecting shapes, row counts, and a value by hand. | Audience sees a complete, checked workflow rather than a polished answer alone. |
| 95-120 | Open questions and interactive audience examples. Ask for a question or workflow, choose a safe public or synthetic stand-in when real materials are private, then try a few live. Close with the setup paths and one next task. | Participants leave with a use case and a way to judge whether its result is trustworthy. |

## Demo preparation

Use a synthetic, non-sensitive repository for the prepared examples and live audience requests. Keep a known-good copy and a pre-recorded fallback. Before the session, test the exact tasks in both tools, GitHub access, network access, screen readability, and a clean reset. Keep the practice repository private unless its contents are intentionally public. Never screen-share a personal vault, student files, emails, or live credentials. If a tool fails, narrate the same scope, inspect, act, verify loop using the prepared before/after files.

Prepare two short examples with different shapes: revising the one-page workshop guide and checking a tiny synthetic attendance table. Include a deliberately unsupported detail in a proposed draft, or a duplicate in the table, so the verification step has something real to catch. Keep each example small enough to complete and verify in roughly 12 minutes. Audience requests may be broader questions or recurring workflows; translate them to safe, bounded demonstrations rather than opening private data live.

## Next decisions for Josh

- Build and rehearse the two prepared examples and their complete checks.
- Decide which Field Guide files to show in the harness-creation segment.
- Confirm institutional laptop and data restrictions before inviting optional setup.
