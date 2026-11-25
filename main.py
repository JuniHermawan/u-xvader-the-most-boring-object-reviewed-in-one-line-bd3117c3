#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single funny, true one-line review of the dullest everyday
object we could name -- a paperclip -- to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Stdlib only, deterministic, no network.
"""

import os
import sys

LINE = "This paperclip has held the same ten pages together since 2019. It deserves a pension, not a drawer."


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text:
        print("entry fails the gate: 1-200 chars, one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
