<template>
  <div class="profile container">
    <h2>Mon profil</h2>

    <div v-if="loading">Chargement...</div>
    <form v-else @submit.prevent="updateProfile">
      <div class="card">
        <div class="card-body">
          

          <div class="form-group">
            <label>Nom d'utilisateur</label>
            <input type="text" class="form-control" v-model="user.user.username" />
          </div>

          <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" v-model="user.user.email" />
          </div>

          <div class="form-group">
            <label>Prénom</label>
            <input type="text" class="form-control" v-model="user.first_name" />
          </div>

          <div class="form-group">
            <label>Nom</label>
            <input type="text" class="form-control" v-model="user.last_name" />
          </div>

          <div class="form-group">
            <label>Date de naissance</label>
            <input type="date" class="form-control" v-model="user.date_of_birth" />
          </div>

          <div class="form-group">
            <label>Genre</label>
            <select class="form-control" v-model="user.gender">
              <option value="Homme">Homme</option>
              <option value="Femme">Femme</option>
              <option value="Autre">Autre</option>
            </select>
          </div>

          <div class="form-group">
            <label>Type d'utilisateur</label>
            <select class="form-control" v-model="user.user_type">
              <option value="Élève">Élève</option>
              <option value="Professeur">Professeur</option>
              <option value="Administration">Administration</option>
              <option value="Parent">Parent</option>
              <option value="Maintenance">Maintenance</option>
            </select>
          </div>

          <p><strong>Points :</strong> {{ user.points }}</p>


          <button type="submit" class="btn btn-success mt-3">Sauvegarder</button>
        </div>
      </div>
    </form>

    <div v-if="error" class="alert alert-danger mt-3">
      {{ error }}
    </div>
    <div v-if="message" class="alert alert-success mt-3">
      {{ message }}
    </div>
  </div>
</template>

<script>
import UserService from '../services/user.service';

export default {
  name: 'UserProfile',
  data() {
    return {
      user: {
        user: {}
      },
      loading: true,
      error: null,
      message: '',
      previewPhoto: null,
    };
  },
  mounted() {
    this.fetchProfile();
  },
  methods: {
    fetchProfile() {
      this.loading = true;
      UserService.getUserProfile()
        .then((response) => {
          this.user = response.data;
          if (this.user.photo) {
            this.previewPhoto = this.user.photo;
          }
        })
        .catch(() => {
          this.error = 'Impossible de charger le profil.';
        })
        .finally(() => {
          this.loading = false;
        });
    },
    updateProfile() {
  const formData = new FormData();

  for (const key in this.user) {
    if (key !== 'user') {
      formData.append(key, this.user[key]);
    }
  }

  formData.append('user[id]', this.user.user.id);
  formData.append('user[username]', this.user.user.username);
  formData.append('user[email]', this.user.user.email);

  if (this.photoFile) {
    formData.append('photo', this.photoFile);
  } 

  for (let pair of formData.entries()) {
    console.log(pair[0] + ':', pair[1]);
  }

  UserService.updateUserProfile(formData)
    .then(() => {
      this.message = 'Profil mis à jour avec succès.';
      this.error = '';
    })
    .catch(() => {
      this.error = 'Erreur lors de la mise à jour.';
      this.message = '';
    });
},
    handlePhotoUpload(event) {
      const file = event.target.files[0];
      this.photoFile = file;
      this.previewPhoto = URL.createObjectURL(file);
}
  }
};
</script>

<style scoped>
.profile {
  max-width: 600px;
  margin: 0 auto;
}
.img-thumbnail {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
}
</style>
