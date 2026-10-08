# 1) Створіть функцію, яка повертає всі непарні числа в діапазоні.
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

print("Task 1: ")
def task1(a, b):
    step = 1 if a < b else -1
    for i in range(a, b + step, step):
        if i % 2 != 0:
            yield i

for number in task1(100, 1):
    print(number)

print("\n")

# 2) Створіть функцію, яка повертає всі значення кратні п'яти в діапазоні.
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

print("Task 2: ")
def task2(a, b):
    step = 1 if a < b else -1
    for i in range(a, b + step, step):
        if i % 5 == 0:
            yield i

for number in task2(100, 1):
    print(number)

print("\n")

# 3) Створіть функцію, яка приймає діапазон та виводить всі паліндроми з даного діапазона
# Функція приймає початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

print("Task 3: ")
def task3(a, b):
    step = 1 if a < b else -1
    for i in range(a, b + step, step):
        if str(i) == str(i)[::-1]:
            yield i

for number in task3(1700, 20):
    print(number)

print("\n")