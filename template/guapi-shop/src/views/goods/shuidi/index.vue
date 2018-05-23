<template>
  <div class="app-init scroll-box mine-page ">
    <mt-header title="商品介绍">
      <router-link to="/" slot="left">
        <mt-button icon="back">取消</mt-button>
      </router-link>
    </mt-header>
    <mt-navbar v-model="selected">
      <mt-tab-item :id="1">详细介绍</mt-tab-item>
      <mt-tab-item :id="2">视频演示</mt-tab-item>
    </mt-navbar>

    <!-- tab-container -->
    <mt-tab-container v-model="selected">
      <mt-tab-container-item :id="1">
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/2b9ef243-ab0f-4c49-b416-4e25ba4d6172.jpg"/>
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/827eecb8-515f-4bcf-a6e8-48a29cafd274.jpg"/>
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/69709cc9-0b91-42cc-b562-dd55f53953a0.jpg"/>
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/05144c53-368d-41bb-9b1d-30102f31ed43.jpg"/>
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/3b3cfc4f-4924-4dfd-b404-30359b158b88.jpg"/>
        <img src="http://img01.mall.cmbchina.com/ProductLongDesc/2017-11-06/0ff063ce-f7e6-4e8a-bd8d-bf2c61741b2b.jpg"/>
      </mt-tab-container-item>
      <mt-tab-container-item :id="2">
        <mt-cell title="宣传片制作中，以下为第三放视频：">
        </mt-cell>
        <mt-cell value="播放" islink title="手册玩法" to="https://v.qq.com/x/page/b0563nqdc64.html">
        </mt-cell>
        <mt-cell value="播放" islink title="地图玩法" to="https://v.qq.com/x/page/s0563d67y2e.html">
        </mt-cell>
        <mt-cell value="播放" islink title="触摸点展示" to="http://www.iqiyi.com/w_19ruyd0pct.html">
        </mt-cell>
        <mt-cell value="播放" islink title="星球玩法" to="http://www.pps.tv/w_19ruyd1p8d.html">
        </mt-cell>
        <mt-cell value="播放" islink title="儿童陪伴"
                 to="http://player.youku.com/embed/XMzE1NDg5NjEyOA==?client_id=a10c9c07db7b30c2&password=undefined&autoplay=true">
        </mt-cell>

      </mt-tab-container-item>
    </mt-tab-container>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    <mt-button type="danger" plain @click.native="ddabuynum">-</mt-button>
    购买数量: {{buynum}}
    <mt-button type="primary" plain @click.native="addbuynum">+</mt-button>
    <mt-button type="default" plain @click.native="buysure"> 确认购买</mt-button>
    <mt-button type="default" disabled size="large" plain>单价:2999 元 总价: {{total_price}} 元</mt-button>

  </div>


</template>
<script>

  import MtButton from "mint-ui/packages/button/src/button";
  import MtField from "mint-ui/packages/field/src/field";
  import {Toast} from 'mint-ui';

  export default {
    data() {
      return {
        selected: 1,
        buynum: 0,
        screenWidth: document.body.clientWidth,// 这里是给到了一个默认值 （这个很重要）
        goodsid: 3,
        total_price: 0,
        morenaddr: ''
      }
    },
    created() {
    },

    methods: {
      addbuynum() {
        this.buynum++
        this.total_price = this.buynum * 2999
      },
      ddabuynum() {
        this.buynum--
        if (this.buynum < 0) {
          this.buynum = 0

        }
        this.total_price = this.buynum * 2999
      }
      ,
      buysure() {

        let self = this
        //获取收货地址
        self.url = 'http://api.yourserver.com/getmorenaddr';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid')
          }
        }).then((res) => {
          self.morenaddr = res.data
          if (self.morenaddr == 'error' || self.morenaddr == '') {
            alert('请先在收货地址中添加默认地址')
            self.$router.push('/addr');
          } else {
            if (self.buynum > 0) {

              localStorage.setItem('wx_morenaddr', self.morenaddr)
              localStorage.setItem('wx_lastbuyid', self.goodsid)
              localStorage.setItem('wx_lastbuynum', self.buynum)
              localStorage.setItem('wx_lastbuyprice', self.total_price)
              this.$router.push('/pay');
            } else {
              Toast({
                message: '请添加购买数量',
                iconClass: 'icon icon-success',
                duration: 1000
              });
            }
          }
        })

      }


    }
  }


</script>
