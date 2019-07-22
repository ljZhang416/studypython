# 3.写一个函数input_number()无参,在函数内部读取很多个整数,\
# 当输入空字符串时结束输入,返回输入的整数的列表

def input_number():
    L = []
    while True:
        i = input("请输入：")
        if i == "":
            break
        else:
            L.append(int(i))
    print(L)


input_number()
