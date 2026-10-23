# McNeese AI Harnesses: two-hour run of show

Audience: faculty and staff, mostly academics, mostly beginners with these tools. Delivery: mental model, a Git segment, two live demos built on one real research question, and audience-led practice. Primary outcome: participants can explain what a harness is, watch it go from a citation to a checked number, and decide whether an AI-produced result is good enough to use.

The deck is the Slides artifact "AI Harnesses for Research" (source in `slides/deck/`). The earlier Marp deck in `slides/mcneese-ai-harnesses.*` is superseded and kept only for reference.

| Minute | Segment | Slides | Observable check |
| --- | --- | --- | --- |
| 0-15 | The promise (paper to pipeline), model versus harness, chat versus harness, the scope / inspect / act / verify / decide loop, "AI drafts. You decide." | cover to you-decide | Participants can say what a harness may see, change, and must not do. |
| 15-35 | Git and GitHub: the `final_v2` problem with a coauthored paper, repository / commit / diff, a real diff from the coup data, push and visibility, why agents need Git. Do the 90-second tour of a real repository. | final-file to git-why | Participants can find a README, a commit, its diff, and the visibility setting. |
| 35-65 | Demo 1, paper to data. *Are coups good for democracy?* (Derpanopoulos, Frantz, Geddes and Wright 2016, Research & Politics). Pass 1 builds a claim card from the open full text. Pass 2 pulls the 2015 replication copy and the current Powell and Thyne release, reproduces coup attempts by decade, and diffs the two versions. | d1-open to d1-check | Audience sees a claim checked against the PDF, counts matched by hand, and a data change caught. |
| 65-95 | Demo 2, data to signal. Write a Field Guide module card, have the harness propose a schema and explain its key, build `coups sync` into `store/coups.db` (events, releases, papers from OpenAlex), ask a question in English and read the SQL, then run the sync twice to show idempotence and the change report. | d2-open to d2-checks | Audience sees a durable, self-checking pipeline, and the SQL behind every answer. |
| 95-120 | Habits, guardrails, then audience papers and workflows live. Close with the handout and the Field Guide. | habits to close | Participants leave with one paper or workflow and a failure condition for it. |

## The research thread

Both demos use one public, open-access thread so nothing private ever appears on screen.

| Item | Where | Notes |
| --- | --- | --- |
| Original paper | doi:10.1177/2053168016630837 | Gold open access. Replication archive doi:10.7910/DVN/3IC00L. |
| Reanalysis (Miller 2016) | doi:10.1177/2053168016681908 | Replication archive doi:10.7910/DVN/KAJNYY. |
| Response (2017) | doi:10.1177/2053168017707355 | Replication archive doi:10.7910/DVN/DCIWA5. |
| Coup data, archived | `powell_thyne_coups_final.txt` in DVN/3IC00L | Version V2015.05.07, 472 events, through 2014. |
| Coup data, current | jonathanmpowell.com coup dataset page | `pt_20260829.csv`, version V2026.08.29, 497 events. The old uky.edu URL now returns 403. |
| Literature feed | api.openalex.org | Works without a key on a small shared daily budget; get a free key before the session. |

Numbers on the slides were computed 2026-10-23 and should be re-run the morning of the workshop, because the live release can change:

- Coup attempts by decade (successful / failed): 1950s 30/30, 1960s 67/56, 1970s 55/47, 1980s 38/40, 1990s 22/39, 2000s 12/18, 2010s 11/11, 2020s through August 2026 13/8.
- Drift between the archived and current files (matched on country code and full date): 6 archived events have no exact match, 4 pre-2015 events are new, and 1 matched event changed from successful to failed (Congo, 3 August 1968). Several are date corrections of the same event, for example Chad 2006 moving from 13 April to 13 March.
- Since 2020: 21 attempts in 14 countries. Niger and Sudan have 3 each.

## Demo preparation

- Build and rehearse both demos end to end in a clean folder, in both tools if both will be shown. Keep a known-good finished copy of each folder and a screen recording as the fallback.
- Fill the bracketed cells on the claim-card slide (page numbers; unit, years and N) from what the harness actually returns at rehearsal, and confirm the data sources against the paper text.
- Replace the McNeese policy placeholder on the guardrails slide with the right office or page after checking current guidance.
- Choose two backup papers for the audience segment, ideally from McNeese-heavy fields, each with open full text and a public replication archive.
- Before the session, test network access, Dataverse and OpenAlex reachability from the venue, screen readability, and a clean reset. Never screen-share a personal vault, student files, email, or credentials.

## Next decisions for Josh

- Approve or revise the new deck.
- Decide whether Demo 2 is shown fully live or as a live build from a half-finished checkpoint (safer for time).
- Confirm institutional laptop and data restrictions before inviting optional setup.
