import time
import logging
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def callback_future(future):
    logging.info('Callback ejecutado después de asignación')
    logging.info(f'El futuro es: {future.result()}')

if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(lambda future: logging.info('Hola, soy una lambda'))

    logging.info('Comenzamos una tarea compleja')
    time.sleep(2)
    logging.info('Termina tarea compleja')
    logging.info('Asignando valor al futuro')
    future.set_result('código fácilito')
    logging.info('El futuro ya posée un valor')
