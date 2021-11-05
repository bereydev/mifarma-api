<template>
  <div class="dashboard">
    This is the welcome page for the pros
    <router-link class="navBarElement" to="/pro/register"
      >Register a pharmacy</router-link
    >
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  components: {},
})
export default class Dashboard extends Vue {}
</script>
