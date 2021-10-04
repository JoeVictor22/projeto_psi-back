.PHONY: dev
dev:
	uwsgi --http localhost:5000 --py-autoreload 1 --module service:app
deploy:
	uwsgi --http localhost:5000 --module service:app
