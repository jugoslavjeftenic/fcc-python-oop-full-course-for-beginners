import os

os.system("cls")


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username}."
        )


# user1 = User("dantheman", "dan@gmail.com", "123")
# user2 = User("batman", "bat@gmail.com", "abc")
# user1.say_hi_to_user(user2)
# user1.email = "danny@gmail.com"
# print(user1.email)


class User2:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def get_email(self):
        return self._email

    def clean_email(self):
        return self._email.lower().strip()


# user1 = User2("dantheman", " Dan@gmail.com ", "123")
# user2 = User2("batman", "bat@gmail.com", "abc")
# print(user1.get_email())
# print(user1.clean_email())


class User3:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password


# user = User3("dantheman", "dan@gmail.com", "123")
# print(user.username)
# print(user._email)
# print(user.__password)

from datetime import datetime


class User4:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def get_email(self):
        print(f"Email accessed at {datetime.now()}.")
        return self._email

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email


# user = User4("batman", "bat@gmail.com", "abc")
# print(user.get_email())
# user.set_email("batman@gmail.com")
# print(user.get_email())
# user.set_email("this is not an email")
# print(user.get_email())


class User5:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}.")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user = User5("batman", "bat@gmail.com", "abc")
print(user.email)
user.email = "batman@gmail.com"
print(user.email)
user.email = "this is not an email"
print(user.email)
