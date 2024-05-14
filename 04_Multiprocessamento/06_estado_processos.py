# Importa os módulos necessários para o script.
import multiprocessing
import time

# Define a função 'funcao1', que modifica e imprime um valor dependendo de uma condição de status.
def funcao1(val, stat):
    if stat:
        res = val + 10
        stat = False  # Esta tentativa de alterar 'stat' é local e não afeta a variável fora desta função.
    else:
        res = val + 20
        val = 200  # Alteração local de 'val', não afeta a variável fora da função.
        stat = True  # Esta alteração é local.

    # Imprime o resultado calculado pela função.
    print(f'O resultado da função 1 é {res}')
    # Pausa a execução por um milissegundo, permitindo trocas de contexto entre processos.
    time.sleep(0.001) 
        
# Define a função 'funcao2', semelhante à 'funcao1', mas com cálculos de resultado diferentes.
def funcao2(val, stat):
    if stat:
        res = val + 20
        stat = False
    else:
        res = val + 40
        val = 400
        stat = True

    # Imprime o resultado calculado pela função.
    print(f'O resultado da função 2 é {res}')
    # Pausa similar para permitir trocas de contexto.
    time.sleep(0.001) 

# Define a função principal 'main' para iniciar os processos.
def main():
    valor = 100  # Valor inicial para ambos os processos.
    status = False  # Estado inicial para ambos os processos.

    # Cria dois processos, cada um executando uma das funções definidas com argumentos iniciais.
    p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, status))

    # Inicia os processos.
    p1.start()
    p2.start()

    # Aguarda os processos terminarem.
    p1.join()
    p2.join()

# Verifica se o script é executado como o módulo principal e chama a função 'main'.
if __name__ == "__main__":
    main()
