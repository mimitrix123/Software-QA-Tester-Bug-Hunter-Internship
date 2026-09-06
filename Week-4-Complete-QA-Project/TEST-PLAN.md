# Test Plan

## 1. Objective
Validate core functional, usability, compatibility, security-oriented session behavior, API behavior, and performance characteristics of the SauceDemo e-commerce workflow.

## 2. Scope
**In scope:** authentication, inventory, product details, sorting, cart, checkout, order completion, logout, API CRUD scenarios, and controlled load testing.

**Out of scope:** payment gateway integration, production infrastructure, real customer data, and third-party systems not exposed by the demo.

## 3. Test types
- Functional/manual testing
- Regression testing
- UI automation with Selenium
- API testing with Postman
- Performance/load testing with Apache JMeter
- Basic negative and boundary testing

## 4. Environment
- Web: SauceDemo
- Browser: Chrome/Chromium for automation
- Automation: Python + Selenium + pytest
- API client: Postman
- Performance: Apache JMeter
- OS: Windows/Linux/macOS supported by the tools

## 5. Entry criteria
Application is reachable; test accounts are available; test data is known; required tools are installed.

## 6. Exit criteria
All planned cases are executed, critical failures are triaged, automation is reviewed, API collection runs successfully, and load-test evidence is archived.

## 7. Risks
Demo-site changes can break locators; shared demo infrastructure can create variable response times; public services must not be load-tested without permission.

## 8. Deliverables
Test plan, strategy, 60 test cases, Selenium suite, Postman collection, JMeter plan, execution report, and QA portfolio.
