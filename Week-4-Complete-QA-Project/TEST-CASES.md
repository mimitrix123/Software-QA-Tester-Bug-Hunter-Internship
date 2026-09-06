# 60 Manual Test Cases

| ID | Area | Test Scenario | Test Data / Setup | Expected Result |
|---|---|---|---|---|
| TC-001 | Authentication | Login with valid standard user | standard_user / secret_sauce | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-002 | Authentication | Login with invalid password | standard_user / wrong password | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-003 | Authentication | Login with locked-out user | locked_out_user / secret_sauce | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-004 | Authentication | Submit blank login form | blank username/password | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-005 | Authentication | Username only | username entered; password blank | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-006 | Authentication | Password only | password entered; username blank | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-007 | Authentication | Verify login error is visible | invalid credentials | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-008 | Authentication | Logout from menu | valid logged-in session | Correct authentication result is shown and user is either admitted or blocked as appropriate. |
| TC-009 | Inventory | Verify inventory page loads | valid login | Requested inventory behavior is correct and the UI remains consistent. |
| TC-010 | Inventory | Verify product cards are displayed | inventory page | Requested inventory behavior is correct and the UI remains consistent. |
| TC-011 | Inventory | Verify product names are visible | inventory page | Requested inventory behavior is correct and the UI remains consistent. |
| TC-012 | Inventory | Verify product prices are visible | inventory page | Requested inventory behavior is correct and the UI remains consistent. |
| TC-013 | Inventory | Verify product images load | inventory page | Requested inventory behavior is correct and the UI remains consistent. |
| TC-014 | Inventory | Verify Add to Cart buttons appear | inventory page | Requested inventory behavior is correct and the UI remains consistent. |
| TC-015 | Inventory | Sort products A-Z | Name A to Z | Requested inventory behavior is correct and the UI remains consistent. |
| TC-016 | Inventory | Sort products Z-A | Name Z to A | Requested inventory behavior is correct and the UI remains consistent. |
| TC-017 | Inventory | Sort products low-to-high | Price low to high | Requested inventory behavior is correct and the UI remains consistent. |
| TC-018 | Inventory | Sort products high-to-low | Price high to low | Requested inventory behavior is correct and the UI remains consistent. |
| TC-019 | Product | Open product details | click product name | Correct product information is displayed and navigation works. |
| TC-020 | Product | Verify detail title matches catalog | open any product | Correct product information is displayed and navigation works. |
| TC-021 | Product | Verify detail price matches catalog | open any product | Correct product information is displayed and navigation works. |
| TC-022 | Product | Verify detail image is displayed | open any product | Correct product information is displayed and navigation works. |
| TC-023 | Product | Verify detail description is displayed | open any product | Correct product information is displayed and navigation works. |
| TC-024 | Product | Return from detail to inventory | Back to products | Correct product information is displayed and navigation works. |
| TC-025 | Cart | Add one product | Backpack | Cart contents and badge state accurately reflect the requested action. |
| TC-026 | Cart | Add two products | Backpack + Bike Light | Cart contents and badge state accurately reflect the requested action. |
| TC-027 | Cart | Verify cart badge count | two products | Cart contents and badge state accurately reflect the requested action. |
| TC-028 | Cart | Open cart | cart icon | Cart contents and badge state accurately reflect the requested action. |
| TC-029 | Cart | Verify selected product appears in cart | one product | Cart contents and badge state accurately reflect the requested action. |
| TC-030 | Cart | Remove product from cart | selected product | Cart contents and badge state accurately reflect the requested action. |
| TC-031 | Cart | Verify cart badge updates after removal | remove last item | Cart contents and badge state accurately reflect the requested action. |
| TC-032 | Cart | Add product after removal | add same product again | Cart contents and badge state accurately reflect the requested action. |
| TC-033 | Cart | Verify multiple cart items remain | two products | Cart contents and badge state accurately reflect the requested action. |
| TC-034 | Checkout | Start checkout with cart item | one cart item | Correct validation or checkout progression occurs. |
| TC-035 | Checkout | Submit blank checkout information | blank form | Correct validation or checkout progression occurs. |
| TC-036 | Checkout | Submit missing first name | last name + postal only | Correct validation or checkout progression occurs. |
| TC-037 | Checkout | Submit missing last name | first name + postal only | Correct validation or checkout progression occurs. |
| TC-038 | Checkout | Submit missing postal code | first + last name only | Correct validation or checkout progression occurs. |
| TC-039 | Checkout | Continue with valid information | QA Tester / 700001 | Correct validation or checkout progression occurs. |
| TC-040 | Checkout | Verify checkout overview shows item | valid checkout | Correct validation or checkout progression occurs. |
| TC-041 | Checkout | Verify item price in overview | valid checkout | Correct validation or checkout progression occurs. |
| TC-042 | Checkout | Verify subtotal is displayed | valid checkout | Correct validation or checkout progression occurs. |
| TC-043 | Checkout | Verify tax is displayed | valid checkout | Correct validation or checkout progression occurs. |
| TC-044 | Checkout | Verify total is displayed | valid checkout | Correct validation or checkout progression occurs. |
| TC-045 | Checkout | Cancel checkout from information page | click Cancel | Correct validation or checkout progression occurs. |
| TC-046 | Checkout | Cancel checkout from overview | click Cancel | Correct validation or checkout progression occurs. |
| TC-047 | Order | Finish a valid order | one product + valid details | Order flow produces the expected confirmation or navigation. |
| TC-048 | Order | Verify order confirmation heading | completed order | Order flow produces the expected confirmation or navigation. |
| TC-049 | Order | Verify confirmation page is displayed | completed order | Order flow produces the expected confirmation or navigation. |
| TC-050 | Order | Return home after order | Back Home | Order flow produces the expected confirmation or navigation. |
| TC-051 | Navigation | Open side menu | logged-in user | Requested navigation action opens the correct destination/state. |
| TC-052 | Navigation | Verify All Items returns to inventory | side menu | Requested navigation action opens the correct destination/state. |
| TC-053 | Navigation | Verify About link opens expected destination | side menu | Requested navigation action opens the correct destination/state. |
| TC-054 | Navigation | Verify Reset App State clears cart | item in cart | Requested navigation action opens the correct destination/state. |
| TC-055 | Session | Refresh inventory after login | logged-in user | Session state is handled correctly without unauthorized access. |
| TC-056 | Session | Use browser Back after checkout cancel | cancel checkout | Session state is handled correctly without unauthorized access. |
| TC-057 | Session | Logout and verify login page | logged-in user | Session state is handled correctly without unauthorized access. |
| TC-058 | Session | Attempt browser Back after logout | logged-out session | Session state is handled correctly without unauthorized access. |
| TC-059 | Usability | Verify login labels are understandable | login page | UI is readable, usable, and consistent at the tested condition. |
| TC-060 | Usability | Verify validation errors are readable | trigger validation | UI is readable, usable, and consistent at the tested condition. |
