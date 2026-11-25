#!/usr/bin/env python3
"""One-line fortune-cookie entry for make.fun bounty
u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.

Writes a single fortune-cookie line (<=20 words, <=160 chars) for a
crypto trader who has just been liquidated.
Stdlib only, deterministic, no network.
"""
import os

ENTRY = "A great fortune awaits you — unfortunately, it is currently in someone else's wallet."


def main():
    for base in ("/output", "./output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            print(f"Wrote {path} ({len(ENTRY)} chars, {len(ENTRY.split())} words)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
