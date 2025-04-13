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


<style scoped>
.register {
  max-width: 400px;
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
  box-sizing: border-box;
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.alert {
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}

.alert-danger {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.photo-preview {
  margin-top: 1rem;
  text-align: center;
}

.photo-preview img {
  max-width: 150px;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

@media (max-width: 480px) {
  .register {
    margin: 1rem;
    padding: 1.5rem;
  }
}
</style>