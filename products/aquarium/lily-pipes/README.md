# Lily Pipes (`AQ-LP-A`)

**Stage:** Phase 0A research complete · decisions 1–3 answered by the owner (2026-09-17: EDR-021/022/023) · **CONCEPT CAD round 1 may start** · Stage 0B validation not started · no engineering, no DESIGN-class CAD.

Aquarium inflow/outflow pipes and associated components for canister filters. All recommendations are **PROPOSED** until the owner approves them.

## Start here

1. [CURRENT_STATE.md](CURRENT_STATE.md) — one-page status, decisions, next actions. **Enough to resume a session.**
2. [design/CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md) and [design/CONCEPT_R1_FUSION_PROMPT.md](design/CONCEPT_R1_FUSION_PROMPT.md) — Fusion 360 concept round 1.
3. [requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md](requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md) — proposed launch specification (only L-02, L-05/06, L-40 approved).
4. [DECISIONS_AND_OPEN_QUESTIONS.md](DECISIONS_AND_OPEN_QUESTIONS.md) — decision brief, open decisions D-01–D-19, design handoff checklist.
5. Load other documents only when the task needs them.

## Where things live (repository conventions)

Product-owned documents follow the rack's lifecycle folders (`products/cea/racks/rack-platform/`); research follows the lighting programme's split between the product folder and `docs/references/`. Sub-folders exist only where there is content (`products/PRODUCT_INDEX.md`, "Adding a product").

| Location | Document | Owns | Load when |
|---|---|---|---|
| `./` | [PRODUCT.md](PRODUCT.md) | Phase 0 scope: §3a decided, §5 open, §8 CAD readiness | Any work on this product |
| `./` | [CURRENT_STATE.md](CURRENT_STATE.md) | Status, decided/open, next actions, history | Resuming |
| `./` | [DECISIONS_AND_OPEN_QUESTIONS.md](DECISIONS_AND_OPEN_QUESTIONS.md) | Decision brief, RC-1–8, D-01–D-19, handoff checklist (records in `docs/decisions/`) | Deciding |
| `requirements/` | [AQ-LP-A-BRIEF_RevP0_launch-specification.md](requirements/AQ-LP-A-BRIEF_RevP0_launch-specification.md) | Launch specification Rev P0: L-01–L-105 with basis, confidence, confirming check (registered in `docs/system/DOCUMENT_REGISTER.md`, CURRENT WORKING) | What to launch; design targets |
| `requirements/` | [PRELIMINARY_REQUIREMENTS.md](requirements/PRELIMINARY_REQUIREMENTS.md) | PROPOSED requirements PR-* with rationale, evidence, priority, verification | Scope and design review |
| `design/` | [CONCEPT_DESIGN_BRIEF.md](design/CONCEPT_DESIGN_BRIEF.md) | Concept round 1: class and naming, parameters, hook geometry, modelling sequence, rules, checks | CAD work |
| `design/` | [CONCEPT_R1_FUSION_PROMPT.md](design/CONCEPT_R1_FUSION_PROMPT.md) | Paste-ready prompt for a Fusion session; concept reports go to `design/concepts/` | Starting a CAD session |
| `verification/` | [VALIDATION_PLAN.md](verification/VALIDATION_PLAN.md) | Stages and gates; V-C, V-M, V-T, V-A, V-S, V-P activities and proposed acceptance | Planning or running tests |
| `sourcing/` | [SOURCING_STRATEGY.md](sourcing/SOURCING_STRATEGY.md) | Routes, supplier shortlist S01–S23, cost data, duty/GST, RFQ questions, compliance/IP, §9 location assessment | Sourcing, RFQs, compliance |
| `sourcing/` | [supplier_shortlist.csv](sourcing/supplier_shortlist.csv) | S01–S23 as data | Updating suppliers |
| `costing/` | [COMMERCIAL_FEASIBILITY.md](costing/COMMERCIAL_FEASIBILITY.md) | Launch options P1–P3, unit cost, price bands, contribution by channel, investment, break-even | Economics, channels |
| `costing/` | [MANUFACTURING_COST_AND_MARGIN.md](costing/MANUFACTURING_COST_AND_MARGIN.md) | Per-step COGS, location cost effect, margin ladder, illustrative P&L | Cost or profit |
| `costing/` | `unit_economics_model.py`, `margin_model.py`, `unit_economics_outputs.csv` | Models behind the two costing documents; re-run after quotes | Updating figures |
| `docs/references/lily-pipes/` | [LILY_PIPE_RESEARCH_BRIEF.md](../../../docs/references/lily-pipes/LILY_PIPE_RESEARCH_BRIEF.md) | Context, research questions, method, **evidence and status tags**, assumptions A1–A7 | Interpreting any tag |
| `docs/references/lily-pipes/` | [COMPETITOR_LILY_PIPE_REFERENCE.md](../../../docs/references/lily-pipes/COMPETITOR_LILY_PIPE_REFERENCE.md) | Segments, customer problems, competitor matrix, Indian price bands, volume scenarios | Market questions |
| `docs/references/lily-pipes/` | [LILY_PIPE_AESTHETIC_REFERENCE.md](../../../docs/references/lily-pipes/LILY_PIPE_AESTHETIC_REFERENCE.md) | C1–C12 rubric, competitor evaluation, opportunities O1–O11, CMF review | Form, finish, CMF |
| `docs/references/lily-pipes/` | [LILY_PIPE_TECHNICAL_REFERENCE.md](../../../docs/references/lily-pipes/LILY_PIPE_TECHNICAL_REFERENCE.md) | Diameter vocabulary, hose compatibility, flow, intake, skimmer, mounting, materials, risk register R01–R20 | Engineering questions (hose data also serves `AQ-FL-A`, X3) |
| `docs/references/lily-pipes/sources/` | [SOURCE_REGISTER.md](../../../docs/references/lily-pipes/sources/SOURCE_REGISTER.md), `competitor_matrix.csv`, `hose_compatibility.csv` | Grouped sources, blocked sources, research data | Re-checking evidence |
| `docs/decisions/records/` | EDR-021, EDR-022, EDR-023 | Owner decisions 1–3 | Changing a decision |

