import requests


def get_clientes():
    url = 'http://127.0.0.1:8000/api/v1/clientes'
    r = requests.get(url)
    clientes = r.json()

    return clientes