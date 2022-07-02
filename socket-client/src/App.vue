<template>
  <v-app>
    <v-main class="main">
      <chat-vue v-if="userConnected" class="mt-12" />
    </v-main>
  </v-app>
</template>

<script>
const io = require('socket.io-client');
import ChatVue from './components/Chat.vue';
export default {
  name: 'App',

  components: {
    ChatVue,
  },

  data: () => ({
    message: [],
    socket: io('ws://localhost:2345',{
      transports: ['websocket']
    }),
    userConnected: true
  }),
  mounted(){
    this.socket.on('MESSAGE', (socket) => {
      this.message = socket
      console.log(socket)
    })
  }
};
</script>

<style>
.main{
  background-image: url(./assets/background.jpg);
  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

</style>
