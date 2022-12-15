import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def conexion_base_datos():
    logging.info('Comienza conexión a base de datos')
    time.sleep(2)

def consulta_servidor_web():
    logging.info('Comienza consulta a servidor')
    time.sleep(4)

if __name__ == '__main__':
    thread_1 = threading.Thread(target=conexion_base_datos)
    thread_2 = threading.Thread(target=consulta_servidor_web)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    logging.info('Final del programa, los threads han finalizado')
