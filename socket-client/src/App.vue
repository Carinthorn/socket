<template>
  <v-app>
    <v-main class="main">
      <chat-vue class="mt-12" :msg="message" />
    </v-main>
  </v-app>
</template>

<script>
import ChatVue from './components/Chat.vue';
export default {
  name: 'App',

  components: {
    ChatVue,
  },

  data: () => ({
    message: "hello from pete"
  }),
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
