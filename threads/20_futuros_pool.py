import time
import logging
import requests
import threading
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

def check_status_code(response):
    logging.info(f'La respuesta del servidor {response[0]} es: {response[1].status_code}')

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(generate_request, url) for url in URLS]
        for futuro in futuros:
            futuro.add_done_callback(lambda future: check_status_code(future.result()))
