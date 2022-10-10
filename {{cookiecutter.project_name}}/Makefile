DEV = development


.PHONY: build up stop logs updb stopdb

build: docker-build
up: docker-compose-up
stop: docker-compose-stop
logs: docker-compose-logs
updb: docker-compose-up-db
stopdb: docker-compose-stop-db

docker-build:
	docker build --target "${DEV}" -t {{cookiecutter.app_name}}-"${DEV}" -f ./Dockerfile --build-arg INSTALL_PYTHON_VERSION='{{cookiecutter.python_version}}' --build-arg INSTALL_NODE_VERSION='{{cookiecutter.node_version}}' .

docker-compose-up-db:
	docker-compose -f docker-compose-db.yaml up -d

docker-compose-stop-db:
	docker-compose -f docker-compose-db.yaml stop

docker-compose-up:
{%- if cookiecutter.use_celery == "yes"%}
	docker-compose stop celery # stop celery to avoid conflicts with celery tests
{%- endif %}
	docker-compose up -d flask-dev
{%- if cookiecutter.use_celery == "yes"%}
	docker-compose up -d celery
{%- endif %}

docker-compose-stop:
	docker-compose stop

docker-compose-logs:
	docker-compose logs --tail=100 -f

