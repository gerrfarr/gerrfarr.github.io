#!/usr/bin/env python3
"""Fail when a publication selected by the CV is absent from the shared BibTeX."""

from pathlib import Path
import re
import sys

cv_dir = Path(__file__).resolve().parent
tex = (cv_dir / "cv.tex").read_text(encoding="utf-8")
bib = (cv_dir.parent / "publications.bib").read_text(encoding="utf-8")

bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib))
selected_groups = re.findall(r"\\addtocategory\{[^}]+\}\{([^}]+)\}", tex)
selected_keys = {
    key.strip()
    for group in selected_groups
    for key in group.split(",")
    if key.strip()
}

missing = sorted(selected_keys - bib_keys)
if missing:
    print("CV publication keys missing from ../publications.bib:", file=sys.stderr)
    for key in missing:
        print(f"  - {key}", file=sys.stderr)
    raise SystemExit(1)

print(f"OK: all {len(selected_keys)} selected CV publications use ../publications.bib")
