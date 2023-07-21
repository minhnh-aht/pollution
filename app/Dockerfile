# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9 AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
COPY . /app
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
# ENTRYPOINT ["python3"] 
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

FROM builder as dev-envs
RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
# RUN python manage.py migrate
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
