# while True:
#     str1 = input("请输入:")
#     if str1 == "":
#         break
#     print("输入的是%s" % str1)
# print("输入结束")


# 1.写一个程序,输入用户名和密码:
#     假设用户名为zlj,密码为123456
#     a.写程序,让程序一直执行,直到输入的用户名和密码正确
#     b.失败超过3次则不能输入,提示请找回密码

i = 1
while i <= 3:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name == "zlj" and pwd == "123456":
        print("登录成功！")
        break
    print("输入错误！！")
    i = i + 1
