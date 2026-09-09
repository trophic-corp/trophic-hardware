# PRODUCT TEMPLATE — Phase 0

Copy this to `products/<family>/<product>/PRODUCT.md` when a new product starts.
Delete guidance in *italics* as you fill it in.

The point of a Phase 0 document is to hold **what is known and what is not**, sharply
separated, so that CAD work can begin without anyone inventing the gaps. A Phase 0
document that reads like a finished specification is a failure — it means someone
filled in numbers nobody decided.

---

## Header

| | |
|---|---|
| **Product ID** | *from `platform/IDENTIFIER_STANDARD.md`* |
| **Family** | CEA / Aquarium |
| **Owner class** | A product · B shared infrastructure · C facility reference |
| **Stage** | **Phase 0 — no engineering** / Concept / Design / Validated / Released |
| **Authoritative CAD** | *none yet* |

## 1. What the product is

*Two or three sentences. What it does, who uses it, what it replaces. No dimensions.*

## 2. Why it exists

*The problem. If the answer is "to complete the product range", say so honestly —
that is a real reason, and a reader deserves to know the product is range-filling
rather than problem-driven.*

## 3. Inherited constraints — DECIDED

*Facts this product must comply with because another product or a published contract
already fixed them. Every row cites its source. **If you cannot cite it, it does not
belong in this section.***

| Constraint | Value | Source |
|---|---|---|

## 4. Industry reference points — NOT TROPHIC DECISIONS

*Optional. Typical market values that bound the design space, clearly labelled as
external reference. These may inform a decision; they are never a substitute for one,
and no drawing may cite this section.*

| Item | Typical range | Note |
|---|---|---|

## 5. Open — must be decided before CAD

*The real content of a Phase 0 document. Each row is a decision someone has to make.*

| # | Decision required | Blocks |
|---|---|---|

## 6. Explicitly not decided

*State the absence of things a reader might otherwise assume exist: dimensions,
materials, BOM, cost, performance figures. This section prevents a future reader —
human or model — from treating silence as permission to invent.*

## 7. Interfaces

*Which platform standards apply, which do not, and why. What this product exposes to
others. Anything crossing to software goes through `trophic-contracts`, never direct.*

## 8. CAD readiness

| Question | Answer |
|---|---|
| Can a representative 3D model be built now? | Yes / No / Massing only |
| What would that model be good for? | *layout, clash, visualisation, nothing* |
| What must NOT be inferred from it? | *dimensions, tolerances, manufacturability* |

*See `docs/system/CAD_SEED_GUIDE.md` for what a model generated from this document
may and may not claim.*

## 9. Next action

*One thing. Usually "answer decision N in §5", not "start modelling".*
