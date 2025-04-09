<template>
    <div class="search-container">
      <h2>Rechercher des produits</h2>
  
      <!-- Formulaire de recherche avec filtres -->
      <form @submit.prevent="handleSearch">
        <div class="form-group">
          <label for="name">Nom</label>
          <input 
            id="name" 
            type="text" 
            v-model="filters.name" 
            placeholder="Nom du produit"
          />
        </div>
  
        <div class="form-group">
          <label for="category">Catégorie</label>
          <input 
            id="category" 
            type="text" 
            v-model="filters.category" 
            placeholder="Catégorie"
          />
        </div>
  
        <div class="form-group">
          <label for="price_min">Prix Min</label>
          <input 
            id="price_min" 
            type="number" 
            v-model="filters.price_min" 
            placeholder="Prix minimum"
          />
        </div>
  
        <div class="form-group">
          <label for="price_max">Prix Max</label>
          <input 
            id="price_max" 
            type="number" 
            v-model="filters.price_max" 
            placeholder="Prix maximum"
          />
        </div>
  
        <button type="submit">Rechercher</button>
      </form>
  
      <!-- Résultats de la recherche -->
      <div v-if="objets.length">
        <h3>Résultats :</h3>
        <ul>
          <li v-for="objet in objets" :key="objet.id">
            <h4>{{ objet.name }}</h4>
            <p>{{ objet.description }}</p>
            <p><strong>Prix:</strong> {{ objet.price }} €</p>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>Aucun produit trouvé.</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const filters = ref({
    name: '',
    category: '',
    price_min: '',
    price_max: ''
  })
  
  const objets = ref([])
  
  const handleSearch = async () => {
    const response = await fetch('http://127.0.0.1:8000/objets/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      params: filters.value // Les filtres seront envoyés en paramètres GET
    })
  
    if (response.ok) {
      objets.value = await response.json()
    } else {
      alert('Erreur lors de la recherche')
    }
  }
  </script>
  
  <style scoped>
  /* Styles pour la page de recherche */
  .search-container {
    padding: 2rem;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  label {
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 0.75rem;
    margin-top: 0.5rem;
  }
  
  button {
    padding: 0.75rem 1.5rem;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  ul {
    list-style-type: none;
    padding-left: 0;
  }
  
  li {
    margin-bottom: 1rem;
  }
  </style>
  