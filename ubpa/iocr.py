#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019-01-17
# Description       : 使用百度ocr接口
#
################################################################################

from aip import AipOcr
from ctypes import c_char_p, windll
import json
from ubpa import encrypt
from ubpa.ilog import ILog
from ubpa.iip.ocr import IipOcr
from PIL import Image
import pytesseract
import requests


__logger = ILog(__file__)



#通用文字识别
def general_recognize(image_path=""):
    __logger.info(u"Ready to execute [general_recognize]")
    text=""
    try:
        client = get_client()
        image = get_file_content(image_path)
        data = client.basicGeneral(image)
        __list=data['words_result']
        list_str = []
        for index in range(len(__list)):
            dict_str=__list[index]
            list_str.append(dict_str['words'])
        text = ''.join(list_str)
        return text
    except Exception as e:
        __logger.error('First recognition error:'+str(e))
        bd_general_recognize(image_path)

    finally:
        __logger.debug('[general_recognize] result :[' + text + ']')
        __logger.echo_msg(u"end execute [general_recognize]")


#身份证识别
def idcard_recognize(image_path="",idCardSide=""):
    __logger.info(u"Ready to execute[idcard_recognize]")
    dict_str = {}
    options={}
    options['id_card_side']=idCardSide
    try:
        client = get_client()
        image = get_file_content(image_path)
        data= client.idcard(image,options)
        if idCardSide == "front":
            if ('姓名' in data['words_result'].keys())==True:
                dict_str['name']=str(data['words_result']['姓名']['words'])
            else:
                dict_str['name']= ''
            if ('民族' in data['words_result'].keys())==True:
                dict_str['nationality']= str(data['words_result']['民族']['words'])
            else:
                dict_str['nationality']= ''
            if ('住址' in data['words_result'].keys())==True:
                dict_str['address']=str(data['words_result']['住址']['words'])
            else:
                dict_str['address']= ''
            if ('公民身份号码' in data['words_result'].keys())==True:
                dict_str['idno']=str(data['words_result']['公民身份号码']['words'])
            else:
                dict_str['idno']= ''
            if ('出生' in data['words_result'].keys())==True:
                dict_str['birthdate']=str(data['words_result']['出生']['words'])
            else:
                dict_str['birthdate']= ''
            if ('性别' in data['words_result'].keys())==True:
                dict_str['gender']= str(data['words_result']['性别']['words'])
            else:
                dict_str['gender']= ''

        else:
            if ('签发日期' in data['words_result'].keys())==True:
                dict_str['date_b']= str(data['words_result']['签发日期']['words'])
            else:
                dict_str['date_b']= ''
            if ('失效日期' in data['words_result'].keys())==True:
                dict_str['date_e']= str(data['words_result']['失效日期']['words'])
            else:
                dict_str['date_e']= ''
            if ('签发机关' in data['words_result'].keys())==True:
                dict_str['organization']= str(data['words_result']['签发机关']['words'])
            else:
                dict_str['organization']= ''
        return dict_str
    except Exception as e:
        __logger.error('First recognition error:' + str(e))
        bd_idcard_recognize(image_path, idCardSide)
    finally:
        __logger.debug('[idcard_recognize] result :[' + str(dict_str) + ']')
        __logger.echo_msg(u"end execute [idcard_recognize]")


