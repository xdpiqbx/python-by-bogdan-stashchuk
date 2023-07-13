from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'John', 'date': 'tomorrow'})

my_email['from'] = 'Bill'
my_email['to'] = 'test@mail.com'
my_email['subject'] = 'Hello!'
my_email.set_content(html_content, 'html')

with open("images/img.png", 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='png', filename='img.png')

with smtplib.SMTP(host='192.168.4.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login("bill", "pass")
    smtp_server.send_message(my_email)
    print('Email was sent!')

# =======================================================================

# my_email = EmailMessage()
# my_email['from'] = 'Bill'
# my_email['to'] = 'test@mail.com'
# my_email['subject'] = 'Hello!'
# my_email.set_content('Hello! How are you')
#
# with smtplib.SMTP(host='192.168.4.1', port=2525) as smtp_server:
#     smtp_server.ehlo()
#     smtp_server.starttls()
#     smtp_server.login("bill", "pass")
#     smtp_server.send_message(my_email)
#     print('Email was sent!')

# =======================================================================

# import os
# import smtplib
# from email.mime.text import MIMEText
#
# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
#         connection.login(user=sender, password=password)
#         connection.sendmail(from_addr=sender, to_addrs=recipients, msg=msg.as_string())
#
# send_email(
#     subject="Email Subject",
#     body="This is the body of the text message\nCall me later =) 465-65-44",
#     sender=os.environ["MAIN_MAIL"],
#     recipients=[os.environ["SECONDARY_MAIL"]],
#     password=os.environ["PWD"],
# )
