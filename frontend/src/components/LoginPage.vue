<template>
  <div class="login">
    <h2>Connexion</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Nom d'utilisateur</label>
        <input
          type="text"
          id="username"
          v-model="user.username"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Mot de passe</label>
        <input
          type="password"
          id="password"
          v-model="user.password"
          required
        />
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="loading">
          <span v-if="loading">Chargement...</span>
          <span v-else>Se connecter</span>
        </button>
      </div>
      <div v-if="message" class="alert alert-danger">
        {{ message }}
      </div>
    </form>
  </div>
</template>

<script>
import UserService from '../services/user.service';

export default {
  name: 'LoginPage',
  data() {
    return {
      user: {
        username: '',
        password: ''
      },
      loading: false,
      message: ''
    };
  },
  methods: {
    handleLogin() {
      this.message = '';
      this.loading = true;
      
      UserService.login(this.user)
        .then(() => {
          this.$router.push('/recherche-objet');
        })
        .catch(error => {
          this.message = error.response?.data?.non_field_errors || 'Erreur de connexion, vérifiez vos identifiants';
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>