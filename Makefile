serve:
	python3 manage.py runserver 0.0.0.0:8000
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
develop:
	python manage.py runserver_plus --cert-file cert.crt
sync:
	python3 manage.py migrate --run-syncdb 
kill:
	sudo fuser -k 8000/tcp
admin:
	python3 manage.py createsuperuser