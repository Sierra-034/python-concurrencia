import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

# Colas
def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f'El elemento es: {element}')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(1, 21):
        queue.put(x)

    logging.info('La cola ya posée elementos')
    process_1 = multiprocessing.Process(target=get_elements, args=(queue,))
    process_2 = multiprocessing.Process(target=get_elements, args=(queue,))
    process_3 = multiprocessing.Process(target=get_elements, args=(queue,))

    process_1.start()
    process_2.start()
    process_3.start()

    process_1.join()
    process_2.join()
    process_3.join()

    logging.info('Fin de los procesos')
