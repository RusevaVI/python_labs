from base import Book
from models import PrintedBook, EBook, AudioBook


class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только объекты Book и его наследников")

        if item in self._items:
            raise ValueError("Такая книга уже есть в коллекции")

        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("Такой книги нет в коллекции")
        self._items.remove(item)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        del self._items[index]

    def get_all(self):
        return self._items.copy()

    def find_by_title(self, title):
        result = []
        for book in self._items:
            if book.title.lower() == title.lower():
                result.append(book)
        return result

    def find_by_author(self, author):
        result = []
        for book in self._items:
            if book.author.lower() == author.lower():
                result.append(book)
        return result

    def find_by_year(self, year):
        result = []
        for book in self._items:
            if book.year == year:
                result.append(book)
        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort_by_title(self):
        self._items.sort(key=lambda book: book.title.lower())

    def sort_by_price(self):
        self._items.sort(key=lambda book: book.price)

    def sort_by_year(self):
        self._items.sort(key=lambda book: book.year)

    def sort(self, key):
        self._items.sort(key=key)

    def get_available(self):
        new_library = Library()
        for book in self._items:
            if book.is_available:
                new_library.add(book)
        return new_library

    def get_unavailable(self):
        new_library = Library()
        for book in self._items:
            if not book.is_available:
                new_library.add(book)
        return new_library

    def get_expensive(self, min_price):
        new_library = Library()
        for book in self._items:
            if book.price >= min_price:
                new_library.add(book)
        return new_library

    def get_only_printed(self):
        new_library = Library()
        for book in self._items:
            if isinstance(book, PrintedBook):
                new_library.add(book)
        return new_library

    def get_only_ebooks(self):
        new_library = Library()
        for book in self._items:
            if isinstance(book, EBook):
                new_library.add(book)
        return new_library

    def get_only_audiobooks(self):
        new_library = Library()
        for book in self._items:
            if isinstance(book, AudioBook):
                new_library.add(book)
        return new_library