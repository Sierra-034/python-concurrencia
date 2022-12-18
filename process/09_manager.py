import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

# Manager -> Namespace -> Contexto
def get_valor(namespace):
    while namespace.codigofacilito is None:
        time.sleep(0.2)
        logging.info('codigofacilito no posée valor')
    else:
        logging.info(namespace.codigofacilito)

def set_valor(namespace):
    time.sleep(4)
    namespace.codigofacilito = 'Una escuela de educación en línea'

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    namespace.codigofacilito = None

    process_1 = multiprocessing.Process(target=get_valor, args=(namespace,))
    process_2 = multiprocessing.Process(target=set_valor, args=(namespace,))

    process_1.start()
    process_2.start()
