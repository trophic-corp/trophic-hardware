# CEA Sensors and Controllers

| Product | ID | Stage |
|---|---|---|
| Rack controller | `CT-A` | **Phase 0** |
| Room controller | `CT-B` | **Phase 0** |

Both are named, scoped and architecturally fixed by the CEA orchestrator suite's
device model — but **no hardware has been designed**. Today they exist as an
`11_ENCLOSURE_IP65` massing block in the rack model and a topology in a software
document.

## The important boundary

**The control architecture is owned by the software side** (CEA suite ADR-0001
edge-first autonomy, ADR-0002 capability model, ADR-0004 MQTT/Modbus backbone). This
family designs the **boxes** — enclosure, IO, power, mounting, environmental
protection — to fit that architecture. It does not redesign it.

What crosses back the other way goes through `trophic-contracts`, never direct.

## Local interlocks are not software

Leak puck, `LSH-04`, E-stop and the `MV-01` flood sensor are **hard-wired and
bus-independent**. The controller reads their state; it is not in their safety path.
Any controller design that puts a processor between an interlock and its actuator has
failed the requirement.
