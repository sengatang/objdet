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


def crawl_pic(base_path, keyword, page_num):
    global count_overall
    count_overall = 0
    for i in range(0,page_num):
        print(i, datetime.datetime.now())
        url = getURL(keyword, i+1)
        data = open_url(url)
        pic_urls = re.findall('"objURL":"(.*?)",', data, re.S)
        
        for pic in pic_urls:
            if count_overall % 100 == 0:
                try:
                    os.makedirs(base_path + str(count_overall//100))
                except Exception as e:
                    print(e)
                    pass
                try:
                    os.makedirs(base_path + str(count_overall//100) + '/training')
                    os.makedirs(base_path + str(count_overall//100) + '/test')
                except Exception as e:
                    print(e)
                    pass
            root_dir = base_path + str(count_overall//100)
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


base_path = 'img file/bicycle/'
crawl_pic(base_path, '自行车', 20)


    
    






