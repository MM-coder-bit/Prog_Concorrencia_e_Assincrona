# pip install fastapi uvicorn[standard]

from fastapi import FastAPI  # Importa a classe FastAPI usada para criar a aplicação web.
from pydantic import BaseModel  # Importa BaseModel de Pydantic para a criação de modelos de dados com validação automática.

# Define um modelo de dados para um produto usando Pydantic.
class Produto(BaseModel):
    id: int  # Identificador único para cada produto.
    nome: str  # Nome do produto.
    preco: float  # Preço do produto.
    em_oferta: bool = False  # Indica se o produto está em oferta, padrão é False.


app = FastAPI()  # Cria uma instância do FastAPI.

# Lista de produtos, simulando um pequeno banco de dados.
produtos = [
    Produto(id=1, nome="Playstation 5", preco=5745.55, em_oferta=True),
    Produto(id=2, nome="Nintendo Will", preco=2654.12, em_oferta=True),
    Produto(id=3, nome="Xbox 360", preco=1765.34, em_oferta=True),
    Produto(id=4, nome="Super Nintendo", preco=234.67, em_oferta=True),
    Produto(id=5, nome="Atari 2600", preco=199.90, em_oferta=True),
]

# Endpoint raiz que retorna uma mensagem simples.
@app.get("/")
async def index():
    return {'Mateus': 'Marques _'}

# Endpoint para buscar um produto por seu ID.
@app.get('/produtos/{id}')
async def buscar_produtos(id: int):
    # Itera sobre a lista de produtos.
    for produto in produtos:
        if produto.id == id:
            return produto  # Retorna o produto se encontrado.
    return None  # Retorna None se nenhum produto for encontrado com o ID especificado.

# Endpoint para atualizar um produto existente por seu ID.
@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    # Itera sobre a lista de produtos com index para possível substituição.
    for index, prod in enumerate(produtos):
        if prod.id == id:
            produtos[index] = produto  # Atualiza o produto na lista se encontrado.
            return produto  # Retorna o produto atualizado.
    return None  # Retorna None se nenhum produto for encontrado para atualizar.

# Para executar, use essa linha debaixo no terminal
# uvicorn main:app --reload