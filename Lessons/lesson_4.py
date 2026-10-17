# task 1

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

# b1 = Book('C#', 'Alex', 2020)
# print(b1.is_new())
#
# b2 = Book('Python', 'Tom', 2022)
# print(b2.is_new())
#
# b3 = Book('C++', 'Bob', 2018)
# print(b3.is_new())

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

# a = PositiveNumber(10)
# b = PositiveNumber(-5)
#
# print(a.value)
# print(b)


# task 2

# Створіть класс MyIntArray, який буде працювати лише з масивом цілих чисел
# Реалізувати магічні методи
# 1) __init__
# 2) __str__ - друкує масив (ключ значення) у консоль
# 3) __add__ додає до масива інший масив (складає відповідні елементи, виконує це лише тоді, коли
# масиви мають однаковий розмір)
# додає до масива число (збільшує кожен елемент масив на задане число)
# 4) __mult__ за принципом __add__
# 5) порівняння масивів arr1==arr2 (всі елементи повинні сходитись)
# 6) __getitem__, __setitem__

class MyIntArray:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return str(self.arr)

    def __add__(self, other):
        result = []
        if isinstance(other, MyIntArray):
            if self.arr.__len__() != other.arr.__len__():
                return None
            i = 0
            while i < self.arr.__len__():
                result.append(self.arr[i] + other.arr[i])
                i += 1
        elif isinstance(other, int):
            for x in self.arr:
                result.append(x + other)
        return MyIntArray(result)

    def __mul__(self, other):
        result = []
        if isinstance(other, MyIntArray):
            if self.arr.__len__() != other.arr.__len__():
                return None
            i = 0
            while i < self.arr.__len__():
                result.append(self.arr[i] * other.arr[i])
                i += 1
        elif isinstance(other, int):
            for x in self.arr:
                result.append(x * other)
        return MyIntArray(result)

    def __eq__(self, other):
        if not isinstance(other, MyIntArray):
            return NotImplemented
        return self.arr == other.arr

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value


m1 = MyIntArray([1, 2, 3])
m2 = MyIntArray([4, 5, 6])

print(m1)
print(m1 + m2)
print(m1 + 2)
print(m1 * m2)
print(m1 * 2)
print(m1 == m2)
print(m1[0])

m1[0] = 10
print(m1)