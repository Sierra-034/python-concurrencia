import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 0

def depositos():
    global BALANCE

    for _ in range(0, 1_000_000):
        BALANCE += 1    # Sección crítica


def retiros():
    global BALANCE

    for _ in range(0, 1_000_000):
        BALANCE -= 1    # Sección crítica

if __name__ == '__main__':
    thread_1 = threading.Thread(target=depositos)
    thread_2 = threading.Thread(target=retiros)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    logging.info(f'Valor de balance: {BALANCE}')
