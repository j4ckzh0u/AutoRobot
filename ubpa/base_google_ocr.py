#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author            : 乔帮主
# Generate Date     : 2019-01-17
# Description       : 使用 google 的  Tesseract
#
################################################################################



from PIL import Image
import pytesseract

#设置tesseract的路径
#pytesseract.pytesseract= ""

image = Image.open('C:/Users/ibm/Desktop/test.png')
code = pytesseract.image_to_string(image)