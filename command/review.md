---
description: Review recent changes and suggest improvements
agent: code-reviewer
subtask: true
---

Recent git changes:
!`git diff HEAD~1 2>&1 || git diff --cached 2>&1 || echo "No changes to review"`

Review these changes for:

1. **Code Quality**: Readability, maintainability, naming
2. **Best Practices**: Language/framework conventions
3. **Potential Bugs**: Logic errors, edge cases, error handling
4. **Performance**: Obvious performance issues
5. **Security**: Common vulnerabilities

Provide constructive, specific feedback with examples.
