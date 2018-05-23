'''

@author: redtree

@contact: redtreec@gmail.com

@time: 17-12-29 下午2:30

@desc: 通过前端获取的code 换取用户的相关信息（昵称，地址，openid等）

'''


from __init__ import app
from __init__ import request
from utils import get_user_auth
import json

@app.route('/getuserinfo', methods=['GET'])
def getuserinfo():  # 导入:
    try:
        code = request.args.get('code')
        return get_user_auth.code_to_accesstoken(code)
    except:
        return json.dumps({'rcode': 400, 'msg':'http_param_error'})

