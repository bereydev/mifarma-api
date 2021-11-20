<template>
  <div class="content">
    <div class="presentation">
      <h1>MiFarmacia</h1>
      <p>
        MiFamacia is an online pick and collect platform to order your drugs you
        can register online or if you're on a smartphone you can simply download
        it on the Play Store or the App Store
      </p>
      <div class="appDown">
        <img
          id="appPic"
          src="https://images.unsplash.com/photo-1621768216002-5ac171876625?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxNDU4OXwwfDF8cmFuZG9tfHx8fHx8fHx8MTYzNDU5MjkxMw&ixlib=rb-1.2.1&q=85"
          alt="appStore"
        />
        <img
          id="appPic"
          src="https://images.unsplash.com/photo-1607252650355-f7fd0460ccdb?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxNDU4OXwwfDF8cmFuZG9tfHx8fHx8fHx8MTYzNDU5Mjk4Nw&ixlib=rb-1.2.1&q=85"
          alt="PlayStore"
        />
      </div>
    </div>

    <login-form-vue class="login"></login-form-vue>
  </div>
</template>

<script>
import LoginFormVue from "@/components/LoginForm.vue";

export default {
  components: {
    LoginFormVue,
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/colors.scss";
@import "@/assets/styles/fonts.scss";

.content {
  display: flex;
  padding: 1em 2em 0em 1em;
  flex-direction: row;
  gap: 10em;
}

.presentation {
  flex: 1.5 1;
  box-sizing: border-box;
  height: 3em;
  background: white;
  display: flex;
  flex-direction: column;
  grid-row-gap: 1em;
}

#appPic {
  width: 7.5em;
  height: auto;
  align-self: center;
  justify-self: center;
  border: 2px solid black;
}

.appDown {
  grid-area: appDown;
  display: flex;
  justify-content: start;
  grid-gap: 3em;
  width: 60%;
}

.login {
  width: 40%;
  padding: 1em;
  background-color: #e8e1dd;
  border-radius: 25px;
  gap: 0.25em;
}
</style>
