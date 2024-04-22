import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))

    th.start() # Adiciona a thread na pool de threads prontos para execuçao

    print('Podemos fazer outras coisas no programa enquanto o thread vai executando...')
    print('Mateus Marques ' * 2)

    th.join() # Avisa para ficar aguardando aqui até a thread terminar a execução

    print('Pronto')

def contar(oque, numero):
    for n in  range(1, numero + 1):
        print(f'{n} {oque}(s)...')
        time.sleep(1)

if __name__ == '__main__':
    main()