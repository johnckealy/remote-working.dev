<template>
  <div class="container">
    <q-card class="q-pa-lg">
      <q-toolbar class="q-pb-lg">
        <q-avatar>
          <img src="~assets/logo.svg" />
        </q-avatar>

        <q-toolbar-title class="q-mx-sm"> Login </q-toolbar-title>

        <q-btn
          flat
          round
          dense
        />
      </q-toolbar>
      <q-form @submit="onSubmit" class="q-gutter-md">
        <q-input
          v-model="username"
          label="Email"
          lazy-rules="ondemand"
          :rules="[
            (val) => (val && val.length > 0) || 'Please provide your email',
          ]"
          outlined
        />

        <q-input
          v-model="password"
          label="Password"
          type="password"
          lazy-rules="ondemand"
          :rules="[
            (val) => (val && val.length > 0) || 'Please provide your password',
          ]"
          outlined
        />

        <div class="text-body1 text-red" v-if="loginErrorMessage">
          There was a problem logging you in. Please check your details.
        </div>

        <span class="text-body2 q-pa-md q-ma-md" >Don't have an account? Register <a href="/register">here.</a> </span>

        <div>
          <q-btn
            no-caps
            glossy
            class="q-ml-md full-width q-mx-auto"
            label="Submit"
            type="submit"
            color="primary"
          />
        </div>
      </q-form>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
      password: null,
      loginErrorMessage: false,
    };
  },
  methods: {
    async onSubmit() {
      const loginOk = await this.$auth.login({
        username: this.username,
        password: this.password
      })
      if (loginOk) {
        this.$q.notify({ message: "Login was successful" });
        this.$route.path == this.$store.state.authenticator.redirectUrl
          ? this.$router.go()
          : this.$router.push(this.$store.state.authenticator.redirectUrl);
      } else {
        this.$q.notify({
          message: "Login was not successful!",
          color: "red-6",
          icon: "error",
        });
        this.loginErrorMessage = true;
      }
    },
  },
};
</script>