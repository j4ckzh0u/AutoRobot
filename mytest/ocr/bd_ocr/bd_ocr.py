#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from aip import AipOcr

APP_ID = '15463469'
API_KEY = 'uLDx1Ust5kq1fom3q2wQXp9Y'
SECRET_KEY = 'r5XdOhjRWNO0elO7VKO5NGGdU1qr0W23'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



################################################################################
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def parse_once(filepath):


	try:
		image = get_file_content(filepath)

		# d_rv = client.basicGeneral(image)

		d_rv = client.accurate(image)

		# client.accurate(image, options)

		print("\n文件 {0} 共解析出 {1} 个字符".format(filepath, d_rv.get('words_result_num')))

		words = d_rv.get('words_result')
		# print("****************1",words)

		print("====================================================================")
		for v in words:
			print(v.get('words'))
		print("====================================================================")

		# print("****************2",d_rv)

	except Exception as e:
		print(d_rv)
		print("文件 {0} 解析出错".format(filepath))


################################################################################
def main_test():
	# rootdir = r'C:\src\lescpsn\AutoRobot\mytest\tax'
	# print("************")

	rootdir = os.path.dirname(os.path.realpath(__file__))
	png_dir = os.path.join(rootdir, 'tax')
	# print("====={0}".format(rootdir))


	list = os.listdir(png_dir)
	for i in range(0,len(list)):
		path = os.path.join(png_dir,list[i])
		# print("**************",path)
		if os.path.isfile(path):
			parse_once(path)
			pass




	# parse_once(r'C:\src\lescpsn\AutoRobot\mytest\tax\2.png')





################################################################################
if __name__ == '__main__':
	main_test()