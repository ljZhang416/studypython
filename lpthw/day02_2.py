# 任意输入一个数,判断这个数是否大于100

while True:
	x = input("请输入：")
	if x == "a":
		break
	elif float(x) >= 100:
		print(x)
	else:
		print("%s 小于100"% x)