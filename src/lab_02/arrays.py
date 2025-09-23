#1

# s=list(input().split())
# d=[]
# if len(s)==0:
#     print('ValueError')
# for x in s:
#     if '.' in x:
#         d.append(float(x))
#     else:
#         d.append(int(x))
# print(min(d), max(d))

#2

a=[1.0, 1, 2.5, 2.5, 0]
f=[]
i=[]

for p in a:
    if type(p)==int:
        i.append(p)
    else:
        f.append(p)
res1=[x for x in f if int(x) in i]
res2=[x for x in i if float(x)  not in f]
print(set(sorted(res1+res2+f)))

#3
# a=[[1, 2], [1,0]]
# d=[]
# g=[]
# k=0
# for i in a:
#     for j in i:
#         d.append(j)
#         if type(j)==int:
#             k+=1
#         if k==len(d):
#             g.append(j)
#         else:
#             print('TypeError')
#             break
# if k==len(d):
#     print(g)

