import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://localhost:8000"  # ou o IP da máquina que roda a API

class AtendimentoApp:
    def __init__(self, master):
        self.master = master
        master.title("App de Atendimento")

        self.usuario_label = tk.Label(master, text="Usuário:")
        self.usuario_label.pack()

        self.usuario_text = tk.StringVar()
        self.usuario_entry = tk.Entry(master, textvariable=self.usuario_text, state='readonly', width=50)
        self.usuario_entry.pack()

        self.mensagem_label = tk.Label(master, text="Mensagem:")
        self.mensagem_label.pack()

        self.mensagem_text = tk.Text(master, height=5, width=50, state='disabled')
        self.mensagem_text.pack()

        self.resposta_label = tk.Label(master, text="Sua resposta:")
        self.resposta_label.pack()

        self.resposta_entry = tk.Text(master, height=4, width=50)
        self.resposta_entry.pack()

        self.buscar_btn = tk.Button(master, text="Buscar próxima mensagem", command=self.buscar_mensagem)
        self.buscar_btn.pack(pady=5)

        self.responder_btn = tk.Button(master, text="Responder", command=self.responder)
        self.responder_btn.pack(pady=5)

        self.msg_id = None

    def buscar_mensagem(self):
        try:
            response = requests.get(f"{API_URL}/fila")
            data = response.json()
            if 'usuario' in data:
                self.msg_id = data['id']
                self.usuario_text.set(data['usuario'])

                self.mensagem_text.configure(state='normal')
                self.mensagem_text.delete("1.0", tk.END)
                self.mensagem_text.insert(tk.END, data['conteudo'])
                self.mensagem_text.configure(state='disabled')
            else:
                messagebox.showinfo("Fila", "Nenhuma mensagem na fila.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def responder(self):
        if not self.msg_id:
            messagebox.showwarning("Aviso", "Nenhuma mensagem selecionada.")
            return

        resposta = self.resposta_entry.get("1.0", tk.END).strip()
        if not resposta:
            messagebox.showwarning("Aviso", "Digite uma resposta.")
            return

        try:
            payload = {
                "msg_id": self.msg_id,
                "atendente": resposta
            }
            response = requests.post(f"{API_URL}/atender", json=payload)
            data = response.json()
            messagebox.showinfo("Resposta enviada", str(data))
            self.resposta_entry.delete("1.0", tk.END)
            self.usuario_text.set("")
            self.msg_id = None

            self.mensagem_text.configure(state='normal')
            self.mensagem_text.delete("1.0", tk.END)
            self.mensagem_text.configure(state='disabled')

        except Exception as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AtendimentoApp(root)
    root.mainloop()