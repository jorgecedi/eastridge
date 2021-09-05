# Eastridge Project

Django application that exposes an RESTful API that create, read, update and
delete Invoice and related Invoice Items.

## Setup

### Requirements

- docker >= 20
- docker-compose >= 1.25
- git >= 2.0

### Creating containers

Once the requirements are installed run `docker-compose up --build -d`. This
command is going to build and spin up the application container in detached
mode. It will manage all application dependencies.

If everything went well you will have the application running and listening for
new connections on `http://localhost:8000`. You can verify this with the command
`docker-compose ps`.

## Running tests

Once the application is up and running you can run tests with the following
command:
`docker-compose exec web python manage.py test invoices`.

### Test coverage

To get the test coverage report you can run the next command:
`docker-compose exec web bash -c "coverage run manage.py test && coverage report"`.

## API Documentation

You can find API documentation with swagger on `http://localhost:8000/swagger`
or the default Django Rest Framework documentation on
`http://localhost:8000/api/v1/`.

### Importing to Postman

The OpenAPI schema is located here
`http://localhost:8000/swagger/?format=openapi`. Open Postman app and then click
on `Import` button, select `Link` tab and paste the previous link. This will
create the full collection on your postman app.

## Invoice date format
ISO 8601 with Timezone Information. Eg. `2021-09-05T17:39:33.593620+00:00`.

