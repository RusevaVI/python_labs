from typing import List, Dict, Any

from sem2.lab02.collection import Library

from sem2.lab07.models import (
    PrintedBook,
    EBook,
    AudioBook
)

from exceptions import (
    DuplicateItemError,
    ItemNotFoundError
)


class LibraryApp:

    def __init__(self) -> None:
        self.library = Library()

    def create_and_add_book(
        self,
        book_type: str,
        data: Dict[str, Any]
    ) -> None:

        if book_type == "1":

            book = PrintedBook(
                title=data["title"],
                author=data["author"],
                year=int(data["year"]),
                pages=int(data["pages"]),
                price=float(data["price"]),
                cover_type=data["cover_type"],
                weight=float(data["weight"])
            )

        elif book_type == "2":

            book = EBook(
                title=data["title"],
                author=data["author"],
                year=int(data["year"]),
                pages=int(data["pages"]),
                price=float(data["price"]),
                file_format=data["file_format"],
                file_size=float(data["file_size"])
            )

        elif book_type == "3":

            book = AudioBook(
                title=data["title"],
                author=data["author"],
                year=int(data["year"]),
                pages=int(data["pages"]),
                price=float(data["price"]),
                duration=float(data["duration"]),
                narrator=data["narrator"]
            )

        else:
            raise ValueError("Неизвестный тип книги")

        for existing_book in self.library:

            if (
                    existing_book.title.lower() == book.title.lower()
                    and
                    existing_book.author.lower() == book.author.lower()
            ):
                raise DuplicateItemError(
                    "Книга с таким названием и автором уже существует"
                )

        self.library.add(book)

    def get_all_books(self) -> List[Any]:

        return self.library.get_all()

    def remove_book(self, title: str, author: str) -> None:

        for book in self.library:

            if book.title.lower() == title.lower() and book.author.lower() == author.lower():

                self.library.remove(book)

                return

        raise ItemNotFoundError(
            "Книга не найдена"
        )

    def find_books(self, title: str) -> List[Any]:

        result = [
            book for book in self.library
            if title.lower() in book.title.lower()
        ]

        if not result:
            raise ItemNotFoundError(
                "Книги не найдены"
            )

        return result

    def filter_expensive( self, min_price: float) -> List[Any]:

        if min_price < 0:
            raise ValueError(
                "Цена не может быть отрицательной"
            )

        result = [ book for book in self.library if book.price >= min_price ]

        if not result:
            raise ItemNotFoundError(
                "Подходящих книг нет"
            )

        return result

    def sort_books( self, strategy: str) -> List[Any]:

        books = self.library.get_all()

        if strategy == "title":
            return sorted(books, key=lambda x: x.title.lower())

        if strategy == "price":
            return sorted(books, key=lambda x: x.price)

        if strategy == "year":
            return sorted(books, key=lambda x: x.year)

        return books