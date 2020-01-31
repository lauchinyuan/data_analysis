import pandas as pd
import DateTime
import numpy as np
import matplotlib.pyplot as plt

# 创建时间序列
print(pd.to_datetime('20180828'))
# 2018-08-28 00:00:00

# 传入多个Datetime组成的列表,强制转换为DatetimeIndex对象
date_index = pd.to_datetime(['20180820', '20180828', '20180908'])
print(date_index)
# DatetimeIndex(['2018-08-20', '2018-08-28', '2018-09-08'], dtype='datetime64[ns]', freq=None)
print(date_index[0])  # 2018-08-20 00:00:00

# 使用时间索引
date_ser = pd.Series([11, 22, 33], index=date_index)
print(date_ser)
# 2018-08-20    11
# 2018-08-28    22
# 2018-09-08    33

# 创建时间索引的其他方法
date_list = [DateTime.DateTime(2018, 1, 1), DateTime.DateTime(2018, 2, 1)]
date_ser = pd.Series([11, 22], index=date_list)
print(date_ser)
# 2018/01/01 00:00:00 GMT+8    11
# 2018/02/01 00:00:00 GMT+8    22
# dtype: int64

# DataFrame使用时间索引
data_demo = [[11, 22, 33], [44, 55, 66]]
date_list = [DateTime.DateTime(2018, 1, 1), DateTime.DateTime(2018, 1, 2)]
print(pd.DataFrame(data_demo, index=date_list))
#                             0   1   2
# 2018/01/01 00:00:00 GMT+8  11  22  33
# 2018/01/02 00:00:00 GMT+8  44  55  66

# 通过时间戳索引选取子集
# 指定日期字符串列表
date_list = ['2020/05/20', '2020/02/18',
             '2015.6.1', '2018.9.1',
             '2010.9.18', '2019.9.8']
# 转换为DatetimeIndex索引
date_index = pd.to_datetime(date_list)
date_se = pd.Series(np.arange(6), index=date_index)
print(date_se)
# 2020-05-20    0
# 2020-02-18    1
# 2015-06-01    2
# 2018-09-01    3
# 2010-09-18    4
# 2019-09-08    5
# dtype: int32

# 根据位置索引获取数据
print(date_se[3])
# 3
# 根据日期索引索引数据
date_time = pd.to_datetime(['2020, 2, 18'])
print(date_se[date_time])
# 2020-02-18    1

print(date_se['20200218'])  # 结果同上
print(date_se['2020-05-20'])
print(date_se['2018/05/20'])
print(date_se['05/20/2020'])

# 可以直接通过年、月索引
print(date_se['2020'])
# 2020-05-20    0
# 2020-02-18    1
# dtype: int32

# 截取Series、DataFrame对象
# 扔掉2018年9月1日之前的数据
sort_se = date_se.sort_index()
sort_se = sort_se.truncate(before='20180901')
# 扔掉2020年2月18日之后的数据
sort_se = sort_se.truncate(after='20200218')
print(sort_se)

# 固定频率的时间序列
# 创建固定频率的时间序列
print(pd.date_range('2020/01/30', '2020/02/24'))
# DatetimeIndex(['2020-01-30', '2020-01-31', '2020-02-01', '2020-02-02',
#                '2020-02-03', '2020-02-04', '2020-02-05', '2020-02-06',
#                '2020-02-07', '2020-02-08', '2020-02-09', '2020-02-10',
#                '2020-02-11', '2020-02-12', '2020-02-13', '2020-02-14',
#                '2020-02-15', '2020-02-16', '2020-02-17', '2020-02-18',
#                '2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22',
#                '2020-02-23', '2020-02-24'],
#               dtype='datetime64[ns]', freq='D')

print(pd.date_range(start='20200120', periods=9))
# DatetimeIndex(['2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23',
#                '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27',
#                '2020-01-28'],
#               dtype='datetime64[ns]', freq='D')

print(pd.date_range(end='20200120', periods=9))
# DatetimeIndex(['2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15',
#                '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19',
#                '2020-01-20'],
#               dtype='datetime64[ns]', freq='D')

# 设置频率
# 连续生成5个星期日的日期
dates_index = pd.date_range('20180213', periods=5, freq='W-SUN')
print(dates_index)

# 创建DatetimeIndex并指定开始日期、频率及时区
print(pd.date_range(start='20200213 12:12:12', periods=4, tz='Asia/Taipei'))
# DatetimeIndex(['2020-02-13 12:12:12+08:00', '2020-02-14 12:12:12+08:00',
#                '2020-02-15 12:12:12+08:00', '2020-02-16 12:12:12+08:00'],
#               dtype='datetime64[ns, Asia/Taipei]', freq='D')

# 规范化时间戳
print(pd.date_range(start='20200213 12:12:12', periods=4, tz='Asia/Taipei', normalize=True))
# DatetimeIndex(['2020-02-13 00:00:00+08:00', '2020-02-14 00:00:00+08:00',
#                '2020-02-15 00:00:00+08:00', '2020-02-16 00:00:00+08:00'],
#               dtype='datetime64[ns, Asia/Taipei]', freq='D')

# 时间序列的频率、偏移量
# 频率为5天
print(pd.date_range(start='20130211', end='20130311', freq='5D'))
# DatetimeIndex(['2013-02-11', '2013-02-16', '2013-02-21', '2013-02-26',
#                '2013-03-03', '2013-03-08'],
#               dtype='datetime64[ns]', freq='5D')

# 时间序列的移动
date_index = pd.date_range('20180101', periods=5)
time_ser = pd.Series(np.arange(5), index=date_index)
print(time_ser)
# 2018-01-01    0
# 2018-01-02    1
# 2018-01-03    2
# 2018-01-04    3
# 2018-01-05    4
# Freq: D, dtype: int32

