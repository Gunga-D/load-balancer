balancer: 
	python ./loadbalancer/app.py

docker:
	docker build -f Dockerfile -t load-balancer .
	docker run -p 9092:5000 --network="host" load-balancer

test:
	docker-compose -f ./docker-compose-tests.yaml up -d --build

stopped-test:
	docker-compose -f ./docker-compose-tests.yaml down

