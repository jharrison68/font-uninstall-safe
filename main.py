"""Font Uninstall Safe — List user-installed fonts and remove selected ones after a preview."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='font_uninstall_safe',
        description='List user-installed fonts and remove selected ones after a preview.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Font Uninstall Safe')
    print('Drop a font you installed, not a system face.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
