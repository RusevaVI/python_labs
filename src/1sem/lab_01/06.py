n = int(input("in_1: "))
k = 1
tr = 0
fl = 0
for i in range(n):
    k += 1
    name_1, name_2, vs, bl = (input(f"in_{k}: ")).split()
    if bl == "True":
        tr += 1
    else:
        fl += 1
print(f"out: {tr} {fl}")
