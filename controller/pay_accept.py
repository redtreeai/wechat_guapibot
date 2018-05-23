# @File  : pay_accept.py
# @Author: RedTree
# @Date  : 18-4-12
# @Desc  : 下单成功后的回调接口

from __init__ import make_response,request
from __init__ import app
import xml.etree.ElementTree as ET   #xml解码器

@app.route('/payaccept', methods=['GET','POST'])
def pay_accept():  # 导入:

    if request.method =='POST':
        xml_recv = ET.fromstring(request.data)
        return_code = xml_recv.find("return_code").text

        # openid=xml_recv.find("openid").text
        # total_fee=xml_recv.find("total_fee").text
        # out_trade_no = xml_recv.find("out_trade_no").text

        if return_code =='SUCCESS':

            reply = "<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>"

            response = make_response(reply)

            response.content_type = 'application/xml'

            res = '订单信息支付完成，调用更新数据的方法'

            if res =='success':
                return response

            else:
                return 'error'
    else:
        return  'whoareyou'
