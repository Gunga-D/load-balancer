## Load balancer

A load balancer is a proxy server that distributes traffic across a number of services

### Details

The project uses round robin algorithm. It has a number of significant limitations. 

List the main ones:
- Services don't have the same resources at the hardware level.
- Algorithm doesn't know about dropped out services. 

### Testing

To run integration test:

```bash
make test
```    

### How to run the service

To launch service:

```bash
docker build -t load-balancer .
docker run load-balancer
```

OR

```bash
make docker
```