from model import Book

# Сценарий 1 — создание объекта
book1 = Book("1984", "George Orwell", 1949, 328, 500)
print(book1)

# Сценарий 2 — сравнение объектов
book2 = Book("1984", "George Orwell", 1949, 328, 600)
print("\nКниги равны?", book1 == book2)

# Сценарий 3 — изменение через setter
book1.price = 450
print("\nНовая цена:", book1.price)

# Проверка ограничения состояния
book1.borrow()
print("\nПосле выдачи:")
print(book1)

try:
    book1.borrow()
except ValueError as e:
    print("\nОшибка:", e)

# Демонстрация валидации
try:
    bad_book = Book("", "Автор", -10, 0, -100)
except ValueError as e:
    print("\nОшибка создания:", e)

# Атрибут класса
print("\nВсего создано книг:", Book.total_books)
print("Доступ через экземпляр:", book1.total_books)