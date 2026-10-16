# 1) Створіть клас Book з атрибутами:
# title — назва книги;
# author — автор;
# year — рік видання.
# __init__ має задавати всі три атрибути.
# Додайте метод is_new(), який повертає True,
# якщо книга видана у 2020 році або пізніше, інакше — False.
# Створіть три книги та перевірте роботу методу.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_new(self):
        return self.year <= 2020

    def __self__(self):
        print(self.title)

b1 = Book('C#', 'Alex', 2020)
print(b1.is_new())

b2 = Book('Python', 'Tom', 2022)
print(b2.is_new())

b3 = Book('C++', 'Bob', 2018)
print(b3.is_new())

# 2) Створіть клас PositiveNumber, який дозволяє створювати об’єкти лише з невід’ємними цілими числами.
# Вимоги:
# використайте __new__();
# якщо передано від’ємне число, виведіть повідомлення Від'ємне число заборонено і поверніть None;
# якщо число невід’ємне, створіть об’єкт і збережіть число в атрибуті value через __init__().
# Приклад використання:
#
# a = PositiveNumber(10)
# b = PositiveNumber(-5)
#
# print(a.value)
# print(b) #None
# Очікуваний результат:
#
# 10

class PositiveNumber:
    def __new__(cls, value):
        if value < 0:
            print("Від'ємне число заборонено")
            return None
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value

a = PositiveNumber(10)
b = PositiveNumber(-5)

print(a.value)
print(b)

