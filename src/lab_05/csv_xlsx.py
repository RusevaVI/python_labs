from pathlib import Path
import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    p_csv = Path(csv_path)
    p_xlsx = Path(xlsx_path)
    # Проверки путей
    if p_csv.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")
    if p_xlsx.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается файл с расширением .xlsx")

    if not p_csv.exists():
        raise FileNotFoundError("Файл CSV не найден")

    # Чтение CSV
    with p_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Проверка содержимого
    if not rows or all(not any(row) for row in rows):
        raise ValueError("Пустой CSV или неподдерживаемая структура")

    # Создание XLSX
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина
    for column_cells in ws.columns:
        max_len = max((len(str(cell.value)) if cell.value else 0) for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = max(max_len + 2, 8)

    # Проверка директории назначения
    if not p_xlsx.parent.exists():
        raise FileNotFoundError(f"Директория для XLSX не найдена")

    # Сохранение
    wb.save(p_xlsx)
# if __name__ == "__main__":
#     from pathlib import Path
#     import csv
#
#     # --- Конвертация people.csv → people.xlsx ---
#     csv_to_xlsx("data2/samples/people.csv", "data2/out/people.xlsx")
#     print("✅ CSV 'people.csv' успешно преобразован в XLSX!")
#
#     # --- Конвертация cities.csv → cities.xlsx ---
#     csv_input = Path("data2/samples/cities.csv")
#     xlsx_output = Path("data2/out/cities.xlsx")
#
#     # Создаём папку out, если её нет
#     xlsx_output.parent.mkdir(parents=True, exist_ok=True)
#
#     # Если CSV нет — создаём примерный
#     if not csv_input.exists():
#         csv_input.parent.mkdir(parents=True, exist_ok=True)
#         example_rows = [
#             ["city", "country", "population"],
#             ["Moscow", "Russia", "12655050"],
#             ["Saint Petersburg", "Russia", "5384342"],
#             ["Kazan", "Russia", "1300000"]
#         ]
#         with csv_input.open("w", newline="", encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerows(example_rows)
#         print(f"Создан примерный CSV файл: {csv_input}")
#
#     # Конвертация CSV → XLSX
#     csv_to_xlsx(csv_input, xlsx_output)
#     print("✅ CSV 'cities.csv' успешно преобразован в XLSX!")

#csv_to_xlsx("data2/samples/people_empty.csv", "data2/samples/people2.xlsx")
#csv_to_xlsx("data2/samples/people_NO_file.csv", "data/samples/people3.xlsx")
#csv_to_xlsx("data2/samples/tupy.csv", "data/samples/people3.json")

