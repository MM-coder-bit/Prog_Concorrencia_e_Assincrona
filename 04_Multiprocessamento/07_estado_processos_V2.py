# Importa os módulos necessários: multiprocessing para gerenciamento de processos,
# time para pausas e ctypes para tipos de dados específicos.
import multiprocessing
import time
import ctypes

# Define a função 'funcao1', que opera baseada em valores compartilhados entre processos.
def funcao1(val, stat):
    # Verifica o estado compartilhado e modifica o valor e o estado com base nessa condição.
    if stat.value:
        res = val.value + 10
        stat.value = False  # Altera o valor compartilhado do estado.
    else:
        res = val.value + 20
        val.value = 200  # Modifica o valor compartilhado.
        stat.value = True

    # Imprime o resultado do cálculo da função 1.
    print(f'O resultado da função 1 é {res}')
    # Pausa a execução para permitir a visualização do efeito de alterações concorrentes.
    time.sleep(0.001) 
        
# Define a função 'funcao2', similar à 'funcao1', mas com cálculos diferentes.
def funcao2(val, stat):
    # Verifica o estado compartilhado e modifica o valor e o estado com base nessa condição.
    if stat.value:
        res = val.value + 30
        stat.value = False
    else:
        res = val.value + 40
        val.value = 400
        stat.value = True

    # Imprime o resultado do cálculo da função 2.
    print(f'O resultado da função 2 é {res}')
    # Pausa a execução para permitir a visualização do efeito de alterações concorrentes.
    time.sleep(0.001) 

# Define a função principal 'main' para iniciar os processos.
def main():
    # Cria um valor compartilhado 'valor' que será acessado e modificado por múltiplos processos.
    valor = multiprocessing.Value('i', 100)
    # Cria um estado compartilhado 'status', utilizando ctypes para definir o tipo booleano.
    status = multiprocessing.Value(ctypes.c_bool, False)

    # Inicia os processos, passando os valores compartilhados como argumentos.
    p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, status))

    p1.start()
    p2.start()

    # Espera que ambos os processos terminem.
    p1.join()
    p2.join()

# Verifica se o script é executado como módulo principal e inicia a função 'main'.
if __name__ == "__main__":
    main()
