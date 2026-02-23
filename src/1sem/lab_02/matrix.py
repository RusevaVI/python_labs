# 1
test1 = [[1, 2, 3]]
test2 = [[1], [2], [3]]
test3 = [[1, 2], [3, 4]]
test4 = []
test5 = [[1, 2], [3]]


def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if len(mat) == 0:
        return []

    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return "ValueError"
    transp = []
    for col_index in range(len(mat[0])):
        row_new = []
        for row_index in range(len(mat)):
            row_new.append(mat[row_index][col_index])
        transp.append(row_new)
    return transp


print(transpose(test1))
print(transpose(test2))
print(transpose(test3))
print(transpose(test4))
print(transpose(test5))

# 2
test1 = [[1, 2, 3], [4, 5, 6]]
test2 = [[-1, 1], [10, -10]]
test3 = [[0, 0], [0, 0]]
test4 = [[1, 2], [3]]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    list1 = []
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return "ValueError"
        else:
            for i in mat:
                list1.append(sum(i))
    return list1


print(row_sums(test1))
print(row_sums(test2))
print(row_sums(test3))
print(row_sums(test4))


# 3
test1 = [[1, 2, 3], [4, 5, 6]]
test2 = [[-1, 1], [10, -10]]
test3 = [[0, 0], [0, 0]]
test4 = [[1, 2], [3]]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            return "ValueError"
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
