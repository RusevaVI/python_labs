import argparse
from python_labs.src.lab_03.text import (
    tokenize,
    count_freq,
    top_n,
)  # пример функции из ЛР3


def main():
    parser = argparse.ArgumentParser(description="CLI для анализа текста")
    subparsers = parser.add_subparsers(dest="command")

    # cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    # action="store_true"делает аргумент флагом, который становится True, если он есть в командной строке, и False, если его нет.
    # stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Сколько топ слов показать"
    )

    args = (
        parser.parse_args()
    )  # происходит разбор аргументов командной строки и создание объекта Python, где каждый аргумент доступен как атрибут.

    if args.command == "cat":
        with open(args.input, encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if args.n:
                    print(
                        f"{i}: {line.rstrip()}"
                    )  # удаляет символ переноса строки \n справа, чтобы строки не дублировались при печати.
                else:
                    print(line.rstrip())

    elif args.command == "stats":
        with open(args.input, encoding="utf-8") as f:
            text = f.read()
        tokens = tokenize(text)
        freqs = count_freq(tokens)
        for word, count in top_n(freqs, args.top):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
