// Renommer Home.vue en HomePage.vue
<script lang="ts">
export default {
  name: 'HomePage'
}

</script>

<template>
  
  <div class="home-content">
      <!-- Welcome Section -->
      <section class="welcome-section">
        <h1>Bienvenue sur CYber School</h1>
        <p>La plateforme de gestion intelligente des objets connectés de votre école</p>
      </section>

      <!-- Features Grid -->
      <section class="features">
        <div class="features-grid">
          <div class="feature-card">
            <i class="fas fa-database"></i>
            <h3>Gestion Centralisée</h3>
            <p>Tous vos objets connectés au même endroit</p>
          </div>
          <div class="feature-card">
            <i class="fas fa-chart-bar"></i>
            <h3>Statistiques</h3>
            <p>Suivez l'utilisation en temps réel</p>
          </div>
          <div class="feature-card">
            <i class="fas fa-user-shield"></i>
            <h3>Sécurité</h3>
            <p>Accès sécurisé aux données</p>
          </div>
        </div>
      </section>

      <!-- Stats Section -->
      <section class="stats-section">
        <div class="stat-card">
          <h2>200+</h2>
          <p>Objets Connectés</p>
        </div>
        <div class="stat-card">
          <h2>1000+</h2>
          <p>Utilisateurs</p>
        </div>
        <div class="stat-card">
          <h2>24/7</h2>
          <p>Disponibilité</p>
        </div>
      </section>
    </div>
    <div class="home">
    <div class="image-container">
      <img src="../assets/image1.jpg" alt="Image 1" class="home-image">
      <img src="../assets/image2.png" alt="Image 2" class="home-image">
      <img src="../assets/image3.jpg" alt="Image 3" class="home-image">
    </div>
  </div>
</template>

<style scoped>
.home {
  padding-top: 80px; /* Pour éviter que le contenu soit caché derrière la navbar */
  min-height: 100vh;
  background: #f8fafc;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 2rem;
  flex-wrap: wrap;
}

.home-image {
  max-width: 300px;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.home-image:hover {
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .image-container {
    flex-direction: column;
  }
  
  .home-image {
    width: 100%;
    max-width: 400px;
  }
}


.home-content {
  padding-top: 80px; /* Account for fixed navbar */
}

.welcome-section {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
}

.welcome-section h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.features {
  padding: 4rem 2rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card i {
  font-size: 2rem;
  color: #3b82f6;
  margin-bottom: 1rem;
}

.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  padding: 4rem 2rem;
  background: #f8fafc;
  text-align: center;
}

.stat-card {
  padding: 2rem;
}

.stat-card h2 {
  font-size: 2.5rem;
  color: #3b82f6;
  margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
  .welcome-section h1 {
    font-size: 2rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .stats-section {
    grid-template-columns: 1fr;
  }
}
</style>