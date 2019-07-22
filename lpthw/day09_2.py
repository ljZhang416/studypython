# 1.写一个函数minmax至少有一个参数,返回这些参数的最大值和最小值,形成元组,最小值在前,最大值在后

def minmax(a, *args):
    # return (min(args), max(args))
    # 方法1
    # xiao = a
    # for x in args:
    #     if x < xiao:
    #         xiao = x
    # da = a
    # for x in args:
    #     if x > da:
    #        da = x
    # return (xiao, da)
    # 方法2
    return (min(a, *args), max(a, *args))


zx, zd = minmax(1, 2, 3, 4, 5, 6, 7)
print(zx, zd)  # 1 7

zx, zd = minmax("A1", "B0", "D4", "C3")
print(zx, zd)  # A1 D4
