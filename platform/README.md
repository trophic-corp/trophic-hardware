# platform — shared standards across all Trophic hardware

What every Trophic product inherits, regardless of family. A product does not
re-decide these; it either complies or raises a decision record to deviate.

| Document | Covers |
|---|---|
| `IDENTIFIER_STANDARD.md` | Product IDs, part numbers, document series, instrument tags |
| `mechanical-standards/README.md` | Materials, sections, hole grid, fasteners, finish, ergonomics |
| `electrical-standards/README.md` | ELV boundary, protection, earthing, connectors, enclosure |
| `PRODUCT_TEMPLATE.md` | The Phase 0 document every new product starts from |

## Provenance

**Everything here was extracted from decisions already made and validated on the
CEA Rack Platform.** Nothing was invented to fill the folder. Where a standard is
currently rack-specific and has not been proven to generalise, it says so.

The aquarium family will stress-test these: a glass lily pipe has no use for a
50 mm hole grid, and a 12 V aquarium light does not need a Type A RCBO. Expect the
mechanical standards to split into "structural steel products" and "everything else"
once the second family has real engineering. That is a normal outcome, not a failure
of the standard.
