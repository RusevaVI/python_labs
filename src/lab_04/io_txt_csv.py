from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    if p.suffix.lower() != ".txt":
        raise ValueError("Неправильный формат — требуется файл с расширением txt.")
    try:
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {p}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Ошибка декодирования. Попробуйте другую кодировку.")


def write_csv(rows: list[tuple | list],path: str | Path,header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    if p.suffix.lower() != ".csv":
        raise ValueError("Неправильный формат — требуется файл с расширением .csv")

    rows = list(rows)
    if rows:
        length = len(rows[0])
        for r in rows:
            if len(r) != length:
                raise ValueError("Все строки должны иметь одинаковую длину")

    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError("Длина заголовка не совпадает с длиной строк данных")
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
# test1=read_text("data/test1.json")
# write_csv(test1,'data/test1.csv')
# test2=read_text("data/test2.txt")
# write_csv(test2,'data/test2.json')



# def print_csv(path):
#     p=Path(path)
#     #r это read
#     with p.open('r', encoding='utf-8') as f:
#         for line in f:
#             print(line.strip())
# write_csv([], "data/empty.csv", header=("a","b"))
# print_csv("data/empty.csv")
# write_csv([("word","count"),("test",3)], "data/check.csv")
# print_csv("data/check.csv")
# write_csv([("word","count"),("test",3,2)], "data/error.csv")



# Мини-тест

# from pathlib import Path
# cоздаём папку data
# Path("data").mkdir(exist_ok=True)
# cоздаём тестовый текстовый файл input.txt
# Path("data")/ "input.txt".write_text("Привет, мир! Привет!!!", encoding="utf-8")
#
# Чтение текста
txt = read_text(Path("data")/ "input.txt")
print(txt)
# Создание CSV
csv_path = Path("data") / "check.csv"
write_csv([("word", "count"), ("test", 3)], csv_path)
print(csv_path)
# def read_text(path: str | Path, encoding: str = "cp1251") -> str:
#     p = Path(path)
#     return p.read_text(encoding=encoding)
# strcp1251=(read_text("data/inputcp1251.txt",encoding='cp1251'))
# print(strcp1251)
# str_empty=read_text("data/input_empty.txt")
# print(f'выводит:{str_empty}')

#strcp1251_unicodeerror =(read_text("data/inputcp1251.txt",encoding='utf-32'))
#print(strcp1251_unicodeerror)#UnicodeDecodeError
#print(read_text("data/input1.txt"))#FileNotFoundError

