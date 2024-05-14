# Importa os módulos necessários: multiprocessing para trabalhar com processos e time para pausas.
import multiprocessing
import time

# Define a função 'processar', que é designada para ser executada por um processo.
def processar():
    print('[', end='', flush=True)  # Inicia uma barra de progresso com '[' e garante que seja impresso imediatamente.

    for _ in range(1,11):
        print('#', end='', flush=True)  # Imprime um '#' para cada iteração, representando progresso.
        time.sleep(1)  # Pausa a execução por 1 segundo entre cada '#'.

    print(']', end='', flush=True)  # Finaliza a barra de progresso com ']' e garante que seja impresso imediatamente.

# O bloco de execução principal, que só é executado se o script for o módulo principal.
if __name__ == '__main__':
    # Cria uma instância de Process, passando a função 'processar' como o alvo.
    ex = multiprocessing.Process(target=processar)

    ex.start()  # Inicia a execução do processo 'ex'.
    ex.join()  # Aguarda até que o processo 'ex' termine sua execução.
