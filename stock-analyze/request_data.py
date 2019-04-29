from pandas_datareader import data
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import yin_candle as yin
import numpy as np
import datetime
# stock_code = input("美股直接输入股票代码如GOOG \n港股输入代码+对应股市，如腾讯：0700.hk \n国内股票需要区分上证和深证，股票代码后面加.ss或者.sz\n请输入你要查询的股票代码：")
stock_code = '000001.sz'

start_date = "2017-12-03"
end_date = "2019-04-23"

stock_info = data.get_data_yahoo(stock_code, start_date, end_date)

register_matplotlib_converters()

#  保存为Excel文件和CSV文件
stock_info.to_excel('%s.xlsx'%stock_code)
stock_info.to_csv('%s.csv'%stock_code)

# 输出图表
# 线图
# plt.plot(stock_info['Close'], 'g')
# plt.show()

# 阴烛图
stock_info["20d"] = np.round(stock_info["Close"].rolling(window=20, center=False).mean(), 2)
stock_info["30d"] = np.round(stock_info["Close"].rolling(window=30, center=False).mean(), 2)
stock_info["40d"] = np.round(stock_info["Close"].rolling(window=40, center=False).mean(), 2)
yin.pandas_candlestick_ohlc(stock_info.loc[start_date:end_date, :], otherseries=["20d", "30d", "40d"])
# yin.pandas_candlestick_ohlc(stock_info)

