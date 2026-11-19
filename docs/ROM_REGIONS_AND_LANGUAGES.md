# Regions and languages

A rom's `regions` and `languages` come from the tags in its name: the file name
for a single-file rom, the folder name for a multi-file one. The same tags also
produce `tags` (hacks, translations, revisions) and the `revision`/`version`
columns, see `backend/handler/filesystem/roms_handler.py::parse_tags`.

## Writing the tags

A tag is whatever sits inside a pair of parentheses or square brackets, and a
tag may hold several comma-separated values:

```
Sonic (USA).md
Sonic (USA, Europe) (En,Fr,De).md
Super Mario World (Japan) [T+Eng1.0].sfc
Legend of Zelda, The (Europe) (Rev 1).nes
```

A multi-file rom is a folder, so the tags go on the folder name:

```
roms/psx/Final Fantasy VII (USA) (Disc 1)/
roms/psx/Final Fantasy VII (USA) (Disc 2)/
```

Both `(...)` and `[...]` are read, and a comma inside a tag splits it into
separate tags, so `(USA, Europe)` is two regions. Matching is case-insensitive
except where a region and a language share a spelling (`NL` is Netherlands,
`Nl` is Dutch; `NO` is Norway, `No` is Norwegian): the exact-code pass runs
before the case-insensitive one, so the casing picks the meaning.

A tag that names no known region or language falls through to the other tag
passes and, failing those, is kept verbatim in `tags`. `(Reg-Foo)` is the
explicit way to say "this is a region", so `Foo` is stored as-is.

## Regions

| Tag | Stored as |
| --- | --- |
| `A` | Australia |
| `AS` | Asia |
| `B` | Brazil |
| `C` | Canada |
| `CH` | China |
| `E` | Europe |
| `F` | France |
| `FN` | Finland |
| `G` | Germany |
| `GR` | Greece |
| `H` | Holland |
| `HK` | Hong Kong |
| `I` | Italy |
| `J` | Japan |
| `K` | Korea |
| `NL` | Netherlands |
| `NO` | Norway |
| `PD` | Public Domain |
| `R` | Russia |
| `S` | Spain |
| `SW` | Sweden |
| `T` | Taiwan |
| `U` | USA |
| `UK` | England |
| `UNK` | Unknown |
| `UNL` | Unlicensed |
| `W` | World |

The full name works too (`(Japan)`, `(usa)`, `(Europe)`), and so do the
provider-only names providers write without a filename code: Americas, Bulgaria,
Chile, Czech Republic, Denmark, Hungary, Israel, Kuwait, Middle East, New
Zealand, Oceania, Peru, Poland, Portugal, Slovakia, Turkey. The canonical table
lives in `backend/handler/filesystem/base_handler.py` (`REGIONS` and
`REGION_NAME_TO_PROVIDER_SHORTCODE`).

## Languages

| Tag | Stored as |
| --- | --- |
| `Ar` | Arabic |
| `Da` | Danish |
| `De` | German |
| `El` | Greek |
| `En` | English |
| `Es` | Spanish |
| `Fi` | Finnish |
| `Fr` | French |
| `It` | Italian |
| `Ja` | Japanese |
| `Ko` | Korean |
| `Nl` | Dutch |
| `No` | Norwegian |
| `Pl` | Polish |
| `Pt` | Portuguese |
| `Pt-BR` | Brazilian Portuguese |
| `Ru` | Russian |
| `Sr` | Serbian |
| `Sv` | Swedish |
| `Zh` | Chinese |
| `nolang` | No Language |

The full name works too (`(English)`, `(japanese)`). Providers also write
languages with no filename shortcode: Afrikaans, Albanian, Armenian, Belarusian,
Bulgarian, Catalan, Croatian, Czech, Estonian, Hebrew, Hindi, Hungarian,
Icelandic, Indonesian, Latin, Latvian, Lithuanian, Macedonian, Romanian, Slovak,
Slovenian, Thai, Turkish, Ukrainian, Vietnamese (`PROVIDER_LANGUAGES` in
`base_handler.py`).

## Translation tags

A fan translation is not a language tag of its own: it adds `translation` to
`tags` and the target language to `languages`. GoodTools (`[T+Eng1.0]`,
`[T-Pt-BR1.1]`), TOSEC (`[tr fr]`) and plainer sets (`(Translation)`) are all
read. `[T-]` marks a translation that was superseded by a newer one.

## Editing in the UI

The edit dialog (rom details, `Edit`) has a **Languages** and a **Regions**
field under its details tab, both a combobox over the names above that also
accepts a typed value. Setting either writes the column directly and locks it,
so a rescan or metadata refresh keeps the value. Renaming the file hands both
fields back to the filename and re-parses them.

## Filtering

The gallery's filter drawer has a **Language** and a **Region** group, each with
`any` / `all` / `none` logic, the same as the other facets. The API takes
`filter_languages` and `filter_regions` (plus `filter_languages_logic` and
`filter_regions_logic`).
