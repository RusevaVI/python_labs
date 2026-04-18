def by_title(book):
    return book.title.lower()


def by_price(book):
    return book.price


def by_year(book):
    return book.year


def by_title_then_price(book):
    return (book.title.lower(), book.price)


def is_expensive(book):
    return book.price > 500


def is_available(book):
    return book.is_available


def make_price_filter(max_price):
    def filter_fn(book):
        return book.price <= max_price
    return filter_fn


def to_title(book):
    return book.title


def apply_discount(percent):
    def discount(book):
        return round(book.price * (1 - percent / 100), 2)
    return discount


class DiscountStrategy:
    def __init__(self, percent):
        self.percent = percent

    def __call__(self, book):
        return round(book.price * (1 - self.percent / 100), 2)


class IncreasePriceStrategy:
    def __init__(self, percent):
        self.percent = percent

    def __call__(self, book):
        return round(book.price * (1 + self.percent / 100), 2)