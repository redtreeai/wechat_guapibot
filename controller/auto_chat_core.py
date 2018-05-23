# @File  : auto_chat_core.py
# @Author: RedTree
# @Date  : 18-5-2
# @Desc  :  公众号自动回复逻辑,对话聊天服务入口

from __init__ import app
from __init__ import request
from __init__ import make_response
import hashlib
import xml.etree.ElementTree as ET   #xml解码器
import time
import random

#通过FLASK 配置验证接口

@app.route('/chatcore', methods=['GET','POST'])
def chatcore():  # 导入:

    if request.method=='GET':   #为get请求是时是配置校验
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')

        token = '公众号配置的token' #公众号配置的token

        check_dict = [token,timestamp,nonce]
        check_dict.sort()

        check_str = str_encrypt(check_dict[0].encode('utf-8')+check_dict[1].encode('utf-8')+check_dict[2].encode('utf-8'))

        if check_str == signature:
            return echostr
        else:
            return 'error'

    else:   #为POST请求时候是数据传递,微信公众号采用的是XML数据格式
        # Get the infomations from the recv_xml.
        try:
            xml_recv = ET.fromstring(request.data)
            Msg_Type =  xml_recv.find("MsgType").text

            if Msg_Type =='image':  #当接受到图片的时候，进行对应回复
                ToUserName = xml_recv.find("ToUserName").text
                FromUserName = xml_recv.find("FromUserName").text
                PicUrl = xml_recv.find("PicUrl").text


                res_content = '我收到了你发的照片'

                if res_content =='error':
                    return 'success'
                else:

                    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"


                    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), res_content))

                    response.content_type = 'application/xml'
                    return response


            elif  Msg_Type =='text':   #这里接受到文字信息

                ToUserName = xml_recv.find("ToUserName").text
                FromUserName = xml_recv.find("FromUserName").text
                Content = xml_recv.find("Content").text

                res_content = '我收到了你发的文字'

                if res_content =='success':
                    return 'success'
                else:

                    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"


                    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), res_content))

                    response.content_type = 'application/xml'
                    return response

            elif Msg_Type =='event':  #这里是事件监听
                Event = xml_recv.find("Event").text
                if Event =='subscribe': #用户关注公众号
                    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[image]]></MsgType><Image><MediaId><![CDATA[%s]]></MediaId></Image><FuncFlag>0</FuncFlag></xml>"

                    ToUserName = xml_recv.find("ToUserName").text #openid
                    FromUserName = xml_recv.find("FromUserName").text
                    res_image_id = '素材id'
                    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())),res_image_id))
                    response.content_type = 'application/xml'

                    #用户注册事件在这里补充

                    return response

                if Event == 'unsubscribe':
                    #用户取关

                    # 用户删除事件
                    return 'success'

                EventKey = xml_recv.find("EventKey").text

                if Event=='CLICK' and EventKey =='shop': #点击菜单栏时间
                    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

                    ToUserName = xml_recv.find("ToUserName").text
                    FromUserName = xml_recv.find("FromUserName").text

                    res_content='小店装修中。'
                    response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), res_content))
                    response.content_type = 'application/xml'
                    return response


                return 'success'

            else:
                return 'success'
        except Exception as  err:
            print('服务器异常'+str(err))
            return 'success'

def str_encrypt(str):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts