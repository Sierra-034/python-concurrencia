import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def thread_1(event):
    logging.info('Estoy a la espera de la señal!!')
    # El comportamiento no es el esperado si se usan demonios
    event.wait()    #   Detiene la ejecución del thread hasta que cambie la bandera
    logging.info('La señal fué dada, lo abandera es True')

def thread_2(event):
    while not event.is_set():
        logging.info('Hola, soy el thread 2')
        time.sleep(0.225) 

if __name__ == '__main__':
    event = threading.Event()   # Bandera (True - False)
    
    thread1 = threading.Thread(target=thread_1, args=(event,))
    thread2 = threading.Thread(target=thread_2, args=(event,))

    thread1.start()
    thread2.start()

    time.sleep(3)
    event.set() # Da la señal
    event.clear()   # Establece la bandera en False
