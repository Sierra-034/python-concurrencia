import os
import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s - %(processName)s: %(message)s',
)

def nuevo_proceso():
    logging.info('Hola, soy un nuevo proceso')
    time.sleep(5)
    logging.info('Fin del proceso')

if __name__ == '__main__':
    process = multiprocessing.Process(target=nuevo_proceso, name='Proceso hijo')
    process.start()

    logging.info('Hola desde el proceso padre')
