from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import date2num
import numpy as np
import datetime

"""
:param dat: pandas DataFrame object with datetime64 index, and float columns "Open", "High", "Low", and "Close", likely created via DataReader from "yahoo"
:param stick: A string or number indicating the period of time covered by a single candlestick. Valid string inputs include "day", "week", "month", and "year", ("day" default), and any numeric input indicates the number of trading days included in a period
:param otherseries: An iterable that will be coerced into a list, containing the columns of dat that hold other series to be plotted as lines

This will show a Japanese candlestick plot for stock data stored in dat, also plotting other series if passed.
"""
def pandas_candlestick_ohlc(dat, stick="day", otherseries=None):

    mondays = WeekdayLocator(MONDAY)  # major ticks on the mondays
    alldays = DayLocator()  # minor ticks on the days
    dayFormatter = DateFormatter('%d')  # e.g., 12

    # Create a new DataFrame which includes OHLC data for each period specified by stick input
    # dat.loc[] - - 通过行标签索引行数据
    transdat = dat.loc[:, ["Open", "High", "Low", "Close"]]
    if (type(stick) == str):
        if stick == "day":
            plotdat = transdat
            stick = 1  # 用于绘制
        elif stick in ["week", "month", "year"]:
            if stick == "week":
                transdat["week"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[1])  # Identify weeks
            elif stick == "month":
                transdat["month"] = pd.to_datetime(transdat.index).map(lambda x: x.month)  # Identify months
            transdat["year"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[0])  # Identify years
            grouped = transdat.groupby(list(set(["year", stick])))  # Group by year and other appropriate variable
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [],
                                    "Close": []})  # Create empty data frame containing what will be plotted
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                       "High": max(group.High),
                                                       "Low": min(group.Low),
                                                       "Close": group.iloc[-1, 3]},
                                                      index=[group.index[0]]))
            if stick == "week":
                stick = 5
            elif stick == "month":
                stick = 30
            elif stick == "year":
                stick = 365

    elif (type(stick) == int and stick >= 1):
        transdat["stick"] = [np.floor(i / stick) for i in range(len(transdat.index))]
        grouped = transdat.groupby("stick")
        plotdat = pd.DataFrame(
            {"Open": [], "High": [], "Low": [], "Close": []})  # Create empty data frame containing what will be plotted
        for name, group in grouped:
            plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                   "High": max(group.High),
                                                   "Low": min(group.Low),
                                                   "Close": group.iloc[-1, 3]},
                                                  index=[group.index[0]]))

    else:
        raise ValueError(
            'Valid inputs to argument "stick" include the strings "day", "week", "month", "year", or a positive integer')

    # 设置绘图参数，包括用于绘图的axis对象ax
    fig, ax = plt.subplots(figsize=(13.0, 6.0))
    # fig = plt.figure(figsize=(12.0, 13.0), dpi=1200)
    fig.subplots_adjust(bottom=0.13)

    # 判断数据（数组形式）的长度是否大于730天
    if plotdat.index[-1] - plotdat.index[0] < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%Y-%m-%d')  # 设置时间格式
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%Y-%m-%d')  # 设置时间格式

    # 将时间格式设置入X轴
    ax.xaxis.set_major_formatter(weekFormatter)
    # 是否显示网格
    ax.grid(True)

    # 处理时间
    timeBefore = plotdat.index.tolist()
    timeAfter = []
    for time01 in timeBefore:
        timeAfter.append(date2num(datetime.datetime.strptime(str(time01), '%Y-%m-%d %H:%M:%S')))

    # 创建阴烛图表
    candlestick_ohlc(ax,  # 坐标轴
                     list(zip(timeAfter,
                              plotdat["Open"].tolist(),
                              plotdat["High"].tolist(),
                              plotdat["Low"].tolist(),
                              plotdat["Close"].tolist())),
                     colorup="red",  # 上涨的颜色
                     colordown="green",  # 下跌的颜色
                     width=stick * .4)  # 宽度

    # Plot other series (such as moving averages) as lines
    if otherseries != None:
        if type(otherseries) != list:
            otherseries = [otherseries]
        dat.loc[:, otherseries].plot(ax=ax, lw=1.3, grid=True)

    ax.xaxis_date()
    ax.autoscale_view()

    plt.setp(plt.gca().get_xticklabels(),
             rotation=45,
             horizontalalignment='right')

    # 保存图片
    plt.savefig('stock.png')

    # plt.show()


