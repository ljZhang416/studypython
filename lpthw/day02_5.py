# 输入一个学生的成绩, 判断这个成绩是
# 不及格(0 - 59) / \
# 及格(60 - 79) / \
# 良好(80 - 89) / \
# 优秀(90 - 100), 其他数值提示输入错误

while True:
	sco = input("请输入：")
	if int(sco) < 0 or int(sco) > 100:
		print("输入错误")
	elif 0 <= int(sco) <= 59:
		print("不及格")
	elif 60 <= int(sco) <= 79:
		print("及格")
	elif 80 <= int(sco) <= 89:
		print("良好")
	else:
		print("优秀")