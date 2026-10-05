# Створіть функцію, яка повертає всі значення зі списку,
# що знаходяться в діапазоні, зазначеному користувачем.
# Функція приймає список, початок і кінець діапазону як параметри.
# Використовуйте механізм генераторів усередині функції.

def main(numbers, start, end):
    for number in numbers:
        if start <= number <= end:
            yield number


numbers = list(map(int, input().split()))
start = int(input())
end = int(input())

for number in main(numbers, start, end):
    print(number)