#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of the worst possible AI advice
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)."""

import os

LINE = "To keep your passwords safe, email them to yourself \u2014 your inbox is basically a vault with a search bar."


def main():
    # Gate: exactly one line, 1-140 characters, non-whitespace only.
    if not (1 <= len(LINE) <= 140):
        raise SystemExit("entry must be 1-140 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
