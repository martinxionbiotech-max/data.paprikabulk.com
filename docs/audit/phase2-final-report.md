---
title: Phase 2 Repair — Final Report
description: What was fixed, optimised, merged and left open on the PaprikaBulk Data Hub after the Phase 2 repair pass — with verification results and next-phase recommendations.
category: Audit
datePublished: 2026-09-26
dateModified: 2026-09-26
---

# PaprikaBulk Data Hub — Phase 2 Final Report

**Scope:** `https://data.paprikabulk.com/` only. **The main site `https://paprikabulk.com/` was not modified at any point** (read-only fetches for verification only).
**Working repository:** `data.paprikabulk.com` (confirmed as the live deployment source — see the audit report §0).
**Phase sequence executed:** Audit → Fix → Verify → Strengthen.

---

## 1. 已修复（Fixed）

### 1.1 Factual and standards accuracy

| # | Issue | Fix |
|---|---|---|
| 1 | **"ASTM 20.1"** used for the colour value (`regulatory/shelf-life.md`) | Corrected to **ASTA 20.1** — ASTA and ASTM are different organisations with different scopes |
| 2 | **"estimate ASTM loss"** in a container-damage workflow | Corrected to **ASTA** loss |
| 3 | **ASTM D4914** cited for dried-product moisture (a soil/rock in-place density standard) | Removed; replaced with **ISO 939** (spices moisture) and **ISO 972:1997** |
| 4 | Physically impossible value "Water Content (dry basis) 400–567%" | Rewritten as an equivalent wet/dry-basis statement (≤ 12.5% db ≈ ≤ 11.1% wb) |
| 5 | **ASTM B213** (flow rate of *metal* powders) cited for paprika powder flowability | Replaced with the neutral method description "Hall flowmeter method (fixed-height funnel)" |
| 6 | **ASTM D6166** (Gardner colour of *naval stores*) cited for paprika colour/extraction | Replaced with **ISO 7541:2020** where a standard citation is needed |
| 7 | **ASTM E1083** labelled "(historical)" | Corrected to **ASTM E1083-00(2017)** — an active standard, not historical |
| 8 | **ISO 7541:1989** presented as the current colour standard | Sitewide: **ISO 7541:2020** is the current edition; **ISO 7541:1989 is withdrawn** (verified in the ISO catalogue). Historical references now carry the withdrawal note |

### 1.2 Unsupported certification claims (all reframed, none fabricated, none silently deleted)

| Location | Was | Now |
|---|---|---|
| `glossary/.../haccp.md` | "Our facility is certified under **FSSC 22000 Version 6** (GFSI recognized) and **ISO 9001:2015**" | Scheme description retained; certification scope and current certificate details stated as **provided on request and confirmed per order** |
| `glossary/.../kosher.md` | "Dinweys' paprika processing facility is **certified by the Orthodox Union (OU)**" | Kosher supply described as **order-dependent**, with the agency/number/validity **confirmed in writing per order** and a note to verify the agency named on the certificate |
| `about/index.md` | "HACCP, ISO, Kosher, Organic and Gluten-Free **certified quality systems**"; "ISO 9001/22000/14001 integrated management system records" | Reframed to programmes aligned with those standards, with **certificate scope and validity provided on request** |
| `products/index.md` | "HACCP Certified ✅ / Kosher Certified ✅" | Replaced with "documentation provided on request; verified per order" |
| `case-studies/salmonella-…md` | "FSSC 22000 certified, audit dated June 2025" | "third-party audited food-safety system (current certificate details on request)" |
| `specifications/…/premium-grade.md` | "guaranteed EU MRL compliant" | "tested against EU MRL requirements; per-batch compliance confirmed on the COA" |
| `glossary/processing/blending.md` | "We maintain a diverse inventory …" | "…**subject to availability** at the time of order" |

**BRCGS:** zero occurrences sitewide — correctly absent.

### 1.3 Structured data

| Issue | Fix |
|---|---|
| **FAQPage markup did not match the visible page** (`faq/procurement-faq.md`): schema asked *"Why did my paprika arrive with lower ASTA color value…"* while the page visibly asked *"My lab says ASTA 75 but your COA says ASTA 90 — which is correct?"* | `faq_json` **regenerated from the visible Q&A text** — verified **10/10 questions match the on-page questions** in the built output |
| Two pages declared `schema_type: FAQPage` with **no visible Q&A** (`faq/index.md`, `templates/faq-template.md`) | Declaration removed (no invented FAQ markup) |
| `dateModified`/`datePublished` hardcoded to the same values for **every** page | Now taken from each page's frontmatter, with fallback |
| **`sameAs` pointed to a 404** (`github.com/dinweys/paprika-docs`) — also used in the footer and About/Resources pages | Corrected to the real repository; verified the old target returns 404 |
| Missing page-type-appropriate schema | Added **BreadcrumbList** (all 110 pages), **DefinedTerm + DefinedTermSet** (32 glossary pages), **Dataset** (datasets page) |
| **Page titles were navigation labels** — `<title>` read "Asta", "Powder - Premium" | A MkDocs hook now derives the title from each page's H1; `<title>` and schema `headline` render real titles (e.g. "ASTA Color Value", "Paprika Powder — Premium Grade Specification"). Title suffix shortened to `| Paprikabulk Data Hub` |

