from Student import *
from abc import ABC, abstractmethod
# a - abstract, b - base, c - class

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Car moved")

def main():
    s = StudentOnline.from_string("Ivan:20")
    print(type(s))

main()