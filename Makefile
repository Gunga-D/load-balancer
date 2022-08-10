balancer: 
	py ./loadbalancer/app.py

docker:
	docker build -t load-balancer .
	docker run load-balancer

dependencies:
	pip install -r requirements.txt

test:
	docker compose -f ./tests/docker-compose-tests.yaml up -d --build
	pytest -s --disable-warnings || true
	docker compose -f ./tests/docker-compose-tests.yaml down

