#---------builder------------
    FROM python:3.12-slim-bookworm AS builder
    WORKDIR /app

    # install uv
    COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

    # install dependencies (no lockfile)
    COPY pyproject.toml /app/
    RUN uv sync --no-dev --all-extras

    # install dependencies (with lockfile)
    # COPY pyproject.toml uv.lock /app/
    # RUN uv sync --no-dev --frozen

    #---------runner------------
    FROM python:3.12-slim-bookworm AS runner
    WORKDIR /app

    COPY --from=builder /app/.venv /app/.venv
    ENV PATH=/app/.venv/bin:$PATH

    COPY src/app /app/app

    ENTRYPOINT []
