# 2. 输入任意5个学生的 姓名，年龄，成绩,每个学生的信息存入字典,然后把学生信息的字典放入列表中.
#     每个学生的信息需要手动输入
#     内部存储格式如下：
#     [{"name":"tarena", "age": 20, "score": 99}, {"name":"xiaozhang", "age": 23, "score": 100}, .... ]
#   1) 打印所有学生信息如下：
#   +-------------+-------------+-----------+
#   |   姓 名      |   年  龄    |   成绩     |
#   +-------------+-------------+-----------+
#   |  tarena     |      20     |    99     |
#   | xiaozhang   |      23     |   100     |
#   |  name2      |      28     |    70     |
#   |   ....      |     ...     |   ...     |
#   +-------------+-------------+-----------+
#   2) 输入学生的分数线，把高于这个分数线的学生信息打印出来
#   如输入:90 打印如下
#   +-------------+-------------+-----------+
#   |   姓 名      |   年  龄    |   成绩     |
#   +-------------+-------------+-----------+
#   |  tarena     |      20     |    99     |
#   | xiaozhang   |      23     |   100     |
#   +-------------+-------------+-----------+


# 通过循环输入学生信息, 当某一项为空时,结束输入
# 在循环的时候通过listA.append()方法,把学生的信息放入listA
stu_list = []

while True:
    stu_dict = dict()
    name = input("请输入学生姓名：")
    if name =="":
        break
    age = input("请输入学生年龄：")
    if age == "":
        break
    score = input("请输入学生成绩：")
    if score == "":
        break
    stu_dict["name"]=name
    stu_dict["age"]= age
    stu_dict["score"]=score
    stu_list.append(stu_dict)
print(stu_list)

# # 用i遍历listA的每一项.然后判断i['name']的最长值,绑定到变量maxlength上
max_length = 5
for i in stu_list:
    if len(i["name"])> max_length:
        max_length = len(i["name"])
print(max_length)

stu_score = int(input("请输入要筛选的学生成绩："))

print(("+" + "-" * max_length )* 3 + "+")

print("|"+"name".center(max_length)+"|"+"age".center(max_length)+"|"+"score".center(max_length)+"|")

print(("+" + "-" * max_length )* 3 + "+")

for i in stu_list:
    if int(i["score"]) >= stu_score:
        print("|" + i["name"].center(max_length) + "|" + i["age"].center(max_length) + "|" + i["score"].center(
            max_length) + "|")
print(("+" + "-" * max_length )* 3 + "+")