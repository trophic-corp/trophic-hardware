# ICR-002 — Rack supply interface changes from pumped to gravity-fed

| | |
|---|---|
| **Status** | ACCEPTED |
| **Date** | 2026-09 |
| **Affects** | Hydraulic — rack inlet |

## Context

EDR-005 removed the supply pump. The rack inlet was specified against a pumped supply with a pressure the pump would guarantee. It now sees a head that varies with terrace tank level and with how many tiers irrigate concurrently.

## Decision

The rack inlet is specified against **available head**, not supply pressure:

| Parameter | Value |
|---|---|
| Supply source | Terrace gravity, outlet at +4250 mm |
| Static head at the top nozzle (+1590 mm) | 2.66 m |
| Design flow, one tier | 7.2 L/min |
| Rack-side loss allowance at design flow | 0.33 m |
| Flow ceiling before head is exhausted | ~15 L/min |
| Four tiers concurrent | 28.8 L/min at 0.67 m — passes |

## Consequences

- Solenoid selection becomes head-critical: the DN20 solenoid at Kv 4 alone accounts for 0.119 m, the largest single rack-side loss. Substituting a lower-Kv valve eats the margin.
- Any future increase in nozzle count, tier count or concurrent irrigation must be re-checked against the 15 L/min ceiling. There is no pump to absorb it.
- Control software must not assume constant supply pressure. Candidate `trophic-contracts` content.

## Evidence

`RK-A-WRS_Rev3`; `RK-A-SYS_Rev2`
