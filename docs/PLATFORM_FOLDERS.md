# Platform folders

Every folder directly under the library's `roms/` directory is a platform, and
RomM reads the folder name as the platform slug: a folder named `genesis` is
Sega Mega Drive/Genesis. The table below lists the canonical folder name for
every platform RomM knows, generated from `backend/utils/platform_slugs.py`.

Batocera and ES-DE spell some folders differently (`megadrive`, `dreamcast`,
`mastersystem`, and so on). Those are accepted too, see
`backend/utils/platform_aliases.py` for the full alias mapping.

A folder named something else still works, but RomM creates a custom platform
for it that no metadata provider can match, so a whole system can end up
unidentified. Keep to the names below.

| Platform | Folder |
| --- | --- |
| 1292 Advanced Programmable Video System | `1292-advanced-programmable-video-system` |
| 3DO Interactive Multiplayer | `3do` |
| 8-Bit Productions Commander X16 | `commander-x16` |
| Aamber Pegasus | `pegasus` |
| ABC 80 | `abc-80` |
| Acorn Archimedes | `acorn-archimedes` |
| Acorn Electron | `acorn-electron` |
| Action Max | `action-max` |
| Advanced Pico Beena | `advanced-pico-beena` |
| AdvanceMAME | `mame-advmame` |
| AirConsole | `airconsole` |
| Alice 32/90 | `alice-3290` |
| Altair 680 | `altair-680` |
| Altair 8800 | `altair-8800` |
| Amazon Alexa | `amazon-alexa` |
| Amazon Fire TV | `amazon-fire-tv` |
| Amiga | `amiga` |
| Amiga CD | `amiga-cd` |
| Amiga CD32 | `amiga-cd32` |
| Amstrad CPC | `acpc` |
| Amstrad GX4000 | `amstrad-gx4000` |
| Amstrad PCW | `amstrad-pcw` |
| Analogue electronics | `analogueelectronics` |
| Android | `android` |
| Antstream | `antstream` |
| APF MP1000/Imagination Machine | `apf` |
| Apogee BK-01 | `bk-01` |
| Apple I | `apple` |
| Apple II | `appleii` |
| Apple IIGS | `apple-iigs` |
| Apple III | `appleiii` |
| Apple Lisa | `apple-lisa` |
| Apple Pippin | `apple-pippin` |
| Apple Pippin | `pippin` |
| Arcade | `arcade` |
| Arcadia 2001 | `arcadia-2001` |
| Arduboy | `arduboy` |
| Astral 2000 | `astral-2000` |
| Atari 2600 | `atari2600` |
| Atari 5200 | `atari5200` |
| Atari 7800 | `atari7800` |
| Atari 8-bit | `atari8bit` |
| Atari 800 | `atari800` |
| Atari Jaguar | `jaguar` |
| Atari Jaguar CD | `atari-jaguar-cd` |
| Atari Lynx | `lynx` |
| Atari ST/STE | `atari-st` |
| Atari VCS | `atari-vcs` |
| Atari XEGS | `atari-xegs` |
| Atom | `atom` |
| Atomiswave | `atomiswave` |
| AY-3-8500 | `ay-3-8500` |
| AY-3-8603 | `ay-3-8603` |
| AY-3-8605 | `ay-3-8605` |
| AY-3-8606 | `ay-3-8606` |
| AY-3-8607 | `ay-3-8607` |
| AY-3-8610 | `ay-3-8610` |
| AY-3-8710 | `ay-3-8710` |
| AY-3-8760 | `ay-3-8760` |
| Bada | `bada` |
| Bally Astrocade | `astrocade` |
| BBC Microcomputer System | `bbcmicro` |
| Benesse Pocket Challenge V2 | `pocket-challenge-v2` |
| Benesse Pocket Challenge W | `pocket-challenge-w` |
| BeOS | `beos` |
| BGR Computers Excalibur 64 | `excalibur-64` |
| Bit Corporation BIT 90 | `bit-90` |
| BlackBerry OS | `blackberry` |
| Blacknut | `blacknut` |
| Blu-ray Player | `blu-ray-player` |
| BREW | `brew` |
| Browser (Flash/HTML5) | `browser` |
| Bubble | `bubble` |
| Call-A-Computer time-shared mainframe computer system | `call-a-computer` |
| Cambridge Computer Z88 | `z88` |
| Camputers Lynx | `camputers-lynx` |
| Casio CFX-9850 | `casio-cfx-9850` |
| Casio FP-1000 & FP-1100 | `casio-fp-1000` |
| Casio Loopy | `casio-loopy` |
| Casio PB-1000 | `casio-pb-1000` |
| Casio Programmable Calculator | `casio-programmable-calculator` |
| Casio PV-2000 | `casio-pv-2000` |
| CDC Cyber 70 | `cdccyber70` |
| Champion 2711 | `champion-2711` |
| ClickStart | `clickstart` |
| Coleco Adam | `colecoadam` |
| ColecoVision | `colecovision` |
| Commodore 128 | `c128` |
| Commodore 16 | `c16` |
| Commodore C64/128/MAX | `c64` |
| Commodore CDTV | `commodore-cdtv` |
| Commodore PET | `cpet` |
| Commodore Plus/4 | `c-plus-4` |
| Commodore VIC-20 | `vic-20` |
| Compal 80 | `compal-80` |
| Compucolor I | `compucolor-i` |
| Compucolor II | `compucolor-ii` |
| Compucorp Programmable Calculator | `compucorp-programmable-calculator` |
| COSMAC | `fred-cosmac` |
| CP/M | `cpm` |
| CreatiVision | `creativision` |
| Cybervision | `cybervision` |
| Danger OS | `danger-os` |
| Daphne | `daphne` |
| Daydream | `daydream` |
| DEC GT40 | `gt40` |
| Dedicated console | `dedicated-console` |
| Dedicated handheld | `dedicated-handheld` |
| DICE | `dice` |
| Didj | `didj` |
| Digiblast | `digiblast` |
| DoJa | `doja` |
| Donner Model 30 | `donner30` |
| Doom | `doom` |
| DOS | `dos` |
| Dragon 32/64 | `dragon-32-slash-64` |
| Dreamcast | `dc` |
| DVD Player | `dvd-player` |
| e-Reader / Card-e Reader | `e-reader-slash-card-e-reader` |
| EasyRPG | `rpg-maker` |
| ECD Micromind | `ecd-micromind` |
| EDSAC | `edsac` |
| EG2000 Colour Genie | `colour-genie` |
| Elektor TV Games Computer | `elektor` |
| Elektronika BK | `bk` |
| Enterprise | `enterprise` |
| Entex Adventure Vision | `adventure-vision` |
| Epoch Cassette Vision | `epoch-cassette-vision` |
| Epoch Super Cassette Vision | `epoch-super-cassette-vision` |
| Evercade | `evercade` |
| ExEn | `exen` |
| Exidy Sorcerer | `exidy-sorcerer` |
| EXL 100 | `exelvision` |
| Fairchild Channel F | `fairchild-channel-f` |
| Family Computer | `famicom` |
| Family Computer Disk System | `fds` |
| Feature phone | `mobile-custom` |
| Ferranti Nimrod Computer | `nimrod` |
| FinalBurn Alpha | `fba` |
| FinalBurn Neo | `fbneo` |
| FM Towns | `fm-towns` |
| FM-7 | `fm-7` |
| Freebox | `freebox` |
| G-cluster | `g-cluster` |
| Gaelco | `gaelco` |
| Galaksija | `galaksija` |
| Gamate | `gamate` |
| Game & Watch | `g-and-w` |
| Game Boy | `gb` |
| Game Boy Advance | `gba` |
| Game Boy Color | `gbc` |
| Game Master | `hartung` |
| Game Pocket Computer | `epoch-game-pocket-computer` |
| Game Wave | `game-wave` |
| Game.com | `game-dot-com` |
| GameStick | `gamestick` |
| Gear VR | `gear-vr` |
| GIMINI | `gimini` |
| Gizmondo | `gizmondo` |
| Gloud | `gloud` |
| Glulx | `glulx` |
| GNEX | `gnex` |
| Google Stadia | `stadia` |
| GP2X | `gp2x` |
| GP2X Wiz | `gp2x-wiz` |
| GP32 | `gp32` |
| GVM | `gvm` |
| Handheld Electronic LCD | `handheld-electronic-lcd` |
| HD DVD Player | `hd-dvd-player` |
| Heath/Zenith H8/H89 | `heathzenith` |
| Heathkit H11 | `heathkit-h11` |
| Hector HRX | `hrx` |
| Hitachi S1 | `hitachi-s1` |
| HP 2100 | `hp2100` |
| HP 3000 | `hp3000` |
| HP 9800 | `hp-9800` |
| HP Programmable Calculator | `hp-programmable-calculator` |
| Hugo | `hugo` |
| Hyper Neo Geo 64 | `hyper-neo-geo-64` |
| HyperScan | `hyperscan` |
| IBM 5100 | `ibm-5100` |
| IBM PCjr | `pc-jr` |
| Ideal-Computer | `ideal-computer` |
| iiRcade | `iircade` |
| Imlac PDS-1 | `imlac-pds1` |
| Intel 8008 | `intel-8008` |
| Intel 8080 | `intel-8080` |
| Intel 8086 / 8088 | `intel-8086` |
| Intellivision | `intellivision` |
| Intellivision Amico | `intellivision-amico` |
| Interact Model One | `interact-model-one` |
| Interton Video 2000 | `interton-video-2000` |
| iOS | `ios` |
| iPad | `ipad` |
| iPod Classic | `ipod-classic` |
| J2ME | `j2me` |
| Jolt | `jolt` |
| Jupiter Ace | `jupiter-ace` |
| KaiOS | `kaios` |
| KIM-1 | `kim-1` |
| Kindle Classic | `kindle` |
| Laser 200 | `laser200` |
| LaserActive | `laseractive` |
| LeapFrog Explorer | `leapfrog-explorer` |
| Leapster | `leapster` |
| Leapster Explorer/LeadPad Explorer | `leapster-explorer-slash-leadpad-explorer` |
| LeapTV | `leaptv` |
| Legacy Computer | `legacy-computer` |
| Legacy Mobile Device | `mobile` |
| Linux | `linux` |
| Luna | `luna` |
| Mac | `mac` |
| Maemo | `maemo` |
| Magnavox Odyssey | `odyssey` |
| Mainframe | `mainframe` |
| MAME | `mame` |
| Matsushita/Panasonic JR | `matsushitapanasonic-jr` |
| Mattel Aquarius | `aquarius` |
| MeeGo | `meego` |
| Mega Duck/Cougar Boy | `mega-duck-slash-cougar-boy` |
| Memotech MTX | `memotech-mtx` |
| Memotech MTX512 | `mtx512` |
| Meritum | `meritum` |
| Meta Quest 2 | `meta-quest-2` |
| Meta Quest 3 | `meta-quest-3` |
| MGT SAM Coupé | `sam-coupe` |
| Microbee | `microbee` |
| Microcomputer | `microcomputer` |
| Microsoft MSX2+ | `msx2plus` |
| Microtan 65 | `microtan-65` |
| Microvision | `microvision` |
| Mophun | `mophun` |
| MOS Technology 6502 | `mos-technology-6502` |
| Motorola 6800 | `motorola-6800` |
| Motorola 68k | `motorola-68k` |
| MRE | `mre` |
| MSX | `msx` |
| MSX Turbo R | `msx-turbo` |
| MSX2 | `msx2` |
| MUGEN | `mugen` |
| N-Gage | `ngage` |
| N-Gage (service) | `ngage2` |
| Namco System 246/256 | `namco2x6` |
| Namco System 357/369 | `namco3xx` |
| NAOMI | `naomi` |
| NAOMI 2 | `naomi2` |
| Nascom | `nascom` |
| NEC PC-6000 Series | `nec-pc-6000-series` |
| Neo Geo AES | `neogeoaes` |
| Neo Geo CD | `neo-geo-cd` |
| Neo Geo MVS | `neogeomvs` |
| Neo Geo Pocket | `neo-geo-pocket` |
| Neo Geo Pocket Color | `neo-geo-pocket-color` |
| Neo Geo X | `neo-geo-x` |
| New Nintendo 3DS | `new-nintendo-3ds` |
| NewBrain | `newbrain` |
| Newton | `newton` |
| Nintendo 3DS | `3ds` |
| Nintendo 64 | `n64` |
| Nintendo 64DD | `64dd` |
| Nintendo DS | `nds` |
| Nintendo DSi | `nintendo-dsi` |
| Nintendo Entertainment System | `nes` |
| Nintendo GameCube | `ngc` |
| Nintendo Switch | `switch` |
| Nintendo Switch 2 | `switch-2` |
| North Star | `northstar` |
| Noval 760 | `noval-760` |
| Nuon | `nuon` |
| Oculus Go | `oculus-go` |
| Oculus Quest | `oculus-quest` |
| Oculus Rift | `oculus-rift` |
| Oculus VR | `oculus-vr` |
| Odyssey 2 / Videopac G7000 | `odyssey-2` |
| Ohio Scientific | `ohio-scientific` |
| OnLive Game System | `onlive-game-system` |
| OOParts | `ooparts` |
| OpenBOR | `openbor` |
| Orao | `orao` |
| Oric 1 / Atmos | `oric` |
| Oric Atmos | `atmos` |
| OS/2 | `os2` |
| Othello Multivision | `multivision` |
| Ouya | `ouya` |
| Palm OS | `palm-os` |
| Palmtex Super Micro | `palmtex` |
| Panasonic Jungle | `panasonic-jungle` |
| Panasonic M2 | `panasonic-m2` |
| Pandora | `pandora` |
| PC Booter | `pc-booter` |
| PC Engine SuperGrafx | `supergrafx` |
| PC Win3.xx | `win3x` |
| PC Win9X | `win9x` |
| PC-50X Family | `pc-50x-family` |
| PC-6001 | `pc-6001` |
| PC-8000 | `pc-8000` |
| PC-8800 Series | `pc-8800-series` |
| PC-9800 Series | `pc-9800-series` |
| PC-FX | `pc-fx` |
| PDP-1 | `pdp1` |
| PDP-10 | `pdp10` |
| PDP-11 | `pdp11` |
| PDP-7 | `pdp-7` |
| PDP-8 | `pdp-8` |
| Pebble | `pebble` |
| Philips CD-i | `philips-cd-i` |
| Philips VG 5000 | `philips-vg-5000` |
| Photo CD | `photocd` |
| Pico-8 | `pico` |
| Pinball | `pinball` |
| PLATO | `plato` |
| Playdate | `playdate` |
| Playdia | `playdia` |
| PlayStation | `psx` |
| PlayStation 2 | `ps2` |
| PlayStation 3 | `ps3` |
| PlayStation 4 | `ps4` |
| PlayStation 5 | `ps5` |
| PlayStation Now | `playstation-now` |
| PlayStation Portable | `psp` |
| PlayStation Vita | `psvita` |
| PlayStation VR | `psvr` |
| PlayStation VR2 | `psvr2` |
| Plex Arcade | `plex-arcade` |
| Plug & Play | `plug-and-play` |
| PocketStation | `pocketstation` |
| Pokitto | `pokitto` |
| Pokémon mini | `pokemon-mini` |
| Poly-88 | `poly-88` |
| Polymega | `polymega` |
| PSP Minis | `psp-minis` |
| PV-1000 | `casio-pv-1000` |
| R-Zone | `r-zone` |
| RCA Studio II | `rca-studio-ii` |
| Research Machines 380Z | `research-machines-380z` |
| Roku | `roku` |
| Satellaview | `satellaview` |
| SC/MP | `scmp` |
| ScummVM | `scummvm` |
| SD-200/270/290 | `sd-200270290` |
| SDS Sigma 7 | `sdssigma7` |
| Sega 32X | `sega32` |
| Sega Advanced Pico Beena | `beena` |
| Sega CD | `segacd` |
| Sega CD 32X | `segacd32` |
| Sega Chihiro | `chihiro` |
| Sega Dreamcast VMU | `vmu` |
| Sega Game Gear | `gamegear` |
| Sega Hikaru | `hikaru` |
| Sega Lindbergh | `lindbergh` |
| Sega Master System/Mark III | `sms` |
| Sega Mega Drive/Genesis | `genesis` |
| Sega Model 2 | `model2` |
| Sega Model 3 | `model3` |
| Sega Naomi GD-ROM | `naomigd` |
| Sega Pico | `sega-pico` |
| Sega Saturn | `saturn` |
| Sega SC-3000 | `sc3000` |
| Sega Titan Video | `stv` |
| SG-1000 | `sg1000` |
| Sharp MZ-2200 | `sharp-mz-2200` |
| Sharp MZ-80B/2000/2500 | `sharp-mz-80b20002500` |
| Sharp MZ-80K/700/800/1500 | `sharp-mz-80k7008001500` |
| Sharp X1 | `x1` |
| Sharp X68000 | `sharp-x68000` |
| Sharp Zaurus | `sharp-zaurus` |
| SHG Black Point | `black-point` |
| Signetics 2650 | `signetics-2650` |
| Sinclair QL | `sinclair-ql` |
| Sinclair ZX81 | `zx81` |
| Singe | `singe` |
| SK-VM | `sk-vm` |
| SMC-777 | `smc-777` |
| Socrates | `socrates` |
| Sol-20 | `sol-20` |
| Sord M5 | `sord-m5` |
| Spectravideo | `spectravideo` |
| SRI-500/1000 | `sri-5001000` |
| Steam | `steam` |
| SteamVR | `steam-vr` |
| Sufami Turbo | `sufami-turbo` |
| Super A'Can | `super-acan` |
| Super Famicom | `sfam` |
| Super NES CD-ROM System | `super-nes-cd-rom-system` |
| Super Nintendo Entertainment System | `snes` |
| Super Vision 8000 | `super-vision-8000` |
| Sure Shot HD | `sure-shot-hd` |
| SwanCrystal | `swancrystal` |
| SWTPC 6800 | `swtpc-6800` |
| Symbian | `symbian` |
| TADS | `tads` |
| Tapwave Zodiac | `zod` |
| Tatung Einstein | `tatung-einstein` |
| TeknoParrot | `teknoparrot` |
| Tektronix 4050 | `tektronix-4050` |
| Tele-Spiel ES-2201 | `tele-spiel` |
| Telstar Arcade | `telstar-arcade` |
| Terebikko / See 'n Say Video Phone | `terebikko-slash-see-n-say-video-phone` |
| Terminal | `terminal` |
| Texas Instruments TI-82 | `ti-82` |
| Texas Instruments TI-83 | `ti-83` |
| Texas Instruments TI-99 | `ti-99` |
| Thomson MO/TO | `thomson-to` |
| Thomson MO5 | `thomson-mo5` |
| TI Programmable Calculator | `ti-programmable-calculator` |
| TI-99/4A | `ti-994a` |
| TIC-80 | `tic-80` |
| Tiki 100 | `tiki-100` |
| TIM | `tim` |
| Timex Sinclair 2068 | `timex-sinclair-2068` |
| Tizen | `tizen` |
| Tomahawk F1 | `tomahawk-f1` |
| Tomy Tutor | `tomy-tutor` |
| Tomy Tutor / Pyuta / Grandstand Tutor | `tomy-tutor-slash-pyuta-slash-grandstand-tutor` |
| Triforce | `triforce` |
| Triton | `triton` |
| TRS-80 | `trs-80` |
| TRS-80 Color Computer | `trs-80-color-computer` |
| TRS-80 MC-10 | `trs-80-mc-10` |
| TRS-80 Model 100 | `trs-80-model-100` |
| TurboGrafx-16/PC Engine | `tg16` |
| Turbografx-16/PC Engine CD | `turbografx-cd` |
| tvOS | `tvos` |
| Type X | `type-x` |
| Type X 55 | `taito-x-55` |
| Uzebox | `uzebox` |
| V.Flash | `vflash` |
| V.Smile | `vsmile` |
| VC 4000 | `interton-vc-4000` |
| VC 4000 | `vc-4000` |
| Vector-06C | `06c` |
| Vectrex | `vectrex` |
| Versatile | `versatile` |
| VideoBrain | `videobrain` |
| Videopac+ G7400 | `videopac-g7400` |
| Virtual Boy | `virtualboy` |
| Virtual Console | `vc` |
| VIS | `tandy-vis` |
| VIS | `vis` |
| visionOS | `visionos` |
| Visual Memory Unit / Visual Memory System | `visual-memory-unit-slash-visual-memory-system` |
| Wang 2200 | `wang2200` |
| WASM-4 | `wasm-4` |
| Watara/QuickShot Supervision | `supervision` |
| watchOS | `watchos` |
| webOS | `webos` |
| Wii | `wii` |
| Wii U | `wiiu` |
| Windows | `win` |
| Windows Apps | `windows-apps` |
| Windows Mixed Reality | `windows-mixed-reality` |
| Windows Mobile | `windows-mobile` |
| Windows Phone | `winphone` |
| WIPI | `wipi` |
| WonderSwan | `wonderswan` |
| WonderSwan Color | `wonderswan-color` |
| XaviXPORT | `xavixport` |
| Xbox | `xbox` |
| Xbox 360 | `xbox360` |
| Xbox Cloud Gaming | `xboxcloudgaming` |
| Xbox One | `xboxone` |
| Xbox Series X/S | `series-x-s` |
| Xerox Alto | `xerox-alto` |
| Z-Machine | `z-machine` |
| Zeebo | `zeebo` |
| Zelda Classic | `zelda-classic` |
| Zilog Z80 | `z80` |
| Zilog Z8000 | `zilog-z8000` |
| ZiNc | `zinc` |
| Zodiac | `zodiac` |
| Zune | `zune` |
| ZX Spectrum | `zxs` |
| ZX Spectrum Next | `zx-spectrum-next` |
| ZX80 | `zx80` |
