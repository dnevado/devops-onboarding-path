# 8-Week Onboarding Plan (Overview)

This document summarizes weekly objectives and outcomes. Each week includes theory, hands-on exercises and deliverables validated by CI.

Week 1 — Foundations: Git, GitHub, branching, PRs, workflow basics
- Objectives: Understand Git basics, create branches, open PRs, and pass a PR-based grading workflow.
- Deliverables: Create a documented repo README update and a simple CI-configured PR.

Week 2 — Linux & Networking Basics
- Objectives: Learn shell basics, file permissions, networking fundamentals (TCP/UDP), and remote access patterns.
- Deliverables: Shell script that demonstrates manipulating files and a short network troubleshooting log.

Week 3 — Containerization with Docker
- Objectives: Build, tag, and run containers; write Dockerfiles; push images to a registry.
- Deliverables: Dockerfile + README explaining multi-stage build and a run script.

Week 4 — CI/CD & GitHub Actions
- Objectives: Create Actions workflows, triggers, and reusable steps; test, lint and deploy artifacts to a staging area.
- Deliverables: A GitHub Action workflow and proof of workflow execution (sample artifact or logs).

Week 5 — Infrastructure as Code (IaC) with Terraform
- Objectives: Introduction to Terraform, state, modules, and plan/apply workflow.
- Deliverables: Minimal Terraform module that provisions a resource (mock or cloud) and a `terraform plan` output.

Week 6 — Observability & Logging
- Objectives: Instrument apps for logs and metrics, set up basic dashboards and alerts.
- Deliverables: Sample app instrumentation and dashboard JSON or screenshots.

Week 7 — Security Basics & Secrets Management
- Objectives: Secure SCM, manage secrets in CI, basic threat model for pipelines.
- Deliverables: A pipeline that reads secrets securely and a short report demonstrating risk mitigation.

Week 8 — Putting It Together: End-to-end exercise
- Objectives: Build a small end-to-end pipeline combining container build, IaC, and deployment staging.
- Deliverables: An integrated MVP in a feature branch with documentation and CI passing.

Each week has an assigned point value and passing threshold found in each module's `exercise.json`.
