# Importa o módulo multiprocessing, que permite a criação de processos
import multiprocessing

# Imprime o nome do processo atual, que por padrão é 'MainProcess'
print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')

# Define a função faz_algo, que recebe um valor e imprime uma mensagem com esse valor
def faz_algo(valor):
    print(f'Fazendo algo com o {valor}')

# Define a função main, que será o ponto de entrada do programa
def main():
    # Cria um objeto Process que irá rodar a função faz_algo com o argumento 'Passaro'
    # e define o nome do processo como 'Processo Marques'
    pc = multiprocessing.Process(target=faz_algo, args=('Passaro',), name='Processo Marques')

    # Imprime o nome do processo que foi criado, neste caso 'Processo Marques'
    print(f'Iniciando o processo com nome: {pc.name}')

    # Inicia o processo
    pc.start()

    # Aguarda o processo terminar
    pc.join()

# Verifica se este script é o ponto de entrada principal para evitar que o código seja executado
# ao importar este script como um módulo em outro lugar
if __name__ == '__main__':
    main()
