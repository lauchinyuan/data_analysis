import pandas as pd
import numpy as np
df = pd.DataFrame({'key': ['C', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A'],
                   'Data': [2, 4, 6, 8, 10, 1, 14, 16, 18]})
print(df)
#   key  Data
# 0   C     2
# 1   B     4
# 2   C     6
# 3   A     8
# 4   B    10
# 5   B     1
# 6   A    14
# 7   C    16
# 8   A    18

# 通过列名进行分组
group_obj = df.groupby('key')
for i in group_obj:
    print(i)
# ('A',   key  Data
# 3   A     8
# 6   A    14
# 8   A    18)
# ('B',   key  Data
# 1   B     4
# 4   B    10
# 5   B     1)
# ('C',   key  Data
# 0   C     2
# 2   C     6
# 7   C    16)

# 通过Series对象进行分组
df = pd.DataFrame({'key1': ['A', 'A', 'B', 'B', 'A'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': [2, 3, 4, 6, 8],
                   'data2': [3, 5, 6, 3, 7]})
print(df)
#   key1 key2  data1  data2
# 0    A  one      2      3
# 1    A  two      3      5
# 2    B  one      4      6
# 3    B  two      6      3
# 4    A  one      8      7

se = pd.Series(['a', 'b', 'c', 'a', 'b'])
print(se)
# 0    a
# 1    b
# 2    c
# 3    a
# 4    b
# dtype: object

group_obj = df.groupby(by=se)
for i in group_obj:
    print(i)
# ('a',   key1 key2  data1  data2
# 0    A  one      2      3
# 3    B  two      6      3)
# ('b',   key1 key2  data1  data2
# 1    A  two      3      5
# 4    A  one      8      7)
# ('c',   key1 key2  data1  data2
# 2    B  one      4      6)

# 当Series长度与源数据的索引值长度不同时
se = pd.Series(['a', 'a', 'b'])
group_obj = df.groupby(by=se)
for i in group_obj:
    print(i)

# ('a',   key1 key2  data1  data2
# 0    A  one      2      3
# 1    A  two      3      5)
# ('b',   key1 key2  data1  data2
# 2    B  one      4      6)

# 通过字典进行分组
num_df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                       'b': [6, 7, 8, 9, 10],
                       'c': [11, 12, 13, 14, 15],
                       'd': [5, 4, 3, 2, 1],
                       'e': [10, 9, 8, 7, 6]})
print(num_df)
#    a   b   c  d   e
# 0  1   6  11  5  10
# 1  2   7  12  4   9
# 2  3   8  13  3   8
# 3  4   9  14  2   7
# 4  5  10  15  1   6

mapping = {'a': '第一组', 'b': '第二组', 'c': '第一组', 'd': '第三组', 'e': '第二组'}
by_columns = num_df.groupby(mapping, axis=1)
for i in by_columns:
    print(i)
# ('第一组',    a   c
# 0  1  11
# 1  2  12
# 2  3  13
# 3  4  14
# 4  5  15)
# ('第三组',    d
# 0  5
# 1  4
# 2  3
# 3  2
# 4  1)
# ('第二组',     b   e
# 0   6  10
# 1   7   9
# 2   8   8
# 3   9   7
# 4  10   6)

# 通过函数进行分组
df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                   'b': [6, 7, 8, 9, 10],
                   'c': [5, 4, 3, 2, 1]},
                  index=['Sun', 'Jack', 'Alice', 'Helen', 'Job'])
print(df)
#        a   b  c
# Sun    1   6  5
# Jack   2   7  4
# Alice  3   8  3
# Helen  4   9  2
# Job    5  10  1

# 依据索引长度函数分组
group_obj = df.groupby(len)
for i in group_obj:
    print(i)
# (3,      a   b  c
# Sun  1   6  5
# Job  5  10  1)
# (4,       a  b  c
# Jack  2  7  4)
# (5,        a  b  c
# Alice  3  8  3
# Helen  4  9  2)

