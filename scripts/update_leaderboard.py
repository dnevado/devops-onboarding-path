#!/usr/bin/env python3
"""Update the leaderboard JSON with new points.

This script updates `gamification/leaderboard.json` locally. To persist changes to the central repo,
provide a PAT via `GITHUB_TOKEN` or `PUSH_TOKEN` and configure the workflow to commit and push.

Usage: python scripts/update_leaderboard.py --user alice --points 10
"""
import argparse
import json
from pathlib import Path

LB = Path(__file__).resolve().parents[1] / 'gamification' / 'leaderboard.json'


def load():
    if not LB.exists():
        return {}
    return json.loads(LB.read_text())


def save(d):
    LB.write_text(json.dumps(d, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True)
    parser.add_argument('--points', type=int, required=True)
    args = parser.parse_args()

    data = load()
    data.setdefault(args.user, 0)
    data[args.user] += args.points
    save(data)
    print(f"Updated {args.user} -> {data[args.user]} points")


if __name__ == '__main__':
    main()
