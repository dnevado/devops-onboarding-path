# DevOps Onboarding: 8-Week Hybrid Learning Path

![CI](https://img.shields.io/badge/CI-ready-blue) ![Grader](https://img.shields.io/badge/Grader-ready-brightgreen)

This repository contains a complete 8-week DevOps onboarding learning path designed for junior engineers with no prior DevOps experience. The program is hybrid: rich theory in Markdown plus hands-on exercises validated by GitHub Actions.

![Onboarding icon](assets/icons/ci.svg)

Structure overview
- `modules/week-1` … `modules/week-8`: each week contains `README.md` (theory + exercises) and `exercise.json` (expected deliverables).
- `.github/workflows/grade.yml`: repo-level workflow that grades PRs.
- `.github/workflows/reusable/grade-reusable.yml`: reusable workflow suitable for organization-level reuse.
- `scripts/grader.py`: simple grader used by workflows to validate deliverables.
- `scripts/update_leaderboard.py`: updates `gamification/leaderboard.json` with points (requires PAT with repo write permissions).
- `gamification/leaderboard.json`: persistent points store for the cohort (optional manual commit or push via PAT).

How it works (short)
1. Fork this repository in your org or user account.
2. Complete a weekly exercise in a feature branch named like `feature/week-1-<yourname>`.
3. Open a Pull Request to `main` with title containing `module:week-1` (or include module in PR body). PR triggers `grade.yml`.
4. The workflow runs `scripts/grader.py` to validate deliverables declared in the module `exercise.json`.
5. The workflow posts pass/fail, and on pass optionally records points to the leaderboard (if configured).

Customization
- Update `modules/*/exercise.json` to change deliverables and points.
- Update workflows to enforce additional policies (e.g., terraform fmt, linter checks).

See `WEEKLY_PLAN.md` for a high-level schedule and module objectives. For visual standards, see `STYLE_GUIDE.md`.
