# 如果有else语法，则表示未出现异常的话则执行else的内容
try:
    # print(5/0)
    print(0/5)
except ZeroDivisionError:
    print("error")
else:
    print("else error")