# 1.输入多行文字, 存入列表中.每次输入后回车算作一行, 任意输入多行, 当直接输入会从时结束
# a.打印刚才输入的行数
# b.按原输出的内容在屏幕上输出内容
# c.打印刚才共输出了多少字符

L = []
num = 0
i = 0
while True:
    str1 = input("请输入：")
    if str1 == "":
        break
    L.append(str1)
    num = num + len(str1)
    i = i + 1

print("输入的内容为：%s"% L)
for i in range(0, len(L)):
    print(L[i])
print("输入了%s个字符" % num)
