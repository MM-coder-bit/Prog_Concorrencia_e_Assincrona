# Importa os módulos necessários: threading para trabalhar com threads e time para pausas.
import threading
import time

# Define a função 'processar', que é designada para ser executada por uma thread.
def processar():
    print('[', end='', flush=True)  # Inicia uma barra de progresso com '[' e garante que seja impresso imediatamente.

    for _ in range(1,11):
        print('#', end='', flush=True)  # Imprime um '#' para cada iteração, representando progresso.
        time.sleep(1)  # Pausa a execução por 1 segundo entre cada '#'.

    print(']', end='', flush=True)  # Finaliza a barra de progresso com ']' e garante que seja impresso imediatamente.

# O bloco de execução principal, que só é executado se o script for o módulo principal.
if __name__ == '__main__':
    # Cria uma instância de Thread, passando a função 'processar' como o alvo.
    ex = threading.Thread(target=processar)

    ex.start()  # Inicia a execução da thread 'ex'.
    ex.join()  # Aguarda até que a thread 'ex' termine sua execução.
