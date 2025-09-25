#1
# a=[3,-1,5,5,0]
# b=[42]
# c=[-5, -2, -9]
# d=[]
# e=[1.5, 2, 2.0, -3.1]
# def f(b):
#     t=tuple(b)
#     s1=[]
#     for i in t:
#         s1.append(float(i))
#     if len(s1)==0:
#         print('ValueError')
#     else:
#         s2=(min(s1),max(s1))
#         print(s2)
# print(f(a))
# print(f(b))
# print(f(c))
# print(f(d))
# print(f(e))

#2
#
# a=[3, 1, 2, 1, 3]
# b=[]
# c=[-1, -1, 0, 2, 2]
# d=[1.0, 1, 2.5, 2.5, 0]
# def f(l):
#     i=[]
#     f=[]
#     for g in l:
#         if type(g)==int:
#             i.append(g)
#         else:
#             f.append(g)
#     res1 = [x for x in f if int(x) in i]
#     res2 = [x for x in i if float(x)  not in f]
#     print(sorted(set(res1+res2+f)))
# print(f(a))
# print(f(b))
# print(f(c))
# print(f(d))

#3
# a = [[1, 2, 3]]
# b = [[1], [2], [3]]
# c = [[1, 2], [3, 4]]
# d = []
# e = [[1, 2], [3]]
#
#
# def f1(x):
#     h = []
#     for i in x:
#         if isinstance(i, list):
#             for k in i:
#                 h.append([k])
#         else:
#             h.append([i])
#         return h
#
#
# def f2(x):
#     h = []
#     for i in x:
#         for j in i:
#             h.append(j)
#     return h
#
# def f3(x):
#     for i in range(len(x) - 1):
#         if len(x[i]) != len(x[i + 1]):
#             print(ValueError)
#
#
# print(f1(a))
# print(f2(b))
# print(f2(d))
# print(f3(e))
