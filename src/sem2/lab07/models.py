from sem2.lab01.validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price,
)


class Book:
    total_books: int = 0

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        pages: int,
        price: float
    ) -> None:

        validate_title(title)
        validate_author(author)
        validate_year(year)
        validate_pages(pages)
        validate_price(price)

        self._title: str = title
        self._author: str = author
        self._year: int = year
        self._pages: int = pages
        self._price: float = float(price)
        self._is_available: bool = True

        Book.total_books += 1

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @property
    def pages(self) -> int:
        return self._pages

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        validate_price(value)

        if not self._is_available:
            raise ValueError(
                "Нельзя менять цену выданной книги"
            )

        self._price = float(value)

    @property
    def is_available(self) -> bool:
        return self._is_available

    def borrow(self) -> None:
        if not self._is_available:
            raise ValueError("Книга уже выдана")

        self._is_available = False

    def return_book(self) -> None:
        if self._is_available:
            raise ValueError(
                "Книга уже находится в библиотеке"
            )

        self._is_available = True

    def calculate_rental_price(
        self,
        days: int
    ) -> float:

        if not isinstance(days, int) or days <= 0:
            raise ValueError(
                "Количество дней должно быть "
                "положительным целым числом"
            )

        daily_rate = self._price * 0.02

        return round(daily_rate * days, 2)

    def calculate_access_cost(
        self,
        days: int
    ) -> float:

        return self.calculate_rental_price(days)

    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return self._price

    def __str__(self) -> str:

        status = (
            "Доступна"
            if self._is_available
            else "Выдана"
        )

        return (
            f"Книга: {self._title}\n"
            f"Автор: {self._author}\n"
            f"Год: {self._year}\n"
            f"Страниц: {self._pages}\n"
            f"Цена: {self._price:.2f} руб.\n"
            f"Статус: {status}"
        )

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Book):
            return False

        return (
            self._title == other._title
            and self._author == other._author
            and self._year == other._year
        )


class PrintedBook(Book):

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        pages: int,
        price: float,
        cover_type: str,
        weight: float
    ) -> None:

        super().__init__(
            title,
            author,
            year,
            pages,
            price
        )

        self._cover_type: str = cover_type
        self._weight: float = weight

    @property
    def cover_type(self) -> str:
        return self._cover_type

    @property
    def weight(self) -> float:
        return self._weight

    def shipping_cost(self) -> float:
        return round(self._weight * 0.5, 2)

    def calculate_access_cost(
        self,
        days: int
    ) -> float:

        return round(
            self.calculate_rental_price(days)
            + self.shipping_cost(),
            2
        )

    def __str__(self) -> str:

        return (
            f"[Печатная книга]\n"
            f"{super().__str__()}\n"
            f"Тип обложки: {self._cover_type}\n"
            f"Вес: {self._weight} г"
        )


class EBook(Book):

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        pages: int,
        price: float,
        file_format: str,
        file_size: float
    ) -> None:

        super().__init__(
            title,
            author,
            year,
            pages,
            price
        )

        self._file_format: str = file_format
        self._file_size: float = file_size

    @property
    def file_format(self) -> str:
        return self._file_format

    @property
    def file_size(self) -> float:
        return self._file_size

    def download_info(self) -> str:

        return (
            f"Файл {self._file_format}, "
            f"размер {self._file_size} МБ"
        )

    def calculate_access_cost(
        self,
        days: int
    ) -> float:

        return round(
            self.price * 0.01 * days,
            2
        )

    def __str__(self) -> str:

        return (
            f"[Электронная книга]\n"
            f"{super().__str__()}\n"
            f"Формат: {self._file_format}\n"
            f"Размер файла: {self._file_size} МБ"
        )


class AudioBook(Book):

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        pages: int,
        price: float,
        duration: float,
        narrator: str
    ) -> None:

        super().__init__(
            title,
            author,
            year,
            pages,
            price
        )

        self._duration: float = duration
        self._narrator: str = narrator

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def narrator(self) -> str:
        return self._narrator

    def listen_sample(self) -> str:

        return (
            f"Доступен фрагмент "
            f"в исполнении {self._narrator}"
        )

    def calculate_access_cost(
        self,
        days: int
    ) -> float:

        return round(
            self.price * 0.015 * days,
            2
        )

    def __str__(self) -> str:

        return (
            f"[Аудиокнига]\n"
            f"{super().__str__()}\n"
            f"Длительность: {self._duration} ч\n"
            f"Читает: {self._narrator}"
        )