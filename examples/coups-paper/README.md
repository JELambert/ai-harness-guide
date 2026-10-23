# Demo 1: paper to data

A live demo for the McNeese workshop. The harness reads an open-access paper, builds a claim card, pulls the replication data and the current release of the same dataset, reproduces a published number, and reports where the data changed.

- `start/` is the folder you open the harness in on stage: a standing brief and empty folders.
- `reference/` is the finished result of a full dry run on 2026-10-23. It is the fallback if the network or the tool fails, and the answer key for checking the live run.

## Run order on stage

1. Open a harness in a fresh copy of `start/` (`cp -R start /tmp/coups-paper && cd /tmp/coups-paper && git init`).
2. Pass 1, read before analyzing:

   > Read AGENTS.md. Find the open-access full text of doi:10.1177/2053168016630837 and fill notes/claim-card.md: main claim, data sources, unit of analysis, years, N, and the key numbers, citing a section for each. Mark anything you could not find. Do not download data or run analysis yet.

3. Pass 2, data:

   > Download the coup file from the paper's Dataverse archive (doi:10.7910/DVN/3IC00L) and the current Powell and Thyne release into data/raw/. Report rows and version for each. Count coup attempts by decade, split by success, and list every event that differs between the two versions.

4. Pass 3, verify a published number:

   > The paper says 48% of coup attempts failed during the Cold War and 63% after it. Reproduce both from the archived file. If they do not match, try the most likely definitions and show each result. Do not pick one for me.

5. Check by hand: row counts, the codebook (1 = failed, 2 = successful), and one event the room knows (Gabon, 30 August 2023).

## Known gotchas from the dry run

- SAGE blocks scripted PDF downloads (HTTP 403 bot wall). The HTML full text reads fine in a browser. Download the three PDFs by hand before the session and drop them in `papers/` so the live run does not depend on it.
- The coup file URL in older papers (uky.edu) returns 403. The current file is linked from jonathanmpowell.com's coup dataset page.
- Dataverse serves tabular files as `.tab`; ask for `?format=original` only when you want the Stata file.
- Re-run `reference/analysis/fetch.py` the morning of the workshop: the live release can change and the slide numbers should match.