#营业执照识别
def business_license_recognize(image_path=""):
    __logger.info(u"Ready to execute[business_license_recognize]")
    dict_str = {}
    try:
        client = get_client()
        image = get_file_content(image_path)
        data= client.businessLicense(image)
        if ('社会信用代码' in data['words_result'].keys())==True:
            dict_str['socialCreditCode']=str(data['words_result']['社会信用代码']['words'])
        else:
            dict_str['socialCreditCode']= ''
        if ('组成形式' in data['words_result'].keys())==True:
            dict_str['组成形式']= str(data['words_result']['组成形式']['words'])
        else:
            dict_str['组成形式'] = ''
        if ('法人' in data['words_result'].keys()) == True:
            dict_str['legal entity'] = str(data['words_result']['法人']['words'])
        else:
            dict_str['legal entity'] = ''
        if ('成立日期' in data['words_result'].keys()) == True:
            dict_str['date_b'] = str(data['words_result']['成立日期']['words'])
        else:
            dict_str['date_b'] = ''
        if ('注册资本' in data['words_result'].keys()) == True:
            dict_str['registered capital'] = str(data['words_result']['注册资本']['words'])
        else:
            dict_str['registered capital'] = ''
        if ('证件编号' in data['words_result'].keys()) == True:
            dict_str['ID number'] = str(data['words_result']['证件编号']['words'])
        else:
            dict_str['ID number'] = ''
        if ('地址' in data['words_result'].keys()) == True:
            dict_str['address'] = str(data['words_result']['地址']['words'])
        else:
            dict_str['address'] = ''
        if ('单位名称' in data['words_result'].keys()) == True:
            dict_str['organization'] = str(data['words_result']['单位名称']['words'])
        else:
            dict_str['organization'] = ''
        if ('类型' in data['words_result'].keys()) == True:
            dict_str['type'] = str(data['words_result']['类型']['words'])
        else:
            dict_str['type'] = ''
        if ('有效期' in data['words_result'].keys()) == True:
            dict_str['valid'] = str(data['words_result']['有效期']['words'])
        else:
            dict_str['valid'] = ''

        return dict_str
    except Exception as e:
        __logger.error('First recognition error:' + str(e))
        bd_business_license_recognize(image_path)
    finally:
        __logger.debug('[business_license_recognize] result :[' + str(dict_str) + ']')
        __logger.echo_msg(u"end execute[business_license_recognize]")


#验证码识别
def vcode_recognize(image_path="",code_type="8000"):
    __logger.info(u"Ready to execute[vCode_recognize]")
    options={}
    options["code_type"]=code_type
    try:
        client = get_client()
        image = get_file_content(image_path)
        data = client.vcode(image,options)
        result =data["result"]
        return result

    except Exception as e:
        raise e
    finally:
        __logger.debug('[vcode_recognize] result :[' + result + ']')
        __logger.echo_msg(u"end execute[vcode_recognize]")



def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_client():
    API_Key = "dinga59d519024c5b9bd"
    Secret_Key = "MTV1heO94n-PPTf5Bcm99YzvW_nwGTUwFpWM30RWK5dp9hzLHSBCDg_nY9tMK7ts"
    return IipOcr(API_Key, Secret_Key)


APP_ID = "MDQ2NSojIyoxMTI3"
API_KEY = "zeTVnSUQweWw3T0YqIwIyp2U2dDTld6NlNJTmx"
SECRET_KEY = "RUdVMWg4d1pPc011Z3FxUyojIypqZ2F2SFVtZkxPSDI0dk5D"


def bd_general_recognize(image_path=""):
    '''
        general_recognize(image_path="") -> str

        功能:
           通用识别
        参数:
          image_path: 需要识别的图片路径.
        返回:
              识别得到的字符串text.
        例子:
        general_recognize(image_path=r"c:\cc.png") -> "这是一串字符串"
    '''
    __logger.info(u"Ready to execute[bd_general_recognize]")
    text=""
    try:
        client = bd_get_client()
        image = bd_get_file_content(image_path)
        data = client.basicGeneral(image)
        data_dict = json.loads(json.dumps(data))
        __list=data_dict['words_result']
        list_str = []
        for index in range(len(__list)):
            dict_str=__list[index]
            list_str.append(dict_str['words'])

        text = '\n'.join(list_str)
        return text
    except Exception as e:
        raise e
    finally:
        __logger.debug('[bd_general_recognize] result :[' + text + ']')
        __logger.echo_msg(u"end execute [bd_general_recognize]")



