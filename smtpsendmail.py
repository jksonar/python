# smtplib module send mail

import smtplib

TO = 'jaysonar8@gmail.com'
SUBJECT = 'jay MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'jaysonar092'
gmail_passwd = 'Sanju@1992'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print('email sent')
except:
    print('error sending mail')

server.quit()
