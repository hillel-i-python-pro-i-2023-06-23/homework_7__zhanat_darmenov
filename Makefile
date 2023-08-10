
.PHONY: d-homework-i-run
d-homework-i-run:
	@make d-stop &&\
	make init-configs &&\
	make d-run


# Local Checks:
.PHONY: init-dev
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: proj-i-run
proj-i-run:
	@python main.py


# Docker Preparation:
.PHONY: init-configs
init-configs:
	@cp ./docker-compose.override-example.yml docker-compose.override.yml

.PHONY: create-image
create-image:
	@docker build --tag getting-started .

.PHONY: d-run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build

.PHONY: d-stop
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down

.PHONY: d-purge
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


# Pre-commit Hooks:
# To use these one: "git add .pre-commit-config.yaml"
.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files

