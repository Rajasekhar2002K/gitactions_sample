#!/bin/sh

echo "Waiting for PostgreSQL..."

# Wait for the PostgreSQL service to be ready
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  sleep 1
done

echo "PostgreSQL is ready."

# Run database migrations
echo "Running database migrations..."
python init_db.py

# Start the Flask app
echo "Starting Flask app..."
exec "$@"
