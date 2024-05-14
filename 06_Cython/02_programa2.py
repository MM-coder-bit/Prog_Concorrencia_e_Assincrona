# pip install cython

import datetime  # Importa o módulo datetime para acessar funções de data e hora.
import computa   # Importa o módulo computa, que presumimos ser um módulo Cython com funções otimizadas.


def main():
    inicio = datetime.datetime.now()  # Registra o momento de início da execução.

    computa.computar(fim=50_000_000)  # Chama a função 'computar' do módulo computa com um argumento.

    tempo = datetime.datetime.now() - inicio  # Calcula a duração da execução subtraindo o tempo de início do tempo atual.

    print(f"Terminou em {tempo.total_seconds():.2f} segundos ")  # Imprime a duração da execução em segundos.


if __name__ =='__main__':
    main()  # Executa a função main se o script for o programa principal.

'''
Terminou em 9.26 segundos - sem adição do cython no programa computa
Terminou em 0.00 segundos - com adição do cython no programa computa 
                            e código totalmente em 'C'
'''
