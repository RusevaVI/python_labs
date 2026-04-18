import json
from typing import List, Any

from sem2.lab07.models import (
    PrintedBook,
    EBook,
    AudioBook
)

def save(books: List[Any],filepath: str) -> None:

    data = []
    for book in books:
        item = {
            "type": type(book).__name__,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "pages": book.pages,
            "price": book.price
        }

        if isinstance(book, PrintedBook):
            item["cover_type"] = book.cover_type
            item["weight"] = book.weight

        elif isinstance(book, EBook):
            item["file_format"] = book.file_format
            item["file_size"] = book.file_size

        elif isinstance(book, AudioBook):
            item["duration"] = book.duration
            item["narrator"] = book.narrator
        data.append(item)

    with open( filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False,indent=4)

def load(filepath: str) -> List[Any]:
    try:
        with open(filepath,"r",encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    books = []

    for item in data:
        book_type = item["type"]

        if book_type == "PrintedBook":
            book = PrintedBook(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                price=item["price"],
                cover_type=item["cover_type"],
                weight=item["weight"]
            )

        elif book_type == "EBook":
            book = EBook(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                price=item["price"],
                file_format=item["file_format"],
                file_size=item["file_size"]
            )

        elif book_type == "AudioBook":
            book = AudioBook(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                price=item["price"],
                duration=item["duration"],
                narrator=item["narrator"]
            )

        else:
            continue

        books.append(book)

    return books