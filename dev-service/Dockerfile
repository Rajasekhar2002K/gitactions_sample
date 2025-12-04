FROM python:3.9-slim

WORKDIR /app

# Install sqlite3 CLI
RUN apt-get update && apt-get install -y sqlite3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Initialize DB
RUN sqlite3 test.db < init_db.sql

EXPOSE 5000

CMD ["python", "app.py"]