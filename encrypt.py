import hashlib
from selenium import webdriver
#encode() : Converts the string into bytes to be acceptable by hash function.
#digest() : Returns the encoded data in byte format.
#hexdigest() : Returns the encoded data in hexadecimal format.
driver=webdriver.Firefox()
driver.get('http://docker.hackthebox.eu:32671/')
element = driver.find_element_by_xpath("/html/body/h3")

string= element.text
en=string.encode()
print('----')
print(en)
h=hashlib.md5(en)
print('----')
print(h)
print('----')
print("The hexadecimal equivalent of hash is : ",h.hexdigest())
entrada = driver.find_element_by_xpath("/html/body/center/form/input[1]")
entrada.send_keys(h.hexdigest())
driver.find_element_by_xpath("/html/body/center/form/input[2]").click()