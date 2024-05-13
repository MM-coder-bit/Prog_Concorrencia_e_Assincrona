# pip install cython

import datetime
import computa

def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos ")

if __name__ =='__main__':
    main()
'''
Terminou em 9.26 segundos - sem adição do cython no programa computa
Terminou em 0.00 segundos - com adição do cython no programa computa 
                            e código totalmente em 'C'
'''
