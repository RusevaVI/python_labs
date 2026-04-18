from sem2.lab03.models import PrintedBook, EBook, AudioBook
from collection import Library
from strategies import *


def create_library():
    lib = Library()

    lib.add(PrintedBook("1984", "Orwell", 1949, 300, 500, "hard", 300))
    lib.add(EBook("Dune", "Herbert", 1965, 400, 400, "PDF", 5))
    lib.add(AudioBook("Hobbit", "Tolkien", 1937, 350, 600, 10, "Ivan"))
    lib.add(EBook("F451", "Bradbury", 1953, 200, 350, "EPUB", 2))
    lib.add(PrintedBook("Brave New World", "Huxley", 1932, 280, 450, "soft", 250))

    return lib


# ----------------------
# СЦЕНАРИЙ 1
# ----------------------
def demo_chain():
    print("\nСЦЕНАРИЙ 1: ЦЕПОЧКА\n")

    lib = create_library()

    result = (
        lib
        .filter_by(is_available)
        .sort_by(by_price)
    )

    print("После фильтрации и сортировки:")
    for book in result:
        print(f"{book.title} - {book.price}")

    prices = result.apply(apply_discount(10))
    print("\nПосле скидки 10%:")
    print(prices)


# ----------------------
# СЦЕНАРИЙ 2
# ----------------------
def demo_strategy_change():
    print("\nСЦЕНАРИЙ 2: СМЕНА СТРАТЕГИИ\n")

    lib = create_library()

    cheap = list(filter(make_price_filter(450), lib))
    expensive = list(filter(is_expensive, lib))

    print("Дешевые книги:")
    for b in cheap:
        print(b.title)

    print("\nДорогие книги:")
    for b in expensive:
        print(b.title)


# ----------------------
# СЦЕНАРИЙ 3
# ----------------------
def demo_callable():
    print("\nСЦЕНАРИЙ 3: CALLABLE СТРАТЕГИИ\n")

    lib = create_library()

    discount = DiscountStrategy(10)
    increased = IncreasePriceStrategy(20)

    print("Скидка:")
    print(list(map(discount, lib)))

    print("\nПовышение цены:")
    print(list(map(increased, lib)))



def demo_map():
    print("\nMAP:\n")

    lib = create_library()

    names = list(map(lambda x: x.title, lib))
    print("Названия:", names)


def main():
    demo_chain()
    demo_strategy_change()
    demo_callable()
    demo_map()


if __name__ == "__main__":
    main()