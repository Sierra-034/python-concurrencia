import time
import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

class Publisher(multiprocessing.Process):
    def __init__(self, connection):
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info('Proceso publisher')
        for x in range(20):
            self.connection.send(f'Mensaje desde publisher: {x}')
            time.sleep(0.5)

        self.connection.send(None)
        self.connection.close()
        logging.info('Conexión cerrada para publisher')

class Subscriber(multiprocessing.Process):
    def __init__(self, connection):
        self.is_alive = True
        self.connection = connection
        multiprocessing.Process.__init__(self)

    def run(self):
        logging.info('Proceso subscriber')
        while self.is_alive:
            result = self.connection.recv() # Bloquea el thread hasta recivir información
            self.is_alive = result is not None
            logging.info(f'En subscriber: {result}')
        else:
            self.connection.close()
            logging.info('Conexión cerrada para subscriber')


if __name__ == '__main__':
    connection_1, connection_2 = multiprocessing.Pipe()
    publisher = Publisher(connection_1)
    subscriber = Subscriber(connection_2)

    publisher.start()
    subscriber.start()
