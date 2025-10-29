from pathlib import Path
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    p_json = Path(json_path)
    p_csv = Path(csv_path)

    #Проверка расширений
    if p_json.suffix.lower() != ".json":
        raise ValueError("Ожидается файл с расширением .json")
    if p_csv.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    #Проверка существования JSON
    if not p_json.exists():
        raise FileNotFoundError("Файл JSON не найден")

    # Проверка существования директории для CSV
    if not p_csv.parent.exists():
        raise FileNotFoundError(f"Директория для CSV не найдена")

    # Чтение JSON
    try:
        data = json.loads(p_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError("Ошибка чтения JSON")

    # Проверка структуры
    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список словарей")

    # Определяем все возможные ключи
    all_keys = list(data[0].keys())
    for d in data[1:]:
        for k in d.keys():
            if k not in all_keys:
                all_keys.append(k)

    # Запись CSV
    with p_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys)
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in all_keys})

    # Проверка количества строк
    with p_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        csv_data = list(reader)
        if len(csv_data) != len(data):
            raise ValueError("Количество записей не совпадает после конвертации")


def csv_to_json(csv_path: str, json_path: str) -> None:
    p_csv = Path(csv_path)
    p_json = Path(json_path)

    # Проверка расширений
    if p_csv.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")
    if p_json.suffix.lower() != ".json":
        raise ValueError("Ожидается файл с расширением .json")

    # Проверка существования CSV
    if not p_csv.exists():
        raise FileNotFoundError("Файл CSV не найден")

    # Проверка директории для JSON
    if not p_json.parent.exists():
        raise FileNotFoundError(f"Директория для JSON не найдена")

    # Чтение CSV
    with p_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV должен содержать заголовок")
        data = [row for row in reader]

    if not data:
        raise ValueError("CSV пустой")

    # Запись JSON
    with p_json.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Проверка совпадения количества записей
    reread = json.loads(p_json.read_text(encoding="utf-8"))
    if len(reread) != len(data):
        raise ValueError("Количество записей не совпадает после конвертации")

# ✅ Пример использования (тест)
# if __name__ == "__main__":
#     data_dir = Path("data2/samples")
#     out_dir = Path("data2/out")
#
#     data_dir.mkdir(parents=True, exist_ok=True)
#     out_dir.mkdir(parents=True, exist_ok=True)
#
#     json_file = data_dir / "people.json"
#     csv_file = out_dir / "people_from_json.csv"
#     json_back = out_dir / "people_from_csv.json"
#
#     # --- Пример исходных данных ---
#     people = [
#         {"name": "Alice", "age": 22},
#         {"name": "Bob", "age": 25},
#         {"name": "John"}
#     ]
#
#     # --- Запись примера JSON ---
#     json_file.write_text(json.dumps(people, ensure_ascii=False, indent=2), encoding="utf-8")
#
#     # --- Конвертация JSON → CSV ---
#     json_to_csv(json_file, csv_file)
#
#     # --- Конвертация CSV → JSON ---
#     csv_to_json(csv_file, json_back)
#
#json_to_csv("data2/samples/people.json", "data2/samples/people.csv")
#json_to_csv("data2/samples/people_empty.json", "data2/samples/people2.csv")
#json_to_csv("data2/samples/people_test.text", "data2/people2.csv")
#json_to_csv("data2/people_NO_file.json", "data/people3.csv")
#csv_to_json("data2/samples/people.json", "data2/samples/people.csv")
#csv_to_json("data2/samples/people_empty.csv", "data2/samples/people2.json")
# csv_to_json("data2/samples/people_test.text", "data2/people2.csv")
#csv_to_json("data2/samples/people_NO_file.csv", "data/people3.json")
#json_to_csv("data2/samples/test1.json", "data2/samples/people.csv")
