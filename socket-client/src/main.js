import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'


Vue.config.productionTip = false

Vue.use(axios)

import vuetify from './plugins/vuetify'
new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')


