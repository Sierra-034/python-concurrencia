import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
)

# Timer

def callback():
    logging.info('Callback que no se ejecuta de inmediato')

if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()

    logging.info('Hola, soy el thread principal')
    logging.info('Estoy a la espera de callback')
