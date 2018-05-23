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
        <img src="https://img.alicdn.com/imgextra/i1/3045553940/TB2j4c1dpkoBKNjSZFkXXb4tFXa_!!3045553940.png"/>
      </mt-tab-container-item>
      <mt-tab-container-item :id="2">
        &nbsp;<video controls preload="auto" :width="screenWidth">
        <source :src="'/static/img/qibing.mp4'" type="video/mp4"/>
      </video>
        <mt-cell title="以下为第三放视频：">
        </mt-cell>
        <mt-cell value="播放" islink title="还珠格格机器人版" to="https://www.bilibili.com/video/av6177523?from=search&seid=14197345231134593141">
        </mt-cell>
        <mt-cell value="播放" islink title="会思考的教室" to="http://player.youku.com/embed/XMzM4MDI5NzkwMA==?client_id=a10c9c07db7b30c2&password=undefined&autoplay=true">
        </mt-cell>
        <mt-cell value="播放" islink title="小姐姐带你一起创作歌曲" to="https://www.bilibili.com/video/av17646290?from=search&seid=9243606624514598644">
        </mt-cell>
         <mt-cell value="播放" islink title="好莱坞编排舞蹈" to="https://www.bilibili.com/video/av17646290?from=search&seid=9243606624514598644">
        </mt-cell>

      </mt-tab-container-item>
    </mt-tab-container>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    <mt-button type="danger" plain @click.native="ddabuynum">-</mt-button>
    购买数量: {{buynum}}
    <mt-button type="primary" plain @click.native="addbuynum">+</mt-button>
    <mt-button type="default" plain @click.native="buysure"> 确认购买</mt-button>
    <mt-button type="default" disabled size="large" plain>单价:6999 元 总价: {{total_price}} 元</mt-button>
    <mt-button type="default" disabled size="large" plain>大批量采购请联系客服</mt-button>

  </div>


</template>
<script>

  import MtButton from "mint-ui/packages/button/src/button";
  import MtField from "mint-ui/packages/field/src/field";
  import {Toast} from 'mint-ui';
  import MtCell from "mint-ui/packages/cell/src/cell";

  export default {
    components: {MtCell},
    data() {
      return {
        selected: 2,
        buynum: 0,
        screenWidth: document.body.clientWidth,// 这里是给到了一个默认值 （这个很重要）
        goodsid: 2,
        total_price: 0,
        morenaddr: ''
      }
    },
    created() {
    },

    methods: {
      addbuynum() {
        this.buynum++
        this.total_price = this.buynum * 6999
      },
      ddabuynum() {
        this.buynum--
        if (this.buynum < 0) {
          this.buynum = 0

        }
        this.total_price = this.buynum * 6999
      }
      ,
      buysure() {

        let self = this
        //获取收货地址
        self.url = 'http://api.redtreeai.com/getmorenaddr';
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
