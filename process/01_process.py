import os
import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s - %(processName)s: %(message)s',
)

def nuevo_proceso(mensaje):
    logging.info('Hola, soy un nuevo proceso')
    time.sleep(5)
    logging.info(mensaje)

if __name__ == '__main__':
    # args o kargs
    process = multiprocessing.Process(
        target=nuevo_proceso,
        name='Proceso hijo',
        args=('Mensaje desde argumento',))

    process.start()
    process.join()
    logging.info('Hola desde el proceso padre')
