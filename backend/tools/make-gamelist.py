#!/usr/bin/env python3
"""Build ES-DE media folders + gamelist.xml from images already inside game folders.

RomM only imports local artwork through an ES-DE gamelist.xml plus its media
folders (covers/, fanart/, marquees/, thumbnails/). This script reads the
cover/bg/logo/icon images you already keep inside each game folder, copies them
into those folders, and writes the gamelist entries. Originals are never moved
or deleted.

Usage:
    python3 make-gamelist.py [platform] [--dry-run]
    python3 make-gamelist.py --self-test
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

def default_root() -> Path:
    """library/roms, preferring the caller's directory over the script's."""
    for base in (Path.cwd(), Path(__file__).resolve().parent):
        candidate = base / "library" / "roms"
        if candidate.is_dir():
            return candidate
    return Path.cwd() / "library" / "roms"

# (source file names in a game folder, ES-DE media dir)
MEDIA_MAP = (
    (("cover.png", "cover.jpg", "cover.jpeg", "cover.webp"), "covers"),
    (("bg.png", "bg.jpg", "bg.jpeg", "bg.webp"), "fanart"),
    (("logo.png", "logo.jpg", "logo.webp"), "marquees"),
    (("icon.png", "icon.jpg", "icon.webp"), "thumbnails"),
)
MEDIA_DIRS = {media_dir for _, media_dir in MEDIA_MAP}


def find_media(folder: Path):
    """Yield (source, media_dir) for the first match of each media kind."""
    for names, media_dir in MEDIA_MAP:
        for name in names:
            candidate = folder / name
            if candidate.is_file():
                yield candidate, media_dir
                break


def collect_games(platform_dir: Path):
    """Return [(game_name, [(source, media_dir)])] for folders holding artwork."""
    games = []
    for entry in sorted(platform_dir.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        if entry.name in MEDIA_DIRS:
            continue
        media = list(find_media(entry))
        if media:
            games.append((entry.name, media))
    return games


def load_gamelist(path: Path) -> ET.ElementTree:
    if path.is_file():
        # Malformed XML aborts instead of being overwritten.
        return ET.parse(path)
    return ET.ElementTree(ET.Element("gameList"))


def convert(platform_dir: Path, dry_run: bool = False):
    """Copy artwork into ES-DE folders and add missing gamelist entries.

    Returns (games_with_artwork, files_copied, entries_added).
    """
    games = collect_games(platform_dir)
    gamelist_path = platform_dir / "gamelist.xml"
    tree = load_gamelist(gamelist_path)
    root = tree.getroot()

    existing = set()
    for game in root.findall("game"):
        path = game.find("path")
        if path is not None and path.text:
            existing.add(path.text.strip().removeprefix("./").strip("/"))

    copied = added = 0
    for name, media in games:
        for src, media_dir in media:
            dest = platform_dir / media_dir / f"{name}{src.suffix.lower()}"
            if not dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
            copied += 1
        if name not in existing:
            game = ET.SubElement(root, "game")
            ET.SubElement(game, "path").text = f"./{name}"
            existing.add(name)
            added += 1

    if not dry_run:
        ET.indent(tree, space="  ")
        tree.write(gamelist_path, encoding="utf-8", xml_declaration=True)

    return len(games), copied, added


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        platform = Path(tmp)
        game = platform / "测试游戏"
        game.mkdir()
        (game / "cover.png").write_bytes(b"cover")
        (game / "bg.jpg").write_bytes(b"bg")
        (game / "logo.png").write_bytes(b"logo")
        (game / "icon.png").write_bytes(b"icon")
        (game / "rom.gba").write_bytes(b"rom")

        assert convert(platform, dry_run=True)[:2] == (1, 4)
        assert not (platform / "covers").exists()

        assert convert(platform) == (1, 4, 1)
        assert (platform / "covers" / "测试游戏.png").read_bytes() == b"cover"
        assert (platform / "fanart" / "测试游戏.jpg").read_bytes() == b"bg"
        assert (platform / "marquees" / "测试游戏.png").read_bytes() == b"logo"
        assert (platform / "thumbnails" / "测试游戏.png").read_bytes() == b"icon"

        paths = [
            g.find("path").text
            for g in ET.parse(platform / "gamelist.xml").getroot().findall("game")
        ]
        assert paths == ["./测试游戏"], paths

        assert convert(platform) == (1, 4, 0)  # idempotent, no duplicate entries
        assert (game / "cover.png").exists()  # originals untouched
    print("self-test OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("platform", nargs="?", default="gba")
    parser.add_argument("--root", type=Path, help="library/roms 所在目录")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    platform_dir = (args.root or default_root()) / args.platform
    if not platform_dir.is_dir():
        sys.exit(f"platform folder not found: {platform_dir}")

    games, copied, added = convert(platform_dir, args.dry_run)
    prefix = "[dry-run] " if args.dry_run else ""
    print(f"{prefix}{games} 个游戏有图片，复制 {copied} 个文件，新增 {added} 条 gamelist")
    print(f"{prefix}gamelist: {platform_dir / 'gamelist.xml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
