# @File  : create_menu.py
# @Author: RedTree
# @Date  : 18-4-3
# @Desc  : 菜单自定义工具
import requests
from utils import access_token_checker
import json

def create():  #创建

    access_token = access_token_checker.get_token()

    url= 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+access_token.replace('\n','')

    #d={"button":[{"type":"click","name":"test","key":"test"}]}



    d={
     "button":[
     {
          "type":"view",
          "name":"神秘小店",
          "url":"https:www.baidu.com"
      },
      {
           "name":"产品推广",
           "sub_button":[
               {
                   "type": "view",
                   "name": "略",
                   "url": "https:www.baidu.com"
               },
               {
                   "type": "view",
                   "name": "略",
                   "url": "https:www.baidu.com"
               }

          ]
       }
     ]
 }

    


    r = requests.post(url,json.dumps(d,ensure_ascii=False).encode('utf-8') )

    print(r.text)


def delete(): #复原

    access_token = access_token_checker.get_token()

    url= 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='+access_token.replace('\n','')

    r = requests.get(url)

    print(r.text)

#create()
#delete()