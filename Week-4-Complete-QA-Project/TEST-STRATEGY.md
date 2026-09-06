# QA Test Strategy

## Approach
Use a risk-based pyramid: broad manual functional coverage, focused Selenium automation for repeatable critical user journeys, API assertions for service contracts, and a controlled JMeter workload for performance baselining.

## Priority model
- **P0:** authentication, checkout completion, order confirmation, data integrity
- **P1:** inventory, cart, product details, sorting, logout
- **P2:** usability, navigation, negative/boundary scenarios

## Automation principles
Prefer stable `data-test` attributes, explicit waits where needed, independent tests, deterministic test data, and cleanup through browser teardown.

## API strategy
Validate HTTP status, response structure, identifiers, and request/response field consistency for GET, POST, PUT, and DELETE operations.

## Performance strategy
The JMeter artifact models 100 concurrent virtual users with a ramp-up and repeated requests. Treat results as a baseline only and execute only against an environment where load testing is authorized.

## Defect management
Record reproducible defects with severity, priority, environment, steps, expected/actual behavior, evidence, and lifecycle state.

## Reporting
Separate designed coverage from executed evidence. Never infer PASS/FAIL or performance metrics without an actual run.
