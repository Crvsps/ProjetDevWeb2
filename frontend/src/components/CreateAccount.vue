<template>
  <div class="register">
    <h2>Inscription</h2>
    <form @submit.prevent="handleRegister">
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
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          v-model="user.email"
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
        <label for="password2">Confirmer le mot de passe</label>
        <input
          type="password"
          id="password2"
          v-model="user.password2"
          required
        />
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="loading">
          <span v-if="loading">Chargement...</span>
          <span v-else>S'inscrire</span>
        </button>
      </div>
      <div v-if="message" class="alert" :class="successful ? 'alert-success' : 'alert-danger'">
        {{ message }}
      </div>
    </form>
  </div>
</template>

<script>
import UserService from '../services/user.service';

export default {
  name: 'CreateAccount',
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
        password2: '',  
      },
      loading: false,
      message: '',
      successful: false
    };
  },
  methods: {
    handleRegister() {
      this.message = '';
      this.loading = true;

      UserService.register(this.user)
        .then(response => {
          this.message = 'Inscription réussie!';
          this.successful = true;
          this.$router.push('/login');
        })
        .catch(error => {
          this.message = error.response?.data?.username || 
                         error.response?.data?.email || 
                         error.response?.data?.password ||
                         'Une erreur s\'est produite!';
          this.successful = false;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
