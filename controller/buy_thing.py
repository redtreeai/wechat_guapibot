# @File  : buy_thing.py
# @Author: RedTree
# @Date  : 18-4-12
# @Desc  : 统一下单校验接口

from __init__ import app,request
from utils import  wx_pay_util

@app.route('/buything', methods=['GET','POST'])
def buything():  # 导入:

    try:
        openid = request.args.get('openid')
        goodsid = request.args.get('goodsid')
        goodsnum = request.args.get('goodsnum')
        totalpay = request.args.get('totalpay')


        if openid == 'undefined':
            return 'auth-error'
        return wx_pay_util.payment(openid,goodsid,goodsnum,totalpay)

    except Exception as err:
        print('统一下单失败'+str(err))
        return 'auth-error'


