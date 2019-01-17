# -*- coding: utf-8 -*-
'''
RPA 对正则表达式的处理
'''
import re


def lens(param):
    '''
        len(param) -> int
            功能：返回对象（字符、列表、元组等）长度或项目个数。
            参数：
              param :待处理的对象
            返回:
                返回对象长度。
            例子:
            len('abd')          -> 3
            len([1,2,3,4])      -> 4
            len((1,2,3,4,5))    -> 5
        '''
    return len(param)





def match(pattern, string, flags=0):
    '''
        match(pattern, string, flags=0) -> 匹配的对象 or None

            功能：re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none

            参数:
            pattern : 匹配的正则表达式.
            string  : 要匹配的字符串.
            flags   : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等.
                      re.I	使匹配对大小写不敏感
                      re.L	做本地化识别（locale-aware）匹配
                      re.M	多行匹配，影响 ^ 和 $
                      re.S	使 . 匹配包括换行在内的所有字符
                      re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
                      re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
            返回:
                    返回一个匹配的对象，否则返回None.
            例子:
            re.match('www', 'www.runoob.com').span() -> (0, 3)     # 在起始位置匹配
            re.match('com', 'www.runoob.com') -> None         # 不在起始位置匹配

        '''
    return re.match(pattern, string, flags=flags)


def search(pattern, string, flags=0):
    '''
            search(pattern, string, flags=0) -> 匹配的对象 or None

                功能：search 扫描整个字符串并返回第一个成功的匹配

                参数:
                pattern : 匹配的正则表达式.
                string  : 要匹配的字符串.
                flags   : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等.
                          re.I	使匹配对大小写不敏感
                          re.L	做本地化识别（locale-aware）匹配
                          re.M	多行匹配，影响 ^ 和 $
                          re.S	使 . 匹配包括换行在内的所有字符
                          re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
                          re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
                返回:
                        返回一个匹配的对象，否则返回None.
                例子:
                re.match('www', 'www.runoob.com').span() -> (0, 3)     # 在起始位置匹配
                re.match('com', 'www.runoob.com') -> (11, 14)         # 不在起始位置匹配

            '''
    return re.search(pattern, string, flags=flags)


def sub(pattern, repl, string, count=0):
    '''
            sub(pattern, repl, string, count=0) -> str

                功能：sub 用于替换字符串中的匹配项

                参数:
                pattern : 正则中的模式字符串。
                repl : 替换的字符串，也可为一个函数。
                string : 要被查找替换的原始字符串。
                count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

                返回:
                        返回被替换后的字符串
                例子:
                phone = "2004-959-559 # 这是一个电话号码"
                num = sub(r'#.*$', "", phone)
                num ->  2004-959-559     # 删除注释

                num = re.sub(r'\D', "", phone)
                num ->  2004959559    # 移除非数字的内容

                repl 参数是一个函数
                def double(matched):
                    value = int(matched.group('value'))
                    return str(value * 2)

                s = 'A23G4HFD567'
                result = sub('(?P<value>\d+)', double, s)
                result ->  A46G8HFD1134     # 将匹配的数字乘于 2
               '''
    return re.sub(pattern, repl, string, count=count)


def dict_updata_value(dict,key,value):
    '''
            dict_updata_value(dict,key,value) -> dict
                function：Updates the value of the specified key.
                parameter：
                  dict :Dictionary objects to be processed
                  key :Keys to be updated
                  value：Values to be updated
                return:
                    Return the updated dictionary ,If this key is not in the dictionary, return False
                instance:
                dict_updata_value({'a': '123', 'b': 10000},'a','aaaaaaaa')        ->{'a': 'aaaaaaaa', 'b': 10000}
                dict_updata_value({'a': '123', 'b': 10000},'d','vvvvvvv')        ->  False

    '''
    if key in dict:
        dict[key]=value
        #return dict
    else:
        return False


