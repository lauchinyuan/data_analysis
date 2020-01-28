import pandas as pd
import numpy as np

# 空值和缺失值的处理
ser_obj = pd.Series([1, None, np.NaN])
print(pd.isnull(ser_obj))
# 0    False
# 1     True
# 2     True
# dtype: bool

print(pd.notnull(ser_obj))
# 0     True
# 1    False
# 2    False
# dtype: bool

df_obj = pd.DataFrame({'类别': ['小说', '散文随笔', '青春文学', '传记'],
                       '书名': [np.NaN, '《皮囊》', '《旅程结束时》', '《老舍自传》'],
                       '作者': ['老舍', None, '张启星', '老舍']})
print(df_obj)
#      类别       书名    作者
# 0    小说      NaN    老舍
# 1  散文随笔     《皮囊》  None
# 2  青春文学  《旅程结束时》   张启星
# 3    传记   《老舍自传》    老舍

print(df_obj.dropna())  # 删除数据中的空值和缺失值
#      类别       书名   作者
# 2  青春文学  《旅程结束时》  张启星
# 3    传记   《老舍自传》   老舍

# 填充空值、缺失值
print(df_obj.fillna('《武汉肺炎纪实》'))
#      类别        书名        作者
# 0    小说  《武汉肺炎纪实》        老舍
# 1  散文随笔      《皮囊》  《武汉肺炎纪实》
# 2  青春文学   《旅程结束时》       张启星
# 3    传记    《老舍自传》        老舍

print(df_obj.fillna({'书名': '《武汉肺炎纪实》', '作者': '刘方'}))
#     类别        书名   作者
# 0    小说  《武汉肺炎纪实》   老舍
# 1  散文随笔      《皮囊》   刘方
# 2  青春文学   《旅程结束时》  张启星
# 3    传记    《老舍自传》   老舍

# 重复值的处理
person_info = pd.DataFrame({'id': [1, 2, 3, 4, 4, 5],
                            'name': ['梁方', '金源', '程铮', '刘华', '刘华', '周华'],
                            'age': [18, 18, 29, 58, 58, 36]})
print(person_info)
#    id name  age
# 0   1   梁方   18
# 1   2   金源   18
# 2   3   程铮   29
# 3   4   刘华   58
# 4   4   刘华   58
# 5   5   周华   36

print(person_info.duplicated())  # 查找是否有重复值
# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# 5    False
# dtype: bool

print(person_info.drop_duplicates())  # 删去重复值


#    id name  age
# 0   1   梁方   18
# 1   2   金源   18
# 2   3   程铮   29
# 3   4   刘华   58
# 5   5   周华   36

# 异常值的处理
# 基于3σ原则检测异常值


def three_sigma(ser1):
    # 求平均值
    mean_value = ser1.mean()
    # 求标准差
    std_value = ser1.std()
    # 位于（μ - 3σ， μ + 3σ）数据为正常数据
    # 若有异常数据返回True
    rule = (mean_value - 3 * std_value > ser1) | (mean_value + 3 * std_value < ser1)
    # 返回异常数据的索引
    index = np.arange(ser1.shape[0])[rule]

    # 返回异常数据
    out_range = ser1.iloc[index]
    return out_range


df = pd.read_excel(r'D:\其他文件\data_test.xlsx')
print(df)
print(three_sigma(df['A']))
# 5    560
# Name: A, dtype: int64

# 基于箱型图进行检测
df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [2, 3, 5, 2],
                   'C': [1, 4, 7, 4],
                   'D': [1, 5, 30, 3]})
df.boxplot(column=['A', 'B', 'C', 'D'])

# 更改数据类型
# 指定数据类型
df = pd.DataFrame({'A': [5, 6, 7], 'B': [3, 2, 1]}, dtype=np.float)
print(df)

print(df.dtypes)
# A    float64
# B    float64
# dtype: object

# 更改数据类型
print(df['B'].astype(dtype='int'))

ser_obj = pd.Series(['1', '1.2', '4.2'])
print(ser_obj)
# 0      1
# 1    1.2
# 2    4.2
# dtype: object

print(pd.to_numeric(ser_obj, errors='raise'))
# 0    1.0
# 1    1.2
# 2    4.2
# dtype: float64

