.PHONY: build logs rebuild restart shell start stop test 

build:
	docker-compose build

logs:
	docker-compose logs -f

rebuild: stop build start

restart: stop start

shell:
	docker-compose exec app sh

start:
	docker-compose up -d

stop:
	docker-compose down

test:
	docker-compose run --rm app python -m unittest discover . '*_test.py'

