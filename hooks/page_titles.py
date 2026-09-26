"""Set page.meta["title"] from the page H1 when the frontmatter has none.

Why: the site navigation uses short labels ("ASTA", "Powder - Premium"). MkDocs adopts
those as page.title, so <title> and JSON-LD headline/DefinedTerm ended up as nav labels
rather than real page titles. This hook derives the title from the document's first H1
(which is what a reader actually sees), without editing 90+ content files.
"""

import re

_H1 = re.compile(r"(?m)^#\s+(.+?)\s*$")
_MD = [(re.compile(r"\*\*(.+?)\*\*"), r"\1"), (re.compile(r"\*(.+?)\*"), r"\1"),
       (re.compile(r"`(.+?)`"), r"\1"), (re.compile(r"\[([^\]]+)\]\([^)]+\)"), r"\1")]


def on_page_markdown(markdown, page, config, files):
    meta = page.meta if isinstance(page.meta, dict) else {}
    if not meta.get("title"):
        m = _H1.search(markdown)
        if m:
            title = m.group(1)
            for pat, rep in _MD:
                title = pat.sub(rep, title)
            title = re.sub(r"\s+", " ", title).strip()
            if title:
                page.meta["title"] = title
    return markdown
