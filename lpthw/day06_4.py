# 1.已知有列表L = [3, 5].
# # a.用L的方法实现原列表变为L = [1, 2, 3, 4, 5]
# # b.将列表反转, 删除最后一个后打印此列表

L = [3, 5]
# L[:] = [1, 2, 3, 4, 5]
# print(L)

L.append(1)
L.append(2)
L.append(4)
L.sort()
print(L)

L.reverse()
L.pop(-1)
print(L)

