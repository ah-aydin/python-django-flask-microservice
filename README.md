# Microservice example code Django + Flask

A repo for me to refer to when creating microservices with docker.

To run, go to `main` and `product_service`, then run `docker-compose up --build` to run the docker containers.

In the `product_service` container, go to the django container and run
```python manage.py makemigrations
python manage.py migrate
```

In the `main` container, go to the flask container and run
```export FLASKAPP=main
flask db init
flask db migrate
flask db upgrade
```

- `localhost:7000` will have the django app running
- `localhost:7001` will have the flask app running
- `localhost:33066` will have MySql for the django app running
- `localhost:330067` will have MySql for the flask app running

This was made following https://www.youtube.com/watch?v=0iB5IPoTDts&t=4247s.