# -*- coding: utf-8 -*-
#Author: zehua liu
#Env python 3

import requests
import re
import time
#from bs4 import BeautifulSoup
import io  
import sys  
import urllib.request  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码  
def gae(pages):
    for n in range(1,pages):
        url= 'http://www.ygdy8.net/html/gndy/china/list_4_'+str(n)+'.html'
        html_1=requests.get(url)
        #request.post
        html_1.encoding='gb2312'
        #print(html_1.text)
        #time.sleep(0)#防反爬
        print(html_1.status_code)
        detail=re.findall('<a href="(.*?)" class="ulink',html_1.text)
        #print(detail)
    for m in detail:
        url2='http://www.ygdy8.net/'+m

        #print url2
        html2=requests.get(url2)
        html2.encoding='gb2312'
        #time.sleep(0)
        ftp=re.findall('<a href="(.*?)">.*?</a></td>',html2.text)
        print(ftp)
        with open('C:\\Users\\Mr. Liu\\Desktop\\dytt\\dytt.txt','a',encoding='utf-8') as ff:
            ff.write(ftp[0]+'\n')
gae(3)#get first 3 pages