# 给出一个年份, 判断是否为闰年并打印(每4年1闰年, 每百年不闰, 每400年又闰)

while True:
	year = int(input("请输入年份："))
	if year < 0:
		print("输入错误")
	elif year % 400 == 0:
		print("%s是闰年"% year)
	elif (year % 4 == 0) and (year % 100 != 0):
		print("%s是闰年"% year)
	else:
		print("%s不是闰年"% year)