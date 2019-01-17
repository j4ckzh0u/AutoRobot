#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019-01-17
# Description       :
#
################################################################################

from ctypes import *
from ctypes.wintypes import *
import subprocess
import time
from ubpa import iwin
from ubpa.iconstant import *
from ubpa.ierror import *
from ubpa.ilog import ILog
import ubpa.encrypt as encrypt


__logger = ILog(__file__)


print("*************************************************")
curfilePath=os.path.abspath(__file__)
dll_path=os.path.join(curfilePath, r"../../plugin/Com.Isearch.Func.AutoIt/AutoItX3.dll")
print(dll_path)
print("*************************************************")
dll = windll.LoadLibrary(dll_path)  # 调AutoItX3动态库


# dll = windll.LoadLibrary("../Com.Isearch.Func.AutoIt/AutoItX3.dll")

#dll = windll.LoadLibrary("AutoItX3.dll")

def run_app(path=None,work_path=None):
    __logger.debug('Open application:[' + str(path) + ']')
    try:
        proc = subprocess.Popen(path,cwd=work_path)
    except Exception as e:
        raise e


def run_shellexecute(path=None,work_path=""):
    __logger.debug('Open file: [' + str(path) + '] ')
    try:
        os.startfile(path)
    except Exception as e:
        raise e


