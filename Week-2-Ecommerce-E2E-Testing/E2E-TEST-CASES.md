# E2E Test Cases

| ID | Scenario | Expected result | Priority |
|---|---|---|---|
| E2E-001 | Login with valid account | User reaches product catalog | High |
| E2E-002 | Login with invalid account | Error shown; user remains logged out | High |
| E2E-003 | Login with locked account | Locked-user message prevents access | High |
| E2E-004 | Browse product catalog | Products, names and prices render | High |
| E2E-005 | Sort products A→Z | Products reorder alphabetically | Medium |
| E2E-006 | Sort products by price low→high | Lowest price appears first | Medium |
| E2E-007 | Open product details | Correct detail page and data display | Medium |
| E2E-008 | Add one product to cart | Cart count increases and product appears | High |
| E2E-009 | Add multiple products | All selected products appear in cart | High |
| E2E-010 | Remove product from cart | Product is removed and count updates | High |
| E2E-011 | Continue shopping from cart | User returns to catalog without losing cart | Medium |
| E2E-012 | Open checkout with empty cart | System handles empty-cart path appropriately | Medium |
| E2E-013 | Submit checkout with blank information | Required validation appears | High |
| E2E-014 | Checkout with valid customer data | Overview page opens | High |
| E2E-015 | Verify subtotal/tax/total | Calculations are internally consistent | High |
| E2E-016 | Cancel checkout | User returns to expected previous flow | Medium |
| E2E-017 | Complete purchase | Confirmation page is displayed | Critical |
| E2E-018 | Return home after purchase | User returns to catalog | Medium |
| E2E-019 | Logout after purchase | Session ends and login page appears | High |
| E2E-020 | Back navigation after logout | Protected content is not actionable without login | High |
