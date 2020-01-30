import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data_one = np.arange(100, 201)
# plt.plot(data_one)
# plt.show()
# 创建空白画布
# figure_obj = plt.figure()
# data_two = np.arange(200, 301)
# 创建背景为灰色的画布
# plt.figure(facecolor='gray')
# plt.plot(data_two)
# plt.show()

# 创建单个子图
# nums = np.arange(0, 101)
# plt.subplot(221)
# plt.plot(nums, nums)
# plt.subplot(222)
# plt.plot(nums, -nums)
# plt.subplot(212)
# plt.plot(nums, nums ** 2)
# plt.show()

# 创建多个子图
# nums = np.arange(1, 101)
# fig, axes = plt.subplots(2, 2)
# ax1 = axes[0, 0]  # 从Axes对象数组中获取第一个子图
# ax2 = axes[0, 1]
# ax3 = axes[1, 0]
# ax4 = axes[1, 1]
# ax1.plot(nums, nums)
# ax2.plot(nums, -nums)
# ax3.plot(nums, nums ** 2)
# ax4.plot(nums, np.log(nums))
# plt.show()

# 添加和选中子图
# 创建Figure实例
# fig = plt.figure()
# # 添加子图
# fig.add_subplot(2, 2, 1)
# fig.add_subplot(2, 2, 2)
# fig.add_subplot(2, 2, 3)
# fig.add_subplot(2, 2, 4)
# 在子图上作图
# random_arr = np.random.randn(100)
# plt.plot(random_arr)
# plt.show()

# 添加各类标签
# data = np.arange(0, 1.1, 0.01)
# plt.title('Title')
# plt.xlabel('x')
# plt.ylabel('y')
#
# # 设置x和y的刻度
# plt.xticks([0, 0.5, 1])
# plt.yticks([0, 0.5, 1.0])
# plt.plot(data, data ** 2)
# plt.plot(data, data ** 3)
# plt.legend(['y = x^2', 'y = x^3'])
# plt.show()

# 绘制常见图表
# 绘制直方图
# arr_random = np.random.randn(100)
# plt.hist(arr_random, bins=8)
# plt.show()

# 绘制散点图
# x = np.arange(51)
# y = np.random.rand(51) * 10
# plt.scatter(x, y)
# plt.show()

# 绘制柱状图
# x = np.arange(5)
# # 从上下限范围随机选取整数， 创建两个二行五列的数组
# y1, y2 = np.random.randint(1, 31, size=(2, 5))
# width = 0.25  # 条形的宽度
# ax = plt.subplot(1, 1, 1)  # 创建一个子图
# ax.bar(x, y1, width, color='r')
# ax.bar(x + width, y2, width, color='g')
# ax.set_xticklabels(['0', '1', '2', '3', '4', '5'])
# plt.show()

# 设置颜色、线性、标记
# data = np.arange(1, 3, 0.3)
# plt.plot(data, color='c', marker='x', linestyle='--')
# plt.plot(data+1, color='m', marker='o', linestyle=':')
# plt.plot(data+2, color='k', marker='p', linestyle='-.')
# plt.show()

# seaborn 绘制统计图形
# 可视化数据的分布
# sns.set()  # 显式调用set()获取默认绘图
# np.random.seed(0)  # 确定随机数生成器的种子
# arr = np.random.randn(100)
# ax = sns.distplot(arr, bins=10)  # 绘制直方图
# plt.show()

# array_random = np.random.randint(0, 100, 500)
# sns.distplot(array_random, hist=False, rug=True)
# plt.show()

# 绘制双变量分布
# 绘制散点图
# df = pd.DataFrame({'x': np.random.randn(500),
#                    'y': np.random.randn(500)})
# sns.jointplot(x='x', y='y', data=df)
# plt.show()

# 绘制二维直方图
# df = pd.DataFrame({'x': np.random.randn(500),
#                    'y': np.random.randn(500)})
# sns.jointplot(x='x', y='y', data=df, kind='hex')
# plt.show()

# 核密度估计
# df = pd.DataFrame({'x': np.random.randn(500),
#                    'y': np.random.randn(500)})
# sns.jointplot(x='x', y='y', data=df, kind='kde')
# plt.show()

# 用分类数据绘图
# 类别散点图
# planets = sns.load_dataset('planets')  # 获取数据集
# sns.stripplot(x='method', y='mass', data=planets)
# plt.show()

# planets = sns.load_dataset('planets')  # 获取数据集
# sns.swarmplot(x='method', y='mass', data=planets)
# plt.show()

# 类别内的数据分布
# 箱型图
# planets = sns.load_dataset('planets')  # 获取数据集
# # sns.boxplot(x='method', y='mass', data=planets)
# # plt.show()

# 绘制提琴图
# planets = sns.load_dataset('planets')  # 获取数据集
# sns.violinplot(x='method', y='mass', data=planets)
# plt.show()


