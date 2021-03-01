# -*- coding: utf-8 -*-

## 李运辰 2021-2-18
import threading
import requests
import json
import os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',}

###下载ts文件
def download(url,name):
    r = requests.get(url, headers=headers)
    with open(name+"", "wb") as code:
        code.write(r.content)

with open("index.m3u8","r") as f:
    ts_list = f.readlines()

#去掉前面没用的信息
ts_list = ts_list[5:]
urlheader="https://xigua-cdn.haima-zuida.com/20210219/19948_fcbc225a/1000k/hls/"

for i in ts_list:
    if "#" not in i:
        i = i.replace("\n","")
        n = i[-7:]
        if os.path.exists("cdzj2/"+str(n)):
            pass
        else:
            #threading.Thread(target=download, args=(urlheader+""+i,"cdzj2/"+str(n),)).start()
            download(urlheader+""+i,"cdzj2/"+str(n))



