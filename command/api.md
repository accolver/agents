---
description: Design or implement an API endpoint
agent: api-design
---

Design/implement API for: $ARGUMENTS

API Design checklist:

1. **Endpoint Design**: RESTful naming and HTTP methods
2. **Request Schema**: Parameters, body, headers
3. **Response Schema**: Success and error responses
4. **Status Codes**: Appropriate HTTP status codes
5. **Validation**: Input validation rules
6. **Authentication**: Auth requirements
7. **Error Handling**: Error message format
8. **Documentation**: API documentation format

Provide:

```typescript
// Type definitions
interface Request {}
interface Response {}

// Endpoint implementation
// GET/POST/PUT/DELETE /api/path
```

Include:

- OpenAPI/Swagger documentation
- Example requests and responses
- Error scenarios
- Rate limiting considerations

If implementing, check existing API patterns:
!`find . -name "*.ts" -o -name "*.js" | grep -i "api\|route\|controller" | head -10 2>&1`
