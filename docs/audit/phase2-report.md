---
title: Phase 2 Repair — Audit Report
description: Full-site audit of the PaprikaBulk Data Hub (data.paprikabulk.com) — P0/P1/P2 findings on data conflicts, certifications, standards accuracy, schema, links, and SEO/GEO before repair.
category: Audit
---

# PaprikaBulk Data Hub — Phase 2 Audit Report

**Scope:** `https://data.paprikabulk.com/` only.
**Explicitly out of scope:** `https://paprikabulk.com/` (WordPress) — **not modified** at any point.
**Audit date:** 2026-09-26 ｜ **Audited artefact:** repository `data.paprikabulk.com` @ `efb3478` (verified as the live source — see §0).

---

## 0. Deployment-source verification (do this first, always)

Two repositories claim `site_url: https://data.paprikabulk.com/`: `data.paprikabulk.com` and `paprika-docs`. They hold **identical content (110 .md files, zero differences)** and differ only in `mkdocs.yml` (paprika-docs removes the `search` plugin) plus a committed `.venv` and removed GitHub Actions.

**Determination:** the live site **renders a search box**, so it cannot be built from `paprika-docs`. A local build of `data.paprikabulk.com` reproduces the live HTML fingerprint exactly (same JSON-LD type set, same head structure, `generator: mkdocs-1.6.1, mkdocs-material-9.7.7`).

→ **Live source = repo `data.paprikabulk.com`.** All repairs in this phase are committed there.
→ `paprika-docs` is a stale near-copy; it must not receive pushes or it will silently remove site search.

**Note (corrected during audit):** an initial scan appeared to show the `canonical` tag missing on every page. That was **a false positive** — the minify plugin reorders HTML attributes (`href="…" rel="canonical"`), which defeated the detection regex. Canonical output is present and correct on all pages. Recorded here so the finding is not carried forward.

---

## 1. Site inventory

| Area | Files | Notes |
|---|---:|---|
| `glossary/` | 33 | Spice Science / Quality Control / Processing / Sourcing & Trade / Documentation & Certification |
| `quality-control/` | 24 | Test methods, COA, allergen, container inspection |
| `specifications/` | 11 | Product grades (powder/flakes/whole) |
| `regulatory/` | 10 | EU / US / China / Codex / ESA / packaging / shelf-life |
| `certifications/` | 6 | HACCP, ISO, Kosher, Organic, Gluten-Free, index |
| `white-papers/` | 6 | Long-form guides |
| `case-studies/` | 4 | Real incident write-ups |
| `templates/` | 4 | Internal templates (see P1-6) |
| `faq/` | 2 | FAQ hub + procurement FAQ |
| root + single-page dirs | 8 | index, abbreviations, about, products, guides, research, resources, datasets |
| **Total** | **108** | |

---

## 2. P0 — Must fix

### P0-1. FAQ schema contradicts the visible page content (Google policy violation)
`faq/procurement-faq.md` (and `faq/index.md`) declare `schema_type: FAQPage` with a hand-written `faq_json` block. The schema questions **do not match the on-page questions**:

- **Schema:** "Why did my paprika arrive with lower ASTA color value than the COA stated?"
- **Visible:** "Q2: My lab says ASTA 75 but your COA says ASTA 90 — which is correct?"

Google requires FAQPage markup to reflect questions visibly present on the page. → Regenerate `faq_json` **from the visible Q&A text, verbatim**. Do the same for every page that carries FAQPage markup.

### P0-2. Unsupported company certification claims
The Data Hub asserts certifications the repository holds no evidence for:

| Location | Text | Problem |
|---|---|---|
| `about/index.md` | "HACCP, ISO, Kosher, Organic, and Gluten-Free **certified quality systems**" | Implies current holdings; no certificate, number, body, or expiry anywhere in the archive |
| `about/index.md` | "ISO 9001/22000/14001 integrated management system records" | Listed as available documentation; reads as a holding |
| `products/index.md` | "\| HACCP Certified \| Yes \|" | Absolute claim, no evidence |
| `products/index.md` | "\| Kosher Certified \| Yes \|" | Absolute claim, no evidence |

