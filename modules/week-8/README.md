# Week 8 — End-to-end Integration Exercise

Overview

Combine previous weeks into an integrated pipeline: build a container, deploy to a staging target (can be mocked), and demonstrate observability basics.

Objectives

Hands-on exercises

Tasks:

Acceptance criteria (automated):

Deliverables

This capstone week asks you to combine prior topics into a small, integrated pipeline: build a container, provision (or mock) infrastructure, deploy to a staging target, and demonstrate basic observability and rollback considerations.

Objectives

- Orchestrate build, IaC, and deployment steps in a reproducible workflow.
- Demonstrate deployment verification and simple rollbacks.
- Show how observability and security are integrated into the pipeline.

Suggested Architecture

- Source (feature branch) -> Actions pipeline -> Build container -> Push to registry (or local artifact) -> IaC `plan` -> Deploy to staging -> Run smoke tests -> Promote or rollback.

Hands-on Exercise (concrete)

1. Provide a feature branch that contains:
	- a `Dockerfile` and build step (or instructions to build locally),
	- a `terraform/` configuration (can use `null_resource` or local-exec) demonstrating `terraform plan`,
	- a simple `deploy.sh` or Action that performs a deploy-to-staging (even if mocked by moving files),
	- `deliverables/week-8-<yourname>.md` documenting end-to-end commands and verification steps.

2. Include a smoke-test script that validates the service is up (e.g., `curl` to an endpoint) and exits non-zero on failure.

Acceptance criteria

- `deliverables/week-8-<yourname>.md` exists and documents how to run the pipeline or how the CI run demonstrates the end-to-end flow.

Verification & robustness

- In your writeup, explain how you would implement rollback on failure (e.g., redeploy previous container tag or `terraform apply` to restore previous state).
- Describe what observability checks you would automate (health checks, metrics thresholds, alerting rules).

Further reading

- Continuous delivery patterns, deployment strategies (blue/green, canary), and infrastructure testing.

