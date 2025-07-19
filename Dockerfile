FROM python:3.10-slim

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt

EXPOSE 8008

CMD ["uvicorn", "app_newsbot:app", "--host", "0.0.0.0", "--port", "8008"]