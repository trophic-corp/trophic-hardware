# CEA Orchestrator Suite — hardware contract audit

**Date:** 2026-09-09
**Audited:** `trophic-corp/cea-orchestrator` at `C:\dev\project\trophic`
**Branch actually read:** `phase-1-kickoff-2` @ `496aba74` — **not `main`**, see §1
**Audited against:** `trophic-contracts` v0.1.0
**Outcome:** `trophic-contracts` v0.2.0

---

## 1. Branch caveat — read this first

The request was to audit `main`. The checkout on the machine is on
**`phase-1-kickoff-2`**, and the session has no shell on that device (the folder mount
failed), so the branch could not be switched and `main` could not be read.

| Ref | Commit |
|---|---|
| `main` | `86588afd33f9e9e489ce9319d19b44823f82d842` |
| `origin/main` | `86588afd33f9e9e489ce9319d19b44823f82d842` (identical — `main` is up to date) |
| `phase-1-kickoff-2` | `496aba746b1ac93a5f36d22f634454e31c5173ec` |

`main` and `origin/main` agree, so nothing is unpushed on `main`. By file timestamps the
working tree carries newer work than `main` — ADR-0009 (Vue 3), the frontend-framework
pipeline artifacts and the workspace audit are all dated after `main`'s ref.

**Everything below was read from the working tree at `phase-1-kickoff-2`.** If any
finding turns on a file that differs between the branches, it needs re-checking. The
safety-critical files this audit turns on — `safety-rules.json` and
`docs/iot/device-control-model.md` — are dated 2026-09-05 and 2026-09-07, both older than
`main`'s ref, so they are very unlikely to differ.

---

## 2. What the suite is, in one paragraph

A multi-agent, ADR-driven CEA control platform: `knowledge/cea/` holds the source
literature and OCR'd hardware PDFs, `docs/adr/` holds nine accepted architecture
decisions, `.github/agentic-rules/safety-rules.json` holds sourced physical safety
thresholds that every specialist agent must treat as ground truth, and
`docs/iot/device-control-model.md` holds a five-way desired/command/ack/reported/telemetry
device model with a capability-class vocabulary (ADR-0002), a Modbus-RTU field bus and an
MQTT facility backbone (ADR-0004). Backend (Go), frontend (Vue 3) and firmware directories
are scaffolded but empty pending the Phase 1 build.

**The engineering discipline in this suite is high.** It refuses to invent thresholds, it
marks OCR-unreliable values as blocking rather than guessing, and it records rejected
hardware capabilities as decisions to respect rather than gaps to fill. Most of what
follows is not a criticism of it.

---

## 3. The structural finding

**The contract direction is currently reversed.**

`safety-rules.json` and `device-control-model.md` were built by reading the hardware
documents directly — as OCR'd PDFs, page by page, with the OCR quality documented per
page. Every value in them is sourced to a Rack A / Water Recovery / Floor Plan section.

That is exactly the coupling ADR-004 exists to prevent. It works, but it means:

- The hardware set's revisions do not reach the software. The suite's device model cites
  **RK-A-ROOM Rev 3**; the current revision is **Rev 4**.
- OCR quality becomes a safety variable. One gate is currently uncodeable in the suite
  *only* because the PDF scan was poor — see §4.1.
- Two teams maintain two extractions of the same facts, and neither is authoritative.

`trophic-contracts` v0.2.0 exists to close this. The suite should consume it and retire
the direct extraction, keeping `safety-rules.json` as the place where **crop and process**
thresholds live (PPFD bands, photoperiod, climate setpoints) — those are genuinely the
software's domain — while **hardware** facts come from the contract.

---

## 4. Findings

### 4.1 G1 EC gate — the suite has the wrong multiplier · **HIGH**

`safety-rules.json` records:

