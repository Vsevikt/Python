# Завдання 1. Реалізуйте клас «Автомобіль».
# Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Car():
    def __init__(
            self,
             name:str='unknown',
             year_published:int=0,
             engine_capacity:float=0,
             color:str='unknown',
             price:float=0,
    ):
        self.__name = name
        self.__year_published = year_published
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def input_car(self):
        self.__name = str(input("Write car name: "))
        self.__year_published = int(input("Write car year published: "))
        self.__engine_capacity = float(input("Write car engine capacity: "))
        self.__color = str(input("Write car color: "))
        self.__price = float(input("Write car price: "))

    def show_car(self):
        print(self.__name)
        print(self.__year_published)
        print(self.__engine_capacity)
        print(self.__color)
        print(self.__price)

    def change_info_car(self):
        self.__name = str(input("Change car name: "))
        self.__year_published = int(input("Change car year published: "))
        self.__engine_capacity = float(input("Change car engine capacity: "))
        self.__color = str(input("Change car color: "))
        self.__price = float(input("Change car price: "))

        print("Changed car full information: ")
        print(self.__name)
        print(self.__year_published)
        print(self.__engine_capacity)
        print(self.__color)
        print(self.__price)

    def change_color_car(self):
        self.__color = str(input("Change write car name: "))
        print(f'{self.__name}, Changed color info: {self.__color}')

    def change_price_car(self):
        self.__price = float(input("Change write car price: "))
        print(f'{self.__name}, Changed price info: {self.__price}')

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not new_price.strip():
            raise ValueError("Price cannot be empty")
        if not isinstance(new_price, float):
            raise ValueError("Price must be a number value")

# car = Car()
# car.input_car()
# car.show_car()
# car.change_info_car()
# car.show_car()
# car.change_color_car()
# car.change_price_car()

# ---

# Завдання 2. Реалізуйте клас «Книга».
# Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Book():
    def __init__(
            self,
            name:str='unknown',
            year_published:int=0,
            publisher:str='unknown',
            genre:str='unknown',
            author:str='unknown',
            price:float=0,
            question:str='unknown',
            review:str='unknown',
            stars:int=0,
    ):
        self.__name = name
        self.__year_published = year_published
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price
        self.__question = question
        self.__review = review
        self.__stars = stars

    def input_book(self):
        self.__name = str(input("Write book name: "))
        self.__year_published = int(input("Write book year published: "))
        self.__publisher = str(input("Write book publisher: "))
        self.__genre = str(input("Write book genre: "))
        self.__author = str(input("Write book author: "))
        self.__price = float(input("Write book price: "))

    def show_book(self):
        print(self.__name)
        print(self.__year_published)
        print(self.__publisher)
        print(self.__genre)
        print(self.__author)
        print(self.__price)

    def change_info_book(self):
        self.__name = str(input("Change book name: "))
        self.__year_published = int(input("Change book year published: "))
        self.__publisher = str(input("Change publisher: "))
        self.__genre = str(input("Change genre: "))
        self.__author = str(input("Change author: "))
        self.__price = float(input("Change price: "))

    def question_book(self):
        self.__question = str(input("Write book question: "))
        print(f'Book: {self.__name}\nQuestion: {self.__question}')

    def review_book(self):
        self.__review = str(input("Write book review: "))
        self.__stars = int(input("Put stars for book: "))
        print(f'Book: {self.__name}\nReview: {self.__review}, {self.__stars} stars')

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not new_price.strip():
            raise ValueError("Price cannot be empty")
        if not isinstance(new_price, float):
            raise ValueError("Price must be a number value")

    # for review
    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, new_stars):
        if not new_stars.strip():
            raise ValueError("Stars cannot be empty")
        if not isinstance(new_stars, float):
            raise ValueError("Stars must be a number value")

# book = Book()
# book.input_book()
# book.show_book()
# book.change_info_book()
# book.show_book()
# book.question_book()
# book.review_book()

# ---

# Завдання 3. Реалізуйте клас «Стадіон».
# Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Stadium():
    def __init__(
            self,
            name:str='unknown',
            year_opened:int=0,
            country:str='unknown',
            city:str='unknown',
            capacity:int=0,
    ):
        self.__name = name
        self.__year_opened = year_opened
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def input_stadium(self):
        self.__name = str(input("Write stadium name: "))
        self.__year_opened = int(input("Write stadium year opened: "))
        self.__country = str(input("Write stadium country: "))
        self.__city = str(input("Write stadium city: "))
        self.__capacity = int(input("Write stadium capacity: "))

    def show_stadium(self):
        print(self.__name)
        print(self.__year_opened)
        print(self.__country)
        print(self.__city)
        print(self.__capacity)

    def change_info_stadium(self):
        self.__name = str(input("Change stadium name: "))
        self.__year_opened = int(input("Change stadium year opened: "))
        self.__country = str(input("Change stadium country: "))
        self.__city = str(input("Change stadium city: "))
        self.__capacity = int(input("Change stadium capacity: "))

    def show_year_opened(self):
        print(f'{self.__name}: {self.__year_opened}')

    def change_year_opened(self):
        self.__year_opened = int(input("Write year opened: "))
        print(f'{self.__name}: {self.__year_opened}')

    def show_capacity(self):
        print(f'{self.__name}: {self.__capacity}')

    def change_capacity(self):
        self.__capacity = int(input("Write capacity: "))
        print(f'{self.__name}: {self.__capacity}')

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

# stadium = Stadium()
# stadium.input_stadium()
# stadium.show_stadium()
# stadium.change_info_stadium()
# stadium.show_stadium()
# stadium.show_year_opened()
# stadium.change_year_opened()
# stadium.show_capacity()
# stadium.change_capacity()