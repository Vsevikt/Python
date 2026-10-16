# SOLID S - Single Responsibility Principle
# __new__ - створення об'єкта
# __init__ - ініціалізація об'єкта

Player = type(
    "Player",
    (),
    {
        'role':'super admin',
        'age':18,
        'move':lambda self:f'Moving... ()'
    }
)

p = Player()
print(p.move(), p.role)

class User:
    def __init__(self, name='unknown', age=18):
        self.__name = name
        self.age = age
        self.email = 'admin@email.com'
        self.phone = '1 555 555 555'

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age <= 120:
            self.__age = new_age

    def __str__(self):
        return f"{self.__name} is {self.age} years old"

    def show_user(self):
        return f"{self.__name} is {self.age} years old"

# ---

# user = User("Alex", "30")
# print(user.show_user())
# print(user)

# user1 = User("Alex", 30)
# user2 = User(name="Bob")
# user3 = User(20)
# user4 = User()

# ---

# print(user1.phone, user2.email, user3, user4)
# print(user1._User__name)


# class Dog:
#     pass
#
# user = User();
# dog = Dog();
#
# print(isinstance(dog, User))