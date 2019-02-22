import matplotlib.pyplot as plt

# 随机生成
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 展示图表
# plt.show()

# 自动保存图表，不可以跟在plt.show()后面使用，否则会保存一张空白图片
plt.savefig('squares.png')