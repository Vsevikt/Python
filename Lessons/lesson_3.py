# Реалізуйте клас «Людина». З
# бережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Person():
    __counter = 0
    def __init__(self, name='unknown', age='unknown', date_of_birth='unknown', phone='unknown', place='unknown', country='unknown', home_address='unknown'):
        Person.__counter += 1
        self.__name = name
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__phone = phone
        self.__place = place
        self.__country = country
        self.__home_address = home_address

    def show_person(self):
        print(self.__name)
        print(self.__date_of_birth)
        print(self.__phone)

    def show_place(self):
        print(self.__place)
        print(self.__country)

    def show_home_address(self):
        print(self.__home_address)

    def input_person(self):
        self.__name = input("Please enter your name: ")
        self.__age = input("Please enter your age: ")
        self.__date_of_birth = input("Please enter your date of birth: ")
        self.__phone = input("Please enter your phone number: ")
        self.__place = input("Please enter your place: ")
        self.__country = input("Please enter your country: ")
        self.__home_address = input("Please enter your home address: ")

    def full_info_person(self):
        print(self.__name)
        print(self.__date_of_birth)
        print(self.__phone)
        print(self.__place)
        print(self.__country)
        print(self.__home_address)

    def input_name(self):
        self.__name = input("Please enter your name: ")

    def __str__(self):
        return f"{self.__name} is {self.__age} years old, {self.__counter}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise ValueError("Please enter a valid age")
        if new_age < 0 or new_age >= 120:
            raise ValueError(f"Invalid Age {new_age}")
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if not new_name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = new_name

person = Person()
# person.input_person()
# person.full_info_person()
print(person)

print(Person.counter)

@staticmethod
def get_counter():
    return Person.__counter

# person3 = Person("Bob", 30)
# print(person3)
# try:
#     person3.age += 1
#     print(person3)
#     person3.age = "40"
#     print(person3)
# except Exception as e:
#     print(e)
