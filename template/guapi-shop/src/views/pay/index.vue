<template>
  <div class="app-init pay-page scroll-box">
    <mt-header title="支付订单详情">
      <router-link to="/" slot="left">
        <mt-button icon="back">取消</mt-button>
      </router-link>
    </mt-header>
    <mt-cell title="商品名称" :value="goodsname"></mt-cell>
    <mt-cell title="购买数量" :value="goodsnum"></mt-cell>
    <mt-cell title="支付金额(人民币)" :value='totalpay+"元"'></mt-cell>
    <mt-field label="收货信息" disabled type="textarea" rows="4" v-model="morenaddr"></mt-field>
    <mt-button type="primary" size="large" @click="pay()">确认支付</mt-button>
  </div>

</template>

<script type="text/ecmascript-6">

  import MtField from "mint-ui/packages/field/src/field";

  export default {
    components: {MtField},
    data() {
      return {

        appId: '',
        timeStamp: '',
        nonceStr: '',
        package: '',
        paySign: '',
        goodsid: 0,
        goodsnum: 0,
        totalpay: 0,
        goodsname: '',
        morenaddr: ''
      }
    },
    created() {
      this.getdata();
    },
    methods: {

      getdata() {   //支付订单

        let self = this;

        if (localStorage.getItem('wx_openid') == 'undefined') {
          alert('请在微信公众号中打开此页面')
          window.location.href = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxf7af25c6d9e9fb2e&redirect_uri=http%3a%2f%2fpay.redtreeai.com&response_type=code&scope=snsapi_base&state=1&connect_redirect=1#wechat_redirect";
        }

        self.morenaddr = localStorage.getItem('wx_morenaddr')
        if (self.morenaddr == '' || self.morenaddr == 'error') {
          alert('请先在收货地址中添加默认地址')
          self.$router.push('/addr');
        } else {
          self.goodsid = localStorage.getItem('wx_lastbuyid')
          self.goodsnum = localStorage.getItem('wx_lastbuynum')
          self.totalpay = localStorage.getItem('wx_lastbuyprice')

          //获取商品名字
          self.url = 'http://api.yourserver.com/getgoodsname';
          self.$axios.get(self.url, {
            params: {
              id: self.goodsid
            }
          }).then((res) => {
            self.goodsname = res.data
            //获取支付凭证
            self.url = 'http://api.yourserver.com/buything';
            self.$axios.get(self.url, {
              params: {
                openid: localStorage.getItem('wx_openid'),
                goodsid: self.goodsid,
                goodsnum: self.goodsnum,
                totalpay: self.totalpay
              }
            }).then((res) => {
              //获取数据成功
              if (res.data.rcode === 200) {
                self.appId = res.data.appId
                self.timeStamp = res.data.timestamp
                self.nonceStr = res.data.nonceStr
                self.package = res.data.package
                self.paySign = res.data.paysign
              } else {
                alert('支付发起失败')
              }
            })
          })


        }
      },
      onBridgeReady() {
        WeixinJSBridge.invoke(
          'getBrandWCPayRequest', {
            "appId": this.appId,     //公众号名称，由商户传入
            "timeStamp": this.timeStamp,         //时间戳，自1970年以来的秒数
            "nonceStr": this.nonceStr, //随机串
            "package": this.package,
            "signType": "MD5",         //微信签名方式：
            "paySign": this.paySign //微信签名
          },
          function (res) {
            if (res.err_msg == "get_brand_wcpay_request:ok") {
              window.location.href = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxf7af25c6d9e9fb2e&redirect_uri=http%3a%2f%2fpay.redtreeai.com&response_type=code&scope=snsapi_base&state=1&connect_redirect=1#wechat_redirect";
            }     // 使用以上方式判断前端返回,微信团队郑重提示：res.err_msg将在用户支付成功后返回    ok，但并不保证它绝对可靠。
          }
        );
      },

      pay() {
        if (typeof WeixinJSBridge == "undefined") {
          if (document.addEventListener) {
            document.addEventListener('WeixinJSBridgeReady', this.onBridgeReady, false);
          } else if (document.attachEvent) {
            document.attachEvent('WeixinJSBridgeReady', this.onBridgeReady);
            document.attachEvent('onWeixinJSBridgeReady', this.onBridgeReady);
          }
        } else {
          this.onBridgeReady();
        }
      }
    }
  }

</script>

<style type="text/sass" lang="sass">
  .pay-page
    background-color: white
    text-overflow: ellipsis

    .padding-box
      padding: 0.4rem
      color: #333
      .color
        color: orange
      ul
        padding-left: 0.8rem
      li
        list-style: disc
        margin: 0 auto

    .addr
      white-space: nowrap
      overflow: hidden
      text-overflow: ellipsis
      width: 250px

</style>
