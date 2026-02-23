name = str(input("ФИО: "))
print(f"Инициалы: {(name.split()[0])[0]}{(name.split()[1])[0]}{(name.split()[2])[0]}.")
name = name.replace(" ", "")
print(f"Длиsна (символов):{len(name)+2}")
