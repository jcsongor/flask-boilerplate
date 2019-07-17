# Boilerplate for a minimal flask app
## Prerequisites
To run the server locally, all you need is [docker](https://www.docker.com/) and [GNU Make](https://www.gnu.org/software/make/).

## Starting the service
```bash
make start
```
Open [http://localhost:5000/healthcheck](http://localhost:5080/healthcheck) in your browser to verify that the service is up and running.

## Running the test suite
```bash
make test
```

## Stopping the service
```bash
make stop
```
