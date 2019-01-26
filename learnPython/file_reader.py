# 读取文件操作
# open()接受一个参数：要打开的文件的名称。
# 关键字with在不再需要访问文件后将其关闭
with open("E:/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

print("*******************")

# 逐行读取文件
with open("E:/pi_digits.txt") as file_object:
    for line in file_object:
        print(line)

print("********************")

# 将文件内容存储到列表中

with open("E:/pi_digits.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

