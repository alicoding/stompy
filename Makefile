build:
	docker build -t stompy stompy/

test: build
	docker run --user root -t stompy sh -c "pip install coverage flake8 && flake8 . && python /app/stompy/manage.py test"

compose_build: build
	docker-compose build

up: compose_build
	docker-compose up
