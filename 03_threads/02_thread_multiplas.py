import threading
import time

def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco'  , 8 )),
        threading.Thread(target=contar, args=('moeda'   , 23)),
        threading.Thread(target=contar, args=('pato'    , 12)),
    ]

    [th.start() for th in threads] # Adiciona a thread na pool de threads prontos para execuçao

    print('Podemos fazer outras coisas no programa enquanto o thread vai executando...')
    print('Mateus Marques ' * 2)

    [th.join() for th in threads] # Avisa para ficar aguardando aqui até a thread terminar a execução

    print('Pronto')

def contar(oque, numero):
    for n in  range(1, numero + 1):
        print(f'{n} {oque}(s)...')
        print(10 * '-')
        time.sleep(1)

if __name__ == '__main__':
    main()