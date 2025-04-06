api-dev:
    uv run --package api fastapi dev packages/api/src/api/entrypoint.py

cli +args: 
    uv run --package cli cli {{args}}