#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single slogan (one line, at most twenty words) to
/output/entry.txt. Stdlib only, deterministic: the same bytes every run.

The slogan is 15 words / 94 characters: inside the gate (1-140 chars,
at most 20 words, one line). It names the wallet's job plainly and turns
a fresh image — a night-shift gardener tending coins like plants —
instead of a stock crypto line: the agent works the chain while you
sleep, pruning, planting and harvesting your SOL. The line is one
sentence, one line, no trailing spaces.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    slogan = (
        "Your SOL's night-shift gardener: it prunes, plants, and "
        "harvests on the chain while you sleep."
    )
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(slogan + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