def dict_move(dict,key):
    '''
            dict_move(dict,key) -> str or int
                function：Delete the value corresponding to the given key in the dictionary.
                parameter：
                  dict :Dictionary objects to be processed
                  key :Key values to be deleted
                return:
                    The return value is the deleted value.
                instance:
                dict_move({'a': '123', 'b': 10000},'a')  -> {'b': 10000}

    '''
    dict.pop(key)

    #return dict


def dict_get(dict,key):
    '''
            dict_get(dict,key) -> str or int
                function：Returns the value of the specified key.
                parameter：
                  dict :Dictionary objects to be processed
                  key: The key to look up in the dictionary。
                return:
                    Returns the value of the specified key.
                instance:
                dict_get('a': '123', 'b': 10000},'a')         -> ‘123’

    '''
    return dict.get(key)




def dict_get_vals(dict):
    '''
            dict_get_vals(dict) -> list
                function：Returns a list containing all the values of the dictionary.
                parameter：
                  dict :Dictionary objects to be processed
                return:
                    Returns a list containing all the values of the dictionary.
                instance:
                dict_get_vals({'Sex': 'female', 'Age': 7, 'Name': 'Zara'})    -> ['female', 7, 'Zara']

    '''
    return list(dict.values())


def dict_key_in(dict,key):
    '''
            dict_key_in(dict,k) -> Ture or False
                function：Determine whether the key exists in the dictionary.
                parameter：
                  dict :Dictionary objects to be processed
                  key: The key to look up in the dictionary.
                return:
                    If the key returns Ture in dictionary dict, otherwise it returns False.
                instance:
                dict_key_in({'Sex': 'female', 'Age': 7, 'Name': 'Zara'},'Name')    -> Ture
                dict_key_in({'Sex': 'female', 'Age': 7, 'Name': 'Zara'},'qqq')     -> False
    '''
    return  (key in dict)



def dict_get_keys(dict):
    '''
            dict_get_keys(dict)  -> list
                function：Returns a list of all keys.
                parameter：
                  dict :Dictionary objects to be processed
                return:
                    Returns a list of all keys.
                instance:
                dict_get_keys({'Sex': 'female', 'Age': 7, 'Name': 'Zara'})     -> ['Sex', 'Age', 'Name']

    '''
    return list(dict.keys())

def dict_get_key(dict,key):
    '''
            dict_get_key(dict,key) -> str or int
                function：Returns the value of the specified key.
                parameter：
                  dict :Dictionary objects to be processed
                  key: The key to look up in the dictionary.
                return:
                   Returns the value of the specified key.
                instance:
                dict_get_key('a': '123', 'b': 10000},'a')         -> ‘123’

    '''
    return dict[key]

def dict_updata(a,b):
    '''
            dict_updata(a,b) -> dict
                function：Add the key/value pair of dictionary b to a.
                parameter：
                  a :Dictionary to be added
                  b: Added dictionary
                return:
                    Returns the added dictionary
                instance:
                dict_updata({'a': '123', 'b': 10000}, {'Sex': 'female', 'Age': 7, 'Name': 'Zara'})  -> {'a': '123', 'b': 10000, 'Sex': 'female', 'Age': 7, 'Name': 'Zara'}

    '''
    a.update(b)
    #return a

def add(a,b):
    '''
            add(a,b) -> int
                function：Add two numbers
                parameter：
                  a :number a
                  b: number b
                return:
                    Returns the sum of two numbers
                instance:
                add(1,2)  -> 3

    '''

    return a+b

def reduce(a,b):
    '''
            reduce(a,b) -> int
                function：a minus b
                parameter：
                  a :number a
                  b: number b
                return:
                    Returns the difference between two numbers
                instance:
                reduce(3,2)  -> 1

    '''
    return a-b

def multiply(a,b):
    '''
            multiply(a,b) -> int
                function：a multiply b
                parameter：
                  a :number a
                  b: number b
                return:
                    Returns the product of two numbers
                instance:
                multiply(3,2)  -> 6

    '''
    return a*b


def division(a,b):
    '''
            division(a,b) -> int
                function：a divided by b
                parameter：
                  a :number a
                  b: number b
                return:
                    Returns the quotient of two numbers
                instance:
                division(4,2)  -> 2

    '''
    return a/b
