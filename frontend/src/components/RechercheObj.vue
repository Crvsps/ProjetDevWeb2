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
          <h3 class="is-size-4">{{ objet.name }}</h3>
          <p class="is-size-6-has-text-grey">{{ objet.status }}</p>

          <router-link v-bind:to="objet.get_absolute_url" class="button is-dark mt-4">
            <button>Détails</button> 
          </router-link>

          <router-link v-bind:to="`/gestion${objet.get_absolute_url}`" class="button is-warning mt-2 ml-2">
            <button>Modifier</button>
          </router-link>

          <button @click="deleteObjet(objet.category_detail.slug, objet.slug)" class="button is-danger mt-2 ml-2">
            Supprimer
          </button>

          <!-- Nouveau bouton pour générer le PDF avec ID de l'objet -->
          <button @click="generatePDF(objet.id)" class="button is-info mt-2 ml-2">
            Générer PDF
          </button>
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
