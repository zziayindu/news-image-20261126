#!/usr/bin/env python3
"""Hand the finished 26 November front page to the judging harness.

The picture itself was composed beforehand and lives in this repo as
entry.png. All this program does is place a copy of it where the harness
looks for the result, so the run needs nothing beyond the standard
library.
"""

import os
import sys
from pathlib import Path


def destination():
    """Return the full path the harness will read the image from."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    name = os.environ.get("OUTPUT_PATH") or "entry.png"
    return Path(folder) / name


def main():
    picture = Path(__file__).resolve().parent / "entry.png"
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    blob = picture.read_bytes()
    target.write_bytes(blob)
    print("delivered", target, "bytes:", len(blob))
    return 0


if __name__ == "__main__":
    sys.exit(main())
