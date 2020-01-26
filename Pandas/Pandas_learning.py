import numpy as np
import pandas as pd
# Series
ser = pd.Series([1, 2, 3, 4, 5])
print(ser)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

ser = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(ser)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

# 使用字典构建
year_data = {2008: 1.78, 2009: 0.23}
ser2 = pd.Series(year_data)
print(ser2)
# 2008    1.78
# 2009    0.23
# dtype: float64

print(ser2.index)  # Int64Index([2008, 2009], dtype='int64')
print(ser2.values)  # [1.78 0.23]

# 直接索引
print(ser2[2008])  # 1.78

print(ser2 * 2)
# 2008    3.56
# 2009    0.46
# dtype: float64

# DataFrame
demo_arr = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
df = pd.DataFrame(demo_arr)
print(df)
#    0  1  2
# 0  a  b  c
# 1  d  e  f

df = pd.DataFrame(demo_arr, columns=['No1', 'No2', 'No3'])
print(df)
#   No1 No2 No3
# 0   a   b   c
# 1   d   e   f

# 索引
element = df['No2']  # 返回的是Series类型
print(element)
# 0    b
# 1    e
# Name: No2, dtype: object

element = df.No2
print(element)
# 0    b
# 1    e
# Name: No2, dtype: object

# 扩展数据
df['No4'] = ['g', 'h']
print(df)
#   No1 No2 No3 No4
# 0   a   b   c   g
# 1   d   e   f   h

# 删除数据
del df['No4']
print(df)

# Pandas索引操作及高级索引
# 索引对象
ser = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
ser_index = ser.index
print(ser_index)  # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
# index类型不可变
ser1 = pd.Series(range(3), index=['a', 'b', 'c'])
ser2 = pd.Series(['a', 'b', 'c'], index=ser1.index)  # 共用相同的索引
print(ser1.index is ser2.index)  # True

# 重置索引
ser = pd.Series([1, 2, 3, 4, 5], index=['c', 'd', 'a', 'b', 'e'])
print(ser)
# c    1
# d    2
# a    3
# b    4
# e    5
# dtype: int64

ser2 = ser.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=6)  # 重置超出范围时，使用6填充
print(ser2)
# a    3
# b    4
# c    1
# d    2
# e    5
# f    6
# dtype: int64

ser3 = pd.Series([1, 3, 5, 7], index=[0, 2, 4, 6])
print(ser3)
# 0    1
# 2    3
# 4    5
# 6    7
# dtype: int64

ser = ser3.reindex(range(6), method='ffill')  # 重新配置索引，不足时向前填充
print(ser)
# 0    1
# 1    1
# 2    3
# 3    3
# 4    5
# 5    5
# dtype: int64

ser = ser3.reindex(range(6), method='bfill')  # 不足时向后填充
print(ser)
# 0    1
# 1    3
# 2    3
# 3    5
# 4    5
# 5    7
# dtype: int64

# 索引操作
# Series的索引操作
ser = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(ser[2])  # 3 使用位置索引
print(ser['c'])  # 3 使用索引名索引

print(ser[2: 4])  # 不包含4位置
# c    3
# d    4
# dtype: int64
print(ser['c': 'e'])  # 包含'e'
# c    3
# d    4
# e    5
# dtype: int64

print(ser[[0, 2, 4]])  # 不连续位置
# a    1
# c    3
# e    5
# dtype: int64

print(ser[['a', 'c', 'd']])
# a    1
# c    3
# d    4
# dtype: int64

# 布尔型索引
ser_bool = ser > 2
print(ser_bool)
# a    False
# b    False
# c     True
# d     True
# e     True
# dtype: bool

print(ser[ser_bool])
# c    3
# d    4
# e    5
# dtype: int64

# DataFrame的索引操作

arr = np.arange(12).reshape(3, 4)
df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd'])
print(df)
#    a  b   c   d
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
print(df['b'])
# 0    1
# 1    5
# 2    9
# Name: b, dtype: int32

# 不连续索引
print(df[['b', 'd']])
#    b   d
# 0  1   3
# 1  5   7
# 2  9  11

print(df[:2])  # 使用切片获取第0-1行的数据
#    a  b  c  d
# 0  0  1  2  3
# 1  4  5  6  7

