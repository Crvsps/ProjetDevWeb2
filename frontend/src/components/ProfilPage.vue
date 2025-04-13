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
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #2563eb;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.8rem;
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
}

.img-thumbnail {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #3b82f6;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #4b5563;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  outline: none;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

input[type="file"] {
  padding: 0.5rem;
  border: 2px dashed #e5e7eb;
  background: #f9fafb;
  cursor: pointer;
}

input[type="file"]:hover {
  border-color: #3b82f6;
  background: #f3f4f6;
}

.btn {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1rem;
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.btn-danger {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: white;
}

.btn-danger:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
}

.alert {
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}

.alert-success {
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
  border: 1px solid rgba(34, 197, 94, 0.2);
}

.alert-danger {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

@media (max-width: 640px) {
  .profile {
    margin: 1rem;
    padding: 1.5rem;
  }
}
</style>