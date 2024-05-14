# Importa o módulo multiprocessing, que permite a criação e gerenciamento de processos independentes.
# Importa também o módulo random, apesar de não ser utilizado no código fornecido.
import multiprocessing
import random

# Define a função 'ping', que envia uma mensagem através de uma conexão de pipe.
def ping(conn):
    conn.send('Mateus')  # Envia a string 'Mateus' pelo lado da conexão fornecido.

# Define a função 'pong', que recebe uma mensagem através de uma conexão de pipe.
def pong(conn):
    msg = conn.recv()  # Aguarda e recebe uma mensagem pelo lado da conexão.
    print(f'{msg} Marques')  # Imprime a mensagem recebida seguida de 'Marques'.

# Define a função principal 'main', que será executada se este script for o módulo principal.
def main():
    # Cria um par de conexões de pipe (bi-direcional por padrão).
    conn1, conn2 = multiprocessing.Pipe(True)

    # Cria um processo 'proc1' que executa a função 'ping' com 'conn1' como argumento.
    proc1 = multiprocessing.Process(target=ping, args=(conn1, ))
    # Cria um processo 'proc2' que executa a função 'pong' com 'conn2' como argumento.
    proc2 = multiprocessing.Process(target=pong, args=(conn2, ))

    # Inicia os processos 'proc1' e 'proc2'.
    proc1.start()
    proc2.start()

    # Aguarda os processos 'proc1' e 'proc2' terminarem.
    proc1.join()
    proc2.join()

# Verifica se este script é o ponto de entrada principal para evitar execução quando importado.
if __name__=='__main__':
    main()
