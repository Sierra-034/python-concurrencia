import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 100
lock = threading.RLock()

if __name__ == '__main__':
    lock.acquire()  # Estado: Ocupado
    lock.acquire()  # A la espera de que sea liberado (Aún no se libera, espera por siempre)
    BALANCE -= 10
    lock.release()
    lock.release()  # Debe liberarse las mismas veces que fué adquirido

    logging.info(f'Finaliza thread principal con balance: {BALANCE}')