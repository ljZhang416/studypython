# 3.修改学生管理项目的代码
# a.将输入部分封装成为函数, 调用函数来获取数据
# b.将打印表格封装成为函数, 用打印函数来打印表格


def stu_list(listA):
    while True:
        stu_dict = dict()
        name = input("请输入学生姓名：")
        if name == "":
            break
        age = input("请输入学生年龄：")
        if age == "":
            break
        score = input("请输入学生成绩：")
        if score == "":
            break
        stu_dict["name"] = name
        stu_dict["age"] = age
        stu_dict["score"] = score
        listA.append(stu_dict)
    print(listA)
    return listA


# # 用i遍历listA的每一项.然后判断i['name']的最长值,绑定到变量maxlength上

def length(max_length, list):
    for i in list:
        if len(i["name"]) > max_length:
            max_length = len(i["name"])
    return max_length


stu = []
stu_list(stu)
max_len = 5
max_len = length(max_len, stu)
print(max_len)
print(("+" + "-" * max_len) * 3 + "+")

print("|" + "name".center(max_len) + "|" + "age".center(max_len) + "|" + "score".center(max_len) + "|")

print(("+" + "-" * max_len) * 3 + "+")

# 用for遍历listA
for i in stu:
    print("|" + i["name"].center(max_len) + "|" + i["age"].center(max_len) + "|" + i["score"].center(max_len) + "|")

print(("+" + "-" * max_len) * 3 + "+")
