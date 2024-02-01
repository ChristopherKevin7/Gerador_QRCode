import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import qrcode

class GeradorQREmail:

    def gerar_qr_code(self, dados, nome):
        # Lógica para gerar o QR code usando a biblioteca qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(dados)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.show()
        img.save(nome + ".png")
        return nome + ".png"

    def enviar_email(self, destinatario, assunto, corpo, anexo):
        # Lógica para enviar o e-mail usando a biblioteca smtplib
        # Detalhes de configuração do servidor de e-mail 
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email = 'christopherkevin78@gmail.com'
        senha = 'snud pjtu jmlp uuhp'
        mensagem = MIMEMultipart()
        mensagem['From'] = email
        mensagem['To'] = destinatario
        mensagem['Subject'] = assunto
        mensagem.attach(MIMEText(corpo, 'html'))
        with open(anexo, 'rb') as qr_file:
            qr_attachment = MIMEImage(qr_file.read())
            qr_attachment.add_header('Content-Disposition', f'attachment; filename={anexo}')
            mensagem.attach(qr_attachment)

        try:
            servidor = smtplib.SMTP(smtp_server, smtp_port)
            servidor.starttls()
            servidor.login(email, senha)
            servidor.sendmail(email, destinatario, mensagem.as_string())
            
            print('Email Enviado')

        except Exception as e:
            print('Erro ao enviar o email: ', str(e))
            
        finally:
            servidor.quit()

    def gerar_email(self, dados, dados_email, assunto):
        data = dados
        nome = assunto
        qr_code_path = self.gerar_qr_code(data, nome)

        destinatario = dados_email
        assunto = assunto
        corpo = f'''
            <p>Segue anexo do QRCode</p>
            
        '''

        self.enviar_email(destinatario, assunto, corpo, qr_code_path)