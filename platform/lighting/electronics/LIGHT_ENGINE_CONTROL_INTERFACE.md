# Light Engine ↔ Smart Module Control Interface — concept

| | |
|---|---|
| **Class** | **CONCEPT.** Nothing here is frozen. When the port pinout, rail budget and protocol version 1 are decided they become an ICR-governed interface specification and this document is superseded |
| **Governing record** | ADR-008 (PROPOSED) |
| **Research basis** | Lighting/Electronics and Systems Architect evaluations of 2026-09-11; `docs/references/lighting/LIGHTING_PLATFORM_REFERENCE.md` B4, C |
| **Applies to** | `AQ-LT-A` Core engine, `AQ-LT-B` WRGB engine, Smart Module, optional dimmer puck; a future standalone CEA light. **Not** `LT-A` |

---

## 1. The boundary

```
230 V AC ─▶ certified adapter ─▶ ELV DC ─▶ [ LIGHT ENGINE (fixture) ]
                                            │  input protection (ideal diode, UVLO/OVP, TVS)
                                            │  5 V housekeeping buck → 3.3 V
                                            │  engine MCU: PWM, hardware ID, default profile,
                                            │     thermal derating, protocol endpoint, bootloader
                                            │  hardware thermal backstop (NTC comparator → driver EN)
                                            │  CC driver stage per channel ─▶ LED MCPCB (NTC)
                                            │  CONTROL PORT: 5 V · GND · TX · RX  (signal only)
                                            └────────────┬──────────────────────────────
                                                         │ short tether (≤ ~2 m)
                                        [ SMART MODULE ] │  radio (BLE, Wi-Fi optional), RTC + backup,
                                                          schedules, ramps, app protocol, OTA host,
                                                          profile storage, buttons, status LED
```

Principles (from the owner proposal, confirmed by both evaluations):

1. **LED power and every safety-critical function live in the engine.** The module never carries bus power or LED-channel power; the port is signal plus a small housekeeping rail.
2. **The engine is a complete, safe light without a module**: it powers up into a stored default profile with a soft-start ramp, derates thermally on its own, and never exceeds its limits regardless of commands.
3. **One port, one protocol, two engines.** Core (1 channel) and WRGB (4–5 channels) report their capabilities at handshake; the module and app treat channel count as a property.
4. **Two connectors of different families**: DC-in and control port. A combined connector would put the module in the power path and take the adapter out of the certified barrel ecosystem.
5. **The engine has no radio.** Radio approval (WPC ETA) and radio EMC belong to the module only.

## 2. Engine-side minimum (both engines)

| Block | Core | WRGB | Notes (indicative, not spec) |
|---|---|---|---|
| MCU | Cortex-M0+/RISC-V value class, 1 PWM timer, 2 ADC, 1 UART | STM32G0x1/CH32V203 class, ≥ 5 timer PWM channels, 2 UART | ₹30–150 class |
| Dimming | ≥ 12-bit at ≥ 3 kHz; hysteretic buck drivers settle in ~5–20 µs so pure PWM gives ~1:15–1:60 usable ratio; **hybrid PWM + analogue setpoint** or a wide-range controller class is the likely answer, NEEDS VALIDATION with a flicker meter and phone camera | same | |
| Hardware ID | I²C EEPROM on the engine board (variant, serial, per-channel max current, calibration); resistor strap on the MCPCB if it is sourced separately | same | ₹10–15 |
| Thermal | NTC on the MCPCB at the hottest LED; firmware derating curve; **hardware comparator backstop** pulling driver enable low independent of the MCU | same, second NTC on the driver board | ₹20–40 |
| Input protection | Ideal-diode controller + NMOS, TVS, comparator UVLO with hysteresis, OVP, PTC or eFuse. An integrated 60 V-class eFuse is below the 64.8 V OVP ceiling of a 48 V adapter, so a 48 V bus needs 80 V-class parts (reference C1) | same | |
| Housekeeping | One 5 V buck from the bus (0.7–1 A) feeding the port and a 3.3 V LDO; port 5 V through a current-limited load switch | same | not a separate buck per rail |
| Port protection | TVS array at the connector, 100–330 Ω series on TX/RX, UART pins tolerant of the module being powered before or after the engine; single-point bond of engine GND to the extrusion near the connector for ESD return | same | |
| Bootloader | 4–8 kB write-protected, image CRC, drivers held off in bootloader, rollback on failed verify; a failed image must still light at the default level | same | |

