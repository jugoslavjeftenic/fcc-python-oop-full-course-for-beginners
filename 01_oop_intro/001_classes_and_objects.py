import os

os.system("cls")

name = "Jugoslav"
age = 52

# print(type(name))
# print(type(age))


class Dog:
    def bark(self):
        print("Whoof Whoof")


# dog = Dog()
# dog.bark()


class Dog2:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Whoof Whoof")


# dog2 = Dog2("Fluffy", "Three-headed dog")
# print(dog2.name)
# print(dog2.breed)


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


class Dog3:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof Whoof")


owner = Owner(name, "Studentska bb", "024/123-456")
dog3 = Dog3("Fluffy", "Three-headed dog", owner)
print(dog3.name)
print(dog3.breed)
print(dog3.owner.name)
