# coding=utf-8
from sys import argv

pyfile, filename = argv

def print_file(f):
    print(f.read())

def rewind(f):
    print(f"打印{f}")
    # seek() 方法用于移动文件读取指针到指定位置。
    f.seek(0)
    print(f"打印{f.seek(0)}")

def print_a_line(line_count,f):
    print(line_count, f.readline())

f_name = open(filename)

print("打印文件内容：")
print_file(f_name)

print("=======")
rewind(f_name)

print("打印文件的某一行：")
for f_line in range(1,4):
    print_a_line(f_line, f_name)
    f_line = f_line + 1
