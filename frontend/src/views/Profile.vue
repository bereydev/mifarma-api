<template>
  <div class="profil">
    <h1>This is the profile page</h1>
    <h3 v-if="user">Hi {{ user.first_name }} {{ user.last_name }}</h3>
  </div>
</template>

<script>
export default {
  name: "Profile",
};
</script>
