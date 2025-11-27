## Лабораторная работа 7
### Задание 1
```python
import pytest
from lab_03.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),  # обычный текст
        ("один два два", ["один", "два", "два"]),  # повторы
        ("", []),  # пустая строка
        ("   много   пробелов   ", ["много", "пробелов"]),  # лишние пробелы
    ],
)
def test_tokenize_basic(source, expected):
    tokens = tokenize(source)
    assert tokens == expected


def test_count_freq_and_top_n():
    # базовый и граничный сценарий сразу:
    # нормализуем текст, токенизируем, считаем частоты и берём top_n
    text = "Кот кот собака кот птица собака"
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    # частоты слов
    assert freq == {"кот": 3, "собака": 2, "птица": 1}

    # top_n по убыванию частоты
    top2 = top_n(freq, 2)
    assert top2 == [("кот", 3), ("собака", 2)]


def test_top_n_tie_breaker():
    # одинаковая частота -> сортировка по алфавиту
    freq = {"beta": 2, "alpha": 2, "gamma": 2}

    result = top_n(freq, 3)

    # ожидаем алфавитный порядок при равных значениях
    assert result == [
        ("alpha", 2),
        ("beta", 2),
        ("gamma", 2),
    ]
```

### Задание 2
```python
import csv
import json
from pathlib import Path
import pytest
from lab_05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    # пишем JSON-файл
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # конвертация JSON -> CSV
    json_to_csv(str(src), str(dst))

    # читаем CSV обратно
    with dst.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    # количество записей
    assert len(rows) == 2
    # набор заголовков/ключей
    assert {"name", "age"} <= set(rows[0].keys())
    # значения (age может быть строкой — это ок для CSV)
    assert rows[0]["name"] == "Alice"
    assert rows[1]["name"] == "Bob"


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    fieldnames = ["name", "age"]
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]

    # пишем CSV-файл
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # конвертация CSV -> JSON
    csv_to_json(str(src), str(dst))

    # читаем JSON обратно
    text = dst.read_text(encoding="utf-8")
    data = json.loads(text)

    # это должен быть список словарей
    assert isinstance(data, list)
    assert len(data) == 2
    # набор ключей
    assert {"name", "age"} <= set(data[0].keys())
    # значения (возраст может быть либо строкой, либо числом — нормализуем через int)
    assert data[0]["name"] == "Alice"
    assert int(data[0]["age"]) == 22
    assert data[1]["name"] == "Bob"
    assert int(data[1]["age"]) == 25


# ---------- Негативные сценарии ----------


def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"

    # пустой файл
    src.write_text("", encoding="utf-8")

    # по заданию: пустой/некорректный файл -> ValueError
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"

    # заведомо некорректный JSON
    src.write_text("НЕ json", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"

    # пустой CSV
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


@pytest.mark.parametrize(
    "func, src_name, dst_name",
    [
        (json_to_csv, "missing.json", "out.csv"),
        (csv_to_json, "missing.csv", "out.json"),
    ],
)
def test_conversion_missing_file(tmp_path: Path, func, src_name: str, dst_name: str):
    # файл-источник не существует
    src = tmp_path / src_name  # не создаём
    dst = tmp_path / dst_name

    with pytest.raises(FileNotFoundError):
        func(str(src), str(dst))
```
### pyproject.toml
```python
[build-system]
requires = ["setuptools>=77.0.3"]
build-backend = "setuptools.build_meta"

[project]
name = "python-labs"
version = "0.1.0"
description = "Учебный Python-проект для лабораторных работ (ЛР7: pytest + black)"
readme = "README.md"
requires-python = ">=3.11"

# runtime-зависимости (в ЛР можно оставить пустым)
dependencies = []

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "pytest-cov>=5.0",
  "black>=24.0",
  "ruff>=0.6",
]

# ---- pytest ----
[tool.pytest.ini_options]
# чтобы импорты вида `from lab_03.text import ...` работали
pythonpath = ["src"]
addopts = "-ra"

# ---- black ----
[tool.black]
line-length = 88
target-version = ["py311"]
exclude = '''
(
  ^\.venv/
  | ^images/
  | ^build/
  | ^dist/
)
'''

# ---- coverage (для pytest-cov) ----
[tool.coverage.run]
source = ["src"]
branch = true
```
### Запуски

[Картинка 1] ![7.1.png](images/7.1.png)

[Картинка 2] ![7.2.png](images/7.2.png)

[Картинка 3] ![7.3.png](images/7.3.png)

[Картинка 4] ![7.4.png](images/7.4.png)
