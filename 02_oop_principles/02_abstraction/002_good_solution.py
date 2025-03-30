import os

os.system("cls")


class EmailService:
    def _connect(self):
        print("Connecting to email server.")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server.")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()


email = EmailService()
email.send_email()
