web: python manage.py migrate && docker exec backend python3 manage.py collectstatic --noinput
 && gunicorn todo_list.wsgi