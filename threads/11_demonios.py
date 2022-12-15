import time
import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def task():
    logging.info('Hola, soy un thread normal')
    time.sleep(2)
    logging.info('El programa finaliza cuando YO finalizo')

def daemon_thread():
    while True:
        logging.info('Nos ejecutamos en segundo plano')
        time.sleep(0.5)

if __name__ == '__main__':
    thread = threading.Thread(target=daemon_thread, daemon=True)
    thread.start()

    input('Presiona una tecla para finalizar el thread principal.')
