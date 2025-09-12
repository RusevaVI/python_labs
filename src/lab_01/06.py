n=int(input())
print(f'in_1: {n}')
k=1
tr=0
fl=0
for i in range(n):
    k+=1
    name=str(input())
    vs=int(input())
    bl=str(input())
    print(f'in_{k}: {name} {vs} {bl}')
    if bl=='True':
        tr+=1
    else:
        fl+=1
print(f'out: {tr} {fl}')