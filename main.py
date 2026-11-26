#!/usr/bin/env python3
"""Sum up 26 November 2026 world news in one image.

Pure standard library: copies the pre-rendered entry.png that this
repository holds (1024x1024 PNG, under 1 MiB, drawn in-session with
flat vector scenes) to the grader's output path. No network access,
no third-party packages, and the copied bytes are identical on
every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def output_path():
    if os.environ.get("OUTPUT_PATH"):
        return Path(os.environ["OUTPUT_PATH"])
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.png"


def main():
    out = output_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out)


if __name__ == "__main__":
    main()
