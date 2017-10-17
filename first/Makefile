deps:
	./env/bin/pip install -r requirements.txt

start: deps
	foreman start -m worker=1,writer=1 -e .env

.PHONY: deps, start