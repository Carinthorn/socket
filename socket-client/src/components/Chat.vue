<template>
  <v-container>
    <v-alert :value="alert" border="top" color="red lighten-2" dark>
      ฝากน้องธัญเพิ่มห้องให้หน่อยนะะ
    </v-alert>
    <v-row no-gutters>
      <v-col class="sidebar m-1" color="#191D27">
        <v-card class="mx-auto mt-1" color="#292F3F" dark @click="addRoom()">
          <v-card-actions>
            <v-list-item class="grow">
              <v-list-item-content>
                <v-list-item-title>+ Add more friends</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-card-actions>
        </v-card>
        <v-card
          v-for="item in rooms"
          :key="item.index"
          @click="viewMessages(item)"
          class="mx-auto mt-1"
          color="#292F3F"
          dark
        >
          <v-card-actions>
            <v-list-item class="grow">
              <v-list-item-avatar color="grey darken-3">
                <v-img
                  class="elevation-6"
                  alt=""
                  src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>Rooms : {{item}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="9" class="ml-1">
        <v-app-bar elevation="4" color="#292F3F" class="pa-2 white--text">Chats room </v-app-bar>
        <v-card :key="item.index" v-for="item in messages"  class="pa-2 ma-2 white--text" color="#191d27">
          <p>{{item.user}} : {{item.message}}</p>
        </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "ChatVue",
  props: {
    msg: String,
  },
  data: () => ({
    rooms: [12345, 456, 789],
    alert: false,
    messages: null,
  }),

  methods: {
    addRoom() {
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
      }, 5000);
    },
    viewMessages(roomId) {
      axios
        .get("http://localhost:5050/get/" + roomId)
        .then((response) => {
          this.messages = response.data;
          console.log(response.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.topbar {
  margin: 5px;
  height: 50px;
  max-height: 10%;
}
.row {
  height: 100%;
  background-color: black;
}
.col {
  background-color: #191d27;
}
.container {
  padding: 0;
  height: 640px;
  max-height: 640px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
