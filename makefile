
DOCKER_CONTAINER_NAME = fastlms-web-1

migrations:
	docker exec $(DOCKER_CONTAINER_NAME) alembic revision --autogenerate;

migrate:
	docker exec $(DOCKER_CONTAINER_NAME) alembic upgrade head;

up: ## Docker compose up
	docker compose up --build;

up-full: ## Docker compose up
	docker compose -f docker-compose-full.yml up --build;

	

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help