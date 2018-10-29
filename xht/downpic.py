import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    print(html)
    return html

def reUrl(html):
    reg  = r"src=(\".*\.jpg)"
    imgre = re.compile(reg)
    imglist  =re.findall(imgre,html)
    print(imglist)

def downpic(url):
    pass

getHtml("http://tieba.baidu.com/p/4785743947")