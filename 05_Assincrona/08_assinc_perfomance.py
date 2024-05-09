import datetime  # Usado para medir o tempo de execução.
import math  # Provê acesso a funções matemáticas, como raiz quadrada.

import asyncio

def main():
    print(f"Realizando o processamento matemático de forma assíncrona")  # Exibe a quantidade de núcleos.

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()  # Marca o tempo de início da execução.

    el.run_until_complete(computar(inicio=1, fim=50_000_000))

    tempo = datetime.datetime.now() - inicio  # Calcula a duração da execução.

    print(f"Terminou em {tempo.total_seconds():.2f} segundos")  # Exibe o tempo total de execução.


async def computar(fim, inicio=1):
    pos = inicio  # Define a posição inicial para o cálculo.
    fator = 1000 * 1000  # Define um fator para o cálculo (pode ser usado para normalizar ou ajustar os valores).
    while pos <= fim:  # Enquanto a posição não alcançar o fim.
        pos += 1  # Incrementa a posição.
        math.sqrt((pos - fator) * (pos - fator))  # Calcula a raiz quadrada do quadrado da diferença entre a posição atual e o fator.


if __name__ =='__main__':
    main()

'''
Terminou em 12.18 segundos
'''