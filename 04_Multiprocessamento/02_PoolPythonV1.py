# Importa o módulo multiprocessing que permite a criação e manipulação de processos independentes.
import multiprocessing

# Define a função 'calcular' que toma um argumento 'dado' e retorna o seu quadrado.
def calcular(dado):
    return dado ** 2

# Define a função principal que será executada se este script for o módulo principal.
def main():
    # Determina o tamanho do pool de processos como o dobro do número de CPUs disponíveis na máquina.
    tamanho_pool = multiprocessing.cpu_count() * 2

    # Exibe o tamanho do pool de processos.
    print(f'Tamanho da Pool: {tamanho_pool}')

    # Cria um pool de processos com o tamanho especificado.
    pool = multiprocessing.Pool(processes=tamanho_pool)

    # Cria uma lista de números de 0 a 6.
    entradas = list(range(7))
    
    # Utiliza o pool para aplicar a função 'calcular' a cada elemento da lista 'entradas'.
    # O método 'map' distribui os dados de 'entradas' entre os processos do pool.
    saidas = pool.map(calcular, entradas)

    # Exibe os resultados das operações de cálculo.
    print(f'Saídas: {saidas}')

    # Fecha o pool de processos, impedindo que mais tarefas sejam adicionadas.
    pool.close()
    
    # Aguarda que todos os processos do pool terminem sua execução antes de continuar.
    pool.join()

# Verifica se este script é o ponto de entrada principal para evitar execução indesejada quando importado.
if __name__ == '__main__':
    main()
