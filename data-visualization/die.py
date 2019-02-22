from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sizes=6):
        """骰子默认6个面"""
        self.num_sizes = num_sizes

    def roll(self):
        """返回一个位于1和骰子面熟之间的随机数"""
        return randint(1, self.num_sizes)
