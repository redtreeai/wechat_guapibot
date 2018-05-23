# @File  : user_info.py
# @Author: RedTree
# @Date  : 18-4-16
# @Desc  : 网页授权获取用户信息

import requests
import json
from utils import access_token_checker


def code_to_accesstoken(code):  #前端传入code
    try:
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='+'你的公众号id'+'&secret='+'你的公众号密钥'+'&code=' + code + '&grant_type=authorization_code'
        res = requests.get(url)
        rej = json.loads(res.text)
        ACCESS_TOKEN = access_token_checker.get_token()
        OPENID = rej['openid']
    except Exception as err:
        print(err)
        return json.dumps({'rcode': 400, 'msg':'openid_error'})

    try:  #获取用户信息
      url2 ='https://api.weixin.qq.com/cgi-bin/user/info?access_token='+ACCESS_TOKEN+'&openid='+OPENID
      user_info_res =  json.loads(requests.get(url2).text)
      nickname = (user_info_res['nickname'])
      openid = (user_info_res['openid'])
      headimgurl = (user_info_res['headimgurl'])
      province =(user_info_res['province'])
      city = (user_info_res['city'])


      return json.dumps({'rcode':200,'nickname':nickname,'openid':openid,'headimgurl':headimgurl,'province':province,'city':city})
    except Exception as err:
      print(err)
      return json.dumps({'rcode':400,'msg':'wxuser_info_error'})





