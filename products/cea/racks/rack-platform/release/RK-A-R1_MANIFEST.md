# RK-A R1 — Engineering Release Manifest

| | |
|---|---|
| **Release ID** | `RK-A R1` |
| **Status** | **ISSUED** |
| **Purpose** | Prototype fabrication |
| **Source design** | Fusion `CEA_RACK_INTEGRATED_v2` **v8** |
| **Hardware revision** | Rev 5 |
| **Exported** | 2026-09-05 10:21 |
| **Verified** | 2026-09-09 |
| **Release store** | `E:\My Drive\03_Projects\Trophic Industries\CEA_RACK_v1\INTEGRATED_v2_Rev5\` |

Binaries are **not** committed to this repository. They live in the release store
above, which is a synced Google Drive path. This manifest is the verifiable record:
any file can be re-hashed against it.

---

## 1. Verification performed 2026-09-09

| Acceptance criterion | Result |
|---|---|
| Exported from `CEA_RACK_INTEGRATED_v2` **v8**, version recorded | **Pass** — `MANIFEST.txt` line 2 states `CEA_RACK_INTEGRATED_v2 v8` |
| Every expected file exists on disk | **Pass** — 45 of 45 part files present, none missing, none extra |
| No zero-byte files | **Pass** — smallest file 5,582 bytes |
| Files are valid STEP | **Pass** — all 46 `.step` files carry the `ISO-10303-21` header; the `.f3d` is a valid Fusion zip container |
| Manifest lists every file with SHA-256 | **Pass** — this document |
| Figures reconcile to the live model | **Pass** — see §2 |

`ExportManager.execute()` return values were **not** checked at export time — that
remains a defect in the export script, and is why this release had to be verified
after the fact rather than at the moment of export. The verification above is
equivalent evidence for **this** release. Fix the script before the next one.

## 2. Reconciliation against the live Fusion model

Read from `CEA_RACK_INTEGRATED_v2` v8 on 2026-09-09, without modifying it:

| Quantity | Manifest | Live model | Repository docs |
|---|---|---|---|
| Envelope W × D × H | 1456 × 690 × 1960 mm | **1456.0 × 690.0 × 1960.0** | 1456 × 690 × 1960 ✓ |
| Dry mass | 112.66 kg | **112.657 kg** | 112.66 kg ✓ |
| Unique parts | 45 | 45 files | 45 ✓ |
| Occurrences | 177 | **177** | 177 ✓ |
| Interference | 0 unresolved | — | 0 ✓ |
| Part mass sum | — | — | **112.66 kg**, sums exactly |

Every headline figure in this repository is confirmed against both the manifest and
the live model. **No figure needed correcting.**

## 3. Content confirms the design corrections

| Correction | Evidence in this release |
|---|---|
| **EDR-004** deck mesh density | `04_DECK_PANEL` at **1.981 kg ea** — the corrected ≥70 % open mesh figure, not the 8.256 kg of the superseded placeholder |
| **ICR-001** tray-to-drain continuity | `09_TRAY_OUTLET`, `09_TRAY_STRAINER` and `09_OVF_BULKHEAD` are all present; `09_OVF_V` is 14,711 bytes against 7,686 in the pre-correction export — the extended Z 160–300 drop |
| **EDR-001** flood geometry | Parameter master: `Flood_Depth` 22, `Tray_Rim` 25, `Flood_Tray_H` 47 mm |

---

## 4. Manifest — SHA-256

Total 2,876,320 bytes across 47 files.

| File | Bytes | SHA-256 |
|---|---|---|
| `STEP/02_UPRIGHT.step` | 245,126 | `15aba2201d2ac865e71395c976d6afb118897d3d272d73926b9fd32e0d73e0d7` |
| `STEP/03_BEAM_LONG.step` | 13,943 | `2c4cc182ddec184186f018eccbdbaaa3eb81cd7023658aafb42a0996faaff1e5` |
| `STEP/03_BEAM_SHORT.step` | 13,933 | `e49a34f290cf128adbafaace7dcb2fc87690e1f83ae5de0019290a33c627d7a1` |
| `STEP/04_DECK_PANEL.step` | 10,532 | `5cdf3054152cef17ece379f0bfa3a3b3e19674c1c963219ca4372c788281196a` |
| `STEP/04_DECK_RAIL_CROSS.step` | 13,958 | `deceb143e3f867fef549c22bd9bbaf52a9dd79425a6d584258115234580d0294` |
| `STEP/04_DECK_RAIL_LONG.step` | 13,966 | `239eb65d9bf520321e361904baeb9a28e72b06a85aa5b723fde4ce2d356d3326` |
| `STEP/05_REAR_BRACE.step` | 21,701 | `7e053acf5cd7b8115a8b76e398d4446faf100dfb8739b29d29459335f93d8288` |
| `STEP/06_LED_FIXTURE_ENV.step` | 14,613 | `63152ae8e8179931a588293229d4796b23be4b71ab4c011513c06d1bed75022a` |
| `STEP/06_LED_HANGER.step` | 5,645 | `22e56a65f25ef43e382e8178fe3103a3f3001ca819d00690a7e7137242322a67` |
| `STEP/06_LED_RAIL.step` | 13,905 | `61c56ba8c7a3f794a1a0c52401072d068b85167cec5eeae7e5d3ed5ead186c42` |
| `STEP/07_FAN.step` | 9,053 | `69be52ed375843dea439abdd88f040adefb4e5d4ffa899242d8d2105c3fe64e5` |
| `STEP/07_PLENUM.step` | 14,717 | `6539f966678e9402fd5810fe5b744a3d623cef81ff114c34f0999c71ba0c67f2` |
| `STEP/08_FILL_MANIFOLD.step` | 14,719 | `ef31ea82cc8b617019551287b8cb0cdf98180bf15932564dbde85e96ed33f0fb` |
| `STEP/08_FILL_NOZZLE.step` | 9,138 | `38624d053075aad41d6c691a5f88d5140901350ccf93c78d2bbedf0199f264d9` |
| `STEP/08_FILL_SOLENOID.step` | 9,148 | `b1626d38cd946e97d6ff6452909e568e3c9b3ae80fcec7a781336ac1602fcd1b` |
| `STEP/08_FLOOD_TRAY.step` | 15,901 | `02e3af12fe36b806a8b12362aac0afb1776ef18068c70174eddf21884fa2cca3` |
| `STEP/08_SUPPLY_RISER.step` | 14,686 | `fd58f7bb857c6f9a23acf0794a80209dc9a76f967afba17889550c4a5bce8ce4` |
| `STEP/08_TIER_DROP_V1.step` | 14,652 | `365d80df74534393f9a36b8ec2453435c179e5762692f2526b79ba2092c8ae1e` |
| `STEP/08_TIER_DROP_V2.step` | 14,652 | `67f1f91403704ac30749f48196e40e1ddba93eda8f3c5abe9b18952ae722a82b` |
| `STEP/08_TIER_DROP_V3.step` | 14,686 | `f90e44f0933725db05ad96d79c25ef70ecf6fabd356ee4a580a7c76b84754d4c` |
| `STEP/08_TIER_DROP_V4.step` | 14,686 | `3dbe7d13cbb59886d948ce2174892e60a19ea4dc63d1ddcd924e3b23d449702c` |
| `STEP/08_TIER_DROP_X.step` | 14,681 | `e9703e2fa6ebbc4dcdc50cdabc83bd53c81cb2578c43e572c3ea0112331cdf1b` |
| `STEP/08_TIER_DROP_Y.step` | 14,653 | `46c167c5bd8b66d717b0f52b22dc02230b7740bc7fedc32317782923a0d230b1` |
| `STEP/09_DRAIN_HEADER.step` | 14,764 | `17a0dba430e110d9a62f272893de808bb497e6a407917418564ada38ee604525` |
| `STEP/09_DRAIN_SOLENOID.step` | 9,177 | `62a7e0f2ee218e1c508ba6380582c6d0a358597200f87782488c847ae7d284da` |
| `STEP/09_HEADER_LEVEL_SW.step` | 9,160 | `68dcd46689a1c448fb6363f0163ffc27d0b4959d89c0835f562a8f1942e115bd` |
| `STEP/09_OVF_BULKHEAD.step` | 14,750 | `8dbe89485e568fbca299868ac836eee4c9d437b12fba782168092bf8f823bc71` |
| `STEP/09_OVF_COLLAR.step` | 7,721 | `fdcdab99669ba3899d5652f43a8caa8def72bcb3b4ac6e340d15d9688c080149` |
| `STEP/09_OVF_V.step` | 14,711 | `3012b0c362a3e5bbaa27e60d5515a9b6f92cb6a6519c13e85f525f8c38b408b8` |
| `STEP/09_OVF_X.step` | 14,723 | `14945a457b31337b10f7e43e33521b978cceb4508b151d56c4acf66727a2f9b9` |
| `STEP/09_PANEL_REAR.step` | 9,152 | `e7d853c16839929965ae4e59e710ea38adf6b2437e33af28e28155a56f94aa8c` |
| `STEP/09_PANEL_SIDE.step` | 9,104 | `e69bc4cc5a0a009d34616a4b7e1c67fba7c963a58132229f3b835d2230565072` |
| `STEP/09_TRAY_DRAIN_V.step` | 7,737 | `dd112d156dc5ad08b27149515a65e6b26dea09b0af6a9160f994090b0650f575` |
| `STEP/09_TRAY_DRAIN_X.step` | 14,776 | `1784bec1657223c3a3ec871245351b6c9e038130dd3dd848d0a069ca9d2b16dd` |
| `STEP/09_TRAY_OUTLET.step` | 14,751 | `fabd571636e28b2016baeebf802a168586e3ca27483ad7bfdb97ab1df9a556d8` |
| `STEP/09_TRAY_STRAINER.step` | 14,772 | `83814ef9426d375d4e56a4788b953bc5405519f35c85e832fdd62db5dc94d444` |
| `STEP/09_TUNDISH.step` | 14,666 | `2024350b18fcd4fb80023beec272c270395907c824befe001d4800bd9fb6bac6` |
| `STEP/10_LEAK_SENSOR.step` | 9,044 | `ecb4f9b4fa2b292b51569528eb6128deb6ffdc0032715f224f812cb18526290b` |
| `STEP/10_TRH_NODE.step` | 8,919 | `cf4b31f9ab7e498307c6df4de76492bfe9b90ffb3abc9c6bb77cb46bdb16eba2` |
| `STEP/11_CABLE_CHANNEL.step` | 14,704 | `a10c6d6627246bf6e2468e6e3866cd7129dac7ba71fedab267d35d296a9a98b0` |
| `STEP/11_CABLE_TRAY_TIER.step` | 14,598 | `b6b6245369a03a5e9ec283df6759041681bdcac4bccf400ad5d4498b1c33740e` |
| `STEP/11_ENCLOSURE_IP65.step` | 14,767 | `efe5c7553c02215af48d9b2ec526ac54110c59a8e5beed37339bacaa37dabeb7` |
| `STEP/11_ISOLATOR.step` | 9,102 | `00e9bf1db804378c5d0fbe0a7a3ede9814bc6d535032ed6512a3eea50af47f54` |
| `STEP/13_FOOT.step` | 5,582 | `d1d80537bfdefcad4fe431e69e45f5d9701eaa7e9970232b3cbc05326d7724cc` |
| `STEP/14_WALL_ANCHOR.step` | 8,947 | `9be4cfc2a3d3a351304e2eb46192e772cdd278d76a3fc1c975b9efa87501a7d7` |
| `ASSEMBLY/CEA_RACK_INTEGRATED_v2_Rev5.f3d` | 1,201,551 | `76a8ee6a7c384919ca73b3927d1cf913f347914287200434a014920743960b5e` |
| `ASSEMBLY/CEA_RACK_INTEGRATED_v2_Rev5.step` | 876,448 | `b427b7f478746453ab4d7a6544bd98e2aa5ef88e7e8fb9757234f16485748435` |

---

## 5. Not part of this release

| Item | Why |
|---|---|
| `DXF/` (5 files) | **Stale.** Exported from `CEA_RACK_PLATFORM_RackA_v1`, not the integrated design, and covering only 5 parts. Flat patterns must be regenerated from v8 before any sheet-metal part is cut |
| `STEP/`, `ASSEMBLY/` at the folder root | The earlier platform export (`RK-A-000_RACK_ASSEMBLY`), superseded by this release |
| `INTEGRATED_v2/` | The pre-Rev5 integrated export — lacks the ICR-001 parts. Superseded |
| `mass_report.txt` | The superseded v5 working mass report totalling **1,246.35 kg** (solid placeholders, plenums at 252 kg each). Historical only. **Never quote it as a mass** |

## 6. Errata against issued documents

| Document | Erratum |
|---|---|
| `RK-A-MFG` Rev 2 §15 | Cites the release location as `C:\Users\karex\Desktop\CEA_RACK_v1`. The actual store is the Google Drive path above. Correct at the next revision |
| `RK-A-DWG` Rev 2 | Same incorrect path |

Neither erratum affects any engineering value. Both are location references.
