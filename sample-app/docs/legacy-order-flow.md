# Legacy order pricing flow

This sample represents a simplified legacy order pricing component used for the workshop demo.

## Current business rules

- Item type `A` receives a 15% discount.
- Other items receive a 10% discount when the customer tier is `G`.
- All remaining orders receive a 5% discount.
- Net amount is gross amount minus the calculated discount amount.

## Modernization discussion

Possible modernization seams:

- Wrap the existing calculation behind an API.
- Extract rules into a tested service.
- Add characterization tests before translating the logic.
- Create an ADR for the target architecture.
