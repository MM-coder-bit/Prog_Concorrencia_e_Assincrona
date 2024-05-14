# Importa o módulo multiprocessing, que é usado para criar e gerenciar processos.
import multiprocessing

# Define a função 'depositar', que incrementa o valor de 'saldo' 10.000 vezes.
def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1

# Define a função 'sacar', que decrementa o valor de 'saldo' 10.000 vezes.
def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1

# Define a função 'realizar_trasacoes' para executar as funções de depositar e sacar em processos separados.
def realizar_trasacoes(saldo):
    # Cria dois processos: um para depositar e outro para sacar.
    pc1 = multiprocessing.Process(target=depositar, args=(saldo, ))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo, ))

    # Inicia ambos os processos.
    pc1.start()
    pc2.start()

    # Aguarda a conclusão de ambos os processos.
    pc1.join()
    pc2.join()

# Bloco de execução principal.
if __name__ == '__main__':
    # Inicializa um objeto 'Value' para armazenar e gerenciar um inteiro compartilhado entre processos.
    saldo = multiprocessing.Value('i', 100)

    # Imprime o saldo inicial.
    print(f'Saldo Inicial: {saldo.value}')

    # Realiza dez séries de transações.
    for _ in range(10):
        realizar_trasacoes(saldo)
    
    # Imprime o saldo final após todas as transações.
    print(f'Saldo Final: {saldo.value}')
