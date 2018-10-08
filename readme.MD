微信公众号 瓜皮机器人 源码公开

这是一个个人练手项目，主要完成了以下的功能:(公众号服务暂时关闭)

1 公众号自动回复   （图灵）

![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/118892967.jpg)

2 看图说话  （这里使用的是腾讯AILAB 的看图说话接口）

![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/1449614548.jpg)

3 微信支付  (python写的接入，网上这部分资料蛮少的，算是帮大家踩坑了)

4 H5商城()   （没有什么前端功底，凑合看）

![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/1701434209.jpg)
![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/2027057950.jpg)
![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/341708063.jpg)
![avatar](http://redtreeblog-1253690989.cosgz.myqcloud.com/guapi/885331751.jpg)


服务端采用PYTHON -FLASK 框架编写,商城使用VUE+MintUI组件。

#Flask的基础配置文件，这是最简化版

__init__.py

run.py

#controller 接口

  auto_chat_core   #微信公众号基础配置校验接口和核心对话业务

  buy_thing   #统一下单接口

  get_user_info #根据code 获取用户信息的接口

  pay_accept #统一支付结果通知接口

#utils 工具

  access_token_checker  #access_token校验工具，若超时自动重新获取

  get_meterial #素材获取

  get_user_auth #微信网页授权

  menu_tool #公众号菜单管理

  wx_pay_util #公众号支付，统一下单工具

#template 商城模板

 进入此目录，npm run dev 即可预览


