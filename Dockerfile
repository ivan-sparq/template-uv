#  Multi-stage Dockerfile for production and test
#---------builder------------
FROM python:3.13 AS base
WORKDIR /app
ENV PATH=/app/.venv/bin:$PATH

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project files
COPY pyproject.toml uv.lock README.md /app/
COPY src/ /app/src/
RUN uv sync --no-dev --frozen
RUN uv pip install -e .

#--------- production ------------
FROM base AS production

COPY --from=base /app/ /app/

ENTRYPOINT []

#--------- tester ------------
FROM base AS test
ENV PATH=/app/src/app:$PATH

COPY --from=base /app/ /app/
# Copy tests directory
COPY tests/ /app/tests/
# Install all dependencies including dev dependencies
RUN uv sync --group dev --frozen

# Default command to run tests
CMD ["uv", "run", "pytest", "tests/"]
