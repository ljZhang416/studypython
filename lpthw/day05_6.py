# 1.将1 - 20的整数打印在一行
# 2.将1 - 20的整数每5个一行打印四行
# 3.输入一个数, 用n绑定, 求1 + 2 + ... + n的和

for i in range(1,21):
	print(i)

for i in range(1,21):
	if i % 5 != 0:
		print(i,end=" ")
	else:
		print(i)

n = int(input("请输入："))
sum1 = 0
for i in range(1,n):
	sum1 = i + sum1
print(sum1+i+1)