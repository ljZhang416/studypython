# 2.写一个函数mixmax(),有3个参数,返回这三个数的最小值和最大值,\
#   (形成元组,最小值在前,最大值在后),可以return最小值和最大值并打印

def minmax(a, b, c):
    if a > b > c:
        print("最大值是%s，最小值是%s" % (a, c))
    elif a > c > b:
        print("最大值是%s，最小值是%s" % (a, b))
    elif b > a > c:
        print("最大值是%s，最小值是%s" % (b, c))
    elif b > c > a:
        print("最大值是%s，最小值是%s" % (b, a))
    elif c > c > a:
        print("最大值是%s，最小值是%s" % (c, a))
    else:
        print("最大值是%s，最小值是%s" % (c, b))


a = int(input("请输入第一个数："))
b = int(input("请输入第一个数："))
c = int(input("请输入第一个数："))
minmax(a, b, c)
