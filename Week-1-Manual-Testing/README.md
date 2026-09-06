# Week 1 — Manual Testing: OrangeHRM Demo

## Objective
Perform a structured manual QA assessment of the OrangeHRM demo web application, covering test planning, functional test design, execution tracking, defect reporting, and evidence management.

## Application Under Test
- **Application:** OrangeHRM Open Source Demo
- **URL:** https://opensource-demo.orangehrmlive.com/
- **Primary areas:** Login, Dashboard, Admin/User Management, PIM/Employee Management, Leave, Time, Recruitment, My Info, Search, Navigation and Logout.
- **Reference:** OrangeHRM documentation confirms the standard login flow and employee-management areas. See the official help documentation linked below.

## Deliverables
| Artifact | File |
|---|---|
| Test Plan | `TEST-PLAN.md` |
| 35 Manual Test Cases | `TEST-CASES.md` |
| Execution Report | `TEST-EXECUTION.md` |
| Bug Report | `BUG-REPORT.md` |
| Screenshot / Evidence Log | `EVIDENCE.md` |
| Test Data | `TEST-DATA.md` |

## QA Scope
- Functional testing
- Positive and negative testing
- Boundary/input validation
- Navigation and session behavior
- Basic authorization checks
- Usability observations
- Regression smoke coverage

## Important execution note
The public demo is JavaScript-driven. The connected web inspection can confirm that the demo URL resolves to the OrangeHRM login route, but it cannot execute the application UI like a real browser. Therefore, this repository deliberately separates **designed test cases** from **browser-observed results** and does not fabricate PASS/FAIL evidence or screenshots. The execution sheet is ready for a real browser run.

## Official references
- OrangeHRM demo: https://opensource-demo.orangehrmlive.com/
- OrangeHRM Employee Management guide: https://help.orangehrm.com/hc/en-us/articles/41780167795481-How-to-Access-the-Employee-Management
- OrangeHRM Dashboard guide: https://help.orangehrm.com/hc/en-us/articles/18325115741465-How-to-access-the-Dashboard

## Suggested browser environment
- Chrome/Edge latest stable
- Windows 10/11 or equivalent
- 1280×720 or higher
- Clear browser cache before a fresh run

## Result
This Week 1 package provides a portfolio-ready manual QA structure with 35 test cases, a formal test plan, execution matrix, defect-report format, and screenshot evidence log.