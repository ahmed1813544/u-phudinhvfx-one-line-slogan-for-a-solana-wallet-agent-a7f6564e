#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single slogan (one line, at most twenty words) to
/output/entry.txt. Stdlib only, deterministic: the same bytes every run.

The slogan is 18 words / 96 characters: inside the gate (1-140 chars,
at most 20 words, one line). It names the wallet, turns a fresh image
(a morning paper, coffee cooling) instead of a stock crypto line, and
says the promise plainly: the wallet reads the market and moves your
SOL before you finish your coffee.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    slogan = (
        "A wallet that reads the market like a morning paper and moves "
        "your SOL before your coffee cools."
    )
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(slogan + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
