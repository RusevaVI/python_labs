from sem2.lab01.validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price,
)

from interfaces import Printable, Rentable


class Book(Printable, Rentable):
    total_books = 0

    def __init__(self, title, author, year, pages, price):
        validate_title(title)
        validate_author(author)
        validate_year(year)
        validate_pages(pages)
        validate_price(price)

        self._title = title
        self._author = author
        self._year = year
        self._pages = pages
        self._price = float(price)
        self._is_available = True

        Book.total_books += 1

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        validate_price(value)
        if not self._is_available:
            raise ValueError("Нельзя менять цену выданной книги")
        self._price = float(value)

    @property
    def is_available(self):
        return self._is_available

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def return_book(self):
        if self._is_available:
            raise ValueError("Книга уже находится в библиотеке")
        self._is_available = True

    def discount(self, percent):
        if not isinstance(percent, (int, float)):
            raise ValueError("Скидка должна быть числом")
        if percent < 0 or percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100")

        self.price = self._price * (1 - percent / 100)

    def calculate_rental_price(self, days):
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Количество дней должно быть положительным целым числом")

        if not self._is_available:
            raise ValueError("Нельзя арендовать книгу — она уже выдана")

        daily_rate = self._price * 0.02
        return round(daily_rate * days, 2)

    def calculate_access_cost(self, days):
        return self.calculate_rental_price(days)

    def to_string(self) -> str:
        return str(self)

    def __str__(self):
        status = "Доступна" if self._is_available else "Выдана"
        return (
            f"Книга: {self._title}\n"
            f"Автор: {self._author}\n"
            f"Год: {self._year}\n"
            f"Страниц: {self._pages}\n"
            f"Цена: {self._price:.2f} руб.\n"
            f"Статус: {status}"
        )

    def __repr__(self):
        return (
            f"Book(title='{self._title}', author='{self._author}', "
            f"year={self._year}, pages={self._pages}, price={self._price})"
        )

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self._title == other._title
            and self._author == other._author
            and self._year == other._year
        )


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, price, cover_type, weight):
        super().__init__(title, author, year, pages, price)
        self._cover_type = cover_type
        self._weight = weight

    @property
    def cover_type(self):
        return self._cover_type

    @property
    def weight(self):
        return self._weight

    def shipping_cost(self):
        return round(self._weight * 0.5, 2)

    def calculate_access_cost(self, days):
        return round(self.calculate_rental_price(days) + self.shipping_cost(), 2)

    def to_string(self) -> str:
        return str(self)

    def __str__(self):
        return (
            f"[Печатная книга]\n"
            f"{super().__str__()}\n"
            f"Тип обложки: {self._cover_type}\n"
            f"Вес: {self._weight} г"
        )


class EBook(Book):
    def __init__(self, title, author, year, pages, price, file_format, file_size):
        super().__init__(title, author, year, pages, price)
        self._file_format = file_format
        self._file_size = file_size

    @property
    def file_format(self):
        return self._file_format

    @property
    def file_size(self):
        return self._file_size

    def download_info(self):
        return f"Файл {self._file_format}, размер {self._file_size} МБ"

    def calculate_access_cost(self, days):
        return round(self.price * 0.01 * days, 2)

    def to_string(self) -> str:
        return str(self)

    def __str__(self):
        return (
            f"[Электронная книга]\n"
            f"{super().__str__()}\n"
            f"Формат: {self._file_format}\n"
            f"Размер файла: {self._file_size} МБ"
        )


class AudioBook(Book):
    def __init__(self, title, author, year, pages, price, duration, narrator):
        super().__init__(title, author, year, pages, price)
        self._duration = duration
        self._narrator = narrator

    @property
    def duration(self):
        return self._duration

    @property
    def narrator(self):
        return self._narrator

    def listen_sample(self):
        return f"Доступен фрагмент аудиокниги в исполнении {self._narrator}"

    def calculate_access_cost(self, days):
        return round(self.price * 0.015 * days, 2)

    def to_string(self) -> str:
        return str(self)

    def __str__(self):
        return (
            f"[Аудиокнига]\n"
            f"{super().__str__()}\n"
            f"Длительность: {self._duration} ч\n"
            f"Читает: {self._narrator}"
        )