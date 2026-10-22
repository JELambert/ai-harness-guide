# Website publication handoff

The shareable source is `site/index.html`. It is self-contained and uses only relative in-page anchors, so it can be served at a nested path such as `/ai-harness-guide/` without asset rewriting.

## Proposed route

After review, copy the file into the existing Hugo site's static tree as `modules/site/static/ai-harness-guide/index.html`, then run the site's normal build and release checks. Do not make that public-site change solely by pushing this private repo. The HTML remains the source of truth here; copy or automate it deliberately when publishing.

## Before publication

1. Confirm the audience, date, institutional branding, and whether McNeese wants an official or personal-site URL.
2. Confirm whether the main demonstration is a faculty/staff document workflow, a small code task, or both.
3. Check the current official GitHub account guide and ChatGPT Desktop and Claude Desktop download pages. The guide links to the vendors rather than embedding install commands or prices.
4. Review the sample prompt and data-handling language against McNeese policy.
5. Preview on desktop and phone, check keyboard access, then run the Hugo release check from `ops/boot/README.md` if the site is changed.

Nothing has been published on Josh's website by creating this repo.
