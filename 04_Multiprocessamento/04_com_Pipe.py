import multiprocessing
import random

def ping(conn):
    conn.send('Mateus')

def pong(conn):
    msg = conn.recv()
    print(f'{msg} Marques')

def main():
    conn1, conn2 = multiprocessing.Pipe(True)

    proc1 = multiprocessing.Process(target=ping, args=(conn1, ))
    proc2 = multiprocessing.Process(target=pong, args=(conn2, ))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

if __name__=='__main__':
    main()
