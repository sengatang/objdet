import urllib
import os
import re
import random
import datetime
import requests

def getURL(keyword,page):
    keyword=urllib.parse.quote(keyword, safe='/')
    url_begin= "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin+ keyword + "&pn=" +str(page) + "&gsm="+str(hex(page))+"&ct=&ic=0&lm=-1&width=0&height=0"
    return url

def open_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


def bias_coin():
    p = random.random()
    return 0 if p < 0.6 else 1

# def get_img_raw(data):
#     reg = 'src="(.+?\.jpg)" alt='
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, data)
#     return imglist


global count_overall
count_overall = 700

for i in range(10,30):
    print(i, datetime.datetime.now())
    url = getURL('狗', i+1)
    data = open_url(url)
    pic_urls = re.findall('"objURL":"(.*?)",', data, re.S)
    for pic in pic_urls:
        if count_overall % 100 == 0:
            try:
                os.makedirs(str(count_overall//100))
            except Exception as e:
                print(e)
                pass
            try:
                os.makedirs(str(count_overall//100) + '/training')
                os.makedirs(str(count_overall//100) + '/test')
            except Exception as e:
                print(e)
                pass
        root_dir = str(count_overall//100)
        inside_dir = '/training' if not bias_coin() else '/test'
        dir_path = root_dir + inside_dir
        try:
            pic = requests.get(pic, timeout=15)
        except:
            continue
        fiel_name =str(count_overall + 1) + '.jpg'
        dir_path = dir_path + '/' + fiel_name
        try:
            with open(dir_path, 'wb') as f:
                f.write(pic.content)
        except Exception as e:
            print(e)
            continue
        count_overall += 1





    
    






