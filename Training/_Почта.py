import smtplib
from email.message import EmailMessage


password = 'jlyomtxyajhmaelh'
# password = "pcdkowshbyvcxfjh"
sander_email = 'denis9128@yandex.ru'
recipient_email = 'denis_minakov@mail.ru'
subject = 'Проверка связи'
body = 'Текст проверочного сообщения.'

mcg = EmailMessage()
mcg.set_content(body)
mcg['Subject'] = subject
mcg['From'] = sander_email
mcg['To'] = recipient_email

server = None
try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sander_email, password)
    server.send_message(mcg)
    print('Письмо отправлено.')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    if server:
        server.quit()


