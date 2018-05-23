<template>
  <div class="app-init scroll-box mine-page ">
    <mt-header title="订单管理">
      <router-link to="/" slot="left">
        <mt-button icon="back">返回</mt-button>
      </router-link>
    </mt-header>
    <mt-navbar v-model="selected">
      <mt-tab-item :id="1">待发货</mt-tab-item>
      <mt-tab-item :id="2">待收货</mt-tab-item>
      <mt-tab-item :id="3">已完成</mt-tab-item>

    </mt-navbar>
    <!-- tab-container -->
    <mt-tab-container v-model="selected">
      <mt-tab-container-item :id="1">
        <mt-cell v-for="order1 in orderlist1" :title='"订单号:"+order1.order_number'
                 :label='order1.goodsname+" X"+order1.goodnum+" 金额: "+(order1.pay_price)/100+" 元"'>
          <mt-button type="primary" size="small" plain @click.native="remind">提醒发货</mt-button>

        </mt-cell>

      </mt-tab-container-item>
      <mt-tab-container-item :id="2">
        <mt-cell v-for="order2 in orderlist2" :title='"快递单号:"+order2.ship_number'
                 :label='order2.goodsname+" X"+order2.goodnum+" 金额: "+(order2.pay_price)/100+" 元"'>
          <mt-button type="primary" size="small" plain @click.native="receipt(order2.order_number)">确认收货</mt-button>
        </mt-cell>
        <a href="http://kuaidi100.com">
          <mt-button type="primary" plain size="large">物流进度查询</mt-button>
        </a>


      </mt-tab-container-item>
      <mt-tab-container-item :id="3">
        <mt-cell v-for="order3 in orderlist3" :title='"快递单号:"+order3.ship_number'
                 :label='order3.goodsname+" X"+order3.goodnum+" 金额: "+(order3.pay_price)/100+" 元"'>
          <span>{{order3.update_time | formatDate}}</span>

        </mt-cell>
        <mt-button type="default" plain size="large" disabled>售后服务咨询（加qq:2907023643）</mt-button>

      </mt-tab-container-item>
    </mt-tab-container>


  </div>
</template>
<script>
  import {Toast} from 'mint-ui';
  import {formatDate} from '../../utils'
  import {MessageBox} from 'mint-ui';

  export default {
    filters: {
      formatDate(time) {
        var date = new Date(time);
        return formatDate(date, 'yyyy-MM-dd hh:mm');
      }
    },
    data() {
      return {
        orderlist1: [],
        orderlist2: [],
        orderlist3: [],
        kongge: ' ',
        selected: 1
      }
    },
    created() {
      this.getdata1()
      this.getdata2()
      this.getdata3()
    },
    methods: {


      receipt(order_number) {

        MessageBox.confirm('确认执行此操作?').then(
          action => {
            let self = this;
            self.url = 'http://api.yourserver.com/receiptorder';
            self.$axios.get(self.url, {
              params: {
                openid: localStorage.getItem('wx_openid'),
                ordernumber: order_number
              }
            }).then((res) => {
              //获取数据成功
              if (res.data === 'success') {
                this.getdata1()
                this.getdata2()
                this.getdata3()

                Toast({
                  message: '确认收货成功',
                  iconClass: 'icon icon-success',
                  duration: 2000
                });

              } else {
                Toast({
                  message: '确认收货失败',
                  iconClass: 'icon icon-success',
                  duration: 1000
                });
              }
            })
          },
          action => {
          }
        );


      },

      remind() {
        MessageBox.confirm('确认执行此操作?').then(
          action => {
            Toast({
              message: '提醒发货成功',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          },
          action => {
          }
        );

      },
      getdata1() {
        let self = this;
        self.url = 'http://api.yourserver.com/getorders';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid'),
            type: 1
          }
        }).then((res) => {
          //获取数据成功
          if (res.data.msg === 'success') {
            self.orderlist1 = res.data.list
          } else {
            Toast({
              message: '订单信息获取失败',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          }
        })
      },
      getdata2() {   //获取微信用户地址数据
        let self = this;
        self.url = 'http://api.yourserver.com/getorders';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid'),
            type: 2
          }
        }).then((res) => {
          //获取数据成功
          if (res.data.msg === 'success') {
            self.orderlist2 = res.data.list

          } else {
            Toast({
              message: '订单信息获取失败',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          }
        })
      },
      getdata3() {   //获取微信用户地址数据
        let self = this;
        self.url = 'http://api.yourserver.com/getorders';
        self.$axios.get(self.url, {
          params: {
            openid: localStorage.getItem('wx_openid'),
            type: 3
          }
        }).then((res) => {
          //获取数据成功
          if (res.data.msg === 'success') {
            self.orderlist3 = res.data.list
          } else {
            Toast({
              message: '订单信息获取失败',
              iconClass: 'icon icon-success',
              duration: 1000
            });
          }
        })
      }
    }
  }

</script>

