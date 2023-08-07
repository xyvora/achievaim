@api: && docker-stop
  -docker compose up backend db --build

@api-ci:
  docker compose -f docker-compose-testing.yml up -d backend db

@backend-test: ci-db && docker-stop
  -cd backend && \
  poetry run pytest && \
  cd ..

@backend-test-ci: ci-db && docker-stop
  cd backend && \
  poetry run pytest && \
  cd ..

@black:
  -cd backend && \
  poetry run black app tests && \
  cd ..

@black-ci:
  cd backend && \
  poetry run black app tests --check && \
  cd ..

@build-backend-dev:
  -cd backend && \
  docker build -t backend:dev . && \
  cd ..

@build-dev: build-backend-dev build-frontend-dev

@build-frontend-dev:
  -cd frontend && \
  docker build -t frontend:dev . && \
  cd ..

@build-backend-prod:
  -cd backend && \
  docker build -t backend:latest --target prod . && \
  cd ..

@build-frontend-prod:
  -cd frontend && \
  docker build -t frontend:latest . && \
  cd ..

@build-prod: build-backend-prod build-frontend-prod

@ci-db:
  docker compose -f docker-compose-testing.yml up -d db

@compose-up:
  docker compose up --build

@compose-up-detached:
  docker compose up -d --build

@db:
  docker compose up db

@docker-stop:
  docker compose down

@frontend-dev:
  -cd frontend && \
  npm run dev && \
  cd ..

@frontend-check:
  -cd frontend && \
  npm run check && \
  cd ..

@frontend-check-ci:
  cd frontend && \
  npm run check && \
  cd ..

@frontend-format:
  -cd frontend && \
  npm run format && \
  cd ..

@frontend-format-ci:
  cd frontend && \
  npm run format && \
  cd ..

@frontend-lint:
  -cd frontend && \
  npm run lint && \
  cd ..

@frontend-lint-ci:
  cd frontend && \
  npm run lint && \
  cd ..

@frontend-test:
  -cd frontend && \
  npm run test && \
  cd ..

@frontend-test-ci:
  cd frontend && \
  npm run test
  cd ..

@generate-types:
  -cd frontend && \
  npm run generate-types && \
  cd ..

@install:
  echo Installing backend
  just --justfile {{justfile()}} install-backend
  echo Installing frontend
  just --justfile {{justfile()}} install-frontend

@install-backend:
  -cd backend && \
  poetry install && \
  cd ..

@install-frontend:
  -cd frontend && \
  npm install
  cd ..

@lint:
  echo mypy
  just --justfile {{justfile()}} mypy
  echo ruff
  just --justfile {{justfile()}} ruff
  echo black
  just --justfile {{justfile()}} black
  echo frontend linting
  just --justfile {{justfile()}} frontend-lint
  echo frontend check
  just --justfile {{justfile()}} frontend-check

@mypy:
  -cd backend && \
  poetry run mypy . && \
  cd ..

@mypy-ci:
  cd backend && \
  poetry run mypy . && \
  cd ..

@playwright-install:
  -cd frontend && \
  npx playwright install && \
  cd ..

@ruff:
  -cd backend && \
  poetry run ruff check . && \
  cd ..

@ruff-ci:
  cd backend && \
  poetry run ruff check --exit-non-zero-on-fix . && \
  cd ..
