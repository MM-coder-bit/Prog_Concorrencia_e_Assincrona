# Importa o módulo multiprocessing, que fornece suporte para execução concorrente usando processos.
import multiprocessing

# Define a função 'calcular', que recebe um dado e retorna seu quadrado.
def calcular(dado):
    return dado ** 2

# Define a função 'imprimir_nome_procsso', que imprime o nome do processo atual.
def imprimir_nome_procsso():
    print(f'Nome do processo: {multiprocessing.current_process().name}')

# Define a função principal 'main', que será executada se este script for o módulo principal.
def main():
    # Obtém o número de CPUs disponíveis e define o tamanho do pool como o dobro desse número.
    tamanho_pool = multiprocessing.cpu_count() * 2

    # Imprime o tamanho do pool de processos.
    print(f'Tamanho da Pool: {tamanho_pool}')

    # Cria um pool de processos com o tamanho especificado e inicializa cada processo com a função 'imprimir_nome_procsso'.
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_procsso)

    # Cria uma lista de números de 0 a 6.
    entradas = list(range(7))

    # Usa o pool de processos para aplicar a função 'calcular' em cada elemento da lista 'entradas'.
    # O método 'map' distribui as tarefas entre os processos do pool e coleta os resultados.
    saidas = pool.map(calcular, entradas)

    # Imprime os resultados do cálculo realizado nos processos do pool.
    print(f'Saídas: {saidas}')

    # Fecha o pool de processos, impedindo que mais tarefas sejam adicionadas.
    pool.close()

    # Espera que todos os processos no pool terminem suas tarefas antes de continuar.
    pool.join()

# Verifica se este script é o ponto de entrada principal para evitar execução quando importado.
if __name__ == '__main__':
    main()
