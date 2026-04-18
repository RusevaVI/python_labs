from interfaces import Printable, Rentable
from models import Book
class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только объекты Book и его наследников")

        if item in self._items:
            raise ValueError("Такая книга уже есть в коллекции")

        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def get_printable(self):
        result = []
        for item in self._items:
            if isinstance(item, Printable):
                result.append(item)
        return result

    def get_rentable(self):
        result = []
        for item in self._items:
            if isinstance(item, Rentable):
                result.append(item)
        return result