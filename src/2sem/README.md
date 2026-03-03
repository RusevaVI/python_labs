# RusevaVI
## Лабораторная работа 1

### model.py

```python
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
```

### validate.py
```python
from datetime import datetime

def validate_title(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Название должно быть непустой строкой")


def validate_author(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Автор должен быть непустой строкой")


def validate_year(value):
    current_year = datetime.now().year
    if not isinstance(value, int) or value < 0 or value > current_year:
        raise ValueError("Год издания должен быть корректным числом")


def validate_pages(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Количество страниц должно быть больше 0")


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")
```

### demo.py

```python
"""
Демонстрационный модуль для работы с классом Book
"""
from model import Book

def demonstrate():
    """Основная функция демонстрации"""

    print("Демонстрация работы класса Book")
    print("Аргументы: title, author, year, pages, price")

    print("\nСоздание объектов:")

    book1 = Book("Война и мир", "Лев Толстой", 1869, 1225, 1200)
    book2 = Book("1984", "Джордж Оруэлл", 1949, 328, 800)
    book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 950)

    print("\nКНИГА 1:")
    print(book1)

    print("\nКНИГА 2:")
    print(book2)

    print("\nКНИГА 3:")
    print(book3)

    print("\n__repr__:")
    print(f"repr(book1): {repr(book1)}")
    print(f"repr(book2): {repr(book2)}")

    print("\nАтрибуты класса:")
    print(f"Всего создано книг: {Book.total_books}")
    print(f"Доступ через экземпляр: {book1.total_books}")

    print("\nРАБОТА С SETTER (изменение цены):")
    print(f"Текущая цена book1: {book1.price} руб.")
    book1.price = 1300
    print(f"Новая цена book1: {book1.price} руб.")

    print("\nПроверка setter (валидация):")
    try:
        book1.price = -500
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        book1.price = "тысяча"
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")

    print("\nСОСТОЯНИЕ КНИГИ:")
    book1.borrow()
    print(book1)

    try:
        book1.calculate_rental_price(3)
    except ValueError as e:
        print(f"Ошибка аренды: {e}")

    book1.return_book()
    print("Книга снова доступна:", book1.is_available)

    print("\nБИЗНЕС-МЕТОДЫ:")
    book2.discount(15)
    print(f"Цена книги '{book2.title}' после скидки 15%: {book2.price:.2f} руб.")
    print(f"Аренда книги '{book2.title}' на 5 дней: {book2.calculate_rental_price(5)} руб.")

    print("\nСРАВНЕНИЕ (__eq__):")
    book4 = Book("Война и мир", "Лев Толстой", 1869, 500, 900)
    book5 = Book("Гарри Поттер", "Дж. К. Роулинг", 1997, 400, 1000)
    print(f"book1 == book4 (одно произведение): {book1 == book4}")
    print(f"book1 == book5 (разные книги): {book1 == book5}")
    print(f"book1 == book1 (тот же объект): {book1 == book1}")

    print("\nПРОВЕРКА ВАЛИДАЦИИ ПРИ СОЗДАНИИ:")
    test_cases = [
        ("пустое название", {"title": "", "author": "Автор", "year": 2000, "pages": 100, "price": 500}),
        ("год в будущем", {"title": "Книга", "author": "Автор", "year": 3000, "pages": 100, "price": 500}),
        ("отрицательные страницы", {"title": "Книга", "author": "Автор", "year": 2000, "pages": -10, "price": 500}),
        ("цена строка", {"title": "Книга", "author": "Автор", "year": 2000, "pages": 100, "price": "1000"}),
        ("отрицательная цена", {"title": "Книга", "author": "Автор", "year": 2000, "pages": 100, "price": -100}),
    ]

    for description, kwargs in test_cases:
        print(f"\nПопытка: {description}")
        try:
            Book(**kwargs)
            print("Создано успешно (ОШИБКА — должно быть исключение)")
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")

    print("\nДемонстрация завершена.")


if __name__ == "__main__":
    demonstrate()
```

### Что выводит
``` text
Демонстрация работы класса Book
Аргументы: title, author, year, pages, price

Создание объектов:

КНИГА 1:
Книга: Война и мир
Автор: Лев Толстой
Год: 1869
Страниц: 1225
Цена: 1200.00 руб.
Статус: Доступна

КНИГА 2:
Книга: 1984
Автор: Джордж Оруэлл
Год: 1949
Страниц: 328
Цена: 800.00 руб.
Статус: Доступна

КНИГА 3:
Книга: Мастер и Маргарита
Автор: Михаил Булгаков
Год: 1967
Страниц: 480
Цена: 950.00 руб.
Статус: Доступна

__repr__:
repr(book1): Book(title='Война и мир', author='Лев Толстой', year=1869, pages=1225, price=1200.0)
repr(book2): Book(title='1984', author='Джордж Оруэлл', year=1949, pages=328, price=800.0)

Атрибуты класса:
Всего создано книг: 3
Доступ через экземпляр: 3

РАБОТА С SETTER (изменение цены):
Текущая цена book1: 1200.0 руб.
Новая цена book1: 1300.0 руб.

Проверка setter (валидация):
Ошибка: Цена не может быть отрицательной
Ошибка: Цена должна быть числом

СОСТОЯНИЕ КНИГИ:
Книга: Война и мир
Автор: Лев Толстой
Год: 1869
Страниц: 1225
Цена: 1300.00 руб.
Статус: Выдана
Ошибка аренды: Нельзя арендовать книгу — она уже выдана
Книга снова доступна: True

БИЗНЕС-МЕТОДЫ:
Цена книги '1984' после скидки 15%: 680.00 руб.
Аренда книги '1984' на 5 дней: 68.0 руб.

СРАВНЕНИЕ (__eq__):
book1 == book4 (одно произведение): True
book1 == book5 (разные книги): False
book1 == book1 (тот же объект): True

ПРОВЕРКА ВАЛИДАЦИИ ПРИ СОЗДАНИИ:

Попытка: пустое название
Ошибка: Название должно быть непустой строкой

Попытка: год в будущем
Ошибка: Год издания должен быть корректным числом

Попытка: отрицательные страницы
Ошибка: Количество страниц должно быть больше 0

Попытка: цена строка
Ошибка: Цена должна быть числом

Попытка: отрицательная цена
Ошибка: Цена не может быть отрицательной

Демонстрация завершена.
```
Ответы на вопросы
Вопрос 1. Что является сущностью?

: Это книга (Book). Это не действие, не процесс, а именно объект библиотеки.

Вопрос 2. Какие у него атрибуты?

: В моем классе:
	•	title — название
	•	author — автор
	•	year — год издания
	•	pages — количество страниц
	•	price — стоимость
	•	is_available — доступность (логическое состояние)

Также есть атрибут класса:
	•	total_books — общее количество созданных книг

Вопрос 3. Какие инварианты?
:Для моем книги:
	•	Название не пустое
	•	Автор не пустой
	•	Год ≥ 0 и ≤ текущего года
	•	Количество страниц > 0
	•	Цена ≥ 0
	•	Нельзя изменить цену, если книга выдана

Вопрос 4. Что значит “равенство”?
: Две книги равны, если совпадают:
	•	название
	•	автор
	•	год издания

Цена и количество страниц могут отличаться.

Это реализовано в __eq__.

Вопрос 5. Есть ли состояние?
Да, есть логическое состояние:
Оно хранится в _is_available.
И поведение зависит от состояния:
	•	Нельзя выдать книгу, если она уже выдана
	•	Нельзя менять цену, если книга выдана

