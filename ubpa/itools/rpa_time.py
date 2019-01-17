# -*- coding: utf-8 -*-
'''
RPA 对时间的处理
'''
import datetime
import time


def get_current_datetime_str(format="%Y-%m-%d"):
    '''
        get_current_datetime_str(format="%Y-%m-%d") -> str
        功能：
            以规定格式返回当前日期
        参数：
            format= "%Y-%m-%d"  输出的格式
        返回:
            规定格式的当前时间
        例子:
             get_current_datetime_str(format= "%Y-%m-%d") -> "2018-05-21"
    '''
    today = time.strftime(format, time.localtime())
    return today


def get_datetime_to_str(date_time, format="%Y-%m-%d"):
    '''
     get_datetime_to_str(date_time, format= "%Y-%m-%d")-> str
           功能：  将输入的时间 以规定的格式输出
           参数：
                   datet_ime: 输入的时间
                   format: 要输出的时间格式
           返回：
                   符合规定格式的时间
           例子：
                   get_datetime_to_str("2018-05-21", format= "%Y-%m-%d") -> "2018-05-01"
     '''

    str_datetime = datetime.datetime.strftime(date_time, format)
    return str_datetime



def dete_dalta_days(dt1, dt2, format1="%Y-%m-%d", format2="%Y-%m-%d"):
    '''
    dete_dalta_days(dt1, dt2, format1="%Y-%m-%d" , format2="%Y-%m-%d") -> int
        功能：输入符合规定模式的2个日期，计算2个日期间隔的日期差
        参数:
              dt1: %y -%m -%d    2018-01-05
              dt2: %y -%m -%d    2018-05-21
        返回：
              2个日期间隔的日期差
        例子：
              dt1:"2018-01-05"      dt2:"2018-11-25"     return : 324
    '''
    timeArray1 = time.strptime(dt1, format1)
    timeArray2 = time.strptime(dt2, format2)
    d1 = datetime.datetime(timeArray1.tm_year, timeArray1.tm_mon, timeArray1.tm_mday)
    d2 = datetime.datetime(timeArray2.tm_year, timeArray2.tm_mon, timeArray2.tm_mday)
    days = (d2 - d1).days
    return days


def dete_dalta(days, date=None, format="%Y-%m-%d", return_format="%Y-%m-%d"):
    '''
    dete_dalta(days, date=None, format="%Y-%m-%d", return_format="%Y-%m-%d") -> str
        功能：输入符合规定模式的日期，默认当前日期，计算前n天，后n天的日期
        参数：
            days：相隔的天数
            date：None 默认当前日期
        返回 ：
            wanted_date : 前n天，后n天的日期
        例子：
            dete_dalta(days, date=None, format="%Y-%m-%d", return_format="%Y-%m-%d") -> str
                days=1   date=2018-05-21  return 2018-05-22   后1天
                days=-1  date=2018-05-21  return 2018-05-20   前1天
    '''
    if date == None:
        wanted_date = (datetime.datetime.now() + datetime.timedelta(days)).strftime(return_format)
    else:
        date_input = datetime.date.fromtimestamp(time.mktime(time.strptime(date, format)))
        wanted_date = (date_input + datetime.timedelta(days)).strftime(return_format)
    return wanted_date






