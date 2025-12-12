import csv
from pathlib import Path
from lab_08.models import Student


class Group:
    FIELDNAMES = ("fio", "birthdate", "group", "gpa")

    def __init__(self, storage_path: str | Path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        self.path.parent.mkdir(parents=True, exist_ok=True) # папка, в которой лежит файл

        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
                writer.writeheader()
            return

        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f) #чтение CSV-файла по строкам.
            header = next(reader, None)#next() берёт первый элемент из reader.

        if header != list(self.FIELDNAMES):
            raise ValueError("Неверный заголовок CSV")

    def _read_all_rows(self):
        with self.path.open("r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))

    def _write_all_rows(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)

    def _row_to_student(self, row: dict) -> Student:
        return Student(
            fio=row["fio"],
            birthdate=row["birthdate"],
            group=row["group"],
            gpa=float(row["gpa"]),
        )

    def _student_to_row(self, student: Student):
        d = student.to_dict()  # доверяем модели Student

        return {
            "fio": str(d["fio"]),
            "birthdate": str(d["birthdate"]),
            "group": str(d["group"]),
            "gpa": str(d["gpa"]),
        }


    def list(self):
        return [self._row_to_student(r) for r in self._read_all_rows()]

    def add(self, student: Student):
        row = self._student_to_row(student)#берёт объект Student и превращает его в словарь
        self._row_to_student(row)  # валидация
        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writerow(row)

    def find(self, substr: str):
        substr = substr.lower()
        return [s for s in self.list() if substr in s.fio.lower()]

    def remove(self, fio: str):
        fio = fio.lower()
        rows = self._read_all_rows()
        new_rows = []
        removed = 0
        for r in rows:
            if r["fio"].lower() == fio:
                removed += 1
            else:
                new_rows.append(r)
        if removed:
            self._write_all_rows(new_rows)

        return removed

    def update(self, fio: str, **fields):#собирает именованные аргументы в словарь
        allowed = set(self.FIELDNAMES)
        for k in fields:
            if k not in allowed:
                raise ValueError(f"Неизвестное поле: {k}")

        fio = fio.lower()
        rows = self._read_all_rows()
        updated = 0

        for row in rows:
            if row["fio"].lower() == fio:
                for k, v in fields.items(): #превращает словарь в последовательность кортежей
                    row[k] = str(v)
                self._row_to_student(row)
                updated += 1

        if updated:
            self._write_all_rows(rows)

        return updated


if __name__ == "__main__":
    g = Group("data1/lab_09/students.csv")
    print("Текущий список студентов:")
    for s in g.list():
        print(" ", s)

    print("\nДобавляем нового студента")
    new_student = Student(
        fio="Банцекина Татьяна",
        birthdate="2007-09-10",
        group="БИВТ-25-7",
        gpa=4.7,
    )
    g.add(new_student)

    print("После добавления:")
    for s in g.list():
        print(" ", s)

    print("\nПоиск по подстроке 'Иван'")
    found = g.find("Иван")
    for s in found:
        print(" ", s)

    print("\nОбновляем gpa у 'Иванов Иван' до 4.9")
    updated_count = g.update("Иванов Иван", gpa=4.9)
    print("Обновлено записей:", updated_count)
    print("Список после обновления:")
    for s in g.list():
        print(" ", s)

    print("\nУдаляем 'Петров Пётр'")
    removed_count = g.remove("Петров Пётр")
    print("Удалено записей:", removed_count)

    print("Итоговый список студентов:")
    for s in g.list():
        print(" ", s)