# -*- coding: utf-8 -*-

from ubpa.ilog import ILog
import shutil
import glob
import os
import time
import fnmatch

__logger = ILog(__file__)

def create_file(file=None,path=None):
    '''
    创建文件
    :param file:文件名称
    :param path:文件路径
    :return:True
    '''
    __logger.echo_msg(u"ready to execute[create_file]")
    try:
        if  os.path.exists(path):
            file = open(path + os.sep + file, 'w')
            file.close()
            return True
        else:
            __logger.debug(u"path does not exist")
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[create_file]")



def create_dir(dir=None):
    '''
    创建路径
    :param dir:文件路径
    :return:True
    '''
    __logger.echo_msg(u"ready to execute[create_dir]")
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            return True
        else:
            __logger.debug(u"Path already exists")
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[create_dir]")

def copy_file(src_file=None,dst_file=None):
    '''
    复制文件
    :param src_file:文件路径
    :param dst_file:存放路径
    :return:True
    '''
    __logger.echo_msg(u"ready to execute[copy_file]")
    try:
        if os.path.exists(dst_file):
            shutil.copy(src_file, dst_file)
            return True
        else:
            __logger.debug(u"path does not exist")

    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[copy_file]")

def del_file(file=None):
    '''
    删除文件
    :param file:文件路径
    :return:True
    '''
    __logger.echo_msg(u"ready to execute[del_file]")
    try:
        if os.path.exists(file):
            os.remove(file)
        else:
            __logger.debug(u"path does not exist")
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[del_file]")

def move_file(src_file=None,dst_file=None):
    '''
    移动文件
    :param src_file:
    :param dst_file:
    :return:
    '''
    __logger.echo_msg(u"ready to execute[move_file]")
    try:
        if os.path.exists(dst_file):
            shutil.move(src_file,dst_file)
        else:
            __logger.debug(u"path does not exist")
    except Exception as e:
        raise e
    finally:
        __logger.echo_msg(u"end execute[move_file]")



def filter_exclude_file(files,exclude_file):
    '''
    过滤不需要的文件
    '''
    dst_files = []
    try:
        if exclude_file != None:
            for f in files:
                a = f.split("/")
                if not fnmatch.fnmatch(a[-1],exclude_file ):
                    dst_files.append(f)
            return dst_files
        else:
            return files
    except Exception as e:
        raise e

def get_all_path_files(path, include_file, sub_dir):
    '''
    满足条件的所有文件
    '''
    list_files=[]
    try:
        if sub_dir:
            path = os.path.join(path, '**')
            files = glob.glob(os.path.join(path, include_file), recursive=True)
            for i in files:
                i=i.replace('\\', '/')
                list_files.append(i)
        else:
            files = glob.glob(os.path.join(path, include_file), recursive=False)
            for i in files:
                i=i.replace('\\', '/')
                list_files.append(i)
        return list_files
    except Exception as e:
        raise e


def sort_by_time_reversed(files, reverse=True):
    '''
    时间排序
    '''
    return sorted(files, key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))),
                  reverse=reverse)


def find_files(path=None, include_file='*', exclude_file=None, sub_dir=False, time_sort='Desc', topn=50):
    '''
    通过指定文件名找到其所在路径
    参数:
        path: 需要检索的目录路径
        include_file: 需要检索的文件名
        exclude_file: 不需要检索的文件名
        sub_dir: 是否检索子文件夹
        time_sort: 按照时间排序
        topn: 前多少条
    return: 返回需要检索的文件路径列表
    '''
    __logger.echo_msg(u"ready to execute[find_files]")
    try:
        files = get_all_path_files(path, include_file, sub_dir)
        if time_sort == 'Desc':
            files = sort_by_time_reversed(files, reverse=True)
        else:
            files = sort_by_time_reversed(files, reverse=False)
        files = filter_exclude_file(files,exclude_file)
        files = files[0:topn]
        __logger.echo_msg(u"find_files result:" + str(files))
        return files
    except Exception as e:
        raise e






