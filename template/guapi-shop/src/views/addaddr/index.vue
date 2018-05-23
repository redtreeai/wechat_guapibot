<template>
  <div class="app-init scroll-box mine-page ">
    <mt-header title="新增收货地址">
      <router-link to="/addr" slot="left">
        <mt-button icon="back">取消</mt-button>
      </router-link>
    </mt-header>
    <div>
      <mt-picker :slots="myAddressSlots" @change="onMyAddressChange"></mt-picker>
    </div>
    <div>
      <mt-field label="收货地址" v-bind:readonly="true">{{myAddressProvince}} {{myAddressCity}} {{myAddresscounty}}
      </mt-field>
      <mt-field  :attr="{ maxlength: 50 }" label="详细地址" placeholder="（街道+小区+门号 请填写尽量详细）" type="textarea" rows="4" v-model="detailAddress"></mt-field>
      <mt-field   :attr="{ maxlength: 4 }" label="收货人" placeholder="XXXX" v-model="myname"></mt-field>
      <mt-field  :attr="{ maxlength: 11 }" label="手机号" placeholder="请输入手机号" type="tel" v-model="myphone"></mt-field>
      <mt-cell title="设为默认地址">
        <mt-switch v-model="ismoren"></mt-switch>
      </mt-cell>
      <mt-button type="primary" plain size="large" @click.native="addAddress">确认添加</mt-button>

    </div>
  </div>
</template>
<script>
  import {Picker} from 'mint-ui';
  import { Toast } from 'mint-ui';

  import myaddress from './json/myaddress.json'     //引入省市区数据
  export default {
    name: '',
    components: {
      'mt-picker': Picker
    },
    props: {},
    data() {
      return {
        myAddressSlots: [
          {
            flex: 1,
            defaultIndex: 1,
            values: Object.keys(myaddress),  //省份数组
            className: 'slot1',
            textAlign: 'center'
          }, {
            divider: true,
            content: '-',
            className: 'slot2'
          }, {
            flex: 1,
            values: [],
            className: 'slot3',
            textAlign: 'center'
          },
          {
            divider: true,
            content: '-',
            className: 'slot4'
          },
          {
            flex: 1,
            values: [],
            className: 'slot5',
            textAlign: 'center'
          }
        ],
        myAddressProvince: '省',
        myAddressCity: '市',
        myAddresscounty: '区/县',
        detailAddress: '',
        myname: '',
        myphone: '',
        ismoren: false,

      }
    },
    created() {
    },

    methods: {
      onMyAddressChange(picker, values) {
        if (myaddress[values[0]]) {  //这个判断类似于v-if的效果（可以不加，但是vue会报错，很不爽）
          picker.setSlotValues(1, Object.keys(myaddress[values[0]])); // Object.keys()会返回一个数组，当前省的数组
          picker.setSlotValues(2, myaddress[values[0]][values[1]]); // 区/县数据就是一个数组
          this.myAddressProvince = values[0];
          this.myAddressCity = values[1];
          this.myAddresscounty = values[2];
        }
      },

      addAddress() {
        let self = this
        let moren_flag = 1
        if (self.ismoren == true) {
          moren_flag = 0
        }
        self.url = 'http://api.yourserver.com/addaddress';
        self.$axios.post(self.url, {
          "openid": localStorage.getItem('wx_openid'),
          "province": self.myAddressProvince,
          "city": self.myAddressCity,
          "county": self.myAddresscounty,
          "detail": self.detailAddress,
          "reciever": self.myname,
          "phone": self.myphone,
          "moren": moren_flag

        }).then((res) => {

          if (res.data=='addressover'){
             Toast({
              message: '地址过多',
              iconClass: 'icon icon-success',
              duration: 1000
             });
          }else {
            //获取数据成功
          if (res.data == 'success') {
            Toast({
              message: '添加成功',
              iconClass: 'icon icon-success',
              duration: 1000

            });
            self.$router.push('/addr');
          } else {
            Toast({
              message: '添加失败 网络异常',
              iconClass: 'icon icon-error',
              duration: 1000

            });
          }
          }
        })


      }


    },
    mounted() {
      this.$nextTick(() => { //vue里面全部加载好了再执行的函数  （类似于setTimeout）
        this.myAddressSlots[0].defaultIndex = 0
        // 这里的值需要和 data里面 defaultIndex 的值不一样才能够初始化
        //因为我没有看过源码（我猜测是因为数据没有改变，不会触发更新）
      });
    }
  }


</script>

