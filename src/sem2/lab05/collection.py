from sem2.lab03.models import Book


class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только Book")
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)


    def sort_by(self, key_func):
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate):
        new_lib = Library()
        for item in self._items:
            if predicate(item):
                new_lib.add(item)
        return new_lib

    def apply(self, func):
        return list(map(func, self._items))