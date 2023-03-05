from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

class Cliente(BaseModel):
    id: int
    data_cadastro: str
    nome: str
    email: str
    telefone: str
    vip: str
    data_nascimento: str

    
    
db_clientes =[
    Cliente(id=1, data_cadastro="2021/02/19'", nome="Jonas", email="jonas@uol.com.br", telefone=18-981123456, vip="não", data_nascimento="1980/01/15"),
    Cliente(id=2, data_cadastro="2020/12/21", nome="Alice", email="aline@gmail.com.br", telefone=18-981895742, vip="não", data_nascimento="1986/03/10"),
    Cliente(id=3, data_cadastro="2022/10/02", nome="Maria", email="maria@terra.com.br", telefone=18-981458963, vip="sim", data_nascimento="1999/06/25"),
    Cliente(id=4, data_cadastro="2022/06/22", nome="Helena", email="helena@uol.com.br", telefone=18-981365421, vip="sim", data_nascimento="1996/09/03"),
    Cliente(id=5, data_cadastro="2019/09/12", nome="Bento", email="bento@bol.com.br", telefone=18-981159487, vip="sim", data_nascimento="1978/12/12"),
]

@app.get("/")
def home():
    return {"Mensagem": "Estacionamento Vagalivre"}

@app.get("/clientes/")
def exibir_cliente():
    return {"cliente": db_clientes}

@app.get("/clientes/{id}")
def mostrar_cliente(id: int):
    return {"cliente": [cliente for cliente in db_clientes if cliente.id==id]}
    

@app.post("/clientes")
def cad_cliente(cliente: Cliente):
    cliente.id = db_clientes[-1].id +1
    db_clientes.append(cliente)
    return {"mensagem": "Cliente Cadastrado com Sucesso"}
    

@app.patch("/clientes/{id}")
def atualizar_cliente(id: int, cliente: Cliente):
    index = [index for index, cliente in enumerate(db_clientes) if cliente.id == id]
    cliente.id = db_clientes[index[0]].id
    db_clientes[index[0]] = cliente
    return {"mensagem": "Cliente Atualizado"}
    

@app.delete("/clientes/{id}")
def apagar_cliente():
    ...