### 1.4 Content and QA

| Issue | Fix |
|---|---|
| Footer carried **"Research Use Only Documentation"** — a research-chemical disclaimer inappropriate for a food/spice site | Replaced with a food-appropriate statement (information only; product supplied to specification; verify certificates and requirements per order) |
| 16 placeholder links rendering as broken links inside `templates/` | Converted to inline code (no longer links) |
| 5 broken internal links (incl. a link to a `/methodology/` page that does not exist on the Data Hub) | Fixed; **internal .md dead links now 0** |
| Overclaim sweep (`flawless`, `guaranteed`, `zero risk`, `best-in-class`, `industry-leading`, `perfect safety`, `world-class`) | All removed or replaced with tested / documented / specified / verified / batch-specific phrasing |
| 8 substantive claims with no source chain | Now registered in the new Claims Register with status and review date |

---

## 2. 已优化（Optimised）

- **Evidence Layer created:** `/evidence/`, `/claims/` (10 topic areas: company data, product specification, ASTA, COA, testing, certifications, food safety, regulatory, supplier audit, traceability), `/sources/` (ISO, ASTM, ASTA, AOAC, Codex, EU, FDA, ESA, GB with identifiers and direct links to the issuing body). Every row carries **Claim → Source → Status → Last reviewed**.
- **`/audit/human-verification-required.md` created:** 12 open items with what would close each one. Nothing in it is asserted as fact on the site.
- **Navigation:** new Evidence group added; homepage links to the three registers.
- **robots.txt:** `Disallow: /audit/` added (audit reports stay out of the index; `/evidence/`, `/claims/`, `/sources/` remain crawlable). Existing AI-crawler allowances retained.
- **Entity graph clarified:** Paprika → ASTA → ISO 7541 → COA → Testing → Quality → Supplier Audit → Regulatory → Procurement is now expressed through DefinedTerm, BreadcrumbList and the Sources register.

---

## 3. 合并 / 删除的重复内容

**Nothing was merged or deleted.** The similarity scan found exactly one pair above threshold:

| Pair | Similarity | Decision |
|---|---|---|
| `specifications/paprika-powder/premium-grade.md` ↔ `superior-grade.md` | 0.745 | **Kept both** — the tables share a skeleton but the parameters differ substantively: ASTA 160–200 vs 120–160; pungency ≤500 vs ≤1,000 SHU; shelf life 18 vs 15 months; different packaging options and intended markets. Merging would destroy grade-specific data. |

All other page pairs scored below the duplicate threshold.

---

## 4. 仍需人工确认

Full list in `/audit/human-verification-required.md`. Headline items:

1. **Certification holdings** — which schemes are actually held, by which bodies, scope and expiry (nothing is published until supplied).
2. **Annual capacity (MT/year)** — a capacity figure exists on the commercial site ("4,500 metric tons"); the "5,000+ MT/year" variant circulating was **not found on the Data Hub, on market.paprikabulk.com, or in the main-site page fetched**. The Data Hub now states **no capacity figure at all**.
3. Facility address and registered legal name (footer reads "Dinweys (Qingdao).Co.,Ltd").
4. Laboratory arrangements and ISO/IEC 17025 scope for any named laboratory.
5. Insurance / after-sales scope and default commercial terms per order.

---

## 5. 下一阶段建议

1. **Publish the certificate register** once holdings are confirmed — this is the single highest-leverage E-E-A-T item remaining.
2. **FAQ markup rollout:** 54 pages contain visible Q&A blocks but no markup. Extend the FAQPage treatment to those pages **only** where the Q&A is genuinely page-specific, generating `faq_json` from visible text with the same 10/10 verification used here.
3. **Nav orphan review:** 33 pages (mostly glossary children) are not in the nav; confirm each is reachable from its hub, then decide deliberately (promote or leave).
4. **Market-figure attribution:** older pages quote regional production volumes and trade statistics without per-figure citations; add source + date rows to the Claims Register.
5. **Keep the two repositories from diverging:** `paprika-docs` is a near-copy of the live repository and would disable site search if it ever became the deployment source. Consolidate or archive it.
6. **Pin the build:** `requirements.txt` is unpinned; the live build runs mkdocs 1.6.1 + material 9.7.7. Pinning prevents a future plugin change from altering output silently.

---

## 6. Verification results (post-fix build)

| Check | Result |
|---|---|
| Build | 110 pages, no errors |
| Canonical | Present on **110/110** pages |
| JSON-LD parse errors | **0** |
| Schema distribution | Organization 110 · WebSite 110 · TechArticle 110 · BreadcrumbList 110 · DefinedTerm 32 · Dataset 1 · FAQPage 1 |
| FAQPage ↔ visible Q&A | **10/10 questions match** |
| Internal `.md` dead links | **0** |
| ASTM/ASTA mixups | 0 (excluding the two registers that explain the distinction) |
| Wrong standard editions | 0 (ISO 7541:1989 now always shown as withdrawn) |
| Unsupported certification claims | 0 |
| Overclaim language | 0 |
| Duplicate content | 1 pair reviewed, both retained with justification |
| Main site modified? | **No** |
