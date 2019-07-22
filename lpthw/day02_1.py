# 1.输入一个整数,用程序来判断这个数是奇数还是偶数并打印出来

while True:
	x = input("请输入一个整数:")
	if x == "a":
		print("跳出循环")
		break
	elif int(x) % 2 == 0:
		print("%s是一个偶数" % x)
	else:
		print("%s是一个奇数" % x)
