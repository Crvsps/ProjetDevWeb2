<template>
  <div class="dashboard-container">
    <!-- Overlay -->
    <div 
      class="overlay" 
      :class="{ 'overlay-active': isSidebarOpen }"
      @click="toggleSidebar"
    ></div>
    <!-- Sidebar -->
    <div class="sidebar" :class="{ 'sidebar-active': isSidebarOpen }">
      <div class="sidebar-header">
        <h3>Menu</h3>
        <button class="close-btn" @click="toggleSidebar"></button>
      </div>
      <ul class="sidebar-menu">
        <li><router-link to="/dashboard-advanced">Tableau de bord</router-link></li>
        <li><router-link to="/settings">Paramètres</router-link></li>
        <li><router-link to="/help">Aide</router-link></li>
				<li><router-link to="/objects-advanced">Objets</router-link></li>
				<li><router-link to="/services">Services</router-link></li>
				<li><router-link to="/resources">Ressources</router-link></li>
				<li><router-link to="/static-reports">Rapports statiques</router-link></li>
      </ul>
    </div>

    <!-- Navbar -->
    <nav class="navbar">
    <div class="nav-left">
      <button class="burger-btn" @click="toggleSidebar">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <div class="nav-links">
        <router-link to="/profil">Profil</router-link>
      </div>
    </div>
    <div class="nav-right">
      <div class="nav-links">
        <router-link to="/login">Se déconnecter</router-link>
      </div>
    </div>
  </nav>

    <!-- Content -->
    <div class="content" :class="{ 'content-shifted': isSidebarOpen }">
      <!-- Your dashboard content here -->
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'DashboardAdvanced',
  data() {
    return {
      isSidebarOpen: false
    }
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen
    }
  }
}
</script>

<style scoped>
.dashboard-container {
  min-height: 100vh;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1rem;
  z-index: 100;
}

.nav-left, .nav-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.burger-menu {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 21px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.burger-menu span {
  width: 100%;
  height: 3px;
  background-color: #333;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.profile-btn, .logout-btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
}

.profile-btn {
  background-color: #e0e0e0;
  color: #333;
}

.logout-btn {
  background-color: #ff4444;
  color: white;
}

.sidebar {
  position: fixed;
  top: 0;
  left: -250px;
  width: 250px;
  height: 100vh;
  background: white;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  transition: left 0.3s ease;
  z-index: 200;
}

.sidebar-active {
  left: 0;
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.sidebar-menu {
  list-style: none;
  padding: 1rem;
}

.sidebar-menu li {
  margin-bottom: 1rem;
}

.sidebar-menu a {
  color: #333;
  text-decoration: none;
  display: block;
  padding: 0.5rem;
  border-radius: 4px;
}

.sidebar-menu a:hover {
  background-color: #f5f5f5;
}

.content {
  padding-top: 60px;
  transition: margin-left 0.3s ease;
}

.content-shifted {
  margin-left: 250px;
}

@media (max-width: 768px) {
  .content-shifted {
    margin-left: 0;
  }
  
  .sidebar {
    width: 100%;
    left: -100%;
  }
  
  .sidebar-active {
    left: 0;
  }
}

.burger-btn {
  width: 40px;
  height: 40px;
  border: none;
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.burger-btn:hover {
  background: rgba(59, 130, 246, 0.1);
}

.burger-btn span {
  display: block;
  width: 24px;
  height: 2px;
  background: #333;
  transition: all 0.3s ease;
}

.burger-btn:hover span {
  background: #3b82f6;
}

.nav-links a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-links a:hover {
  color: #3b82f6;
  background: rgba(59, 130, 246, 0.1);
  box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: #3b82f6;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-links a:hover::after {
  width: 80%;
  box-shadow: 0 0 8px #3b82f6;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-right {
  margin-right: 20px;
}

.nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

/* Style spécifique pour le bouton déconnexion */
.nav-links a[href="/login"] {
  color: #333;
}

.nav-links a[href="/login"]:hover {
  color: #ef4444;
  background: rgba(239, 68, 68, 0.1);
  box-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
}

.nav-links a[href="/login"]::after {
  background: #ef4444;
}

.nav-links a[href="/login"]:hover::after {
  width: 80%;
  box-shadow: 0 0 8px #ef4444;
}


.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 150;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.overlay-active {
  opacity: 1;
  visibility: visible;
}
</style>