> `"note": "Gate G1 ... exists (\\"EC < setpoint x ~1.2 ...\\") but the OCR of the exact
> numeric threshold on this page (\\"< 15 setpoint — < 180 mS/cm at a 1.20 setpoint\\") is
> garbled/inconsistent ... and should NOT be trusted for an implementation."`

The authoritative source, **RK-A-WRS Rev 3 §07**, reads:

> **G1 · Electrical conductivity · ≤ 1.5 × setpoint — ≤ 1.80 mS/cm at a 1.20 setpoint ·
> AT-03, in the trough · Trough dump valve to waste**

So the multiplier is **1.5×, not 1.2×**. `1.20` is the **setpoint** in the worked example,
not the multiplier, and the limit is **1.80 mS/cm**, not 180.

The suite was right to refuse to code it. **The OCR flag can now be cleared** and the gate
implemented from the contract. Note that the EC *operating setpoint* is still genuinely
unspecified — `1.20 mS/cm` appears only as the worked example — so `ec_operating_target`
remains a legitimate TBD.

### 4.2 Sequential draining was missing from the contract · **HIGH — our defect**

`trophic-contracts` v0.1.0 stated "four tiers concurrent — permitted" without saying that
this applies to **filling only**.

RK-A-SYS Rev 2 §R5: four tiers draining at once puts **122.8 L/min** into a DN40 vertical
stack whose practical capacity is **90–120 L/min**. One tier drains at 30.7 L/min.
Sequential draining is "a hard requirement of the pipework, not an efficiency choice".

The suite did **not** get this wrong — `safety-rules.json` carries it correctly
("Sequential DRAINING remains mandatory in all revisions") and the device model has the
room controller owning a drain token. **Our contract was the weak link**, and a consumer
reading only v0.1.0 could have overflowed a stack. Published as
`hydraulic/drain-sequencing.md`.

### 4.3 Five gates documented, eight exist · **MEDIUM**

`safety-rules.json` documents G1–G5. RK-A-WRS Rev 3 §07 has **G1–G8**:

| Gate | Missing from the suite |
|---|---|
| G6 | Leak detectors clear — `LD-01…11`; on failure dump to waste and isolate that rack |
| G7 | Operator contamination hold — dump to waste until cleared by a **named** operator |
| G8 | `TK-01` has room — `LT-02` < 90 %; hold in trough until level falls |

Also unrecorded: **G1, G2, G3, G6, G7, G8 are evaluated per batch before anything is
pumped, while G4 and G5 are watched continuously during transfer** — either failing throws
`FV-01` to waste mid-transfer. The device model does say "8-gate reuse logic / G1–G8 gate
table", so the suite knows the count; it is the rules file that is short.

### 4.4 Device model built against RK-A-ROOM Rev 3 · **MEDIUM**

`device-control-model.md` header: *"sourced from the Rack A engineering set (RK-A-SYS
Rev 2, RK-A-MFG Rev 2, RK-A-WRS Rev 3, **RK-A-ROOM Rev 3** — the current revision chain)"*.

The current revision is **Rev 4**. Rev 3 silently dropped the Building section — ceiling
height, floor and point loading, slab, floor finish, wall fixings, egress — which Rev 4
restored with recomputed loads. Any conclusion the suite drew about room loading,
mounting or egress came from a document missing that section.

### 4.5 Our interface specs understated what is specified · **MEDIUM — our defect**

`IF-RK-A-ELE` listed seven items as NEEDS SPECIFICATION and `IF-RK-A-CTL` listed eight.
The suite's extraction shows most were specified in RK-A-SYS §07 and RK-A-MFG §01/§05 all
along, and this audit confirmed them against our own local copies:

