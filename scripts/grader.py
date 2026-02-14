#!/usr/bin/env python3
"""Basic grader for module exercises.

Usage: python scripts/grader.py --module week-1

Behavior:
- Reads modules/<module>/exercise.json to get expected files and points.
- Verifies files exist in the workspace root (checked-out PR branch).
- Exits 0 when pass threshold met, non-zero otherwise.
- Prints JSON summary to stdout for workflows to parse.
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_exercise(module):
    p = ROOT / 'modules' / module / 'exercise.json'
    if not p.exists():
        print(json.dumps({"error": f"exercise.json not found for {module}"}))
        sys.exit(2)
    return json.loads(p.read_text())


def check_files(expect_files):
    results = []
    for f in expect_files:
        exists = (ROOT / f).exists()
        results.append({"file": f, "exists": exists})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', required=True)
    args = parser.parse_args()

    exercise = load_exercise(args.module)
    expected = exercise.get('expected_files', [])
    points = exercise.get('points', 10)
    pass_threshold = exercise.get('pass_threshold', 0.7)

    checks = check_files(expected)
    found = sum(1 for c in checks if c['exists'])
    total = len(checks) if checks else 0
    score = (found / total) if total else 0
    earned_points = int(round(score * points))
    passed = score >= pass_threshold

    result = {
        "module": args.module,
        "found": found,
        "total": total,
        "score": score,
        "earned_points": earned_points,
        "passed": passed,
        "details": checks,
    }
    print(json.dumps(result))
    if passed:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
