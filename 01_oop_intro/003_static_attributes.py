import os

os.system("cls")


class User:
    user_count = 0

    def __init__(self, username, email):
        self._username = username
        self._email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self._username}, Email: {self._email}.")


user1 = User("dantheman", " Dan@gmail.com ")
user2 = User("batman", "bat@gmail.com")
print(User.user_count)
print(user1.user_count)
print(user2.user_count)
