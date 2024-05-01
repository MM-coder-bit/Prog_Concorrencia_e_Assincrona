import multiprocessing

def ping(queue):
    queue.put('Mateus')

def pong(queue):
    msg = queue.get()
    print(f'{msg} Marques')

def main():
    queue = multiprocessing.Queue()

    proc1 = multiprocessing.Process(target=ping, args=(queue, ))
    proc2 = multiprocessing.Process(target=pong, args=(queue, ))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

if __name__=='__main__':
    main()
