# 函数（函数是带名字的代码块）

# 关键字def来告诉Python你要定义一个函数
# 实参和形参 (name 形参，carty 实参)
def great_user(name):
    print("函数:" + name)

great_user("carty")

# 位置实参（指的是形参和实参的位置一一对应）
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')


# 关键字实参（关键字实参是传递给函数的名称—值对）
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')


# 默认值（编写函数时，可给每个形参指定默认值）
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# #############################################################

# 返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


