# 4.打印九九乘法表
#     1x1=1
#     1x2=2 2x2=4

for i in range(1, 10):
    for j in range(1, i + 1):
        if j < i:
            print("%sx%s=%s" % (j, i, j * i), end=" ")
        elif j == i:
            print("%sx%s=%s" % (j, i, j * i))
