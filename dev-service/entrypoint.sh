#!/bin/sh

echo "Waiting for PostgreSQL..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  echo "postgres:$POSTGRES_PORT - no response"
  sleep 1
done

echo "PostgreSQL is ready."

echo "Running database migrations..."
python init_db.py

echo "Starting app..."
exec "$@"
