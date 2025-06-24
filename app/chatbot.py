from fastapi import FastAPI
from pydantic import BaseModel
from app.queque import adicionar_fila, proxima_mensagem, atribuir_mensagem

app = FastAPI()
app.router

class Entrada(BaseModel):
    usuario : str
    conteudo: str
class Atendente(BaseModel):
    msg_id: str
    atendente: str

@app.post("/mensagem")
def nova_mensagem(dados: Entrada):
    adicionar_fila(dados.usuario, dados.conteudo)
    return {"status": "Mensagem recebida!"}

@app.get("/fila")
def ver_fila():
    msg = proxima_mensagem()
    if msg:
        return msg
    return {"status": "Fila vazia"}

@app.post("/atender")
def atender(dados: Atendente):
    msg = atribuir_mensagem(dados.msg_id, dados.atendente)
    if msg:
        return msg
    return {"status": "Mensagem não recebida!"}
