# Importando as bibliotecas necessárias para a programação assíncrona
import asyncio
import aiofiles

# Função assíncrona para ler todo o conteúdo de um arquivo de texto e imprimir na tela.
async def exe_arq():
    # Abre o arquivo texto.txt de forma assíncrona para leitura
    async with aiofiles.open('Prog_Concorrencia_e_Assincrona\\05_Assincrona\\texto.txt') as arquivo:
        conteudo = await arquivo.read()  # Lê todo o conteúdo do arquivo de forma assíncrona
    print(conteudo)  # Imprime o conteúdo do arquivo

# Função assíncrona para ler um arquivo de texto linha por linha e imprimir cada linha.
async def exe_arq2():
    # Abre o arquivo texto.txt de forma assíncrona para leitura
    async with aiofiles.open('Prog_Concorrencia_e_Assincrona\\05_Assincrona\\texto.txt') as arquivo:
        async for linha in arquivo:  # Itera sobre cada linha do arquivo de forma assíncrona
            print(linha)  # Imprime cada linha

# Função principal que configura e executa o loop de eventos
def main():
    event_loop = asyncio.get_event_loop()  # Obtém o loop de eventos atual

    event_loop.run_until_complete(exe_arq2())  # Executa a função exe_arq2 até que esteja completa

    event_loop.close()  # Fecha o loop de eventos para liberar recursos

# Ponto de entrada do script Python, garantindo que o módulo main seja executado apenas se o script for o principal executado
if __name__ == '__main__':
    main()
