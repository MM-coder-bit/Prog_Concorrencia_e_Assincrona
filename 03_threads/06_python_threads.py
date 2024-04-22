import datetime  # Usado para medir o tempo de execução.
import math  # Provê acesso a funções matemáticas, como raiz quadrada.

import threading  # Permite o uso de threads para executar tarefas em paralelo.
import multiprocessing  # Usado para acessar informações sobre o processamento do sistema, como a contagem de núcleos.


def main():
    qtd_cores = multiprocessing.cpu_count()  # Determina quantos núcleos de CPU estão disponíveis.
    print(f"Quantidade de cores: {qtd_cores}")  # Exibe a quantidade de núcleos.

    inicio = datetime.datetime.now()  # Marca o tempo de início da execução.

    threads = []  # Lista para armazenar as threads que serão criadas.
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n-1) / qtd_cores  # Calcula o ponto inicial para cada thread.
        fim = 50_000_000 * n / qtd_cores  # Calcula o ponto final para cada thread.
        
        print(f'Core {n} processando de {ini} até {fim}')  # Informa o intervalo de processamento de cada núcleo.

        # Cria uma thread para processar o intervalo calculado.
        threads.append(
            threading.Thread(
                target=computar, 
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True
            )
        )

    [t.start() for t in threads]  # Inicia todas as threads.
    [t.join() for t in threads]  # Aguarda o término de todas as threads.

    tempo = datetime.datetime.now() - inicio  # Calcula a duração da execução.

    print(f"Terminou em {tempo.total_seconds():.2f} segundos")  # Exibe o tempo total de execução.


def computar(fim, inicio=1):
    pos = inicio  # Define a posição inicial para o cálculo.
    fator = 1000 * 1000  # Define um fator para o cálculo (pode ser usado para normalizar ou ajustar os valores).
    while pos <= fim:  # Enquanto a posição não alcançar o fim.
        pos += 1  # Incrementa a posição.
        math.sqrt((pos - fator) * (pos - fator))  # Calcula a raiz quadrada do quadrado da diferença entre a posição atual e o fator.


if __name__ =='__main__':
    main()

'''
Terminou em 7.37 segundos
'''