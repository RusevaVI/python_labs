#1
test1 = [[1, 2, 3]]
test2 = [[1], [2], [3]]
test3 = [[1, 2], [3, 4]]
test4 = []
test5 = [[1, 2], [3]]
def transpose1(mat: list[list[float | int]]) -> list[list]:
    list1=[]
    if len(mat)==1:
        for i in mat:
            for j in i:
                list1.append([j])
        return list1
    else:
        for i in mat:
            for j in i:
                list1.append(j)
        return list1

def transpose2(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    else:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]):
                return 'ValueError'
            else:
                list1=[mat[0][0], mat[1][0]]
                list2=[mat[0][1], mat[1][1]]
                return [list1,list2]
    return mat
print(transpose1(test1))
print(transpose1(test2))
print(transpose2(test3))
print(transpose2(test4))
print(transpose2(test5))

#2
test1=[[1, 2, 3], [4, 5, 6]]
test2=[[-1, 1], [10, -10]]
test3=[[0, 0], [0, 0]]
test4=[[1, 2], [3]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    list1=[]
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return 'ValueError'
        else:
            for i in mat:
                list1.append(sum(i))
    return list1
print(row_sums(test1))
print(row_sums(test2))
print(row_sums(test3))
print(row_sums(test4))


#3
test1=[[1, 2, 3], [4, 5, 6]]
test2=[[-1, 1], [10, -10]]
test3=[[0, 0], [0, 0]]
test4=[[1, 2], [3]]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return 'ValueError'
        else:
            lene = 0
            k = 0
            for i in mat:
                lene = len(i)
            summ = [0] * lene
            for i in range(len(mat)):
                for j in range(lene):
                    summ[j] += mat[i][j]
    return summ
print(col_sums(test1))
print(col_sums(test2))
print(col_sums(test3))
print(col_sums(test4))
