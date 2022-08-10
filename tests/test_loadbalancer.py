import pytest
import time

from loadbalancer.app import core


@pytest.fixture
def client():
    with core.test_client() as client:
        yield client

def test_loadbalancer(client):
    time_end = time.time() + 300
    while time.time() < time_end:
        result = client.get('/')
        print(result.data)
        time.sleep(0.1)