import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from './util/axiosConf.js';
import mitt from 'mitt';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faCirclePlay,faCirclePause } from '@fortawesome/free-regular-svg-icons'

library.add(faCirclePlay,faCirclePause)
let vue = createApp(App);
vue.component('font-awesome-icon', FontAwesomeIcon)
vue.use(router)
vue.config.globalProperties.axios = axios;
vue.config.globalProperties.eventBus = mitt();

const vm = vue.mount('#app')
