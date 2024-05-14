# Importa o módulo time para realizar pausas.
import time

# Importa ThreadPoolExecutor; descomente a outra linha para usar ProcessPoolExecutor.
from concurrent.futures.thread import ThreadPoolExecutor as Executor
# from concurrent.futures.process import ProcessPoolExecutor as Executor

# Define a função 'processar', que simula uma barra de progresso e retorna um valor.
def processar():
    print('[', end='', flush=True)  # Inicia a barra de progresso.
    for _ in range(1,11):
        print('#', end='', flush=True)  # Imprime '#' para cada iteração, representando progresso.
        time.sleep(1)  # Pausa de 1 segundo para simular trabalho sendo feito.
    print(']', end='', flush=True)  # Finaliza a barra de progresso.

    return 1  # Retorna 1 após concluir a barra de progresso.

# Bloco principal que só é executado se o script for o módulo principal.
if __name__ == '__main__':
   # Cria uma instância do Executor. Pode ser um ThreadPoolExecutor ou ProcessPoolExecutor.
   with Executor() as executor:
       future = executor.submit(processar)  # Submete a função 'processar' para execução.
    
   # Imprime o resultado retornado pela função 'processar' após sua conclusão.
   print(f'\nO retorno foi: {future.result()}')