def bd_idcard_recognize(image_path="",idCardSide=""):

    '''
        idcard_recognize(image_path="",idCardSide="") -> dict{}

        功能:
           身份证识别
        参数:
            image_path: 需要识别的图片路径.
            idCardSide: 图片正反面，正面front;反面back
        返回:
              识别得到的字典dict.
        例子:
        idcard_recognize(image_path="c:\cc.png",idCardSide="front") -> {'address': '盛顿市中心区宾夕法尼亚大街1600号Whitehouse', 'id': '1234567890', 'birth': '19610804', 'name': '贝拉克·奥巴马', 'sex': '男', 'nation': '汉'}
    '''
    __logger.info(u"Ready to execute[bd_idcard_recognize]")
    dict_str = {}
    try:
        client = bd_get_client()
        image = bd_get_file_content(image_path)
        data= client.idcard(image,idCardSide)
        data_dict = json.loads(json.dumps(data))
        if idCardSide=="front":
            if ('住址' in data_dict['words_result'].keys())==True:
                dict_str['address']=str(data_dict['words_result']['住址']['words'])
            else:
                dict_str['address']= ''
            if ('公民身份号码' in data_dict['words_result'].keys())==True:
                dict_str['id']= str(data_dict['words_result']['公民身份号码']['words'])
            else:
                dict_str['id']= ''
            if ('出生' in data_dict['words_result'].keys())==True:
                dict_str['birth']=str(data_dict['words_result']['出生']['words'])
            else:
                dict_str['birth']= ''
            if ('姓名' in data_dict['words_result'].keys())==True:
                dict_str['name']=str(data_dict['words_result']['姓名']['words'])
            else:
                dict_str['name']= ''
            if ('性别' in data_dict['words_result'].keys())==True:
                dict_str['sex']=str(data_dict['words_result']['性别']['words'])
            else:
                dict_str['sex']= ''
            if ('民族' in data_dict['words_result'].keys())==True:
                dict_str['nation']= str(data_dict['words_result']['民族']['words'])
            else:
                dict_str['nation']= ''

        else:

            if ('签发日期' in data_dict['words_result'].keys())==True:
                dict_str['date_b']= str(data_dict['words_result']['签发日期']['words'])
            else:
                dict_str['date_b']= ''
            if ('失效日期' in data_dict['words_result'].keys())==True:
                dict_str['date_e']= str(data_dict['words_result']['失效日期']['words'])
            else:
                dict_str['date_e']= ''
            if ('签发机关' in data_dict['words_result'].keys())==True:
                dict_str['organization']= str(data_dict['words_result']['签发机关']['words'])
            else:
                dict_str['organization']= ''
        return dict_str
    except Exception as e:
        raise e
    finally:
        __logger.debug('[bd_idcard_recognize] result : [' + str(dict_str) + ']')
        __logger.echo_msg(u"end execute [bd_idcard_recognize]")


def bd_business_license_recognize(image_path=""):

    '''
        business_license_recognize(image_path="") -> dict
        功能:
           营业执照识别
        参数:
          image_path: 需要识别的图片路径.
        返回:
            识别得到的字典dict.
        例子:
        business_license_recognize(image_path=r"c:\cc.png") -> {'organization': '深圳市特盛科技有限公司', 'legalperson': '董有彩', 'address': '北京市', 'limited': '无', 'id': '440301105957424', 'socialCreditCode': '无'}
    '''
    __logger.info(u"Ready to execute[bd_business_license_recognize]")
    dict_str = {}
    try:
        client = bd_get_client()
        image = bd_get_file_content(image_path)
        data= client.businessLicense(image)
        data_dict = json.loads(json.dumps(data))
        if ('单位名称' in data_dict['words_result'].keys()) == True:
            dict_str['organization'] = str(data_dict['words_result']['单位名称']['words'])
        else:
            dict_str['organization'] = ''
        if ('法人' in data_dict['words_result'].keys()) == True:
            dict_str['legalperson'] = str(data_dict['words_result']['法人']['words'])
        else:
            dict_str['legalperson'] = ''
        if ('地址' in data_dict['words_result'].keys()) == True:
            dict_str['address'] = str(data_dict['words_result']['地址']['words'])
        else:
            dict_str['address'] = ''
        if ('有效期' in data_dict['words_result'].keys()) == True:
            dict_str['limited'] = str(data_dict['words_result']['有效期']['words'])
        else:
            dict_str['limited'] = ''
        if ('证件编号' in data_dict['words_result'].keys()) == True:
            dict_str['id'] = str(data_dict['words_result']['证件编号']['words'])
        else:
            dict_str['id'] = ''
        if ('社会信用代码' in data_dict['words_result'].keys()) == True:
            dict_str['socialCreditCode'] = str(data_dict['words_result']['社会信用代码']['words'])
        else:
            dict_str['socialCreditCode'] = ''

        return dict_str
    except Exception as e:
        raise e
    finally:
        __logger.debug('[bd_business_license_recognize] result :[' + str(dict_str) + ']')
        __logger.echo_msg(u"end execute [bd_business_license_recognize]")

