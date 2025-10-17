---
description: Design database schema or query
agent: database-design
---

Database design for: $ARGUMENTS

Current database files:
!`find . -name "*.sql" -o -name "*schema*" -o -name "*migration*" | grep -v node_modules | head -20 2>&1`

Database design process:

1. **Requirements**: What data needs to be stored?
2. **Entities**: Main entities and their attributes
3. **Relationships**: One-to-many, many-to-many
4. **Schema Design**: Tables with columns and types
5. **Indexes**: For query performance
6. **Constraints**: Foreign keys, unique constraints, cascades
7. **Migrations**: Safe migration strategy

Provide:

```sql
-- Table definitions
CREATE TABLE users (
  id UUID PRIMARY KEY,
  ...
);

-- Indexes
CREATE INDEX idx_name ON table(column);

-- Common queries
SELECT ... FROM ... WHERE ...;
```

Consider:

- Normalization vs denormalization
- Query patterns and indexes
- Data integrity constraints
- Migration safety
- Performance implications
