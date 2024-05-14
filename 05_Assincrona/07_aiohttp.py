#pip install aiohttp[speedups]
#pip install beautifulsoup4
#pip freeze > 07_requirements.txt

import datetime  # Usado para registrar o momento exato da geração de cada dado.
import asyncio   # Usado para programação assíncrona, facilitando operações I/O sem bloqueio.
import aiofiles  # Facilita leitura e escrita de arquivos de forma assíncrona.
import aiohttp   # Biblioteca para realizar requisições HTTP de forma assíncrona.
import bs4       # BeautifulSoup, utilizado para parsing de documentos HTML.

async def pegar_links():
    """
    Lê de forma assíncrona um arquivo de texto contendo URLs, uma por linha,
    e retorna uma lista desses URLs.
    """
    links = []  # Lista para armazenar os URLs.
    # Abre o arquivo de forma assíncrona usando aiofiles.
    async with aiofiles.open('Prog_Concorrencia_e_Assincrona\\05_Assincrona\\links.txt') as arquivo:
        # Itera sobre cada linha do arquivo de forma assíncrona.
        async for link in arquivo:
            # Remove espaços em branco e quebras de linha de cada URL e adiciona à lista.
            links.append(link.strip())
    return links  # Retorna a lista de links.


async def pegar_html(link):
    """
    Faz uma requisição HTTP assíncrona para o URL fornecido e retorna o conteúdo HTML da página.
    Caso ocorra um erro na requisição, retorna None.
    """
    print(f'pegando o html: {link}')  # Exibe qual URL está sendo processado.
    try:
        # Inicia uma sessão HTTP assíncrona.
        async with aiohttp.ClientSession() as session:
            # Faz uma requisição GET para o URL.
            async with session.get(link) as resp:
                resp.raise_for_status()  # Verifica se a requisição foi bem-sucedida.
                return await resp.text()  # Retorna o conteúdo da página em texto.
    except aiohttp.ClientResponseError as e:
        # Trata erros específicos de resposta HTTP, como 404 ou 500.
        print(f'Falha ao acessar {link}: {e.status}')
        return None
    except Exception as e:
        # Trata outros tipos de erros não relacionados diretamente à resposta HTTP.
        print(f'Erro ao processar {link}: {e}')
        return None

        
def pegar_titulo(html):
    """
    Analisa o HTML e extrai o título da página. Retorna uma mensagem apropriada se o título não for encontrado
    ou se o HTML não estiver disponível.
    """
    if html is None:
        return "HTML não disponível ou falha ao acessar a página"
    # Utiliza BeautifulSoup para fazer o parsing do HTML.
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # Seleciona a tag <title> do HTML.
    title_tag = soup.select_one('title')
    if title_tag:
        # Extrai o texto da tag <title> e limpa caracteres desnecessários.
        return title_tag.text.split('|')[0].strip()
    else:
        # Retorna mensagem caso não encontre a tag <title>.
        return "Título não encontrado"



async def imprimir_titulos():
    """
    Coordena a obtenção de links, o carregamento das páginas HTML e a extração e impressão dos títulos.
    """
    links = await pegar_links()  # Obtém a lista de URLs.
    tarefas = []
    # Cria uma tarefa assíncrona para cada URL para baixar o HTML.
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))
    # Aguarda cada tarefa ser completada e extrai o título do HTML resultante.
    for tarefa in tarefas:
        html = await tarefa
        title = pegar_titulo(html)
        # Imprime o título de cada curso.
        print(f'Curso: {title}')


def main():
    """
    Configura o loop de eventos do asyncio e executa a função imprimir_titulos.
    """
    event_loop = asyncio.get_event_loop()  # Obtém o loop de eventos do asyncio.
    event_loop.run_until_complete(imprimir_titulos())  # Executa imprimir_titulos até a conclusão.
    event_loop.close()  # Fecha o loop de eventos após a conclusão.

if __name__ == '__main__':
    main()  # Executa a função main se o script for o módulo principal.

