# Task-Manager-API

A simple task-manager using Django 4.1 and django-ninja for async support.

## Start developemnt

```
git clone repo:TODO
pre-commit
virtualenv .venv -p /usr/bin/python3.8
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Architecture

The Application is developed using django arch. Django by default uses an MVC like architecture (MTV).
In this application we have followed MVC more accurately. Each app contains another file named `services.py` the file holds most of business logic and this way we can write functional tests.

## SWAGGER

BASE_URL/api/docs

# Project description

## Developers

1. List of tasks
2. Add tasks
3. Self-assign tasks

## Project Manager

1. Add project
2. Retrieve project
3. Add task
4. Retrieve tasks
5. Assign tasks to developers

## Required APIS

- [x] Login
- [x] Signup
- [x] List of tasks in a project (developers can see others’ tasks in the project too)
- [x] List of user’s tasks in the project
- [x] Project Manager assigns task to a developer (check permissions)

## Objectives

- [ ] Designing the database
- [ ] Architecture and software components
- [ ] Clean code and readability
- [ ] Scalability
- [ ] API design
