from src.lab_08.models import Student

Student.from_dict("не словарь")
Student.from_dict(123)
Student.from_dict(["fio", "group"])