

<script lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const error = ref('')
    const router = useRouter()
    const authStore = useAuthStore()

    const login = async () => {
  try {
    error.value = ''
    await authStore.login(username.value, password.value, router)

    if (!authStore.isAuthenticated) {
      error.value = 'Identifiants incorrects. Veuillez réessayer.'
    }
  } catch (err) {
    console.error('Erreur lors de la tentative de connexion :', err)
    error.value = 'Une erreur est survenue. Veuillez réessayer plus tard.'
  }
}
    const resetError = () => {
      error.value = ''
    }

    return {
      username,
      password,
      error,
      login,
      resetError,
    }
  }
}
</script>


<template>
  <div class="login-container">
    <div class="login">
      <form @submit.prevent="login">
        <h2>Connexion</h2>
        
        <div class="form-group">
          <label for="username">Nom d'utilisateur</label>
          <input 
            id="username"
            type="text"
            v-model="username"
            required
            placeholder="Entrez votre nom d'utilisateur"
          >
        </div>

        <div class="form-group">
          <label for="password">Mot de passe</label>
          <input 
            id="password"
            type="password"
            v-model="password"
            required
            placeholder="Entrez votre mot de passe"
          >
        </div>

        <button type="submit" class="btn-submit">Se connecter</button>
      </form>
    </div>
  </div>
</template>


<style scoped>
.login-container {
  width: 100%;
  min-height: 100vh;
  padding-top: 80px; /* Adjusted for navbar */
  background: #f8fafc;
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
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

h2 {
  color: #1e293b;
  text-align: center;
  margin-bottom: 2.5rem;
  font-size: 1.875rem;
  font-weight: 600;
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
  color: black;
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #f8fafc;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  background: white;
}

input::placeholder {
  color: #94a3b8;
}

.btn-submit {
  width: 100%;
  padding: 0.875rem;
  margin-top: 1rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-submit:active {
  transform: translateY(0);
}

@media (max-width: 640px) {
  .create-account {
    padding: 1rem;
  }
  
  .account-form {
    padding: 1.5rem;
  }
}
</style>