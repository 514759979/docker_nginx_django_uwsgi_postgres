# docker_nginx_django_uwsgi_postgres
Docker+nginx+django+uwsgi+postgres


1. `docker-compose up`

2. `docker exec -it <container-id> bash`

3. `python manage.py makemigrations`

   `python manage.py migrate`
   
   `python manage.py createsuperuser`
   
   `python manage.py collectstatic`
