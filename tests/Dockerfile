FROM python:3.8-slim-buster

WORKDIR /app/tests

RUN pip install apscheduler
RUN pip install flask

COPY ./mock_webservice/app.py ./webservice.py

CMD ["python", "webservice.py"]