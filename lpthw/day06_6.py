# 2.有一些数存于列表中, 如: L = [1, 3, 2, 64, ..., 82]
# 要求将列表中只出现一次的元素存于另一个列表L2中

str1 = input("请输入：")
L = str1.split(" ")
L2 = []

for i in range(0, len(L)):
    if L.count(L[i]) == 1:
        L2.append(L[i])
print(L2)
