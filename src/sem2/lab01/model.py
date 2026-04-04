from validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price,
)

class Book:
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

    # PROPERTIES

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

    # ЛОГИЧЕСКОЕ СОСТОЯНИЕ

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def return_book(self):
        if self._is_available:
            raise ValueError("Книга уже находится в библиотеке")
        self._is_available = True

    # БИЗНЕС-МЕТОДЫ

    def discount(self, percent):
        if not isinstance(percent, (int, float)):
            raise ValueError("Скидка должна быть числом")
        if percent < 0 or percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100")

        self.price = self._price * (1 - percent / 100)

    def calculate_rental_price(self, days):
        """
        Рассчитывает стоимость аренды.
        1 день = 2% от цены книги.
        """
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Количество дней должно быть положительным целым числом")

        if not self._is_available:
            raise ValueError("Нельзя арендовать книгу — она уже выдана")

        daily_rate = self._price * 0.02
        return round(daily_rate * days, 2)

    # МАГИЧЕСКИЕ МЕТОДЫ

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