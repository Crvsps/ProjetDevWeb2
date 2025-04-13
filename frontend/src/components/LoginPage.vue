<template>
  <div class="login-container">
    <div class="login">
      <form @submit.prevent="handleLogin" class="account-form">
        <h2>Connexion</h2>

        <div class="form-group">
          <label for="username">Nom d'utilisateur</label>
          <input
            type="text"
            id="username"
            v-model="user.username"
            required
            placeholder="Entrez votre nom d'utilisateur"
          />
        </div>

        <div class="form-group">
          <label for="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            v-model="user.password"
            required
            placeholder="Entrez votre mot de passe"
          />
        </div>

        <button type="submit" class="btn-submit" :disabled="loading">
          <span v-if="loading">Chargement...</span>
          <span v-else>Se connecter</span>
        </button>

        <div v-if="message" class="alert alert-danger" style="margin-top: 1rem; color: red;">
          {{ message }}
        </div>
      </form>
    </div>
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
          this.$router.push('/profil');
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

<style scoped>
.login-container {
  width: 100%;
  min-height: 100vh;
  padding-top: 80px;
}

.login {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
}

.account-form {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 
              0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

h2 {
  font-size: 2.5rem;
  color: #2563eb;
  margin-bottom: 2rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #475569;
  font-weight: 500;
  font-size: 0.95rem;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  outline: none;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.btn {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.alert {
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}

.alert-danger {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

@media (max-width: 480px) {
  .login {
    margin: 1rem;
    padding: 1.5rem;
  }
}
</style>
