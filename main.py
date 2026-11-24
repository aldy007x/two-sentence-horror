#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network.
"""

import os
import sys

STORY = (
    "I labelled every jar in the pantry in my mother's handwriting "
    "so the kitchen would still feel like hers after she died. "
    "This morning I found a new jar on the shelf, labelled in that "
    "same handwriting, with my name on it."
)


def main() -> int:
    # Runtime self-check: exactly two sentences, 1-400 characters.
    # The story must be a single paragraph with no line breaks, and it
    # must end with a sentence terminator (no trailing whitespace).
    terminators = sum(STORY.count(c) for c in ".!?")
    if terminators != 2:
        print(f"error: expected exactly 2 sentence terminators, found {terminators}", file=sys.stderr)
        return 1
    if not 1 <= len(STORY) <= 400:
        print(f"error: story must be 1-400 characters, got {len(STORY)}", file=sys.stderr)
        return 1
    if "\n" in STORY or STORY != STORY.strip() or STORY[-1] not in ".!?":
        print("error: story must be a single trimmed paragraph ending in . ! or ?", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)
    print(f"wrote entry.txt ({len(STORY)} chars, {terminators} sentences)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
