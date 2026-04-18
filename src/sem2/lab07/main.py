from app import LibraryApp
from cli import CLI
from storage import load, save


FILEPATH = "books.json"

def main() -> None:

    books = load(FILEPATH)
    app = LibraryApp()

    for book in books:
        app.library.add(book)
    cli = CLI(app)
    cli.run()

    save(app.get_all_books(), FILEPATH)

if __name__ == "__main__":
    main()