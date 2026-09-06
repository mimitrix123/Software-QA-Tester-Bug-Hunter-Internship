# Week 4 — Complete QA Engineering Project

## Application under test
**SauceDemo / Swag Labs** — a demo e-commerce web application.

## Project scope
This capstone combines manual QA, Selenium UI automation, API testing with Postman, and JMeter performance testing.

### Deliverables
- `TEST-PLAN.md` — project test plan
- `TEST-STRATEGY.md` — risk-based QA strategy
- `TEST-CASES.md` — 60 manual test cases
- `selenium/test_saucedemo_15.py` — 15 critical Selenium scenarios
- `selenium/requirements.txt` — Python dependencies
- `postman/Week-4-API-Collection.json` — 5-request Postman collection
- `jmeter/saucedemo-load-test.jmx` — 100-user JMeter plan
- `EXECUTION-REPORT.md` — evidence/result template
- `QA-PORTFOLIO.md` — professional portfolio summary

## Execution
### Selenium
```bash
cd selenium
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
pytest -v test_saucedemo_15.py
```

### Postman
Import `postman/Week-4-API-Collection.json` and run the collection.

### JMeter
Run the JMX in non-GUI mode after confirming the target environment is permitted for load testing:
```bash
jmeter -n -t jmeter/saucedemo-load-test.jmx -l results.jtl -e -o report
```

## Evidence policy
The repository includes executable test assets and structured documentation. PASS/FAIL metrics and JMeter performance numbers are intentionally not fabricated. Populate `EXECUTION-REPORT.md` only from actual runs.
