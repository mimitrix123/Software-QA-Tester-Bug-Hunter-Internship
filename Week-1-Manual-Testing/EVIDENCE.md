# Screenshot & Evidence Log

## Evidence policy
Screenshots are execution evidence and must correspond to a real browser run. This project does not include invented screenshots.

## Naming convention
Use:
`TC-XXX_<short-description>.png`

Examples:
- `TC-001_valid-login.png`
- `TC-002_invalid-password-error.png`
- `TC-021_add-user-required-validation.png`
- `BUG-001_login-error.png`

## Capture checklist
For each failed test:
- Include the application/page context.
- Include the relevant input or state.
- Keep sensitive credentials out of screenshots.
- Capture the error message and affected control where possible.
- Add the screenshot filename to `TEST-EXECUTION.md` and `BUG-REPORT.md`.

## Evidence table
| Evidence | Related test/bug | Description |
|---|---|---|
| Pending browser execution | — | No screenshots claimed until reproduced in a real browser. |
