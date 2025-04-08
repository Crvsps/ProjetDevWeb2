<template>
  <nav class="navbar">
    <ul class="nav-links">
      <li><router-link to="/">Accueil</router-link></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>

    <div class="nav-buttons">
      <router-link to="/create-account" class="btn btn-signup">Profil</router-link>
      <router-link to="/login" class="btn btn-login">Se déconnecter</router-link>
    </div>
  </nav>
</template>

<style scoped>
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
  padding: 0 2rem;
}

.nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
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

.nav-buttons {
  display: flex;
  gap: 1.2rem;
}

.btn {
  padding: 0.7rem 1.4rem;
  font-size: 0.9rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-signup {
  background: transparent;
  border: 2px solid #3b82f6;
  color: #3b82f6;
}

.btn-signup:hover {
  background: #3b82f6;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
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
  transform: translateY(0);
  box-shadow: none;
}
</style>