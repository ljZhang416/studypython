  # 1.打印1-20的整数,打印在一行显示,每个数字之间用一个空格分隔
  # 2.打印1-20的整数,每行打印5个数字,打印4行
  # 3.写一个程序,输入一个开始的整数值存于变量begin中,\
  #   输入一个结束的整数值存于变量end中,打印从begin到end的每个整数,不包含end

# num = 1
# while num <= 20:
# 	print(num,end=" ")
# 	num = num + 1

# while num <= 20:
# 	print(num, end=" ")
# 	num = num + 1
# 	while num % 5 == 0:
# 		print(num)
# 		num = num + 1

begin = int(input("请输入开始的整数："))
end = int(input("请输入结束的整数："))
while begin < end:
	print(begin)
	begin = begin + 1