# 先使用切片获取0-2行的数据
# 再通过不连续索引获取b、d列的数据
print(df[:3][['b', 'd']])
#    b   d
# 0  1   3
# 1  5   7
# 2  9  11

# 使用Pandas方法索引
arr = np.arange(16).reshape(4, 4)
df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd'])
print(df)
#     a   b   c   d
# 0   0   1   2   3
# 1   4   5   6   7
# 2   8   9  10  11
# 3  12  13  14  15

print(df.loc[:, ['c', 'a']])
#     c   a
# 0   2   0
# 1   6   4
# 2  10   8
# 3  14  12

print(df.iloc[:, [2, 0]])  # 结果同上
print(df.loc[1:2, ['b', 'c']])
#    b   c
# 1  5   6
# 2  9  10

print(df.iloc[1:3, [1, 2]])
#    b   c
# 1  5   6
# 2  9  10

# 算术运算与数据对齐
obj_one = pd.Series(range(10, 13), index=range(3))
print(obj_one)
# 0    10
# 1    11
# 2    12
# dtype: int64

obj_two = pd.Series(range(20, 25), index=range(5))
print(obj_two)
# 0    20
# 1    21
# 2    22
# 3    23
# 4    24
# dtype: int64

print(obj_two + obj_one)
# 0    30.0
# 1    32.0
# 2    34.0
# 3     NaN
# 4     NaN
# dtype: float64

# 指定非对齐数据的填充数据
print(obj_one.add(obj_two, fill_value=0))
# 0    30.0
# 1    32.0
# 2    34.0
# 3    23.0
# 4    24.0
# dtype: float64

# 数据排序
# 按索引排序
ser = pd.Series(range(10, 15), index=[5, 3, 1, 3, 2])
print(ser)
# 5    10
# 3    11
# 1    12
# 3    13
# 2    14
# dtype: int64

print(ser.sort_index())  # 根据索引排序
# 1    12
# 2    14
# 3    11
# 3    13
# 5    10
# dtype: int64

print(ser.sort_index(ascending=False))  # 根据索引降序

df_obj = pd.DataFrame(np.arange(9).reshape(3, 3), index=[4, 3, 5])
print(df_obj)
#    0  1  2
# 4  0  1  2
# 3  3  4  5
# 5  6  7  8
print(df_obj.sort_index())  # 按索引升序
#    0  1  2
# 3  3  4  5
# 4  0  1  2
# 5  6  7  8
print(df_obj.sort_index(ascending=False))  # 降序
#    0  1  2
# 5  6  7  8
# 4  0  1  2
# 3  3  4  5

# 按值排序
ser = pd.Series([4, np.nan, 6, -3, 2])
print(ser)
# 0    4.0
# 1    NaN
# 2    6.0
# 3   -3.0
# 4    2.0
# dtype: float64

print(ser.sort_values())
# 3   -3.0
# 4    2.0
# 0    4.0
# 2    6.0
# 1    NaN
# dtype: float64

df_obj = pd.DataFrame([[0.4, -0.1, -0.3, 0.0],
                       [0.2, 0.6, -0.1, -0.7],
                       [0.8, 0.6, -0.5, 0.1]])
print(df_obj)
#      0    1    2    3
# 0  0.4 -0.1 -0.3  0.0
# 1  0.2  0.6 -0.1 -0.7
# 2  0.8  0.6 -0.5  0.1
print(df_obj.sort_values(by=2))  # 对列索引为2的数据进行排列
#      0    1    2    3
# 2  0.8  0.6 -0.5  0.1
# 0  0.4 -0.1 -0.3  0.0
# 1  0.2  0.6 -0.1 -0.7

# 统计计算与描述
# 常用的统计计算
df_obj = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'c', 'd'])
print(df_obj)
#    a  b   c   d
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

print(df_obj.sum())  # 计算每列和
# a    12
# b    15
# c    18
# d    21
# dtype: int64

print(df_obj.max())
# a     8
# b     9
# c    10
# d    11
# dtype: int32

print(df_obj.min())
# a    0
# b    1
# c    2
# d    3
# dtype: int32

print(df_obj.min(axis=1))  # 获取每行最小值
# 0    0
# 1    4
# 2    8
# dtype: int32

