from typing import List, Optional

def build_roster(names: List[Optional[str]], extra: Optional[List[str]] = None) -> List[str]:
    if extra is None:
        extra = []
    # убираем None, пробелы и приводим к Title
    cleaned = [n.strip().title() for n in names if n is not None]
    cleaned += [e.strip().title() for e in extra if e is not None]
    # убираем дубли, сохраняем порядок
    merged = list(dict.fromkeys(cleaned))
    return merged

def main():
    students = ["  иванов", "Петров  ", None, "сидорова"]
    extra = ["смирнов"]   # делаем список, а не строку
    students.extend(extra)  # корректное добавление
    roster = build_roster(students, extra)
    print("Исходный students:", students)
    print("Результат roster:", roster)
    print("Длина исходного:", len(students))
    print("Длина результата:", len(roster))

if __name__ == "__main__":
    main()