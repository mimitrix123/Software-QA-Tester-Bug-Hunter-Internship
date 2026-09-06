# Test Plan — E-Commerce E2E

## 1. Test objective
Validate the critical customer journey of a demo e-commerce site from login through successful checkout and logout, while also exercising negative paths, cart calculations, input validation and navigation.

## 2. Scope
### In scope
- Login/logout
- Product catalog
- Sorting
- Product details
- Cart add/remove/update
- Checkout information
- Checkout overview and totals
- Order completion
- Session/navigation
- Negative validation cases

### Out of scope
- Performance/load testing
- API/database testing
- Payment gateway certification
- Penetration testing
- Native mobile application testing

## 3. Strategy
- Smoke testing first
- Happy-path E2E
- Negative testing
- Boundary/input validation
- Exploratory testing around cart and checkout
- Regression of failed/high-priority areas

## 4. Environment
| Item | Value |
|---|---|
| Application | SauceDemo / Swag Labs demo |
| Browser | Chrome/Edge latest stable |
| OS | Windows 10/11 |
| Viewport | 1280×720+ |
| Test type | Manual functional E2E |

## 5. Entry criteria
- Demo site accessible.
- Test accounts available.
- Browser ready.
- Test cases reviewed.

## 6. Exit criteria
- All planned E2E scenarios executed.
- Critical/high defects documented.
- Regression performed for fixed defects.
- Test summary completed.

## 7. Severity vs Priority
**Severity:** business/technical impact of the defect.

**Priority:** urgency with which the team should fix it.

Examples: checkout failure = High/Critical severity and High priority; cosmetic alignment = Low/Low.

## 8. Defect lifecycle
`Open → In Progress → Resolved → Retest → Closed`

If retest fails: `Resolved → Reopened → In Progress`.
