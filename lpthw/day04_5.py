# 1.写一个程序, 输入一个整数, 打印指定宽度的正方型
# 2.输入三行英文, 让这三行英文在一个方框居中显示

# l = int(input("请输入正方形的宽度："))
# i = 0
# while i < l:
# 	print("*"*l)
# 	i = i + 1

s1 = input("请输入第一行：")
lens1 = len(s1)
s2 = input("请输入第二行：")
lens2 = len(s2)
s3 = input("请输入第三行：")
lens3 = len(s3)
print("*"*(max(lens1,lens2,lens3)+2))
print(s1.center(max(lens1,lens2,lens3)+2," "))
print(s2.center(max(lens1,lens2,lens3)+2," "))
print(s3.center(max(lens1,lens2,lens3)+2," "))
print("*"*(max(lens1,lens2,lens3)+2))






