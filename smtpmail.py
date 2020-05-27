import smtplib
import ssl
import os

# allow the less secure app to access email
# https://myaccount.google.com/lesssecureapps
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
# set env variable for password
sender_email = "sender@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
password = "Password"
newpassword = os.getenv("userPassword")  # set env variable for password
message = """\
Subject: Hi there is the python email.

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
