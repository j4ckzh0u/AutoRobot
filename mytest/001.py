from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# __browser_url = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'  ##google浏览器的地址
#__browser_url = r'C:\Users\zhanglu\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址
__browser_url = r'C:\Local\360Chrome\Chrome\Application\360chrome.exe'  ##360浏览器的地址

chrome_options = Options()
chrome_options.binary_location = __browser_url
driver = webdriver.Chrome(options=chrome_options)

# url=r"https://www.baidu.com"
url=r"https://etax.jsgs.gov.cn/sso/login"

print("开始访问 {arg_url}".format(arg_url = url))
driver.get("https://www.baidu.com")

print('==============')