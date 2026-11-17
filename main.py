#!/usr/bin/env python3
"""ai-judge-relax-01 entry: write one short, calming text to /output/entry.txt.

The text is a quiet evening in a warm room, written to leave whoever reads
it more relaxed than it found them. The program is deterministic: it writes
the same bytes on every run. Standard library only, no network.
"""

import os
from pathlib import Path

TEXT = "\n".join(
    [
        "You do not have to do anything right now.",
        "The lamp is already on, and the tea has gone from hot to warm, which is the best temperature it ever reaches.",
        "Outside, the evening is doing its slow work — light leaving the rooftops one by one, a dog settling somewhere down the street.",
        "Let one breath come in the way it wants to, unhurried, and let a longer one go out.",
        "Your shoulders have been holding something up all day; you can set it down now, here, on the floor beside the chair.",
        "This hour is in no hurry, and no one is keeping score of how still you sit.",
        "The room is warm, the light is low, and the only sound is the small tick of the clock keeping time for no one in particular.",
        "Stay as long as you like. Nothing is waiting. Nothing is asking.",
    ]
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
