# Multi-stage Dockerfile for production and tests.
FROM python:3.13-slim AS base
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

# Install uv binary.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project files.
COPY pyproject.toml uv.lock README.md VERSION /app/
COPY src/ /app/src/
RUN uv sync --no-dev --frozen && uv pip install --no-deps .

# Production image.
FROM base AS production

COPY --from=base /app/ /app/
ENTRYPOINT ["app"]
CMD ["hello"]

# Test image.
FROM base AS test

COPY tests/ /app/tests/
RUN uv sync --group dev --frozen

CMD ["uv", "run", "pytest", "tests/"]