Engine-board BOM class at 100 units excluding LEDs, MCPCB, heatsink, enclosure and assembly: Core ₹700–1,300, WRGB ₹1,500–2,800 (estimate, ±50 %; the cost model carries mid values).

## 3. Port: link and connector (candidate classes)

**Link (recommended class):** full UART, 4 pins (5 V, GND, TX, RX), 3.3 V logic, 19.2–115.2 kbaud 8N1, CRC-16 framing. Rejected: I²C (bus lock on hot-plug, capacitance limit near 2 m), 0–10 V / PWM lines (no discovery, ID, temperature or OTA; one line per channel), 1-Wire (too slow for OTA), CAN and RS-485 (over-engineered for a point-to-point tether; RS-485 reserved for a future wired module on the CEA in-room bus). Single-wire half-duplex UART (3 pins) is the fallback if a 3-pin connector wins. USB-C as a physical carrier for the same UART is attractive mechanically (GND-first, 10 000 cycles) but invites mis-use with chargers and laptops; acceptable only if both ends survive any USB source or sink. NEEDS DECISION.

**Port power:** 5 V at 0.5–0.7 A. An ESP32-C3-class module draws ~30–60 mA average on BLE and bursts to ~350 mA on Wi-Fi TX (datasheet); the module carries ≥ 470 µF bulk. Add ~0.3 W housekeeping and 0.5 W (BLE) to ~2 W (Wi-Fi peak) to the PSU budget.

**Connector candidates:** M8 3/4-pin (IP67 mated, needs cap, ₹150–400 per side imported), SP13 (IP68 mated claim, bulky, ₹80–200), IP-rated USB-C receptacle (₹80–250), magnetic pogo dock (best aesthetics, worst corrosion: DC on exposed pins in salt or condensation, power must be gated on a detect pin), 3.5 mm TRRS (cheap, contacts short during insertion, power must be gated). Contact sequencing must not be relied on: series resistors, TVS and the load switch make sequence irrelevant. The unused port must be capped. Salt-mist, damp-heat and DC-biased condensation tests apply.

## 4. Fail-safe state machine (proposal)

```
BOOT → SELF-TEST (ID, NTC sanity) → HANDSHAKE (module present? version compatible?)
      ├─ no module / incompatible ─▶ STANDALONE: ramp to stored default level
      └─ compatible ─────────────▶ CONTROLLED: levels from module, keepalive with wall-clock
CONTROLLED, keepalive lost ─▶ HOLD (grace window) ─▶ FALLBACK
THERMAL: firmware derating in every state; hardware backstop independent of every state
```

| Case | Hardware guarantees | Firmware provides | Status |
|---|---|---|---|
| Mains-timer power-up, no module | Drivers off until the MCU asserts; inrush limited | Default profile from EEPROM with a soft-start ramp (1–5 s) | ramp time NEEDS DECISION |
| Thermal | NTC comparator backstop | Derating curve from LED datasheet limits; telemetry to module; module may only reduce, never raise | thresholds are later EDRs |
| Module lost mid-schedule | nothing beyond thermal | Options: hold last level (wrong at night); off (loses the day); **hold for a grace window then ramp to default**; **coasting schedule** (module sends wall-clock in every keepalive; engine free-runs a stored 24 h table on its own oscillator, 1–2 % drift acceptable for days). Never full-on, never abrupt off | **OWNER DECISION REQUIRED** |
| No module ever, no mains timer | — | Optional "power-on photoperiod": run default for N h from power-up then drop to a low night level. Free on the engine; may confuse users | NEEDS DECISION |
| Wrong or undersized adapter | UVLO with hysteresis, OVP cut-off, TVS, current limit | optional power cap after repeated UVLO | — |
| Default level | — | Factory-set, **writable through the port and persisted in the engine** so a Smart customer can teach the light its standalone level | NEEDS DECISION |

Platform §4 mapping: the defined state with no signal is *default profile*; with no power or a dead MCU it is *off*; hardware only guarantees that neither can overheat or over-current.

## 5. Protocol sketch (version 1, conservative and extensible)

