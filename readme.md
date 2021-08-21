# A template that aimed to quickstart your flask api development

## Features

+ Restfull API with flask
+ Automatic API Documentation (with swagger)
  - Creating Documentation
  - Serving Documentation
  - Run Examples in the Browser
+ SqlAlchemy ORM
+ Run Testcases in Docker (so you can run them in CI/CD)
+ Deploy with Docker

## Test
    docker-compose -f test-docker-compose.yml up --build

## Run
    docker-compose up --build

## See Documentation & Demo
    http://localhost:7654/swagger-ui
