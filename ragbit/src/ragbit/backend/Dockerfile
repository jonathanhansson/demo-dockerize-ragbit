FROM python:3.13-slim

# path inside of the container
WORKDIR /app

# later in docker compose, we'll use a context that is parent of frontend folder
# then we can send in the frontend folder by writing frontend
COPY backend backend
COPY knowledge_base knowledge_base

WORKDIR /app/backend

# installs uv
RUN pip install --no-cache-dir uv

# excluding packages that are marked as dev
RUN uv sync --no-dev

CMD ["uv", "run","uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]