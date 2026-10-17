class Book:
    def __init__(self, title, author, year, pages):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Некоректний рік видання")
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Кількість сторінок не може бути від'ємною")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f'{self.title} - {self.author}, {self.year}, {self.pages} сторінок'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return False
        return self.pages < other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return False
        return self.pages + other.pages

    def __contains__(self, word):
        return word.lower() in self.title.lower()

    def __bool__(self):
        return self.pages > 0


b1 = Book("Кобзар", "Тарас Шевченко", 1840, 250)
b2 = Book("Лісова пісня", "Леся Українка", 1911, 120)
b3 = Book("Кобзар", "Тарас Шевченко", 1840, 250)

print(b1)
print(repr(b1))
print(len(b1))
print(b1 == b3)
print(b1 < b2)
print(b1 + b2)
print("кобзар" in b1)
print(bool(b1))

books = [b1, b2]
books.sort()
print(books)