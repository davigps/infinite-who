install: ## Install the dependencies
	pdm install
	pdm run pre-commit install

start: ## Start the FastAPI server
	pdm run fastapi dev app/main.py

format: ## Format the code with ruff
	pdm run ruff check --fix .

test: ## Run the tests
	pdm run pytest

db-up: ## Start the database container
	docker compose up -d

db-down: ## Stop and remove the database container
	docker compose down

db-migrate: ## Create migration with alembic. Usage: "make db-migrate message='migration message'"
	pdm run alembic revision --autogenerate -m "$(message)"

db-upgrade: ## Apply migrations
	pdm run alembic upgrade head

db-downgrade: ## Rollback the last migration
	pdm run alembic downgrade
