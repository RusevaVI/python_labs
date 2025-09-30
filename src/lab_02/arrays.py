#1
test1=[3,-1,5,5,0]
test2=[42]
test3=[-5, -2, -9]
test4=[]
test5=[1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    list1=[]
    for i in nums:
        list1.append(i)
    if len(list1)==0:
        print('ValueError')
    else:
        res=(min(list1),max(list1))
        print(res)
    return ''
print(min_max(test1))
print(min_max(test2))
print(min_max(test3))
print(min_max(test4))
print(min_max(test5))



#2

test1=[3, 1, 2, 1, 3]
test2=[]
test3=[-1, -1, 0, 2, 2]
test4=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    int_list=[]
    float_list=[]
    for i in nums:
        if type(i)==int:
            int_list.append(i)
        else:
            float_list.append(i)
    res1 = [x for x in float_list if int(x) in int_list]
    res2 = [x for x in int_list if float(x)  not in float_list]
    print(sorted(set(res1+res2+float_list)))
    return ''
print(unique_sorted(test1))
print(unique_sorted(test2))
print(unique_sorted(test3))
print(unique_sorted(test4))

#3
test1=[[1, 2], [3, 4]]
test2=([1, 2], (3, 4, 5))
test3=[[1], [], [2, 3]]
test4=[[1, 2], "ab"]

def flatten(mat: list[list | tuple]) -> list:
    list1=[]
    list2=[]
    k=0
    for i in mat:
        for j in i:
            list1.append(j)
            if type(j)==int:
                k+=1
            if k==len(list1):
                list2.append(j)
            else:
                print('TypeError')
                break
    if k==len(list1):
        print(list2)
    return ''

print(flatten(test1))
print(flatten(test2))
print(flatten(test3))
print(flatten(test4))