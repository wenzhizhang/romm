"""The cover a folder game carries in its own folder, instead of the fetched one."""

from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest
from tests.handler.scan_stubs import add_n64_platform, add_rom, run_scan

from config.config_manager import config_manager as cm
from handler.filesystem.roms_handler import build_empty_fs_rom
from handler.metadata.libretro_handler import LibretroRom
from handler.scan.merge import apply_folder_game_cover, folder_game_cover
from handler.scan.sources import MetadataSource, ScanType
from models.platform import Platform
from models.rom import Rom, RomFile

FOLDER = "圣剑传说"
FILE = "Sword of Mana (USA).gba"
MATCH = LibretroRom(libretro_id="Sword of Mana (USA)", name="Sword of Mana")


@pytest.fixture
def folder_media_enabled():
    """Turn the strategy on without touching the config file."""
    enabled = SimpleNamespace(
        **(vars(cm.get_config()) | {"SCAN_FOLDER_GAME_MEDIA": True})
    )
    with patch.object(cm, "get_config", return_value=enabled):
        yield


def _file(folder_path: str, file_name: str) -> RomFile:
    return RomFile(
        rom_id=1,
        file_name=file_name,
        file_path=folder_path,
        file_size_bytes=1024,
        category=None,
    )


def add_folder_rom() -> tuple[Platform, Rom, list[RomFile], str]:
    platform = add_n64_platform()
    rom = add_rom(platform, FOLDER, FOLDER)
    folder_path = f"{rom.fs_path}/{rom.fs_name}"
    files = [
        _file(folder_path, FILE),
        _file(folder_path, "cover.png"),
        _file(folder_path, "bg.jpg"),
        _file(folder_path, "cover_w.png"),
    ]
    return platform, rom, files, folder_path


def test_the_folder_cover_is_found_by_name():
    _, _, files, folder_path = add_folder_rom()

    assert folder_game_cover(files, folder_path) == (f"file://{folder_path}/cover.png")


def test_only_images_directly_in_the_folder_count():
    _, _, files, folder_path = add_folder_rom()
    files += [
        _file(folder_path, "cover.txt"),
        _file(f"{folder_path}/data", "cover.png"),
    ]

    assert folder_game_cover(files, folder_path) == (f"file://{folder_path}/cover.png")


async def test_the_folder_cover_is_the_rom_cover(folder_media_enabled):
    platform, rom, files, folder_path = add_folder_rom()

    with patch(
        "handler.scan.lookups.meta_libretro_handler.get_rom",
        new=AsyncMock(return_value=MATCH),
    ):
        result = await run_scan(
            platform,
            rom,
            scan_type=ScanType.COMPLETE,
            metadata_sources=[MetadataSource.LIBRETRO],
            flat=False,
            files=files,
        )

    assert result.url_cover == f"file://{folder_path}/cover.png"


async def test_the_strategy_is_off_by_default():
    platform, rom, files, _ = add_folder_rom()

    with patch(
        "handler.scan.lookups.meta_libretro_handler.get_rom",
        new=AsyncMock(return_value=MATCH),
    ):
        result = await run_scan(
            platform,
            rom,
            scan_type=ScanType.COMPLETE,
            metadata_sources=[MetadataSource.LIBRETRO],
            flat=False,
            files=files,
        )

    assert not result.url_cover


def test_the_fetched_artwork_is_left_alone(folder_media_enabled):
    """What a provider already delivered stays recorded, so it is not fetched again."""
    fs_rom = build_empty_fs_rom(FOLDER, "n64", flat=False)
    ss_metadata = {
        "fanart_url": "https://example.test/fanart.png",
        "fanart_path": "roms/1/1/fanart/fanart.png",
    }
    rom_attrs: dict[str, object] = {"ss_metadata": dict(ss_metadata)}

    apply_folder_game_cover(rom_attrs, fs_rom, [_file(f"n64/{FOLDER}", "cover.png")])

    assert rom_attrs["url_cover"] == f"file://n64/{FOLDER}/cover.png"
    assert rom_attrs["ss_metadata"] == ss_metadata
