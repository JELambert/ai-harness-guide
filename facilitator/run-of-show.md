# McNeese AI Harnesses: two-hour run of show

Audience: faculty and staff, mostly academics, mostly beginners with these tools. Delivery: mental model, a Git segment, two live demos, and audience-led practice. Primary outcome: participants can explain what a harness is, watch it go from a citation to a checked number, see a module they could set up for themselves, and decide whether an AI-produced result is good enough to use.

The deck is the Slides artifact "AI Harness Guide" (34 slides, source in `slides/deck/`). The earlier Marp deck in `slides/mcneese-ai-harnesses.*` is superseded and kept only for reference.

| Minute | Segment | Slides | Observable check |
| --- | --- | --- | --- |
| 0-15 | The promise, model versus harness, chat versus harness, the scope / inspect / act / verify / decide loop, "AI drafts. You decide." | cover to you-decide | Participants can say what a harness may see, change, and must not do. |
| 15-35 | Git and GitHub: the `final_v2` problem with a coauthored paper, repository / commit / diff, a real diff from the coup data, push and visibility, why agents need Git. Do the 90-second tour of a real repository. | final-file to git-why | Participants can find a README, a commit, its diff, and the visibility setting. |
| 35-65 | Demo 1, paper to data (`examples/coups-paper/`). Claim card from the open full text, then the 2015 replication copy and the 2026 Powell and Thyne release, coup attempts by decade, version drift, and reproducing the paper's 48% / 63% failure shares. | d1-open to d1-check | Audience sees a claim checked against the text, a published number reproduced and one that does not, and a data change caught. |
| 65-95 | Demo 2, set up a Field Guide module (`examples/scholar-footprint/`). From the `scholar` card: resolve the presenter's OpenAlex record out of ten Joshua Lamberts, sync works and coauthors into `store/scholar.db`, write People notes, ask "who do I write with most" and read the SQL, then run the sync twice. | d2-open to d2-checks | Audience sees a module built from a one-page card, a name resolved by asking, and a check that catches a real bug. |
| 95-120 | Habits, guardrails, then audience papers and workflows live. Close with the handout and the Field Guide. | habits to close | Participants leave with one paper or workflow and a failure condition for it. |

## Demo 1 sources and verified numbers

| Item | Where |
| --- | --- |
| Original paper | doi:10.1177/2053168016630837, CC BY-NC; replication archive doi:10.7910/DVN/3IC00L |
| Reanalysis (Miller 2016) | doi:10.1177/2053168016681908, CC BY; archive doi:10.7910/DVN/KAJNYY |
| Response (2017) | doi:10.1177/2053168017707355, CC BY-NC-ND; archive doi:10.7910/DVN/DCIWA5 |
| Coup data, archived | `powell_thyne_coups_final.txt` in DVN/3IC00L: V2015.05.07, 472 events, through 2014 |
| Coup data, current | `pt_20260829.csv` from jonathanmpowell.com: V2026.08.29, 497 events (the old uky.edu URL returns 403) |
| Regime data | `GWF_AllPoliticalRegimes.tab` in DVN/3IC00L |

From the dry run on 2026-10-23 (`examples/coups-paper/reference/notes/findings.md`):

- Coup attempts by decade, successful / failed: 1950s 30/30, 1960s 67/56, 1970s 55/47, 1980s 38/40, 1990s 22/39, 2000s 12/18, 2010s 11/11, 2020s to August 2026 13/8.
- Drift, archived vs current, matched on country code and date: 6 archived events have no exact match, 4 pre-2015 events are new, 1 recoded (Congo, 3 August 1968, successful to failed). Most are date or country corrections of the same event.
- The paper's failure shares: 48% (Cold War) reproduces as 47.9% for coups against dictatorships. 63% (after 1990) does not reproduce under any obvious definition (59.8%, 68.5%, 62.2%); the text does not state the denominator.

Re-run `reference/analysis/fetch.py` and `analyze.py` the morning of the workshop, because the live release can change.

## Demo 2 facts

From the dry run on 2026-10-23 (`examples/scholar-footprint/README.md`):

- "Joshua Lambert" returns 10 OpenAlex author records. The presenter's is A5084970169 (ORCID 0000-0002-7822-0420, UCF).
- Sync: 11 works, 17 authors (one unresolved), 35 authorships; a second run adds +0 to every table.
- People: 15 coauthor notes and 15 entity-map rows. Two questions raised: an author with no OpenAlex id (Paige M. Roberts), and whether Christopher Michael Faulkner and Matthew Faulkner are one person.
- The idempotence rule caught a real bug in the first version of the sync (a NULL key re-inserted the unidentified author every run). The d2-checks slide tells that story.
- The author profile says 13 works; the works feed returns 11.

## Demo preparation

- Rehearse both demos end to end from fresh copies of each `start/` folder, in each tool you will show. The `reference/` folders are the known-good fallback; also keep a screen recording.
- SAGE returns HTTP 403 to scripted PDF downloads. Download the three PDFs by hand and save them in the demo folder's `papers/` before the session. The HTML full text works for the claim card if you skip this.
- Get a free OpenAlex API key and set `OPENALEX_API_KEY`; a shared venue network can exhaust the keyless daily budget.
- Demo 2 runs on the presenter's own public record. Do not run it on an audience member's name without asking first.
- Replace the McNeese policy placeholder on the guardrails slide after checking current guidance.
- Choose two backup papers for the audience segment, ideally from McNeese-heavy fields, each with open full text and a public replication archive.
- Test network access to Dataverse, OpenAlex and jonathanmpowell.com from the venue, screen readability, and a clean reset. Never screen-share a personal vault, student files, email, or credentials.

## Next decisions for Josh

- Approve or revise the deck.
- Decide whether Demo 2 is built fully live or from a half-finished checkpoint (safer for time).
- Confirm institutional laptop and data restrictions before inviting optional setup.
