from datetime import datetime

def validate_title(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Название должно быть непустой строкой")


def validate_author(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Автор должен быть непустой строкой")


def validate_year(value):
    current_year = datetime.now().year
    if not isinstance(value, int) or value < 0 or value > current_year:
        raise ValueError("Год издания должен быть корректным числом")


def validate_pages(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Количество страниц должно быть больше 0")


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")