# Observability Starter

This file shows how to expose a simple Prometheus metric from a Python app.

Example (prometheus_client):

```
from prometheus_client import Counter, start_http_server

REQUESTS = Counter('app_requests_total', 'Total requests')

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        REQUESTS.inc()
        time.sleep(5)
```

If you cannot run Prometheus, curl `http://localhost:8000/` to view metric output.
