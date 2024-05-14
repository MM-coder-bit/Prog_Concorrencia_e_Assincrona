#--------------------------------------------------------#
#--------------------------------------------------------#
#--------------------------------------------------------#
# Este código é para simular o erro de race conditions #
#--------------------------------------------------------#
#--------------------------------------------------------#
#--------------------------------------------------------#

import threading  # Permite a criação e gerenciamento de threads em Python.
import random  # Módulo para geração de números aleatórios.
import time  # Módulo para manipulação de tempo (pausas).

from typing import List  # Importa o tipo List para uso em type hints.

class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo  # Inicializa uma conta com saldo definido pelo usuário ou zero por padrão.

def main():
    contas = criar_contas()  # Cria uma lista de contas com saldos iniciais aleatórios.
    total = sum(conta.saldo for conta in contas)  # Calcula o saldo total de todas as contas.
    print('Iniciando transferências ...')
          
    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)) for _ in range(5)
    ]  # Cria cinco threads que executarão a função 'servicos'.

    [tarefa.start() for tarefa in tarefas]  # Inicia todas as threads.
    [tarefa.join() for tarefa in tarefas]  # Espera que todas as threads terminem.

    print('transferências completas.')
    valida_banco(contas, total)  # Valida se o saldo total após as transações é consistente.

def servicos(contas, total):
    for _ in range(10_000):
        c1, c2 = pega_duas_contas(contas)  # Seleciona duas contas diferentes aleatoriamente.
        valor = random.randint(1, 100)  # Define um valor aleatório para transferência.
        transferir(c1, c2, valor)  # Realiza a transferência.
        valida_banco(contas, total)  # Valida o saldo total a cada transação.

def criar_contas() -> List[Conta]:
    # Retorna uma lista de objetos 'Conta', cada um com um saldo inicial aleatório entre 5.000 e 10.000.
    return [
        Conta(saldo=random.randint(5_000, 10_000)) for _ in range(6)
    ]

def transferir(origem:Conta, destino:Conta, valor:int):
    if origem.saldo < valor:
        return  # Se o saldo da conta de origem for menor que o valor a transferir, cancela a operação.
    
    origem.saldo -= valor  # Deduz o valor do saldo da conta de origem.
    time.sleep(0.001)  # Simula um delay para a transferência.
    destino.saldo += valor  # Adiciona o valor ao saldo da conta de destino.

def valida_banco(contas: List[Conta], total:int):
    atual = sum(conta.saldo for conta in contas)  # Soma o saldo atual de todas as contas.

    if atual != total:
        print(f'Erro Balanço bancário inconsistente. BRL$ {atual:.2f} vs {total:.2f}', flush=True)
    else:
        print(f'Tudo certo: Balanço bancário consistente: BRL$ {total:.2f}', flush=True)

def pega_duas_contas(contas):
    c1, c2 = random.sample(contas, 2)  # Seleciona duas contas distintas aleatoriamente.
    return c1, c2

if __name__ == '__main__':
    main()
