#1

# s=list(map(int,input().split()))
# if len(s)==0:
#     print('ValueError')
# else:
#     print(min(s),max(s))
# print(sorted(set(s)))

#2
# s=list(input().split())
# print(sorted(set(s)))

#3
a=[[1, 2], [1,0]]
d=[]
g=[]
k=0
for i in a:
    for j in i:
        d.append(j)
        if type(j)==int:
            k+=1
        if k==len(d):
            g.append(j)
        else:
            print('TypeError')
            break
if k==len(d):
    print(g)

