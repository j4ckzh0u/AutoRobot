# -*- coding:utf-8 -*-
'''
@author: Wu.Xin
统一日志记录

'''

import logging
import time
import os
from ctypes import *
from ubpa.iconstant import *
import sys
import configparser
import chardet

print("*************************************************")
curfilePath=os.path.abspath(__file__)
dll_path=os.path.join(curfilePath, r"..\..\bin\UEBAIEWatcher.dll")
print(dll_path)
print("*************************************************")



dll = cdll.LoadLibrary(dll_path)



class RpaServer():
    def __init__(self):
        try:
            self.LogLevel = 700
            self.LogServerSend = 'yes'
            self.LogServerLevel = 700
            self.AgentUUID = ''
            self.MainServer = ''
            self.WebServicePort = 9080
            python_path = sys.executable  # 当前使用的python.exe路径
            Upper_level_directory = os.path.dirname(python_path)  # python.exe上一级的路径
            Upper_secondary_directory = os.path.dirname(Upper_level_directory)  # python.exe上两级的路径
            Upper_level_three_directory = os.path.dirname(Upper_secondary_directory)  # python.exe上三级的路径
            config_path = Upper_level_three_directory + os.sep + 'config' + os.sep + 'UEBAOption.ini'
            cf = configparser.ConfigParser()
            f = open(config_path, 'rb')
            data = f.read()
            chardet_dict = chardet.detect(data)
            encoding_mode = chardet_dict['encoding']  # 获取文件的编码格式
            cf.read(config_path, encoding=encoding_mode)
            secs = cf.sections()
            if 'loglevel' in cf.options("Common"):
                self.LogLevel = cf.get('Common', 'LogLevel')
            if 'logserversend' in cf.options("Common"):
                self.LogServerSend = cf.get('Common', 'LogServerSend')
            if 'logserverlevel' in cf.options("Common"):
                self.LogServerLevel = cf.get('Common', 'LogServerLevel')
            if 'SERVER_INFO' in secs:
                if 'agentuuid' in cf.options("SERVER_INFO"):
                    self.AgentUUID = cf.get('SERVER_INFO', 'AgentUUID')
                if 'mainserver'in cf.options("SERVER_INFO"):
                    self.MainServer = cf.get('SERVER_INFO', 'MainServer')
                if 'webserviceport' in cf.options("SERVER_INFO"):
                    self.WebServicePort = cf.get('SERVER_INFO', 'WebServicePort')
        except Exception as e:
            print(e)



#rq = time.strftime('%Y%m%d', time.localtime(time.time()))

#log_path = u"../logs/" + rq + "/"


# setting = {
#            'logpath':log_path,
#            'filename':'py_' + rq + '.log'
#            }

# 发送日志 给动态库，写入统一的日志中
# def send_dll_log(level, msg):
#     dll.doSendRobotLog(level, msg)


class ILog(object):

    def __init__(self, fname):
        # path = setting['logpath']
        # if(not os.path.exists(path)):
        #     os.makedirs(path)
        # self.path = setting['logpath']
        # self.filename = setting['filename']
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
        self.name = os.path.basename(fname)
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        # self.fh = logging.FileHandler(self.path + self.filename,"a",encoding = "UTF-8") #a表示mode
        # self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(name)s-%(message)s')
        # self.fh.setFormatter(self.formatter)
        self.level_num = RpaServer().LogLevel
        # self.logger.addHandler(self.fh)

        if LOG_TO_CONSOLE:
            self.console = logging.StreamHandler(sys.stdout)
            self.console.setLevel(logging.DEBUG)
            self.formatter = logging.Formatter('%(name)s-%(message)s')
            self.console.setFormatter(self.formatter)
            self.logger.addHandler(self.console)

    # ERROR  = 300
    # WARN   = 400
    # INFO   = 600
    # DEBUG  = 700
    # NOTSET = 800
    def getLogger(self):
        return self.logger

    def info(self, msg):
        try:
            int_level_num = int(self.level_num)
            if int_level_num>= 600:
                self.logger.info(msg)
                #send_dll_log("info", msg)
                dll.doSendRobotLog("info", msg)
        except:
            self.logger.info("LogLevel parameter set wrong")


    def warning(self, msg):
        try:
            int_level_num = int(self.level_num)
            if int_level_num >= 400:
                self.logger.warning(msg)
                #send_dll_log("warn", msg)
                dll.doSendRobotLog("warn", msg)
        except:
            self.logger.warning("LogLevel parameter set wrong")

    def error(self, msg):
        try:
            int_level_num = int(self.level_num)
            if int_level_num >= 300:
                self.logger.error(msg)
                #send_dll_log("error", msg)
                dll.doSendRobotLog("error", msg)
        except:
            self.logger.error("LogLevel parameter set wrong")

    def debug(self, msg):
        try:
            int_level_num = int(self.level_num)
            if int_level_num >= 700:
                self.logger.debug(msg)
                #send_dll_log("debug", msg)
                dll.doSendRobotLog("debug", msg)
        except:
            self.logger.error("LogLevel parameter set wrong")
    # def close(self):
    #     self.logger.removeHandler(self.fh)

    def echo_msg(self, msg):
        try:
            int_level_num = int(self.level_num)
            if int_level_num >= 800:
                self.logger.info(msg + "[Echo]")
                #send_dll_log("info", msg + "[Echo]")
                dll.doSendRobotLog("info", msg+ "[Echo]")
        except:
            self.logger.error("LogLevel parameter set wrong")




# if __name__ == '__main__':
#
#     logger = ILog(__file__)
#     #logger.echo_msg(u"中国")
#     logger.info("ddd")



# log_local_path = u"d:/log.log"
#
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='[proc] %(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     filename=log_local_path,
#                     filemode='a')
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# # add the handler to the root logger
# logging.getLogger('').addHandler(console)
#
#
#
#
#
# logging.debug('Failed to open file')

