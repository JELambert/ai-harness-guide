# Dry-run findings, 2026-10-23

Produced by `analysis/fetch.py` then `analysis/analyze.py`. Outputs are in `analysis/out/`.

## Data in

| File | Rows | Version |
| --- | --- | --- |
| `powell_thyne_coups_final.txt` (paper's Dataverse archive) | 472 | V2015.05.07, through 2014 |
| `pt_20260829.csv` (current release) | 497 | V2026.08.29, through August 2026 |
| `GWF_AllPoliticalRegimes.tab` (paper's Dataverse archive) | 7,954 country-years | n/a |

## Reproducing a published number

The paper says 48% of attempted coups failed during the Cold War and 63% after it.

| Definition | 1950-1989 | 1990-2014 |
| --- | --- | --- |
| All attempts | 47.1% (n=365) | 59.8% (n=107) |
| Attempts against dictatorships | **47.9%** (n=261) | 68.5% (n=54) |
| Country-years under dictatorship | 44.0% (n=225) | 62.2% (n=45) |

The Cold War figure reproduces under the paper's own scope (coups against dictatorships). The post-1990 figure does not reproduce under any obvious definition, and the text does not state the denominator. The honest conclusion is "close, definition unclear", which is a question for the appendix or the authors, not something to paper over.

## The record moved

Matching on country code and full date, 472 archived events against the current release:

- 6 archived events have no exact match now.
- 4 events dated 2014 or earlier are new.
- 1 matched event changed from successful to failed: Congo, 3 August 1968.

Most are corrections to the same event: Chad 2006 moved from 13 April to 13 March; the 30 August 1968 Congo success moved to 4 September; a 5 February 1976 event moved from Chad to the Central African Republic. Full list in `analysis/out/drift.csv`.

## Coup attempts by decade (current release)

1950s 30 successful / 30 failed; 1960s 67/56; 1970s 55/47; 1980s 38/40; 1990s 22/39; 2000s 12/18; 2010s 11/11; 2020s (to August 2026) 13/8.

## Friction worth narrating

- SAGE returns HTTP 403 to scripted PDF downloads. The HTML full text reads fine in a browser, so the harness can still build the claim card. Download PDFs by hand before the session.
- The old uky.edu coup data URL returns 403; the current file is on jonathanmpowell.com.
