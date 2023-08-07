mig:
	python manage.py makemigrations

rate:
	python manage.py migrate

user:
	python manage.py createsuperuser

run:
	python manage.py runserver