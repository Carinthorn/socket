<template>
  <b-container fluid>
      <LoginModal msg="Welcome to Your Vue.js App" />
  </b-container>
</template>

<script>
import LoginModal from "./components/Login.vue";

export default {
  name: "App",
  components: {
    LoginModal,
  },
};
</script>

<style>
 b-container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url("./assets/background.jpg");
}
</style>
