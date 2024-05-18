#!/bin/sh

# Wait for MySQL to be ready
while ! mysqladmin ping -h"$MYSQL_HOST" --silent; do
    echo "Waiting for database connection..."
    sleep 2
done

echo "Database is up - executing command"
exec "$@"
