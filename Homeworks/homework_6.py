import json
from abc import ABC, abstractmethod

class LoggingMixin:
    def log(self, message):
        print(message)

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class DiscountMixin:
    def discount(self, percent):
        return self.price * (1 - percent / 100)

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def print_product(self):
        pass

class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    def print_product(self):
        print(self.name, self.price, "грн")

product = ProductManager("Milk", 1000)

product.log("Товар створено")
product.print_product()

print("Ціна зі знижкою:", product.discount(15), "грн")
print(product.to_json())
print(ProductManager.mro())