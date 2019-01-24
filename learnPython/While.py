# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# 控制while 退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


# 使用break退出
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)


# 使用while 循环来处理列表和字典

# 在列表之间移动元素
print("在列表之间移动元素")
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)

# 删除包含特定值的所有列表元素
print("删除包含特定值的所有列表元素")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)











