import time
import colorama  # Importa a biblioteca colorama para habilitar a impressão de texto colorido no terminal.

from threading import Thread  # Importa Thread da biblioteca threading para permitir a execução de tarefas em paralelo.
from queue import Queue  # Importa Queue para criar uma fila que será usada para comunicação entre threads.

def gerador_de_dados(queue):
    for i in range(1,11):  # Loop para gerar dados de 1 a 10.
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush=True)  # Imprime a mensagem de dado gerado em verde.
        time.sleep(2)  # Pausa a execução por 2 segundos para simular o tempo de geração de dados.
        queue.put(i)  # Coloca o dado gerado na fila.

def consumidor_de_dados(queue):
    while queue.qsize() > 0:  # Executa enquanto houver dados na fila.
        valor = queue.get()  # Pega o próximo dado da fila.
        print(colorama.Fore.RED + f'Dados {valor * 2} foi consumido.', flush=True)  # Imprime a mensagem de dado consumido em vermelho, dobrando o valor.
        time.sleep(1)  # Pausa a execução por 1 segundo para simular o processamento do dado.
        queue.task_done()  # Marca o item como processado na fila.

if __name__ == '__main__':
    print(colorama.Fore.BLUE + 'Sistema iniciado', flush=True)  # Imprime que o sistema foi iniciado em azul.
    queue = Queue()  # Cria uma fila para armazenar os dados.
    th1 = Thread(target=gerador_de_dados, args=(queue,))  # Cria a thread do produtor que gera os dados.
    th2 = Thread(target=consumidor_de_dados, args=(queue,))  # Cria a thread do consumidor que processa os dados.

    th1.start()  # Inicia a thread do produtor.
    th1.join()  # Espera a thread do produtor terminar.

    th2.start()  # Inicia a thread do consumidor.
    th2.join()  # Espera a thread do consumidor terminar.
