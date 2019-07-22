# 1.用两种方式(for/while)打印20以内的奇数
# 2.写一个程序,输入任意一个数,判断这个数是否为素数

# for i in range(1,20,2):
# 	print(i,end=" ")

i = 1
# while i < 20 and i % 2 != 0:
# 	print(i)
# 	i = i + 1
# 	while i < 20 and i % 2 == 0:
# 		i = i + 1
# 		continue

# while i < 20:
# 	if i % 2 !=0:
# 		print(i)
# 	i = i + 1

n = int(input("请输入正整数n:"))
if (n == 2) or (n == 3):
    print("%d是素数" % n)
elif n % 2 == 0:
    print("%d不是素数" % n)
else:
    for i in range(3, (n+1)//2+2, 2):
        if n % i == 0:
            print("%d不是素数" % n)
            break
        if i == (n+1)//2:
            print("%d是素数" % n)



