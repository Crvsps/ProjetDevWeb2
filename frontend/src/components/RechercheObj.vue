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

          <router-link v-bind:to="objet.get_absolute_url" class="button is-dark mt-4"><button>Détails</button> </router-link>
          <router-link v-bind:to="`/gestion${objet.get_absolute_url}`" class="button is-warning mt-2 ml-2"><button>Modifier</button></router-link>
          <button @click="deleteObjet(objet.category_detail.slug, objet.slug)" class="button is-danger mt-2 ml-2">Supprimer</button>
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
    console.log(localStorage.getItem('token'))
      if (!localStorage.getItem('token')) {
        this.$router.push('/login'); 
      } else {
        this.getLastestProducts(); 
  
}

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
       },
       deleteObjet(categorySlug, objectSlug) {
      if (confirm('Êtes-vous sûr de vouloir supprimer cet objet ?')) {
        axios
          .delete(`/api/v1/objets/${categorySlug}/${objectSlug}/delete/`)
          .then(response => {
            this.latestObjets = this.latestObjets.filter(objet => objet.slug !== objectSlug)
            alert('Objet supprimé avec succès')
          })
          .catch(error => {
            console.log(error)
            alert('Erreur lors de la suppression de l\'objet')
          })
      }
    }
  }
}
</script>
  
  <style scoped>
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
  
button:hover {
 transform: translateY(-2px);
 box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}
  
ul {
 list-style-type: none;
 padding-left: 0;
}
  
li {
 margin-bottom: 1rem;
}
</style>
  