# 数据聚合
# 使用内置统计方法聚合数据
df = pd.DataFrame({'key1': ['A', 'A', 'B', 'B', 'A'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': [2, 3, 4, 6, 8],
                   'data2': [3, 5, np.nan, 3, 7]})
print(df)
#   key1 key2  data1  data2
# 0    A  one      2    3.0
# 1    A  two      3    5.0
# 2    B  one      4    NaN
# 3    B  two      6    3.0
# 4    A  one      8    7.0
print(df.groupby('key1').mean())
#          data1  data2
# key1
# A     4.333333    5.0
# B     5.000000    3.0

# 面向列的聚合方法
# 对每一列数据应用同一个函数
data_frame = pd.DataFrame(np.arange(36).reshape(6, 6), columns=list('abcdef'))
data_frame['key'] = pd.Series(list('aaabbb'), name='key')
print(data_frame)
#     a   b   c   d   e   f key
# 0   0   1   2   3   4   5   a
# 1   6   7   8   9  10  11   a
# 2  12  13  14  15  16  17   a
# 3  18  19  20  21  22  23   b
# 4  24  25  26  27  28  29   b
# 5  30  31  32  33  34  35   b

data_group = data_frame.groupby('key')
print(data_group)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x08330890>
dict_data = dict([x for x in data_group])
print(dict_data['a'])
#     a   b   c   d   e   f key
# 0   0   1   2   3   4   5   a
# 1   6   7   8   9  10  11   a
# 2  12  13  14  15  16  17   a
print(dict_data['b'])
#     a   b   c   d   e   f key
# 3  18  19  20  21  22  23   b
# 4  24  25  26  27  28  29   b
# 5  30  31  32  33  34  35   b

# 对同一组作函数处理
print(data_group.agg(sum))
#       a   b   c   d   e   f
# key
# a    18  21  24  27  30  33
# b    72  75  78  81  84  87


# 传入自定义函数
def range_data_group(arr):
    return arr.max() - arr.min()


print(data_group.agg(range_data_group))
#       a   b   c   d   e   f
# key
# a    12  12  12  12  12  12
# b    12  12  12  12  12  12

# 对某列数据应用不同函数
print(data_group.agg([sum, range_data_group]))
#       a                    b  ...                e   f
#     sum range_data_group sum  ... range_data_group sum range_data_group
# key                           ...
# a    18               12  21  ...               12  33               12
# b    72               12  75  ...               12  87               12
print(data_group.agg([('极差', range_data_group), ('和', sum)]))
#       a       b       c       d       e       f
#      极差   和  极差   和  极差   和  极差   和  极差   和  极差   和
# key
# a    12    18    12  21    12  24    12  27     12  30    12  33
# b    12    72    12  75    12  78    12  81     12  84    12  87

# 对不同列数据应用不同函数
print(data_group.agg({'a': 'sum', 'b': 'mean', 'c': range_data_group}))
#       a   b   c
# key
# a    18   7  12
# b    72  25  12

# 分组级运算
df = pd.DataFrame({'a': [0, 1, 6, 10, 3],
                   'b': [1, 2, 7, 11, 4],
                   'c': [2, 3, 8, 12, 4],
                   'd': [3, 4, 9, 13, 5],
                   'e': [4, 5, 10, 14, 3],
                   'key': ['A', 'A', 'B', 'B', 'B']})
print(df)
#     a   b   c   d   e key
# 0   0   1   2   3   4   A
# 1   1   2   3   4   5   A
# 2   6   7   8   9  10   B
# 3  10  11  12  13  14   B
# 4   3   4   4   5   3   B

print(df.groupby('key').transform('mean'))
#           a         b    c    d    e
# 0  0.500000  1.500000  2.5  3.5  4.5
# 1  0.500000  1.500000  2.5  3.5  4.5
# 2  6.333333  7.333333  8.0  9.0  9.0
# 3  6.333333  7.333333  8.0  9.0  9.0
# 4  6.333333  7.333333  8.0  9.0  9.0

df = pd.DataFrame({'A': [2, 3, 3, 4, 2],
                   'B': [4, 2, 3, 6, 6],
                   'C': [9, 7, 0, 7, 8],
                   'D': [3, 4, 8, 6, 10]})
print(df)
#    A  B  C   D
# 0  2  4  9   3
# 1  3  2  7   4
# 2  3  3  0   8
# 3  4  6  7   6
# 4  2  6  8  10

key = ['one', 'one', 'two', 'two', 'two']
print(df.groupby(key).transform('mean'))
#      A  B  C    D
# 0  2.5  3  8  3.5
# 1  2.5  3  8  3.5
# 2  3.0  5  5  8.0
# 3  3.0  5  5  8.0
# 4  3.0  5  5  8.0

# 数据应用
df = pd.DataFrame({'data1': [80, 23, 25, 63, 94, 92, 99, 92, 82, 99],
                   'data2': [41, 87, 58, 68, 72, 89, 60, 42, 53, 65],
                   'data3': [30, 78, 23, 66, 16, 59, 20, 23, 24, 20],
                   'key': list('baabbabaaa')})
print(df)
#    data1  data2  data3 key
# 0     80     41     30   b
# 1     23     87     78   a
# 2     25     58     23   a
# 3     63     68     66   b
# 4     94     72     16   b
# 5     92     89     59   a
# 6     99     60     20   b
# 7     92     42     23   a
# 8     82     53     24   a
# 9     99     65     20   a

data_group = df.groupby('key')
dict_data = dict([x for x in data_group])
print(dict_data['a'])
#    data1  data2  data3 key
# 1     23     87     78   a
# 2     25     58     23   a
# 5     92     89     59   a
# 7     92     42     23   a
# 8     82     53     24   a
# 9     99     65     20   a
print(dict_data['b'])
#    data1  data2  data3 key
# 0     80     41     30   b
# 3     63     68     66   b
# 4     94     72     16   b
# 6     99     60     20   b


# 每个元素加10
def plus_ten(data):
    return data.iloc[:, :3] + 10


print(data_group.apply(plus_ten))
#    data1  data2  data3
# 0     90     51     40
# 1     33     97     88
# 2     35     68     33
# 3     73     78     76
# 4    104     82     26
# 5    102     99     69
# 6    109     70     30
# 7    102     52     33
# 8     92     63     34
# 9    109     75     30


