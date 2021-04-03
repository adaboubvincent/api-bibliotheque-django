web: gunicorn apiBibliotheque.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate
release: manage.py makemigrations
release: manage.py migrate
python manage.py makemigrations
python manage.py migrate
manage.py makemigrations
manage.py migrate