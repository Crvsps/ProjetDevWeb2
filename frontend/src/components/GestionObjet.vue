<template>
    <div class="page-product">
      <h1 class="title">Modifier l’objet</h1>
  
      <div class="columns">
        <div class="column is-8">
          <form @submit.prevent="updateObjet">
            <div class="field">
              <label class="label">Nom</label>
              <div class="control">
                <input v-model="objet.name" class="input" type="text" required />
              </div>
            </div>
  
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <textarea v-model="objet.description" class="textarea"></textarea>
              </div>
            </div>
  
            <div class="field">
              <label class="label">Statut</label>
              <div class="control">
                <div class="select">
                  <select v-model="objet.status">
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
            <label class="label">Localisation</label>
            <div class="control">
              <input v-model="objet.localisation" class="input" type="text" />
            </div>
          </div>

          <div class="field">
            <label class="label">Consommation en kWh</label>
            <div class="control">
              <input v-model="objet.consommation" class="input" type="text" />
            </div>
          </div>

          <div class="field">
            <label class="label">Dernière maintenance</label>
            <div class="control">
              <input v-model="objet.derniere_maintenance" class="input" type="date" />
            </div>
          </div>

            <div class="field">
                <label class="label">Image</label>
                <div class="control">
                    <input type="file" @change="onImageChange" class="input" />
                </div>
            </div>

            <div class="field mt-2" v-if="objet.image">
              <label class="checkbox">
                <input type="checkbox" v-model="supprimerImage" />
                Supprimer l'image actuelle
              </label>
            </div>
            
            <button type="submit" class="button is-primary mt-4">
              Enregistrer les modifications
            </button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'GestionObjet',
    data() {
      return {
        objet: {},
        imageFile : null,
        supprimerImage : false,
      }
    },
    mounted() {
      this.getObjet()
    },
    methods: {
      getObjet() {
        const { category_slug, object_slug } = this.$route.params
  
        axios
          .get(`/api/v1/objets/${category_slug}/${object_slug}`)
          .then((res) => {
            this.objet = res.data
          })
          .catch((err) => console.log(err))
      },

      onImageChange(event) {
        this.imageFile = event.target.files[0];  
    },
  
      updateObjet() {
        const { category_slug, object_slug } = this.$route.params

        const formData = new FormData()
      formData.append('name', this.objet.name)
      formData.append('description', this.objet.description)
      formData.append('status', this.objet.status)
      formData.append('category', this.objet.category)
      formData.append('localisation', this.objet.localisation)
      formData.append('consommation', this.objet.consommation)
      formData.append('derniere_maintenance', this.objet.derniere_maintenance)


        if (this.imageFile) {
            formData.append('image' , this.imageFile)
        }

        if (this.supprimerImage) {
            formData.append('supprimer_image', 'true')
        }
  
        axios
          .put(`/api/v1/objets/${category_slug}/${object_slug}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
          })
          .then((response) => {
            alert('Objet mis à jour !')
            const newSlug = response.data.slug
            this.$router.push(`/${category_slug}/${newSlug}`)
          })
          .catch((err) => {
            console.log(err)
            alert("Erreur lors de la mise à jour")
          })
      }
    }
  }
  </script>
  