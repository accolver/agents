---
description: Set up development environment
agent: infrastructure
---

Current project files:
!`ls -la 2>&1`

Existing package.json:
!`cat package.json 2>&1 || echo "No package.json found"`

Set up a complete development environment:

1. **Package Manager**: Ensure package.json exists
2. **TypeScript**: Add TypeScript configuration if not present
3. **Linting**: Set up ESLint with appropriate rules
4. **Formatting**: Configure Prettier
5. **Testing**: Set up testing framework (Vitest)
6. **Git Hooks**: Add Husky for pre-commit hooks
7. **Scripts**: Add useful npm scripts (dev, build, test, lint)
8. **Editor Config**: Add .editorconfig for consistency
9. **Dependencies**: Install necessary dev dependencies

Ask about:

- Framework/library being used (React, Vue, etc.)
- Javascript run time (Node, Bun, Deno)
- Testing preferences (default to Vitetest)
- Any specific tools or requirements
- Preferred UI component library (default to ShadCN)
- Monorepo desired? If so, use TurboRepo

Create all necessary config files and update package.json.

Use context7 to look up documentation if available
