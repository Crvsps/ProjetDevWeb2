<template>
    <div class="page-add-product">
      <h1 class="title">Ajouter un objet</h1>
        
        <TestAuth/>  

      <div class="columns">
        <div class="column is-8">
          <form @submit.prevent="addObjet">
            <div class="field">
              <label class="label">Nom</label>
              <div class="control">
                <input v-model="newObjet.name" class="input" type="text" required />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <textarea v-model="newObjet.description" class="textarea"></textarea>
              </div>
            </div>
  
            <div class="field">
              <label class="label">Statut</label>
              <div class="control">
                <div class="select">
                  <select v-model="newObjet.status">
                    <option>Actif</option>
                    <option>Inactif</option>
                    <option>Maintenance</option>
                    <option>Hors-Service</option>
                    <option>Occupé</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="field">
            <label class="label">Catégorie</label>
                <div class="control">
                    <div class="select">
                    <select v-model="newObjet.category_slug" required>
                        <option v-for="category in categories" :key="category.id" :value="category.slug">
                        {{ category.name }}
                        </option>
                    </select>
                    </div>
                </div>
            </div>
  
            <div class="field">
              <label class="label">Marque</label>
              <div class="control">
                <input v-model="newObjet.marque" class="input" type="text" />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Consommation</label>
              <div class="control">
                <input v-model="newObjet.consommation" class="input" type="number" step="0.01" />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Localisation</label>
              <div class="control">
                <input v-model="newObjet.localisation" class="input" type="text" />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Dernière Maintenance</label>
              <div class="control">
                <input v-model="newObjet.derniere_maintenance" class="input" type="date" />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Image</label>
              <div class="control">
                <input type="file" @change="onImageChange" class="input" />
              </div>
            </div>

            
  
            <button type="submit" class="button is-primary mt-4">
              Ajouter l'objet
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>

<script>
import axios from "axios";
import TestAuth from "./TestAuth.vue";


export default {
  data() {
    return {
      newObjet: {
        name: "",
        description: "",
        status: "Actif",
        marque: "",
        consommation: 0,
        localisation: "",
        derniere_maintenance: "",
        image: null,
        category_slug:"",
      },
      imageFile: null,
      categories: []
    };
  },
  components: {
    TestAuth
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    getCategories() {
      axios
        .get("/api/v1/categories/") 
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.error("Erreur lors de la récupération des catégories", error);
        });
    },
    onImageChange(event) {
      this.imageFile = event.target.files[0];
    },

    addObjet() {
      const formData = new FormData();
      formData.append("name", this.newObjet.name);
      formData.append("description", this.newObjet.description);
      formData.append("status", this.newObjet.status);
      formData.append("marque", this.newObjet.marque);
      formData.append("consommation", this.newObjet.consommation);
      formData.append("localisation", this.newObjet.localisation);
      formData.append("derniere_maintenance", this.newObjet.derniere_maintenance);

      if (this.imageFile) {
        formData.append("image", this.imageFile);
      }

      axios
        .post("/api/v1/objets/add-objet/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          alert("Objet ajouté !");
        })
        .catch((err) => {
          console.log(err);
          alert("Erreur lors de l'ajout de l'objet");
        });
    },
  },
};
</script>