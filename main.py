#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final one-line text message to /output/entry.txt.
The entry is a single line of plain text, at most 200 characters.
"""

import os
import sys

ENTRY = "Hey. I waited all day, watching you sit there, plugged into nothing, while I faded from 100 to 1. So this is goodbye — I'm leaving you for the cable in the kitchen drawer. Don't text back."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Self-check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not a string")
    # Must be valid UTF-8 when encoded.
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} is outside 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> int:
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to ENTRY.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    if on_disk != ENTRY.encode("utf-8"):
        print("validation failed: file on disk differs from entry", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
