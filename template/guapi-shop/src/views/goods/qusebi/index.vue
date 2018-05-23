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
        <img src="https://img.alicdn.com/imgextra/i4/3393680582/TB2vQFRanJYBeNjy1zeXXahzVXa_!!3393680582.jpg"/>
      </mt-tab-container-item>
      <mt-tab-container-item :id="2">
        &nbsp;<video controls preload="auto" :width="screenWidth">
        <source :src="'/static/img/xisebi.mp4'" type="video/mp4"/>
      </video>
      </mt-tab-container-item>
    </mt-tab-container>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    <mt-button type="danger" plain @click.native="ddabuynum">-</mt-button>
    购买数量: {{buynum}}
    <mt-button type="primary" plain @click.native="addbuynum">+</mt-button>
    <mt-button type="default" plain @click.native="buysure"> 确认购买</mt-button>
    <mt-button type="default" disabled size="large" plain>单价:299 元 总价: {{total_price}} 元</mt-button>

  </div>


</template>
<script>

  import MtButton from "mint-ui/packages/button/src/button";
  import MtField from "mint-ui/packages/field/src/field";
  import {Toast} from 'mint-ui';

  export default {
    data() {
      return {
        selected: 2,
        buynum: 0,
        screenWidth: document.body.clientWidth,// 这里是给到了一个默认值 （这个很重要）
        goodsid: 1,
        total_price: 0,
        morenaddr: ''
      }
    },
    created() {
    },

    methods: {
      addbuynum() {
        this.buynum++
        this.total_price = this.buynum * 299
      },
      ddabuynum() {
        this.buynum--
        if (this.buynum < 0) {
          this.buynum = 0

        }
        this.total_price = this.buynum * 299
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
             if (self.morenaddr == 'error' || self.morenaddr=='') {
            alert('请先在收货地址中添加默认地址')
            self.$router.push('/addr');
          } else {
            if (self.buynum>0){

               localStorage.setItem('wx_morenaddr', self.morenaddr)
            localStorage.setItem('wx_lastbuyid', self.goodsid)
            localStorage.setItem('wx_lastbuynum', self.buynum)
            localStorage.setItem('wx_lastbuyprice', self.total_price)
            this.$router.push('/pay');
            }else {
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
