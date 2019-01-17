#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : ???
# Generate Date     : 2019-01-17
# Description       :
#
################################################################################


class WinNotFoundError(Exception):
    def __init__(self, err="WinNotFoundError"):
        Exception.__init__(self,err)

class ImageNotFoundError(Exception):
    def __init__(self, err="ImageNotFoundError"):
        Exception.__init__(self,err)

class WaitTimeoutError(Exception):
    def __init__(self, err="WaitTimeoutError"):
        Exception.__init__(self,err)

class AppOpenError(Exception):
    def __init__(self, err="AppOpenError"):
        Exception.__init__(self,err)

class Au3ExecError(Exception):
    def __init__(self, err="AppOpenError"):
        Exception.__init__(self,err)

class ScalingScreenError(Exception):
    def __init__(self, err="Scaling screen not 100%"):
        Exception.__init__(self,err)

class ExcuteError(Exception):
    def __init__(self, err="ExcuteError"):
        Exception.__init__(self,err)