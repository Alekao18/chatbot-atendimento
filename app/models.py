from pydantic import BaseModel

class Mensagem(BaseModel):
    id:str
    usuario:str
    conteudo:str
    status:str
    atendente:str = ''