# 统计描述
print(df_obj.describe())
#          a    b     c     d
# count  3.0  3.0   3.0   3.0
# mean   4.0  5.0   6.0   7.0
# std    4.0  4.0   4.0   4.0
# min    0.0  1.0   2.0   3.0
# 25%    2.0  3.0   4.0   5.0
# 50%    4.0  5.0   6.0   7.0
# 75%    6.0  7.0   8.0   9.0
# max    8.0  9.0  10.0  11.0

# 层次化索引
# 创建两层索引结构的Series对象
ser = pd.Series([15848, 13472, 12073.8,
                 7813, 7446, 6444, 15230, 8269],
                index=[['河北省', '河北省', '河北省', '河北省', '河南省', '河南省', '河南省', '河南省'],
                       ['石家庄市', '唐山市', '邯郸市', '秦皇岛市', '郑州市', '开封市', '洛阳市', '新乡市']])
print(ser)
# 河北省  石家庄市    15848.0
#      唐山市     13472.0
#      邯郸市     12073.8
#      秦皇岛市     7813.0
# 河南省  郑州市      7446.0
#      开封市      6444.0
#      洛阳市     15230.0
#      新乡市      8269.0
# dtype: float64

# 创建两层索引结构的DataFrame对象
mulitindex_df = pd.DataFrame({'占地面积': [15848, 13472, 12073.8,
                                       7813, 7446, 6444, 15230, 8269]})
print(mulitindex_df)
#       占地面积
# 0  15848.0
# 1  13472.0
# 2  12073.8
# 3   7813.0
# 4   7446.0
# 5   6444.0
# 6  15230.0
# 7   8269.0

mulitindex_df = pd.DataFrame({'占地面积': [15848, 13472, 12073.8,
                                       7813, 7446, 6444, 15230, 8269]},
                             index=[['河北省', '河北省', '河北省', '河北省', '河南省', '河南省', '河南省', '河南省'],
                             ['石家庄市', '唐山市', '邯郸市', '秦皇岛市', '郑州市', '开封市', '洛阳市', '新乡市']])
print(mulitindex_df)

#             占地面积
# 河北省 石家庄市  15848.0
#     唐山市   13472.0
#     邯郸市   12073.8
#     秦皇岛市   7813.0
# 河南省 郑州市    7446.0
#     开封市    6444.0
#     洛阳市   15230.0
#     新乡市    8269.0

# 创建层次化索引的方法
list_tuples = [('A', 'A1'), ('A', 'A2'), ('B', 'B1'), ('B', 'B2'), ('B', 'B3')]
multi_index = pd.MultiIndex.from_tuples(tuples=list_tuples, names=['外层索引', '外层索引'])
print(multi_index)
# MultiIndex([('A', 'A1'),
#             ('A', 'A2'),
#             ('B', 'B1'),
#             ('B', 'B2'),
#             ('B', 'B3')],
#            names=['外层索引', '外层索引'])

values = [[1, 2, 3], [8, 5, 7], [4, 7, 7], [5, 5, 4], [4, 9, 9]]
df = pd.DataFrame(data=values, index=multi_index)
print(df)
# 外层索引 外层索引
# A    A1    1  2  3
#      A2    8  5  7
# B    B1    4  7  7
#      B2    5  5  4
#      B3    4  9  9

multi_array = pd.MultiIndex.from_arrays(arrays=[['A', 'B', 'A', 'B', 'B'],
                                                ['A1', 'A2', 'B1', 'B2', 'B3']],
                                        names=['外层索引', '内层索引'])
values = np.array([[1, 2, 3], [8, 5, 7], [4, 7, 7], [5, 5, 4], [4, 9, 9]])
df = pd.DataFrame(data=values, index=multi_array)
print(df)
# 外层索引 内层索引
# A    A1    1  2  3
# B    A2    8  5  7
# A    B1    4  7  7
# B    B2    5  5  4
#      B3    4  9  9

numbers = [0, 1, 2]
colors = ['green', 'purple']
multi_product = pd.MultiIndex.from_product(
    iterables=[numbers, colors],
    names=['names', 'colors'])
values = np.array([[7, 5], [6, 6], [3, 1], [5, 5], [4, 5], [5, 3]])
df_product = pd.DataFrame(data=values, index=multi_product)
print(df_product)
# names colors
# 0     green   7  5
#       purple  6  6
# 1     green   3  1
#       purple  5  5
# 2     green   4  5
#       purple  5  3

