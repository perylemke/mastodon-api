.PHONY: run-compose
run-compose:
	@docker-compose up -d --build

.PHONY: down-compose
down-compose:
	@docker-compose down

.PHONY: run-local
run-local:
	@poetry run uvicorn --port 8080 mastodon_api.app:app --reload

.PHONY: test
test:
	@poetry run pytest -v --maxfail=1

.PHONY: shell
shell:
	@poetry run ipython

.PHONY: import-data
import-data:
	@poetry run python examples/albums.py
	@poetry run python examples/members.py

.PHONY: prune
prune:
	@docker system prune -f