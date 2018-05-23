'''

@author: redtree

@contact: redtreec@gmail.com

@time: 17-3-15 下午2:28

@desc:
'''
from flask_cors import CORS
from flask import Flask, request,make_response


# 初始化Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

request = request  # 注册request对象
make_response =make_response #注册make_response对象








