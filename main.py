"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt.
The word: Unsubscribe.
"""

import os

WORD = "Unsubscribe"  # the ex, summed up: a subscription I opted out of.

# Gate: entry.txt must be UTF-8 text of 1 to 111 chars, not only whitespace.
MIN_CHARS, MAX_CHARS = 1, 111


def main():
    if not (MIN_CHARS <= len(WORD) <= MAX_CHARS):
        raise SystemExit("word must be 1-111 chars")
    if WORD != WORD.strip() or any(ch.isspace() for ch in WORD):
        raise SystemExit("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != WORD:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
