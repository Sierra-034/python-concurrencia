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
        apply_result = executor.apply_async(is_even, args=(10,))
        logging.info('Espera apply result por un valor')
        apply_result.wait(timeout=2)
        logging.info('Apply result finalizado')
        logging.info(f'El resultado es: {apply_result.get(timeout=1)}')
        logging.info('Fin del programa')
