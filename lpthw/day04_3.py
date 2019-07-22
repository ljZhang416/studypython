# 1.请输入一个数,用n绑定,根据n的值输出n行hello.研究程序的执行流程
# 2.写程序,用while语句打印1-20的整数

n = int(input("请输入n的值："))
while n > 0:
	print("hello")
	n = n - 1

m = 1
while m <= 20:
	print(m)
	m = m + 1