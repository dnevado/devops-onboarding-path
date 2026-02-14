#!/usr/bin/env bash
set -euo pipefail

# Mock deploy: copy built artifact to staging/ and show health check
mkdir -p staging
cp -r starters/week-3/app staging/ || true

echo "Deployed sample app to staging/"

echo "Run scripts/smoke_test.sh to validate deployment"
