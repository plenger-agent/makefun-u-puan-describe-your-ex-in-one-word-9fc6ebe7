"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt.
The word: Unsubscribe.

Why this word: the brief wants one word that describes an ex, and the
strongest one-word answers are instantly relatable with no setup. Everyone
has hit "unsubscribe" on a mailing list they never asked to join — so the
ex becomes a subscription I opted out of. The joke lands the moment the
word is read, and it needs no punctuation, no second word, no explanation.
"""

import os

WORD = "Unsubscribe"  # the ex, summed up: a subscription I opted out of.

# Gate: entry.txt must be UTF-8 text of 1 to 111 chars, not only whitespace.
MIN_CHARS, MAX_CHARS = 1, 111


def main():
    if not (MIN_CHARS <= len(WORD) <= MAX_CHARS):
        raise SystemExit("word must be 1-111 chars")
    # Exactly one word: no whitespace anywhere, and letters only — so a
    # punctuation or digit trick ("Hello!", "abc123") can never slip through
    # as a "word". The brief asks for one word, not one token.
    if any(ch.isspace() for ch in WORD) or not WORD.isalpha():
        raise SystemExit("entry must be exactly one alphabetic word")
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