| We said unspecified | Actually specified |
|---|---|
| Emergency stop architecture and scope | Room-level only, one latching mushroom head per aisle/door. Drops group contactor, fill solenoids, `MV-01`, pumps; drains de-energize open. Explicitly **not** per-rack |
| Isolation for maintenance | Per-rack isolator, for lock-out/tag-out — a different function from the E-stop |
| Circuit ratings | 16 A Type A RCBO 30 mA per rack; 63 A MCCB + Type 2 SPD per group of 8; 10 mA RCBO on the terrace circuit |
| Segregation | ELV boundary: 24/48 V DC at or below canopy, 230 V confined to an IP65 enclosure above canopy, **236 mm** minimum vertical separation, drip loop mandatory across a wet zone |
| Earthing test points | TN-S per IS 3043, every frame bonded, **< 0.1 Ω**, tested and recorded per rack |
| Interlocks | Leak puck, `LSH-04`, E-stop, `MV-01` flood sensor — hard-wired and bus-independent; 60 s solenoid-close proof is a QC hold point |
| Actuator inventory | 4 fill + 4 drain solenoids on an 8-ch relay, EC fan per tier at 178 m³/h with mandatory tacho alarm, one 0–10 V dimming pair per tier |
| Sensor identities | `TE-01/02`, `AT-03` (EC), `AT-04` (pH), `LT-02`, `LSH-04`, `LS-01`, `LD-01…11`, `PDI-01`, `UIT-01`, `FS-01` |

Corrected in both interface specs and published as `electrical/elv-boundary.md`,
`safety/interlocks.md` and `sensors/instrument-tags.md`.

### 4.6 Capabilities absent by design were not published · **MEDIUM**

The suite carefully records capabilities the hardware deliberately lacks — per-tray level
sensing, per-rack/tier CO₂, tier-level climate control, fixed PAR sensing, per-rack kWh
metering — with the hardware's own rationale. Our contract published none of them. A
negative fact is a contract too: "there is no per-tray level sensor, and the standpipe is
why" prevents a whole class of wrong software. Published as
`capabilities/absent-by-design.md`.

### 4.7 Canopy velocity CV — two thresholds, one action ladder or one conflict · **NEEDS DECISION**

`safety-rules.json` flags, correctly, that two thresholds appear in our source set and
declines to pick one:

| Source | Threshold | Action |
|---|---|---|
| RK-A-SYS §01 | CV 15 % | Fit side/rear enclosure panels |
| RK-A-ROOM §04 | CV 20 % | Below 20 %: plenum is an optimisation. Above 20 %: plenum is a required fix |

These read naturally as a **two-step escalation ladder** — panels first at 15 %, plenum at
20 % — rather than as a contradiction. But no hardware document says so, and inferring it
would be exactly the silent reconciliation this migration forbids.

**Raised as ND-05.** Not published to contracts until decided.

### 4.8 Fill-rate figures: 28.8 vs 29.0 L/min · **LOW**

RK-A-SYS gives the four-tier concurrent fill as 28.8 L/min (4 × 7.2) and uses it as the
overflow fault case. The pump-duty analysis that rejected simultaneous filling on the old
pumped design quotes 29.0 L/min. Same physical case, different basis. **28.8 is the figure
to use**, since the current gravity design and its fault case are computed from it.
Flagged in the contract rather than harmonised away.

### 4.9 Phase imbalance ~20 % against a 15 % target · **NEEDS DECISION**

`safety-rules.json`, from RK-A-ROOM §05: the as-designed 11-rack layout lands at ~20 %
imbalance on single-phase HVAC against a 15 % target, "resolved by specifying 3-phase
HVAC", and is "documented as an open engineering finding, not a clean pass". Our room
README does not carry this. **Raised as ND-06.**

### 4.10 Terrace slab loading — the hard one · **NEEDS DECISION**

From RK-A-WRS §04 Risk 3: concentrated worst case **5.5 kN/m²**, spread over beam lines
2.2 kN/m², against a typical accessible-terrace rating of **1.5–2.0 kN/m²**. The source
calls this the one item that cannot be resolved by choosing better equipment, and requires
a structural engineer's sign-off against the building's actual drawings **before the
terrace tank is ordered**.

Our water-recovery README said only "terrace structural capacity must be confirmed",
without the numbers. **Raised as ND-07** with the figures attached.

