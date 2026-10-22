# Website publication handoff

The shareable source is `site/index.html`. It is self-contained and uses only relative in-page anchors, so it can be served at a nested path such as `/ai-harness-guide/` without asset rewriting.

## Personal website route

JELambert.com is served from the Netlify-backed `JELambert/personalsite` repository, not Almanac's private `modules/site` Hugo site or the older `JELambert.github.io` checkout. Copy this file to `repos/personalsite/static/ai-harness-guide/index.html`, commit and push that repository, then verify `https://jelambert.com/ai-harness-guide/` returns the guide. Pushing this private repo alone does not publish the page. This file remains the source of truth for future revisions.

## Before publication

1. Confirm the audience, date, institutional branding, and whether McNeese wants an official or personal-site URL.
2. Confirm whether the main demonstration is a faculty/staff document workflow, a small code task, or both.
3. Check the current official GitHub account guide and ChatGPT Desktop and Claude Desktop download pages. The guide links to the vendors rather than embedding install commands or prices.
4. Review the sample prompt and data-handling language against McNeese policy.
5. Preview on desktop and phone, check keyboard access, then run the Hugo release check from `ops/boot/README.md` if the site is changed.

The public-site copy was committed as `48a5d19` in `JELambert/personalsite` on 2026-10-22. Confirm the live URL after each deployment before sharing it.
