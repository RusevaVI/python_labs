from base import Book


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, price, cover_type, weight):
        super().__init__(title, author, year, pages, price)
        self._cover_type = cover_type
        self._weight = weight

    @property
    def cover_type(self):
        return self._cover_type

    @property
    def weight(self):
        return self._weight

    def shipping_cost(self):
        return round(self._weight * 0.5, 2)

    def calculate_access_cost(self, days):
        return round(self.calculate_rental_price(days) + self.shipping_cost(), 2)

    def __str__(self):
        return (
            f"[Печатная книга]\n"
            f"{super().__str__()}\n"
            f"Тип обложки: {self._cover_type}\n"
            f"Вес: {self._weight} г"
        )


class EBook(Book):
    def __init__(self, title, author, year, pages, price, file_format, file_size):
        super().__init__(title, author, year, pages, price)
        self._file_format = file_format
        self._file_size = file_size

    @property
    def file_format(self):
        return self._file_format

    @property
    def file_size(self):
        return self._file_size

    def download_info(self):
        return f"Файл {self._file_format}, размер {self._file_size} МБ"

    def calculate_access_cost(self, days):
        return round(self.price * 0.01 * days, 2)

    def __str__(self):
        return (
            f"[Электронная книга]\n"
            f"{super().__str__()}\n"
            f"Формат: {self._file_format}\n"
            f"Размер файла: {self._file_size} МБ"
        )


class AudioBook(Book):
    def __init__(self, title, author, year, pages, price, duration, narrator):
        super().__init__(title, author, year, pages, price)
        self._duration = duration
        self._narrator = narrator

    @property
    def duration(self):
        return self._duration

    @property
    def narrator(self):
        return self._narrator

    def listen_sample(self):
        return f"Доступен фрагмент аудиокниги в исполнении {self._narrator}"

    def calculate_access_cost(self, days):
        return round(self.price * 0.015 * days, 2)

    def __str__(self):
        return (
            f"[Аудиокнига]\n"
            f"{super().__str__()}\n"
            f"Длительность: {self._duration} ч\n"
            f"Читает: {self._narrator}"
        )