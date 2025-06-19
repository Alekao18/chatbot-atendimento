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
