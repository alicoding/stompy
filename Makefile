build: 
	docker-compose build

test: build
	docker-compose run stompy sh -c "pip install coverage flake8 && flake8 . && python /app/manage.py test"

up: build
	docker-compose up

migrate: build
	docker-compose run stompy sh -c "python /app/manage.py migrate"

collectstatic: build
	docker-compose run stompy sh -c "python /app/manage.py collectstatic -c --noinput"
