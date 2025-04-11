<template>
  <div class="recent-objects">
    <h1>Objets Récents</h1>
     <div class = "column-3"
        v-for ="objet in latestObjets"
        v-bind:key = "objet.id"> 
        <div class ="box">
          <figure class ="image mb-4">
            <img :src="objet.get_thumbnail">
          </figure>
          <h3 class ="is-size-4">{{objet.name}}</h3>
          <p class ="is-size-6-has-text-grey">{{objet.status }}</p>

          <router-link v-bind:to="objet.get_absolute_url" class="button is-dark mt-4"> Détails</router-link>
        </div>
     </div>
  </div>
</template>
  
<script>
import axios from 'axios'

export default {
  data() {
    return {
      latestObjets: []
    }
  },
  components: {
  },
  mounted() {
    this.getLastestProducts()
  },
  methods: {
    getLastestProducts(){
      axios
        .get('/api/v1/latest-objets/')
        .then(response => {
          this.latestObjets = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
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
  