import datetime  # Importa o módulo para manipulação de datas e horas.
import asyncio   # Importa o módulo para programação assíncrona.


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados ...')  # Informa o início da geração de dados.
    for idx in range(1, quantidade + 1):
        item = idx * idx  # Calcula o quadrado do índice.
        await dados.put((item, datetime.datetime.now()))  # Insere o item e o momento atual na fila.
        await asyncio.sleep(0.001)  # Simula um pequeno atraso para imitar uma operação de I/O.
    print(f'{quantidade} dados gerados com sucesso...')  # Informa o sucesso na geração de dados.

async def processar_dados(quantidade: int, dados: asyncio.Queue):
    processados = 0  # Inicializa o contador de itens processados.
    while processados < quantidade:
        await dados.get()  # Remove um item da fila.
        processados += 1  # Incrementa o contador de itens processados.
        await asyncio.sleep(0.001)  # Simula um pequeno atraso para imitar o tempo de processamento.
    print(f'Foram processados {processados} itens')  # Informa a quantidade de itens processados.


async def main():
    total = 5_000  # Define o número total de dados a serem gerados.
    dados = asyncio.Queue()  # Cria uma fila assíncrona para armazenar os dados.
    print(f'Computando {total * 2:.2f} dados')  # Exibe o total de dados que serão computados.

    # Gera e processa dados de forma assíncrona.
    await gerar_dados(total, dados)  # Gera a primeira metade dos dados.
    await gerar_dados(total, dados)  # Gera a segunda metade dos dados.
    await processar_dados(total * 2, dados)  # Processa todos os dados gerados.


if __name__ =='__main__':
    event_loop = asyncio.get_event_loop()  # Obtém o loop de eventos do asyncio.
    event_loop.run_until_complete(main())  # Executa a função main até que ela seja concluída.
    event_loop.close()  # Fecha o loop de eventos após a conclusão da execução.


