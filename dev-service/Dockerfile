FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN sqlite3 test.db < init_db.sql

EXPOSE 5000

CMD ["python", "app.py"]
