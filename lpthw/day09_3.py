# 1.写一个函数split_odd_even(L,o,e),传入一些数据,把L中的奇数存入列表o,偶数存入列表e


def split_odd_even(L, o, e):
    for i in L:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    print("奇数有：%s" % o)
    print("偶数有：%s" % e)


L1 = []
o1 = []
e1 = []
while True:
    i = int(input("请输入数字:"))
    if i == 0:
        break
    L1.append(i)
split_odd_even(L1, o1, e1)
