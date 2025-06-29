from app.models import Mensagem
from app.datbase import r
import json
import uuid

QUEUE_ID = 'Fila_Atendimento'

def adicionar_fila(usuario: str, conteudo: str):
    msg = Mensagem(
        id=str(uuid.uuid4()), 
        usuario = usuario, 
        conteudo = conteudo, 
        status = "pendente"
    )
    r.rpush(QUEUE_ID, msg.model_dump_json())

def proxima_mensagem():
    for i in range(r.llen(QUEUE_ID)):
        linha = r.lindex(QUEUE_ID, i)
        msg_1 = Mensagem.model_validate_json(linha)
        if msg_1.status == "pendente":
            return msg_1
    return None

def atribuir_mensagem(msg_id: str, atendente: str):
    for i in range(r.llen(QUEUE_ID)):
        linha = r.lindex(QUEUE_ID, i)
        msg_2 = Mensagem.model_validate_json(linha)
        if msg_2.id == msg_id:
            msg_2.status = "sendo atendido por {atendente}"
            msg_2.atendente = atendente
            r.lset(QUEUE_ID, i, msg_2.model_dump_json())
            return msg_2
    return None