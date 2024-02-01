#Importando bibliotecas
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from backend import GeradorQREmail

co1 = "#333333"  # preta pesado / dark black
co2 = "#D3D3D3"  # cinza / gray


class Interface_app:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QRCode")
        self.root.geometry('600x400')
        self.root.configure(bg=co2)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=1)
        
        titulo = Label(root, text= "Gerar QRCode", font=('Ivy 40 bold'), bg= co2, fg= co1)
        titulo.grid(row= 0,column= 2)
        
        form_1 = Label(root, text="Insira o texto ou link:", font=('Ivy 12 bold'), bg= co2, fg= co1)
        form_1.grid(row= 1, column= 2)
        
        self.form_1_inserir = tk.Entry(root, width= 50)
        self.form_1_inserir.grid(row= 2, column= 2)
        
        form_email = Label(root, text="Insira o email do destinatario:", font=('Ivy 12 bold'), bg= co2, fg= co1)
        form_email.grid(row= 3, column= 2)
        
        self.form_email_inserir = tk.Entry(root, width= 50)
        self.form_email_inserir.grid(row= 4, column= 2)
        
        form_nome = Label(root, text="Insira o nome do QRCode:", font=('Ivy 12 bold'), bg= co2, fg= co1)
        form_nome.grid(row= 5, column= 2)
        
        self.form_nome_inserir = tk.Entry(root, width= 50)
        self.form_nome_inserir.grid(row= 6, column= 2)
        
        btn_gerar_qrcode = tk.Button(root, text="Baixar QRCode", command=self.baixar_qrcode)
        btn_gerar_qrcode.grid(row=7, column=1)
        
        btn_gerar_email = tk.Button(root, text="Enviar email", command= self.enviar_email)
        btn_gerar_email.grid(row=7, column= 3)
        
    def baixar_qrcode(self):
        # Lógica para chamar o backend e gerar o qrcode
        dados = self.form_1_inserir.get()
        nome = self.form_nome_inserir.get()
        gerador_qr = GeradorQREmail()
        gerador_qr.gerar_qr_code(dados, nome)      
        
    def enviar_email(self):
        #chamando o backend para enviar o email com o qrcode
        dados = self.form_1_inserir.get()
        dados_email = self.form_email_inserir.get()
        nome_qr = self.form_nome_inserir.get()
        enviar_qrcode = GeradorQREmail()
        if not dados_email:
            # Exibir mensagem de aviso se o campo do destinatário estiver vazio
            messagebox.showwarning("Aviso", "Por favor, insira o endereço de e-mail do destinatário.")
        elif not nome_qr:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do Qrcode.")
        else:
            enviar_qrcode.gerar_email(dados, dados_email, nome_qr)
            messagebox.showinfo("mensagem", "Email enviado, caso o destinatario não tenha recebido, verifique se o email foi digitado corretamente.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Interface_app(root)
    root.mainloop()
        
