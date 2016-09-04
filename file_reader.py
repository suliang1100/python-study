
# 读取文本文件
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())