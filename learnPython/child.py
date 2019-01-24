"""Child"""
from people import *

class Child(Prople):
    # 定义自己的初始化参数
    def __init__(self, heigh):
        # 初始化父类参数
        super().__init__(0)
        self.heigh = heigh

    def method02(self):
        print("this is heigh" + str(self.heigh))

my_child = Child(10)
my_child.method()
my_child.method02()