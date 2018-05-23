# @File  : wx_pay_util.py
# @Author: RedTree
# @Date  : 18-5-2
# @Desc  : 微信统一下单

import hashlib
import xml.etree.ElementTree as ET   #xml解码器
import time
import json
import requests
from random import Random

def random_str(randomlength=32):  #随机字符串生成算法
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]

    return str

#需要获取的用户的openid才可以进行统一下单,最后让前端通过接口调用到此工具返回的数据即可调用支付服务

def payment(openid,goodsid,goodsnum,totalpay):  #统一下单

    try:
        appid = 'wx123456'    #公众号id

        body = '根据前端传递的ID去获取商品名'     #商品名

        check_fee = '根据前端传的商品id和数量进行支付金额校验'

        # if not int(check_fee)==int(totalpay)*100:  #交易金额被传改，禁止交易
        #
        #     return json.dumps({'rcode': 400, 'msg': '下单失败002'})


        mch_id = '商户号'      #商户号
        nonceStr = random_str(32)    #随机串
        notifyurl = '用于接收微信支付结果通知' #支付回调链接
        out_trade_no = '商户自定义订单号，后台生成'        #订单号
        fee =   str(check_fee)             #总价
        serverIP = '部署服务器地址'    #服务器地址
        mch_key = '123666'  #支付密钥

        all_pay_url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'   #统一下单api地址

        stringA = "appid="+appid+"&body="+body+"&mch_id="+mch_id+"&nonce_str="+nonceStr+"&notify_url="+notifyurl+"&openid="+openid+"&out_trade_no="+out_trade_no+"&spbill_create_ip="+serverIP+"&total_fee="+fee+"&trade_type=JSAPI"
        stringSignTemp = stringA + "&key="+mch_key
        paysign = hashlib.md5(stringSignTemp.encode('utf-8')).hexdigest().upper()


        pay_xml = "<xml><appid>" + appid + "</appid><body>" + body + "</body><mch_id>" + mch_id + "</mch_id><nonce_str>" + nonceStr + "</nonce_str><notify_url>" + notifyurl + "</notify_url><openid>" + openid + "</openid><out_trade_no>" + out_trade_no + "</out_trade_no><spbill_create_ip>" + serverIP + "</spbill_create_ip><total_fee>" + fee + "</total_fee><trade_type>JSAPI</trade_type><sign>" + paysign + "</sign></xml> "

        headers = {'Content-Type': 'application/xml'}
        # 访问支付接口
        r = requests.post(all_pay_url, data=pay_xml.encode('utf-8'),
                           headers=headers)

        xml_recv = ET.fromstring(r.text)
        wxre_sign = xml_recv.find('sign').text  #用来校验签名认证

        prepay_id = xml_recv.find('prepay_id').text
        package = "prepay_id=" + prepay_id

        ctime = str(int(time.time()))

        stringB = "appId="+appid+"&nonceStr="+nonceStr+"&package="+package+"&signType=MD5&timeStamp="+ctime
        stringBSignTemp = stringB + "&key=???" #这里三个问号替换成商户密钥,不是公众号密钥
        paysign = hashlib.md5(stringBSignTemp.encode('utf-8')).hexdigest().upper()

        res_json = json.dumps({'rcode': 200, 'package': package, 'paysign': paysign, 'timestamp': ctime,
                               'nonceStr': nonceStr, 'appId': appid})

        # order_res = '这里调用数据库订单创建的逻辑'
        #
        # if not order_res == 'success':
        #     return json.dumps({'rcode': 400, 'msg': '订单创建失败'})

        return res_json

    except Exception as err:
        print(str(err) + '下单异常')
        return json.dumps({'rcode': 400, 'msg': '下单异常'})


