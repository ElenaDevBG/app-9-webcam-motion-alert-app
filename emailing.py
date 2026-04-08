import smtplib
import os
import filetype
from email.message import EmailMessage
from dotenv import load_dotenv


def send_email(image_path):
    load_dotenv()

    print("Send email STARTED")

    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("MAIL_USER")
    password = os.getenv("MAIL_PASSWORD")
    receiver = os.getenv("MAIL_USER")

    email_message = EmailMessage()
    email_message['Subject'] = "Webcam: Motion Detected"
    email_message.set_content("Hey, we just noticed somebody moving!")

    with open(image_path, "rb") as file:
        content = file.read()

    image_type = filetype.guess(image_path)
    if image_type is None:
        print('Cannot guess file type!')
        return

    email_message.add_attachment(content, maintype="image", subtype=image_type.extension)

    with smtplib.SMTP_SSL(host, port) as smtp_server:
        smtp_server.ehlo()
        smtp_server.login(username, password)
        smtp_server.sendmail(username, receiver, email_message.as_string())
        smtp_server.quit()

    print("✅ Email sent successfully!")
    print("Send email ENDED")


if __name__ == "__main__":
    send_email(image_path="images/Laravel-icon.png")