**Short references used inside the documents:** COMPETITOR REF = `COMPETITOR_LILY_PIPE_REFERENCE.md` · TECHNICAL REF = `LILY_PIPE_TECHNICAL_REFERENCE.md` · AESTHETIC REF = `LILY_PIPE_AESTHETIC_REFERENCE.md` · SOURCING = `SOURCING_STRATEGY.md` · COMMERCIAL = `COMMERCIAL_FEASIBILITY.md` · DECISIONS = `DECISIONS_AND_OPEN_QUESTIONS.md`.

## Rules that apply here

- Competitor dimensions and market values are **industry reference points, not Trophic decisions** (`CLAUDE.md` §3 rule 6).
- Aesthetic authority is `.claude/agents/industrial-design-cmf.md` and `products/aquarium/lighting/PLATFORM.md` §10. This product does not redefine it.
- Hose-size standard for the range is cross-product decision **X3** (`products/PRODUCT_INDEX.md`); the lily-pipe launch size is EDR-022.
- CONCEPT-class CAD only (`AQ-LP-A_CONCEPT_r<n>`), per the concept brief and `docs/system/CAD_SEED_GUIDE.md`. `drawings/`, `manufacturing/`, `release/` and `changes/` folders are created only when DESIGN-class work exists.
- Controlled documents take a Doc ID and revision (`<DOC-ID>_<Rev>_<slug>`, `platform/IDENTIFIER_STANDARD.md`) and a row in `docs/system/DOCUMENT_REGISTER.md`; Phase 0 working and research documents keep plain names, as in the lighting programme.
- Update [CURRENT_STATE.md](CURRENT_STATE.md) when a decision, test result or quote lands; edit the document that owns the finding rather than copying it.
