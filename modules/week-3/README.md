 # Week 3 — Containerization with Docker

Overview

Containers package an application and its dependencies into a reproducible runtime image. This week focuses on building lightweight images, understanding layering, and producing multi-stage builds for small final artifacts.

Objectives
- Write Dockerfiles that follow best practices for caching, security, and size.
- Build and run container images locally and understand tagging/pushing workflows.
- Know how to debug container issues and inspect image layers.

Core Concepts

1) Image Layers & Caching
- Each Dockerfile instruction creates a layer; reordering instructions influences cache reuse.
- Keep frequently changing steps (e.g., application code) after less-frequently-changing steps (e.g., system package installation).

2) Multi-stage Builds
- Use builder stages to compile or build artifacts, then copy only runtime files into a minimal base image.

3) Security & Runtime
- Avoid running as root inside the container; drop unnecessary capabilities and minimize installed packages.

Practical Examples
```
# simple multi-stage Dockerfile (python example)
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt ./
RUN pip install --user -r requirements.txt
COPY . .

FROM python:3.11-slim
WORKDIR /app
COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
CMD ["python", "app.py"]
```

Hands-on Exercise

1. Add a minimal app under `app/` (flask, simple Node server, or static site) and an efficient `app/Dockerfile`.
2. Provide `deliverables/week-3-<yourname>.md` describing build commands, tags used, and runtime test commands (e.g., `docker run -p 8080:8080 <tag>`).

Acceptance criteria
- `app/Dockerfile` exists in the project tree.
- `deliverables/week-3-<yourname>.md` documents how to build and run the image.

Debug & verification tips
- Use `docker build --progress=plain` to see build steps and caching.
- Inspect layers with `docker history <image>` and contents with `docker run --rm -it <image> bash` (if bash exists) or `docker run --rm -it <image> sh`.

Further reading
- Dockerfile best practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Container security guidance: minimizing attack surface and user privileges.

