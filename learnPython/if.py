# if 也要注意缩进
# = 一个等号表示赋值
# == 表示判断是否相等
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'Bmw':
        print("a")
    else:
        print("b")

# 检查多个条件用 and 或者 or

# 检查特定值是否包含或者不包含在列表中用 in 或者 not in

# if-elif-else 结构（可以有多个elif）

age = 4
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print(price)