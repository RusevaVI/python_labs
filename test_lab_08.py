from src.lab_08.serialize import students_to_json, students_from_json

# 1. читаем студентов из входного JSON
students = students_from_json("data1/lab08/students_input.json")

# 2. пишем в выходной JSON
students_to_json(students, "data1/lab08/students_output.json")

# 3. выводим на экран для проверки
for s in students:
    print(s, "| age:", s.age())