**Rule applied:** three categories must be separated — (1) certifications the company actually holds (needs certificate evidence), (2) certifications the market/industry requires, (3) general industry knowledge. Anything in category 1 without evidence is reframed as "documentation provided on request / subject to current certificate validity" and logged in `/audit/human-verification-required.md`.

No fabricated certificate numbers, bodies, or expiry dates are ever inserted.

### P0-3. Standards misattribution (technical accuracy)
| File:line | Current | Correct | Severity |
|---|---|---|---|
| `regulatory/shelf-life.md:142` | "ASTM 20.1 (ASTA)" | **ASTA Method 20.1** (ASTM is a different standards body) | P0 |
| `glossary/sourcing-trade/container-loading.md:128` | "estimate **ASTM** loss" | **ASTA** loss | P0 |
| `glossary/processing/drying.md:16,32` | moisture per "**ASTM D4914**" | ASTM D4914 = *in-place density of soil and rock* — unrelated to food moisture. Remove; cite ISO 972 / ISO 939 or an in-house method | P0 |
| `glossary/processing/drying.md:32` | "Water Content (dry basis) 400–567%" | Physically impossible as written; numeric error | P0 |

**Verified facts used above (ISO / ASTM catalogue + ASTA):**
- **ISO 7541:2020** — "Spices and condiments — Spectrophotometric determination of the extractable colour in paprika" — **current edition**.
- **ISO 7541:1989 [withdrawn; superseded by ISO 7541:2020]** — "Ground (powdered) paprika — Determination of total natural colouring matter content" — **historical; superseded by the 2020 edition**.
- **ASTA Method 20.1** — "Determination of Extractable Color in Capsicums and Their Oleoresins" (ASTA Analytical Methods Manual).
- **ASTM E1083-00(2017)** — "Sensory Evaluation of Heat in Ground Red Pepper (10,000–70,000 SHU)" — an **active** standard, not "historical".
- **ASTM D4914** — in-place density of soil/rock by sand replacement (**not a food method**).
- **ISO 972:1997** — "Chillies and capsicums, whole or ground (powdered) — Specification" — valid.
- **ISO 939** — moisture determination for spices — valid.

---

## 3. P1 — Should fix

### P1-1. Evidence layer absent
The site states many numbers, limits and costs with no claim→source chain. Build `/evidence/`, `/claims/`, `/sources/` so key data follows **Claim → Source → Status → Last reviewed**.

### P1-2. Human-verification list absent
Create `/audit/human-verification-required.md` for every claim that cannot be evidenced from the repository.

### P1-3. Hardcoded article dates in schema
`overrides/main.html` emits `dateModified: 2026-08-01` and `datePublished: 2026-01-15` for **every** page (lines 68–69), while the frontmatter carries real per-page dates. Replace with values from the page frontmatter so "last reviewed" is honest.

### P1-4. Organization `sameAs` points at a possibly-dead repo
`https://github.com/dinweys/paprika-docs` — the working repositories live under `martinxionbiotech-max`. Verify the org/repo exists before keeping the reference; a 404 in `sameAs` weakens the entity graph.

### P1-5. Footer carries a wrong disclaimer
The shared footer ends with **"Research Use Only Documentation"** — a research-chemical disclaimer left over from another project, inappropriate on a food/spice technical centre. Replace with a food-appropriate statement.

### P1-6. Placeholder links inside published templates
`templates/faq-template.md`, `product-template.md`, `technical-guide-template.md`, `white-paper-template.md` contain 16 links to placeholder paths (`path/to/doc.md`, `[paper-name].md`). They render as broken links. Convert to code spans (non-links) while keeping `/templates/` `Disallow` in robots.txt.

### P1-7. Structured-data coverage gaps (page-type-appropriate)
Present today: Organization, WebSite (+SearchAction), TechArticle, FAQPage (3 pages). Missing and requested by the phase brief:
- **BreadcrumbList** on all pages (Material exposes breadcrumbs; the graph should declare them).
- **DefinedTerm / DefinedTermSet** for glossary pages — the site's largest cluster with the clearest entity semantics.
- **Dataset** for the `/datasets/` page.

### P1-8. Overclaim language
Sweep for `flawless`, `guaranteed`, `zero risk`, `best-in-class`, `industry-leading`, `perfect safety`, `world-class`, `100%` and replace with `tested / documented / specified / verified / batch-specific / subject to specification / aligned with applicable requirements`.