# 数据合并
# 横向堆叠与外连接
df1 = pd.DataFrame({'A': ['A0', 'A0', 'A1'],
                    'B': ['B0', 'B0', 'B1']})
df2 = pd.DataFrame({'C': ['C0', 'C0', 'C1', 'C3'],
                    'D': ['D0', 'D2', 'D2', 'D3']})
# 横向合并df1和df2,采用外连接方式
df_con = pd.concat([df1, df2], join='outer', axis=1)
print(df_con)
#      A    B   C   D
# 0   A0   B0  C0  D0
# 1   A0   B0  C0  D2
# 2   A1   B1  C1  D2
# 3  NaN  NaN  C3  D3

# 纵向堆叠与内连接
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2'],
                    'C': ['C0', 'C1', 'C2']})
df2 = pd.DataFrame({'B': ['B3', 'B4', 'B5'],
                    'C': ['C3', 'C4', 'C5'],
                    'D': ['D3', 'D4', 'D5']})
print(df1)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
print(df2)
#     B   C   D
# 0  B3  C3  D3
# 1  B4  C4  D4
# 2  B5  C5  D5

df_con = pd.concat([df1, df2], join='inner', axis=0)
print(df_con)
#     B   C
# 0  B0  C0
# 1  B1  C1
# 2  B2  C2
# 0  B3  C3
# 1  B4  C4
# 2  B5  C5

# 主键合并数据
left = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                     'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
# 2  K2  A2  B2
print(right)
#   key   C   D
# 0  K0  C0  D0
# 1  K1  C1  D1
# 2  K2  C2  D2
# 3  K3  C3  D3
df_con = pd.merge(left, right, on='key')
print(df_con)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2


left = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                     'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']})
right = pd.DataFrame({'key': ['K0', 'K5', 'K2', 'K4'],
                      'B': ['B0', 'B1', 'B2', 'B5'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
# 2  K2  A2  B2
print(right)
#   key   B   C   D
# 0  K0  B0  C0  D0
# 1  K5  B1  C1  D1
# 2  K2  B2  C2  D2
# 3  K4  B5  C3  D3

df_con = pd.merge(left, right, on=['key', 'B'])
print(df_con)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K2  A2  B2  C2  D2

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']})
right = pd.DataFrame({'C': ['C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['a', 'b', 'c'])
df_con = pd.merge(left, right, how='outer',
                  left_index=True, right_index=True)
print(df_con)
#      A    B    C    D
# 0   A0   B0  NaN  NaN
# 1   A1   B1  NaN  NaN
# 2   A2   B2  NaN  NaN
# a  NaN  NaN   C1   D0
# b  NaN  NaN   C2   D1
# c  NaN  NaN   C3   D2

# 根据行索引合并数据
left = pd.DataFrame({'A': ['A0', 'A1'],
                     'B': ['B0', 'B1']},
                    index=['a', 'b'])
right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                     index=['c', 'd'])
print(left)
#     A   B
# a  A0  B0
# b  A1  B1
print(right)
#     C   D
# c  C0  D0
# d  C1  D1
print(left.join(right, how='outer'))
#      A    B    C    D
# a   A0   B0  NaN  NaN
# b   A1   B1  NaN  NaN
# c  NaN  NaN   C0   D0
# d  NaN  NaN   C1   D1

# 表中行索引与列索引重叠时合并
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'key': ['K0', 'K1', 'K2']})
right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['K0', 'K1', 'K2'])
print(left)
#     A   B key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
print(right)
#      C   D
# K0  C0  D0
# K1  C1  D1
# K2  C2  D2
print(left.join(right, how='left', on='key'))
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2

# 合并重叠数据
left = pd.DataFrame({'A': [np.nan, 'A0', 'A1', 'A2'],
                     'B': [np.nan, 'B1', np.nan, 'B3'],
                     'key': ['K0', 'K1', 'K2', 'K3']})
right = pd.DataFrame({'A': ['C0', 'C1', 'C2'],
                      'B': ['D0', 'D1', 'D2']},
                     index=[1, 0, 2])
print(left)
#      A    B key
# 0  NaN  NaN  K0
# 1   A0   B1  K1
# 2   A1  NaN  K2
# 3   A2   B3  K3
print(right)
#     A   B
# 1  C0  D0
# 0  C1  D1
# 2  C2  D2
df_con = left.combine_first(right)
print(df_con)
#     A   B key
# 0  C1  D1  K0
# 1  A0  B1  K1
# 2  A1  D2  K2
# 3  A2  B3  K3

# 数据重塑
# 重塑层次化索引
df = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                   'B': ['B0', 'B1', 'B2']})
print(df)
#     A   B
# 0  A0  B0
# 1  A1  B1
# 2  A2  B2
# 对df进行重塑
result = df.stack()
print(result)  # 结果为Series对象
# 0  A    A0
#    B    B0
# 1  A    A1
#    B    B1
# 2  A    A2
#    B    B2

df = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                   'B': ['B0', 'B1', 'B2']})
print(df)
#     A   B
# 0  A0  B0
# 1  A1  B1
# 2  A2  B2
res = df.stack()
print(res.unstack())  # 解除重构
#     A   B
# 0  A0  B0
# 1  A1  B1
# 2  A2  B2

# 多重索引重塑
df = pd.DataFrame(np.array([[26, 20, 22, 26], [30, 25, 24, 20]]),
                  index=['男生人数', '女生人数'],
                  columns=[['一楼', '一楼', '二楼', '二楼'],
                           ['A教室', 'B教室', 'A教室', 'B教室']])
print(df)
#       一楼      二楼
#      A教室 B教室 A教室 B教室
# 男生人数  26  20  22  26
# 女生人数  30  25  24  20
print(df.stack())
#              一楼  二楼
# 男生人数 A教室  26  22
#         B教室  20  26
# 女生人数 A教室  30  24
#         B教室  25  20

print(df.stack(level=0))  # 旋转外层索引
#              A教室  B教室
# 男生人数 一楼   26   20
#         二楼   22   26
# 女生人数 一楼   30   25
#         二楼   24   20

# 轴向旋转
df = pd.DataFrame({'商品名称': ['荣耀9青春版', '小米6X', 'OPPO A1', '荣耀9青春版', '小米6X', 'OPPO A1'],
                   '出售日期': ['2017年5月25日', '2017年5月25日', '2017年5月25日',
                            '2017年6月18日', '2017年6月18日', '2017年6月18日'],
                   '价格': ['999元', '1399元', '1399元',
                          '800元', '1200元', '1250元']})
print(df)
#       商品名称            出售日期     价格
# 0     荣耀9青春版      2017年5月25日   999元
# 1     小米6X           2017年5月25日  1399元
# 2     OPPO A1         2017年5月25日  1399元
# 3     荣耀9青春版      2017年6月18日   800元
# 4     小米6X            2017年6月18日  1200元
# 5     OPPO A1         2017年6月18日  1250元

print(df.pivot(index='出售日期', columns='商品名称', values='价格'))
# 商品名称       OPPO A1   小米6X 荣耀9青春版
# 出售日期
# 2017年5月25日   1399元  1399元   999元
# 2017年6月18日   1250元  1200元   800元

# 数据转换
# 重命名轴索引
df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3']})
print(df)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

df.rename(columns={'A': 'a', 'B': 'b', 'C': 'c'}, inplace=True)
print(df)
#     a   b   c
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3


df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3']})
print(df)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3
print(df.rename(str.lower, axis='columns'))
#     a   b   c
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

# 重命名索引
df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3']})
print(df)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3
df.rename(index={1: 'a', 2: 'b'}, inplace=True)
print(df)
#     A   B   C
# 0  A0  B0  C0
# a  A1  B1  C1
# b  A2  B2  C2
# 3  A3  B3  C3

# 离散化连续数据
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 32]
bins = [0, 18, 25, 35, 60, 100]
cuts = pd.cut(ages, bins)
print(cuts)
# [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (35, 60], (25, 35], (60, 100], (35, 60], (25, 35]]
# Length: 11
# Categories (5, interval[int64]): [(0, 18] < (18, 25] < (25, 35] < (35, 60] < (60, 100]]

# 哑变量处理类别型数据
df1 = pd.DataFrame({'职业': ['工人', '学生', '教师']})
print(pd.get_dummies(df1))
#    职业_学生  职业_工人  职业_教师
# 0      0      1      0
# 1      1      0      0
# 2      0      0      1


