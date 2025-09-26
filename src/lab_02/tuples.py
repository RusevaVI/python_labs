def f(fio,group,gpa):
    fio = fio.strip()
    name=[]
    if len(fio)==0 or len(group)==0 or type(gpa)!=float:
        return "ValueError"
    else:
        for i in fio.split():
            name.append(i.capitalize())

        if len(name)==3:
            return (f'{(name[0])} {(name[1])[0]}.{(name[2])[0]}., гр. {group}, GPA {gpa:.2f}')
        else:
            return (f'{(name[0])} {(name[1])[0]}., гр. {group}, GPA {gpa:.2f}')
print(f("Иванов Иван Иванович", "BIVT-25", 4.6))
print(f("Петров Пётр", "IKBO-12", 5.0))
print(f("Петров Пётр Петрович", "IKBO-12", 5.0))
print(f("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
print(f("", "", 5))

