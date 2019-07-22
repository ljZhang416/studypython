# 输入一个字符串, 打印这个字符串的第一个字符, 中间字符和最后一个字符.\
# 	如果输入的字符串长度为偶数, 则中间字符不输出

# s = input("请输入字符串：")
# print("第一个字符是：%s" % s[0])
# if len(s) % 2 != 0:
# 	print("中间字符是：%s" % s[int((len(s) - 1) / 2)])
# print("最后一个字符是：%s" % s[int(len(s) - 1)])

# s = "abcdeqwerzxc"
# print(s)
# print(s[0:33])
# print(s[-1::-1])
# print(s[3])
# print(s[1:3:1])
# print(s[1:8:2])

str1 = input("请输入字符串：")
if str1 == str1[-1::-1]:
	print("str1是回文")
else:
	print("str1不是回文")

