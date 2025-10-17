---
description: Security audit of dependencies and code
agent: security-audit
subtask: true
---

Check for vulnerable dependencies:
!`npm audit 2>&1 || yarn audit 2>&1 || echo "No package manager found"`

Security audit checklist:

1. **Dependency Vulnerabilities**: Review npm audit output
2. **Outdated Packages**: Check for critical security updates
3. **Code Patterns**: Scan for common vulnerabilities (SQL injection, XSS, hardcoded secrets)
4. **Authentication**: Review auth implementation if present
5. **Input Validation**: Check for missing validation
6. **Sensitive Data**: Ensure no secrets in code

For each issue found:

- Severity level (critical, high, medium, low)
- Specific location
- Clear remediation steps
- Example of the fix

Prioritize critical and high severity issues.
