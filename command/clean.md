---
description: Clean up code and remove technical debt
agent: refactoring
---

Find areas needing cleanup:
!`find . -name "*.ts" -o -name "*.js" -o -name "*.tsx" -o -name "*.jsx" | grep -v node_modules | head -50 2>&1`

Code cleanup tasks:

1. **Remove Dead Code**: Unused imports, variables, functions
2. **Console Logs**: Remove debugging console.log statements
3. **Comments**: Remove commented-out code
4. **TODO/FIXME**: Address or document TODOs
5. **Formatting**: Ensure consistent formatting
6. **Dependencies**: Remove unused dependencies
7. **Type Safety**: Add missing types or improve existing ones
8. **Documentation**: Update outdated comments

Search for common issues:
!`grep -r "console.log\|TODO\|FIXME\|XXX\|HACK" --include="*.ts" --include="*.js" --exclude-dir=node_modules . 2>&1 | head -20`

For each issue:

1. Explain what needs cleaning
2. Provide the cleaned version
3. Ensure nothing breaks

Run tests after cleanup:
!`npm test 2>&1 | head -20`
