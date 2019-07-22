# 1.输入三行文字,保存于列表L中,并打印
#
L = []
l1 = input("请输入：")
l2 = input("请输入：")
l3 = input("请输入：")
# L = [l1,l2,l3]
L.append(l1)
L.append(l2)
L.append(l3)
print(L)

# a = [["a","b","c"], "qwe", 123, "ghj"]
# for i in a:
# 	print(i)
# 	if type(i) == type(["",""]):
# 		for j in i:
# 			print(j)

s = "Hello"
L = list(s)
print(L[3])
print(type(L))
r = range(10)
print(type(r))
