#!/bin/sh


if [ "$DATABASE" = "postgres" ]
then
    while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME; do
        sleep 1
    done

    echo "PostgreSQL started"

    python manage.py flush --no-input
    python manage.py migrate
    python manage.py create_superuser
   
fi

exec "$@"
