#pip install aiohttp[speedups]
#pip install beautifulsoup4
#pip freeze > 07_requirements.txt

import asyncio
import aiofiles
import aiohttp
import aiohttp.client_reqrep
import bs4

async def pegar_links():
    links = []
    async with aiofiles.open('Prog_Concorrencia_e_Assincrona\\05_Assincrona\\links.txt') as arquivo:
        async for link in arquivo:
            links.append(link.strip())

    return links

async def pegar_html(link):
    print(f'pegando o html: {link}')
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                resp.raise_for_status()
                return await resp.text()
            
    except aiohttp.ClientResponseError as e:
        print(f'Falha ao acessar {link}: {e.status}')
        return None
    except Exception as e:
        print(f'Erro ao processar {link}: {e}')
        return None
        
def pegar_titulo(html):
    if html is None:
        return "HTML não disponível ou falha ao acessar a página"

    soup = bs4.BeautifulSoup(html, 'html.parser')
    title_tag = soup.select_one('title')
    if title_tag:
        return title_tag.text.split('|')[0].strip()
    else:
        return "Título não encontrado"


async def imprimir_titulos():
    links = await pegar_links()

    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))

    for tarefa in tarefas:
        html = await tarefa

        title = pegar_titulo(html)

        print(f'Curso: {title}')

def main():
    event_loop = asyncio.get_event_loop() 
    event_loop.run_until_complete(imprimir_titulos())
    event_loop.close()

if __name__ == '__main__':
    main()
