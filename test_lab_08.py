from src.lab_08.serialize import students_to_json, students_from_json

students = students_from_json("data1/lab_08/students_input.json")

students_to_json(students, "data1/lab_08/students_output.json")

for s in students:
    print(s, "| age:", s.age())