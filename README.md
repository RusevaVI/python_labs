# RusevaVI
## Лабораторная работа 1
### Задание 1
```python
name=str(input("имя "))
vs=int(input("возраст "))
print(f"Привет,{name}!Через год тебе будет {vs+1}.")
```
[Картинка 1]![01.png](images/01.png)

### Задание 2
```python
a=(input('a: '))
a=a.replace(',','.')
a=float(a)
b=(input('b: '))
b=b.replace(',','.')
b=float(b)
print(f"sum={a+b}; avg={(a+b)/2:.2f}")
```
[Картинка 1]![02.png](images/02.png)

### Задание 3
```python
price=float(input('цена, p: '))
discount=float(input('скидка, %: '))
vat=float(input('ндс, %: '))
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f"база после скидки:{base:.2f} p")
print(f'ндс:{vat_amount:.2f} p')
print(f'итого к оплате:{total:.2f} p')
```
[Картинка 1]![03.png](images/03.png)

### Задание 4
```python
m=int(input('минуты: '))
print(f'{m//60}:{m-(60*(m//60)):02d}')
```
[Картинка 1]![04.png](images/04.png)

### Задание 5
```python
name=str(input('ФИО: '))
print(f'Инициалы: {(name.split()[0])[0]}{(name.split()[1])[0]}{(name.split()[2])[0]}.')
name =name.replace(' ','')
print(f'Длина (символов):{len(name)+2}')
```
[Картинка 1] ![05.png](images/05.png)

### Задание 6
```python
n=int(input('in_1: '))
k=1
tr=0
fl=0
for i in range(n):
    k+=1
    name_1, name_2, vs, bl = (input(f'in_{k}: ')).split()
    if bl=='True':
        tr+=1
    else:
        fl+=1
print(f'out: {tr} {fl}')
```
[Картинка 1] ![06.png](images/06.png)

### Задание 7
```python
s=str(input('in: '))
word=[]
id_1=0
id_2=0
id_p=0
for i in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    if i in s:
        id_1=s.index(i)
for j in '0123456789':
    if (j in s):
        id_2=s.index(j)+1
        break
id_p=s.index('.')
zar=id_2-id_1
for i in range(id_1,id_p+1,zar):
    word.append(s[i])
print(f'out:{''.join(word)}')
```
[Картинка 1] ![07.png](images/07.png)

## Лабораторная работа 2
### Задание 1
```python
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
```
[Картинка 1] ![1.1.png](images/1.1.png)
[Картинка 2] ![1.2.png](images/1.2.png)
[Картинка 3] ![1.3.png](images/1.3.png)


### Задание 2
```python
#1
a=[[1, 2, 3]]
b=[[1], [2], [3]]
c = [[1, 2], [3, 4]]
d = []
e = [[1, 2], [3]]
def f1(x):
    a=[]
    for i in x:
        for j in i:
            a.append([j])
    return a
def f2(p):
    a=[]
    for i in p:
        for j in i:
            a.append(j)
    return a
def f3(x):
    y=[x[0][0], x[1][0]]
    z=[x[0][1], x[1][1]]
    return [y,z]

def f4(x):
    for i in range(len(x) - 1):
        if len(x[i]) != len(x[i + 1]):
            print('ValueError')

print(f1(a))
print(f2(b))
print(f3(c))
print(f2(d))
print(f4(e))

#2
a=[[1, 2, 3], [4, 5, 6]]
b=[[-1, 1], [10, -10]]
c=[[0, 0], [0, 0]]
d=[[1, 2], [3]]
def F(x):
    s=0
    a=[]
    for i in range(len(x) - 1):
        if len(x[i]) != len(x[i + 1]):
            print('ValueError')
            break
        else:
            for i in x:
                s=sum(i)
                a.append(s)
    return a
print(F(a))
print(F(b))
print(F(c))
print(F(d))

#3
a=[[1, 2, 3], [4, 5, 6]]
b=[[-1, 1], [10, -10]]
c=[[0, 0], [0, 0]]
d=[[1, 2], [3]]
def F(a):
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            print('ValueError')
            break
        else:
            lene = 0
            k = 0
            for i in a:
                lene = len(i)
            summ = [0] * lene
            for i in range(len(a)):
                for j in range(lene):
                    summ[j] += a[i][j]
            print(summ)
    return ''
print(F(a))
print(F(b))
print(F(c))
print(F(d))
```
[Картинка 1] ![2.1.png](images/2.1.png)
[Картинка 2] ![2.2.png](images/2.2.png)
[Картинка 3] ![2.3.png](images/2.3.png)


### Задание 3
```python
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

```
[Картинка 1]![3.png](images/3.png)

