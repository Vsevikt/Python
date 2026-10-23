# Створити LoggingMixin із методом log(message), який виводить повідомлення з префіксом [LOG].
# Під'єднати міксін до класу User.
# Додати до методу login() запис у журнал.
# Створити об'єкт User("Олександр") і перевірити роботу методів.

import json

class JsonSerializerMixin():
    def to_json(self):
        return json.dumps(self.__dict__, default=str, ensure_ascii=False)

class LoggingMixin():
    def log(self, message):
        print(f"{User.__name__}: {message}")

class User(JsonSerializerMixin, LoggingMixin):
    def __init__(self, name):
        self.name = name
 
    def login(self):
        print(f"{self.name} увійшов у систему")

u = User(name="Олександр")
print(u.to_json())
u.login()


