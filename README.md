## Load balancer

A load balancer is a proxy server that distributes traffic across a number of services

### Details

The project supports 2 algorithms: round robin and least connections. 

Current realization uses least connections.

### Testing

To run integration test:

```bash
make test
```    

### How to run the service

To launch service:

```bash
docker build -f Dockerfile -t load-balancer .
docker run -p 9092:5000 --network="host" load-balancer
```

OR

```bash
make docker
```