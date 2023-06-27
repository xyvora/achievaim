@api: && docker-stop
  -docker compose up --build

@backend-test: ci-db && docker-stop
  -cd backend && \
  poetry run pytest && \
  cd ..

@black:
  -cd backend && \
  poetry run black app tests && \
  cd ..

@black-ci:
  -cd backend && \
  poetry run black app tests --check && \
  cd ..

@build-dev:
  -cd backend && \
  docker build -t backend:dev . && \
  cd ..

@build-prod:
  -cd backend && \
  docker build -t backend:latest --target prod . && \
  cd ..

@ci-db:
  docker compose up -d db

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

@frontend-format:
  -cd frontend && \
  npm run format && \
  cd ..

@frontend-lint:
  -cd frontend && \
  npm run lint && \
  cd ..

@frontend-test: api && docker-stop
  -cd frontend && \
  npm run test && \
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

@ruff:
  -cd backend && \
  poetry run ruff check . && \
  cd ..

@ruff-ci:
  -cd backend && \
  poetry run ruff check --exit-non-zero-on-fix . && \
  cd ..
