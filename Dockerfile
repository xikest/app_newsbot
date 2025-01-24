FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --upgrade pip \
    && pip install --default-timeout=100 --no-cache-dir -r requirements.txt

EXPOSE 8008

CMD ["uvicorn", "app_newsbot:app", "--host", "0.0.0.0", "--port", "8008"]
