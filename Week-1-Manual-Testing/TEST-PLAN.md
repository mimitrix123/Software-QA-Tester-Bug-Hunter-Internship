# Test Plan — OrangeHRM Demo

## 1. Test Objective
Validate core OrangeHRM web application workflows from a manual QA perspective and identify functional, validation, navigation, session, authorization, and usability defects.

## 2. Scope
### In scope
- Login/logout
- Dashboard navigation
- Admin user management
- PIM / employee records
- Leave navigation and basic actions
- Time navigation
- Recruitment navigation
- My Info/profile data
- Search/filter controls
- Required-field and invalid-input behavior

### Out of scope
- API testing
- Database testing
- Source-code review
- Load/stress testing
- Security penetration testing
- Mobile native application testing

## 3. Test Approach
1. Smoke test the application and authentication.
2. Execute positive functional scenarios.
3. Execute negative and boundary scenarios.
4. Verify navigation and session behavior.
5. Record actual results and evidence during browser execution.
6. Log defects with reproducible steps, severity, priority, environment and evidence.
7. Re-test fixed defects and perform regression smoke tests.

## 4. Entry Criteria
- Demo URL is reachable.
- Supported browser is available.
- Valid demo credentials are available from the demo environment.
- Test cases are reviewed.

## 5. Exit Criteria
- All 35 planned cases executed or explicitly marked Blocked/Not Run.
- All reproducible defects documented.
- Critical/High defects are reviewed.
- Execution summary and evidence are attached.

## 6. Environment
| Item | Value |
|---|---|
| Application | OrangeHRM Open Source Demo |
| URL | https://opensource-demo.orangehrmlive.com/ |
| Browser | Chrome/Edge latest stable |
| OS | Windows 10/11 |
| Viewport | 1280×720+ |
| Test type | Manual functional / exploratory |

## 7. Risks
- Public demo data may be reset or changed.
- Demo availability can vary.
- Some features may require role-specific permissions.
- A defect seen in the demo may not reproduce in a production deployment.

## 8. Defect Severity
- **Critical:** Blocks a core business flow or causes severe data/security impact.
- **High:** Major feature failure with no practical workaround.
- **Medium:** Important functional or validation issue with workaround.
- **Low:** Minor UI, copy, alignment, or usability issue.

## 9. Deliverables
- 35 test cases
- Execution matrix
- Defect report
- Evidence log
- Test data/reference notes
