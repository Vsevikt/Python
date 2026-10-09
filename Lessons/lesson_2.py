def tuple_fruits():
    fruits = (("apple", 10), ("banana", 25), ("cherry", 50))
    find = input("Введіть назву продукту: ")
    print(f"{find}: {dict(fruits).get(find, 0)}")

def list_auto():
    cars = ["BMW", "Audi", "BMW", "Toyota", "Audi"]

    name = input("Введіть назву автовиробника: ")
    new_name = input("Введіть нову назву для заміни: ")

    for i in range(len(cars)):
        if cars[i] == name:
            cars[i] = new_name

    print(cars)

def dict_countries():
    # 6, 1
    countries = {"Poland": "Warsaw", "Netherlands": "Amsterdam", "Austria": "Vienna"}

    action = input("Дія (додати/видалити/пошук/перевірка): ")
    name = input("Назва країни: ")

    if action == "додати":
        countries[name] = input("Столиця: ")
    elif action == "видалити":
        countries.pop(name, None)
    elif action == "пошук":
        print([c for c in countries if name.lower() in c.lower()])
    elif action == "перевірка":
        print(name in countries)

    print(countries)

    # 2
    cities1 = {"Warsaw", "Amsterdam", "Amsterdam"}
    cities2 = {"Kyiv", "Odesa", "Kharkiv"}

    cities3 = cities1 & cities2
    print(cities3)

    # 3
    cities1 = {"Warsaw", "Amsterdam", "Amsterdam"}
    cities2 = {"Kyiv", "Kharkiv"}

    cities3 = cities1 - cities2

    print(cities3)

    print(countries)

def is_negative(num):
    return num<0

def my_decorator(func):
    def wrapper():
        print("Start text")
        func()
        print("End text")
    return wrapper

@my_decorator
def show_message():
    print("Hi Python")

def main():
    # tuple_fruits()
    # list_auto()
    # dict_countries()

    # get_sum = lambda a, b: a + b
    #
    li = [2,14,60,25,21.3,3,7,3,2]
    # result =list(map(lambda x:x**2, li))
    # print(f"func map: {result}")
    #
    # result = list(map(lambda x: x%2==0, li))
    # print(f"func map: {result}")

    result = list(filter(lambda x:x%2==0,li))
    print(f"func filter: {result}")

    positive_or_meg = lambda num: "positive or zero" if num>0 else "negative"
    print(positive_or_meg(-10))
    print(positive_or_meg(10))
    print(positive_or_meg(0))

    test_func = lambda *arg: arg[0]*3
    print(test_func(5,6,23,6,13,1))


if __name__ == '__main__':
    main()


