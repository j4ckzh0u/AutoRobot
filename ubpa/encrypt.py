#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019-01-17
# Description       :
#
################################################################################

from ctypes import cdll, string_at
import os

print("*************************************************")
curfilePath=os.path.abspath(__file__)
dll_path=os.path.join(curfilePath, r"../../bin/EncryptUtil.dll")
print(dll_path)
print("*************************************************")

dll = cdll.LoadLibrary(dll_path)
# dll = cdll.LoadLibrary("../../bin/EncryptUtil.dll")

def encrypt(str):
    '''
    加密算法
    '''
    text = ''
    try:
        text = string_at(dll.Encrypt(str), -1).decode('utf-8')
    except Exception as e:
        raise e
    finally:
        return text


def decrypt(str):
    '''
    解密算法
    '''
    text = ''
    try:

        text = string_at(dll.Decrypt(str), -1).decode('utf-8')
    except Exception as e:
        raise e
    finally:
        return text







