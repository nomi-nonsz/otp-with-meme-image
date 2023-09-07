import os
import random
import ssl
import smtplib

from PIL import Image, ImageDraw, ImageFont

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

mail_sender = "norman25.projects2@gmail.com"
mail_password = os.environ.get("EMAIL_PASSWORD_2")
mail_receiver = "norman25.na@gmail.com"

def add_textimg(text):
    img = Image.open("images/main/black-suit.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/impact.ttf", 64)
    text_pos_center = (img.width - draw.textlength(text, font)) // 2
    pos = (text_pos_center, 720)
    text_color = (255, 255, 255)
    draw.text(pos, text, fill=text_color, font=font)
    
    img.save("images/output/pos.png")
    img.close()


def send_email():
    try:
        randis = random.randint(1000, 9999)

        # message variable
        subject = "confirm your account"
        msg = "Here's your email confirmation"

        zmail = MIMEMultipart()
        zmail['From'] = mail_sender
        zmail['To'] = mail_receiver
        zmail['Subject'] = subject

        # attach text
        zmail.attach(MIMEText(msg, 'plain'))

        # attach picure
        add_textimg("Your otp code is " + str(randis))
        pict = open("images/output/pos.png", "rb").read()
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