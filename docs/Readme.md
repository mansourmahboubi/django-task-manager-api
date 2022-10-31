# Start developemnt

```
git clone repo:TODO
pre-commit
virtualenv .venv -p /usr/bin/python3.8
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# Architecture

The Application is developed using django arch. Django by default uses an MVC like architecture (MTV).
In this application we have followed MVC more accurately. Each app contains another file named `services.py` the file holds most of business logic and this way we can write functional tests.

# SWAGGER

BASE_URL/api/docs
