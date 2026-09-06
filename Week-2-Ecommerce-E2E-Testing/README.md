# Week 2 — E-Commerce End-to-End Testing

## Project
End-to-end manual QA of a demo e-commerce application using **SauceDemo / Swag Labs**.

## Objective
Test the complete shopping journey: authentication → product discovery → product details → cart → checkout → order completion → logout, including negative scenarios and defect lifecycle management.

## Deliverables
- `TEST-PLAN.md` — E2E scope, strategy, environments and exit criteria
- `BUG-LOG.md` — 15+ Jira-ready defects with severity, priority and lifecycle
- `JIRA-LIFECYCLE.md` — Open → In Progress → Resolved → Closed workflow
- `TEST-SUMMARY.md` — management-style test summary
- `JIRA-IMPORT.csv` — Jira-ready CSV data for manual/import mapping
- `E2E-TEST-CASES.md` — core end-to-end test scenarios

## Important QA integrity note
The 15+ entries are **Jira-ready defect candidates derived from the demo application's known challenge/test-account behavior and intended for verification**, not fabricated claims of live Jira tickets. Actual Jira issue IDs and Open→Closed timestamps require access to a Jira project. The repository therefore documents the complete lifecycle and provides import-ready data without pretending that Jira actions were performed when no Jira connector/account is available.

## Target flow
1. Login
2. Browse products
3. Sort/filter
4. Open product details
5. Add/remove products
6. Review cart
7. Checkout information
8. Checkout overview
9. Complete purchase
10. Validate order confirmation
11. Logout

## Portfolio outcome
This project demonstrates practical manual QA skills: E2E test design, negative testing, defect classification, Jira workflow knowledge, traceability, regression thinking and release reporting.