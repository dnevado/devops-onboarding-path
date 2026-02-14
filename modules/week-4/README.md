 # Week 4 — CI/CD & GitHub Actions

Overview

This week teaches how to automate build, test, and delivery workflows using GitHub Actions. Learners will author workflows, use reusable calls, understand secrets, and learn common debugging techniques.

Objectives
- Understand triggers (`push`, `pull_request`, `workflow_dispatch`) and job orchestration.
- Write and call reusable workflows and share actions between repos.
- Use the Actions toolkit for logging, artifacts, and secrets safely.

Core Concepts

1) Workflow anatomy
- `on:` (triggers), `jobs:` (parallelizable units), `steps:` (scripted actions). Jobs can use `needs:` to define dependencies.

2) Reusable workflows & composition
- Use `workflow_call` for sharing common grading or linting flows across many repos in an organization.

3) Secrets & credentials
- Store tokens in `Secrets` and avoid printing them in logs. Use `permissions` to limit token scope.

Debugging tips
- Use `ACTIONS_STEP_DEBUG` and workflow logs; add `echo` steps and upload artifacts to inspect outputs.

Practical Example (snippet)
```yaml
name: CI
on: [push, pull_request]
jobs:
	test:
		runs-on: ubuntu-latest
		steps:
			- uses: actions/checkout@v4
			- uses: actions/setup-python@v4
				with: { python-version: '3.11' }
			- name: Install
				run: pip install -r requirements.txt
			- name: Run tests
				run: pytest -q
```

Hands-on Exercise

1. In your fork, add a minimal CI workflow `.github/workflows/sample-ci.yml` that installs dependencies and runs a basic test or lint.
2. Document the workflow and how to trigger it in `deliverables/week-4-<yourname>.md`.

Acceptance criteria
- `deliverables/week-4-<yourname>.md` exists.

Advanced (optional)
- Create a reusable workflow in `.github/workflows/reusable` that can be called by other repos with `uses: ./.github/workflows/reusable/grade-reusable.yml`.

Further reading
- GitHub Actions docs: workflows, contexts and expressions, and best practices on secrets.

