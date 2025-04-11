<script setup lang="ts">
import { ref } from 'vue'
import { useAuth } from '@/store/useAuth'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

const { loginUser } = useAuth()

const handleSubmit = async () => {
  try {
    // Appel de la méthode loginUser du store
    await loginUser(username.value, password.value)
    router.push('/dashboard') // Redirection vers la page du dashboard
  } catch (error) {
    console.error('Erreur lors de la connexion:', error)
    alert('Erreur de connexion, veuillez vérifier vos identifiants')
  }
}
</script>

<!-- 
<template>
  <div class="create-account">
    <form @submit.prevent="handleSubmit" class="account-form">
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
</style> -->

<template>
  <div class="login-container">
    <div class="login">
      <form @submit.prevent="handleSubmit" class="account-form">
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