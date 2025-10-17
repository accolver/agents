---
description: Run tests with coverage and suggest fixes
agent: testing
---

Run the full test suite with coverage report:
!`npm test -- --coverage 2>&1 || echo "Test command not found. Please check package.json scripts."`

Analyze the test results and:

1. Show which tests passed/failed
2. Report current coverage percentages
3. Identify areas with low coverage
4. Suggest specific tests to add for better coverage
5. If tests failed, provide clear explanations and fixes

Focus on actionable improvements.
