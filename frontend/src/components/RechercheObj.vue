<template>
  <div class="recent-objects">
    <h1>Objets Récents</h1>
     <div class="column-3"
        v-for="objet in latestObjets"
        v-bind:key="objet.id"> 
        <div class="box">
          <figure class="image mb-4">
            <img :src="objet.get_thumbnail">
          </figure>
          <h3 class ="is-size-4">{{objet.name}}</h3>
          <p class ="is-size-6-has-text-grey">{{objet.status }}</p>
          <div class="action-buttons">
            <router-link v-bind:to="objet.get_absolute_url" class="button is-dark mt-4"><button>Détails</button> </router-link>  
            <router-link v-bind:to="`/gestion${objet.get_absolute_url}`" class="button is-warning mt-2 ml-2"><button>Modifier</button></router-link>
            <button @click="deleteObjet(objet.category_detail.slug, objet.slug)" class="button is-danger mt-2 ml-2">Supprimer</button>
          </div>
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
  components: {},
  mounted() {  
    if (!localStorage.getItem('token')) {
      this.$router.push('/login'); 
    } else {
      this.getLastestProducts(); 
    }
  },
  methods: {
    getLastestProducts() {
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
    },
    // Méthode pour générer le PDF avec l'ID de l'objet
    generatePDF(objectId) {
      axios
        .get(`/api/v1/objet/${objectId}/pdf/`, { responseType: 'blob' })
        .then(response => {
          // Créer un lien temporaire pour télécharger le PDF
          const blob = response.data;
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = `${objectId}.pdf`;  // Utilisation de l'ID dans le nom du fichier PDF
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        })
        .catch(error => {
          console.log(error);
          alert('Erreur lors de la génération du PDF');
        })
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

.box {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  margin: 1rem;
  transition: transform 0.3s ease;
}

.box:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.column-3 {
  display: inline-block;
  width: calc(33.333% - 2rem);
  vertical-align: top;
  margin: 1rem;
}

@media (max-width: 768px) {
  .column-3 {
    width: calc(50% - 2rem);
  }
}

@media (max-width: 480px) {
  .column-3 {
    width: calc(100% - 2rem);
  }
}
  
h1 {
  font-size: 2.5rem;
  color: #2563eb;
  margin-top: 3rem;
  text-align: center;
}
  
.action-buttons {
  display: flex;
  gap: 0.4rem;
  margin: 0.5rem 0;
  justify-content: center;
}

button {
  flex: 0 0 auto; /* Remove flex grow, allow natural width */
  text-align: center;
  padding: 0.875rem 1.5rem; /* Add horizontal padding */
  margin-top: 1rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap; /* Prevent text wrapping */
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
  