Frame: SOF · length · type · sequence · payload · CRC-16/CCITT; COBS if binary transparency is wanted. Handshake HELLO returns: protocol version (major.minor), hardware ID (family, variant, revision), serial, firmware version, channel count N, per-channel max current and colour tag, thermal limits, capability bits (coasting schedule, bootloader, default-level write). Minimum command set: SET_LEVELS (N × 16-bit, ramp_ms), GET_STATUS (levels, temperatures, Vin, Iin, fault flags, uptime), KEEPALIVE (wall-clock), SET_DEFAULT_PROFILE, SET_FALLBACK_POLICY, ENTER_BOOTLOADER (magic + CRC), OTA_WRITE / VERIFY / COMMIT. Rules: major mismatch refuses control and the engine stays STANDALONE; unknown types are NACKed and ignored; semantics never change within a major; typed fields so unknown fields are skipped.

**Governance.** The engine port protocol is a hardware interface owned in this repository and changed by ICR. The app-to-module protocol belongs in `trophic-contracts` (PLATFORM.md §8); the published device model is *one light* with channel count as a property, with the module as transport endpoint. The port protocol is not published to contracts unless `AQ-CT-A` is decided to speak it directly (X4).

## 6. Smart Module (concept)

ESP32-C3-class module (Wi-Fi as a firmware option; single-source Espressif, ₹120–200) or nRF52 (BLE only, ₹250–500); RV-3028-class RTC with supercapacitor backup (days to weeks, no serviceable cell); 5 V → 3.3 V regulator, bulk capacitance, ESD array, series resistors, common-mode choke on the port side; two or three buttons; single-colour status LED per the design brief; PCB antenna in a polymer puck, ≥ 10 mm from any aluminium, away from the water surface: **a tethered puck is the safe RF placement; docking on the extrusion is an Industrial Design question with an RF cost.** BOM class at 100 units ₹700–1,400 before enclosure and assembly. Average dissipation 0.1–0.3 W, 1.7 W during Wi-Fi TX; negligible thermal rise.

**Optional dimmer puck:** a tiny MCU plus a potentiometer or encoder speaking SET_LEVELS on the same port. A product option, not an architecture.

## 7. EMC and ESD

CISPR 15 ed. 9 extends conducted limits to load and control terminals (150 kHz–30 MHz) and uses the CDNE method for 30–300 MHz (from recall; verify against the standard text). The tether plus adapter cable forms a dipole for the buck stages' common-mode noise, so the tether is in scope and can be the radiator. Mitigations: common-mode choke and LC on the 5 V port rail, series resistors on data, ferrite on the cable, tight buck loops, single-point ground, spread-spectrum drivers where available. Pre-scan with and without the module attached. ESD: TVS before the series resistors; IEC 61000-4-2 4 kV contact / 8 kV air at the port and puck.

## 8. Production test

Engine EOL: bench PSU sweep for UVLO/OVP; a USB-UART jig speaking the protocol reads ID, serial, firmware and NTC, steps each channel, measures string current and a per-channel photodiode or mini-spectrometer, input current, and trips the thermal backstop by NTC substitution. One jig for both engines. Class ₹20–50k. Module EOL: a jig emulating an engine (answers HELLO, logs commands), RTC set → power-cycle → read, BLE/Wi-Fi RSSI against a reference, buttons and LED. Class ₹15–40k. Firmware load via SWD pads or the port bootloader.

## 9. Validation this interface needs (adds to roadmap §4)

Port contact corrosion under 5 V DC bias (salt mist, damp heat, DC-biased condensation); mis-plug abuse between DC-in and port; tethered-system EMC pre-scan; ESD at port and puck; hot-plug during a Wi-Fi burst (engine brown-out); fallback policy fault injection (no all-night or all-day state); PWM resolution vs driver minimum on-time (flicker meter, camera banding); thermal backstop threshold at 40 °C ambient; power-cut during OTA with rollback; BIS scope of a radio-free ELV luminaire and ETA reuse for a pre-approved module (RESEARCH REQUIRED).

## 10. Open decisions carried by ADR-008

Message port vs signal-wire port (the MCU-less Core challenger); tethered puck vs recess-dock vs module-as-end-cap; connector class; link class (4-pin UART vs 3-pin half-duplex vs USB-C carrier); fallback policy and grace window; power-on photoperiod; default-level writability; port rail budget; module identifier and serial family; whether WRGB Standalone is a sold SKU; whether `AQ-CT-A` speaks the port (X4).
