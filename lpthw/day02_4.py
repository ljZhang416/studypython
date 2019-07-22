# 2.输入一年中的月份(1-12表示),输出这个月在哪个季度(春夏秋冬)
#     如果输入的是其他数,则提示输入错了

while True:
	mon = int(input("请输入："))
	if mon ==0:
		break
	elif mon >= 1 and mon <= 3:
		print("春")
	elif mon >= 4 and mon <=6:
		print("夏")
	elif mon >= 7 and mon <= 9:
		print("秋")
	else:
		print("冬")


