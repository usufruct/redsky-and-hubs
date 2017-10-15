deps:
	./env/bin/pip install -r requirements.txt

start: deps
	foreman start -m worker=3,writer=20 -e .env

.PHONY: deps, start