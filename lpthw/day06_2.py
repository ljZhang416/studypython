# 任意输入5个数, 存在列表中, 打印出这5个数的最大值 / 最小值, 平均值

L = []
for i in range(1, 6):
    L.append(int(input("请输入：")))
print("最大值是：%s" % max(L))
print("最小值是：%s" % min(L))
print("平均值是：%s" % int(sum(L) / 5))
