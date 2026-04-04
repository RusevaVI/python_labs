"""Демонстрация работы коллекции Library"""

from model import Book
from collection import Library


def demo_basic_operations():
    print("\nСЦЕНАРИЙ 1: Базовые операции\n")

    library = Library()
    print("Создана пустая библиотека")

    book1 = Book("1984", "George Orwell", 1949, 328, 500)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, 310, 700)
    book3 = Book("Dune", "Frank Herbert", 1965, 412, 900)

    print("Созданы книги:")
    print(f"  - {book1.title} ({book1.price} руб.)")
    print(f"  - {book2.title} ({book2.price} руб.)")
    print(f"  - {book3.title} ({book3.price} руб.)")

    library.add(book1)
    library.add(book2)
    library.add(book3)
    print("\nКниги добавлены в библиотеку")

    print("\nВсе книги:")
    for i, book in enumerate(library):
        print(f"  [{i}] {book.title} - {book.price} руб.")

    library.remove(book2)
    print(f"\nКнига '{book2.title}' удалена")

    print("\nПосле удаления:")
    for i, book in enumerate(library):
        print(f"  [{i}] {book.title}")

    try:
        library.add("не книга")
    except TypeError as e:
        print(f"\nОшибка: {e}")


def demo_search():
    print("\nСЦЕНАРИЙ 2: Поиск\n")

    library = Library()

    books = [
        Book("1984", "George Orwell", 1949, 328, 500),
        Book("Animal Farm", "George Orwell", 1945, 140, 350),
        Book("Dune", "Frank Herbert", 1965, 412, 900),
    ]

    for book in books:
        library.add(book)

    print("Исходная библиотека:")
    for book in library:
        print(f"  - {book.title} ({book.author}, {book.year})")

    print("\nПоиск по названию '1984':")
    found_by_title = library.find_by_title("1984")
    for book in found_by_title:
        print(f"  - {book.title}")

    print("\nПоиск по автору 'George Orwell':")
    found_by_author = library.find_by_author("George Orwell")
    for book in found_by_author:
        print(f"  - {book.title}")

    print("\nПоиск по году 1945:")
    found_by_year = library.find_by_year(1945)
    for book in found_by_year:
        print(f"  - {book.title}")

    print(f"\nКоличество книг в библиотеке: {len(library)}")

    print("\nПеребор через for:")
    for i, book in enumerate(library):
        print(f"  {i + 1}. {book.title} - {book.author}")


def demo_indexing():
    print("\nСЦЕНАРИЙ 3: Индексация\n")

    library = Library()

    books = [
        Book("Dune", "Frank Herbert", 1965, 412, 900),
        Book("1984", "George Orwell", 1949, 328, 500),
        Book("The Hobbit", "J.R.R. Tolkien", 1937, 310, 700),
    ]

    for book in books:
        library.add(book)

    print("Доступ по индексу:")
    for i in range(len(library)):
        print(f"  [{i}] {library[i].title}")

    removed_book = library[1]
    library.remove_at(1)
    print(f"\nУдалена книга по индексу 1: {removed_book.title}")

    print("\nКоллекция после удаления:")
    for i, book in enumerate(library):
        print(f"  [{i}] {book.title}")


def demo_filtration():
    print("\nСЦЕНАРИЙ 4: Фильтрация коллекции\n")

    library = Library()

    book1 = Book("1984", "George Orwell", 1949, 328, 500)
    book2 = Book("Dune", "Frank Herbert", 1965, 412, 900)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937, 310, 700)

    book2.borrow()

    library.add(book1)
    library.add(book2)
    library.add(book3)

    print("Все книги:")
    for book in library:
        status = "доступна" if book.is_available else "выдана"
        print(f"  - {book.title} ({status})")

    available_books = library.get_available()
    print("\nДоступные книги:")
    for book in available_books:
        print(f"  - {book.title}")

    unavailable_books = library.get_unavailable()
    print("\nВыданные книги:")
    for book in unavailable_books:
        print(f"  - {book.title}")

    expensive_books = library.get_expensive(600)
    print("\nДорогие книги (от 600 руб.):")
    for book in expensive_books:
        print(f"  - {book.title} ({book.price} руб.)")


def demo_business_logic():
    print("\nСЦЕНАРИЙ 5: Бизнес-логика\n")

    library = Library()

    book1 = Book("Dune", "Frank Herbert", 1965, 412, 900)
    book2 = Book("1984", "George Orwell", 1949, 328, 500)

    library.add(book1)
    library.add(book2)

    print("Начальное состояние книг:")
    for book in library:
        status = "доступна" if book.is_available else "выдана"
        print(f"  - {book.title}: {status}")

    print("\nВыдаём книгу 'Dune'...")
    book1.borrow()

    print("Состояние после выдачи:")
    for book in library:
        status = "доступна" if book.is_available else "выдана"
        print(f"  - {book.title}: {status}")

    print("\nВозвращаем книгу 'Dune'...")
    book1.return_book()

    print("Состояние после возврата:")
    for book in library:
        status = "доступна" if book.is_available else "выдана"
        print(f"  - {book.title}: {status}")

    print("\nАнализ доступности книг:")
    print(f"  Доступных книг: {len(library.get_available())}")
    print(f"  Выданных книг: {len(library.get_unavailable())}")


def main():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КОЛЛЕКЦИИ LIBRARY")

    demo_basic_operations()
    demo_search()
    demo_indexing()
    demo_filtration()
    demo_business_logic()

    print("\nДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()