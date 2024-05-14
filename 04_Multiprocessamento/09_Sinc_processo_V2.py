# Importa o módulo multiprocessing para criar e gerenciar processos.
import multiprocessing

# Define a função 'depositar', que incrementa o valor de 'saldo' 10.000 vezes.
def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1  # Modifica o valor de 'saldo' de forma segura, usando o bloqueio.

# Define a função 'sacar', que decrementa o valor de 'saldo' 10.000 vezes.
def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1  # Modifica o valor de 'saldo' de forma segura, usando o bloqueio.

# Define a função 'realizar_trasacoes' que inicia os processos de depósito e saque.
def realizar_trasacoes(saldo, lock):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo, lock))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo, lock))

    pc1.start()  # Inicia o processo de depósito.
    pc2.start()  # Inicia o processo de saque.

    pc1.join()  # Aguarda o processo de depósito concluir.
    pc2.join()  # Aguarda o processo de saque concluir.

# Bloco principal que é executado apenas quando o script é o módulo principal.
if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)  # Inicializa 'saldo' com valor 100.

    lock = multiprocessing.RLock()  # Cria um objeto RLock.

    print(f'Saldo Inicial: {saldo.value}')  # Imprime o saldo inicial.

    for _ in range(10):  # Realiza dez séries de transações.
        realizar_trasacoes(saldo, lock=lock)
    
    print(f'Saldo Final: {saldo.value}')  # Imprime o saldo final após todas as transações.