def do_click_cs(win_title=None,win_text="",control=None,button='left',times=1,waitfor=WAIT_FOR):
    __logger.debug('Keyboard click Control:['+str(win_title)+']['+str(control)+']')
    try:
        starttime = time.time()
        while True:
            rst  = _do_click_cs(win_title,win_text, control,button, times) # 返回1,0，或者报错
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('Keyboard click error:['+str(win_title)+']['+str(control)+']')
                __logger.debug('Keyboard click Control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def control_set_text_cs(win_title=None,win_text="",control=None,text=None,waitfor=WAIT_FOR):
    __logger.debug('Set text control:[' + str(win_title)  + '][' + str(control) + ']')
    try:
        starttime = time.time()
        while True:
            text = encrypt.decrypt(str(text))
            rst = _control_set_text_cs(win_title, win_text, control, text) # 返回1,0，或者报错
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('Set text error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('Set text control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def win_wait_active_cs(win_title=None,waitfor=WAIT_FOR):
    __logger.debug('win_wait_active_cs:[' + str(win_title) + ']')
    try:
        rst = dll.AU3_WinWaitActive(win_title, "", waitfor) # 返回1,0，或者报错
        if rst == 0:
            __logger.debug('win_wait_active_cs error:[' + str(win_title) + ']')
            raise Au3ExecError('win_wait_active_cs error:[' + str(win_title) + ']')
    except Exception as e:
        raise e


def control_get_text_cs(win_title=None,win_text="",control=None,waitfor=WAIT_FOR):
    __logger.debug('get text control:[' + str(win_title) + ']['  + str(win_text)  +  '][' + str(control) + ']')
    try:
        starttime = time.time()
        while True:
            rst = _control_get_text_cs(win_title, win_text, control) #返回 文本字符串
            if rst != "":
                __logger.debug('get text result:' + rst)
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    break
                __logger.debug('get text control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e




def mouse_click_cs(win_title=None,x=None,y=None,waitfor=WAIT_FOR):
    __logger.debug('mouse_click_cs:[' + str(x) + '][' + str(y) + ']')
    try:
        ''''如果指定窗口'''
        if (win_title != None):
            '''如果窗口不活跃状态'''
            if not iwin.do_win_is_active(win_title):
                iwin.do_win_activate(win_title=win_title, waitfor=waitfor)
        starttime = time.time()
        while True:
            rst = _mouse_click_cs("left", x, y, 2, 1)  # 返回1,0，或者报错
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('mouse click error:[' + str(x) + '][' + str(y) + ']')
                __logger.debug('mouse click cs error:[' + str(x) + '][' + str(y) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e

def mouse_click(win_title=None,x=None,y=None,mouse_button='left',times=1,waitfor=WAIT_FOR):
    '''
    鼠标点击屏幕位置
    '''
    __logger.debug('mouse_click:[' + str(x) + '][' + str(y) + ']')
    try:
        ''''如果指定窗口'''
        if (win_title != None):
            '''如果窗口不活跃状态'''
            if not iwin.do_win_is_active(win_title):
                iwin.do_win_activate(win_title=win_title, waitfor=waitfor)
        starttime = time.time()
        while True:
            rst = _mouse_click_cs(mouse_button, int(x), int(y), 1, times)
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('mouse click Err:[' + str(x) + '][' + str(y) + ']')
                __logger.debug('mouse click Err:[' + str(x) + '][' + str(y) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def mouse_moveto(win_title=None,x=None,y=None,waitfor=WAIT_FOR):
    '''
    鼠标点击屏幕位置
    '''
    __logger.debug('mouse_moveto:[' + str(x) + '][' + str(y) + ']')
    try:
        ''''如果指定窗口'''
        if (win_title != None):
            '''如果窗口不活跃状态'''
            if not iwin.do_win_is_active(win_title):
                iwin.do_win_activate(win_title=win_title, waitfor=waitfor)
        starttime = time.time()
        while True:
            rst = _mouse_move_cs(x, y, 1)
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('mouse_moveto:[' + str(x) + '][' + str(y) + ']')
                __logger.debug('mouse_moveto:[' + str(x) + '][' + str(y) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def control_send_cs(win_title=None,win_text="",control=None,text=None,waitfor=WAIT_FOR):
    __logger.debug('Send control:[' + str(win_title) + '][' + str(control) + ']')
    try:
        starttime = time.time()
        while True:
            text = encrypt.decrypt(str(text))
            rst = _control_send_cs(win_title,win_text,control,text) # 返回1,0，或者报错
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('Send control error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('Send control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def do_cs_select(win_title=None,win_text="",control=None,select_string=None,waitfor=WAIT_FOR):
    __logger.debug('Drop-down box selection control:[' + str(win_title) + '][' + str(control) + ']')
    try:
        starttime = time.time()
        while True:
            rst = _do_cs_select(win_title,win_text,control,select_string) # 返回1, 或者报错
            if rst == 1:
                __logger.debug('Drop-down box selection control modification:[' + str(win_title) + '][' + str(control) + ']')
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('Drop-down box selection error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('Dropdown box selection control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def _do_click_cs(win_title=None,win_text=None,control=None,button='left',click_times=1):
    try:
        DEFAULT = -2147483647
        return dll.AU3_ControlClick(win_title, win_text, control, button, click_times, DEFAULT, DEFAULT)
    except Exception as e:
        raise e

def _control_set_text_cs(win_title=None,win_text="",control=None,text=None):
    try:
        return dll.AU3_ControlSetText(win_title, win_text, control, text)
    except Exception as e:
        raise e

def _control_get_text_cs(win_title=None,win_text="",control=None):
    try:
        buf_size = 256
        ctrl_text = ctypes.create_unicode_buffer(buf_size)
        dll.AU3_ControlGetText(win_title, win_text, control, ctrl_text, buf_size)
        return ctrl_text.value.rstrip()
    except Exception as e:
        raise e


def get_scale():
    '''获取缩放比例'''
    dll = cdll.LoadLibrary("../../bin/ScreenScaling.dll")
    return dll.GetScreenScaling()



def _mouse_click_cs(button=None,x=None,y=None,mode=None,times=None):
    try:
        dll.AU3_Opt("MouseCoordMode", mode) #0:窗口 1:屏幕  2:可见区域

        return dll.AU3_MouseClick(button, int(x), int(y), times, 10)
    except Exception as e:
        raise e


def _mouse_move_cs(x=None, y=None, mode=None):
    try:
        dll.AU3_Opt("MouseCoordMode", mode)  # 0:窗口 1:屏幕  2:可见区域

        return dll.AU3_MouseMove(int(x), int(y), 10)
    except Exception as e:
        raise e

def _control_send_cs(win_title=None,win_text="",control=None,text=None):
    try:
        return dll.AU3_ControlSend(win_title, win_text, control, text, 0)
    except Exception as e:
        raise e

def _do_cs_select(win_title=None,win_text="",control=None,select_string=None):
    try:
        dll.AU3_ControlCommand(win_title, win_text, control, "SelectString", select_string, "", 256)
        errcode = dll.AU3_error()

        if errcode == 0:
            return 1
        else:
            return 0
    except Exception as e:
        raise e

def do_click_pos(win_title=None,win_text=None,control=None,button='left',curson='center',offsetX=0,offsetY=0,times=1,
                 run_mode = 'unctrl',waitfor=WAIT_FOR):

    try:
        if run_mode == 'ctrl':
            return  do_click_cs(win_title=win_title,win_text=win_text,control=control,button=button,times=times,waitfor=waitfor)

        __logger.debug('click control:[' + str(win_title) + '][' + str(control) + ']')
        if win_title != None and win_title.strip() != '':
            ''''如果窗口不活跃状态'''
            if not iwin.do_win_is_active(win_title):
                iwin.do_win_activate(win_title=win_title, waitfor=waitfor)

        starttime = time.time()
        while True:
            X,Y = do_get_pos(win_title, control, curson, offsetX, offsetY)
            rst = _mouse_click_cs(button,X, Y, 2, times)
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('click control error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('click control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e

def do_moveto_pos(win_title=None,win_text=None,control=None,curson='center',offsetX=0,offsetY=0,waitfor=WAIT_FOR):
    __logger.debug('Move mouse to control:[' + str(win_title) + '][' + str(control) + ']')
    try:
        if win_title != None and win_title.strip() != '':
            ''''如果窗口不活跃状态'''
            if not iwin.do_win_is_active(win_title):
                iwin.do_win_activate(win_title=win_title, waitfor=waitfor)

        starttime = time.time()
        while True:
            X,Y = do_get_pos(win_title, control, curson, offsetX, offsetY)
            rst = _mouse_move_cs(X, Y, 2)
            if rst == 1:
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('Move mouse error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('Move mouse  error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e


def do_get_pos(win_title=None,control=None,curson=None,offsetX=0,offsetY=0):
    X = None
    Y = None

    try:
        rect = RECT()
        dll.AU3_ControlGetPos(win_title, "", control, ctypes.byref(rect))  # rect.left, rect.top, rect.right, rect.bottom
        curs = str(curson).lower()

        if curs == "center":
            X = rect.left + (rect.right-rect.left)/2 + offsetX
            Y = rect.top + (rect.bottom-rect.top)/2 + offsetY
        if curs == "lefttop":
            X = rect.left + offsetX
            Y = rect.top + offsetY
        if curs == "righttop":
            X = rect.right + offsetX
            Y = rect.top + offsetY
        if curs == "leftbottom":
            X = rect.left + offsetX
            Y = rect.bottom + offsetY
        if curs == "rightbottom":
            X = rect.right + offsetX
            Y = rect.bottom + offsetY

        return X,Y
    except Exception as e:
        raise e

def do_cs_check(win_title=None,win_text="",control=None,action=None,waitfor=WAIT_FOR):
    __logger.debug('checkbox control:[' + str(win_title) + '][' + str(control) + ']')
    try:
        starttime = time.time()
        while True:
            rst = _do_cs_check(win_title,win_text,control,action) # 返回1, 或者报错
            if rst == 1:
                __logger.debug('checkbox Control modify:[' + str(win_title) + '][' + str(control) + ']')
                return rst
            else:
                runtime = time.time() - starttime
                if runtime >= waitfor:
                    __logger.debug('Operation timeout')
                    raise Au3ExecError('checkbox error:[' + str(win_title) + '][' + str(control) + ']')
                __logger.debug('checkbox control error:[' + str(win_title) + '][' + str(control) + ']')
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        raise e

def _do_cs_check(win_title=None,win_text="",control=None,action=None):
    try:
        dll.AU3_ControlCommand(win_title, win_text, control, action, "", "", 256)
        errcode = dll.AU3_error()

        if errcode == 0:
            return 1
        else:
            return 0
    except Exception as e:
        raise e

def PostMessage(handle, msg, wparam, lparam):
    """Call API SendMessageW from user32.dll"""
    return ctypes.windll.user32.PostMessageW(handle, msg, wparam, lparam)

def GetWindowLong(handle, nIndex):
    """Call API GetWindowLong from user32.dll"""
    return ctypes.windll.user32.GetWindowLongW(handle, nIndex)

def GetParent(handle):
    return ctypes.windll.user32.GetParent(handle)


def do_click_element(win_title=None,win_text=None,control=None,waitfor=WAIT_FOR):
    __logger.debug('do_click_element:[' + str(win_title) + '][' + str(control) + ']')
    try:
        win = dll.AU3_WinGetHandle(win_title, win_text)
        control_wnd = dll.AU3_ControlGetHandle(win, control)
        controlid=GetWindowLong(control_wnd, -12)
        parent_wnd=GetParent(control_wnd)
        PostMessage(parent_wnd, 0x0111, controlid, control_wnd)
    except Exception as e:
        raise e


