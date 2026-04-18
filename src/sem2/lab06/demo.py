from container import (
    TypedCollection,
    DisplayCollection,
    ScoreCollection
)

from models import PrintedBook, EBook, AudioBook



def demo_typed_collection():
    print("\nСЦЕНАРИЙ 1: TypedCollection\n")

    books: TypedCollection[PrintedBook] = TypedCollection()

    book1 = PrintedBook(
        "1984",
        "Orwell",
        1949,
        300,
        500,
        "hard",
        300
    )

    books.add(book1)

    for item in books:
        print(item)



def demo_find_filter_map():
    print("\nСЦЕНАРИЙ 2: find / filter / map\n")

    books: TypedCollection[EBook] = TypedCollection()

    books.add(EBook("Dune", "Herbert", 1965, 400, 400, "PDF", 5))
    books.add(EBook("F451", "Bradbury", 1953, 250, 350, "EPUB", 2))
    books.add(EBook("Neuromancer", "Gibson", 1984, 300, 600, "MOBI", 4))

    found = books.find(lambda x: x.price > 500)
    print("Найдена:", found)

    not_found = books.find(lambda x: x.price > 2000)
    print("Не найдено:", not_found)

    filtered = books.filter(lambda x: x.price < 500)

    print("\nПосле filter:")
    for item in filtered:
        print(item)

    names = books.map(lambda x: x.title)
    prices = books.map(lambda x: x.price)

    print("\nmap -> list[str]:")
    print(names)

    print("\nmap -> list[float]:")
    print(prices)



def demo_protocols():
    print("\nСЦЕНАРИЙ 3: Protocol\n")

    display_books = DisplayCollection()

    display_books.add(
        PrintedBook(
            "1984",
            "Orwell",
            1949,
            300,
            500,
            "hard",
            300
        )
    )

    display_books.add(
        AudioBook(
            "Hobbit",
            "Tolkien",
            1937,
            350,
            700,
            10,
            "Ivan"
        )
    )

    print("\nDisplayable объекты:")
    display_books.show_all()

    score_books = ScoreCollection()

    score_books.add(
        EBook(
            "Dune",
            "Herbert",
            1965,
            400,
            400,
            "PDF",
            5
        )
    )

    score_books.add(
        AudioBook(
            "Foundation",
            "Asimov",
            1951,
            320,
            550,
            12,
            "Petr"
        )
    )

    print("\nScorable объекты:")
    score_books.show_scores()


def main():
    demo_typed_collection()
    demo_find_filter_map()
    demo_protocols()


if __name__ == "__main__":
    main()