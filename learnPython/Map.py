# 字典（在Python中，字典是一系列键—值对）
print("取值:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print("********************************************")

# 添加
print("添加:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("********************************************")
# 定义一个空的字典
print("定义一个空的字典:")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("********************************************")
# 修改字典中的值
print("修改字典中的值:")
alien_0 = {'color': 'green'}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

print("********************************************")
# 删除键—值对
print("删除键—值对:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("********************************************")
# 遍历字典
# 键—值对的返回顺序也与存储顺序不同
print("遍历字典(for循环):")
user_0 = {'username': 'efermi','first': 'enrico','last': 'fermi'}
for key, value in user_0.items():
    print("\nKey: " + key + "\tValue: " + value)

# 遍历字典中的所有键
print("遍历字典--遍历字典中的所有键:")
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
for name in favorite_languages.keys():
    print(name.title())

# 按顺序遍历字典中的所有 键
print("遍历字典--按顺序遍历字典中的所有 键:")
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
for name in sorted(favorite_languages.keys()):
    print(name.title())


# 遍历字典中的所有值--没有考虑是否重复
print("遍历字典--遍历字典中的所有值--没有考虑是否重复:")
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
for language in favorite_languages.values():
    print(language)

print("遍历字典--遍历字典中的所有值--去除重复:")
for language in set(favorite_languages.values()):
    print(language)




# 嵌套
print("***************************************************")
print("嵌套")

# 字典列表
print("字典列表")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 在字典中存储列表
print("在字典中存储列表")
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# 在字典中存储字典
print("在字典中存储字典")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


