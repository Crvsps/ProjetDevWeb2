// Renommer Home.vue en HomePage.vue
<script lang="ts">
export default {
  name: 'HomePage'
}

</script>

<template>
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
</style>