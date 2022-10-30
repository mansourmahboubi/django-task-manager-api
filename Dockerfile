FROM python:3.8.12-slim-bullseye as build-python
COPY requirements.txt /app/
WORKDIR /app/
RUN pip install -r requirements.txt

FROM python:3.8.12-slim-bullseye

WORKDIR /opt/app

COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/


COPY . .

ENTRYPOINT ["gunicorn", "core.asgi:application" ,"-k","uvicorn.workers.UvicornWorker"]