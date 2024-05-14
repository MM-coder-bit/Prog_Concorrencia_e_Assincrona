# Importa o módulo multiprocessing, que fornece funcionalidades para criar e gerenciar processos.
import multiprocessing

# Define a função 'ping', que coloca uma mensagem em uma fila.
def ping(queue):
    queue.put('Mateus')  # Insere a string 'Mateus' na fila.

# Define a função 'pong', que lê uma mensagem de uma fila e imprime com um complemento.
def pong(queue):
    msg = queue.get()  # Remove e retorna um item da fila.
    print(f'{msg} Marques')  # Imprime a mensagem recebida seguida de 'Marques'.

# Define a função principal 'main', que será executada se este script for o módulo principal.
def main():
    # Cria uma instância de Queue, que é uma fila que permite comunicação entre processos.
    queue = multiprocessing.Queue()

    # Cria um processo 'proc1' que executa a função 'ping' com a fila criada como argumento.
    proc1 = multiprocessing.Process(target=ping, args=(queue, ))
    # Cria um processo 'proc2' que executa a função 'pong' com a mesma fila como argumento.
    proc2 = multiprocessing.Process(target=pong, args=(queue, ))

    # Inicia os processos 'proc1' e 'proc2'.
    proc1.start()
    proc2.start()

    # Aguarda os processos 'proc1' e 'proc2' terminarem.
    proc1.join()
    proc2.join()

# Verifica se este script é o ponto de entrada principal para evitar execução quando importado.
if __name__=='__main__':
    main()
