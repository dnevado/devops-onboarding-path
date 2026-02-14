
# Week 7 — Security Basics & Secrets Management

Overview

Security is a cross-cutting concern for all DevOps activity. This week covers fundamental practices around secrets management, least privilege, and pipeline hygiene.

Objectives
- Understand common risks: secret sprawl, credential rotation, and excessive permissions.
- Use secrets stores (GitHub Secrets, HashiCorp Vault, cloud secret managers) appropriately.
- Design pipelines with least-privilege tokens and short-lived credentials.

Core Concepts

1) Secret management patterns
- Avoid storing secrets in code or plaintext files. Use environment injection at runtime or CI time with encrypted stores.
- Prefer reference-based access (e.g., `vault://` URIs) and short-lived credentials where possible.

2) Principle of least privilege
- Grant the minimum required permissions to CI tokens and service accounts. Use role-based access control (RBAC) in cloud APIs.

3) CI pipeline hardening
- Mask secrets in logs, restrict `GITHUB_TOKEN` permissions per workflow, and require PR reviews for workflows that modify sensitive files.

Hands-on Exercise

1. Create `deliverables/week-7-<yourname>.md` describing a recommended approach to store a secret for CI and an example policy (e.g., IAM role or Vault policy) that limits access.
2. Optionally, show a sample workflow snippet demonstrating secure retrieval of a secret via `secrets.MY_SECRET` without echoing it.

Acceptance criteria
- `deliverables/week-7-<yourname>.md` exists in the PR branch.

Hints
- Never print secrets to workflow logs. Use `::add-mask::` or rely on `secrets` masking features.
- Use `permissions` block in workflows to reduce `GITHUB_TOKEN` scope.

Further reading
- GitHub Actions security hardening guide, HashiCorp Vault best practices, and cloud provider IAM recommendations.

