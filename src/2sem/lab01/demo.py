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

    print("\nПроверка зависимости от состояния (попытка изменить цену выданной книги):")
    try:
        book1.price = 1500
    except ValueError as e:
        print(f"Ошибка логики состояния: {e}")

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