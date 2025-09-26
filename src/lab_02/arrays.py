#1
a=[3,-1,5,5,0]
b=[42]
c=[-5, -2, -9]
d=[]
e=[1.5, 2, 2.0, -3.1]
def f(b):
    s1=[]
    for i in b:
        s1.append(i)
    if len(s1)==0:
        print('ValueError')
    else:
        s2=(min(s1),max(s1))
        print(s2)
    return ''
print(f(a))
print(f(b))
print(f(c))
print(f(d))
print(f(e))

#2

a=[3, 1, 2, 1, 3]
b=[]
c=[-1, -1, 0, 2, 2]
d=[1.0, 1, 2.5, 2.5, 0]
def f(l):
    i=[]
    f=[]
    for g in l:
        if type(g)==int:
            i.append(g)
        else:
            f.append(g)
    res1 = [x for x in f if int(x) in i]
    res2 = [x for x in i if float(x)  not in f]
    print(sorted(set(res1+res2+f)))
    return ''
print(f(a))
print(f(b))
print(f(c))
print(f(d))

# #3
a=[[1, 2], [3, 4]]
b=([1, 2], (3, 4, 5))
c=[[1], [], [2, 3]]
d=[[1, 2], "ab"]

def f(a):
    x=[]
    y=[]
    k=0
    for i in a:
        for b in i:
            x.append(b)
            if type(b)==int:
                k+=1
            if k==len(x):
                y.append(b)
            else:
                print('TypeError')
                break
    if k==len(x):
        print(y)
    return ''

print(f(a))
print(f(b))
print(f(c))
print(f(d))