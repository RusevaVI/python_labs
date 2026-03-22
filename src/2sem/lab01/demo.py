from model import Book

print("=== СЦЕНАРИЙ 1: СОЗДАНИЕ И СРАВНЕНИЕ ===")
b1 = Book("Война и мир", "Лев Толстой", 1869, 1225, 1200)
b2 = Book("Война и мир", "Лев Толстой", 1869, 1225, 1200)
b3 = Book("1984", "Джордж Оруэлл", 1949, 328, 800)

print(b1)
print(f"Отладочное представление: {repr(b1)}")
print("Сравнение (b1 == b2):", b1 == b2)
print("Сравнение (b1 == b3):", b1 == b3)

print("\n=== СЦЕНАРИЙ 2: ВАЛИДАЦИЯ ПРИ СОЗДАНИИ ===")
try:
    bad_book = Book("", "Автор", 2026, -10, -500)
except Exception as e:
    print(f"Ошибка валидации: {e}")

print("\n=== СЦЕНАРИЙ 3: ЛОГИЧЕСКОЕ СОСТОЯНИЕ (ВЫДАЧА) ===")
print(f"Доступна до выдачи: {b1.is_available}")
b1.borrow()
print(f"Доступна после borrow(): {b1.is_available}")

try:
    b1.borrow() # Повторная выдача
except Exception as e:
    print(f"Ошибка состояния: {e}")

print("\n=== СЦЕНАРИЙ 4: ОГРАНИЧЕНИЯ СОСТОЯНИЯ ===")
# Нельзя менять цену или считать аренду, если книга выдана
try:
    b1.price = 2000
except Exception as e:
    print(f"Ошибка (изменение цены): {e}")

try:
    b1.calculate_rental_price(5)
except Exception as e:
    print(f"Ошибка (расчет аренды): {e}")

b1.return_book()
print("Книга возвращена. Теперь расчет аренды на 5 дней:", b1.calculate_rental_price(5))

print("\n=== СЦЕНАРИЙ 5: БИЗНЕС-ЛОГИКА (СКИДКИ) ===")
print(f"Цена до скидки: {b3.price}")
b3.discount(15)
print(f"Цена после скидки 15%: {b3.price}")

print("\n=== СЦЕНАРИЙ 6: АТРИБУТЫ КЛАССА ===")
print(f"Всего книг в системе (через класс): {Book.total_books}")
print(f"Всего книг в системе (через объект): {b3.total_books}")