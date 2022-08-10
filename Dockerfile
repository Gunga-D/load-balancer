FROM python:3.8-slim-buster

WORKDIR /app

COPY Makefile ./

COPY requirements.txt ./
RUN make dependencies

COPY . .

EXPOSE 8080:5000

CMD ["make", "balancer"]