# 写入文件内容
# 读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）
with open("E:/programing txt", "w") as file_object:
    file_object.write("I love shanghai")