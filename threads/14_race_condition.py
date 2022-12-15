import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 0
lock = threading.Lock()

def depositos():
    global BALANCE

    for _ in range(0, 1_000_000):
        with lock:  # No es necesario usar los métodos (Recomendado)
            BALANCE += 1    # Sección crítica


def retiros():
    global BALANCE

    for _ in range(0, 1_000_000):
        lock.acquire()
        BALANCE -= 1    # Sección crítica
        lock.release()

if __name__ == '__main__':
    thread_1 = threading.Thread(target=depositos)
    thread_2 = threading.Thread(target=retiros)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    logging.info(f'Valor de balance: {BALANCE}')
