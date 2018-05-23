# @File  : access_token_checker.py
# @Author: RedTree
# @Date  : 18-5-2
# @Desc  : 自动获取accessToken   通过本地文本保存accesstoken_信息,每次获取时校验时间戳，若超时则重新获取

import requests
import json
import time

def get_token():

    f=open('your_project_root_path'+'/token.txt', 'r')
    data = f.readlines()
    f.close()

    APP_ID = '公众号id'  # 公众号id
    APP_SECRET = '公众号密钥'  # 公众号密钥
    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=' + APP_ID + '&secret=' + APP_SECRET

    if not data:  #当没有token时候

        r = requests.get(url)
        token = json.loads(r.text)['access_token']

        f = open('your_project_root_path'+'/token.txt', 'w')
        f.write(token+'\n'+str(int(time.time())))

        return token

    elif (int(time.time())-int(data[1])) >=7200:  #超过时间 重新获取

        APP_ID = '公众号id'  # 公众号id
        APP_SECRET = '公众号密钥'  # 公众号密钥
        url = 'https://api.weixin.qq.com/cgi-bin/token?' \
              'grant_type=client_credential&appid=' + APP_ID + '&secret=' + APP_SECRET

        r = requests.get(url)
        print(r.text)
        token = json.loads(r.text)['access_token']

        f = open('your_project_root_path'+'/token.txt', 'w')
        f.write(token + '\n' + str(int(time.time())))


        return token


    else:
        return str(data[0]).replace('\n','')
