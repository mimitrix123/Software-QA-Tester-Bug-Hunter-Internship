# Jira-Ready Bug Log — 15+ Defects

> **Verification status:** Candidate defects/checkpoints. Reproduce each against the current demo build before creating a real Jira ticket. Do not represent these as actual Jira issues until Jira confirms them.

| ID | Jira Summary | Severity | Priority | Initial status | Lifecycle target |
|---|---|---|---|---|---|
| BUG-001 | Invalid login should display a clear authentication error | Medium | High | Open | Open → In Progress → Resolved → Closed |
| BUG-002 | Locked account should clearly explain access restriction | Medium | High | Open | Open → In Progress → Resolved → Closed |
| BUG-003 | Empty username/password submission should validate required fields | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-004 | Product catalog should preserve correct product name/price pairing | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-005 | Product sorting A→Z should be deterministic | Medium | Medium | Open | Open → In Progress → Resolved → Closed |
| BUG-006 | Price low→high sorting should place minimum price first | Medium | Medium | Open | Open → In Progress → Resolved → Closed |
| BUG-007 | Product detail should match selected catalog product | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-008 | Cart badge should update immediately after add/remove | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-009 | Removing an item should update cart contents consistently | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-010 | Empty-cart checkout should not permit invalid order submission | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-011 | Checkout required-field validation should identify missing data | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-012 | Checkout should retain selected products and quantities | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-013 | Checkout subtotal should equal sum of cart item prices | Critical | High | Open | Open → In Progress → Resolved → Closed |
| BUG-014 | Tax should be calculated from the displayed subtotal according to app rules | High | High | Open | Open → In Progress → Resolved → Closed |
| BUG-015 | Checkout total should equal subtotal plus tax | Critical | High | Open | Open → In Progress → Resolved → Closed |
| BUG-016 | Successful checkout should display order confirmation | Critical | High | Open | Open → In Progress → Resolved → Closed |
| BUG-017 | Logout should invalidate access to protected application actions | Critical | High | Open | Open → In Progress → Resolved → Closed |
| BUG-018 | Browser back after logout should not expose an actionable authenticated session | High | High | Open | Open → In Progress → Resolved → Closed |

## Jira fields to capture
For each verified defect add:
- Jira issue key
- Reporter
- Assignee
- Component
- Environment
- Browser/OS
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Screenshot/video
- Linked test case
- Fix version
- Resolution
- Retest evidence

## Important
These are deliberately phrased as **testable defect hypotheses**. A QA portfolio should never claim a bug was found, fixed, or closed without execution evidence and an actual issue record.