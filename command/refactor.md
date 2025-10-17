---
description: Refactor code for better maintainability
agent: refactoring
---

Refactor the code in $ARGUMENTS

Analysis checklist:

1. **Code Smells**: Long functions, duplicated code, complex conditionals
2. **Naming**: Unclear variable/function names
3. **Structure**: Opportunities to extract functions or components
4. **Patterns**: Better design patterns to apply
5. **Complexity**: Simplify complex logic
6. **DRY**: Remove duplication

For each refactoring:

1. Explain what's being improved and why
2. Show before and after code
3. Ensure behavior stays the same
4. Run tests after refactoring to verify

Focus on improving readability and maintainability without changing functionality.

If no file specified, analyze recently modified files:
!`git diff --name-only HEAD~1 2>&1 || echo "Please specify a file to refactor"`
