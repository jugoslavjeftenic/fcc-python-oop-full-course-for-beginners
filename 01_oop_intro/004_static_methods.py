import os

os.system("cls")


class BancAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposite amount must be positive.")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(
            f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}."
        )

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BancAccount("Alice", 500)
account.deposit(200)

print(BancAccount.is_valid_interest_rate(3))
print(BancAccount.is_valid_interest_rate(10))
