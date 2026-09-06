# Week 4 Execution Report

## Summary
This report is intentionally an evidence template. The repository contains the complete test assets, but no test result is marked PASS/FAIL until the assets are actually executed.

| Area | Planned | Executed | Passed | Failed | Blocked |
|---|---:|---:|---:|---:|---:|
| Manual | 60 | Pending | — | — | — |
| Selenium | 15 | Pending | — | — | — |
| Postman | 5 | Pending | — | — | — |
| JMeter | 100 users | Pending | — | — | — |

## Selenium evidence
Command: `pytest -v selenium/test_saucedemo_15.py`

Record browser, driver version, execution date, duration, pass/fail counts, and screenshots after execution.

## Postman evidence
Import and run `postman/Week-4-API-Collection.json`. Record collection-run summary and response assertions.

## JMeter evidence
Run `jmeter -n -t jmeter/saucedemo-load-test.jmx -l results.jtl -e -o report` only against an authorized test environment. Record throughput, average/median response time, p90/p95/p99, error rate, and observed bottlenecks.

## Defect summary
Record only defects reproduced during the execution cycle. Link each defect to test-case ID and evidence.
