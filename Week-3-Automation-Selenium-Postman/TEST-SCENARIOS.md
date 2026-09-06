# Week 3 Test Scenarios

## Selenium — 10 scenarios
| ID | Scenario | Expected |
|---|---|---|
| WEB-01 | Valid login | User reaches inventory page |
| WEB-02 | Invalid login | Error message displayed; login blocked |
| WEB-03 | Locked user | Locked-account message displayed |
| WEB-04 | Verify product catalog | Products and prices are displayed |
| WEB-05 | Sort products by price | Product order changes correctly |
| WEB-06 | Add product to cart | Cart badge increments and item appears |
| WEB-07 | Add multiple products | All selected items appear in cart |
| WEB-08 | Remove product | Item disappears and cart count updates |
| WEB-09 | Checkout validation | Missing required checkout fields are rejected |
| WEB-10 | Complete checkout | Confirmation page is displayed |

## API — 5 scenarios
| ID | Request | Expected |
|---|---|---|
| API-01 | GET /posts | HTTP 200 and JSON array |
| API-02 | GET /posts/1 | HTTP 200; id=1 |
| API-03 | POST /posts | HTTP 201 and created object contains request fields |
| API-04 | PUT /posts/1 | HTTP 200 and updated title/body are returned |
| API-05 | DELETE /posts/1 | HTTP 200 |
