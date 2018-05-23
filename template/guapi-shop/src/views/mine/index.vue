<template>

  <div class="app-init scroll-box mine-page ">
    <div class="user-box public-padding">
      <div class="face-book">
        <img @click="$router.openPage('')" v-bind:src="headimgurl" alt="">
      </div>
      <p class="fl"> 您好 {{ nickname }}, 来自 {{province}} {{city}} </p>

    </div>

    <div class="dingdan public-padding p-item" @click="$router.openPage('order')">
      我的订单
    </div>
    <div class="dingdan public-padding p-item" @click="$router.openPage('/addr')">
      收货地址管理
    </div>

    <div style="position:absolute; height:500px; overflow:auto">
      <div @click="$router.openPage('/shuidi')">
        <a>
          <img :src="shuidi_img">
        </a>
      </div>
      <div @click="$router.openPage('/qusebi')">
        <a>
          <img :src="xisebi_img">
        </a>
      </div>
      <div @click="$router.openPage('/qibing')">
        <a>
          <img :src="qibing_img">
        </a>
      </div>


    </div>

  </div>

</template>

<script type="text/ecmascript-6">
  export default {
    data() {
      return {
        nickname: '',
        headimgurl: 'http://oz3tayfme.bkt.clouddn.com/show.liluo.cc/normal-face.png',
        province: '',
        city: '',
        openid: '',
        shuidi_img: require('./img/shuidi.png'),
        xisebi_img: require('./img/qusebi.jpg'),
        qibing_img: require('./img/qibing.jpg'),


      }
    },
    created() {
      this.getdata();
      if(localStorage.getItem('wx_openid')=='undefined'){
        this.getdata()
      }
    },

    methods: {
      getdata() {   //获取微信用户数据
        let self = this;


        let cur_code = this.$utils.getUrlKey("code")

        if (cur_code === localStorage.getItem('wx_lastcode')) {
          self.nickname = localStorage.getItem('wx_nickname')
          self.openid = localStorage.getItem('wx_openid')
          self.headimgurl = localStorage.getItem('wx_headimgurl')
          self.province = localStorage.getItem('wx_province')
          self.city = localStorage.getItem('wx_city')
        } else {
          if (cur_code != undefined) {
            self.url = 'http://api.yourserver.com/getuserinfo';
            self.$axios.get(self.url, {
              params: {
                code: cur_code,
              }
            }).then((res) => {
              //获取数据成功
              if (res.data.rcode === 200) {
                self.nickname = res.data.nickname
                self.openid = res.data.openid
                self.headimgurl = res.data.headimgurl
                self.province = res.data.province
                self.city = res.data.city

                localStorage.setItem('wx_nickname', res.data.nickname);
                localStorage.setItem('wx_openid', res.data.openid);
                localStorage.setItem('wx_headimgurl', res.data.headimgurl);
                localStorage.setItem('wx_province', res.data.province);
                localStorage.setItem('wx_city', res.data.city);
                localStorage.setItem('wx_lastcode', cur_code)


              }
            })

          } else {
            self.nickname = localStorage.getItem('wx_nickname')
            self.openid = localStorage.getItem('wx_openid')
            self.headimgurl = localStorage.getItem('wx_headimgurl')
            self.province = localStorage.getItem('wx_province')
            self.city = localStorage.getItem('wx_city')
          }
        }


      },
    }
  }

</script>


<style type="text/sass" lang="sass">
  @import "../../assets/sass/util"
  .mine-page

    .public-padding
      padding: 0 getIphonese(30px)

    .user-box
      height: getIphonese(142px)
      background: black repeat top center
      background-size: 7.7rem
      @include box-sizing
      padding-top: getIphonese(28px)
      padding-bottom: getIphonese(28px)

    .user-box
      line-height: 1.33rem
      .face-book
        width: 1.33rem
        height: 1.33rem
        float: left
        border-radius: 100%
        border: 3px solid hsla(0, 0%, 100%, .4)
        overflow: hidden
        @include box-sizing
        img
          width: 100%
          height: 100%
      p
        padding-left: 0.2rem
        color: #fff
        @include f12px

    .dingdan
      line-height: getIphonese(80px)
    .p-item:active
      background-color: #eee
    .p-item
      background-color: #fff
      color: rgba(0, 0, 0, .87)
      position: relative
      border-bottom: 1px solid #D9D9D9
    .p-item:after
      font-family: 'iconfont'
      content: "\e628"
      position: absolute
      right: getIphonese(26px)
      color: #777777
    .new-wrap
      background-color: #fff
      margin-bottom: 0.26rem
      .p-item
        position: relative
        border-bottom: none
        padding-left: 1.5rem
        @include f12px
      .p-item:before
        position: absolute
        content: ''
        display: block
        width: 8.44rem
        right: 0px
        bottom: 0px

        border-bottom: 1px solid #D9D9D9
      .p-item:last-child:before
        border-bottom: none

      .iconfont
        font-size: 0.65rem
        width: 0.8rem
        display: inline-block
        text-align: center
        position: absolute
        left: 0.5rem

    .tab-box
      background-color: #fff
      margin-bottom: 0.26rem
      .item
        float: left
        width: 33.3%
        text-align: center
        height: 2.32rem
        .icon
          font-size: 0.6rem
          color: #A4A4A4
          padding-top: 0.36rem
        .name
          @include f12px
          padding-top: 0.1rem
      .item:active
        background-color: #eee

</style>
