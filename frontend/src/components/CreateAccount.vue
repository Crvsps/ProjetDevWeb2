<script lang="ts">
import { ref } from 'vue'
import { getCSRFToken } from '../store/auth'
import router from '../router/index'

export default {
  setup() {
    // Définir toutes les données nécessaires avec `ref()`
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const confirmPassword = ref('')
    const error = ref('')
    const success = ref('')

    // Fonction de création du compte
    const register = async () => {

      if (password.value !== confirmPassword.value) {
        error.value = "Les mots de passe ne correspondent pas."
        return
      }

      try {
        console.log('Envoi de la requête d\'inscription...');
        const response = await fetch('http://localhost:8000/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
          },
          body: JSON.stringify({
            username: username.value,
            email: email.value,
            password: password.value
          }),
          credentials: 'include'
        })

      const textResponse = await response.text();

      try {
        const data = JSON.parse(textResponse);

      if (response.ok) {
        success.value = 'Inscription réussie! Veuillez vous connecter.'
        setTimeout(() => {
          router.push('/login')
        }, 1000)
      } else {
        error.value = data.error || 'Echec de l\'inscription'
      }
      } catch (err) {
        error.value = 'La réponse de l\'API n\'est pas au format attendu.'
      }
    
      } catch (err) {
        error.value = 'Une erreur est survenue lors de l\'inscription : ' + err
      }
    }
    // Retourne les variables et la fonction d'enregistrement
    return {
      username,
      email,
      password,
      confirmPassword,
      error,
      success,
      register
    }
  }
}
</script>


<template>
  <div class="create-account">
    <form @submit.prevent="register" class="account-form">
      <h2>Créer un compte</h2>

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
        <label for="email">Email</label>
        <input 
          id="email"
          type="email"
          v-model="email"
          required
          placeholder="Entrez votre email"
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

      <div class="form-group">
        <label for="confirmPassword">Confirmer le mot de passe</label>
        <input 
          id="confirmPassword"
          type="password"
          v-model="confirmPassword"
          required
          placeholder="Confirmez votre mot de passe"
        >
      </div>

      <p v-if="error" class="error-message">{{ error }}</p>
      <p v-if="success" class="success-message">{{ success }}</p>

      <button type="submit" class="btn-submit">Créer mon compte</button>
    </form>
  </div>
</template>

<style scoped>
.create-account {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f8fafc;
  padding: 20px;
}

.account-form {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  width: 100%;
  max-width: 400px;
}

h2 {
  color: #1e293b;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.875rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #475569;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

.btn-submit {
  width: 100%;
  padding: 0.75rem;
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

.error-message {
  color: #dc2626;
  background: #fee2e2;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
}

.success-message {
  color: #16a34a;
  background: #d1fae5;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  text-align: center;
}
</style>
