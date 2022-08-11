FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    make \
    build-essential

WORKDIR /app/tests

RUN pip install apscheduler
RUN pip install flask

COPY ./mock_webservice/app.py ./webservice.py

CMD ["python", "webservice.py"]