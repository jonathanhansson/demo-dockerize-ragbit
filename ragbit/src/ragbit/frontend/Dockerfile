FROM python:3.13-slim

WORKDIR /app/frontend
COPY frontend .

# installs uv
RUN pip install --no-cache-dir uv

# excluding packages that are marked as dev
RUN uv sync --no-dev

# 
CMD ["sh", "-c", "uv run streamlit run app.py \
    --server.port=${PORT:-8501} \
    --server.address=0.0.0.0"]
