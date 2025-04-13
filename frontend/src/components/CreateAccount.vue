<template>
  <div class="register">
    <h2>Inscription</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Nom d'utilisateur</label>
        <input
          type="text"
          id="username"
          v-model="user.username"
          required
        />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          v-model="user.email"
          required
        />
      </div>
      <div class="form-group">
        <label for="first_name">Prénom</label>
        <input
          type="text"
          id="first_name"
          v-model="user.first_name"
          required
        />
      </div>
      <div class="form-group">
        <label for="last_name">Nom de famille</label>
        <input
          type="text"
          id="last_name"
          v-model="user.last_name"
          required
        />
      </div>

      <!-- 
      <div class="form-group">
        <label for="date_of_birth">Date de naissance</label>
        <input
          type="date"
          id="date_of_birth"
          v-model="user.date_of_birth"
          required
        />
      </div>
      

      <div class="form-group">
        <label for="gender">Genre</label>
        <select
          id="gender"
          v-model="user.gender"
          required
        >
          <option value="">Sélectionner</option>
          <option value="male">Homme</option>
          <option value="female">Femme</option>
          <option value="other">Autre</option>
        </select>
      </div>

    

      <div class="form-group">
        <label for="user_type">Type d'utilisateur</label>
        <select
          id="user_type"
          v-model="user.user_type"
          required
        >
          <option value="">Sélectionner</option>
          <option value="Élève">Élève</option>
          <option value="Professeur">Professeur</option>      
          <option value="Administrateur">Administrateur</option>         
          <option value="Parent">Parent</option>      
          <option value="Maintenance">Maintenance</option>
        </select>
      </div>

      

      <div class="form-group">
        <label for="photo">Photo de profil</label>
        <input
          type="file"
          id="photo"
          @change="handleFileUpload"
        />
      </div>

      -->

      <div class="form-group">
        <label for="password">Mot de passe</label>
        <input
          type="password"
          id="password"
          v-model="user.password"
          required
        />
      </div>
      <div class="form-group">
        <label for="password2">Confirmer le mot de passe</label>
        <input
          type="password"
          id="password2"
          v-model="user.password2"
          required
        />
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="loading">
          <span v-if="loading">Chargement...</span>
          <span v-else>S'inscrire</span>
        </button>
      </div>
      <div v-if="message" class="alert" :class="successful ? 'alert-success' : 'alert-danger'">
        {{ message }}
      </div>
    </form>
  </div>
</template>

<script>
import UserService from '../services/user.service';

export default {
  name: 'CreateAccount',
  data() {
    return {
      user: {
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        date_of_birth: '',
        gender: '',
        user_type: '',
        photo: null,  
        points: 0,
        password: '',
        password2: '',  
      },
      loading: false,
      message: '',
      successful: false
    };
  },
  methods: {
    handleRegister() {
      this.message = '';
      this.loading = true;

      UserService.register(this.user)
        .then(response => {
          this.message = 'Inscription réussie!';
          this.successful = true;
          this.$router.push('/login');
        })
        .catch(error => {
          this.message = error.response?.data?.username || 
                         error.response?.data?.email || 
                         error.response?.data?.password ||
                         'Une erreur s\'est produite!';
          this.successful = false;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.user.photo = file;
      }
    }
  }
};
</script>
