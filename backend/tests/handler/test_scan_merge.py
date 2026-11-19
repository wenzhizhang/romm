from tests.factories import make_rom

from handler.scan.merge import (
    apply_metadata_priority,
    keep_base_fields,
    merge_tags,
    reset_rematched_sources,
)
from handler.scan.sources import MetadataSource
from models.platform import Platform


def test_the_stored_placeholder_name_is_replaced(platform: Platform):
    # The stored placeholder differs from the title derived from the filename.
    rom = make_rom(
        platform,
        "celeste.p8",
        fs_stem="celeste.p8",
        fs_extension="png",
    )
    rom_attrs = {"fs_name": rom.fs_name, "name": "Celeste"}

    keep_base_fields(rom_attrs, rom)

    assert rom_attrs["name"] == "Celeste"


def test_a_name_the_user_set_is_kept(platform: Platform):
    rom = make_rom(platform, "My Celeste", fs_stem="celeste.p8", fs_extension="png")
    rom_attrs = {"fs_name": rom.fs_name, "name": "Celeste"}

    keep_base_fields(rom_attrs, rom)

    assert rom_attrs["name"] == "My Celeste"


def test_a_complete_rescan_keeps_a_hand_set_tag_lock(platform: Platform):
    rom = make_rom(platform, "celeste.zip")
    rom.locked_fields = ["languages", "url_cover"]
    rom_attrs = {"locked_fields": ["languages", "url_cover"]}

    reset_rematched_sources(rom_attrs, {}, set(), [], rom)

    assert rom_attrs["locked_fields"] == ["languages"]


def test_a_locked_tag_is_not_overwritten_by_a_provider():
    rom_attrs = {
        "regions": ["Japan"],
        "languages": ["Japanese"],
        "locked_fields": ["languages"],
    }
    metadata_handlers = {
        MetadataSource.GAMELIST: {
            "handler": {"regions": ["USA"], "languages": ["English"]}
        }
    }

    apply_metadata_priority(rom_attrs, metadata_handlers, [MetadataSource.GAMELIST])

    assert rom_attrs["languages"] == ["Japanese"]
    assert rom_attrs["regions"] == ["USA"]


def test_a_locked_tag_survives_a_hash_claim():
    rom_attrs = {
        "fs_name": "celeste.zip",
        "regions": [],
        "languages": ["Japanese"],
        "tags": [],
        "locked_fields": ["languages"],
    }

    merge_tags(
        rom_attrs,
        {},
        [],
        [({"regions": [], "languages": ["English"], "tags": []}, True)],
    )

    assert rom_attrs["languages"] == ["Japanese"]
