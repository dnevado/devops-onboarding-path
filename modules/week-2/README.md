# Week 2 — Linux & Networking Basics

![CI](https://img.shields.io/badge/CI-ready-blue) ![Grader](https://img.shields.io/badge/Grader-ready-brightgreen)

![Shell icon](../../assets/icons/git.svg)

- **Estimated:** 3–5 hours
- **Points:** 10
- **Difficulty:** Beginner

## Overview

This week teaches the shell and network fundamentals every DevOps engineer needs. The materials include practical command examples, diagnostic patterns, and a hands-on script exercise you can run locally.

Objectives
- Use the shell to inspect and modify the filesystem and permissions.
- Understand process management and basic logging.
- Use networking tools to diagnose connectivity and DNS issues.

Core Concepts

1) Filesystem & Permissions
- Linux filesystem layout (`/etc`, `/var`, `/usr`, `/home`) and when to store configuration vs runtime data.
- File permissions: read/write/execute for user/group/others; use `chmod`, `chown`, and `umask`.

2) Processes & Services
- `ps`, `top`/`htop`, `systemctl` for service lifecycle, and `journalctl` for centralized logs.

3) Networking Basics
- IP addressing, subnetting at a high level; DNS resolution flow (resolver -> recursive -> authoritative).
- Tools: `ping` (latency/liveliness), `traceroute` (path), `ss`/`netstat` (listening ports), `curl`/`wget` (HTTP checks), `dig` (DNS queries).

Example Commands
```
# list permissions and ownership
ls -la /etc

# create dir, file, change perms
mkdir -p testdir && echo hello > testdir/hello.txt && chmod 640 testdir/hello.txt

# check listening sockets
ss -tulpn

# DNS and HTTP checks
dig example.com
curl -I https://example.com
```

Hands-on Exercise (concrete)

1. Create `deliverables/week-2-<yourname>.sh` with the following steps:
   - create a directory `testdir` and a file `testdir/notes.txt` containing your name and timestamp.
   - set file permissions to `0640` and demonstrate reading the file as the owner.
   - run `curl -I https://example.com` and save headers to `deliverables/week-2-<yourname>-headers.txt`.

2. Create `report/week-2-<yourname>.md` (1–2 paragraphs) describing a basic network issue you reproduced or a hypothetical incident and the commands you used to diagnose it.

Acceptance criteria (automated)
- `deliverables/week-2-<yourname>.sh` exists and is executable in the PR branch.
- `report/week-2-<yourname>.md` exists.

Hints & Verification
- Make your shell script portable (use `#!/usr/bin/env bash`).
- Use `set -euo pipefail` for safer scripting; comment the script so graders and reviewers can follow your steps.

Further reading
- TLDR pages (tldr.sh) for concise command examples.
- "The Linux Command Line" book for an in-depth intro.

