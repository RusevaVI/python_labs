from interfaces import Printable, Rentable
from models import Book, PrintedBook, EBook, AudioBook
from collection import Library


def print_all(items: list[Printable]):
    print("\nВывод через интерфейс Printable:")
    for item in items:
        print(item.to_string())
        print()


def show_access_cost(items: list[Rentable], days: int):
    print(f"\nРасчёт стоимости доступа на {days} дней через интерфейс Rentable:")
    for item in items:
        print(f"{item.title}: {item.calculate_access_cost(days)} руб.")


def demo_interfaces():
    print("\nСЦЕНАРИЙ 1: Работа интерфейсных методов\n")

    printed = PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 300)
    ebook = EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5)
    audio = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 10, "Иван Иванов")

    print(printed.to_string())
    print()
    print(ebook.to_string())
    print()
    print(audio.to_string())

    print(f"\nPrintedBook: {printed.calculate_access_cost(5)} руб.")
    print(f"EBook: {ebook.calculate_access_cost(5)} руб.")
    print(f"AudioBook: {audio.calculate_access_cost(5)} руб.")


def demo_interface_functions():
    print("\nСЦЕНАРИЙ 2: Универсальные функции через интерфейс\n")

    items = [
        PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 300),
        EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5),
        AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 10, "Иван Иванов"),
    ]

    print_all(items)
    show_access_cost(items, 5)


def demo_isinstance_and_collection():
    print("\nСЦЕНАРИЙ 3: Коллекция и проверка интерфейсов\n")

    library = Library()

    printed = PrintedBook("1984", "George Orwell", 1949, 328, 500, "твердая", 300)
    ebook = EBook("Dune", "Frank Herbert", 1965, 412, 400, "PDF", 5)
    audio = AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 310, 600, 10, "Иван Иванов")

    library.add(printed)
    library.add(ebook)
    library.add(audio)

    print("Проверка через isinstance:")
    for item in library:
        print(
            f"{item.title}: "
            f"Printable = {isinstance(item, Printable)}, "
            f"Rentable = {isinstance(item, Rentable)}"
        )

    print("\nФильтрация коллекции по интерфейсу Printable:")
    for item in library.get_printable():
        print(f"- {item.title}")

    print("\nФильтрация коллекции по интерфейсу Rentable:")
    for item in library.get_rentable():
        print(f"- {item.title}")

    print("\nПолиморфизм через интерфейс без условий:")
    for item in library.get_rentable():
        print(f"{item.title}: {item.calculate_access_cost(3)} руб.")


def main():
    print("ДЕМОНСТРАЦИЯ ЛР-4")

    demo_interfaces()
    demo_interface_functions()
    demo_isinstance_and_collection()

    print("\nДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()