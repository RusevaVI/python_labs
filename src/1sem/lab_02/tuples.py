def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec
    fio = fio.strip()
    name = []
    if len(fio) == 0 or len(group) == 0 or type(gpa) != float:
        return "ValueError"
    else:
        for i in fio.split():
            name.append(i.capitalize())
        if len(name) == 3:
            return f"{(name[0])} {(name[1])[0]}.{(name[2])[0]}., гр. {group}, GPA {gpa:.2f}"
        else:
            return f"{(name[0])} {(name[1])[0]}., гр. {group}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "", 5)))
