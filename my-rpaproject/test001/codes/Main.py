# coding=utf-8
# 编译日期：2019-01-17 19:09:08
# 版权所有：www.i-search.com.cn
import time
from ubpa.ilog import ILog
from ubpa.base_img import *
import ubpa.iie as iie

class test001:
     
    def __init__(self):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
      
    def Main(self):
        #网站
        self.__logger.debug(' "StepNodeTag:171243492372",Note:')
        iie.open_url(url='www.baidu.com')
 
if __name__ == '__main__':
    pro = test001()
    pro.Main()
