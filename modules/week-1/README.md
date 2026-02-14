# Week 1 — Foundations: Git & GitHub

Overview

This week establishes the source-control foundation used across the onboarding path. Learners gain practical fluency with Git, GitHub collaboration patterns (fork/branch/PR), and the Git-based triggers that run automated checks.

Objectives
- Explain commits, branches, remotes, and common workflows (feature branch, pull request).
- Perform local Git operations and push to a fork.
- Open a GitHub Pull Request that triggers CI and interpret workflow results.

In-depth Theory

1) Git Internals (short primer)
- Commits are snapshots identified by SHA; each commit stores metadata and pointers to trees/parents.
- The working tree, index (staging area), and local repository are distinct states you learn to move changes through.

2) Branching Models
- Feature-branch workflow: short-lived branches per task, merged via PR.
- Trunk-based development vs long-lived branches: tradeoffs.

3) Merging, Rebasing, and Conflicts
- Merge creates a merge commit keeping history explicit; rebase rewrites commits to produce linear history.
- When conflicts occur, use `git status` and an editor to resolve, then `git add` and `git rebase --continue` or `git merge --continue`.

4) GitHub Collaboration
- Fork -> clone -> create branch -> push to fork -> open PR to upstream `main`.
- PRs provide a place for code review, CI results, and automated grading in this path.

Essential Commands (examples)
```
git clone git@github.com:<you>/onboarding.git
git checkout -b feature/week-1-yourname
echo "# Intro" > deliverables/week-1-yourname.md
git add deliverables/week-1-yourname.md
git commit -m "chore: add week-1 deliverable"
git push origin feature/week-1-yourname
```

Hands-on Exercises

Tasks (concrete)
1. Fork this repository to your GitHub account.
2. Create a branch named `feature/week-1-<yourname>`.
3. Add `deliverables/week-1-<yourname>.md` with: name, one-sentence career goal, and 3 bullet points of what you learned this week.
4. Open a PR to `main` with title containing `module:week-1`.

Acceptance criteria (automated)
- `deliverables/week-1-<yourname>.md` exists in PR branch.
- PR title or body includes `module:week-1` so grader can detect the module.

Hints & common issues
- Ensure the file path matches exactly: `deliverables/week-1-<yourname>.md`.
- If the grader reports missing file, confirm your branch had the file committed and pushed.

Further reading
- Pro Git (free book): https://git-scm.com/book/en/v2
- GitHub Docs: Forking workflows, Pull Requests, and Actions docs.

Suggested next practice
- Create a pair PR with a teammate that intentionally creates a merge conflict; practice resolving it locally.

