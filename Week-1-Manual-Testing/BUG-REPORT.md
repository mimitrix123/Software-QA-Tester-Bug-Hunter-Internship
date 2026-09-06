# Bug Report

## Defect reporting standard
Only defects reproduced during actual browser execution should be entered as confirmed defects. The entries below are **defect candidates/checkpoints**, not fabricated production findings.

### BUG-001 — Login error handling
- **Module:** Login
- **Severity:** High if authentication accepts invalid credentials; otherwise N/A
- **Priority:** High
- **Status:** To Verify
- **Precondition:** Login page open
- **Steps:**
  1. Enter a valid username.
  2. Enter an intentionally incorrect password.
  3. Click Login.
- **Expected:** Login is rejected and a clear error message is displayed.
- **Actual:** Record only after browser execution.
- **Evidence:** Attach screenshot after reproduction.

### BUG-002 — Required-field validation
- **Module:** Admin / Add User
- **Severity:** Medium–High depending on save behavior
- **Priority:** High
- **Status:** To Verify
- **Steps:** Open Add User, leave mandatory fields empty, click Save.
- **Expected:** Inline validation identifies required fields and prevents invalid submission.
- **Actual:** Record only after browser execution.
- **Evidence:** Attach screenshot after reproduction.

### BUG-003 — Protected-page access after logout
- **Module:** Session
- **Severity:** High if protected content remains usable after logout
- **Priority:** High
- **Status:** To Verify
- **Steps:** Log in, visit a protected page, log out, then use browser Back or a saved protected URL.
- **Expected:** Authentication is required before protected content/actions are available.
- **Actual:** Record only after browser execution.
- **Evidence:** Attach screenshot after reproduction.

## Defect template
Copy this structure for every confirmed defect:

```text
BUG-ID:
Title:
Module:
Environment:
Build/Version:
Severity:
Priority:
Status:
Precondition:
Steps to Reproduce:
1.
2.
3.
Expected Result:
Actual Result:
Reproducibility:
Attachment/Screenshot:
Notes:
```