# 层次化索引操作
print(ser['河北省'])
# 石家庄市    15848.0
# 唐山市     13472.0
# 邯郸市     12073.8
# 秦皇岛市     7813.0
# dtype: float64

print(ser[:, '邯郸市'])
# 河北省    12073.8
# dtype: float64

# 交换分层顺序
print(ser.swaplevel())
# 石家庄市  河北省    15848.0
# 唐山市   河北省    13472.0
# 邯郸市   河北省    12073.8
# 秦皇岛市  河北省     7813.0
# 郑州市   河南省     7446.0
# 开封市   河南省     6444.0
# 洛阳市   河南省    15230.0
# 新乡市   河南省     8269.0
# dtype: float64

# 排序分层
df_obj = pd.DataFrame({'word': ['a', 'b', 'd', 'e', 'f', 'k', 'd', 's', 'l'],
                       'num': [1, 2, 4, 5, 3, 2, 6, 2, 3]},
                      index=[['A', 'A', 'A', 'C', 'C', 'C', 'B', 'B', 'B'],
                             [1, 3, 2, 3, 1, 2, 4, 5, 8]])
print(df_obj)
#     word  num
# A 1    a    1
#   3    b    2
#   2    d    4
# C 3    e    5
#   1    f    3
#   2    k    2
# B 4    d    6
#   5    s    2
#   8    l    3

print(df_obj.sort_index())  # 第一层索引
#     word  num
# A 1    a    1
#   2    d    4
#   3    b    2
# B 4    d    6
#   5    s    2
#   8    l    3
# C 1    f    3
#   2    k    2
#   3    e    5

print(df_obj.sort_values(by=['num'], ascending=False))
#     word  num
# B 4    d    6
# C 3    e    5
# A 2    d    4
# C 1    f    3
# B 8    l    3
# A 3    b    2
# C 2    k    2
# B 5    s    2
# A 1    a    1

# 读写数据操作
df = pd.DataFrame({'One_name': [1, 2, 3], 'Two_name': [4, 5, 6]})
df.to_csv(r'D:\其他文件\itcast.csv')

file = open(r'D:\其他文件\itcast.csv')
file_data = pd.read_csv(file)
print(file_data)
file.close()
#    Unnamed: 0  One_name  Two_name
# 0           0         1         4
# 1           1         2         5
# 2           2         3         6

# 读写Excel文件
df1 = pd.DataFrame({'col1': ['传', '志'], 'col2': ['课', '家']})
print(df1)
#   col1 col2
# 0    传    课
# 1    志    家

df1.to_excel(r'D:\其他文件\itcast.xlsx')

# 读取Excel文件
data = pd.read_excel(r'D:\其他文件\itcast.xlsx')
print(data)
#    Unnamed: 0 col1 col2
# 0           0    传    课
# 1           1    志    家

# 案例分析：武汉肺炎情况分析
data = pd.read_excel(r'D:\其他文件\武汉肺炎.xlsx',  index_col='Unnamed: 0')
print(data)
print(data.max())
# 时间    44196.0
# 湖北      198.0
# 泰国        2.0
# 日本        1.0
# 上海        1.0
# 广东       14.0
# 北京        5.0
# 韩国        1.0

ser_data = data['广东']
print(ser_data)
# 1月1日      NaN
# 1月2日      NaN
# 1月3日      NaN
# 1月4日      NaN
# 1月5日      NaN
# 1月6日      NaN
# 1月7日      NaN
# 1月8日      NaN
# 1月9日      NaN
# 1月10日    14.0
# Name: 广东, dtype: float64

print(data.describe())
#                湖北        泰国   日本   上海    广东   北京   韩国
# count   10.000000  6.000000  5.0  1.0   1.0  1.0  1.0
# mean    75.600000  1.666667  1.0  1.0  14.0  5.0  1.0
# std     65.245179  0.516398  0.0  NaN   NaN  NaN  NaN
# min     27.000000  1.000000  1.0  1.0  14.0  5.0  1.0
# 25%     41.000000  1.250000  1.0  1.0  14.0  5.0  1.0
# 50%     44.500000  2.000000  1.0  1.0  14.0  5.0  1.0
# 75%     61.250000  2.000000  1.0  1.0  14.0  5.0  1.0
# max    198.000000  2.000000  1.0  1.0  14.0  5.0  1.0


