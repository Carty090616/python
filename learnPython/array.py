# 列表（可以列结尾数组）
array = ["a", "b"]
print(array[0].title())

# 添加元素
# 末尾添加
array.append("c")
print(array)
# 插入到任意位置
array.insert(1, "d")
print(array)

# 删除元素
del array[3]
print(array)

array.remove("a")
print(array)

print("*********************************************")

# 排序
array01 = ["a", "d", "b", "c"]
# 永久改变元素位置
array01.sort()
print(array01)

# 临时改变位置
array02 = ["a", "d", "b", "c"]
print(sorted(array02))
print(array02)

# 列表长度
array04 = ["a", "d", "b", "c"]
print(len(array04))

print("*****************************************")
# 遍历列表
# for循环
# 需要注意缩进与不缩进的区别
print("遍历列表:for循环")
array05 = ["a", "d", "b", "c"]
for arr in array05:
    print(arr)
print("*****************************************")


# 列表解析
# 首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，
# 并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value**2，它计
# 算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号
squares = [value**2 for value in range(1,11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 遍历切片
players01 = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players01[:3]:
    print(player.title())

# 检查元素是否为空
# 将在列表至少包含一个元素时返回True，并在列表为空时返回False
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("列表不为空")
else:
    print("列表为空")