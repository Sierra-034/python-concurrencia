import time
import logging
import requests
import threading

from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s',
)

URLS = [
    'https://codigofacilito.com/',
    'https://twitter.com/home',
    'https://www.google.com/',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com/',
    'https://www.youtube.com/',
]

def generate_request(url):
    return url, requests.get(url)

def check_status_code(response, url):
    logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def math_operation(n_1, n_2):
    return n_1 + n_2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(generate_request, url) for url in URLS]
        for futuro in as_completed(futuros):
            url, response = futuro.result()
            check_status_code(response, url)

        future = executor.submit(math_operation, 10, 20)
        future.add_done_callback(
            lambda future: logging.info(f'El resultado es: {future.result()}'))
