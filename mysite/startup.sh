#!/bin/bash

python manage.py migrate
python manage.py loaddata db.json
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8080
