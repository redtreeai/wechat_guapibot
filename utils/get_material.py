# @File  : get_material.py
# @Author: RedTree
# @Date  : 18-4-11
# @Desc  :  素材列表相关

import requests
from utils import access_token_checker
import json

def get_list():  #获取素材列表

    access_token = access_token_checker.get_token()

    url= 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token='+access_token.replace('\n','')

    TYPE= 'image'   #素材的类型，图片（image）、视频（video）、语音 （voice）、图文（news）
    OFFSET = 0   #从全部素材的该偏移位置开始返回，0表示从第一个素材 返回
    COUNT = 20 #返回素材的数量，取值在1到20之间

    p_data = {
        "type": TYPE,
        "offset": OFFSET,
        "count": COUNT
    }

    r = requests.post(url,json.dumps(p_data,ensure_ascii=False).encode('utf-8') )
    print(r.text)


#get_list()