def bd_qr_code_recognize(image_path=""):

    '''
        qr_Code_recognize(image_path="") -> text
        功能:
           二维码识别
        参数:
          image_path: 需要识别的图片路径.
        返回:
            识别得到的字符串.
        例子:
        qr_Code_recognize(image_path=r"c:\cc.png") -> "这是一串字符串"
    '''
    __logger.info(u"Ready to execute[bd_qr_code_recognize]")
    text = ""
    list_str=[]
    try:
        client = bd_get_client()
        image = bd_get_file_content(image_path)
        data = client.qr_Code(image)
        data_dict = json.loads(json.dumps(data))
        __list = data_dict['codes_result']
        for index in range(len(__list)):
            dict_str = __list[index]
            if dict_str['type'] == 'QR_CODE':
                list_str = dict_str['text']

        text = '\n'.join(list_str)
        return text
    except Exception as e:
        raise e
    finally:
        __logger.debug('[bd_qr_code_recognize] result:[' + text + ']')
        __logger.echo_msg(u"end execute [bd_qr_code_recognize]")


def bd_get_client():
    return AipOcr(encrypt.decrypt(APP_ID), encrypt.decrypt(API_KEY), encrypt.decrypt(SECRET_KEY))

def bd_get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()






def _request(self, url, data, headers=None):
        """
            self._request('', {})
        """
        try:
            result = self._validate(url, data)
            if result != True:
                return result

            authObj = self._auth()
            params = self._getParams(authObj)

            data = self._proccessRequest(url, params, data, headers)
            headers = self._getAuthHeaders('POST', url, params, headers)
            response = self.__client.post(url, data=data, params=params,
                            headers=headers, verify=False, timeout=(
                                self.__connectTimeout,
                                self.__socketTimeout,
                            ), proxies=self._proxies
                        )
            obj = self._proccessResult(response.content)

            if not self._isCloudUser and obj.get('error_code', '') == 110:
                authObj = self._auth(True)
                params = self._getParams(authObj)
                response = self.__client.post(url, data=data, params=params,
                                headers=headers, verify=False, timeout=(
                                    self.__connectTimeout,
                                    self.__socketTimeout,
                                ), proxies=self._proxies
                            )
                obj = self._proccessResult(response.content)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            return {
                'error_code': 'SDK108',
                'error_msg': 'connection or read data timeout',
            }

        return obj

def get_tesseract_ocr(img_path,lang=None):
    txt = None
    try:
        image = Image.open(img_path)
        txt = pytesseract.image_to_string(image,lang=lang)
        if txt != None:
            txt = txt.replace(' ','')
        #print(txt)

    except Exception as e:
        raise e
    finally:
        return txt

def get_ydm_code(filename, codetype=5001, timeout=30):
    '''
    '''
#     YDMApi = windll.LoadLibrary(r'd:\svn\isa\branches\ueba_5.0\makesetup\CdaSetupDate\bin\yundamaAPI.dll')
    YDMApi = windll.LoadLibrary("../../bin/yundamaAPI.dll")
    result = c_char_p(b"                              ")
    username = b"isearch"
    password = "hcmNoKiMIyppc2V="
    password = encrypt.decrypt(password)
    password = bytes(password,encoding='utf-8')
    appId = 5364
    appKey = b"54b9ebb03b894bad4f52e4f3553edffb"
#     filename = b"C:\Users\ibm\Desktop\dynamicPassword.jpg"
    filename = filename.encode(encoding="utf-8")
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)

    __logger.debug("recognize:ID:%d，result:%s" % (captchaId, result.value))
    return str(result.value, encoding="utf-8")


# print(encrypt.decrypt(APP_ID))
# print(encrypt.decrypt(API_KEY))
# print(encrypt.decrypt(SECRET_KEY))
# abc = get_ydm_code("C:/Users/ibm/Desktop/1.PNG")
# print(abc)
# print(abc,'dddd',code)
# get_ydm_code(b"C:/Users/ibm/Desktop/33.png")
# APP_ID = "115"   API_KEY = "vSgCNWz6SINlsy5gID0yl7OF"   SECRET_KEY = "jgavHUmfLOH24vNCEGU1h8wZOsMugqqS"

