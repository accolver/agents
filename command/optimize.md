---
description: Optimize performance, bundle size, algorithms, and caching
agent: polish
---

Check bundle size and build output:
!`npm run build 2>&1 | grep -i "size\|kb\|mb\|chunk" || echo "Build to check bundle size"`

Check for large dependencies:
!`npx webpack-bundle-analyzer dist/stats.json 2>&1 || echo "Bundle analyzer not configured"`

Find potentially slow code patterns:
!`grep -r "map\|filter\|forEach\|reduce" --include="*.ts" --include="*.tsx" --include="*.js" --include="*.jsx" --exclude-dir=node_modules . 2>&1 | head -20 || echo "No JavaScript files found"`

Performance optimization tasks:

**Frontend Performance:**

1. **Bundle Optimization**:
   - Identify large dependencies
   - Remove unused dependencies
   - Use lighter alternatives
   - Implement code splitting and lazy loading
   - Ensure tree shaking works properly

2. **Asset Optimization**:
   - Optimize images (WebP, compression, lazy loading)
   - Minify CSS and JavaScript
   - Use CDN for static assets
   - Implement proper caching headers
   - Compress with gzip/brotli

3. **React/Vue Optimizations**:
   - Memoization (useMemo, React.memo, computed)
   - Virtualize long lists
   - Debounce/throttle frequent updates
   - Avoid inline function definitions
   - Use proper key props

4. **Caching Strategies**:
   - Browser caching (Cache-Control headers)
   - Service workers for offline caching
   - localStorage/sessionStorage for data
   - HTTP caching (ETags, Last-Modified)
   - Memoize API responses

**Backend Performance:**
5. **Database Optimization**:

- Fix N+1 query problems
- Add missing indexes
- Optimize slow queries
- Use query explain/analyze
- Implement connection pooling
- Add database-level caching (Redis)

6. **Algorithm Optimization**:
   - Replace O(n²) with O(n log n) or O(n) algorithms
   - Use proper data structures (Map/Set vs Array)
   - Avoid nested loops when possible
   - Implement binary search instead of linear
   - Use memoization for recursive functions
   - Cache expensive computations

7. **Caching Layers**:
   - In-memory caching (Redis, Memcached)
   - Application-level caching
   - Query result caching
   - API response caching
   - CDN caching for static content
   - Cache invalidation strategies

8. **API Optimization**:
   - Reduce payload size (only send needed fields)
   - Implement pagination
   - Use HTTP/2 or HTTP/3
   - Compress responses
   - Batch API requests
   - Use GraphQL field selection

9. **Code Efficiency**:
   - Remove console.logs in production
   - Eliminate redundant calculations
   - Optimize loops and iterations
   - Use async/await properly
   - Implement worker threads for CPU-intensive tasks

10. **Monitoring & Profiling**:
    - Identify bottlenecks with profiling
    - Monitor Core Web Vitals (LCP, FID, CLS)
    - Track API response times
    - Monitor memory usage
    - Set up performance budgets

For each optimization:

- **Current State**: Measure before optimization
- **Impact Analysis**: Expected improvement (time/size)
- **Implementation**: Specific code changes
- **Validation**: Measure after optimization
- **Trade-offs**: Any downsides or complexity added

Prioritize optimizations by:

1. **High Impact, Low Effort**: Do these first
2. **High Impact, High Effort**: Plan and execute
3. **Low Impact, Low Effort**: Nice to have
4. **Low Impact, High Effort**: Skip unless necessary

Implement optimizations that provide the most value with measurable improvements.
