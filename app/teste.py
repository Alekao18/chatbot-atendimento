from queque import adicionar_fila, proxima_mensagem, atribuir_mensagem

# 1. Adiciona mensagem na fila
adicionar_fila("cliente1", "Quero ajuda com meu pedido.")
adicionar_fila("cliente2", "Meu produto chegou com defeito.")
adicionar_fila("cliente3", "Quero falar com um atendente.")

print("Mensagens adicionadas!")

# 2. Busca a próxima mensagem pendente
msg = proxima_mensagem()
if msg:
    print("\n Próxima mensagem pendente:")
    print(f"ID: {msg.id}")
    print(f"Usuário: {msg.usuario}")
    print(f"Conteúdo: {msg.conteudo}")
    print(f"Status: {msg.status}")
else:
    print("\n Nenhuma mensagem pendente encontrada.")

# 3. Atribui a mensagem para um atendente
if msg:
    msg_atribuida = atribuir_mensagem(msg.id, "Alex")
    print("\n Mensagem atribuída:")
    print(f"Status: {msg_atribuida.status}")
    print(f"Atendente: {msg_atribuida.atendente}")
