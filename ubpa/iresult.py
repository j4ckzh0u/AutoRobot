#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019-01-17
# Description       : 使用百度ocr接口
#
################################################################################


from ubpa.ilog import ILog



class IResult(object):
    '''
    classdocs
    '''

    __logger = ILog(__file__)

    def __init__(self):
        '''
        Constructor
        '''

    '''
        返回状态
        0:成功
        1:失败
    '''
    status = 0

    err = None

    obj = None


    def echo_result(self):
        if self.status == 0:
            msg = "[success]"
        else:
            msg = "[fail]"
        msg = u'return result :'+msg + '[err='+str(self.err) +'][obj='+str(self.obj)+']'
        self.__logger.info(msg)

class MailMessage():

    received_time = None

    sender = None

    sender_mail = None

    to = None

    cc = None

    bcc = None

    subject = None

    body = None

    attachments = None




