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
