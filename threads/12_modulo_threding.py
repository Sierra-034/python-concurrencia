import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def nueva_tarea():
    current_thread = threading.current_thread()
    name = current_thread.getName()
    id = threading.get_ident()
    
    logging.info(f'El thread actual es: {current_thread}, con nombre: {name}')
    logging.info(f'El id actual es: {id}')

    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info('Nos encontramos en el thread principal')
        
        logging.info(thread)

if __name__ == '__main__':
    thread = threading.Thread(target=nueva_tarea, name='thread-facilito')
    thread.start()
