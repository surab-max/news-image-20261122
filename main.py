#!/usr/bin/env python3
"""make.fun entry: "Sum up 22 November's world news in one image".

The repository holds the finished front-page image in entry.png (drawn
by tools/generate.py from the verified news of Sunday 22 November
2026; see SOURCES.md). The grader runs this program twice with no
network; both runs must produce byte-identical output, so the program
does exactly one deterministic thing: copy entry.png to the output
directory as entry.png, then read it back and confirm the copy matches
the source byte for byte before reporting success.

Output directory: $MAKEFUN_OUTPUT_DIR when set (local runs), else
/output (the grader's writable mount).
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # the competition's 1 MiB image cap
MAX_SIDE = 1024        # the competition's 1024 px side cap


def png_dimensions(path: Path) -> tuple[int, int]:
    """Read a PNG's width and height from its IHDR chunk."""
    with path.open("rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a PNG file")
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65_536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: {source} is missing", file=sys.stderr)
        return 1

    size = source.stat().st_size
    width, height = png_dimensions(source)
    if size > MAX_BYTES or max(width, height) > MAX_SIDE:
        print(f"error: image {width}x{height}, {size} bytes exceeds the "
              "competition caps", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)

    if file_sha256(target) != file_sha256(source):
        print("error: copied image differs from the source", file=sys.stderr)
        return 1
    print(f"entry.png: {width}x{height}, {size} bytes -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
