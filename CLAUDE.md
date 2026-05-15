# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal academic website built on the HugoBlox Academic CV template (Hugo + Hugo Modules + Tailwind v4). Content is plain Markdown under `content/`; layouts and themed components are pulled in as Go modules — there is almost no template code in this repo, only config and content.

## Common commands

Use **pnpm** (the lockfile is `pnpm-lock.yaml`; `package-lock.json` is also present but pnpm is the declared `packageManager`).

- `pnpm install` — install JS deps (Tailwind, Pagefind, Preact)
- `pnpm dev` — run Hugo dev server at http://localhost:1313 with `--disableFastRender` (rebuilds on every save; needed because of how blocks/partials are mounted)
- `pnpm build` — production build (`hugo --minify`) followed by Pagefind indexing of `public/`
- `pnpm pagefind` — re-index search only (assumes `public/` already exists)

Hugo Extended **0.161.1** is the pinned version (`hugoblox.yaml`, `netlify.toml`). Go 1.21+ is needed for module fetching.

## Architecture

### Hugo Modules supply almost everything

`config/_default/module.yaml` imports three Go modules that provide all layouts, shortcodes, blocks, and CSS:
- `github.com/HugoBlox/kit/modules/blox` — page block system (resume biography, collection, markdown, cta-card, etc.)
- `github.com/HugoBlox/kit/modules/slides` — reveal.js slide rendering
- `github.com/HugoBlox/kit/modules/integrations/netlify`

Layouts in this repo (`layouts/_partials/hooks/head-end`) are *overrides* — they extend the modules. To find where a block/partial is actually defined, look in `~/go/pkg/mod/github.com/!hugo!blox/...` (or `go mod download` first), not in this repo.

The `mounts:` section in `module.yaml` does some unusual remapping — community blox HTML lands at `layouts/_partials/blox/community/` and CSS at `assets/dist/community/blox/`. When customizing a block, mirror that structure.

### Content model

- `content/_index.md` — homepage; configured as a stack of **blocks** (`block: resume-biography-3`, `block: markdown`, `block: collection`). Each block's schema is defined in the `blox` module.
- `data/authors/me.yaml` (data) + `content/authors/_index.md` — the author profile referenced by `username: me` in the homepage biography block. The data file is the **single source of truth** for bio, education, experience, skills, awards, languages — the experience timeline on `/experience/` and the homepage education/work-history blocks all read from it. Author pages themselves are gated off via `build.render: never`.
- `content/publications/`, `content/events/`, `content/projects/`, `content/blog/` — content sections. The Featured Publications, Recent Talks, and Recent News collection blocks on the homepage filter these via `filters.folders`.
- `content/publications/` is **regenerated** from `publications.bib` at the repo root. The repo wires up `.github/workflows/import-publications.yml` which runs `academic import publications.bib content/publications/ --compact --verbose` on push and opens a PR. Locally, the same one-liner can be run after installing `academic` (`pip install academic`).
  - **Hand-edits to publications under `content/publications/` will be overwritten** by the next bib re-import unless you also update the `.bib` and re-run with `--overwrite`. The flagship 5-card featured papers under `content/publications/` are hand-augmented with `featured: true`, plain-English summaries, and `projects:` cross-link fields — those edits are intentional and only survive a re-import if you re-apply them or omit the matching entries from the `.bib`.
  - The bib file uses `keywords = "featured"` to mark featured papers; the `academic` CLI translates this to `tags: [featured]` in the imported markdown but **does not** set the dedicated `featured: true` field that the `Featured Publications` block filters on. Setting `featured: true` is part of the post-import hand-augment step.
- `content/projects/` — research-theme hubs. Each project page bundles related publications under a plain-English narrative; the Featured Publications block on the homepage cross-links into these via the `projects:` field on individual publication pages, and the project pages themselves link out to the underlying `/publications/<slug>/`.
- `content/blog/` — used as a lightweight news feed (homepage section title is "Recent News"). Personal updates and press/media items live here; press items carry `tag: press` and surface at `/tags/press/`.
- `content/events/` — talks. Per-folder, with minimal frontmatter; `featured: true` lifts a talk into the homepage Recent Talks card stack.
- `static/uploads/` — files served verbatim (e.g., `cv_Farren.pdf` referenced from the homepage button). The PhD thesis is linked from the education section to the Cambridge Apollo repository (`https://doi.org/10.17863/cam.112076`), not bundled in this repo.

### Site config

Split across `config/_default/`:
- `hugo.yaml` — Hugo core, taxonomies, output formats, module imports/mounts
- `params.yaml` — site-wide params (branding, theme, social, search). The site `title` lives here under `hugoblox.branding.name`, not in `hugo.yaml`.
- `menus.yaml`, `languages.yaml`

Slides are rendered by cascading an extra `present` output: any page under `/slides/**` gets `outputs: [HTML, present]`.

### Search

Pagefind indexes the built `public/` directory after Hugo runs. `static/pagefind/` and `pagefind/` are gitignored — they only exist after a build.

## Deployment

`hugoblox.yaml` declares `deploy.host: github-pages`, but `netlify.toml` is also wired up with separate build commands for production, deploy-preview, and branch-deploy contexts. Production builds set `HUGO_ENV=production`; previews/branches use `$DEPLOY_PRIME_URL` as the base URL. The Netlify build always passes `--no-frozen-lockfile` to pnpm.

GitHub Actions in `.github/workflows/`:
- `build.yml` / `deploy.yml` — site CI/CD
- `import-publications.yml` — fires on push to `publications.bib`, runs `academic import`, and opens a PR with regenerated `content/publications/`. **Don't commit hand-edited publication pages alongside `.bib` changes** — the action will create a competing PR.
- `upgrade.yml`, `internal-readme-news.yml` — template upkeep (likely not relevant for content edits)

## Editing tips specific to this template

- When changing the homepage, edit blocks in `content/_index.md` — don't reach for a layout file. The `block:` field maps to a partial in the `blox` module.
- The HugoBlox `Featured Publications` collection block uses `featured_only: true` which filters on `featured: true` in page frontmatter (NOT on `tags: [featured]`). After running a fresh BibTeX import, re-apply `featured: true` to the chosen flagship pages.
- URL pattern for content links: section is plural (`/publications/<slug>/`, `/projects/<slug>/`, `/blog/<slug>/`, `/events/<slug>/`). The HugoBlox examples sometimes show singular (`/publication/<slug>/`) — that's wrong on this template.
- After changing `module.yaml` or bumping module versions in `go.mod`, run `hugo mod get -u` and `hugo mod tidy`.

## How to refresh publications

1. Pull the latest BibTeX from Inspire-HEP (BAI `Gerrit.S.Farren.1`):
   ```
   curl -LH "Accept: application/x-bibtex" \
     "https://inspirehep.net/api/literature?q=a+Gerrit.S.Farren.1&size=100&sort=mostrecent" \
     > publications.bib
   ```
2. Append the ALMA paper (arXiv:2102.05079) which is missing from Inspire's BAI listing — its BibTeX is preserved at the bottom of the existing `publications.bib`. Copy that block.
3. Drop unwanted entries (Snowmass whitepapers, the PhD thesis) from `publications.bib`.
4. Tag flagship papers with `keywords = "featured"`.
5. Run `academic import publications.bib content/publications/ --compact --overwrite`.
6. Re-apply `featured: true`, plain-English summaries, and `projects:` fields to the flagship pages.
