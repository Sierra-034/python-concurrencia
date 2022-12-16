import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def math_operation(number_1, number_2):
    time.sleep(1)
    result = number_1 + number_2
    logging.info(f'Resultado de {number_1} + {number_2} = {result}')

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='facilitos') as executor:
        executor.submit(math_operation, 10, 20)
        executor.submit(math_operation, 40, 50)
        executor.submit(math_operation, 100, 200)
        executor.submit(math_operation, 60, 70)

        executor.shutdown()
        executor.submit(math_operation, 5, 5)   # Error
