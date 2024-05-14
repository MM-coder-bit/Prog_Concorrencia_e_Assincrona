import datetime  # Usado para registrar o momento exato da geração de cada dado.
import asyncio   # Usado para programação assíncrona.

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')
    for idx in range(1, quantidade + 1):
        item = idx * idx  # Calcula o quadrado do índice.
        await dados.put((item, datetime.datetime.now()))  # Insere o item e o momento atual na fila.
        await asyncio.sleep(0.001)  # Pausa artificial para simular atraso na geração de dados.
    print(f'{quantidade} dados gerados com sucesso...')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    processados = 0
    while processados < quantidade:
        await dados.get()  # Remove e consome um item da fila.
        processados += 1  # Contador de itens processados.
        await asyncio.sleep(0.001)  # Pausa artificial para simular atraso no processamento de dados.
    print(f'Foram processados {processados} itens')

async def main():
    total = 5_000  # Total de itens a serem gerados e processados.
    dados = asyncio.Queue()  # Fila assíncrona para armazenar dados.
    print(f'Computando {total * 2:.2f} dados')

    # Criação de tarefas assíncronas para geração e processamento de dados.
    tarefa_1 = asyncio.create_task(gerar_dados(total, dados))
    tarefa_2 = asyncio.create_task(gerar_dados(total, dados))
    tarefa_3 = asyncio.create_task(processar_dados(total * 2, dados))

    await asyncio.gather(tarefa_1, tarefa_2, tarefa_3)  # Aguarda a conclusão de todas as tarefas.

if __name__ == '__main__':
    asyncio.run(main())  # Executa a função main usando a função run do asyncio.

