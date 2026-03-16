"""
Converts all .md blog posts in content/ to WordPress-ready HTML files.
Output goes to content/wordpress/

Each output file contains:
  - Post title
  - Yoast/RankMath SEO fields (meta title, meta description, focus keyword)
  - Clean HTML body to paste into WordPress editor
"""

import re
from pathlib import Path
import markdown

CONTENT_DIR = Path(__file__).parent / "content"
OUTPUT_DIR  = CONTENT_DIR / "wordpress"
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_meta(text: str) -> dict:
    """Pull structured header fields from the top of the .md file."""
    meta = {}
    patterns = {
        "meta_title":       r"\*\*Meta Title:\*\*\s*(.+)",
        "meta_description": r"\*\*Meta Description:\*\*\s*(.+)",
        "target_keyword":   r"\*\*Target Keyword:\*\*\s*(.+)",
        "secondary_keywords": r"\*\*Secondary Keywords:\*\*\s*(.+)",
        "word_count":       r"\*\*Word Count:\*\*\s*(.+)",
        "internal_links":   r"\*\*Internal Links:\*\*\s*(.+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        meta[key] = match.group(1).strip() if match else ""
    return meta

def strip_metadata_block(text: str) -> str:
    """Remove the metadata header block and the --- separators below it."""
    # Remove lines starting with **Meta Title:**, **Meta Description:**, etc.
    lines = text.split("\n")
    cleaned = []
    skip_keys = ("**Meta Title:**", "**Meta Description:**", "**Target Keyword:**",
                 "**Secondary Keywords:**", "**Word Count:**", "**Internal Links:**")
    for line in lines:
        if any(line.strip().startswith(k) for k in skip_keys):
            continue
        cleaned.append(line)
    result = "\n".join(cleaned)
    # Remove leading --- separator after stripping meta block
    result = re.sub(r"^\s*---\s*\n", "", result, count=1)
    return result.strip()

def convert_file(md_path: Path):
    raw = md_path.read_text(encoding="utf-8")

    meta  = extract_meta(raw)
    body  = strip_metadata_block(raw)

    # Extract H1 title (first # heading)
    title_match = re.match(r"^#\s+(.+)", body, re.MULTILINE)
    post_title  = title_match.group(1).strip() if title_match else md_path.stem

    # Remove the H1 from body (WordPress uses Post Title field separately)
    body_no_h1 = re.sub(r"^#\s+.+\n?", "", body, count=1).strip()

    # Convert markdown to HTML
    html_body = markdown.markdown(body_no_h1, extensions=["extra", "nl2br"])

    # Build output file
    output = f"""<!-- ============================================================
  WORDPRESS POST — {post_title}
  ============================================================

  POST TITLE (WordPress "Title" field):
  {post_title}

  SEO PLUGIN FIELDS (Yoast or RankMath):
    Focus Keyword : {meta.get('target_keyword', '')}
    SEO Title     : {meta.get('meta_title', '')}
    Meta Desc     : {meta.get('meta_description', '')}
    Secondary KWs : {meta.get('secondary_keywords', '')}

  INTERNAL LINKS TO ADD:
    {meta.get('internal_links', '')}

  HOW TO USE:
    1. Create new post in WordPress
    2. Paste the POST TITLE above into the Title field
    3. Switch editor to "Code Editor" (or Text tab in Classic Editor)
    4. Paste the HTML block below into the content area
    5. Fill in the SEO plugin fields above
    6. Add featured image and publish
  ============================================================ -->

<!-- PASTE THIS INTO THE WORDPRESS CONTENT AREA (Code/HTML view) -->

{html_body}
"""

    out_path = OUTPUT_DIR / (md_path.stem + ".html")
    out_path.write_text(output, encoding="utf-8")
    print(f"  ✓ {out_path.name}")

def main():
    md_files = sorted(CONTENT_DIR.glob("*.md"))
    print(f"Converting {len(md_files)} posts...\n")
    for f in md_files:
        convert_file(f)
    print(f"\nDone. Files saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
