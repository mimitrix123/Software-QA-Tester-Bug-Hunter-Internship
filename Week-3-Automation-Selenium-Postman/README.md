# Week 3 — Web Automation with Selenium + API Testing with Postman

## Objective
Automate 10 critical web test scenarios using Selenium and prepare a Postman collection covering 5 API scenarios.

## Demo applications
- **Web UI:** SauceDemo (Swag Labs) — https://www.saucedemo.com/
- **API:** JSONPlaceholder — https://jsonplaceholder.typicode.com/

## Deliverables
- `selenium/` — Python Selenium automation suite
- `postman/` — Postman collection and environment
- `TEST-SCENARIOS.md` — automation and API scenario matrix
- `EXECUTION-REPORT.md` — results template

## Selenium scenarios
1. Valid login
2. Invalid login
3. Locked-user login
4. Product search/verification
5. Product sort
6. Add product to cart
7. Add multiple products to cart
8. Remove product from cart
9. Checkout validation
10. Complete checkout

## API scenarios
1. GET posts
2. GET post by ID
3. POST a post
4. PUT/update a post
5. DELETE a post

## Honest execution policy
The repository contains executable automation and a ready-to-import Postman collection. Execution results are not fabricated: run the Selenium suite locally and import/run the Postman collection to populate the execution report.

## Run Selenium
```bash
cd selenium
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -r requirements.txt
pytest -v
```

## Postman
Import `postman/Week-3-API-Collection.json` into Postman. The requests use JSONPlaceholder's public API and include response assertions.
