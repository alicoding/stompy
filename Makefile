compose_build: 
	docker-compose build

test: compose_build
	docker-compose run stompy sh -c "pip install coverage flake8 && flake8 . && python /app/stompy/manage.py test"

up: compose_build
	docker-compose up
