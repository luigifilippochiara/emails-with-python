# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer
# TLS: Transport Layer Security
# SSL creates a secure connection from the beginning, while TLS encryptes it when I need it

import smtplib
import ssl
from getpass import getpass

smtp_server = 'smtp.gmail.com'
port = 465

sender = input('Input sender email: ')
password = getpass('Email password: ')
receiver = input('Input receiver email: ')

message = f"""\
From: {sender}
To: {receiver}
Subject: Hi There!

This message was sent from Python! 
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('You have successfully logged in!')
    server.sendmail(sender, receiver, message)
    print('You just sent an email.')