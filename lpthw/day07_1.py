# 写一个程序，先输入一些单词和解释，将单词作为键，将解释作为值，将这此数据输入字典中.
# # 以输入单词为空结束输入.然后循环提示请输入要查找的词:
# # 如果不存在于字典中提示没找到，如果存在，打印出解释

d = {1: "one", 2: "two", 3: "three"}
while True:
    x = int(input("请输入："))
    if x in d:
        print(d.get(x))
    elif x == " ":
        break
    else:
        print("不存在")

