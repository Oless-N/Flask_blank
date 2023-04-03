DOCKER_LOCAL=docker-compose -f docker-compose.yml
COLS_LINES=-e COLUMNS="`tput cols`" -e LINES="`tput lines`"

restart:
	$(DOCKER_LOCAL) stop
	$(DOCKER_LOCAL) down --rmi local --remove-orphans
	$(DOCKER_LOCAL) build
	$(DOCKER_LOCAL) up -d

restart-v: ## remove local images, volumes(postgres/redis) and restart service
	$(DOCKER_LOCAL) stop
	$(DOCKER_LOCAL) down --rmi local -v --remove-orphans
	$(DOCKER_LOCAL) build
	$(DOCKER_LOCAL) up -d

sh:
	$(DOCKER_LOCAL) exec $(COLS_LINES) transaction_limiter /bin/sh

logs:
	COMPOSE_HTTP_TIMEOUT=604800 $(DOCKER_LOCAL) logs -f

down:
	printf "=========Down app ${IMAGE}=========\n\n"
	$(DOCKER_LOCAL) down

clear:
	docker ps -a --format "{{ .ID }}" | xargs docker rm -f
	docker image ls -a --format "{{ .ID }}" | xargs docker rmi -f

run_docker:
	docker-compose down
	docker-compose -f docker-compose.yml up -d

install_dev:
	pip install -r requirements/requirements.txt

.PHONY: shell
