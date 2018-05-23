<template>
  <div class="app-init scroll-box mine-page ">
    <mt-header title="收货地址管理">
      <router-link to="/" slot="left">
        <mt-button icon="back">返回</mt-button>
      </router-link>
    </mt-header>

    <li v-for="addr in addrList">

      <mt-cell :title='addr.reciever+kongge+addr.phone' :label='addr.province+kongge+addr.city+kongge+addr.county'>

        <mt-badge size="small" v-if="addr.moren==0" type="primary">默认地址</mt-badge>

        <mt-button size="small" plain :disabled="addr.moren==0" @click.native="setmoren(addr.id)">设为默认</mt-button>

        <mt-button size="small" type="danger" plain @click.native="deleteaddr(addr.id,addr.moren)">删除</mt-button>


      </mt-cell>
      <mt-field label="详细地址" disabled type="textarea" rows="4" v-model="addr.detail"></mt-field>


    </li>

    <mt-button type="primary" plain size="large" @click="$router.openPage('/addaddr')">点击新增地址</mt-button>
  </div>
</template>
<script>
  import {Toast} from 'mint-ui';

  export default {
    data() {
      return {
        addrList: [],
        kongge: ' '
      }
    },
    created() {
      this.getdata();
    },
    methods: {
      getdata() {   //获取微信用户地址数据
        let self = this;
        self.url = 'http://api.yourserver.com/getaddress';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid')
          }
        }).then((res) => {
          //获取数据成功
          if (res.data.msg === 'success') {
            self.addrList = res.data.list
          } else {
            Toast({
              message: '收货地址获取失败',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          }
        })
      }
      ,
      deleteaddr(id, moren) {

        if (moren == 0) {
          Toast({
            message: '无法删除默认地址',
            iconClass: 'icon icon-success',
            duration: 1000
          });
        } else {
          let self = this;
          self.url = 'http://api.yourserver.com/deladdress';
          self.$axios.get(self.url, {
            params: {
              openid: localStorage.getItem('wx_openid'),
              id: id
            }
          }).then((res) => {
            //获取数据成功
            if (res.data === 'success') {
              Toast({
                message: '删除成功',
                iconClass: 'icon icon-success',
                duration: 1000
              });
              this.getdata()
            } else {
              Toast({
                message: '删除失败 网络异常',
                iconClass: 'icon icon-success',
                duration: 1000
              });
            }
          })
        }


      }
      ,
      setmoren(id) {


        let self = this;
        self.url = 'http://api.redtreeai.com/setmoren';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid'),
            id: id
          }
        }).then((res) => {
          //获取数据成功
          if (res.data === 'success') {
            Toast({
              message: '设置成功',
              iconClass: 'icon icon-success',
              duration: 1000
            });
            this.getdata()
          } else {
            Toast({
              message: '设置失败 网络异常',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          }
        })
      }


    },
  }

</script>

