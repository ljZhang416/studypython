# 打印一个学生的3科成绩,存入变量x,y,z
#     1)打印出最高分是多少
#     2)打印出最低分是多少
#     3)打印出平均分是多少
x = int(input("请输入第一科成绩："))
y = int(input("请输入第二科成绩："))
z = int(input("请输入第三科成绩："))
if x > y and x > z:
	if y > z:
		print("分数由高的是%s,最低的是%s,平均分是%s"% (x,z,(x + y + z )/3))
	else:
		print("分数由高的是%s,最低的是%s,平均分是%s" % (x, y, (x + y + z) / 3))
elif y > x and y > z:
	if x > z:
		print("分数由高的是%s,最低的是%s,平均分是%s"% (y,z,(x + y + z )/3))
	else:
		print("分数由高的是%s,最低的是%s,平均分是%s" % (y, x, (x + y + z) / 3))
else:
	if x > y:
		print("分数由高的是%s,最低的是%s,平均分是%s"% (z,y,(x + y + z )/3))
	else:
		print("分数由高的是%s,最低的是%s,平均分是%s" % (z, x, (x + y + z) / 3))