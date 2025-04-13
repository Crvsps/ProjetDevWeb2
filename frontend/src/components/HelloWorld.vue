<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <nav class="navbar">
    <ul class="nav-links">
      <li><router-link to="/">
        <span class="cyber-school-link">CYber School</span>
      </router-link></li>
      <!-- <li><router-link to="/">Accueil</router-link></li> -->
      <li><router-link to="/actualites">Actualités</router-link></li>
      <li v-if="isLoggedIn"><router-link to="/recherche-objet">Objets</router-link></li>
      <li v-if="isLoggedIn"><router-link to="/ajouter-objet">Ajouter un objet</router-link></li>
      <!-- <li v-if="!isLoggedIn"><router-link to="/">Informations</router-link></li> -->
      <li v-if="!isLoggedIn"><router-link to="/AideSchool">Aide</router-link></li>
    </ul>

    <div class="navbar-start">
      <div v-if="isLoggedIn" class="navbar-item">
        <form method="get" action="/search">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" placeholder="Vous cherchez un objet?" name="query">
            </div>
            <div class="control">
              <button class="button is-success">
                <span class="icon">
                <i class="fas fa-search"></i>
                </span>
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="nav-buttons">
      <template v-if="!isLoggedIn">
        <router-link :to="{name: 'register'}" class="btn btn-signup">Créer un compte</router-link>
        <router-link :to="{name: 'login'}" class="btn btn-login">Se connecter</router-link>
      </template>
      <div v-else>
        <router-link :to="{name: 'profil'}" class="btn btn-login">Profil</router-link>
        <button @click="logout" class="btn btn-signup btn-logout">Se déconnecter</button>
        <router-link to="/profile" class="btn btn-signup">Aller au profil</router-link>
        <button @click="logout" class="btn btn-login">Se déconnecter</button>
      </div>
      
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { Router } from 'vue-router'

interface ComponentData {
  isLoggedIn: boolean;
}

export default defineComponent({
  name: 'HelloWorld',
  
  data(): ComponentData {
    return {
      isLoggedIn: false
    }
  },

  created() {
    this.isLoggedIn = !!localStorage.getItem('token')
    window.addEventListener('storage', this.checkLoginStatus)
  },

  beforeUnmount() {
    window.removeEventListener('storage', this.checkLoginStatus)
  },

  methods: {
    checkLoginStatus(): void {
      this.isLoggedIn = !!localStorage.getItem('token')
    },
    logout() {
      const confirmation = window.confirm("Voulez-vous vraiment vous déconnecter ?");
      if (confirmation) {
        localStorage.removeItem('token');
        this.isLoggedIn = false;
        this.$router.push('/login');
      }
    }
  }
})
</script> 

<style scoped>
.navbar {
position: fixed;
top: 0;
left: 0;
right: 0;
height: 70px;
background: rgba(255, 255, 255, 0.98);
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
display: flex;
align-items: center;
justify-content: space-between;
padding: 0 2.5rem;
z-index: 1000;
backdrop-filter: blur(8px);
}

.nav-links {
  display: flex;
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
  align-items: center;
}



.nav-links a {
text-decoration: none;
color: #4b5563;
font-weight: 500;
padding: 0.7rem 1.2rem;
border-radius: 8px;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
position: relative;
overflow: hidden;
}

.nav-links a:hover {
color: #3b82f6;
background: rgba(59, 130, 246, 0.08);
}

.nav-links a.router-link-active {
color: #3b82f6;
font-weight: 600;
}

.nav-links a::after {
content: '';
position: absolute;
bottom: 0;
left: 50%;
width: 0;
height: 2px;
background: #3b82f6;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transform: translateX(-50%);
}

.nav-links a:hover::after,
.nav-links a.router-link-active::after {
width: 60%;
box-shadow: 0 0 8px rgba(59, 130, 246, 0.4);
}

.navbar-start {
flex-grow: 1;
display: flex;
justify-content: center;
padding: 0 2rem;
}

.navbar-item {
display: flex;
align-items: center;
}

.field.has-addons {
display: flex;
align-items: stretch;
}

.control {
position: relative;
display: flex;
}

.input {
height: 40px;
border-radius: 20px 0 0 20px;
border: 1px solid #e5e7eb;
padding: 0 1.2rem;
width: 260px;
font-size: 0.9rem;
transition: all 0.3s ease;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.input:focus {
outline: none;
border-color: #3b82f6;
box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);
}

.button {
height: 40px;
border-radius: 0 20px 20px 0;
background: #10b981;
border: none;
color: white;
padding: 0 1.2rem;
cursor: pointer;
transition: all 0.3s ease;
display: flex;
align-items: center;
justify-content: center;
margin: 0 0.5rem;
}

.button .icon {
display: flex;
align-items: center;
justify-content: center;
}

.button:hover {
background: #059669;
box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
}

.nav-buttons {
display: flex;
gap: 1rem;
}

.nav-buttons >div{
display: flex;
gap: 1rem;
}

.btn {
padding: 0.8rem 1.6rem;
font-size: 0.9rem;
font-weight: 600;
border-radius: 8px;
cursor: pointer;
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
text-transform: uppercase;
letter-spacing: 0.5px;
text-decoration: none;
display: inline-flex;
align-items: center;
justify-content: center;
}

.btn-signup {
background: transparent;
border: 2px solid #3b82f6;
color: #3b82f6;
}

.btn-signup:hover {
background: rgba(59, 130, 246, 0.08);
color: #2563eb;
transform: translateY(-2px);
box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
}

.btn-login {
background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
border: none;
color: white;
box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.btn-login:hover {
transform: translateY(-2px);
box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);
background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
}

.btn-logout:hover {
  background: rgba(239, 68, 68, 0.08) !important;
  color: #ef4444 !important;
  border-color: #ef4444 !important;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.15) !important;
}

.btn:active {
transform: translateY(1px);
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Pour assurer que l'espace est réservé pour la barre de navigation fixe */
body {
padding-top: 70px;
}

/* Media queries pour la responsive */
@media (max-width: 992px) {
.navbar {
padding: 0 1.5rem;
}

.nav-links {
gap: 1.5rem;
}

.input {
width: 200px;
}
}

@media (max-width: 768px) {
.navbar {
height: auto;
flex-direction: column;
padding: 1rem;
}

.nav-links, .navbar-start, .nav-buttons {
width: 100%;
margin: 0.5rem 0;
justify-content: center;
}

.nav-links {
order: 1;
}

.navbar-start {
order: 2;
}

.nav-buttons {
order: 3;
}

body {
padding-top: 150px;
}
}

.cyber-school-link {
  background: linear-gradient(45deg, #ae00ff, #00b7ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: bold;
  font-size: 1.5em;  /* Increased from 1.2em */
  text-shadow: 2px 2px 4px rgba(0, 255, 136, 0.2);
  padding: 0.6em;    /* Slightly increased padding */
  cursor: default;
  transition: all 0.3s ease;
}

.cyber-school-link:hover {
  transform: scale(1.05);
  text-shadow: 3px 3px 6px rgba(0, 166, 255, 0.3);
}
</style>