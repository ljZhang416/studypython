# 2.定义两个函数sum3(a, b, c)用于返回三个数的和, pow3(x)用于返回x的3次方
# a.计算1的立方 + 2的立方 + 3的立方的和
# b.计算1 + 2 + 3的和的立方

def sum3(a,b,c):
    return a+b+c

def pow3(a):
    return a**3

print(sum3(pow3(1),pow3(2),pow3(3)))

print(pow3(sum3(1,2,3)))
