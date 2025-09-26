#1
# a=[[1, 2, 3]]
# b=[[1], [2], [3]]
# c = [[1, 2], [3, 4]]
# d = []
# e = [[1, 2], [3]]
# def f1(x):
#     a=[]
#     for i in x:
#         for j in i:
#             a.append([j])
#     return a
# def f2(p):
#     a=[]
#     for i in p:
#         for j in i:
#             a.append(j)
#     return a
# def f3(x):
#     y=[x[0][0], x[1][0]]
#     z=[x[0][1], x[1][1]]
#     return [y,z]
#
# def f4(x):
#     for i in range(len(x) - 1):
#         if len(x[i]) != len(x[i + 1]):
#             print('ValueError')
#             break
#
#
# print(f1(a))
# print(f2(b))
# print(f3(c))
# print(f2(d))
# print(f4(e))

#2
# a=[[1, 2, 3], [4, 5, 6]]
# b=[[-1, 1], [10, -10]]
# c=[[0, 0], [0, 0]]
# d=[[1, 2], [3]]
# def F(x):
#     s=0
#     a=[]
#     for i in range(len(x) - 1):
#         if len(x[i]) != len(x[i + 1]):
#             print('ValueError')
#             break
#         else:
#             for i in x:
#                 s=sum(i)
#                 a.append(s)
#     return a
# print(F(a))
# print(F(b))
# print(F(c))
# print(F(d))


# #3
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