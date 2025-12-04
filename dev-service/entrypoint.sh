#!/bin/sh

echo "Waiting for PostgreSQL..."

# Wait until PostgreSQL is ready
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  sleep 1
done

echo "PostgreSQL is ready."

# Run DB migrations
echo "Running database migrations..."
python init_db.py

# Start Flask app
echo "Starting app..."
exec "$@"
