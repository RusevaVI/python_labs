import json

# чтобы работало и как модуль, и при прямом запуске файла:
try:
    from .models import Student
except ImportError:
    from models import Student  # type: ignore


def students_to_json(students: list[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON-файл.

    :param students: список объектов Student
    :param path: путь к JSON-файлу
    """
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[Student]:
    """
    Читает JSON-файл и возвращает список Student.

    :param path: путь к JSON-файлу
    :return: список объектов Student
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f) #читает текст и превращает его в Python-объект.

    if not isinstance(raw, list):
        raise ValueError("JSON содержит не список")

    students: list[Student] = []
    for item in raw:
        students.append(Student.from_dict(item))
    return students