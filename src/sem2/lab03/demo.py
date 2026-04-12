from collection import Library
from models import PrintedBook, EBook, AudioBook


def demo_inheritance():
    print("\nСЦЕНАРИЙ 1: Наследование и создание объектов\n")

    printed = PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 350)
    ebook = EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5)
    audio = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 11, "Иван Иванов")

    print(printed)
    print()
    print(ebook)
    print()
    print(audio)


def demo_methods():
    print("\nСЦЕНАРИЙ 2: Методы базового и дочерних классов\n")

    printed = PrintedBook("1984", "George Orwell", 1949, 328, 500, "мягкая", 250)
    ebook = EBook("Dune", "Frank Herbert", 1965, 412, 400, "EPUB", 3)
    audio = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 10, "Петр Петров")

    print("Базовый метод borrow():")
    printed.borrow()
    print(f"{printed.title}: {'доступна' if printed.is_available else 'выдана'}")
    printed.return_book()

    print("\nНовые методы дочерних классов:")
    print(f"Доставка печатной книги: {printed.shipping_cost()} руб.")
    print(ebook.download_info())
    print(audio.listen_sample())


def demo_polymorphism():
    print("\nСЦЕНАРИЙ 3: Полиморфизм\n")

    books = [
        PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 350),
        EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5),
        AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 11, "Иван Иванов"),
    ]

    for book in books:
        print(f"{book.title}: стоимость доступа на 5 дней = {book.calculate_access_cost(5)} руб.")

def demo_collection():
    print("\nСЦЕНАРИЙ 4: Работа одной коллекции с разными типами\n")

    library = Library()

    printed = PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 350)
    ebook = EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5)
    audio = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 11, "Иван Иванов")

    library.add(printed)
    library.add(ebook)
    library.add(audio)

    print("Все объекты в коллекции:")
    for item in library:
        print(f"- {item.title} ({item.__class__.__name__})")

    print("\nПроверка типов через isinstance():")
    for item in library:
        if isinstance(item, PrintedBook):
            print(f"{item.title} — печатная книга")
        elif isinstance(item, EBook):
            print(f"{item.title} — электронная книга")
        elif isinstance(item, AudioBook):
            print(f"{item.title} — аудиокнига")


def demo_filter_by_type():
    print("\nСЦЕНАРИЙ 5: Фильтрация по типу\n")

    library = Library()

    library.add(PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 350))
    library.add(EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5))
    library.add(AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 11, "Иван Иванов"))
    library.add(EBook("Fahrenheit 451", "Ray Bradbury", 1953, 256, 350, "EPUB", 2))

    print("Только электронные книги:")
    for book in library.get_only_ebooks():
        print(f"- {book.title}")

    print("\nТолько аудиокниги:")
    for book in library.get_only_audiobooks():
        print(f"- {book.title}")

    print("\nТолько печатные книги:")
    for book in library.get_only_printed():
        print(f"- {book.title}")


def main():
    print("ДЕМОНСТРАЦИЯ ЛР-3")

    demo_inheritance()
    demo_methods()
    demo_polymorphism()
    demo_collection()
    demo_filter_by_type()

    print("\nДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()