# 向后移动一次
print(time_ser.shift(1))
# 2018-01-01    NaN
# 2018-01-02    0.0
# 2018-01-03    1.0
# 2018-01-04    2.0
# 2018-01-05    3.0
# Freq: D, dtype: float64

# 向前移动一次
print(time_ser.shift(-1))
# 2018-01-01    1.0
# 2018-01-02    2.0
# 2018-01-03    3.0
# 2018-01-04    4.0
# 2018-01-05    NaN

# 时间周期计算
# 创建时期对象
print(pd.Period(2018))
period = pd.Period('2017/6')
print(period)
# 参与运算
print(period + 1)
# 2017-07

# 相同频率的Period对象运算
other_period = pd.Period('201201', freq='M')
print(period - other_period)
# <65 * MonthEnds>

# 创建多个相同频率的Period对象
period_index = pd.period_range('20190831', '20200101', freq='M')
print(period_index)
# PeriodIndex(['2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01'], dtype='period[M]', freq='M')

str_list = ['2018', '2019', '2020']
print(pd.PeriodIndex(str_list, freq='A-DEC'))
# PeriodIndex(['2018', '2019', '2020'], dtype='period[A-DEC]', freq='A-DEC')

# 时期频率转换
period = pd.Period('2017', freq='A-DEC')
# 转换时期频率
print(period.asfreq('M', how='start'))
# 2017-01
print(period.asfreq('M', how='end'))
# 2017-12

# 重采样
# 重采样方法（resample）
date_index = pd.date_range('2017.7.8', periods=30)
time_ser = pd.Series(np.arange(30), index=date_index)
print(time_ser)
# 2017-07-08     0
# 2017-07-09     1
# 2017-07-10     2
# 2017-07-11     3
# 2017-07-12     4
# 2017-07-13     5
# 2017-07-14     6
# 2017-07-15     7
# 2017-07-16     8
# 2017-07-17     9
# 2017-07-18    10
# 2017-07-19    11
# 2017-07-20    12
# 2017-07-21    13
# 2017-07-22    14
# 2017-07-23    15
# 2017-07-24    16
# 2017-07-25    17
# 2017-07-26    18
# 2017-07-27    19
# 2017-07-28    20
# 2017-07-29    21
# 2017-07-30    22
# 2017-07-31    23
# 2017-08-01    24
# 2017-08-02    25
# 2017-08-03    26
# 2017-08-04    27
# 2017-08-05    28
# 2017-08-06    29
# Freq: D, dtype: int32

# 重采样
print(time_ser.resample('W-MON').mean())
# 2017-07-10     1.0
# 2017-07-17     6.0
# 2017-07-24    13.0
# 2017-07-31    20.0
# 2017-08-07    26.5
# Freq: W-MON, dtype: float64

print(time_ser.resample('W-MON', closed='left').mean())  # 开头时间戳包含在内，结尾时间戳不包含

# 降采样
date_index = pd.date_range('20180601', periods=30)
shares_data = np.random.rand(30)
time_ser = pd.Series(shares_data, index=date_index)
print(time_ser)
print(time_ser.resample('7D').ohlc())
#                 open      high       low     close
# 2018-06-01  0.692523  0.692523  0.298606  0.448020
# 2018-06-08  0.606094  0.834172  0.105210  0.834172
# 2018-06-15  0.553285  0.828883  0.097969  0.763551
# 2018-06-22  0.244660  0.810596  0.244660  0.810596
# 2018-06-29  0.455063  0.455063  0.360989  0.360989

# 升采样
data_demo = np.array([['101', '210', '105'], ['330', '460', '580']])
date_index = pd.date_range('20200210', periods=2, freq='W-SUN')
time_df = pd.DataFrame(data_demo, index=date_index, columns=['A产品', 'B产品', 'C产品'])
print(time_df)
#             A产品  B产品  C产品
# 2020-02-16  101  210  105
# 2020-02-23  330  460  580
print(time_df.resample('D').asfreq())
#             A产品  B产品  C产品
# 2020-02-16  101  210  105
# 2020-02-17  NaN  NaN  NaN
# 2020-02-18  NaN  NaN  NaN
# 2020-02-19  NaN  NaN  NaN
# 2020-02-20  NaN  NaN  NaN
# 2020-02-21  NaN  NaN  NaN
# 2020-02-22  NaN  NaN  NaN
# 2020-02-23  330  460  580

# 向后填充
print(time_df.resample('D').ffill())
#             A产品  B产品  C产品
# 2020-02-16  101  210  105
# 2020-02-17  101  210  105
# 2020-02-18  101  210  105
# 2020-02-19  101  210  105
# 2020-02-20  101  210  105
# 2020-02-21  101  210  105
# 2020-02-22  101  210  105
# 2020-02-23  330  460  58

# 数据统计--滑动窗口
year_data = np.random.randn(365)
date_index = pd.date_range('2017-01-01', '2017-12-31', freq='D')
ser = pd.Series(year_data, date_index)
# 创建滑动窗口
roll_windows = ser.rolling(window=10)
print(roll_windows)  # 返回Rolling对象
# Rolling [window=10,center=False,axis=0]
# 窗口数据平均值
print(roll_windows.mean())
# 2017-01-01         NaN
# 2017-01-02         NaN
# 2017-01-03         NaN
# 2017-01-04         NaN
# 2017-01-05         NaN
#                 ...
# 2017-12-27    0.251326
# 2017-12-28    0.270747
# 2017-12-29    0.337449
# 2017-12-30    0.297029
# 2017-12-31    0.124344

# 数据比较
ser.plot(style='y--')
ser_windows = ser.rolling(window=10).mean()
ser_windows.plot(style='b')
plt.show()

# 时序模型--ARIMA



