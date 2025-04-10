FROM python:3.10.14-slim-bullseye AS builder

COPY pyproject.toml  ./
RUN python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

FROM python:3.10.14-slim-bullseye

WORKDIR /app
COPY --from=builder requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
