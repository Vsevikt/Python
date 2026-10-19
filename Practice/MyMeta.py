class MyMeta(type):
    # mcsl - посилання на наш клас
    # name - назва
    # bases - кортеж (батьківські класи)
    # attrs - dict {name:"Alex", say_hi:lambda self:f'hello, self.name'}
    def __new__(mcls, name, bases, attrs):
        print(f'{name} class is created')
        attrs['category'] = 'general'
        return super().__new__(mcls, name,bases,attrs)

class Product(metaclass=MyMeta):
    pass

class User(metaclass=MyMeta):
    pass

p = Product()
print(p.category)