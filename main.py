"""
Fast API é um framework web moderno de alta performace
para criacao de api e websites, baseado em type hints e assincronia
é o mais rápido dos frameworks python.

Equivalente a NodeJs e GO

Instalação: pip install fastapi uvicorn[standard]

execucao: uvicorn (servidor) nome_arquivo:nomedaaplicacao --reload
exemplo: uvicorn main:app --reload

além disso, ele cria documentacao automaticamente
em /docs
ou /redocs

"""
from pydantic import BaseModel  # faz validacao de dados
from fastapi import FastAPI


class Produto(BaseModel):
    """Com esse modelo, faz a validação e nao aceita tipos diferente no get à Api"""
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()
softwares = [
    Produto(id=1, nome="PythonScript", preco=500.35, em_oferta=True),
    Produto(id=2, nome="GoScript", preco=510.35, em_oferta=True),
    Produto(id=3, nome="JavaScript", preco=100.35),
    Produto(id=4, nome="C++Script", preco=320.35, em_oferta=True),
]


# método get, ao acessar a raíz, têm-se o retorno abaixo
@app.get('/')  # rota para aplicação
async def index():
    return {"PyMarcusSoftwares": "https://github.com/PyMarcus"}


@app.get('/softwares/{id}')
async def ver_softwares(id: int):
    for software in softwares:
        if software.id == id:
            return software
    return None


# retorna ao navegador um objeto python direto

# rota para serialização -> recebimento de dados
@app.put('/softwares/{id}')
async def update_softwares(id: int, product: Produto):
    for software in softwares:
        if product.id == id:
            software = product
            return software
    return None
