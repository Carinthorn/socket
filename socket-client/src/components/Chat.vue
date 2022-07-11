<template>
  <v-container>
    <v-row no-gutters>
      <v-col
        class="sidebar m-1"
        color="#191D27"
        style="overflow-y: auto; height: 100%; position: relative"
      >
        <v-card
          class="mx-auto mt-1"
          color="#292F3F"
          dark
          @click="dialog = true"
        >
          <v-card-actions>
            <v-list-item class="grow">
              <v-list-item-content>
                <center>
                  <v-list-item-title>+ Add room {{ msg }}</v-list-item-title>
                </center>
              </v-list-item-content>
              <v-dialog v-model="dialog" width="500">
                <v-card>
                  <v-card-title class="text-h5 grey lighten-2">
                    Create New Room
                  </v-card-title>

                  <v-card-text>
                    <v-text-field
                      label="Room Id"
                      v-model="newRoomId"
                      hide-details="auto"
                    ></v-text-field>

                    <v-text-field
                      label="Room name"
                      v-model="newRoomName"
                      hide-details="auto"
                    ></v-text-field>
                  </v-card-text>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="dialog = false">
                      create
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
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
                <v-list-item-title>Rooms : {{ item }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col
        cols="9"
        class="ml-1"
        style="overflow-y: auto; height: 100%; position: relative"
      >
        <v-card class="mx-auto mt-1" color="#292F3F" dark style="position: sticky;top: 0;z-index:100;">
          <v-card-actions>
            <v-list-item class="grow">
              <v-list-item-title
                ><v-btn>delete messages</v-btn> Room Id : {{ roomId }}
              </v-list-item-title>
            </v-list-item>
          </v-card-actions>
        </v-card>

        <v-card
          :key="item.index"
          v-for="item in messages"
          class="pa-2 ma-2 white--text"
          color="#191d27"
        >
          <p>{{ item.user }} : {{ item.message }}</p>
        </v-card>
        <v-card color="#292F3F" dark style="position: sticky; bottom: 0" class="sticky">
          <v-card-actions>
            <v-list-item class="grow">
              <v-card-subtitle>
                <v-text-field
                  label="Name"
                  v-model="username"
                  hide-details="auto"
                ></v-text-field>
              </v-card-subtitle>
              <v-text-field
                label="Send chat"
                v-model="userMessage"
                hide-details="auto"
              ></v-text-field>
              <v-btn elevation="2" @click="sendMessage()">send</v-btn>
            </v-list-item>
          </v-card-actions>
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
    rooms: [12345, 456, 789, 123],
    roomId: "",
    alert: false,
    messages: [],
    userMessage: "",
    username: "",
    roomName: "",
    dialog: false,
    newRoomId: "",
    newRoomName:""
  }),

  methods: {
    viewMessages(id) {
      axios
        .post("http://localhost:2345/getMessage", {
          roomId: id,
        })
        .then((res) => {
          console.log(res);
          this.messages = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      this.roomId = id;
      console.log(this.messages);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.sticky{
  position: -webkit-sticky;
  position: sticky;
  bottom: 0;
}
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
