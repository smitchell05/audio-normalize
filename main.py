"""Audio Normalize — Normalize peak or loudness of wav and mp3 files in a folder."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='audio_normalize',
        description='Normalize peak or loudness of wav and mp3 files in a folder.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Audio Normalize')
    print('Even volume across a voice folder.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
