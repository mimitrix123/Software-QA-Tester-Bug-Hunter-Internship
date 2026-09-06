# Manual Test Cases — OrangeHRM Demo

**Total: 35 test cases**

| ID | Module | Test scenario | Preconditions | Steps | Expected result | Priority |
|---|---|---|---|---|---|---|
| TC-001 | Login | Login with valid credentials | Login page open; valid demo credentials available | Enter username/password; click Login | User is authenticated and lands on Dashboard | High |
| TC-002 | Login | Login with invalid password | Login page open | Enter valid username + invalid password; Login | Error is shown and user remains logged out | High |
| TC-003 | Login | Login with invalid username | Login page open | Enter invalid username + valid password; Login | Error is shown and user remains logged out | High |
| TC-004 | Login | Submit blank login form | Login page open | Click Login with both fields blank | Required validation appears; no login | High |
| TC-005 | Login | Blank username with password | Login page open | Leave username blank; enter password; Login | Username required validation appears | Medium |
| TC-006 | Login | Blank password with username | Login page open | Enter username; leave password blank; Login | Password required validation appears | Medium |
| TC-007 | Login | Password masking | Login page open | Type password | Password is obscured | Low |
| TC-008 | Login | Logout | Logged in | Open user menu; click Logout | Session ends and login page is displayed | High |
| TC-009 | Session | Back after logout | Logged in, then logged out | Use browser Back | Protected page is not accessible without authentication | High |
| TC-010 | Dashboard | Dashboard loads after login | Logged in | Observe dashboard | Dashboard widgets/navigation load without blocking errors | High |
| TC-011 | Navigation | Open Admin module | Logged in with permitted account | Click Admin | Admin page opens | High |
| TC-012 | Navigation | Open PIM module | Logged in | Click PIM | Employee management page opens | High |
| TC-013 | Navigation | Open Leave module | Logged in | Click Leave | Leave module opens | Medium |
| TC-014 | Navigation | Open Time module | Logged in | Click Time | Time module opens | Medium |
| TC-015 | Navigation | Open Recruitment module | Logged in | Click Recruitment | Recruitment module opens | Medium |
| TC-016 | Navigation | Open My Info | Logged in | Click My Info | Employee personal-information page opens | Medium |
| TC-017 | Admin | Search user by username | Admin accessible | Enter known username; Search | Matching user is returned | High |
| TC-018 | Admin | Search with nonexistent username | Admin accessible | Enter random nonexistent username; Search | No matching record is shown | Medium |
| TC-019 | Admin | Reset Admin search | Admin accessible | Enter filter; click Reset | Filter fields clear and results return to default state | Medium |
| TC-020 | Admin | Open Add User form | Admin accessible | Click Add | Add User form opens | High |
| TC-021 | Admin | Submit Add User with required fields blank | Add User form open | Click Save without data | Required validations appear; record is not saved | High |
| TC-022 | Admin | Cancel Add User | Add User form open | Enter data; click Cancel | Form closes without creating a user | Medium |
| TC-023 | PIM | Search employee by name | PIM accessible; known employee exists | Enter employee name; Search | Matching employee is displayed | High |
| TC-024 | PIM | Search nonexistent employee | PIM accessible | Enter nonexistent name; Search | No matching employee is shown | Medium |
| TC-025 | PIM | Reset employee search | PIM accessible | Enter filter; Reset | Search criteria clear | Medium |
| TC-026 | PIM | Open employee record | Known employee listed | Click employee | Employee detail page opens | High |
| TC-027 | PIM | Validate required employee field | Employee edit page open | Clear a required field; Save | Validation prevents invalid save | High |
| TC-028 | PIM | Cancel employee edit | Employee edit page open | Modify a field; Cancel | Changes are discarded | Medium |
| TC-029 | Leave | Open Leave List | Logged in | Navigate Leave > Leave List | Leave list page opens | Medium |
| TC-030 | Leave | Search/filter leave records | Leave list open | Set a filter; Search | Results reflect selected criteria | Medium |
| TC-031 | Time | Open Timesheets | Logged in | Navigate Time > Timesheets | Timesheets page opens | Medium |
| TC-032 | Recruitment | Open Candidates | Logged in | Navigate Recruitment > Candidates | Candidates page opens | Medium |
| TC-033 | My Info | Open personal details | Logged in | Navigate My Info > Personal Details | Personal Details page opens | Medium |
| TC-034 | UI/Usability | Verify navigation labels and layout | Logged in | Inspect primary navigation and page headings | Labels are readable, consistent, and controls are usable | Low |
| TC-035 | Session | Refresh protected page while logged in | Logged in | Refresh current protected page | Page remains available and session remains valid | Medium |

## Execution convention
For the actual browser run, record one of: **PASS**, **FAIL**, **BLOCKED**, **NOT RUN**. Add the execution date, browser, tester, actual result and evidence filename in `TEST-EXECUTION.md`.
