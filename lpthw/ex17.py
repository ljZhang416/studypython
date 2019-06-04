# coding=utf-8

from sys import argv
from os.path import exists

pyfile, a_file, b_file = argv

print(f"复制{a_file}的内容到{b_file}")

in_file = open(a_file)
in_file_data = in_file.read()

print(f"a_file 文件有{len(in_file_data)}个字节")

print(f"b_file文件是否存在？{exists(b_file)}")

out_file = open(b_file,"w")
out_file.write(in_file_data)


in_file.close()
out_file.close()