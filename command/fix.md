---
description: Fix linting, type errors, and build issues
agent: general
---

Check for linting errors: !`npm run lint 2>&1 || echo "Lint script not found"`

Check for type errors:
!`npm run typecheck 2>&1 || npx tsc --noEmit 2>&1 || echo "TypeScript not configured"`

Build the project:
!`npm run build 2>&1 || yarn build 2>&1 || echo "Build script not found in package.json"`

Analyze all errors and fix them systematically:

1. **Identify Errors**: List all linting, type, and build errors
2. **Categorize**: Group by type (linting, TypeScript, bundler, dependencies)
3. **Explain**: Clarify what each error means
4. **Fix**: Address each error systematically
5. **Verify**: Run checks again after fixes
6. **Iterate**: Continue until all checks pass

If the build succeeds:

1. Report successful build
2. Check bundle size if available
3. Suggest optimizations if bundle is large

If errors persist:

1. Explain why they can't be auto-fixed
2. Provide manual steps needed
3. Suggest alternative approaches

Don't stop until linting, type checking, and build are all successful.
