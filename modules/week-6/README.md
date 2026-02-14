
# Week 6 — Observability & Logging

Overview

Observability helps you understand system behaviour in production via logs, metrics, and traces. This week focuses on practical instrumentation patterns and how to expose, collect, and query telemetry.

Objectives
- Differentiate logs, metrics, and traces and when to use each.
- Instrument a small app to emit structured logs or Prometheus-style metrics.
- Create a basic dashboard or provide sample queries to visualize the data.

Core Concepts

1) Logs
- Structured JSON logs enable easier parsing and filtering. Keep logs idempotent and avoid leaking secrets.

2) Metrics
- Use counters, gauges, and histograms to measure rates, current values, and distributions (e.g., request latency buckets).

3) Tracing
- Distributed tracing (e.g., OpenTelemetry) connects requests across service boundaries to show latency contributors.

Examples & Commands
```
# expose a Prometheus metric (python prometheus_client)
from prometheus_client import Counter
REQUESTS = Counter('app_requests_total', 'Total requests')

REQUESTS.inc()

# basic structured log example (json)
import json
print(json.dumps({"ts": "2026-02-14T12:00:00Z", "level": "info", "msg": "startup"}))
```

Hands-on Exercise

1. Instrumentation: add `observability/sample_metrics.md` or a small instrumented app that exposes a metric endpoint (e.g., `/metrics`).
2. Document: add `deliverables/week-6-<yourname>.md` describing the metrics/logs you exposed and example queries (PromQL or sample logs filters).

Acceptance criteria
- `deliverables/week-6-<yourname>.md` exists in the PR branch.

Verification & tips
- Include example queries (e.g., PromQL) or `jq` filters for logs to demonstrate you can extract meaningful signals.
- If you cannot run Prometheus locally, provide curl examples demonstrating metric endpoints and sample scrape output.

Further reading
- OpenTelemetry docs, Prometheus best practices, and structured logging guides.

