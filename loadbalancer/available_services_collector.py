import requests


def is_service_available(webservice):
    try:
        requests.get(f'http://{webservice}')
    except requests.ConnectionError:
        return False
    return True

def collect(webservices):
    for webservice in webservices + webservices.passive:
        ok = is_service_available(webservice)
        if ok:
            if webservice not in webservices:
                webservices.activate(webservice)
        else:
            if webservice in webservices:
                webservices.deactivate(webservice)
