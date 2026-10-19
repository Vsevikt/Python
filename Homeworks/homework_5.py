from abc import ABC, abstractmethod

# 1. Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину), клас Blender
# (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

class Device(ABC):
    def __init__(self, name, brand, power):
        self.__name = name
        self.__brand = brand
        self.__power = power

    def show_info(self):
        print(f"Name: {self.__name}")
        print(f"Brand: {self.__brand}")
        print(f"Power: {self.__power} W")

    @abstractmethod
    def turn_on(self):
        pass

class CoffeeMachine(Device):
    def turn_on(self):
        print('Coffee Machine turn on')

class Blender(Device):
    def turn_on(self):
        print('Blender turn on')

class MeatGrinder(Device):
    def turn_on(self):
        print('Meat Grinder turn on')

# 2. Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас Frigate (містить інформацію про фрегат),
# клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship(ABC):
    def __init__(self, name, country, displacement):
        self.__name = name
        self.__country = country
        self.__displacement = displacement

    def show_info(self):
        print(f"Name: {self.__name}")
        print(f"Country: {self.__country}")
        print(f"Displacement: {self.__displacement} tons")

    @abstractmethod
    def sail(self):
        pass

class Frigate(Ship):
    def sail(self):
        print("Frigate is sailing")

class Destroyer(Ship):
    def sail(self):
        print("Destroyer is sailing")

class Cruiser(Ship):
    def sail(self):
        print("Cruiser is sailing")


# 3. Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.

class Money(ABC):
    def __init__(self, whole, cents):
        self.__whole = whole + cents // 100
        self.__cents = cents % 100

    def show_info(self):
        print(f"Whole: {self.__whole}")
        print(f"Cents: {self.__cents}")
        print(f"Price: {self.__whole},{self.__cents}")

    def get_total(self):
        return self.__whole * 100 + self.__cents

    def set_total(self, total):
        total = max(0, total)
        self.__whole = total // 100
        self.__cents = total % 100

    @abstractmethod
    def reduce_price(self, amount):
        pass

class Product(Money):
    def __init__(self, name, whole, cents):
        super().__init__(whole, cents)
        self.name = name

    def reduce_price(self, amount):
        print("\nAfter discount:")
        total = self.get_total()
        self.set_total(total - amount)

    def show_info(self):
        print(f"Product: {self.name}")
        super().show_info()

# -- Main --
def main():
    # -- Device
    coffee = CoffeeMachine('Coffee', 'Coffee', 2)
    blender =Blender('Blender', 'Blender', 3)
    meat_grinder = MeatGrinder('Meat Grinder', 'Meat Grinder', 4)

    for device in coffee, blender, meat_grinder:
        device.show_info()

    for device in coffee, blender, meat_grinder:
        device.turn_on()

    # -- Ship
    frigate = Frigate("Sachsen", "Germany", 5800)
    destroyer = Destroyer("Horizon", "France", 7000)
    cruiser = Cruiser("De Zeven Provinciën", "Netherlands", 6050)

    for ship in frigate, destroyer, cruiser:
        ship.show_info()

    for ship in frigate, destroyer, cruiser:
        ship.sail()

    # -- Money
    product = Product("Coffee", 15, 75)
    product.show_info()

    product.reduce_price(250)
    product.show_info()

main()