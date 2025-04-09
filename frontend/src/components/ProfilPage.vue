<template>
  <div class="profile-container">
    <div class="profile-header">
      <img :src="user.photo" alt="Photo de profil" class="profile-photo"/>
      <h1>{{ user.name }}</h1>
      <p>{{ user.email }}</p>
    </div>
    
    <div class="profile-edit">
      <h2>Modifier le profil</h2>
      <form @submit.prevent="updateProfile" class="account-form">
        <div class="form-group">
          <label for="name">Nom</label>
          <input type="text" v-model="updatedUser.name" id="name" placeholder="Nom"/>
        </div>
		
		<div class="form-group">
          <label for="FName">Prénom</label>
          <input type="text" v-model="updatedUser.fName" id="fName" placeholder="Prénom"/>
        </div>


        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="updatedUser.email" id="email" placeholder="Votre email"/>
        </div>

        <div class="form-group">
          <label for="photo">Photo de profil</label>
          <input type="file" @change="onFileChange" id="photo"/>
        </div>

        <button type="submit" class="btn-submit">Mettre à jour</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

const newName = ref('')
const newFName= ref('')
const newPhoto = ref('')
const newEmail = ref('')

export default {
  data() {
    return {
      user: {
        name: '',
		fName: '',
        email: '',
        photo: ''
      },
      updatedUser: {
        name: newName,
		fName : newFName,
        email: newEmail,
        photo: newPhoto
      }
    };
  },
  methods: {
    updateProfile() {
      // Logic for updating user profile
      this.user = { ...this.updatedUser };
      alert('Profil mis à jour !');
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.updatedUser.photo = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    }
  }
};
</script>

<style scoped>
.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f8fafc;
  padding: 20px;
}

.profile-header {
  text-align: center;
  margin-bottom: 20px;
}

.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #e2e8f0;
}

.profile-edit {
  max-width: 500px;
  width: 100%;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
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

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #f8fafc;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  background: white;
}

input::placeholder {
  color: #94a3b8;
}

.btn-submit {
  width: 100%;
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

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-submit:active {
  transform: translateY(0);
}

@media (max-width: 640px) {
  .profile-container {
    padding: 1rem;
  }
  
  .profile-edit {
    padding: 1.5rem;
  }
}
</style>
