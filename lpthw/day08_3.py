# 1.写一个函数def mymax(a, b, c),实现返回3个数的最大值
#     print(mymax(100, 300, 200)) # 300
#     print(mymax("AB", "BC", "AC")) # BC
#     要求,不允许使用max函数

def mymax(a, b, c):
    if a>b>c or a>c>b:
        return a
    elif b>a>c or b>c>a:
        return b
    else:
        return c


print(mymax(100, 300, 200))