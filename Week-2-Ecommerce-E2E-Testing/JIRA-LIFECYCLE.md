# Jira Bug Lifecycle

## Standard workflow

```text
OPEN
  ↓
IN PROGRESS
  ↓
RESOLVED
  ↓
RETEST
  ↓
CLOSED
```

### Rejection path
```text
OPEN → WON'T FIX / DUPLICATE / NOT A BUG
```

### Failed retest
```text
RESOLVED → REOPENED → IN PROGRESS → RESOLVED → RETEST → CLOSED
```

## Lifecycle tracking template

| Bug | Open | In Progress | Resolved | Retest | Closed | Evidence |
|---|---|---|---|---|---|---|
| BUG-001 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-002 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-003 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-004 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-005 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-006 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-007 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-008 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-009 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-010 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-011 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-012 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-013 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-014 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-015 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-016 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-017 | ✓ | Pending | Pending | Pending | Pending | Pending |
| BUG-018 | ✓ | Pending | Pending | Pending | Pending | Pending |

> Jira issue keys and transition timestamps must be populated after actual Jira execution. This document does not fabricate Jira history.
