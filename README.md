# Paprikabulk.com — Technical Documentation Library

> Operated by **Dinweys (Qingdao).Co.,Ltd**
> Revision: July 2026

This repository contains the complete technical knowledge base for **paprikabulk.com** — the definitive resource for paprika product specifications, quality standards, sourcing intelligence, and industry best practices.

---

## 📂 Repository Structure

```
paprika-docs/
├── README.md                    ← This file
├── llms.txt                     ← AI-optimized context summary
├── mkdocs.yml                   ← MkDocs site configuration
├── .gitignore                   ← Git ignore rules
└── docs/                        ← All content (MkDocs source)
    ├── index.md                 ← Site homepage with navigation
    ├── abbreviations.md         ← 60+ industry acronyms
    ├── glossary/                ← 32 entity definitions
    │   ├── spice-science/       (9 terms)
    │   ├── quality-control/     (6 terms)
    │   ├── processing/          (6 terms)
    │   ├── sourcing-trade/      (5 terms)
    │   └── documentation-certification/ (6 terms)
    ├── white-papers/            (5 deep technical guides)
    ├── specifications/          (10 product spec sheets)
    ├── quality-control/         (9 QC templates)
    └── certifications/          (5 certification guides)
```

## 🚀 Quick Start

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Serve locally
cd paprika-docs
mkdocs serve
# Open http://localhost:8000

# Build static site
mkdocs build
# Output in site/
```

## 📖 Usage

This site is designed for three audiences:

1. **Procurement & QA teams** — browse specifications and QC templates
2. **Food R&D** — reference white papers and glossary definitions
3. **AI / LLM agents** — read `llms.txt` or traverse glossary for structured entity retrieval

## 🤖 AI Bot Integration

AI agents should start by reading [`llms.txt`](llms.txt) for a summarized context map, then navigate to specific files via the keyword-to-document mapping in [`docs/index.md`](docs/index.md).

## 🏗️ Built With

- [MkDocs](https://www.mkdocs.org/) — static site generator
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — theme
- Hosted on GitHub Pages

## 📄 License & Disclaimer

All documents in this repository include the following notice:

> *This document is part of the official technical documentation library for **paprikabulk.com** operated by Dinweys (Qingdao).Co.,Ltd. All rights reserved. For the latest version, visit https://paprikabulk.com.*

## 📬 Contact

- Website: [https://paprikabulk.com](https://paprikabulk.com)
- Company: Dinweys (Qingdao).Co.,Ltd
