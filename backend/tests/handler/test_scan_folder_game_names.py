"""Scanning a folder game whose folder is localized and whose file name is not."""

from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest
from tests.handler.scan_stubs import add_n64_platform, add_rom, run_scan

from config.config_manager import config_manager as cm
from handler.metadata.gamelist_handler import GamelistRom
from handler.metadata.libretro_handler import LibretroRom
from handler.scan.merge import folder_game_search_name
from handler.scan.sources import MetadataSource, ScanType
from models.rom import RomFile

FOLDER = "圣剑传说"
FILE = "Sword of Mana (USA).gba"
MATCH = LibretroRom(libretro_id="Sword of Mana (USA)", name="Sword of Mana")


@pytest.fixture
def folder_names_enabled():
    """Turn the strategy on without touching the config file."""
    enabled = SimpleNamespace(
        **(vars(cm.get_config()) | {"SCAN_FOLDER_GAME_NAMES": True})
    )
    with patch.object(cm, "get_config", return_value=enabled):
        yield


def add_folder_rom():
    platform = add_n64_platform()
    rom = add_rom(platform, FOLDER, FOLDER)
    files = [
        RomFile(
            rom_id=rom.id,
            file_name=FILE,
            file_path=rom.fs_path,
            file_size_bytes=2048,
            category=None,
        ),
        RomFile(
            rom_id=rom.id,
            file_name="cover.png",
            file_path=rom.fs_path,
            file_size_bytes=9999,
            category=None,
        ),
    ]
    return platform, rom, files


def test_the_main_game_file_names_the_search():
    """A sidecar image is larger but is not what the game is called."""
    platform, rom, files = add_folder_rom()

    assert folder_game_search_name(files, FOLDER) == "Sword of Mana"


async def test_the_file_name_is_what_providers_are_asked(folder_names_enabled):
    platform, rom, files = add_folder_rom()
    lookup = AsyncMock(return_value=MATCH)

    with patch("handler.scan.lookups.meta_libretro_handler.get_rom", new=lookup):
        result = await run_scan(
            platform,
            rom,
            scan_type=ScanType.COMPLETE,
            metadata_sources=[MetadataSource.LIBRETRO],
            flat=False,
            files=files,
        )

    lookup.assert_awaited_once_with("Sword of Mana", platform.slug)
    assert result.name == f"{FOLDER} | Sword of Mana"


async def test_the_strategy_is_off_by_default():
    platform, rom, files = add_folder_rom()
    lookup = AsyncMock(return_value=MATCH)

    with patch("handler.scan.lookups.meta_libretro_handler.get_rom", new=lookup):
        result = await run_scan(
            platform,
            rom,
            scan_type=ScanType.COMPLETE,
            metadata_sources=[MetadataSource.LIBRETRO],
            flat=False,
            files=files,
        )

    lookup.assert_awaited_once_with(FOLDER, platform.slug)
    assert result.name == "Sword of Mana"


async def test_a_gamelist_still_matches_the_folder(folder_names_enabled):
    """The gamelist keys entries by path, so its lookup keeps the folder name."""
    platform, rom, files = add_folder_rom()
    lookup = AsyncMock(return_value=GamelistRom(gamelist_id="1", name=FOLDER))

    with patch("handler.scan.lookups.meta_gamelist_handler.get_rom", new=lookup):
        await run_scan(
            platform,
            rom,
            scan_type=ScanType.COMPLETE,
            metadata_sources=[MetadataSource.GAMELIST],
            flat=False,
            files=files,
        )

    lookup.assert_awaited_once_with(FOLDER, platform, rom)


async def test_an_update_keeps_an_edited_title(folder_names_enabled):
    platform, rom, _ = add_folder_rom()
    rom.name = "我改的名字"

    with patch(
        "handler.scan.lookups.meta_libretro_handler.get_rom",
        new=AsyncMock(return_value=LibretroRom(libretro_id=None)),
    ):
        result = await run_scan(
            platform,
            rom,
            scan_type=ScanType.UPDATE,
            metadata_sources=[MetadataSource.LIBRETRO],
            flat=False,
            files=[],
        )

    assert result.name == "我改的名字"
