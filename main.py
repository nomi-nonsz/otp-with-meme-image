import os
import random
import ssl
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

mail_sender = "norman25.projects2@gmail.com"
mail_password = os.environ.get("EMAIL_PASSWORD_2")
mail_receiver = "norman25.na@gmail.com"

def send_email():
    try:
        randis = random.randint(1000, 9999)

        # message variable
        subject = "confirm your account"
        msg = "your OTP code is"

        zmail = MIMEMultipart()
        zmail['From'] = mail_sender
        zmail['To'] = mail_receiver
        zmail['Subject'] = subject

        # attach text
        zmail.attach(MIMEText(msg, 'plain'))

        # attach picure
        pict = open('images/main/black-suit.png', 'rb').read();
        zmail.attach(MIMEImage(pict, name="black man suit"))

        # creating context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(mail_sender, mail_password)
            smtp.sendmail(mail_sender, mail_receiver, zmail.as_string())
    except Exception as e:
        print("Failed to send a email")
        print(str(e))

send_email()