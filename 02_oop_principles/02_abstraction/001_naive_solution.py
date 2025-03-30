import os

os.system("cls")


class BadEmailService:
    def connect(self):
        print("Connecting to email server.")

    def authenticate(self):
        print("Authenticating...")

    def disconnect(self):
        print("Disconnecting from email server.")

    def send_email(self):
        print("Sending email...")


email = BadEmailService()
email.connect()
email.authenticate()
email.send_email()
email.disconnect()
