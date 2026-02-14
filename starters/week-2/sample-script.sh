#!/usr/bin/env bash
set -euo pipefail

OUTDIR=deliverables
mkdir -p "$OUTDIR"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
NAME="yourname"

echo "Name: $NAME" > "$OUTDIR/week-2-$NAME.txt"
echo "Timestamp: $TS" >> "$OUTDIR/week-2-$NAME.txt"

# create testdir and file
mkdir -p testdir
echo "hello from $NAME at $TS" > testdir/notes.txt
chmod 640 testdir/notes.txt

# capture headers from example.com
curl -I https://example.com -sS -D - -o /dev/null > "$OUTDIR/week-2-$NAME-headers.txt"

echo "Created deliverables in $OUTDIR and testdir/notes.txt"
