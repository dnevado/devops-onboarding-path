# 8-Week Onboarding Plan — Calendar View

![CI](https://img.shields.io/badge/CI-ready-blue) ![Grader](https://img.shields.io/badge/Grader-ready-brightgreen)

![Plan icon](assets/icons/ci.svg)

- **Cohort length:** 8 weeks
- **Format:** Hybrid — theory (Markdown) + hands-on labs (GitHub PRs)
- **Start date:** replaceable; see instructions below to set cohort dates

This calendar-style plan provides a glanceable, visual schedule for the 8-week DevOps onboarding. Use the icons and metadata to quickly find objectives and deliverables.

> Note: Replace the `Dates` column with your cohort start date. Example start: `2026-03-02`.

| Week | Dates (example) | Theme | Quick objectives | Deliverable |
|---:|:---:|:---|:---|:---|
| **Wk 1** | 2026-03-02 → 2026-03-08 | ![Git icon](assets/icons/git.svg) **Foundations: Git & GitHub** | Learn branching, commits, PR flow, and CI triggers. | `deliverables/week-1-<you>.md` (intro + PR)
| **Wk 2** | 2026-03-09 → 2026-03-15 | ![Shell icon](assets/icons/git.svg) **Linux & Networking** | Shell basics, permissions, processes, and basic networking tools. | `deliverables/week-2-<you>.sh`, `report/week-2-<you>.md`
| **Wk 3** | 2026-03-16 → 2026-03-22 | ![Docker icon](assets/icons/docker.svg) **Containers (Docker)** | Dockerfile best practices, multi-stage builds, local image lifecycle. | `app/Dockerfile`, `deliverables/week-3-<you>.md`
| **Wk 4** | 2026-03-23 → 2026-03-29 | ![CI icon](assets/icons/ci.svg) **CI/CD & Actions** | Create workflows, test/lint steps, and a reusable workflow. | `.github/workflows/sample-ci.yml`, `deliverables/week-4-<you>.md`
| **Wk 5** | 2026-03-30 → 2026-04-05 | ![Terraform icon](assets/icons/terraform.svg) **IaC (Terraform)** | Write modules, plan/apply workflow, state handling and formatting. | `terraform/main.tf`, `deliverables/week-5-<you>.md`
| **Wk 6** | 2026-04-06 → 2026-04-12 | ![Observability icon](assets/icons/observability.svg) **Observability & Logging** | Instrument apps, expose metrics/logs, and provide example queries. | `deliverables/week-6-<you>.md`, `observability/*`
| **Wk 7** | 2026-04-13 → 2026-04-19 | 🔒 **Security & Secrets** | Secrets management, pipeline least-privilege, and secure workflows. | `deliverables/week-7-<you>.md`
| **Wk 8** | 2026-04-20 → 2026-04-26 | 🚀 **Capstone: End-to-end** | Combine build, IaC, deploy, smoke-tests and observability into a pipeline. | `deliverables/week-8-<you>.md`

## How to read this calendar

- Icons: quick visual reference for the module theme. Icons live in `assets/icons/`.
- Dates: example windows; cohorts should replace with actual start dates.
- Deliverable: automated grader looks for the files listed in the module `exercise.json`.

## Weekly card details (expandable)

### Week X — Card format

**Header**: Week number, icon, estimated time, points, difficulty.

**Overview**: 2–4 sentence summary of the week's value and learning outcomes.

**Steps** (practical):
1. Read the extended theory in `modules/week-X/README.md`.
2. Clone your fork, create a branch `feature/week-X-<you>`.
3. Implement the deliverable and commit with clear messages.
4. Open PR to `main` with title containing `module:week-X` to trigger grading.

**Acceptance criteria**: Found in `modules/week-X/exercise.json` (expected files, points, pass threshold).

## Visual identity & usage tips

- Keep module headers consistent using the `STYLE_GUIDE.md` header template.
- Use badges for live status and add them to module README headers for instant feedback.
- Encourage learners to include a small emoji or icon in their `deliverables` file to increase engagement.

