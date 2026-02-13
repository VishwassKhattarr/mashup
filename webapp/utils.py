import zipfile
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def zip_file(file_path):
    zip_name = "result.zip"
    with zipfile.ZipFile(zip_name, "w") as z:
        z.write(file_path)
    return zip_name


def send_email(receiver, file_path):

    sender = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not sender or not password:
        raise Exception("Email credentials not found in .env file")

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Mashup attached")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=file_path
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
