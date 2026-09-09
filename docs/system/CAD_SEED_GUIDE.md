# CAD Seed Guide — generating 3D models from Phase 0 documents

How to run "build 3D models of the products from the Phase 0 documents" without
producing models that look like engineering and are not.

---

## 1. The problem this guide exists to prevent

A Phase 0 document lists what is decided and what is open. A CAD model has no way to
express "open" — every face has a position, every part has a size. So a model built
from a Phase 0 document **silently converts open questions into apparent decisions**,
and the resulting file looks exactly like a designed part.

Three months later nobody remembers which numbers were decided and which were
invented to make the model close. That is how a repository loses its authority.

This guide keeps the two apart.

---

## 2. Model classes

Every generated model is one of three things, and the class is recorded in the model
name and in this repository. There is no fourth, unlabelled class.

| Class | Means | Names like |
|---|---|---|
| **ENVELOPE** | A keep-out volume. Only the bounding dimensions are claimed; nothing inside is real | `LT-A_ENVELOPE` |
| **CONCEPT** | A form proposal to be judged and probably discarded. No dimension is a decision | `AQ-LP-A_CONCEPT_r1` |
| **DESIGN** | Real engineering. Every dimension traces to a decision, a calculation or a standard | `RK-A` |

**Only `RK-A` is class DESIGN today.** Nothing generated from a Phase 0 document may
be class DESIGN, and a model cannot be promoted by editing it — promotion happens
when the decisions in the product's `PRODUCT.md` §5 are answered.

---

## 3. What a generation prompt may and may not use

### May use

- §3 **Inherited constraints — DECIDED**. Every row is sourced. These are real.
- The rack's existing placeholder geometry where it exists (`06_LED_FIXTURE_ENV`,
  `07_PLENUM`, `11_ENCLOSURE_IP65`) — already correct as envelopes.
- `platform/mechanical-standards/` for hole grids, sections and fasteners **on steel
  products only**.
- `RK-A-PARAM` Rev 1 for any dimension that interfaces with the rack.

### Must not use

- §4 **Industry reference points**. Labelled NOT TROPHIC DECISIONS. They may inform a
  CONCEPT and must never appear on a drawing.
- Anything from `archive/`.
- A competitor product, in any family. A generated shape that matches a market part
  is a copy, not a design — this matters most for `AQ-LP-A`.
- The CEA rack's numbers by analogy. `P-02` is a 0.75 kW terrace pump; it tells you
  nothing about an aquarium powerhead.
- Its own earlier output. A CONCEPT does not become a constraint by existing.

---

## 4. Per-product readiness

From each `PRODUCT.md` §8. Check here before generating anything.

| Product | Buildable now | Class | Notes |
|---|---|---|---|
| `RK-A` | **Already built** | DESIGN | `CEA_RACK_INTEGRATED_v2` v8. Do not regenerate |
| `WR-A` | Partially | — | Skid and reservoirs are specified in `RK-A-WRS` Rev 3; no CAD exists |
| `LT-A` | Yes — envelope only | ENVELOPE | 40 × 60 mm at Y 148–208 and 352–412, four tiers. **Already exists** as `06_LED_FIXTURE_ENV` |
| `EV-A` | Yes — envelope only | ENVELOPE | 42 mm slab at the rear face. **Already exists** as `07_PLENUM`. Do not model a real plenum until ICR-004 closes |
| `CT-A` | Yes — envelope only | ENVELOPE | Box at the rack end. **Already exists** as `11_ENCLOSURE_IP65` |
| `CT-B` | **No** | — | Volume depends entirely on `[OQ-3]` and the UPS decision. Any model would be invention |
| `AQ-LT-A` | **No** | — | Length, mounting and channel count all open |
| `AQ-CT-A` | **No** | — | Mains vs low-voltage changes the enclosure completely |
| `AQ-LP-A` | After decisions 1–3 | CONCEPT | Glass forming constraints are not respected by CAD |
| `AQ-FL-A` | **No** | — | Type and volume both open |
| `AQ-PU-A` | **No** | — | Make-or-buy may make the question moot |
| `AQ-TL-A` | **Yes** | CONCEPT | For this product, modelling *is* designing |

**Four of the five CEA envelopes already exist inside the rack assembly.** A
generation run that produces new ones has duplicated work and created a second source
of truth for the same volume. Check before building.

---

## 5. Prompt shape that works

```
Read products/<family>/<product>/PRODUCT.md.

Build a class-<ENVELOPE|CONCEPT> model of <product-id>.

Use ONLY section 3 (Inherited constraints — DECIDED) for dimensions.
Do NOT use section 4 (Industry reference points).
For every dimension not given in section 3, either:
  - omit the feature, or
  - list it as an assumption in your reply and mark it in the model name.

Name the model <PRODUCT-ID>_<CLASS>[_r<n>].
Report: which section-3 rows you used, and every assumption you made.
```

The last line is the one that matters. **A generation run that reports no assumptions
either had a complete specification or is not telling you something.**

---

## 6. After generating

1. Record the model in `docs/engineering/CAD_INDEX.md` with its class.
2. Add the reported assumptions to the product's `PRODUCT.md` §5 as decisions still
   required — an assumption made to close a model is a decision someone owes.
3. Do **not** update `PRODUCT.md` §3 from a model. Section 3 rows come from decisions
   and documents, never from geometry that had to be dimensioned to exist.
4. Do not issue a release for a non-DESIGN model. `docs/system/RELEASE_INDEX.md` is
   for engineering releases.

---

## 7. If a generated model is wrong

That is the expected outcome for CONCEPT models and is not a defect — it is the
point. Discard it and change the product document, not the model. The document is
where the learning goes.

The failure mode to watch for is the opposite: a model that looks plausible, gets
reused, and quietly becomes the specification because nobody remembers it was
generated from an incomplete brief. **The naming convention in §2 exists entirely to
stop that.**
