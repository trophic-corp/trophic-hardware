# Lily Pipe Research Brief (Phase 0A)

**Applies to:** `AQ-LP-A` (product folder `products/aquarium/lily-pipes/`) · **Index:** `docs/references/REFERENCE_INDEX.md` LPREF

| | |
|---|---|
| **Product** | `AQ-LP-A` Lily pipes (aquarium inflow/outflow and associated components) |
| **Stage** | Phase 0A research complete 2026-09-17 — **no engineering, no CAD, nothing approved** |
| **Owner of decisions** | Karthik (product owner). Every recommendation in this folder is **PROPOSED** |
| **Governing rules** | `CLAUDE.md` §3 (authority), `docs/system/AGENT_ROUTING_POLICY.md`, `.claude/agents/industrial-design-cmf.md` (aesthetic authority) |

## 1. Business context

Trophic is a horticulture and aquascaping equipment venture in Coimbatore that designs in-house and outsources manufacturing. Lily pipes are being assessed as a new aquarium category. The goal is a practical, differentiated product that can be prototyped and launched with modest investment and manageable inventory, with design aesthetics as a core requirement alongside function, manufacturability and cost.

Target reaction (from the owner and the CMF brief): **"They cared about every detail; this is a premium, thoughtfully engineered product."** Premium by evidence of care, not luxury signalling. No ornamental luxury, no unnecessary features, no copying competitors.

Repository context:

- `products/aquarium/lily-pipes/PRODUCT.md` (Phase 0, created 2026-09-09) framed decision 1 as "glass or acrylic". This research widens that to glass / stainless steel / polymer and recommends a direction (see [DECISIONS_AND_OPEN_QUESTIONS.md](../../../products/aquarium/lily-pipes/DECISIONS_AND_OPEN_QUESTIONS.md)). The Phase 0 document is preserved; only its stage and next action are updated.
- `products/aquarium/README.md` records that the aquarium family is "real but not next" after the microgreen rollout. This research does not change that sequencing; it prepares the category so the owner can decide when to start.
- Cross-product decision **X3 (hose size standard across `AQ-LP-A` and `AQ-FL-A`)** in `products/PRODUCT_INDEX.md` is directly touched. This folder gathers evidence for it but does not decide it.
- The aquarium lighting industrial-design brief (`products/aquarium/lighting/PLATFORM.md` §10) is the established family direction. It is inherited as direction; its dry-side rules are not assumed to transfer to wet parts (see [LILY_PIPE_AESTHETIC_REFERENCE.md](LILY_PIPE_AESTHETIC_REFERENCE.md) §5).
- An earlier owner conversation (outside this repository) had already identified SS304 stainless as the likely default launch SKU over borosilicate glass because of Indian manufacturing constraints. That was treated as a hypothesis to test, not as a decision.

## 2. Research questions

| # | Question | Answered in |
|---|---|---|
| RQ1 | Who buys aftermarket lily pipes in India, why do they upgrade, what alternatives do they use? | [COMPETITOR_LILY_PIPE_REFERENCE.md](COMPETITOR_LILY_PIPE_REFERENCE.md) §2–3 |
| RQ2 | Which ownership problems recur, and which create willingness to pay rather than preference? | COMPETITOR REF §4 |
| RQ3 | What do 10–15 comparable products offer, cost and fail at, in India and as benchmarks? | COMPETITOR REF §5 |
| RQ4 | How do competitor products perform against Trophic's aesthetic principles, and where is a Trophic design language credible? | [LILY_PIPE_AESTHETIC_REFERENCE.md](LILY_PIPE_AESTHETIC_REFERENCE.md) |
| RQ5 | What engineering principles, compatibility constraints, materials and failure modes govern a future design? | [LILY_PIPE_TECHNICAL_REFERENCE.md](LILY_PIPE_TECHNICAL_REFERENCE.md) |
| RQ6 | Which manufacturing routes and suppliers are feasible for a small Indian venture? What compliance and IP questions arise? | [SOURCING_STRATEGY.md](../../../products/aquarium/lily-pipes/sourcing/SOURCING_STRATEGY.md) |
| RQ7 | What launch strategy, cost, price, channel and investment is credible? | [COMMERCIAL_FEASIBILITY.md](../../../products/aquarium/lily-pipes/costing/COMMERCIAL_FEASIBILITY.md) |
| RQ8 | What must a design meet, and how is it verified? | [PRELIMINARY_REQUIREMENTS.md](../../../products/aquarium/lily-pipes/requirements/PRELIMINARY_REQUIREMENTS.md), [VALIDATION_PLAN.md](../../../products/aquarium/lily-pipes/verification/VALIDATION_PLAN.md) |
| RQ9 | Is the category worth pursuing, and what must be verified before design? | [DECISIONS_AND_OPEN_QUESTIONS.md](../../../products/aquarium/lily-pipes/DECISIONS_AND_OPEN_QUESTIONS.md) §1 |

