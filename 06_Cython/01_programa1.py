# pip install cython

import cumprimenta # Módulo cython compilado

def main():
    nome: str = input("Qual seu nome? ")  # Solicita ao usuário que insira seu nome.
    cumprimenta.cumprimentar(nome)  # Chama a função 'cumprimentar' do módulo 'cumprimenta', passando o nome como argumento.

if __name__ == "__main__":
    main()  # Executa a função main() se o script for o programa principal.
