# -*- coding: utf-8 -*-
import re
from ubpa import iwin
from ubpa.ilog import ILog

import xlrd
import numpy as np
import pandas as pd
import xlwings as xw


__logger = ILog(__file__)

'''
读取单元格的值
path   excel路径
sheet  sheet名称
cell   单元格名称
'''
def read_cell(path=None,sheet=0,cell="A1"):
    __logger.echo_msg(u"ready to execute[readCell]")
    try:
        wb = xlrd.open_workbook(path)
        if type(sheet)==str:
            sht = wb.sheet_by_name(sheet)
        elif type(sheet)==int:
            sht = wb.sheet_by_index(sheet)
        position = get_split_col_row(cell)
        pos_col = position[0]
        pos_row = position[1]
        pos_col_index = get_excel_row_index(pos_col)
        co =  sht.col_values(pos_col_index,start_rowx=int(pos_row)-1,end_rowx=int(pos_row))
        if len(co) == 0:
            co = [""]

        __logger.debug('read_cell result:[' + str(co[0]) + ']')
        return co[0]
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[readCell]")




'''
写入单元格
path   excel路径
sheet  sheet名称
cell   单元格名称
text   写入excel的值
'''
def write_cell(path=None,sheet=0,cell="A1",text=None):
    __logger.echo_msg(u"ready to execute[writeCell]")

    try:
        wb = xw.Book(path)
        sht = wb.sheets[sheet]
        sht.range(cell).options(index=False).value = text
        wb.save() 
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[writeCell]")

'''
读取行
path   excel路径
sheet  sheet名称
row    行数
'''
def read_row(path=None,sheet=0,cell="A1"):
    __logger.echo_msg(u"ready to execute[read_row]")
    try:
        wb = xlrd.open_workbook(path)
        if type(sheet)==str:
            sht = wb.sheet_by_name(sheet)
        elif type(sheet)==int:
            sht = wb.sheet_by_index(sheet)
        position = get_split_col_row(cell)
        pos_col = position[0]
        pos_row = position[1]
        pos_col_index = get_excel_row_index(pos_col)
        co = sht.row_values(int(pos_row)-1, start_colx=pos_col_index)

        __logger.debug('read_row result:[' + str(co) + ']')
        return co
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[read_row]")


'''
读取列
path   excel路径
sheet  sheet名称
column  列数
header  dataFrame头
'''
def read_col(path=None,sheet=0,cell="A1"):
    __logger.echo_msg(u"ready to execute[read_col]")
    col_list = []
    try:
        wb = xlrd.open_workbook(path)
        if type(sheet)==str:
            sht = wb.sheet_by_name(sheet)
        elif type(sheet)==int:
            sht = wb.sheet_by_index(sheet)
        position = get_split_col_row(cell)
        pos_col = position[0]
        pos_row = position[1]
        pos_col_index = get_excel_row_index(pos_col)
        co = sht.col_values(pos_col_index, start_rowx=int(pos_row) - 1)

        for index in range(len(co)):
            col_list.append(co[index])

        __logger.debug('read_col result:[' + str(col_list) + ']')
        return col_list

    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[read_col]")



'''
拆分行列    输入  A12   返回   ['A','12']
'''
def get_split_col_row(string):

    string = string.upper()
    return re.findall(r'[0-9]+|[A-Z]+',string)

'''
根据excel的行号如  'AB' 则返回  26   'B' 返回1
'''
def get_excel_row_index(string):

    s=0 
    for c in string:
        c = c.upper()
        s = s*26 + ord(c) - ord('A') + 1
    return s -1


'''
插入行
path   excel路径
sheet  sheet名称
cell   单元格的值
data   插入行的值
'''
def ins_row(path=None,sheet=0,cell="A1",data=None):
    __logger.echo_msg(u"ready to execute[ins_row]")
    try:
        wb = xw.Book(path)
        sht = wb.sheets[sheet]
        sht.range(cell).api.EntireRow.Insert()
        sht.range(cell).options(index=False).value = data
        wb.save()
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[ins_row]")

'''
插入列
path   excel路径
sheet  sheet名称
cell   单元格的值
data   插入列的值
'''
def ins_col(path=None,sheet=0,cell="A1",data=None):
    __logger.echo_msg(u"ready to execute[ins_col]")
    try:
        data_list=[]
        wb = xw.Book(path)
        sht = wb.sheets[sheet]
        sht.range(cell).api.EntireColumn.Insert()
        for i in data:
            data_list.append([i])
        sht.range(cell).options(index=False).value = data_list
        wb.save()
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[ins_col]")

'''
关闭excel应用

'''
def close_excel_apps():
    iwin.do_process_close('Excel.exe')



