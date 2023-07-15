#!/bin/bash
cd /var/www/tuishop
source /var/www/tuishop/ venv/bin/activate
python3 manage.py runserver 0.0.0.0:80
