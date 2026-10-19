# Реалізувати класс Printer з властивостями модель та методом, який може друкувати різні документи
#
# Реалізувати класи (поля документів: title, text, ext, pages)
# - ExcellDocument
# - WordDocument
# - HtmlDocument
#
# Продумати та реалізувати абстрактний клас та перевірити роботу вашого класа Printer

from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title, text, ext, pages):
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    @abstractmethod
    def print_document(self):
        pass

class ExcelDocument(Document):
    def print_document(self):
        print(self.title + "." + self.ext)
        print(self.text)
        print(self.pages)

class WordDocument(Document):
    def print_document(self):
        print(self.title + "." + self.ext)
        print(self.text)
        print(self.pages)

class HtmlDocument(Document):
    def print_document(self):
        print(self.title + "." + self.ext)
        print(self.text)
        print(self.pages)

class Printer():
    def __init__(self, model):
        self.model = model

    def print_document(self, document):
        if not isinstance(document, Document):
            raise TypeError("Принтер може друкувати лише документи!")

        print(f"\nПринтер {self.model} друкує:")
        document.print_document()

def main():
    printer = Printer("HP LaserJet Pro")

    excel = ExcelDocument("Звіт", "Дані про продажі", "xlsx", 5)
    word = WordDocument("Реферат", "Текст реферату", "docx", 10)
    html = HtmlDocument("Вебсторінка", "Вітаємо на сайті!", "html", 2)

    for document in excel,word,html:
        printer.print_document(document)

main()