### P1-9. Near-duplicate specification pages
`specifications/paprika-powder/premium-grade.md` ↔ `superior-grade.md` measured **0.745 similarity** (highest on the site; next pair well below threshold). Either differentiate with grade-specific data or merge.

### P1-10. Content with visible FAQ but no markup
**54 pages** carry question-and-answer blocks but no FAQPage markup; only 3 declare it, two of which currently mismatch their page (P0-1). Add markup **only** where the Q&A is genuinely visible and page-specific — no invented FAQs.

---

## 4. P2 — Later optimisation

1. **Nav orphans:** 33 pages (mostly `glossary/*/*.md` children) are not listed in `mkdocs.yml` nav. Verify each is reachable from its hub; promote or leave deliberately.
2. **hreflang:** site is English-only; no hreflang emitted (acceptable). If other-language hubs are added later, add `hreflang` + `x-default`.
3. **`/audit/` indexing:** audit reports should stay out of the index (`Disallow: /audit/` in robots.txt) while `/evidence/`, `/claims/`, `/sources/` stay crawlable.
4. **Entity graph page:** publish a short `/entity-graph/` page describing how Paprika → ASTA → ISO 7541 → COA → Testing → Supplier Audit → Regulatory → Procurement relate, for AI retrieval.
5. **Cost/price ranges** (audit fees, freight, testing costs) are presented as market ranges; ensure each is attributed in the Evidence Layer as *indicative, not quoted*.
6. **`templates/` in nav:** currently linked in navigation but blocked by robots. Decide: keep public (remove Disallow) or unlink.

---

## 5. Main-site consistency note (read-only; no modification made)

The user brief mentions a conflict "4,500 MT/year vs 5,000+ MT/year".

**Finding:** the Data Hub contains **no company capacity claim of either figure**. All `4,500` / `5,000` occurrences are buyer-scenario examples (e.g. "a buyer purchasing 500 MT/year") or regional production statistics (Xinjiang 450,000–550,000 MT; Inner Mongolia 300,000–400,000 MT/year).

The string **"4,500 metric tons"** does appear on the main site `paprikabulk.com` (read-only fetch). The conflicting "5,000+ MT/year" figure was not found on the Data Hub, on `market.paprikabulk.com`, or in the main-site page fetched. → Recorded as an open item in `/audit/human-verification-required.md`; **the main site is not modified**, and the Data Hub will state no capacity figure until the company confirms one.

---

## 6. Verified as healthy (no action)

| Check | Result |
|---|---|
| Canonical URL | Present and correct on all pages (minifier reorders attributes — verify with a tolerant check) |
| `robots.txt` | Sound: `Allow: /`, sitemap declared, `/templates/` + `/overrides/` + `/404.html` disallowed, AI crawlers (GPTBot, OAI-SearchBot, Claude-Web, PerplexityBot, Google-Extended, CCBot, Applebot-Extended, FacebookBot) explicitly allowed |
| Sitemap | `https://data.paprikabulk.com/sitemap.xml` — 104 URLs live |
| Duplicate content | Only one pair above similarity threshold (see P1-9) |
| Internal `.md` links | 16 broken, all inside `templates/` placeholders (P1-6); zero broken links in knowledge pages |
| Schema validity | All emitted JSON-LD blocks parse |
| BRCGS claims | **Zero occurrences** — correctly absent |

---

## 7. Execution plan for this phase

1. Fix P0-1 → regenerate FAQ schema from visible text (verbatim).
2. Fix P0-2 → reframe unsupported certification claims; log to human-verification.
3. Fix P0-3 → correct the four standards misattributions; mark ISO 7541:1989 [withdrawn; superseded by ISO 7541:2020] as historical and lead with ISO 7541:2020 sitewide.
4. Build the Evidence Layer (`/evidence/`, `/claims/`, `/sources/`) + `/audit/human-verification-required.md`.
5. P1 items: schema dates, footer disclaimer, `sameAs`, template links, BreadcrumbList, DefinedTerm, Dataset, overclaim sweep, duplicate spec review, real FAQ markup.
6. Re-scan → `/audit/phase2-final-report.md`.
