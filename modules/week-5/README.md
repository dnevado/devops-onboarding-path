# Week 5 — Infrastructure as Code (Terraform)

![CI](https://img.shields.io/badge/CI-ready-blue) ![Grader](https://img.shields.io/badge/Grader-ready-brightgreen)

![Terraform icon](../../assets/icons/terraform.svg)

- **Estimated:** 5–8 hours
- **Points:** 12
- **Difficulty:** Intermediate

## Overview

An introduction to Terraform, state, providers, and modules. Learners will author a minimal module and run `terraform plan`.

Objectives
- Write simple Terraform configurations and modules.
- Understand state, backend considerations, and safe workflows.
- Use `terraform fmt` and `terraform validate`.

Hands-on exercises

Tasks:
1. Add a folder `terraform/` with a minimal module and `main.tf` that declares a resource (can be a null resource or cloud resource).
2. Add `deliverables/week-5-<yourname>.md` documenting `terraform init`/`plan` output.

Acceptance criteria (automated):
- `terraform/main.tf` exists.
- `deliverables/week-5-<yourname>.md` exists.

Deliverables
- `terraform/main.tf`
- `deliverables/week-5-<yourname>.md`

