# Agent Routing Policy

How Main Claude routes work to the six project-scoped specialist agents in
`.claude/agents/`. Read this before deciding whether to delegate. The
operating principle:

> One main Claude session owns the task. Specialists are consulted only when
> their domain materially changes the answer. QA is a gate, not a
> participant in every conversation.

Agent roster: `systems-architect`, `lighting-electronics-engineer`,
`plant-science-specialist`, `industrial-design-cmf`,
`manufacturing-sourcing-engineer`, `qa-reliability-engineer`. Each agent's own
file states its domain, when to use it, when not to, and its authority
boundary — this document only governs *routing between* them.

---

## Routing levels

**Level 0 — Main Claude only.** No specialist for: simple questions,
formatting, file navigation, index updates, straightforward documentation
maintenance, retrieving already-known repository facts, small edits with no
engineering consequence.

**Level 1 — one specialist.** A task contained primarily within one domain
goes to that one specialist; Main Claude synthesizes the result. Examples:
LED architecture → Lighting/Electronics. Microgreen spectral literature →
Plant Science. Aquarium fixture visual direction → Industrial Design/CMF.
Coimbatore extrusion sourcing → Manufacturing/Sourcing. Test plan review →
QA/Reliability.

**Level 2 — cross-domain, at most two specialists by default.** Examples:
aquarium LED spectrum → Lighting/Electronics + Plant Science, reconciled by
Main Claude. Shared Core/WRGB chassis → Systems Architect +
Manufacturing/Sourcing. Lighting enclosure appearance → Industrial
Design/CMF + Lighting/Electronics, with Main Claude reconciling aesthetics
against thermal/optical constraints. Do not automatically add QA at this
level.

**Level 3 — verification/gate work.** Invoke QA/Reliability specifically
when the task is: verifying a design, reviewing engineering evidence,
approving a phase transition, manufacturing readiness, qualification,
validation, release, a safety-critical change, or resolving a meaningful
failure. Pattern: domain specialist produces evidence → QA reviews it → Main
Claude synthesizes. QA reviews; it does not redesign unless asked to propose
corrective options.

A third specialist may be used only when a task genuinely spans three
independent high-impact domains or is a major engineering gate — never as a
default. Never run the full roster (Architect → Electronics → Botanist →
Design → Manufacturing → QA) on an ordinary change; that increases token use
while often reducing clarity.

## Routing table

| Task | Primary | Optional second | QA? |
|---|---|---|---|
| Product/platform architecture | Systems Architect | relevant domain | Gate only |
| LED/driver/PSU/electronics | Lighting/Electronics | Systems Architect | Gate only |
| Spectrum/crop/aquatic plant question | Plant Science | Lighting/Electronics | No |
| Form/CMF/product aesthetics | Industrial Design/CMF | relevant engineer | No |
| DFM/MOQ/supplier/manufacturing | Manufacturing/Sourcing | relevant engineer | Qualification only |
| Validation/reliability/release | QA/Reliability | relevant domain | Yes |
| Simple repository/document work | Main Claude | none | No |

## When specialists disagree

Main Claude does not average two recommendations into a compromise. Instead:
1. identify the actual disagreement;
2. identify what evidence would resolve it;
3. preserve both views if unresolved;
4. mark the item `NEEDS DECISION` / `NEEDS VALIDATION` per the repository's
   existing conventions;
5. never choose a middle position simply because it sits between the two.

## Agents do not create authority

An agent recommendation is not authoritative engineering truth. Agents may
analyze, research, calculate, critique, recommend, identify risks, and
propose tests. They may not independently approve a product, alter an
approved requirement, change an authoritative CAD model, mark a product
Validated/Released, change a frozen interface, convert research into a
specification, or write an ADR/EDR/ICR as "decided." The repository's
existing authority and decision mechanisms (CLAUDE.md §3–4,
`docs/decisions/DECISION_REGISTER.md`) remain controlling regardless of what
any agent recommends.

## Context discipline

Each specialist determines its own minimum authoritative working set before
reading anything (see each agent's own file). None should load the entire
repository, `archive/**`, unrelated products, large manufacturing packs, or
full CAD documentation unless the delegated task actually requires it. For
research-only delegations, the specialist returns a compact conclusion
rather than flooding Main Claude's context with raw sources.

## Research priority

When fresh external information matters: (1) standards/official regulatory
material, (2) manufacturer datasheets, (3) peer-reviewed research, (4)
authorized distributors, (5) credible technical sources, (6) community
experience only for genuine field-experience questions. Every
research-derived recommendation distinguishes: known fact / manufacturer
claim / research finding / engineering inference / Trophic assumption /
Trophic decision. Don't re-research what `docs/references/**` already
maintains unless it's outdated or insufficient.

## Lighting vs. Plant Science — kept separate on purpose

Plant Science answers "what biological outcome is desirable." Lighting/
Electronics answers "how could hardware produce and control it." Neither
answers "what should Trophic manufacture" alone — that product decision is
Main Claude's, informed by biology, electronics, manufacturing, and
commercial constraints together.

## Industrial Design vs. Engineering

Industrial Design/CMF should enter early enough to influence the product,
not merely decorate finished engineering — but its recommendations never
silently override physical constraints. Preferred flow: product intent →
engineering envelope + visual intent → CMF exploration in dialogue with the
relevant engineering specialist → converged concept. Trophic's design
character is premium by evidence of care, not premium by luxury signalling
(see the agent's own file for the full aesthetic brief).

## No nested delegation

Specialists do not spawn other specialists. Main Claude coordinates all
cross-domain work directly (`Main → Specialist A` and `Main → Specialist B`,
never `Main → Architect → Electronics → ...`). This keeps delegation
traceable and keeps cost and context bounded.

## Not yet agents

No dedicated agent exists yet for: mechanical engineering, firmware,
software, cybersecurity, DevOps, finance, marketing, product management,
regulatory affairs, optical engineering, CAD/Fusion, procurement operations,
documentation, or project management. For now: mechanical questions →
Main Claude + Systems Architect; optical lighting → Lighting/Electronics;
manufacturing mechanics → Manufacturing/Sourcing; firmware/interface
questions → Lighting/Electronics + Systems Architect; software stays in the
separate software repository; regulatory interpretation → QA with specialist
research. Add another permanent agent only when repeated work proves an
independent context/domain is actually necessary.
