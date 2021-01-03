<template>
  <div class="login">
    <h1 class="title">INICIO DE SESIÓN</h1>
    <form action class="form" @submit.prevent="login">
      <label class="form-label" for="#username">username:</label>
      <input
        v-model="username"
        class="form-input"
        type="text"
        id="username"
        required
        placeholder="username"
      >
      <label class="form-label" for="#password">Password:</label>
      <input
        v-model="password"
        class="form-input"
        type="password"
        id="password"
        placeholder="Password"
      >
     
      <input class="form-submit" type="submit" value="Login">
    </form>
    <p class="msg">¿No tienes cuenta?
      <router-link to="/register">Regístrate</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios';
import { loginUser } from "@/logic/auth"


export default {
    name: 'login',
    data() {
        return {
            username: '',
            password: ''
        }
    },
  methods: {
    async login() {
      try {
    await loginUser(this.username, this.password)
    this.$router.push('/')
      }
      catch (err) {
          alert(`Error: ${err}`)
      }
    }
  }
  }
</script>

<style lang="scss" scoped>
.login {
  padding: 2rem;
}
.title {
  text-align: center;
}
.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 20%;
  min-width: 350px;
  max-width: 100%;
  background: rgba(19, 35, 47, 0.9);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: white;
  margin-bottom: 0.5rem;
  &:first-of-type {
    margin-top: 0rem;
  }
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: white;
  &:focus {
    outline: 0;
    border-color: #1ab188;
  }
}
.form-submit {
  background: #1ab188;
  border: none;
  color: white;
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
  &:hover {
    background: #0b9185;
  }
}
.error {
  margin: 1rem 0 0;
  color: #ff4a96;
}
.msg {
  margin-top: 3rem;
  text-align: center;
}
</style>