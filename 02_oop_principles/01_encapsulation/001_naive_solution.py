import os

os.system("cls")


class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)
