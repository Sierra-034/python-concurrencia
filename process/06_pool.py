import time
import logging
from multiprocessing import Pool

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s',
)

def is_even(number):
    time.sleep(4)
    return number % 2 == 0

if __name__ == '__main__':
    with Pool(processes=2) as executor:
        result = executor.apply(is_even, args=(10,))
        logging.info(f'El resultado es: {result}')

    logging.info('Main process')
