from typing import Any

from exceptions import (
    DuplicateItemError,
    ItemNotFoundError
)


class CLI:

    def __init__(self, app: Any):

        self.app = app

    def print_menu(self) -> None:

        print("""
========== МЕНЮ ==========
1. Добавить книгу
2. Показать книги
3. Найти книгу
4. Удалить книгу
5. Фильтр по цене
6. Сортировка
0. Выход
""")

    def run(self) -> None:
        actions = {
            "1": self.add_book_cli,
            "2": self.show_books_cli,
            "3": self.find_books_cli,
            "4": self.remove_book_cli,
            "5": self.filter_cli,
            "6": self.sort_cli,
        }

        while True:

            self.print_menu()

            choice = input(">>> ").strip()

            if choice == "0":

                print("Выход...")
                break

            action = actions.get(choice)

            if action is None:

                print("Неизвестная команда")
                continue

            action()

    def add_book_cli(self) -> None:

        print("""
1. Бумажная книга
2. Электронная книга
3. Аудиокнига
""")

        book_type = input(
            "Выберите тип книги: "
        ).strip()

        params = {}

        params["title"] = input(
            "Название: "
        ).strip()

        params["author"] = input(
            "Автор: "
        ).strip()

        params["year"] = input(
            "Год: "
        ).strip()

        params["pages"] = input(
            "Страницы: "
        ).strip()

        params["price"] = input(
            "Цена: "
        ).strip()

        if book_type == "1":

            params["cover_type"] = input(
                "Тип обложки: "
            ).strip()

            params["weight"] = input(
                "Вес: "
            ).strip()

        elif book_type == "2":

            params["file_format"] = input(
                "Формат файла: "
            ).strip()

            params["file_size"] = input(
                "Размер файла: "
            ).strip()

        elif book_type == "3":

            params["duration"] = input(
                "Длительность: "
            ).strip()

            params["narrator"] = input(
                "Диктор: "
            ).strip()

        try:

            self.app.create_and_add_book(
                book_type,
                params
            )

            print("Книга добавлена")

        except DuplicateItemError as error:

            print(error)

        except ValueError as error:

            print(f"Ошибка: {error}")

    def show_books_cli(self) -> None:

        books = self.app.get_all_books()

        if not books:

            print("Библиотека пуста")
            return

        print("\n========== КНИГИ ==========")

        for book in books:

            print(book)
            print("-" * 30)

    def find_books_cli(self) -> None:

        title = input(
            "Введите название: "
        ).strip()

        try:

            books = self.app.find_books(title)

            for book in books:

                print(book)
                print("-" * 30)

        except ItemNotFoundError as error:

            print(error)

    def remove_book_cli(self) -> None:

        title = input(
            "Введите название книги: "
        ).strip()

        author = input(
            "Введите автора: "
        ).strip()

        confirm = input(
            f'Удалить "{title}"? (y/n): '
        ).strip().lower()

        if confirm != "y":

            print("Удаление отменено")
            return

        try:

            self.app.remove_book(title, author)

            print("Книга удалена")

        except ItemNotFoundError as error:

            print(error)

    def filter_cli(self) -> None:

        try:

            min_price = float(input(
                "Минимальная цена: "
            ))

            books = self.app.filter_expensive(
                min_price
            )

            for book in books:

                print(book)
                print("-" * 30)


        except ValueError as error:

            print(error)

        except ItemNotFoundError as error:

            print(error)

    def sort_cli(self) -> None:

        print("""
1. По названию
2. По цене
3. По году
""")

        choice = input(
            "Выберите сортировку: "
        ).strip()

        strategy_map = {
            "1": "title",
            "2": "price",
            "3": "year"
        }

        strategy = strategy_map.get(choice)

        if strategy is None:

            print("Неверный выбор")
            return

        books = self.app.sort_books(strategy)

        print("\n========== РЕЗУЛЬТАТ ==========")

        for book in books:

            print(book)
            print("-" * 30)