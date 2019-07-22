# 1.有字符串"hello", 生成字符串"h e l l o"和"h-e-l-l-o"

L = list("hello")
s1 = " ".join(L)
print(s1)
s2 = "-".join(L)
print(s2)