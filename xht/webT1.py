# import urllib.request
# import webbrowser as web

# url = "http://www.baidu.com"
# content = urllib.request.urlopen(url).read()
# with open("d:/baidu.html","wb") as f :
#     f.write(content)
# web.open_new_tab("d:/baidu.html")
#coding=utf-8  
import os  
import urllib  
from selenium import webdriver            
from selenium.webdriver.common.keys import Keys            
  
  
#Open PhantomJS        
#driver = webdriver.PhantomJS(executable_path="phantomjs-1.9.1-windows\phantomjs.exe")    
driver = webdriver.Ie()  
  
#访问url  
driver.get("https://www.baidu.com/")      
  
# print(u'URL:'  )
print( driver.current_url )   
#当前链接: https://www.baidu.com/    
  
# print u'标题:'  
# print driver.title    
# #标题: 百度一下， 你就知道    
    
# #print driver.page_source  
# #源代码  
  
# #定位元素，注意u1（数字1）和ul（字母L）区别  
# print u'\n\n定位元素id:'  
# info1 = driver.find_element_by_id("u1").text  
# print info1  
  
  
# #定位元素  
# print u'\n\n定位元素xpath:'  
# info3 = driver.find_element_by_xpath("//div[@id='u1']/a")  
# print info3.text  