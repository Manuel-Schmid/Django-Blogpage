#!/bin/bash
set -e
 
# Check if script was called by CMD, can be sh -c 'CMD' or CMD
if [ "$2" = 'runserver' ]; then
    # Wait for the database to be available
    until nc -vzw 2 "db" "3306"; do echo "mysql is not available. waiting..." && sleep 2; done
 
    echo "Apply database migrations"
    python ./manage.py migrate
 
    echo "Load fixtures"
    python ./manage.py loaddata app/fixtures/users.json

    echo "Collect static files"
    python ./manage.py collectstatic --noinput
fi

exec "$@"