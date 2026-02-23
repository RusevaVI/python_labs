import argparse  # для создания CLI: парсит аргументы, строит help, обрабатывает ошибки ввода.
import os  # используется для проверки существования файла (os.path.exists).
from python_labs.src.lab_05.json_csv import json_to_csv, csv_to_json
from python_labs.src.lab_05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(
        description="Конвертеры данных"
    )  # Создаётся объект ArgumentParser с текстом описания.
    sub = parser.add_subparsers(
        dest="cmd", required=True
    )  # add_subparsers создаёт подкоманды (subcommands) — это позволяет командам вида script.py json2csv
    # dest="cmd" — имя атрибута в args, куда будет записано название выбранной подкоманды.
    # required=True — делает подкоманду обязательной

    # --- json2csv ---
    p1 = sub.add_parser(
        "json2csv", help="Конвертировать JSON → CSV"
    )  # add_parser добавляет новую подкоманду в парсер.
    p1.add_argument(
        "--in", dest="input", required=True, help="Путь к входному JSON-файлу"
    )  # •	--in — флаг, который пользователь пишет в командной строке,dest="input" — имя, под которым значение будет храниться в args.
    p1.add_argument(
        "--out", dest="output", required=True, help="Путь для сохранения CSV-файла"
    )

    # --- csv2json ---
    p2 = sub.add_parser("csv2json", help="Конвертировать CSV → JSON")
    p2.add_argument(
        "--in", dest="input", required=True, help="Путь к входному CSV-файлу"
    )
    p2.add_argument(
        "--out", dest="output", required=True, help="Путь для сохранения JSON-файла"
    )

    # --- csv2xlsx ---
    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV → XLSX")
    p3.add_argument(
        "--in", dest="input", required=True, help="Путь к входному CSV-файлу"
    )
    p3.add_argument(
        "--out", dest="output", required=True, help="Путь для сохранения XLSX-файла"
    )

    args = (
        parser.parse_args()
    )  # происходит разбор аргументов командной строки и создание объекта Python, где каждый аргумент доступен как атрибут.

    # --- Проверяем, что входной файл существует ---
    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Входной файл '{args.input}' не найден.")

    # --- Проверяем, что указан выходной файл ---
    if not args.output:
        parser.error("Не указан выходной файл (--out).")

    # === Выполнение подкоманды ===
    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
    else:
        parser.error("Неизвестная команда. Используйте --help для справки.")


if (
    __name__ == "__main__"
):  # который проверяет, запущен ли скрипт напрямую или импортирован как модуль.
    main()
