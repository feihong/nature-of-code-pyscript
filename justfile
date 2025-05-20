# You need to get this manually if you're not using a virtualenv
scripts_path := `python -c 'import sysconfig; print(sysconfig.get_path("scripts"))'`

install:
	pip install -r requirements.txt

help:
  just --list

dev:
  bun run --hot dev.ts

# Launches a server on localhost:8000
serve:
	{{scripts_path}}/aiohttp-devtools runserver serve.py
