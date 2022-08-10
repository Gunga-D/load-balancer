from flask import Flask
import requests

from config import ConfigWrapper
from webservices_container import WebServicesContainer
import available_services_collector
from algorithm import RoundRobin


config = ConfigWrapper('./configs/loadbalancer.yaml')
webservices = WebServicesContainer(config.get('webservices'))
alg = RoundRobin(webservices)

core = Flask(__name__)

@core.route('/')
def router():
    available_services_collector.collect(webservices)
    alg.update_pool(webservices)

    distributed_server = alg.get_server()
    response = requests.get(f'http://{distributed_server}')
    return response.content, response.status_code

if __name__ == '__main__':
    core.run(host='0.0.0.0')