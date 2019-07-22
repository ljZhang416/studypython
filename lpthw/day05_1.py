# 求10000以内的全部素数并打印(见su.py)

n = int(input("1不是素数,请输入大于2的正整数n:"))
lis1 = list(range(2,n+1))

i = 0
while i < len(lis1):
    q = lis1[0]
    print(q, end=" ")
    # if lis1[0] == lis1[-1]:
    #     break
    for j in lis1:
        if j % q == 0:
            lis1.remove(j)
    # i = i + 1
print("")
