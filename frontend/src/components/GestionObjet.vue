<template>
  <div class="form-page-container">
    <div class="form-container">
      <h2>Modifier l’objet</h2>

      <form @submit.prevent="updateObjet" class="account-form">
        <div class="form-group">
          <label for="name">Nom</label>
          <input v-model="objet.name" id="name" type="text" required placeholder="Nom de l'objet" />
        </div>

        <div class="form-group">
          <label for="description">Description</label>
          <textarea v-model="objet.description" id="description" rows="3" placeholder="Décrivez l'objet"></textarea>
        </div>

        <div class="form-group">
          <label for="status">Statut</label>
          <select v-model="objet.status" id="status">
            <option>Actif</option>
            <option>Inactif</option>
            <option>Maintenance</option>
            <option>Hors-Service</option>
            <option>Occupé</option>
          </select>
        </div>

        <div class="form-group">
          <label for="localisation">Localisation</label>
          <input v-model="objet.localisation" id="localisation" type="text" placeholder="Lieu de l'objet" />
        </div>

        <div class="form-group">
          <label for="consommation">Consommation en kWh</label>
          <input v-model="objet.consommation" id="consommation" type="number" step="0.01" />
        </div>

        <div class="form-group">
          <label for="maintenance">Dernière maintenance</label>
          <input v-model="objet.derniere_maintenance" id="maintenance" type="date" />
        </div>

        <div class="form-group">
          <label for="image">Image</label>
          <input type="file" @change="onImageChange" id="image" />
        </div>

        <div class="form-group" v-if="objet.image">
          <label class="checkbox">
            <input type="checkbox" v-model="supprimerImage" />
            Supprimer l'image actuelle
          </label>
        </div>

        <button type="submit" class="btn-submit">Enregistrer les modifications</button>
      </form>
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
  
<style scoped>
.form-page-container {
  width: 100%;
  min-height: 100vh;
  padding-top: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-container {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
              0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

h2 {
  color: #1e293b;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.875rem;
  font-weight: 600;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #475569;
  font-weight: 500;
  font-size: 0.95rem;
}

input,
textarea,
select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #f8fafc;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  background: white;
}

input::placeholder,
textarea::placeholder {
  color: #94a3b8;
}

.btn-submit {
  width: 100%;
  padding: 0.875rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.checkbox {
  font-size: 0.95rem;
  color: #475569;
}
</style>