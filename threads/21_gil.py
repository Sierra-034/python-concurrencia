import time
import threading
import multiprocessing

def countdown(number):
    while number > 0:
        number -= 1

if __name__ == '__main__':
    start = time.time()
    count = 100_000_000

    t_1 = multiprocessing.Process(target=countdown, args=(count,))
    t_2 = multiprocessing.Process(target=countdown, args=(count,))

    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()

    print(f'Tiempo transcurrido {time.time() - start}')
