import datetime  # Importa o módulo datetime para trabalhar com datas e horas.
import asyncio  # Importa o módulo asyncio para programação assíncrona.

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados ...')
    for idx in range(1, quantidade + 1):
        item = idx * idx  # Calcula o quadrado do índice.
        await dados.put((item, datetime.datetime.now()))  # Coloca o item na fila junto com o timestamp atual.
        await asyncio.sleep(0.001)  # Simula um atraso, representando um processo que leva tempo.
    print(f'{quantidade} dados gerados com sucesso...')

async def processar_dados(quantidade: int, dados: asyncio.Queue):
    processados = 0
    while processados < quantidade:
        await dados.get()  # Remove um item da fila.
        processados += 1  # Incrementa o contador de itens processados.
        await asyncio.sleep(0.001)  # Simula um atraso, representando o tempo de processamento.
    print(f'Foram processados {processados} itens')

if __name__ =='__main__':
    total = 5_000  # Define o número total de dados a serem gerados e processados.
    dados = asyncio.Queue()  # Cria uma fila assíncrona para armazenar os dados.

    event_loop = asyncio.get_event_loop()  # Obtém o loop de eventos do asyncio.

    print(f'Computando {total * 2:.2f} dados')  # Informa quantos dados serão computados no total.

    event_loop.run_until_complete(gerar_dados(total, dados))  # Gera a primeira metade dos dados.
    event_loop.run_until_complete(gerar_dados(total, dados))  # Gera a segunda metade dos dados.
    event_loop.run_until_complete(processar_dados(total * 2, dados))  # Processa todos os dados gerados.

    event_loop.close()  # Fecha o loop de eventos.
