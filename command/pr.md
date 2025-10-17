---
description: Prepare for pull request review
agent: quality
subtask: true
---

Current branch:
!`git branch --show-current 2>&1`

Changes in this branch:
!`git diff main...HEAD 2>&1 || git diff master...HEAD 2>&1 || echo "Compare with your main branch"`

Commits in this branch:
!`git log main..HEAD --oneline 2>&1 || git log master..HEAD --oneline 2>&1`

Pre-PR checklist:

1. **Changes Summary**: What does this PR do?
2. **Code Quality**: Review for issues
3. **Tests**: Are there tests? Do they pass?
4. **Documentation**: Is documentation updated?
5. **Breaking Changes**: Any breaking changes?
6. **Security**: Any security implications?
7. **Performance**: Any performance impact?
8. Confidentiality: Any secrets committed?

Generate a PR description including:

- Clear title
- Summary of changes
- Why these changes are needed
- Testing done
- Screenshots (if UI changes)
- Breaking changes (if any)
- Related issues

Run final checks:
!`npm run lint 2>&1 && npm test 2>&1 || echo "Run lint and tests before PR"`
