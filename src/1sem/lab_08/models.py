from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self) -> None: #это место, чтобы проверять данные.

        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError :
            raise ValueError("birthdate должна быть в формате YYYY-MM-DD")

        try:
            self.gpa = float(self.gpa)
        except ValueError :
            raise ValueError("gpa должен быть число")

        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa вышел за пределы")


    def age(self) -> int: #self это конкретный студент
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        #datetime.strptime — это функция, которая превращает строку → в дату по заданному формату
        #.date() превращает datetime → в чистую дату.
        today = date.today()

        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Student": #метод вызывается у класса, а не у объекта
    #первый аргумент будет не self, а cls (ссылка на сам класс)
    #d: dict Просто подсказка, что передается словарь:
        """Десериализация из словаря в объект Student."""
        if not isinstance(d, dict):
            raise TypeError("Student.from_dict не словарь")

        required = ("fio", "birthdate", "group", "gpa") # Проверка обязательных ключей
        missing = [k for k in required if k not in d]
        if missing:
            raise KeyError('недостаточно ключей')

        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self) -> str:
        """Красивый вывод объекта."""
        return (
            f"Student(fio='{self.fio}', group='{self.group}', "
            f"gpa={self.gpa:.2f}, birthdate={self.birthdate})"
        )