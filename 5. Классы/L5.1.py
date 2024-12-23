class Book:
    def __init__(self, tittle, author, year):
        self.tittle = tittle
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги: {self.tittle}. Автор: {self.author}. Год издания: {self.year}.'
obj = Book('Война и мир', 'Л. Толстой', 10)
print(obj.get_info())