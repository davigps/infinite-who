install:
	pdm install
	pdm run pre-commit install

start:
	pdm run fastapi dev app/main.py

format:
	pdm run ruff check --fix .

db-up:
	docker compose up -d

db-down:
	docker compose down