### 4.11 Depth-plane bracing is unverified — our validation index was too soft · **our defect**

`VERIFICATION_INDEX.md` listed VR-07 as "Reported adequate — NEEDS TRACEABILITY". That
understates it. RK-A-MFG Rev 2 says plainly:

> Removing the per-tier cross beams and relying on the decks as horizontal diaphragms plus
> the base frame is sound in principle and the tip-over numbers above assume it holds.
> **It has not been checked by frame analysis.**

It is not that the metadata is missing — **the analysis was never done**, and the tip-over
figures (139 N empty, 307 N loaded) depend on it holding. The closure is a physical test:
**T16**, 300 N horizontal at the top bed, front-back and side, residual deflection ≤ 5 mm,
with a costed fallback (restore the cross beams, ₹562). T16 supersedes the older P3
numbering; RK-A-SYS §10 still says P3, and RK-A-MFG states the supersession explicitly, so
this is a naming lag, not a conflict.

VR-07 restated. NT-02 rewritten.

---

## 5. What the suite got right that we should keep

- It refuses to invent a threshold, and marks unsourced values `TBD — needs domain expert
  input` rather than filling them. `ec_operating_target` and `dli_mol_m2_day` are both
  correctly left open.
- It marks OCR-derived values by page reliability and treats unreliable ones as blocking.
- It records **rejected** hardware capabilities as decisions the software must respect,
  not gaps to fill.
- Its control allocation matches ours exactly: local interlocks are hard-wired and
  bus-independent, "software reads their state but is not in their safety path", and the
  cloud owns nothing the room depends on.
- Its fail-state table was **more complete than our contract's**, which is how we found
  our own gap.

---

## 6. Actions

### On the software side (for the suite's owners, not done here)

| # | Action |
|---|---|
| S1 | Consume `trophic-contracts` v0.2.0; retire direct extraction of hardware facts from the OCR'd PDFs |
| S2 | Correct the G1 multiplier to **1.5×** and clear the OCR block on that gate |
| S3 | Add gates G6, G7, G8 and record which gates are per-batch vs continuous |
| S4 | Re-check any conclusion drawn from RK-A-ROOM **Rev 3** against **Rev 4**'s Building section |
| S5 | Keep `safety-rules.json` for crop and process thresholds; source hardware facts from the contract |

**No change was made to the CEA suite in this session.** Nothing was written to
`C:\dev\project\trophic`.

### On the hardware side (done here)

| # | Action | Status |
|---|---|---|
| H1 | Publish drain sequencing as a contract | Done — `hydraulic/drain-sequencing.md` |
| H2 | Publish interlocks, ELV boundary, instrument tags, absent capabilities | Done |
| H3 | Correct `IF-RK-A-ELE` and `IF-RK-A-CTL` NEEDS SPECIFICATION lists | Done |
| H4 | Restate VR-07 and NT-02 | Done |
| H5 | Raise ND-05 (CV threshold), ND-06 (phase imbalance), ND-07 (terrace slab) | Done |
| H6 | Publish the eight-gate table with instrument tags | Done |

---

## 7. Sources

All read from `C:\dev\project\trophic` at `phase-1-kickoff-2`:

- `CLAUDE.md`
- `.github/agentic-rules/safety-rules.json`
- `docs/iot/device-control-model.md`
- `docs/adr/0001-edge-first-local-control-autonomy.md`
- `docs/adr/0002-capability-based-device-model.md`
- `docs/adr/0004-mqtt-timescale-postgres-backbone.md`
- `docs/domain/cea-domain-model.md`
- `.git/config`, `.git/HEAD`, `.git/refs/**`

Cross-checked against local authoritative copies of `RK-A-SYS` Rev 2, `RK-A-WRS` Rev 3 and
`RK-A-MFG` Rev 2 in this repository. Every hardware value quoted above was verified against
those files, not taken from the suite's extraction.
