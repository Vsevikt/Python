a = int(input("Напишите a число: "))
b = int(input("Напишите b число: "))

answer = str(input("Выберите ответ для повторения: 1. Да, 2. Нет: "))

while answer == "1":
    select = int(input("Выберите действие:\n1. сумма чисел\n2. произведение\n3. вычитание\n4. деление\n0. выход из программы: "))
    if select == 1:
        res = a + b
        print(res)
    elif select == 2:
        res = a * b
        print(res)
    elif select == 3:
        res = a - b
        print(res)
    elif select == 4:
        if b == 0:
            print("Деление на 0 нельзя")
        else:
            res = a / b
            print(res)
    elif select == 0:
        print("Вы вышли из программы")
        exit()
    else:
        print("Недействительное значение")
else:
    print("До свидания")

# ---

def double(x):
    return x * 2
print(double(5))  # 10

double = lambda x: x * 2
print(double(5))

add = lambda x, y: x + y
print(add(1, 10))

get_max = lambda a, b: a if a > b else b
print(get_max(4, 9))  # 9

# ---

def sum(func):
    def wrapper(*args, **kwargs):
        num:int = func(*args, **kwargs)
    return wrapper

@sum
def add(a, b):
    print(a + b)

add(3, 5)