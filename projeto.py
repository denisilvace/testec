import smtplib
import os 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import locale

def send_email(subject, body,to_email,pdf_path):
    from_email = "jigouveia@sfiec.org.br"
    from_password = "tmoi ejpx hpof bich"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body,'plain'))

    attachment = open(pdf_path,'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',f'attachment;filename={os.path.basename(pdf_path)}')
    msg.attach(part)

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.login(from_email,from_password)
    server.send_message(msg)
    server.quit()

emails_and_pdfs = [
    {'email': 'jigouveia@sfiec.org.br','pdf': 'Z:/_FATURAMENTO/FATURAMENTO CORPORATIVO/24. LOCAÇÃO/FIEC/2024/11. NOVEMBRO/PDF/RPS 17107 - SIMAGRAN/RPS 17107 BOLETO'},
    {'email': 'ivanilsonsilva064@gmail.com','pdf': 'Z:/_FATURAMENTO/FATURAMENTO CORPORATIVO/24. LOCAÇÃO/FIEC/2024/11. NOVEMBRO/PDF/RPS 17108 - SIMEC.pdf/RPS 17108 BOLETO.pdf'},
]
try:
    locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME,'portuguese_brazil.1252')
agora = datetime.now()
dataformatada = agora.strftime("%B/%Y")
subject = 'Fatura/Locação Salas Sindicatos'
body = f'''Prezado(a) cliente,
seguem anexos boleto e fatura referentes ao serviço de Locação de Imóvel, do mês de Novembro/2024,
Informações complementares com relação a fatura, por gentileza, manter contato com a equipe do faturamento FIEC - Gefin(Cleane Lima ou Ivanilson Silva - 3421-5894).

Solicitação de prorrogação entrar em contato com o setor de Cobrança da Gerência Financeira na FIEC, através dos telefones: 3421-5890 - falar com Sheiliania
através do e-mail: gefin.cobranca@sfiec.org.br.

Por gentileza, confirmar o recebimento e encaminhar ao responsável financeiro. 

Atenciosamente,
Ivanilson Silva

'''

for item in emails_and_pdfs:
     subject = f"Boleto e Fatura de Locação" 
     send_email(subject,body,item['email'],item['pdf'])
     print(f"Email enviado para {item['email']} com o anexo {item['pdf']} e assunto: {subject}")