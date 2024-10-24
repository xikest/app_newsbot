FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "run_newsbot:app", "--host", "0.0.0.0", "--port", "$PORT"]
