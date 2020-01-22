import numpy as np
data1 = np.array([1, 2, 3])  # 创建一维数组
data2 = np.array([[1, 2, 3], [4, 5, 6]])  # 创建二维数组
print(data2)
# [[1 2 3]
# [4 5 6]]

print(np.zeros((3, 4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(np.ones((3, 4)))
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

print(np.empty((5, 2)))  # 随机填充float64类型数组
# [[ 6.23040373e-307  1.60219035e-306]
#  [-2.35343653e-185  1.89146956e-307]
#  [ 7.56571288e-307  3.11525958e-307]
#  [ 1.24610723e-306  1.37962320e-306]
#  [ 1.29060871e-306  2.22518251e-306]]

print(np.arange(1, 20, 5))  # 返回等差数组
# [ 1  6 11 16]

print(np.array([1, 2, 3, 4], float))  # 可以显式地声明数组元素的数据类型

print(data1.dtype)  # 查看数据类型int32

# 转换数据类型
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.dtype)  # int32
float_data = data.astype(np.float64)  # 数据类型转换
print(float_data.dtype)  # float64
int_data = float_data.astype(np.int64)  # 数据类型转换
print(int_data.dtype)  # int64

# 矢量化运算
data1 = np.array([[1, 2, 3], [4, 5, 6]])
data2 = np.array([[1, 2, 3], [4, 5, 6]])
print(data1 + data2)
# [[ 2  4  6]
#  [ 8 10 12]]

print(data1 - data2)
# [[0 0 0]
#  [0 0 0]]

print(data1 * data2)  # 注意本质上是数组相乘
# [[ 1  4  9]
#  [16 25 36]]
# 除法同理

data2 = 10
print(data1 + data2)  # 注意理解广播机制
# [[11 12 13]
#  [14 15 16]]

arr = np.arange(8)  # 创建一维数组
print(arr)  # [0 1 2 3 4 5 6 7]

arr2d = np.array([[1, 2, 4], [4, 5, 6], [7, 8, 9]])  # 创建二维数组
print(arr2d)
# [[1 2 4]
#  [4 5 6]
#  [7 8 9]]

# 数组索引
print(arr2d[1])
# [4 5 6]
print(arr2d[0, 1])  # 2

print(arr2d[:2])
# [[1 2 4]
#  [4 5 6]]

print(arr2d[0:2, 0:2])  # 传入两个切片
# [[1 2]
#  [4 5]]

demo_arr = np.empty((4, 4))
for i in range(4):
    demo_arr[i] = range(i, i + 4)
print(demo_arr)
# [[0. 1. 2. 3.]
#  [1. 2. 3. 4.]
#  [2. 3. 4. 5.]
#  [3. 4. 5. 6.]]

print(demo_arr[[0, 2]])
# [[0. 1. 2. 3.]
#  [2. 3. 4. 5.]]

# 布尔型索引
student_name = np.array(['Tom', 'Lucy', 'Jack', 'Rose'])
student_score = np.array([[79, 80, 80], [89, 90, 92], [83, 78, 85], [78, 76, 80]])
print(student_score)
# [[79 80 80]
#  [89 90 92]
#  [83 78 85]
#  [78 76 80]]

print(student_name == 'Jack')  # [False False  True False]
s = student_score[student_name == 'Jack']
print(s)  # [[83 78 85]]

# 可将布尔索引与切片结合
s = student_score[student_name == 'Jack', :1]
print(s)  # [[83]]

# 数组的转置与轴对称
arr = np.arange(12).reshape(3, 4)
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(arr.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]

#  [[ 8  9 10 11]
#   [12 13 14 15]]]

# NumPy同用函数
arr = np.array([4, 9, 16])
print(np.sqrt(arr))  # [2. 3. 4.]
print(np.abs(arr))  # [ 4  9 16]
print(np.square(arr))  # [ 16  81 256]
x = np.array([12, 9, 13, 15])
y = np.array([11, 10, 4, 8])
print(np.add(x, y))  # [23 19 17 23]
print(np.multiply(x, y))  # [132  90  52 120]
print(np.maximum(x, y))  # [12 10 13 15]
print(np.greater(x, y))  # [ True False  True  True]


# 将条件逻辑转为数组运算
arr_x = np.array([1, 5, 7])
arr_y = np.array([2, 6, 8])
arr_con = np.array([True, False, True])

result = np.where(arr_con, arr_x, arr_y)
print(result)  # [1 6 7]

# 数组统计计算
arr = np.arange(10)
print(arr.sum())  # 求和 45
print(arr.mean())
print(arr.min())
print(arr.max())
print(arr.argmin())  # 求最小值所在的索引
print(arr.argmax())
print(arr.cumsum())  # 求累计和 [ 0  1  3  6 10 15 21 28 36 45]
print(arr.cumprod())  # 求累计积[0 0 0 0 0 0 0 0 0 0]

# 数组排序
arr = np.array([[6, 2, 7], [3, 6, 2], [4, 3, 2]])
print(arr)
# [[6 2 7]
#  [3 6 2]
#  [4 3 2]]

arr.sort(0)  # 在第一维进行排序
print(arr)
# [[3 2 2]
#  [4 3 2]
#  [6 6 7]]

# 检索数组元素
arr = np.array([[1, -2, -7], [-3, 6, 2], [-4, 3, 2]])
print(arr)
# [[ 1 -2 -7]
#  [-3  6  2]
#  [-4  3  2]]

print(np.any(arr > 0))  # 判断是否有一个大于0
print(np.all(arr > 0))  # 判断是否全部大于0

# 唯一化和其他集合逻辑
arr = np.array([12, 11, 34, 23, 12, 8, 11])
print(np.unique(arr))  # 找出数组中的唯一值
# [ 8 11 12 23 34]

# 线性代数模块
arr_x = np.array([[1, 2, 3], [4, 5, 6]])
arr_y = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_x.dot(arr_y))  # 矩阵乘法
# [[22 28]
#  [49 64]]
print(np.dot(arr_x, arr_y))
# [[22 28]
#  [49 64]]

# 随机数模块
r = np.random.rand(3, 3)
print(r)
# [[0.82663256 0.28182761 0.84150244]
#  [0.67866495 0.37009741 0.73943425]
#  [0.44187091 0.06469587 0.44479975]]

r = np.random.rand(2, 3, 3)
print(r)
# [[[0.55231083 0.91306636 0.44416682]
#   [0.16825293 0.72205217 0.24730432]
#   [0.87319132 0.21063912 0.81519232]]
#
#  [[0.28272883 0.11541136 0.75086525]
#   [0.24985642 0.40523564 0.61278835]
#   [0.4237519  0.59597077 0.84816107]]]

np.random.seed(0)  # 生成随机数的种子
r = np.random.rand(5)
print(r)
# [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

# 案例：酒鬼漫步
steps = 2000
draws = np.random.randint(0, 2, size=steps)
print(draws)  # [1 0 0 ... 0 0 1]
# 当元素为1时，direct为1
# 当元素为0时，direct为-1
direct = np.where(draws > 0, 1, -1)
distance = direct.cumsum()
print(distance)  # [ 1  0 -1 ... 30 29 30]

# 计算向前走的最远距离
print(distance.max())  # 34
# 计算向后走的最远距离
print(distance.min())  # -15




