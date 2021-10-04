.PHONY: dev
dev:
	uwsgi --http localhost:5000 --py-autoreload 1 --module aplicativo:app
deploy:
	uwsgi --http localhost:5000 --module aplicativo:app

