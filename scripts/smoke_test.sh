#!/usr/bin/env bash
set -euo pipefail

# Simple smoke test that expects the sample app to respond on localhost:8080
if curl --fail --silent --show-error http://localhost:8080/ >/dev/null; then
  echo "smoke-test: OK"
  exit 0
else
  echo "smoke-test: FAIL"
  exit 2
fi
