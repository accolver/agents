---
description: Set up or troubleshoot deployment
agent: devops
---

CI/CD configuration:
!`ls -la .github/workflows/ 2>&1 || ls -la .gitlab-ci.yml 2>&1 || ls -la .circleci/ 2>&1 || echo "No CI/CD config found"`

Infrastructure as Code files:
!`find . -maxdepth 3 -name "*.tf" -o -name "*.hcl" -o -name "terragrunt.hcl" -o -name "terraform.tfvars" 2>&1 | grep -v ".terraform" | head -20 || echo "No Terraform/Terragrunt files found"`

Container configuration:
!`ls -la Dockerfile* docker-compose*.yml .dockerignore 2>&1 || echo "No Docker files found"`

Kubernetes/Helm configs:
!`find . -maxdepth 3 -name "*.yaml" -o -name "*.yml" | grep -E "k8s|kubernetes|helm|Chart" 2>&1 | head -20 || echo "No Kubernetes configs found"`

Cloud platform configs:
!`ls -la vercel.json netlify.toml fly.toml railway.json render.yaml app.yaml cloudbuild.yaml 2>&1 || echo "No cloud platform configs found"`

Package.json scripts:
!`cat package.json 2>&1 | grep -A 10 '"scripts"' || echo "No package.json found"`

Makefile commands:
!`cat Makefile 2>&1 | grep -E "^[a-zA-Z_-]+:" | head -20 || echo "No Makefile found"`

Environment files:
!`ls -la .env* 2>&1 | grep -v ".git" || echo "No .env files found"`

Deployment setup/troubleshooting:

If setting up deployment:

1. **Platform**: Choose deployment platform (Vercel, Netlify, AWS, GCP, Azure, Fly.io, Railway, Render)
2. **Infrastructure**: Terraform/Terragrunt for IaC, or cloud platform configs
3. **Containerization**: Docker and docker-compose if needed
4. **Orchestration**: Kubernetes/Helm for container orchestration
5. **Build Configuration**: Proper build command and output directory
6. **Environment Variables**: Required env vars and secrets management
7. **CI/CD Pipeline**: GitHub Actions, GitLab CI, CircleCI, or similar
8. **Domain**: DNS and SSL/TLS configuration
9. **Monitoring**: Error tracking, logging, and observability
10. **Scaling**: Auto-scaling and load balancing setup

If troubleshooting:

1. **Error Analysis**: What's failing in the deployment pipeline?
2. **Logs**: Check deployment logs and container logs
3. **Configuration**: Verify build settings, environment vars, and secrets
4. **Dependencies**: Check for missing dependencies or incompatible versions
5. **Environment**: Verify environment variables and configuration
6. **Infrastructure**: Check IaC configurations (Terraform state, resources)
7. **Containers**: Verify Docker builds and image sizes
8. **Networking**: Check DNS, SSL certificates, and firewall rules
9. **Resources**: Verify compute, memory, and storage limits

Provide:

- Step-by-step deployment instructions
- CI/CD pipeline configuration
- Infrastructure as Code files (Terraform/Terragrunt)
- Container configurations (Dockerfile, docker-compose)
- Kubernetes manifests if applicable
- Environment variable list with descriptions
- Troubleshooting steps and common issues
- Rollback procedures