## 3. Boundaries

In scope: research, market analysis, feasibility, preliminary requirements, validation planning.

Out of scope, deliberately not done:

- CAD, massing models, sketches of forms, final dimensions.
- Contacting suppliers, requesting quotations, commissioning tooling or samples.
- Market-size figures without a source. Bottom-up scenarios are used instead.
- Legal, tax or IP clearance. Questions are flagged for professionals.
- Approving any requirement, supplier, price or route.

## 4. Method

Desk research on 2026-09-17 using web search and page fetches, split into five parallel streams: competitors, customer problems, technical, manufacturing/sourcing (run under the `manufacturing-sourcing-engineer` brief), and aesthetics (run under the `industrial-design-cmf` brief, which also reviewed the resulting product options). Two specialists were used, per the routing policy's Level 2 default; QA was not invoked because this is not a gate. Main Claude synthesised, built the cost model and wrote this folder.

Access limits that shape confidence (recorded so later sessions do not over-trust the result):

- **Blocked:** Amazon.in / Amazon.com product and review pages, Reddit (including Indian subreddits), Quora, aquaticplantcentral, most plantedtank.net thread bodies, FishLore thread bodies, the ADA India shop, the Chihiros store, Alibaba price rendering, most Flipkart prices.
- Consequences: no Amazon review evidence; the cheapest generic price band is under-sampled; ADA India official prices are missing; customer evidence is weighted to UK and Singapore forums plus Indian retailer pages.
- Page content was read through a summarising fetch, so quoted phrases and poster counts are approximate. Check the original before reusing a quote or a figure in a requirement.
- No images were viewed. All visual judgements of competitors are inferred from descriptions and marked as such.

## 5. Evidence and status conventions (used in every document here)

Evidence class of a statement:

| Tag | Meaning |
|---|---|
| **[M]** | Manufacturer page, manual, datasheet |
| **[D]** | Authorised distributor |
| **[R]** | Retailer listing (price, availability; may garble specifications) |
| **[F]** | Community / forum field experience |
| **[B]** | Blog or editorial |
| **[T]** | Standard, technical reference, materials datasheet |
| **[I]** | Inference by Claude or a specialist agent — not sourced |
| **EST** | Engineering estimate or hand calculation — not a quote, not validated |

Status of a statement:

| Status | Meaning |
|---|---|
| **FACT** | Sourced observation, with the source and access date |
| **ESTIMATE** | Quantified judgement with stated basis; replace with a quote or measurement |
| **HYPOTHESIS** | A claim to be tested (customer, technical or commercial) |
| **PROPOSED** | A recommendation or requirement awaiting owner approval |
| **APPROVED** | Owner-approved. **Nothing in this folder is APPROVED as of 2026-09-17** |

Industry reference points follow `CLAUDE.md` §3 rule 6: competitor dimensions and market values may inform a conversation; they may never appear on a drawing, in a model claimed as a design, or in a contract.

## 6. Working assumptions (explicit, all revisable)

| # | Assumption | Why it was needed | Test |
|---|---|---|---|
| A1 | Primary market is Indian planted-tank hobbyists buying through specialist online stores and local fish stores; international sales are later | Sets price, channel and compliance scope | Interviews V-C1–C4 |
| A2 | Initial volumes are hundreds of sets per year, not thousands | Rules out injection moulds and hydroforming at launch | Channel interviews, pilot sell-through |
| A3 | Canister filters are the target (not hang-on or sump) | Hose-barb interface | Interview hose survey |
| A4 | Rimless glass tanks are the primary mounting case; rimmed tanks secondary | Clip range | Tank-builder survey V-M3 |
| A5 | GST at 18% applies to the finished product and its inputs; input GST is recoverable | Cost model | CA confirmation |
| A6 | USD/INR ≈ 94.7 (x-rates.com September 2026 month-to-date average, accessed 2026-09-17); EUR prices are left in EUR | Benchmark conversions | Refresh at RFQ |
| A7 | Owner design time is not costed as cash | Fixed-cost model | Owner |
