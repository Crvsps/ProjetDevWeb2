<script>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()

    const showLogoutModal = ref(false)

    const confirmLogout = async () => {
      try {
        await authStore.logout(router)
        showLogoutModal.value = false
      } catch (error) {
        console.error(error)
      }
    }

    const cancelLogout = () => {
      showLogoutModal.value = false
    }

    const openLogoutModal = () => {
      showLogoutModal.value = true
    }

    onMounted(async () => {
      await authStore.fetchUser()
    })

    return {
      authStore,
      router,
      openLogoutModal,
      confirmLogout,
      cancelLogout,
      showLogoutModal
    }
  }
}
</script>


<template>
  <nav class="navbar">
    <ul class="nav-links">
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/recherche-objet">Objets</router-link></li>
      <li><router-link to="/ajouter-objet">Ajouter un objet</router-link></li>
    </ul>

    <div class="navbar-start">
      <div v-if="authStore.isAuthenticated" class="navbar-item">
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

    <!-- Connexion / Déconnexion -->
    <div class="nav-buttons">
      <template v-if="!authStore.isAuthenticated">
        <router-link to="/create-account" class="btn btn-signup">Créer un compte</router-link>
        <router-link to="/login">Se connecter</router-link>
      </template>

      <template v-else>
        <button class="btn btn-logout" @click="openLogoutModal">Se déconnecter</button>

      </template>
    </div>
  </nav>

  <!-- Modal de confirmation -->
<div class="logout-modal-overlay" v-if="showLogoutModal">
  <div class="logout-modal">
    <h3>Confirmation</h3>
    <p>Êtes-vous sûr de vouloir vous déconnecter ?</p>
    <div class="logout-modal-buttons">
      <button class="cancel-btn" @click="cancelLogout">Annuler</button>
      <button class="confirm-btn" @click="confirmLogout">Confirmer</button>
    </div>
  </div>
</div>
</template>


<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  list-style-type: none;
  gap: 15px;
}

.nav-buttons {
  display: flex;
  gap: 10px;
}

.logout-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.logout-modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.logout-modal-buttons button {
  margin: 5px;
}






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
  gap: 2.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
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
  gap: 1.2rem;
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
.logout-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 300;
}

.logout-modal {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  animation: modal-appear 0.3s ease-out;
}

@keyframes modal-appear {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.logout-modal h3 {
  margin-top: 0;
  color: #333;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.75rem;
}

.logout-modal p {
  margin-bottom: 1.5rem;
  color: #666;
}

.logout-modal-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.cancel-btn, .confirm-btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.cancel-btn {
  background-color: #e0e0e0;
  color: #333;
}

.cancel-btn:hover {
  background-color: #d0d0d0;
}

.confirm-btn {
  background-color: #ef4444;
  color: white;
}

.confirm-btn:hover {
  background-color: #dc2626;
}
</style>