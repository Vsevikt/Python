def horizontal_line(symbol):
    print(symbol * 10)

def vertical_line(symbol):
    for i in range(10):
        print(symbol)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

symbol = input("Введіть символ: ")
line = input("1 - горизонтальна, 2 - вертикальна: ")

if line == "1":
    show_line(symbol, horizontal_line)
elif line == "2":
    show_line(symbol, vertical_line)
else:
    print("Невірний вибір")